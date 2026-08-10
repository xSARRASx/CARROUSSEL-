#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les images lumineuses des videos 3 et 4 (API image Gemini).

Ces images sont ensuite animees par monter.py (zoom lent facon cinema).
C'est la solution de repli quand le quota Veo est epuise : le quota des
images est independant de celui de la video.
"""
import os, json, base64, pathlib, urllib.request
from concurrent.futures import ThreadPoolExecutor

KEY = os.environ["GEMINI_API_KEY"]
URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
       "gemini-2.5-flash-image:generateContent")
OUT = pathlib.Path(__file__).resolve().parent / "images"
OUT.mkdir(parents=True, exist_ok=True)

NEG = ("Absolutely no text, no letters, no words, no watermark, no logo. "
       "Photorealistic editorial photography, sharp focus, natural skin tones, "
       "correct hands with five fingers, no deformation.")

PLANS = {
    # video 3 : ce que le logement rapporte
    "v3_i1": ("A smiling woman in her thirties opening wide white curtains in a very "
              "bright airy apartment, brilliant morning sunlight flooding the white "
              "room, joyful and calm, high-key lighting, white and cream tones, "
              "seen from a slight distance, natural and warm."),
    "v3_i2": ("A bright sunlit bedroom, perfectly made bed with crisp white linen, "
              "sunlight streaming through a large window onto pale wooden floor, "
              "fresh flowers on the bedside table, very luminous and airy, no people."),
    "v3_i3": ("A smiling man in his forties at a sunlit kitchen table with a laptop "
              "and a coffee cup, bright white kitchen flooded with daylight behind "
              "him, pleased and relaxed expression, warm friendly atmosphere."),
    "v3_i4": ("A very bright modern living room with floor to ceiling windows, white "
              "linen sofa, green plants, sunlight pouring in and reflecting on the "
              "pale wooden floor, airy and spacious, no people."),

    # video 4 : c'est simple et rapide
    "v4_i1": ("Close-up of a woman's hands holding a smartphone at a bright white "
              "kitchen counter, brilliant daylight from a large window behind, "
              "the phone screen plain and blank, fresh and modern, luminous."),
    "v4_i2": ("A friendly woman in her thirties smiling while talking on the phone in "
              "a bright sunlit living room, relaxed confident posture, large window "
              "with brilliant daylight behind her, white and cream interior."),
    "v4_i3": ("Two smiling people shaking hands in front of a bright residential "
              "building entrance on a sunny day, warm natural sunlight, green trees "
              "behind, welcoming professional atmosphere, hands clearly visible "
              "and correctly formed."),
    "v4_i4": ("A relaxed smiling couple sitting together on a sofa in a very bright "
              "sunlit living room, looking at a tablet, brilliant daylight, white "
              "and cream tones, plants, calm and reassuring."),
}


def gen(item):
    nom, prompt = item
    dest = OUT / f"{nom}.png"
    if dest.exists() and dest.stat().st_size > 10000:
        return f"  (deja la) {dest.name}"
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt + " " + NEG}]}],
        "generationConfig": {"imageConfig": {"aspectRatio": "9:16"}},
    }).encode()
    req = urllib.request.Request(URL, data=body,
        headers={"x-goog-api-key": KEY, "Content-Type": "application/json"})
    for essai in range(3):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.load(r)
            for p in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in p:
                    dest.write_bytes(base64.b64decode(p["inlineData"]["data"]))
                    return f"  OK {dest.name} ({dest.stat().st_size // 1024} Ko)"
            return f"  PAS D'IMAGE {dest.name}"
        except Exception as e:
            if essai == 2:
                return f"  ECHEC {dest.name} : {type(e).__name__}"
    return f"  ECHEC {dest.name}"


if __name__ == "__main__":
    print(f"Generation de {len(PLANS)} images lumineuses...")
    with ThreadPoolExecutor(max_workers=4) as ex:
        for ligne in ex.map(gen, PLANS.items()):
            print(ligne, flush=True)
    print("TERMINE")
