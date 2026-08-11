#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anime le post GuestLucky en une petite video verticale pour Instagram.

L'information apparait par etapes (accroche, puis le produit, puis le
rendez-vous), avec un leger mouvement de camera et la musique de fond.

Usage : python3 video_post.py
"""
import sys, pathlib
import numpy as np
import av
from PIL import Image
from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
SORTIE = ICI / "output" / "video"
ETAPES = ICI / "output" / "etapes"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
L, H, FPS = 1080, 1920, 24

# on reutilise la musique ecrite pour Lucky Conciergerie
sys.path.insert(0, str(ICI.parent / "lucky_conciergerie" / "video"))
import musique as compo

# (nom, elements masques, duree a l'ecran)
SEQUENCE = [
    ("etape1", [".facture", ".rdv", ".url"], 3.2),
    ("etape2", [".rdv", ".url"], 3.4),
    ("etape3", [], 5.4),
]
FONDU = 0.55        # duree du fondu enchaine entre deux etapes


def capturer():
    ETAPES.mkdir(parents=True, exist_ok=True)
    page_html = (ICI / "html" / "facturx_story.html").as_uri()
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=CHROME)
        page = nav.new_page(viewport={"width": L, "height": H}, device_scale_factor=2)
        page.goto(page_html)
        page.evaluate("document.fonts.load('800 92px Inter')")
        page.wait_for_function("document.fonts.check('800 92px Inter')")
        page.wait_for_function(
            "Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
        for nom, masques, _ in SEQUENCE:
            page.evaluate("""(masques) => {
                document.querySelectorAll('.facture, .rdv, .url')
                        .forEach(el => el.style.visibility = 'visible');
                masques.forEach(s => document.querySelectorAll(s)
                        .forEach(el => el.style.visibility = 'hidden'));
            }""", masques)
            page.wait_for_timeout(120)
            page.screenshot(path=str(ETAPES / f"{nom}.png"),
                            clip={"x": 0, "y": 0, "width": L, "height": H})
        nav.close()
    print(f"{len(SEQUENCE)} etapes capturees")


def cadre(image_large, avance):
    """Fenetre 9:16 qui se resserre doucement : donne du mouvement sans
    jamais mordre sur les textes, qui restent loin des bords."""
    bw, bh = image_large.size
    k = 1.045 - 0.045 * avance                 # de legerement large a la taille exacte
    cw, ch = L * k, H * k
    x, y = (bw - cw) / 2, (bh - ch) / 2
    return image_large.resize((L, H), Image.LANCZOS, box=(x, y, x + cw, y + ch))


def monter():
    SORTIE.mkdir(parents=True, exist_ok=True)
    dest = SORTIE / "guestlucky_facturx_story.mp4"

    larges = {}
    for nom, _, _ in SEQUENCE:
        im = Image.open(ETAPES / f"{nom}.png").convert("RGB")
        larges[nom] = im.resize((int(L * 1.05), int(H * 1.05)), Image.LANCZOS)

    conteneur = av.open(str(dest), "w")
    flux = conteneur.add_stream("libx264", rate=FPS)
    flux.width, flux.height, flux.pix_fmt = L, H, "yuv420p"
    flux.options = {"crf": "19", "preset": "medium", "profile": "high"}
    flux_audio = conteneur.add_stream("aac", rate=compo.SR)
    flux_audio.bit_rate = 128000

    total = 0
    n_fondu = int(FONDU * FPS)
    for idx, (nom, _, duree) in enumerate(SEQUENCE):
        n = int(round(duree * FPS))
        precedent = SEQUENCE[idx - 1][0] if idx else None
        for i in range(n):
            avance = (total / FPS) / sum(d for *_, d in SEQUENCE)
            img = cadre(larges[nom], avance)
            if precedent and i < n_fondu:      # fondu enchaine depuis l'etape d'avant
                img = Image.blend(cadre(larges[precedent], avance), img,
                                  (i + 1) / n_fondu)
            for paquet in flux.encode(av.VideoFrame.from_image(img)):
                conteneur.mux(paquet)
            total += 1

    for paquet in flux.encode(None):
        conteneur.mux(paquet)

    duree_totale = total / FPS
    piste = compo.composer(duree_totale) * 0.5
    stereo = np.vstack([piste, piste]).astype("float32")
    taille, pts = 1024, 0
    for debut in range(0, stereo.shape[1], taille):
        bloc = stereo[:, debut:debut + taille]
        if bloc.shape[1] < taille:
            bloc = np.pad(bloc, ((0, 0), (0, taille - bloc.shape[1])))
        frame = av.AudioFrame.from_ndarray(np.ascontiguousarray(bloc),
                                           format="fltp", layout="stereo")
        frame.rate, frame.pts = compo.SR, pts
        pts += taille
        for paquet in flux_audio.encode(frame):
            conteneur.mux(paquet)
    for paquet in flux_audio.encode(None):
        conteneur.mux(paquet)

    conteneur.close()
    print(f"OK {dest.name} — {duree_totale:.1f} s, {dest.stat().st_size // 1024} Ko")


if __name__ == "__main__":
    capturer()
    monter()
