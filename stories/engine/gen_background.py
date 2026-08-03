#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les fonds de stories (1080x1920) avec Gemini (gemini-2.5-flash-image).
La cle API vient de la variable d'environnement GEMINI_API_KEY (jamais dans le code).

Usage :
  python3 gen_background.py            # genere les fonds manquants du catalogue
  python3 gen_background.py --force    # regenere tout
"""
import base64, json, os, pathlib, sys, urllib.request, io
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]          # stories/
OUT = ROOT / "assets" / "backgrounds"
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

STYLE = ("Cinematic, moody, dominated by deep navy blue #0d1b2e, subtle warm orange "
         "#E8561F accent glow, very dark with lots of empty dark space so white text "
         "can be overlaid later, high quality photo, no people, no readable text, "
         "no letters, no logo, no watermark, vertical 9:16 composition.")

CATALOG = {
    "bg_navy":         "Abstract minimal dark background, soft diagonal light rays, fine grain, faint orange glow in the upper corner.",
    "bg_immobilier":   "Modern residential apartment building facade at dusk, a few warm lit windows, deep navy night sky, blurred dark foreground.",
    "bg_mindset":      "Desk near a window at night, blurred city bokeh lights outside, one small warm desk lamp glow, everything else in shadow.",
    "bg_conversation": "A smartphone lying on a dark surface, screen glowing softly warm, gentle reflection, seen from above, everything else dark.",
}

def generate(name, subject):
    key = os.environ.get("GEMINI_API_KEY")
    assert key, "GEMINI_API_KEY absente de l'environnement"
    prompt = subject + " " + STYLE
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"imageConfig": {"aspectRatio": "9:16"}},
    }
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:400]
        if e.code == 400 and "imageConfig" in json.dumps(body):
            # ancien serveur sans imageConfig : on retente sans, on recadrera
            body.pop("generationConfig", None)
            req = urllib.request.Request(
                URL, data=json.dumps(body).encode(),
                headers={"Content-Type": "application/json", "x-goog-api-key": key},
            )
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.load(r)
        else:
            raise RuntimeError(f"Gemini HTTP {e.code}: {detail}")

    parts = data["candidates"][0]["content"]["parts"]
    b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    im = Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")

    # recadrage/redimensionnement vers 1080x1920 exact (cover)
    tw, th = 1080, 1920
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
    for name, subject in CATALOG.items():
        path = OUT / f"{name}.jpg"
        if path.exists() and not force:
            print(f"{name}.jpg  deja present, saute (utilise --force pour regenerer)")
            continue
        generate(name, subject)

if __name__ == "__main__":
    main()
