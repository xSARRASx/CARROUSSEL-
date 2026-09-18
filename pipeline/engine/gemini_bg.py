#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gemini_bg.py -- Generation AUTOMATIQUE des photos de fond (Nano Banana Pro).

Contexte (decouvert le 27/07/2026) :
  Seedance ne permet PAS de generer des images par API (401 sur les routes image,
  seule la video est exposee), et le navigateur est bloque par le proxy de cet
  environnement. Or "Nano Banana Pro" est un modele GOOGLE que Seedance revend.
  -> On appelle Google directement : meme modele, meme qualite, 100% automatique.

Cout (tarifs officiels Google, releves le 27/07/2026) :
  gemini-3-pro-image (Nano Banana Pro) : 0,134 $ par image 1K/2K, 0,24 $ en 4K.
  Pas de palier gratuit. Environ 1 $/mois pour 8 fonds de carrousels.

SECRET : la cle vient UNIQUEMENT de la variable d'environnement GEMINI_API_KEY.
Jamais dans le code (repo public).

Usage :
    # Voir le prompt et la requete SANS rien depenser :
    python3 gemini_bg.py --brand lesousloueur --theme "controle fiscal" --dry-run

    # Generer pour de vrai (coute ~0,134 $) :
    python3 gemini_bg.py --brand lesousloueur --theme "..." --out mon_fond.jpg --go

Depuis un script de carrousel :
    from gemini_bg import generate_background
    generate_background("lesousloueur", "le controle fiscal", "v2_xxx_bg.jpg")
"""

import argparse
import base64
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
BG_DIR = ROOT / "assets" / "backgrounds"

BASE = "https://generativelanguage.googleapis.com"
MODEL = "gemini-3-pro-image"          # Nano Banana Pro

# Cascade de secours (constatee le 17/08/2026) : Google a renvoye pendant plus
# d'une heure "gemini-3-pro-image is currently experiencing high demand" sur les
# DEUX routes. 12 relances espacees de 2 minutes n'ont rien donne. La variante
# -preview etait saturee de la meme facon, mais gemini-3.1-flash-image est passee
# du premier coup, avec un rendu conforme aux regles de la PARTIE D.
# -> On essaie les modeles dans cet ordre plutot que d'echouer. Le robot du lundi
#    et celui du jeudi doivent pouvoir se debrouiller seuls.
MODELS = (
    "gemini-3-pro-image",             # Nano Banana Pro, le choix par defaut
    "gemini-3-pro-image-preview",     # meme famille, parfois moins saturee
    "gemini-3.1-flash-image",         # secours valide en conditions reelles
    "gemini-2.5-flash-image",         # dernier filet
)

ASPECT = "4:5"                        # format des slides
SIZE = "2K"                           # 1K / 2K / 4K (2K = bon compromis prix/qualite)

# --------------------------------------------------------------------------
# Prompts de fond par marque (regles PARTIE D du carroussel.md).
# Le THEME de la semaine est injecte pour coller au sujet du carrousel.
# --------------------------------------------------------------------------

COMMON_RULES = """
LAYOUT (STRICT VERTICAL 4:5, THINK 1080 x 1350)
- TOP 38%: almost EMPTY surface, only subtle texture and gentle light falloff.
  A large title will be placed over this zone, so it must stay clean and calm.
- BOTTOM 62%: the objects, arranged with generous breathing room, never crowded.
- Comfortable margins left and right, no object awkwardly cropped.
- CRITICAL: the empty top zone and the scene below must join through a SMOOTH
  CONTINUOUS gradient. NO horizontal seam, NO visible band, NO straight line
  across the frame, NO split between two different backgrounds.

ABSOLUTE EXCLUSIONS
- NO readable text, NO letters, NO numbers, NO typography anywhere.
  Papers, folders, screens and notes are completely BLANK.
- NO logos, NO brand marks. DO NOT draw any logo from memory.
- NO people, NO hands, NO body parts.
- NO screens turned on, NO user interface, NO app icons, NO charts.
- NO visible light rays, NO halos, NO light beams, NO light shafts.
- NO HDR over-processing, NO exaggerated contrast, NO oversaturation.
- NO artificial AI rendering look, NO cheap plastic 3D look.
- NO emoji, NO watermark, NO duplicate objects, NO browser frame.

RENDERING
- Photorealistic photography, natural fine film grain, subtle.
- Shot on Sony A7, sharp focus on the objects, calm and premium color grading.
"""

# ==========================================================================
# 🚨 CONSTAT DE MARTIN (18/09/2026), le deuxieme sur le meme sujet :
#    « les fonds des carrousels c'est de la merde, ils sont tous pareils ».
#    Il avait raison, et la cause etait ICI. Le 02/09 j'avais degele la liste
#    des OBJETS, mais le reste du prompt restait fige : Le Sous Loueur, c'etait
#    TOUJOURS un flat-lay vu du dessus sur fond navy, et Guestlucky TOUJOURS un
#    bureau de nuit en trois quarts. Changer les objets d'une photo dont le
#    cadrage, le decor et la lumiere ne bougent jamais ne change rien.
#    -> Desormais le prompt se COMPOSE : une scene (cadrage + decor + lumiere)
#       tiree d'une banque de 14 par marque, un theme (sombre ou clair), et des
#       objets ecrits d'apres la transcription de la semaine. La rotation est
#       tenue par output/fonds.json : jamais la meme scene qu'aux DEUX
#       dernieres semaines, jamais la meme sur les deux marques le meme jour.
# ==========================================================================

PALETTES = {
    ("lesousloueur", "sombre"): """- Dominant: deep navy blue #0E1B2E and #142841 for surfaces and shadows
- Accent: warm vibrant orange #E8551F to #F25C2A, maximum three small touches
- Secondary: white #FFFFFF for papers, warm cream #F5F5EE, natural kraft brown
- NO violet, NO purple, NO magenta, NO pink, NO green anywhere""",
    ("lesousloueur", "clair"): """- Dominant: warm off-white and cream #F6F3EE to #FFFFFF, pale sand, light kraft
- Accent: warm vibrant orange #E8551F, maximum two small touches
- Secondary: deep navy blue #0E1B2E for the darkest objects only
- Bright, airy, high-key image: the whole frame stays LIGHT
- NO violet, NO purple, NO magenta, NO pink, NO green anywhere""",
    ("guestlucky", "sombre"): """- Base: very deep navy blue #0F1A35 and #0A1228, close to black in the corners
- Primary glow: violet #7B4FE0 and #8B3FD9, coming from off-frame
- Secondary glow: magenta pink #E84A8C and #C13FBE, softer
- White #FFFFFF only for blank papers and faint edge highlights
- NO orange, NO yellow, NO green, NO teal, NO red anywhere""",
    ("guestlucky", "clair"): """- Base: clean white and very pale lilac #F4F1FA to #FFFFFF
- Accent: violet #7B4FE0 and magenta pink #E84A8C, as coloured light or as
  one or two coloured objects, never as a heavy wash
- Soft grey #E7E4EF for shadows, which stay light and open
- Bright, airy, high-key image: the whole frame stays LIGHT
- NO orange, NO yellow, NO green, NO teal, NO red anywhere""",
}

# Chaque scene : (cadrage, decor, lumiere). Le theme dit si l'image sort claire
# ou sombre : il doit correspondre au theme du carrousel (voile blanc ou navy).
SCENES = {
    "lesousloueur": {
        "flatlay_navy": ("sombre", "Top-down flat-lay, camera straight above",
                         "a deep navy blue matte paper surface",
                         "soft directional daylight from the upper left, gentle shadows"),
        "bureau_chene": ("sombre", "Three-quarter view of a desk corner, slightly elevated",
                         "a warm solid oak desk with visible grain",
                         "low late-afternoon sun, long soft shadows across the wood"),
        "beton_soleil": ("sombre", "High angle, objects gathered on the floor",
                         "a raw grey concrete floor with fine texture",
                         "hard directional sunlight, graphic geometric shadows"),
        "nuit_lampe": ("sombre", "Three-quarter close-up",
                       "a dark wooden table at night",
                       "a single warm desk lamp pooling light on the objects, deep shadows around"),
        "table_bistrot": ("sombre", "Low angle across the table edge, shallow depth of field",
                          "a dark walnut bistro table",
                          "soft window light from the side, moody falloff"),
        "escalier": ("sombre", "Slightly high angle, objects placed on a step",
                     "a worn stone step in an old Parisian stairwell, wrought iron rail blurred behind",
                     "natural shade with a soft glow from a distant window"),
        "ardoise": ("sombre", "Tight top-down crop, only two or three objects",
                    "a black slate board with matte texture",
                    "a single hard light source, crisp shadow edges"),
        "marbre_clair": ("clair", "Top-down flat-lay, camera straight above",
                         "a white marble slab with subtle grey veining",
                         "bright diffuse daylight, very soft shadows"),
        "lin_macro": ("clair", "Extreme close-up, shallow depth of field",
                      "a natural undyed linen cloth with visible weave",
                      "soft window light, quiet and even"),
        "appartement": ("clair", "Wide interior shot, objects on the floor in the lower third",
                        "the empty corner of a bright apartment with pale parquet and white walls",
                        "golden hour light coming through an off-frame window"),
        "rebord_fenetre": ("clair", "Eye-level close-up on a window sill",
                           "a painted wooden window sill, blurred rooftops outside",
                           "backlit daylight, soft haze, bright and airy"),
        "kraft_studio": ("clair", "Top-down flat-lay with generous spacing",
                         "a large sheet of natural kraft paper",
                         "even studio softbox light, neutral and clean"),
        "terrazzo": ("clair", "Top-down, objects arranged off-centre",
                     "a pale terrazzo surface with tiny warm flecks",
                     "bright even daylight, minimal shadows"),
        "drap": ("clair", "Three-quarter close-up, soft focus falloff",
                 "a rumpled white cotton bed sheet",
                 "early morning light, gentle and diffuse"),
    },
    "guestlucky": {
        "bureau_nuit": ("sombre", "Three-quarter view, slightly elevated",
                        "a modern ordered desk at night",
                        "ambient LED glow from off-frame sources, blending into darkness"),
        "verre_reflets": ("sombre", "Low three-quarter angle with visible reflections",
                          "a black glass sheet over a dark ground",
                          "violet and magenta reflections from off-frame panels"),
        "velours_macro": ("sombre", "Extreme close-up, very shallow depth of field",
                          "deep violet velvet fabric",
                          "a single soft light grazing the surface"),
        "beton_neon": ("sombre", "High angle, objects gathered together",
                       "dark polished concrete",
                       "a thin violet LED strip off-frame, its glow spilling across the floor"),
        "table_noire": ("sombre", "Straight top-down, dramatic and graphic",
                        "a matte black table surface",
                        "one hard light source, a magenta rim on the object edges"),
        "fenetre_soir": ("sombre", "Eye-level close-up near a window",
                         "a dark sill with a dim interior behind",
                         "cool blue-hour daylight with a faint violet cast"),
        "etagere": ("sombre", "Three-quarter view of a shelf, objects staged on it",
                    "a dark wooden shelf against a deep navy wall",
                    "a soft violet glow behind, deep shadows in front"),
        "studio_blanc": ("clair", "Three-quarter view on a seamless backdrop",
                         "a bright white studio sweep with a subtle violet gradient",
                         "high-key soft light, open airy shadows"),
        "papier_lilas": ("clair", "Top-down flat-lay, generous spacing",
                         "a pale lilac paper surface",
                         "even bright light, barely any shadow"),
        "gris_perle": ("clair", "Three-quarter close-up",
                       "a light pearl grey seamless surface",
                       "soft diffuse light with a violet rim from the right"),
        "plexi_rose": ("clair", "Top-down on a translucent sheet",
                       "a pale pink translucent acrylic sheet",
                       "diffuse backlight glowing through the material"),
        "marbre_violet": ("clair", "Top-down flat-lay",
                          "a white marble surface",
                          "daylight with a soft violet gel light from one side"),
        "tissu_gris": ("clair", "Extreme close-up, shallow depth of field",
                       "light grey wool fabric with visible texture",
                       "soft window light with a faint magenta bounce"),
        "ombres_stores": ("clair", "Top-down on paper, graphic shadow stripes",
                          "a plain white paper surface",
                          "hard sunlight through a window blind, the shadows tinted violet"),
    },
}

GABARIT = """═══════════════════════════════════════════════════════
PREMIUM EDITORIAL PHOTOGRAPH, STRICT VERTICAL 4:5
THEME: {theme}
═══════════════════════════════════════════════════════

FRAMING
{cadrage}.

SETTING
The scene takes place on {decor}, in the context of: {theme}.
{mood}

LIGHTING
{lumiere}.

OBJECTS (lower two thirds only)
{objects}

COLOR PALETTE (STRICT, DO NOT DEVIATE)
{palette}
"""

MOODS = {
    "lesousloueur": "Premium hospitality magazine mood (Kinfolk, Monocle, Conde Nast "
                    "Traveler): a serious short-term rental professional, organised and calm.",
    "guestlucky": "High-end SaaS brand mood (Stripe, Linear, Notion): precise, modern, "
                  "quietly technical.",
}

DEFAULT_OBJECTS = (
    "- CHOOSE 4 to 6 objects that LITERALLY illustrate the theme above.\n"
    "  They must be recognisable as belonging to THAT subject, not to a\n"
    "  generic desk. A viewer who sees only the photo should be able to\n"
    "  guess what the carousel talks about.\n"
    "- Keep every printed surface BLANK: no readable text, no logo,\n"
    "  no numbers, no user interface on any screen."
)

JOURNAL_FONDS = ROOT / "output" / "fonds.json"


def _journal_fonds():
    if JOURNAL_FONDS.is_file():
        try:
            return json.loads(JOURNAL_FONDS.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return {}


def scenes_possibles(marque, theme=None, deja_prise=None):
    """Les scenes utilisables cette semaine pour une marque, de la plus a la
    moins souhaitable. On ecarte les DEUX dernieres scenes de la marque et
    celle que l'autre marque vient de prendre. theme filtre clair / sombre."""
    if marque not in SCENES:
        raise ValueError("Marque inconnue : " + marque)
    passees = _journal_fonds().get(marque, [])[-2:]
    interdits = set(passees) | {deja_prise}
    libres = [n for n, sc in SCENES[marque].items()
              if n not in interdits and (theme is None or sc[0] == theme)]
    if libres:
        return libres
    return [n for n, sc in SCENES[marque].items() if theme is None or sc[0] == theme]


def noter_scene(marque, nom):
    """A appeler apres la generation, pour que la semaine suivante l'evite."""
    assert nom in SCENES[marque], "scene inconnue : %s" % nom
    j = _journal_fonds()
    j.setdefault(marque, []).append(nom)
    j[marque] = j[marque][-6:]
    JOURNAL_FONDS.parent.mkdir(parents=True, exist_ok=True)
    JOURNAL_FONDS.write_text(json.dumps(j, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
    return nom


def build_prompt(brand, theme, objects=None, scene=None):
    """Compose le prompt image de la semaine : marque + scene + sujet + objets."""
    if brand not in SCENES:
        raise ValueError("Marque inconnue : " + brand)
    if scene is None:
        scene = scenes_possibles(brand)[0]
    if scene not in SCENES[brand]:
        raise ValueError("Scene inconnue pour %s : %s" % (brand, scene))
    ton, cadrage, decor, lumiere = SCENES[brand][scene]
    return (GABARIT.format(theme=theme, cadrage=cadrage, decor=decor, lumiere=lumiere,
                           mood=MOODS[brand], objects=objects or DEFAULT_OBJECTS,
                           palette=PALETTES[(brand, ton)]).strip()
            + "\n" + COMMON_RULES)


def theme_de_la_scene(brand, scene):
    """clair ou sombre : le carrousel doit utiliser le MEME theme."""
    return SCENES[brand][scene][0]


def _key():
    k = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not k:
        raise RuntimeError(
            "GEMINI_API_KEY absente. Ajoute-la dans les variables d'environnement "
            "de l'environnement cloud (jamais dans le code).")
    return k


def _post(url, payload):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": _key()},
        method="POST")
    # 180 s ne suffisait pas quand les serveurs Google sont charges : on a vu des
    # TimeoutError alors que l'image etait peut-etre deja facturee. On attend
    # donc largement plutot que de risquer de repayer une generation.
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read().decode("utf-8"))


def _find_image_b64(obj):
    """Cherche la 1re image encodee en base64 n'importe ou dans la reponse."""
    if isinstance(obj, dict):
        # formes connues : {"inlineData":{"data":...}} / {"inline_data":{...}}
        for key in ("inlineData", "inline_data"):
            d = obj.get(key)
            if isinstance(d, dict) and d.get("data"):
                return d["data"]
        # forme "interactions" : {"type":"image","data":"..."} ou {"image":{"data":...}}
        if obj.get("type") == "image" and isinstance(obj.get("data"), str):
            return obj["data"]
        for v in obj.values():
            found = _find_image_b64(v)
            if found:
                return found
    elif isinstance(obj, list):
        for v in obj:
            found = _find_image_b64(v)
            if found:
                return found
    return None


def _payloads(prompt, aspect, size, modele):
    """Deux formes de requete : la nouvelle (interactions) puis l'ancienne
    (generateContent). On essaie la 1re, on bascule sur la 2e si refusee."""
    new_style = (BASE + "/v1beta/interactions", {
        "model": modele,
        "input": [{"type": "text", "text": prompt}],
        "response_format": {"type": "image", "mime_type": "image/jpeg",
                            "aspect_ratio": aspect, "image_size": size},
    })
    old_style = (BASE + "/v1beta/models/" + modele + ":generateContent", {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect, "imageSize": size},
        },
    })
    return [new_style, old_style]


def generate_background(brand, theme, out_name, objects=None, scene=None,
                        aspect=ASPECT, size=SIZE, modeles=None):
    """Genere la photo de fond et l'enregistre dans assets/backgrounds/.
    Renvoie (chemin, prompt_utilise). ATTENTION : consomme du credit Google.

    Essaie les modeles de la cascade MODELS dans l'ordre : un modele sature
    (500/503 "high demand") ne doit pas arreter le robot. Un appel refuse
    n'est pas facture, donc la cascade ne coute rien de plus."""
    if scene is None:
        scene = scenes_possibles(brand)[0]
    prompt = build_prompt(brand, theme, objects, scene)
    if modeles is None:
        modeles = (MODEL,) + tuple(m for m in MODELS if m != MODEL)
    errors = []
    for modele in modeles:
        for url, payload in _payloads(prompt, aspect, size, modele):
            try:
                data = _post(url, payload)
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")[:300]
                errors.append("%s / %s -> %s %s"
                              % (modele, url.rsplit("/", 1)[-1], e.code, body))
                continue
            b64 = _find_image_b64(data)
            if not b64:
                errors.append("%s / %s -> reponse sans image : %s"
                              % (modele, url.rsplit("/", 1)[-1], json.dumps(data)[:200]))
                continue
            BG_DIR.mkdir(parents=True, exist_ok=True)
            out = BG_DIR / out_name
            out.write_bytes(base64.b64decode(b64))
            if modele != MODEL:
                print("      (modele de secours utilise : %s)" % modele)
            noter_scene(brand, scene)      # la rotation ne compte que ce qui existe
            print("      (scene : %s, rendu %s)" % (scene, theme_de_la_scene(brand, scene)))
            return out, prompt
    raise RuntimeError("Generation impossible :\n  " + "\n  ".join(errors))


def main():
    ap = argparse.ArgumentParser(description="Fond de carrousel via Nano Banana Pro.")
    ap.add_argument("--brand", required=True, choices=list(SCENES))
    ap.add_argument("--scene", default=None, help="Nom de la scene (voir SCENES)")
    ap.add_argument("--theme", required=True, help="Sujet du carrousel de la semaine")
    ap.add_argument("--out", default=None, help="Nom du fichier de sortie (.jpg)")
    ap.add_argument("--size", default=SIZE, choices=["1K", "2K", "4K"])
    ap.add_argument("--dry-run", action="store_true",
                    help="Affiche le prompt sans rien depenser")
    ap.add_argument("--go", action="store_true",
                    help="Genere pour de vrai (consomme du credit)")
    args = ap.parse_args()

    prompt = build_prompt(args.brand, args.theme, scene=args.scene)
    if not args.go or args.dry_run:
        cost = {"1K": 0.134, "2K": 0.134, "4K": 0.24}[args.size]
        print("=== MODE A BLANC (0 depense) ===")
        print("Marque   :", args.brand)
        print("Modele   :", MODEL, "| format", ASPECT, "| taille", args.size)
        print("Cout si lance :", cost, "$")
        print("Longueur du prompt :", len(prompt), "caracteres")
        print("--- PROMPT ---")
        print(prompt)
        print("\nPour lancer pour de vrai : ajoute --go")
        return

    out_name = args.out or ("%s_bg.jpg" % args.brand)
    path, used = generate_background(args.brand, args.theme, out_name,
                                     scene=args.scene, size=args.size)
    print("Image generee :", path)


if __name__ == "__main__":
    sys.exit(main())
