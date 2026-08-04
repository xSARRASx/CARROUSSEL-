#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLANCHES DE COMPARAISON pour Martin : version actuelle (icone flat) contre
version 2 (photo reelle facon packshot studio).

Martin regarde depuis son telephone : une planche par sujet, gros titres,
etiquettes claires. Il repond ensuite si on bascule ou pas.

Usage : python3 build_comparatif.py
"""
import base64, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
FONTS = REPO / "pipeline" / "assets" / "fonts"
KIT = ROOT / "assets-montage"
TEST = ROOT / "test-realiste"
OUT_HTML = ROOT / "comparatif" / "html"
OUT_PNG = ROOT / "comparatif"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 1080, 1350

NAVY = "#0d1b2e"
GRIS = "#7b8794"

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

def font_face(w):
    d = b64(FONTS / f"montserrat-latin-{w}-normal.woff2", "font/woff2")
    return (f"@font-face{{font-family:'Mont';font-style:normal;font-weight:{w};"
            f"font-display:block;src:url({d}) format('woff2');}}")

CSS = f"""
{''.join(font_face(w) for w in (500, 700, 800))}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Mont',sans-serif;
   -webkit-font-smoothing:antialiased;}}
.p{{width:{W}px;height:{H}px;background:#fff;padding:54px 48px;display:flex;
   flex-direction:column;}}
.titre{{font-weight:800;font-size:52px;color:{NAVY};text-align:center;}}
.sstitre{{font-weight:500;font-size:30px;color:{GRIS};text-align:center;margin-top:14px;}}
.duo{{flex:1;display:flex;gap:28px;align-items:stretch;margin-top:40px;}}
.col{{flex:1;display:flex;flex-direction:column;}}
.et{{font-weight:800;font-size:30px;text-align:center;padding:16px 0;border-radius:14px;
    letter-spacing:1px;}}
.et.a{{background:#EEF1F5;color:{GRIS};}}
.et.b{{background:{NAVY};color:#fff;}}
.img{{flex:1;margin-top:18px;border:2px solid #E4E9EE;border-radius:18px;
     background-size:contain;background-position:center;background-repeat:no-repeat;
     background-color:#fff;}}
.nom{{font-weight:700;font-size:27px;color:{NAVY};text-align:center;margin-top:16px;}}
"""

# (sujet affiche, fichier v1 du kit) ; la v2 est le meme nom avec "-2" avant .png
SUJETS = [
    ("Le ménage", "icone-menage.png"),
    ("La serrure connectée", "icone-serrure.png"),
    ("Le linge", "icone-linge.png"),
    ("Le check-in autonome", "icone-checkin.png"),
    ("Le jacuzzi", "icone-jacuzzi.png"),
    ("Le cashflow", "icone-cashflow.png"),
    ("La poignée de main", "icone-proprietaire.png"),
    ("Le calendrier des saisons", "icone-saisonnalite.png"),
]

def v2_de(v1):
    return v1.replace(".png", "-2.png")

def planche(titre, v1, v2, nom2):
    a = b64(KIT / v1, "image/png")
    b = b64(KIT / v2, "image/png")
    return f"""<div class="p">
  <div class="titre">{titre}</div>
  <div class="sstitre">Laquelle tu préfères&nbsp;?</div>
  <div class="duo">
    <div class="col"><div class="et a">ACTUEL</div>
      <div class="img" style="background-image:url({a});"></div>
      <div class="nom">{v1}</div></div>
    <div class="col"><div class="et b">VERSION&nbsp;2</div>
      <div class="img" style="background-image:url({b});"></div>
      <div class="nom">{nom2}</div></div>
  </div>
</div>"""

def main():
    OUT_HTML.mkdir(parents=True, exist_ok=True)
    faits = []
    for titre, v1 in SUJETS:
        v2 = v2_de(v1)
        if not (KIT / v1).exists() or not (KIT / v2).exists():
            print(f"  saute {titre} (image manquante)")
            continue
        slug = v2.replace(".png", "")
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{CSS}</style></head><body>{planche(titre, v1, v2, v2)}</body></html>')
        (OUT_HTML / f"comparatif-{slug}.html").write_text(html, encoding="utf-8")
        faits.append(slug)
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=CHROME)
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for slug in faits:
            pg.goto((OUT_HTML / f"comparatif-{slug}.html").as_uri())
            pg.wait_for_function("document.fonts.ready.then(()=>true)")
            pg.wait_for_timeout(250)
            tmp = OUT_PNG / f"{slug}.raw.png"
            pg.screenshot(path=str(tmp), clip={"x": 0, "y": 0, "width": W, "height": H})
            im = Image.open(tmp).convert("RGB").resize((W, H), Image.LANCZOS)
            im.save(OUT_PNG / f"comparatif-{slug}.jpg", "JPEG", quality=92, optimize=True)
            tmp.unlink()
            print(f"comparatif-{slug}.jpg")
        br.close()

if __name__ == "__main__":
    main()
