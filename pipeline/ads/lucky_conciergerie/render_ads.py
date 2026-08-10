#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rend les visuels publicitaires Lucky Conciergerie : HTML -> PNG haute definition
-> JPG aux dimensions exactes attendues par les regies (Meta, Google).

Controle aussi le debordement : un texte qui sort du cadre est signale.

Usage : python3 render_ads.py [motif]
        python3 render_ads.py            -> tout
        python3 render_ads.py A_reseau   -> seulement le concept A
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SCALE = 2  # rendu x2 puis reduction = texte parfaitement net

FORMATS = {
    "story":   (1080, 1920),
    "carre":   (1080, 1080),
    "paysage": (1200, 628),
}


def format_de(nom):
    for f in FORMATS:
        if nom.endswith("_" + f):
            return f
    raise SystemExit(f"format introuvable dans le nom : {nom}")


def render(motif=""):
    html_dir = ROOT / "html"
    png_dir = ROOT / "output" / "png"
    jpg_dir = ROOT / "output" / "jpg"
    png_dir.mkdir(parents=True, exist_ok=True)
    jpg_dir.mkdir(parents=True, exist_ok=True)

    pages = sorted(p for p in html_dir.glob("*.html") if motif in p.stem)
    if not pages:
        raise SystemExit(f"aucun visuel ne correspond a '{motif}'")

    soucis = []
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=CHROME)
        for page_file in pages:
            fmt = format_de(page_file.stem)
            w, h = FORMATS[fmt]
            page = nav.new_page(viewport={"width": w, "height": h},
                                device_scale_factor=SCALE)
            page.goto(page_file.as_uri())
            page.wait_for_function("document.fonts.ready.then(() => true)")
            page.wait_for_function("document.fonts.check('800 80px Manrope')")
            page.wait_for_function(
                "Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
            page.wait_for_timeout(220)

            controle = page.evaluate("""([w, h]) => {
                const ad = document.querySelector('.ad');
                const debordent = [];
                ad.querySelectorAll('.pad *, .col-txt *, .col-gauche *, .col-droite *')
                  .forEach(el => {
                    if (el.tagName === 'svg' || el.closest('svg')) return;
                    const r = el.getBoundingClientRect();
                    if (r.height === 0) return;
                    if (r.bottom > h + 1 || r.right > w + 1 || r.left < -1 || r.top < -1) {
                        debordent.push((el.className || el.tagName) + ' [' +
                            Math.round(r.left) + ',' + Math.round(r.top) + ' -> ' +
                            Math.round(r.right) + ',' + Math.round(r.bottom) + ']');
                    }
                  });
                // du texte tronque par un conteneur trop petit ?
                // tolerance proportionnelle : un line-height serre (titres) fait
                // naturellement depasser le scrollHeight de quelques pixels sans
                // que rien ne soit reellement coupe
                const tronques = [];
                ad.querySelectorAll('.titre, .sous, .puce-txt, .cta, .col-titre, .stat-l')
                  .forEach(el => {
                    const marge = Math.max(6, el.clientHeight * 0.10);
                    if (el.scrollHeight > el.clientHeight + marge ||
                        el.scrollWidth > el.clientWidth + 6) {
                        tronques.push(el.className);
                    }
                  });
                return {debordent, tronques, hauteur: ad.scrollHeight};
            }""", [w, h])

            png = png_dir / f"{page_file.stem}.png"
            page.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": w, "height": h})
            page.close()

            pb = controle["debordent"][:3] + controle["tronques"][:3]
            etat = "  ATTENTION " + " | ".join(pb) if pb else "  ok"
            print(f"{page_file.stem:28s} {fmt:8s} {w}x{h}{etat}")
            if pb:
                soucis.append(page_file.stem)
        nav.close()

    # JPG aux dimensions exactes, sans metadonnees (pret pour les regies pub)
    for png in sorted(png_dir.glob("*.png")):
        if motif and motif not in png.stem:
            continue
        w, h = FORMATS[format_de(png.stem)]
        im = Image.open(png).convert("RGB").resize((w, h), Image.LANCZOS)
        propre = Image.new("RGB", im.size)
        propre.putdata(list(im.getdata()))
        propre.save(jpg_dir / f"{png.stem}.jpg", "JPEG",
                    quality=92, optimize=True, progressive=False, subsampling=1)

    print(f"\nPNG (haute def) : {png_dir}\nJPG (pour la pub) : {jpg_dir}")
    if soucis:
        print("\nA REVOIR : " + ", ".join(soucis))
    else:
        print("\nAucun debordement, tous les visuels sont propres.")


if __name__ == "__main__":
    render(sys.argv[1] if len(sys.argv) > 1 else "")
