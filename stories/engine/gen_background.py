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
