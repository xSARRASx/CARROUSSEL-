#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les fonds de stories (1080x1920) avec Gemini (gemini-2.5-flash-image).
La cle API vient de la variable d'environnement GEMINI_API_KEY (jamais dans le code).

Usage :
  python3 gen_background.py            # genere les fonds manquants du catalogue
  python3 gen_background.py --force    # regenere tout
"""
import base64, json, os, pathlib, sys, time, urllib.request, io
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]          # stories/
OUT = ROOT / "assets" / "backgrounds"
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

STYLE = ("Cinematic, moody, dominated by deep navy blue #0d1b2e, subtle warm orange "
         "#E8561F accent glow, very dark with lots of empty dark space so white text "
         "can be overlaid later, high quality photo, no people, no readable text, "
         "no letters, no logo, no watermark, vertical 9:16 composition.")

# Style "natif Instagram" (stories facon Pierre) : photos naturelles chaudes,
# beaucoup de ciel / zones calmes pour poser du texte dessus.
STYLE_WARM = ("Natural iPhone photo look, golden hour warm light, soft tones, "
              "large calm empty areas (sky or plain surfaces) filling most of the "
              "frame so text can be overlaid, high quality, no people, no readable "
              "text, no letters, no logo, no watermark, vertical 9:16 composition.")

# Fonds pleine page (1080x1920) et images de contenu (cartes, 4:3).
CATALOG = {
    "bg_navy":         {"subject": "Abstract minimal dark background, soft diagonal light rays, fine grain, faint orange glow in the upper corner."},
    "bg_immobilier":   {"subject": "Modern residential apartment building facade at dusk, a few warm lit windows, deep navy night sky, blurred dark foreground."},
    "bg_mindset":      {"subject": "Desk near a window at night, blurred city bokeh lights outside, one small warm desk lamp glow, everything else in shadow."},
    "bg_conversation": {"subject": "A smartphone lying on a dark surface, screen glowing softly warm, gentle reflection, seen from above, everything else dark."},
    "img_poignee":     {"subject": "Close-up of a confident handshake between two people, modern apartment building blurred in the background at dusk, warm window lights.",
                        "size": (1320, 990), "aspect": "4:3"},
    "img_chemin":      {"subject": "Silhouette of a person seen from behind, walking up outdoor stairs at night towards warm city lights in the distance, mist.",
                        "size": (1320, 990), "aspect": "4:3"},
    # Fonds chauds "natif Instagram" (stories facon Pierre)
    "bg_ciel_dore":    {"subject": "Dramatic golden sunset sky with warm orange clouds, dark silhouette of hills and a few trees along the very bottom edge, the sky fills 85 percent of the frame.",
                        "style": STYLE_WARM},
    "bg_prairie":      {"subject": "Green meadow with a small dirt trail, golden hour sunset sky with soft clouds above, sky fills the upper two thirds.",
                        "style": STYLE_WARM},
    "bg_chemin_aube":  {"subject": "Country dirt path through quiet fields at sunrise, soft golden mist, gentle warm sky filling most of the upper frame.",
                        "style": STYLE_WARM},
    "bg_salon_cosy":   {"subject": "Cozy dim living room in the evening, warm floor lamp glow, armchair and plant softly blurred, muted calm tones, slightly out of focus.",
                        "style": STYLE_WARM},
    "bg_ville_doree":  {"subject": "European city rooftops at golden hour seen from above, warm haze, soft sun flare, buildings small in the lower third, calm warm sky above.",
                        "style": STYLE_WARM},
    "bg_mer_calme":    {"subject": "Calm sea at sunset, gentle waves, warm pastel sky with a few soft clouds filling most of the frame, peaceful.",
                        "style": STYLE_WARM},
    # Vague 2 (03/08/2026) : Martin veut des fonds VRAIMENT varies -> 9 fonds
    # chauds supplementaires, meme famille golden hour.
    "bg_plage_aube":   {"subject": "Quiet empty sandy beach at sunrise, soft pastel peach sky filling most of the frame, gentle foam line at the bottom.",
                        "style": STYLE_WARM},
    "bg_montagne":     {"subject": "Soft rolling mountain ridges fading into golden haze at sunset, layers of warm tones, sky filling the upper half.",
                        "style": STYLE_WARM},
    "bg_lac":          {"subject": "Perfectly still mountain lake at golden hour, mirror reflection of a warm sky, thin mist, very calm and empty.",
                        "style": STYLE_WARM},
    "bg_terrasse":     {"subject": "Cozy apartment balcony terrace at sunset with a few plants and string lights softly blurred, warm golden light, calm sky visible.",
                        "style": STYLE_WARM},
    "bg_village":      {"subject": "Charming quiet European village street at golden hour, warm stone facades softly blurred, empty street, soft sun flare.",
                        "style": STYLE_WARM},
    "bg_ble":          {"subject": "Golden wheat field swaying at sunset, warm backlight, soft focus, big calm warm sky filling the upper two thirds.",
                        "style": STYLE_WARM},
    "bg_ciel_rose":    {"subject": "Dreamy pastel pink and orange cloudy sky at dusk, only sky and clouds, very soft and calm.",
                        "style": STYLE_WARM},
    "bg_immeuble_dore":{"subject": "Modern residential apartment building facade bathed in warm golden hour light, a few plants on balconies, soft blur, warm sky above.",
                        "style": STYLE_WARM},
    "bg_bureau_matin": {"subject": "Bright desk near a large window in warm morning sunlight, notebook and coffee cup softly blurred, golden glow, mostly calm bright surfaces.",
                        "style": STYLE_WARM},
    # Vague 3 (10/08/2026) : la video du dimanche parle de COPROPRIETE
    # (assemblee generale, reglement, syndic). Fonds dedies au sujet, meme
    # famille golden hour, pour que les sequences n'aient jamais deux fois
    # le meme fond.
    "bg_hall_immeuble": {"subject": "Entrance hall of a classic residential building, warm afternoon light through the glass door, softly blurred, empty, calm bright walls.",
                        "style": STYLE_WARM},
    "bg_boites_lettres": {"subject": "Row of mailboxes in a residential building hallway, warm soft light, shallow depth of field, calm empty wall above them.",
                        "style": STYLE_WARM},
    "bg_escalier":     {"subject": "Old wooden stairwell of a Parisian building seen from below, warm golden light falling from a skylight, soft blur, empty.",
                        "style": STYLE_WARM},
    "bg_cour":         {"subject": "Quiet inner courtyard of a residential building at golden hour, warm stone facades, a few plants, soft light, empty and calm.",
                        "style": STYLE_WARM},
    "bg_documents":    {"subject": "Stack of plain blank paper sheets and a pen on a wooden table in warm morning sunlight, very shallow depth of field, no writing at all on the pages.",
                        "style": STYLE_WARM},
    "bg_cles":         {"subject": "Set of keys resting on a wooden table near a sunlit window, warm golden light, softly blurred background, calm empty surface.",
                        "style": STYLE_WARM},
    "bg_salon_vide":   {"subject": "Empty furnished living room of a rental apartment in warm afternoon light, sofa and coffee table softly blurred, calm bright wall.",
                        "style": STYLE_WARM},
    "bg_facade_pierre": {"subject": "Classic Haussmann stone building facade with balconies at golden hour, warm light on the stone, soft blur, calm warm sky above.",
                        "style": STYLE_WARM},

    # ------------------------------------------------------------------
    # Vague 3 (14/09/2026) — CAUSE RACINE de « je veux des choses différentes ».
    # Martin l'a dit deux fois le 10/09. On avait corrige les FORMULATIONS,
    # mais pas les IMAGES : 23 fonds utilisables pour deux fournees par semaine
    # qui en consomment 15 a 25 chacune. Mathematiquement, la meme plage et le
    # meme ciel rose revenaient toutes les semaines. Aucune rotation de texte
    # ne repare ca : il fallait elargir la banque.
    # Meme famille golden hour, mais des LIEUX qu'on n'avait pas : interieurs,
    # objets, matieres, ville, saisons. De quoi tenir plusieurs mois sans
    # reprendre le meme visuel.
    # ------------------------------------------------------------------
    "bg_cuisine_matin":  {"subject": "Empty modern kitchen counter in the morning, warm sunlight coming through a window on the right, clean surfaces, soft shadows, the upper half almost empty.",
                          "style": STYLE_WARM},
    "bg_cafe_table":     {"subject": "A single cup of coffee on a wooden table near a bright window, warm morning light, plenty of empty table surface in the upper frame, shallow depth of field.",
                          "style": STYLE_WARM},
    "bg_fenetre_pluie":  {"subject": "Rain drops on a window pane at golden hour, blurred warm city lights behind, large calm out-of-focus area filling most of the frame.",
                          "style": STYLE_WARM},
    "bg_couloir_hotel":  {"subject": "Quiet hotel corridor with warm wall lamps, soft carpet, receding perspective, calm empty walls, nobody in sight.",
                          "style": STYLE_WARM},
    "bg_chambre_lumiere":{"subject": "Neatly made bed in a bright airy bedroom, white linen, warm daylight from a side window, large calm empty wall above the bed.",
                          "style": STYLE_WARM},
    "bg_bureau_papiers": {"subject": "Wooden desk seen from above with a closed notebook and a pen, warm side light, lots of empty desk surface, calm and tidy.",
                          "style": STYLE_WARM},
    "bg_etagere":        {"subject": "Simple wooden shelf against a warm plaster wall, a few books and a small plant, soft afternoon light, large empty wall area above.",
                          "style": STYLE_WARM},
    "bg_toits_pluie":    {"subject": "European rooftops under a soft grey and amber sky after rain, wet tiles catching warm light, wide calm sky filling the upper two thirds.",
                          "style": STYLE_WARM},
    "bg_ruelle":         {"subject": "Narrow old european street at golden hour, warm stone walls, long soft shadows, empty, receding perspective, nobody in sight.",
                          "style": STYLE_WARM},
    "bg_port":           {"subject": "Small fishing harbour at sunrise, a few moored boats in the lower third, soft pastel sky filling the upper frame, very calm water.",
                          "style": STYLE_WARM},
    "bg_foret_automne":  {"subject": "Autumn forest path with warm amber leaves, soft diffused light through the trees, misty depth, calm and quiet.",
                          "style": STYLE_WARM},
    "bg_neige_douce":    {"subject": "Quiet snowy field at dusk with a soft pink and blue sky, bare trees small along the bottom edge, large calm sky filling most of the frame.",
                          "style": STYLE_WARM},
    "bg_champ_ete":      {"subject": "Golden wheat field under a warm late afternoon sky, gentle breeze, soft focus, the sky filling the upper half.",
                          "style": STYLE_WARM},
    "bg_balcon":         {"subject": "Empty balcony with a simple railing overlooking a warm hazy city at sunset, calm sky filling most of the frame.",
                          "style": STYLE_WARM},
    "bg_escalier_bois":  {"subject": "Warm wooden staircase in an old building, soft daylight from above, calm empty wall on one side, nobody in sight.",
                          "style": STYLE_WARM},
    "bg_table_bois":     {"subject": "Close-up of a warm weathered wooden table surface filling the whole frame, soft golden side light, subtle grain, nothing on it.",
                          "style": STYLE_WARM},
    "bg_mur_beton":      {"subject": "Smooth warm concrete wall lit by late afternoon sun, soft diagonal shadow across it, minimal, filling the whole frame.",
                          "style": STYLE_WARM},
    "bg_rideau":         {"subject": "Sheer white curtain glowing with warm backlight from a window, gentle folds, very soft and calm, filling the frame.",
                          "style": STYLE_WARM},
    # ------------------------------------------------------------------
    # Vague 4 (12/10/2026) — MEME CAUSE, MEME REMEDE, UN CRAN PLUS LOIN.
    # Avec 45 fonds et 15 par fournee, la 4e fournee d'affilee ne pouvait plus
    # eviter de reprendre une image vue dans les trois precedentes : il n'en
    # restait qu'UN de libre. Le controle de variete ne l'attrape pas (il ne
    # refuse qu'un fond present dans les TROIS lots precedents), donc c'est
    # arrive sans alerte. On elargit a 63, ce qui redonne une vraie marge.
    # Regle a retenir : des qu'il reste moins de 20 fonds inutilises sur les
    # trois dernieres fournees, on genere une vague.
    # ------------------------------------------------------------------
    "bg_salle_bain":     {"subject": "Clean simple bathroom with a white basin and a mirror, warm morning light from a frosted window, calm empty tiled wall filling the upper frame.",
                          "style": STYLE_WARM},
    "bg_entree":         {"subject": "Entrance hall of an apartment with a closed wooden door and a coat hook, warm daylight on a plain wall, large calm empty area.",
                          "style": STYLE_WARM},
    "bg_canape":         {"subject": "Corner of a linen sofa with two cushions, warm late afternoon light across it, plain calm wall above filling most of the frame.",
                          "style": STYLE_WARM},
    "bg_fenetre_ouverte":{"subject": "Open window with a light curtain moving in the breeze, warm sunlight streaming in, blurred greenery outside, calm and bright.",
                          "style": STYLE_WARM},
    "bg_parquet":        {"subject": "Close-up of a warm oak parquet floor filling the whole frame, soft golden light from a side window, subtle wood grain, nothing on it.",
                          "style": STYLE_WARM},
    "bg_mur_brique":     {"subject": "Old warm red brick wall lit by late afternoon sun, soft texture, minimal, filling the whole frame.",
                          "style": STYLE_WARM},
    "bg_plante":         {"subject": "A single green potted plant near a bright window, warm backlight through the leaves, plain calm wall filling most of the frame.",
                          "style": STYLE_WARM},
    "bg_lampe":          {"subject": "Small warm table lamp glowing on a side table at dusk, soft pool of light, calm darker wall around it with lots of empty space.",
                          "style": STYLE_WARM},
    "bg_miroir":         {"subject": "Round mirror on a warm plaster wall reflecting soft daylight, minimal, large calm empty wall area around it.",
                          "style": STYLE_WARM},
    "bg_cour_interieure":{"subject": "Quiet inner courtyard of an old building at golden hour, warm stone walls, a few plants, calm sky above, nobody in sight.",
                          "style": STYLE_WARM},
    "bg_quai":           {"subject": "Riverside quay at golden hour, calm water reflecting warm light, low stone wall along the bottom, wide soft sky filling the upper frame.",
                          "style": STYLE_WARM},
    "bg_pont":           {"subject": "Old stone bridge over calm water at sunrise, soft mist, pastel sky filling the upper two thirds, very quiet.",
                          "style": STYLE_WARM},
    "bg_marche":         {"subject": "Empty european market street early in the morning, closed shutters, warm low sunlight along the pavement, receding perspective, nobody in sight.",
                          "style": STYLE_WARM},
    "bg_colline":        {"subject": "Rolling green hills at dawn with soft layered mist, warm pastel sky filling the upper two thirds, very calm.",
                          "style": STYLE_WARM},
    "bg_dunes":          {"subject": "Sand dunes with beach grass at golden hour, long soft shadows, wide warm sky filling the upper half, nobody in sight.",
                          "style": STYLE_WARM},
    "bg_oliviers":       {"subject": "Olive grove in warm late afternoon light, silver green leaves, soft rows receding, calm hazy sky above.",
                          "style": STYLE_WARM},
    "bg_brume_matin":    {"subject": "Open field under morning mist with a faint warm sun breaking through, very soft and minimal, large pale calm area filling most of the frame.",
                          "style": STYLE_WARM},
    "bg_toit_terrasse":  {"subject": "Empty rooftop terrace with a simple wooden table at sunset, warm hazy city rooftops far below, wide calm sky filling the upper frame.",
                          "style": STYLE_WARM},
}

def call_gemini(body, key):
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)

def generate(name, subject, size=(1080, 1920), aspect="9:16", style=None):
    key = os.environ.get("GEMINI_API_KEY")
    assert key, "GEMINI_API_KEY absente de l'environnement"
    prompt = subject + " " + (style or STYLE)
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"imageConfig": {"aspectRatio": aspect}},
    }
    data = None
    for attempt, wait in enumerate((0, 8, 25), 1):
        if wait:
            print(f"  ...nouvel essai dans {wait}s ({name})")
            time.sleep(wait)
        try:
            data = call_gemini(body, key)
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:400]
            if e.code == 400 and body.get("generationConfig"):
                # serveur sans imageConfig : on retente sans, on recadrera
                body.pop("generationConfig", None)
                data = call_gemini(body, key)
                break
            if e.code in (429, 500, 503) and attempt < 3:
                continue        # surcharge / quota minute : on attend et on reessaie
            raise RuntimeError(f"Gemini HTTP {e.code}: {detail}")
    assert data, f"Gemini indisponible pour {name} apres 3 essais"

    parts = data["candidates"][0]["content"]["parts"]
    b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    im = Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")

    # recadrage/redimensionnement vers la taille cible exacte (cover)
    tw, th = size
    scale = max(tw / im.width, th / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    x = (im.width - tw) // 2
    y = (im.height - th) // 2
    im = im.crop((x, y, x + tw, y + th))

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.jpg"
    im.save(path, "JPEG", quality=90, optimize=True)
    print(f"{name}.jpg  ({path.stat().st_size // 1024} Ko)")

def main():
    force = "--force" in sys.argv
    for name, spec in CATALOG.items():
        path = OUT / f"{name}.jpg"
        if path.exists() and not force:
            print(f"{name}.jpg  deja present, saute (utilise --force pour regenerer)")
            continue
        generate(name, spec["subject"], size=spec.get("size", (1080, 1920)),
                 aspect=spec.get("aspect", "9:16"), style=spec.get("style"))

if __name__ == "__main__":
    main()
