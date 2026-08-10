#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monte les videos publicitaires Lucky Conciergerie a partir des clips Veo.

- incruste les sous-titres en dur (85 % des vues se font sans le son)
- ajoute le carton final de marque
- exporte un MP4 9:16 en 1080x1920

Usage : python3 monter.py [v1|v2|tout]
"""
import sys, pathlib, av
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ICI = pathlib.Path(__file__).resolve().parent
CLIPS = ICI / "clips"
TAMPON = ICI / "overlays"
SORTIE = ICI / "final"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
L, H, FPS = 1080, 1920, 24

# (clip, duree affichee, texte incruste, texte plus petit ?)
STORYBOARDS = {
    "v1": {
        "titre": "Le dimanche soir",
        "plans": [
            ("v1_p1", 3.0, "<em>21h47.</em><br>Encore un message.", False),
            ("v1_p2", 3.0, "Draps à laver.<br>Ménage à faire.", False),
            ("v1_p3", 3.0, "Et si quelqu'un<br>s'en occupait&nbsp;?", False),
            ("v1_p4", 5.0, "Une <em>conciergerie certifiée</em>,<br>près de chez vous.", False),
            ("v1_p5", 5.0, "Vous, vous ne faites<br><em>plus rien.</em>", False),
            ("v1_p6", 5.0, "Annonce optimisée<br>Tarifs ajustés<br>Voyageurs pris en charge", True),
        ],
        "carton": 6.0,
        # version courte : accroche, preuve, carton (brief section 10)
        "court": ["v1_p1", "v1_p4", "v1_p6"],
    },
    "v2": {
        "titre": "Toutes les conciergeries ne se valent pas",
        "plans": [
            ("v2_p1", 4.0, "Votre conciergerie vous fait-elle vraiment <em>gagner de l'argent&nbsp;?</em>", True),
            ("v2_p2", 6.0, "Des nuits vides.<br>Une commission quand même.", False),
            ("v2_p3", 6.0, "Toutes les conciergeries<br><em>ne se valent pas.</em>", False),
            # le plan 4 (checklist) a bute sur le quota Veo : son message
            # (selection, certification) est deja porte par le carton final
        ],
        "carton": 6.0,
        "court": ["v2_p1", "v2_p3"],
    },
}


def fabriquer_images(page, cles):
    """Rend un PNG transparent par sous-titre + le carton final."""
    TAMPON.mkdir(parents=True, exist_ok=True)
    page.goto((ICI / "overlay.html").as_uri())
    # le conteneur de texte est vide au chargement : sans demande explicite,
    # la police ne serait jamais activee et l'attente tournerait dans le vide
    page.evaluate("document.fonts.load('800 82px Manrope')")
    page.wait_for_function("document.fonts.check('800 82px Manrope')")
    for cle in cles:
        for i, (clip, _, texte, petit) in enumerate(STORYBOARDS[cle]["plans"]):
            page.evaluate("""([t, p]) => {
                const el = document.getElementById('txt');
                el.innerHTML = t;
                el.classList.toggle('petit', p);
            }""", [texte, petit])
            page.wait_for_timeout(90)
            page.screenshot(path=str(TAMPON / f"{clip}.png"), omit_background=True)

    page.goto((ICI / "carton_final.html").as_uri())
    page.evaluate("document.fonts.load('800 62px Manrope')")
    page.wait_for_function("document.fonts.check('800 62px Manrope')")
    page.wait_for_function(
        "Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
    page.wait_for_timeout(150)
    page.screenshot(path=str(TAMPON / "carton.png"))


def bandes_noires(img):
    """Hauteur des bandes noires en haut et en bas : Veo rend parfois un
    cadrage cinemascope a l'interieur du 9:16 demande."""
    a = np.asarray(img.convert("L"), dtype="float32")
    hauteur = a.shape[0]
    lignes = a.mean(axis=1)
    limite = hauteur // 3
    haut = 0
    while haut < limite and lignes[haut] < 12:
        haut += 1
    bas = 0
    while bas < limite and lignes[hauteur - 1 - bas] < 12:
        bas += 1
    return haut, bas


def recadrer(img, haut, bas):
    """Retire les bandes puis recentre sur le ratio 9:16 sans deformer."""
    larg, haut_tot = img.size
    img = img.crop((0, haut, larg, haut_tot - bas))
    larg, hu = img.size
    vise = L / H
    if larg / hu > vise:                      # trop large : on rogne les cotes
        nl = int(round(hu * vise))
        x = (larg - nl) // 2
        img = img.crop((x, 0, x + nl, hu))
    else:                                     # trop haut : on rogne le haut/bas
        nh = int(round(larg / vise))
        y = (hu - nh) // 2
        img = img.crop((0, y, larg, y + nh))
    return img


def frames_du_clip(chemin, secondes):
    """Rend les images d'un clip, redimensionnees en 1080x1920, bouclees si trop court."""
    voulues = int(round(secondes * FPS))
    brut = []
    with av.open(str(chemin)) as c:
        for f in c.decode(video=0):
            brut.append(f.to_image().convert("RGB"))
            if len(brut) >= voulues:
                break
    if not brut:
        raise SystemExit(f"clip illisible : {chemin}")

    # Une vraie bande noire est presente sur TOUTE la duree du plan. Une scene
    # simplement sombre au demarrage, elle, s'eclaircit : on prend donc le
    # minimum mesure sur plusieurs images, jamais la seule premiere.
    temoins = [brut[i] for i in {0, len(brut) // 3, len(brut) // 2,
                                 2 * len(brut) // 3, len(brut) - 1}]
    mesures = [bandes_noires(t) for t in temoins]
    haut = min(m[0] for m in mesures)
    bas = min(m[1] for m in mesures)
    if haut + bas <= 8:
        haut = bas = 0
    else:
        print(f"    {chemin.stem} : bandes noires {haut}/{bas} px, recadrage")

    sortie = []
    for img in brut:
        if haut or bas:
            img = recadrer(img, haut, bas)
        sortie.append(img.resize((L, H), Image.LANCZOS))
    while len(sortie) < voulues:        # clip plus court que prevu : on tient la derniere image
        sortie.append(sortie[-1])
    return sortie[:voulues]


def monter(cle, court=False):
    board = STORYBOARDS[cle]
    SORTIE.mkdir(parents=True, exist_ok=True)
    suffixe = "_15s" if court else "_30s"
    dest = SORTIE / f"lucky_{cle}{suffixe}_9x16.mp4"

    plans = board["plans"]
    if court:
        gardes = board.get("court", [])
        plans = [p for p in plans if p[0] in gardes]

    manquants = [c for c, *_ in plans if not (CLIPS / f"{c}.mp4").exists()]
    if manquants:
        print(f"  clips manquants pour {cle} : {manquants} — video non montee")
        return None

    conteneur = av.open(str(dest), "w")
    flux = conteneur.add_stream("libx264", rate=FPS)
    flux.width, flux.height, flux.pix_fmt = L, H, "yuv420p"
    flux.options = {"crf": "20", "preset": "medium", "profile": "high"}

    total = 0
    for clip, duree, _, _ in plans:
        images = frames_du_clip(CLIPS / f"{clip}.mp4", duree)
        calque = Image.open(TAMPON / f"{clip}.png").convert("RGBA")
        fondu = int(0.25 * FPS)          # le texte s'installe en 0,25 s
        for i, img in enumerate(images):
            fond = img.convert("RGBA")
            if i < fondu:                # fondu d'entree du sous-titre
                c = calque.copy()
                alpha = c.getchannel("A").point(lambda v, k=(i + 1) / fondu: int(v * k))
                c.putalpha(alpha)
                fond.alpha_composite(c)
            else:
                fond.alpha_composite(calque)
            for paquet in flux.encode(av.VideoFrame.from_image(fond.convert("RGB"))):
                conteneur.mux(paquet)
            total += 1

    carton = Image.open(TAMPON / "carton.png").convert("RGB")
    duree_carton = 4.0 if court else board["carton"]
    for _ in range(int(round(duree_carton * FPS))):
        for paquet in flux.encode(av.VideoFrame.from_image(carton)):
            conteneur.mux(paquet)
        total += 1

    for paquet in flux.encode(None):
        conteneur.mux(paquet)
    conteneur.close()

    print(f"  OK {dest.name} — {total / FPS:.1f} s, {dest.stat().st_size // 1024} Ko")
    return dest


def main():
    quoi = sys.argv[1] if len(sys.argv) > 1 else "tout"
    cles = list(STORYBOARDS) if quoi == "tout" else [quoi]

    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=CHROME)
        page = nav.new_page(viewport={"width": L, "height": H}, device_scale_factor=1)
        fabriquer_images(page, cles)
        nav.close()
    print("Sous-titres et carton final prets.")

    for cle in cles:
        monter(cle, court=False)
        monter(cle, court=True)


if __name__ == "__main__":
    main()
