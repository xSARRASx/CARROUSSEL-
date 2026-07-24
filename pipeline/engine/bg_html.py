#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bg_html.py -- Fonds de slides dessines en HTML/CSS puis rendus net via Playwright.

Gratuit, automatique, 0 credit, 0 cle. Bien plus riche qu'un simple degrade :
degrades "mesh", grille tech, aurora, grain SVG, vignette. Rendu 3240x4050 (x3).

Styles dispo : mesh | grid | aurora
Usage :
    python3 pipeline/engine/bg_html.py --brand guestlucky --style mesh
    python3 pipeline/engine/bg_html.py --all      # genere tout (2 marques x 3 styles)
"""

import argparse
import os
import pathlib
import tempfile

from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
BG_DIR = ROOT / "assets" / "backgrounds"

# Palettes (charte mise en page, PARTIE C).
BRANDS = {
    "guestlucky": {
        "navy": "#0a0e27", "deep": "#05060f",
        "a": "#7c3aed", "b": "#ec4899", "c": "#5b21b6",
    },
    "lesousloueur": {
        "navy": "#0d1b2e", "deep": "#081320",
        "a": "#E8561F", "b": "#2086C8", "c": "#E8561F",
    },
}

# Grain photo : bruit SVG (feTurbulence), pose en overlay tres discret.
GRAIN = (
    "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
    "width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence "
    "type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E"
    "%3Crect width='100%25' height='100%25' filter='url(%23n)' "
    "opacity='0.5'/%3E%3C/svg%3E\")"
)


def css_background(brand, style):
    c = BRANDS[brand]
    if style == "mesh":
        # Plusieurs halos doux fondus (facon Stripe / Linear).
        return f"""
        background:
          radial-gradient(60% 45% at 28% 82%, {c['a']}66 0%, transparent 60%),
          radial-gradient(55% 40% at 82% 70%, {c['b']}44 0%, transparent 62%),
          radial-gradient(50% 40% at 60% 100%, {c['c']}55 0%, transparent 65%),
          linear-gradient(180deg, {c['deep']} 0%, {c['navy']} 100%);
        """
    if style == "grid":
        # Navy + grille "blueprint" fine + un halo de marque.
        return f"""
        background:
          radial-gradient(55% 45% at 30% 88%, {c['a']}55 0%, transparent 60%),
          linear-gradient(180deg, {c['deep']} 0%, {c['navy']} 100%);
        """
    if style == "aurora":
        # Bandes diagonales douces facon aurore, en bas.
        return f"""
        background:
          linear-gradient(125deg, transparent 45%, {c['a']}44 62%, transparent 78%),
          linear-gradient(125deg, transparent 55%, {c['b']}3a 72%, transparent 88%),
          radial-gradient(70% 50% at 50% 108%, {c['c']}66 0%, transparent 60%),
          linear-gradient(180deg, {c['deep']} 0%, {c['navy']} 100%);
        """
    raise ValueError("style inconnu : " + style)


def html_for(brand, style):
    bg = css_background(brand, style)
    grid_layer = ""
    if style == "grid":
        grid_layer = f"""
        .grid {{
          position:absolute; inset:0;
          background-image:
            linear-gradient(rgba(255,255,255,.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,.05) 1px, transparent 1px);
          background-size: 90px 90px;
          -webkit-mask-image: radial-gradient(75% 70% at 50% 60%, #000 30%, transparent 82%);
                  mask-image: radial-gradient(75% 70% at 50% 60%, #000 30%, transparent 82%);
        }}"""
    grid_div = '<div class="grid"></div>' if style == "grid" else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      .bg {{ position:relative; width:1080px; height:1350px; overflow:hidden; {bg} }}
      {grid_layer}
      /* grain photo subtil */
      .grain {{ position:absolute; inset:0; background-image:{GRAIN};
                background-size:240px 240px; opacity:.05; mix-blend-mode:overlay; }}
      /* vignette : assombrit haut + bords pour la lisibilite du texte */
      .vig {{ position:absolute; inset:0; background:
              radial-gradient(80% 75% at 50% 62%, transparent 40%, rgba(0,0,0,.45) 100%),
              linear-gradient(180deg, rgba(0,0,0,.35) 0%, transparent 30%); }}
    </style></head><body>
      <div class="bg">{grid_div}<div class="grain"></div><div class="vig"></div></div>
    </body></html>"""


def render_one(brand, style, page):
    html = html_for(brand, style)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        path = f.name
    page.goto(pathlib.Path(path).as_uri())
    page.wait_for_timeout(200)
    BG_DIR.mkdir(parents=True, exist_ok=True)
    out_png = BG_DIR / f"{brand}_html_{style}.png"
    page.screenshot(path=str(out_png), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
    os.remove(path)
    # JPEG aussi (leger, pratique a montrer)
    im = Image.open(out_png).convert("RGB")
    out_jpg = BG_DIR / f"{brand}_html_{style}.jpg"
    im.save(out_jpg, "JPEG", quality=90)
    return out_jpg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", choices=list(BRANDS))
    ap.add_argument("--style", choices=["mesh", "grid", "aurora"])
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    jobs = []
    if args.all:
        for b in BRANDS:
            for s in ["mesh", "grid", "aurora"]:
                jobs.append((b, s))
    else:
        jobs.append((args.brand or "guestlucky", args.style or "mesh"))

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=3)
        for b, s in jobs:
            out = render_one(b, s, page)
            print("Fond rendu :", out)
        browser.close()


if __name__ == "__main__":
    main()
