#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rend les slides HTML d'un carrousel en PNG HD (3240x4050) + JPEG Metricool-ready
(1080x1350, sans EXIF/ICC). Verifie aussi le debordement de chaque slide.

Usage : python3 render.py <slug>
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]


def find_chrome():
    """Trouve le Chromium fourni par l'environnement.

    Le numero de build (chromium-1194) change quand l'image est mise a jour,
    et il ne correspond pas forcement a la version de playwright installee par
    pip : on cherche donc le binaire au lieu de coder le chemin en dur.
    Ne JAMAIS lancer `playwright install` (le reseau bloque le telechargement).
    """
    for pat in ("chromium-*/chrome-linux/chrome", "chromium/chrome-linux/chrome"):
        found = sorted(pathlib.Path("/opt/pw-browsers").glob(pat))
        if found:
            return str(found[-1])          # le build le plus recent
    return None                            # laisse playwright se debrouiller


CHROME = find_chrome()

def render(slug):
    out = ROOT / "output" / slug
    html_dir = out / "html"
    png_dir = out / "png"
    jpg_dir = out / "jpg"
    png_dir.mkdir(parents=True, exist_ok=True)
    jpg_dir.mkdir(parents=True, exist_ok=True)
    htmls = sorted(html_dir.glob("slide_*.html"))
    assert htmls, f"aucune slide dans {html_dir}"

    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": CHROME} if CHROME else {}))
        pg = b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=3)
        for h in htmls:
            pg.goto(h.as_uri())
            pg.wait_for_function("document.fonts.ready.then(()=>true)")
            pg.wait_for_function("document.fonts.check('900 80px Montserrat')")
            pg.wait_for_timeout(250)
            # controle debordement
            over = pg.evaluate("""() => {
                const s = document.querySelector('.slide');
                const bad = [];
                document.querySelectorAll('.pad *').forEach(el => {
                    const r = el.getBoundingClientRect();
                    if (r.bottom > 1350 - 40 || r.right > 1080 || r.left < 0) bad.push(el.className||el.tagName);
                });
                return {scroll: s.scrollHeight, client: s.clientHeight, bad};
            }""")
            flag = "  DEBORDEMENT" if (over["scroll"] > over["client"]+2 or over["bad"]) else "  ok"
            print(f"{h.name}: scroll={over['scroll']} client={over['client']} bad={over['bad'][:4]}{flag}")
            png = png_dir / (h.stem + ".png")
            pg.screenshot(path=str(png), clip={"x":0,"y":0,"width":1080,"height":1350})
        b.close()

    # JPEG Metricool-ready : 1080x1350, sans metadonnees
    for png in sorted(png_dir.glob("slide_*.png")):
        im = Image.open(png).convert("RGB").resize((1080,1350), Image.LANCZOS)
        clean = Image.new("RGB", im.size)
        clean.putdata(list(im.getdata()))
        jpg = jpg_dir / (png.stem + ".jpg")
        clean.save(jpg, "JPEG", quality=88, optimize=True, progressive=False, subsampling=2)
    print(f"PNG dans {png_dir}\nJPEG dans {jpg_dir}")

if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "gl_demo_messagerie_ia")
