#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rend les stories HTML (1080x1920) en PNG HD (2160x3840) puis JPEG pret a poster
(1080x1920, sans metadonnees). Verifie le debordement de chaque story et le
respect des zones libres Instagram (haut 240px / bas 360px).

Usage : python3 render_stories.py <slug>       (defaut : semaine-01)
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 1080, 1920
TOP_SAFE, BOTTOM_SAFE = 240, 360

def render(slug):
    out = ROOT / "output" / slug
    html_dir = out / "html"
    png_dir = out / "png"; png_dir.mkdir(parents=True, exist_ok=True)
    jpg_dir = out / "jpg"; jpg_dir.mkdir(parents=True, exist_ok=True)
    htmls = sorted(html_dir.glob("*.html"))
    assert htmls, f"aucune story dans {html_dir}"

    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for h in htmls:
            pg.goto(h.as_uri())
            pg.wait_for_function("document.fonts.ready.then(()=>true)")
            pg.wait_for_timeout(350)
            over = pg.evaluate(f"""() => {{
                const s = document.querySelector('.story');
                const bad = [];
                document.querySelectorAll('.pad *, .bpad *').forEach(el => {{
                    const r = el.getBoundingClientRect();
                    if (r.bottom > {H - BOTTOM_SAFE + 20} || r.top < {TOP_SAFE - 20} ||
                        r.right > {W} || r.left < 0) bad.push(el.className||el.tagName);
                }});
                return {{scroll: s.scrollHeight, client: s.clientHeight, bad}};
            }}""")
            flag = "  HORS ZONE" if (over["scroll"] > over["client"] + 2 or over["bad"]) else "  ok"
            print(f"{h.stem}: {flag}  {over['bad'][:4] if over['bad'] else ''}")
            pg.screenshot(path=str(png_dir / (h.stem + ".png")),
                          clip={"x": 0, "y": 0, "width": W, "height": H})
        b.close()

    for png in sorted(png_dir.glob("*.png")):
        im = Image.open(png).convert("RGB").resize((W, H), Image.LANCZOS)
        clean = Image.new("RGB", im.size)
        clean.putdata(list(im.getdata()))
        clean.save(jpg_dir / (png.stem + ".jpg"), "JPEG",
                   quality=90, optimize=True, progressive=False, subsampling=2)
    print(f"PNG dans {png_dir}\nJPEG prets a poster dans {jpg_dir}")

if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "semaine-01")
