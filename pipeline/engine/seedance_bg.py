#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
seedance_bg.py -- Etape 3 du robot carrousels : la PHOTO DE FOND via Seedance.

Contexte important (decouvert le 24/07/2026) :
  L'API Seedance (celle qu'un robot appelle avec la cle) ne fait PAS de photo :
  elle ne fait que de la VIDEO. Le "text-to-image" (Seedream, Nano Banana)
  n'existe que sur le site web, avec un humain connecte -> inutilisable par un
  robot automatique.

  ASTUCE : l'API video sait renvoyer une IMAGE de la video (option
  "return_last_frame"). Donc on demande une mini-video et on recupere UNE image :
  c'est notre photo de fond. C'est Seedance, c'est la cle, c'est 100% automatique.

Cout : une generation standard (5s, 720p) = ~60 credits (mesure reel).

SECRET : la cle vient UNIQUEMENT de la variable d'environnement SEEDANCE_API_KEY.
Jamais dans le code (repo public).

Usage :
    # 1) Voir la commande SANS depenser de credits (mode a blanc) :
    python3 pipeline/engine/seedance_bg.py --brand guestlucky --dry-run

    # 2) Lancer la vraie generation (DEPENSE des credits) :
    python3 pipeline/engine/seedance_bg.py --brand guestlucky --go

Sortie : une image de fond dans pipeline/assets/backgrounds/.
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

BASE = "https://api.seedance2.ai"
GEN_ENDPOINT = "/v1/videos/generations"
TASK_ENDPOINT = "/v1/tasks/{id}"

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
BACKGROUNDS_DIR = os.path.join(REPO_ROOT, "pipeline", "assets", "backgrounds")

# --------------------------------------------------------------------------
# Prompts de fond par marque (regles PARTIE D du carroussel.md).
# Fond reutilisable, sobre, photo-realiste, laisse de la place au texte.
# En anglais (meilleurs resultats). Palettes STRICTES, ne pas melanger.
# --------------------------------------------------------------------------

COMMON_EXCLUSIONS = (
    "No text, no letters, no words, no logos, no watermark, no UI, no emoji. "
    "No visible light rays, no halos, no light beams, no light shafts. "
    "No exaggerated contrast, no HDR over-processing, no oversaturation, "
    "no artificial AI look, no cheap plastic 3D. "
    "Photorealistic, natural film grain, subtle premium lighting, "
    "slow gentle camera drift, minimalist composition with empty negative space."
)

BRAND_PROMPTS = {
    "guestlucky": (
        "Premium modern SaaS editorial background, cinematic and calm. "
        "Deep navy blue base (#0F1A35, #0A1228) with soft violet (#7B4FE0) and "
        "magenta pink (#E84A8C) glows blended smoothly into the dark, like a "
        "high-end tech brand (Stripe, Linear, Notion). Abstract, out-of-focus, "
        "smooth gradient atmosphere, plenty of dark empty space for overlaid text. "
        + COMMON_EXCLUSIONS
    ),
    "lesousloueur": (
        "Premium editorial hospitality background, warm and calm, cinematic. "
        "Deep navy blue base (#0E1B2E, #142841) with a warm vibrant orange "
        "(#E8551F) soft glow blended into the dark, magazine mood "
        "(Kinfolk, Monocle, Conde Nast Traveler). Abstract, out-of-focus, smooth "
        "gradient atmosphere, generous dark empty space for overlaid text. "
        "Never use violet or magenta. "
        + COMMON_EXCLUSIONS
    ),
}

# Reglages de generation (economiques et surs).
DEFAULT_ASPECT = "9:16"     # portrait sur : on recadrera en 4:5 ensuite
DEFAULT_RESOLUTION = "720p"  # 720p = ~60 credits (connu). 1080p = plus cher.


def build_payload(brand, aspect=DEFAULT_ASPECT, resolution=DEFAULT_RESOLUTION):
    """Prepare la commande envoyee a Seedance (sans l'envoyer)."""
    if brand not in BRAND_PROMPTS:
        raise ValueError("Marque inconnue : " + brand +
                         " (attendu : guestlucky ou lesousloueur)")
    return {
        "input": {
            "generation_type": "text-to-video",
            "prompt": BRAND_PROMPTS[brand],
            "aspect_ratio": aspect,
            "resolution": resolution,
            "generate_audio": False,   # pas de son : inutile pour une image
            "watermark": False,
            "return_last_frame": True,  # <-- l'astuce : on veut une IMAGE
        }
    }


# --------------------------------------------------------------------------
# Appels reseau
# --------------------------------------------------------------------------

def _api(method, path, body=None):
    key = os.environ.get("SEEDANCE_API_KEY")
    if not key:
        raise RuntimeError("SEEDANCE_API_KEY absente de l'environnement.")
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        raise RuntimeError("Seedance a repondu " + str(e.code) + " : " + detail[:300])


def create_task(payload):
    """Lance la generation. Renvoie (taskId, credits reserves)."""
    _, data = _api("POST", GEN_ENDPOINT, payload)
    return data["taskId"], data.get("credits")


def wait_for_result(task_id, timeout_s=600, every_s=8):
    """Interroge la tache jusqu'a ce qu'elle soit finie. Renvoie le dict data."""
    waited = 0
    while waited < timeout_s:
        _, d = _api("GET", TASK_ENDPOINT.format(id=task_id))
        status = d.get("status")
        if status == "completed":
            return d
        if status == "failed":
            raise RuntimeError("Generation echouee : " + str(d.get("failed_reason")))
        time.sleep(every_s)
        waited += every_s
        print("      ... en cours (" + str(waited) + "s)")
    raise RuntimeError("Delai depasse (la tache n'a pas fini a temps).")


def download_background(task_data, out_path):
    """Recupere l'IMAGE de fond : last_frame_url si dispo, sinon 1re image de
    la video. Recadre en 4:5 et sauve en JPEG."""
    from PIL import Image
    import io

    data = task_data.get("data", {})
    frame_url = data.get("last_frame_url")

    if frame_url:
        raw = _download_bytes(frame_url)
        img = Image.open(io.BytesIO(raw)).convert("RGB")
    else:
        # Secours : pas d'image directe -> on prend la 1re frame de la video.
        import imageio.v3 as iio
        video_url = data.get("results", [None])[0]
        if not video_url:
            raise RuntimeError("Aucune image ni video renvoyee par Seedance.")
        raw = _download_bytes(video_url)
        tmp = out_path + ".tmp.mp4"
        with open(tmp, "wb") as f:
            f.write(raw)
        frame = iio.imread(tmp, index=0)
        os.remove(tmp)
        img = Image.fromarray(frame).convert("RGB")

    img = _crop_4_5(img)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "JPEG", quality=88)
    return out_path, img.size


def _download_bytes(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def _crop_4_5(img):
    """Recadre l'image au format 4:5 (portrait), centre."""
    w, h = img.size
    target = 4 / 5
    if w / h > target:            # trop large -> on coupe les cotes
        new_w = int(h * target)
        left = (w - new_w) // 2
        return img.crop((left, 0, left + new_w, h))
    else:                          # trop haut -> on coupe haut/bas
        new_h = int(w / target)
        top = (h - new_h) // 2
        return img.crop((0, top, w, top + new_h))


# --------------------------------------------------------------------------
# Point d'entree
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Photo de fond Seedance (via video).")
    ap.add_argument("--brand", required=True, choices=["guestlucky", "lesousloueur"])
    ap.add_argument("--dry-run", action="store_true",
                    help="Prepare la commande SANS l'envoyer (0 credit).")
    ap.add_argument("--go", action="store_true",
                    help="Lance la vraie generation (DEPENSE des credits).")
    ap.add_argument("--resolution", default=DEFAULT_RESOLUTION)
    ap.add_argument("--aspect", default=DEFAULT_ASPECT)
    args = ap.parse_args()

    payload = build_payload(args.brand, args.aspect, args.resolution)

    if not args.go or args.dry_run:
        print("=== MODE A BLANC (aucun credit depense) ===")
        print("Marque    :", args.brand)
        print("Endpoint  : POST", BASE + GEN_ENDPOINT)
        print("Reglages  : aspect", args.aspect, "| resolution", args.resolution,
              "| return_last_frame True | audio False")
        print("Prompt    :")
        print("  " + payload["input"]["prompt"])
        print()
        print("Pour lancer pour de vrai : ajoute --go")
        return

    print("=== GENERATION REELLE (credits) -- marque:", args.brand, "===")
    print("[1/3] Envoi de la commande a Seedance...")
    task_id, credits = create_task(payload)
    print("      taskId :", task_id, "| credits reserves :", credits)

    print("[2/3] Attente du rendu...")
    result = wait_for_result(task_id)

    print("[3/3] Recuperation de l'image de fond...")
    out_path = os.path.join(BACKGROUNDS_DIR, args.brand + "_bg.jpg")
    path, size = download_background(result, out_path)
    print("      Image sauvee :", path, "| taille", size[0], "x", size[1])
    print("Termine.")


if __name__ == "__main__":
    sys.exit(main())
