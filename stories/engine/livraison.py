#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LIVRAISON GITHUB DES STORIES — pour le robot Mac de Martin.

Demande de Martin (06/08/2026) : en plus du zip envoyé dans la conversation
(qu'il transfère à son frère), chaque fournée est poussée dans `livraison/`
au format attendu par son robot Mac, qui vient la chercher tout seul pour
programmer les stories sur Instagram.

FORMAT PRODUIT (aligné sur le robot carrousels déjà en place) :

    livraison/stories-<AAAA-MM-JJ>-<sujet>/
        01.jpg, 02.jpg, 03.jpg ...   <- ORDRE DE PUBLICATION
        description.txt              <- texte associé + mémo de publication

La numérotation EST l'ordre de publication : 01 se poste en premier.

Usage :
    python3 livraison.py <lot> [<lot> ...] --sujet <mot-cle> [--date AAAA-MM-JJ]
        [--video <id>] [--titre "<titre francais>"] [--note "<texte libre>"]
    python3 livraison.py --controle      # contrôle d'intégrité, code 1 si problème

⚠️ Le contrôle est OBLIGATOIRE avant le push. S'il signale un problème, on ne
pousse PAS en silence : on alerte Martin en première ligne.
"""
import argparse, datetime, json, pathlib, shutil, sys
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]     # stories/
REPO = ROOT.parent                                      # CARROUSSEL-/
OUT = ROOT / "output"
LIVRAISON = REPO / "livraison"
REGISTRE = ROOT / "robot" / "traite.json"

W_ATTENDU, H_ATTENDU = 1080, 1920
PREFIXE = "stories-"

# Ordre de diffusion conseillé quand plusieurs lots partent ensemble : les
# séquences d'aide d'abord (elles donnent), les formats interactifs ensuite.
def trier_lots(lots):
    def rang(nom):
        if nom.startswith("banque"):      return 0
        if nom.startswith("semaine"):     return 1
        if nom.startswith("temoignages"): return 3
        return 2                                        # interactifs et autres
    return sorted(lots, key=rang)

def jpgs_du_lot(lot):
    d = OUT / lot / "jpg"
    if not d.is_dir():
        return []
    return sorted(d.glob("*.jpg"))

def livrer(lots, sujet, date, video=None, titre=None, note=None):
    lots = trier_lots(lots)
    fichiers = []
    for lot in lots:
        f = jpgs_du_lot(lot)
        if not f:
            print(f"  ALERTE : le lot '{lot}' ne contient aucun JPEG", flush=True)
        fichiers += f
    if not fichiers:
        print("ECHEC : aucune story à livrer.", flush=True)
        return None

    dossier = LIVRAISON / f"{PREFIXE}{date}-{sujet}"
    if dossier.exists():
        shutil.rmtree(dossier)
    dossier.mkdir(parents=True)

    for i, src in enumerate(fichiers, 1):
        shutil.copy2(src, dossier / f"{i:02d}.jpg")

    lignes = [
        f"Fournée de stories du {date}",
        f"Sujet : {sujet}",
    ]
    if titre:
        lignes.append(f"Vidéo source : {titre}")
    if video:
        lignes.append(f"Identifiant YouTube : {video}")
    lignes += [
        "",
        f"{len(fichiers)} stories, à publier dans l'ordre des numéros (01 en premier).",
        "Format : JPEG 1080x1920, prêtes à poster telles quelles.",
        "",
        "À SAVOIR AVANT DE PROGRAMMER :",
        "- Les stories de type quiz et sondage attendent un sticker de vote Instagram,",
        "  qui ne peut pas être ajouté à une story programmée : celles-là se postent",
        "  à la main. Elles laissent volontairement la moitié basse libre.",
        "- Les stories de témoignage ont un cadre en pointillés : c'est Pierre qui y",
        "  colle son screenshot réel. Elles ne partent jamais en programmation auto.",
    ]
    if note:
        lignes += ["", note]
    lignes += ["", "Détail des lots inclus :"]
    for lot in lots:
        lignes.append(f"- {lot} ({len(jpgs_du_lot(lot))} stories)")

    (dossier / "description.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"Livré : livraison/{dossier.name}  ({len(fichiers)} stories)", flush=True)
    return dossier

def controle():
    """Contrôle d'intégrité. Code de sortie 1 si quoi que ce soit cloche."""
    if not LIVRAISON.is_dir():
        print("ALERTE : le dossier livraison/ n'existe pas.", flush=True)
        return 1
    dossiers = sorted(d for d in LIVRAISON.iterdir()
                      if d.is_dir() and d.name.startswith(PREFIXE))
    if not dossiers:
        print("ALERTE : aucune fournée dans livraison/.", flush=True)
        return 1

    alertes = []
    for d in dossiers:
        images = sorted(d.glob("*.jpg"))
        if not images:
            alertes.append(f"{d.name} : aucune image")
            continue
        if not (d / "description.txt").is_file():
            alertes.append(f"{d.name} : description.txt manquant")
        # numérotation continue, sans trou
        attendus = [f"{i:02d}.jpg" for i in range(1, len(images) + 1)]
        reels = [p.name for p in images]
        if reels != attendus:
            alertes.append(f"{d.name} : numérotation incorrecte "
                           f"(attendu 01..{len(images):02d})")
        for p in images:
            if p.stat().st_size == 0:
                alertes.append(f"{d.name}/{p.name} : fichier vide")
                continue
            try:
                with Image.open(p) as im:
                    if im.size != (W_ATTENDU, H_ATTENDU):
                        alertes.append(f"{d.name}/{p.name} : dimensions {im.size} "
                                       f"au lieu de {W_ATTENDU}x{H_ATTENDU}")
            except Exception as e:
                alertes.append(f"{d.name}/{p.name} : illisible ({e})")
        print(f"OK  {d.name}  ({len(images)} stories)", flush=True)

    if alertes:
        print("\nFOURNEE INCOMPLETE — ne pas pousser en silence :", flush=True)
        for a in alertes:
            print(f"  - {a}", flush=True)
        return 1
    print(f"\nControle OK : {len(dossiers)} fournee(s), rien a signaler.", flush=True)
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lots", nargs="*", help="noms des lots dans stories/output/")
    ap.add_argument("--sujet", help="mot-cle du sujet, en minuscules avec tirets")
    ap.add_argument("--date", help="AAAA-MM-JJ (defaut : aujourd'hui)")
    ap.add_argument("--video", help="identifiant YouTube de la video source")
    ap.add_argument("--titre", help="titre francais de la video")
    ap.add_argument("--note", help="texte libre ajoute a description.txt")
    ap.add_argument("--controle", action="store_true")
    a = ap.parse_args()

    if a.controle:
        sys.exit(controle())
    if not a.lots or not a.sujet:
        ap.error("il faut au moins un lot et --sujet (ou alors --controle)")
    date = a.date or datetime.date.today().isoformat()
    d = livrer(a.lots, a.sujet, date, a.video, a.titre, a.note)
    sys.exit(0 if d else 1)

if __name__ == "__main__":
    main()
