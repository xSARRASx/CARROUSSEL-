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
ASPECT = "4:5"                        # format des slides
SIZE = "2K"                           # 1K / 2K / 4K (2K = bon compromis prix/qualite)

# --------------------------------------------------------------------------
# Prompts de fond par marque (regles PARTIE D du carroussel.md).
# Le THEME de la semaine est injecte pour coller au sujet du carrousel.
# --------------------------------------------------------------------------

COMMON_RULES = """
LAYOUT (STRICT VERTICAL 4:5, THINK 1080 x 1350)
- TOP 38%: almost EMPTY surface, only subtle texture and gentle light falloff.
  A large white title will be placed over this zone, so it must stay clean and dark.
- BOTTOM 62%: the objects, arranged with generous breathing room, never crowded.
- Comfortable margins left and right, no object awkwardly cropped.

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

BRAND_PROMPTS = {
    "lesousloueur": """═══════════════════════════════════════════════════════
PREMIUM EDITORIAL FLAT-LAY PHOTOGRAPH, STRICT VERTICAL 4:5
THEME: {theme}
═══════════════════════════════════════════════════════

CONCEPT
Top-down editorial flat-lay photograph on a deep navy blue matte surface.
The scene evokes a serious short-term rental professional, organized and calm,
in the context of: {theme}. Premium hospitality magazine mood
(Kinfolk, Monocle, Conde Nast Traveler).

OBJECTS (lower two thirds only, choose what fits the theme)
{objects}

COLOR PALETTE (STRICT, DO NOT DEVIATE)
- Dominant: deep navy blue #0E1B2E and #142841 for the surface and shadows
- Accent: warm vibrant orange #E8551F to #F25C2A, maximum three small touches
- Secondary: white #FFFFFF for papers, warm cream #F5F5EE, natural kraft brown
- NO violet, NO purple, NO magenta, NO pink, NO green anywhere

LIGHTING
- Soft directional daylight from the upper left, slightly warm
- Gentle soft shadows, no harsh contrast, very slight natural vignette
""" + COMMON_RULES,

    "guestlucky": """═══════════════════════════════════════════════════════
PREMIUM TECH STILL-LIFE PHOTOGRAPH, STRICT VERTICAL 4:5
THEME: {theme}
═══════════════════════════════════════════════════════

CONCEPT
Cinematic premium still-life photograph of a modern ordered desk at night,
seen from a slightly elevated three-quarter angle. High-end SaaS brand mood
(Stripe, Linear, Notion), in the context of: {theme}.

OBJECTS (lower two thirds only, choose what fits the theme)
{objects}

COLOR PALETTE (STRICT, DO NOT DEVIATE)
- Base: very deep navy blue #0F1A35 and #0A1228, close to black in the corners
- Primary glow: violet #7B4FE0 and #8B3FD9, coming from the left, off-frame
- Secondary glow: magenta pink #E84A8C and #C13FBE, softer, from the right
- White #FFFFFF only for blank papers and faint edge highlights
- NO orange, NO yellow, NO green, NO teal, NO red anywhere

LIGHTING
- Ambient LED-style glow from OFF-FRAME sources only, blending into darkness
- Soft reflections on glass and matte surfaces, deep shadows elsewhere
- Cinematic falloff, corners darker than the center bottom
""" + COMMON_RULES,
}

DEFAULT_OBJECTS = {
    "lesousloueur": (
        "- One closed kraft document folder with a completely BLANK cover\n"
        "- A neat stack of white paper sheets, all pages completely BLANK\n"
        "- A pair of apartment keys on a small natural wood keychain\n"
        "- One elegant pen with an orange barrel\n"
        "- Thin-frame reading glasses\n"
        "- One white ceramic espresso cup on a saucer\n"
        "- Two or three small orange paper clips"
    ),
    "guestlucky": (
        "- A small stack of dark folders perfectly aligned, BLANK covers\n"
        "- A tidy pile of white paper sheets, completely BLANK\n"
        "- One smartphone laying flat, screen COMPLETELY OFF, dark glass\n"
        "- One elegant dark pen placed parallel to the papers\n"
        "- One small dark ceramic cup, matte finish\n"
        "- Background dissolving into soft dark bokeh"
    ),
}


def build_prompt(brand, theme, objects=None):
    """Construit le prompt image de la semaine pour une marque + un theme."""
    if brand not in BRAND_PROMPTS:
        raise ValueError("Marque inconnue : " + brand)
    return BRAND_PROMPTS[brand].format(
        theme=theme, objects=objects or DEFAULT_OBJECTS[brand]).strip()


# --------------------------------------------------------------------------
# Appel API Google
# --------------------------------------------------------------------------

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
    with urllib.request.urlopen(req, timeout=180) as r:
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


def _payloads(prompt, aspect, size):
    """Deux formes de requete : la nouvelle (interactions) puis l'ancienne
    (generateContent). On essaie la 1re, on bascule sur la 2e si refusee."""
    new_style = (BASE + "/v1beta/interactions", {
        "model": MODEL,
        "input": [{"type": "text", "text": prompt}],
        "response_format": {"type": "image", "mime_type": "image/jpeg",
                            "aspect_ratio": aspect, "image_size": size},
    })
    old_style = (BASE + "/v1beta/models/" + MODEL + ":generateContent", {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect, "imageSize": size},
        },
    })
    return [new_style, old_style]


def generate_background(brand, theme, out_name, objects=None,
                        aspect=ASPECT, size=SIZE):
    """Genere la photo de fond et l'enregistre dans assets/backgrounds/.
    Renvoie (chemin, prompt_utilise). ATTENTION : consomme du credit Google."""
    prompt = build_prompt(brand, theme, objects)
    errors = []
    for url, payload in _payloads(prompt, aspect, size):
        try:
            data = _post(url, payload)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            errors.append("%s -> %s %s" % (url.rsplit("/", 1)[-1], e.code, body))
            continue
        b64 = _find_image_b64(data)
        if not b64:
            errors.append("%s -> reponse sans image : %s"
                          % (url.rsplit("/", 1)[-1], json.dumps(data)[:200]))
            continue
        BG_DIR.mkdir(parents=True, exist_ok=True)
        out = BG_DIR / out_name
        out.write_bytes(base64.b64decode(b64))
        return out, prompt
    raise RuntimeError("Generation impossible :\n  " + "\n  ".join(errors))


def main():
    ap = argparse.ArgumentParser(description="Fond de carrousel via Nano Banana Pro.")
    ap.add_argument("--brand", required=True, choices=list(BRAND_PROMPTS))
    ap.add_argument("--theme", required=True, help="Sujet du carrousel de la semaine")
    ap.add_argument("--out", default=None, help="Nom du fichier de sortie (.jpg)")
    ap.add_argument("--size", default=SIZE, choices=["1K", "2K", "4K"])
    ap.add_argument("--dry-run", action="store_true",
                    help="Affiche le prompt sans rien depenser")
    ap.add_argument("--go", action="store_true",
                    help="Genere pour de vrai (consomme du credit)")
    args = ap.parse_args()

    prompt = build_prompt(args.brand, args.theme)
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
    path, used = generate_background(args.brand, args.theme, out_name, size=args.size)
    print("Image generee :", path)


if __name__ == "__main__":
    sys.exit(main())
