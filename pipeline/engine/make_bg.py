#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_bg.py -- Fonds "design" generes par code (gratuit, automatique, 0 credit).

Alternative a Seedance/Google : au lieu d'une VRAIE photo IA, on dessine un fond
premium sobre (degrade navy + halo de la couleur de marque + grain + vignette).
Parfait comme fond a ~50% derriere le texte des slides.

Palettes (charte mise en page, PARTIE C du carroussel.md) :
  - Guestlucky   : navy #0a0e27, violet #7c3aed, magenta #ec4899
  - Le Sous Loueur: navy #0d1b2e, orange #E8561F, bleu #2086C8

Usage :
    python3 pipeline/engine/make_bg.py --brand guestlucky
    python3 pipeline/engine/make_bg.py --brand lesousloueur --variant 2
"""

import argparse
import math
import os

import numpy as np
from PIL import Image, ImageFilter

W, H = 1080, 1350  # format slide 4:5

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
BG_DIR = os.path.join(REPO_ROOT, "pipeline", "assets", "backgrounds")

BRANDS = {
    "guestlucky": {
        "top": (8, 11, 30),        # navy tres fonce (#080b1e)
        "bottom": (16, 22, 55),    # navy un peu plus clair
        "glow1": (124, 58, 237),   # violet #7c3aed
        "glow2": (236, 72, 153),   # magenta #ec4899
    },
    "lesousloueur": {
        "top": (10, 20, 34),       # navy #0a1422
        "bottom": (18, 34, 58),    # navy plus clair
        "glow1": (232, 86, 31),    # orange #E8561F
        "glow2": (32, 134, 200),   # bleu #2086C8
    },
}


def _hex(c):
    return "#%02x%02x%02x" % c


def vertical_gradient(top, bottom):
    """Degrade vertical haut (sombre) -> bas (un peu plus clair)."""
    t = np.linspace(0, 1, H)[:, None]
    grad = np.zeros((H, W, 3), np.float32)
    for i in range(3):
        grad[:, :, i] = (top[i] * (1 - t) + bottom[i] * t)
    return grad


def radial_glow(cx, cy, radius, color, strength):
    """Halo lumineux doux, centre (cx, cy), rayon en pixels."""
    ys, xs = np.mgrid[0:H, 0:W]
    dist = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    falloff = np.clip(1 - dist / radius, 0, 1) ** 2  # doux sur les bords
    glow = np.zeros((H, W, 3), np.float32)
    for i in range(3):
        glow[:, :, i] = color[i] * falloff * strength
    return glow


def add_grain(img, amount=6.0):
    """Grain photo subtil (bruit gaussien)."""
    noise = np.random.normal(0, amount, (H, W, 1)).astype(np.float32)
    return img + noise


def vignette(img, strength=0.55):
    """Assombrit les bords + le haut (lisibilite du texte)."""
    ys, xs = np.mgrid[0:H, 0:W]
    cx, cy = W / 2, H * 0.62
    dist = np.sqrt(((xs - cx) / (W * 0.75)) ** 2 + ((ys - cy) / (H * 0.75)) ** 2)
    mask = np.clip(1 - dist * strength, 0.35, 1)[:, :, None]
    return img * mask


def build(brand, variant=1):
    c = BRANDS[brand]
    img = vertical_gradient(c["top"], c["bottom"])

    if variant == 1:
        # 2 halos dans le tiers bas, en diagonale, discrets.
        img += radial_glow(W * 0.30, H * 0.80, W * 0.75, c["glow1"], 0.55)
        img += radial_glow(W * 0.80, H * 0.66, W * 0.60, c["glow2"], 0.30)
    else:
        # variante : un seul halo large centre-bas, plus sobre.
        img += radial_glow(W * 0.55, H * 0.85, W * 0.95, c["glow1"], 0.45)
        img += radial_glow(W * 0.20, H * 0.55, W * 0.45, c["glow2"], 0.16)

    img = vignette(img, 0.5)
    img = add_grain(img, 5.0)
    img = np.clip(img, 0, 255).astype(np.uint8)

    pic = Image.fromarray(img, "RGB")
    # leger flou pour fondre les halos facon photo
    pic = pic.filter(ImageFilter.GaussianBlur(1.2))
    return pic


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True, choices=list(BRANDS))
    ap.add_argument("--variant", type=int, default=1, choices=[1, 2])
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    os.makedirs(BG_DIR, exist_ok=True)
    out = args.out or os.path.join(
        BG_DIR, "%s_design_v%d.jpg" % (args.brand, args.variant))
    pic = build(args.brand, args.variant)
    pic.save(out, "JPEG", quality=90)
    print("Fond genere :", out, "|", pic.size)


if __name__ == "__main__":
    main()
