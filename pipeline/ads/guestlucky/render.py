#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rend les posts GuestLucky : HTML -> PNG haute definition -> JPG aux dimensions
exactes attendues par Instagram. Signale tout debordement de texte.

Usage : python3 render.py [motif]
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SCALE = 2

FORMATS = {
    "portrait": (1080, 1350),   # le format qui occupe le plus de place dans le fil
    "carre":    (1080, 1080),
    "story":    (1080, 1920),
}


def format_de(nom):
    for f in FORMATS:
        if nom.endswith("_" + f):
            return f
    raise SystemExit(f"format introuvable dans le nom : {nom}")


def render(motif=""):
    png_dir, jpg_dir = ROOT / "output" / "png", ROOT / "output" / "jpg"
    png_dir.mkdir(parents=True, exist_ok=True)
    jpg_dir.mkdir(parents=True, exist_ok=True)

    pages = sorted(p for p in (ROOT / "html").glob("*.html") if motif in p.stem)
    if not pages:
        raise SystemExit(f"aucun post ne correspond a '{motif}'")

    soucis = []
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=CHROME)
        for f in pages:
            w, h = FORMATS[format_de(f.stem)]
            page = nav.new_page(viewport={"width": w, "height": h}, device_scale_factor=SCALE)
            page.goto(f.as_uri())
            page.evaluate("document.fonts.load('800 82px Inter')")
            page.wait_for_function("document.fonts.check('800 82px Inter')")
            page.wait_for_function(
                "Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
            page.wait_for_timeout(200)

            controle = page.evaluate("""([w, h]) => {
                const post = document.querySelector('.post');
                const dehors = [];
                post.querySelectorAll('.pad *').forEach(el => {
                    if (el.tagName === 'svg' || el.closest('svg')) return;
                    const r = el.getBoundingClientRect();
                    if (r.height === 0) return;
                    if (r.bottom > h + 1 || r.right > w + 1 || r.left < -1 || r.top < -1)
                        dehors.push(el.className || el.tagName);
                });
                const tronques = [];
                post.querySelectorAll('.titre, .sous, .rdv-val, .f-total-val, .badge')
                    .forEach(el => {
                        const marge = Math.max(8, el.clientHeight * 0.25);
                        if (el.scrollHeight > el.clientHeight + marge ||
                            el.scrollWidth > el.clientWidth + 6) tronques.push(el.className);
                    });
                return {dehors, tronques};
            }""", [w, h])

            page.screenshot(path=str(png_dir / f"{f.stem}.png"),
                            clip={"x": 0, "y": 0, "width": w, "height": h})
            page.close()

            pb = controle["dehors"][:3] + controle["tronques"][:3]
            print(f"{f.stem:26s} {w}x{h}" + ("  ATTENTION " + " | ".join(pb) if pb else "  ok"))
            if pb:
                soucis.append(f.stem)
        nav.close()

    for png in sorted(png_dir.glob("*.png")):
        if motif and motif not in png.stem:
            continue
        w, h = FORMATS[format_de(png.stem)]
        im = Image.open(png).convert("RGB").resize((w, h), Image.LANCZOS)
        propre = Image.new("RGB", im.size)
        propre.putdata(list(im.getdata()))
        propre.save(jpg_dir / f"{png.stem}.jpg", "JPEG", quality=93,
                    optimize=True, progressive=False, subsampling=1)

    print(f"\nPNG : {png_dir}\nJPG : {jpg_dir}")
    print("A REVOIR : " + ", ".join(soucis) if soucis else "\nTous les posts sont propres.")


if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "")
