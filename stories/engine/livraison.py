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
        auto/       <- LE ROBOT MAC NE PROGRAMME QUE CE DOSSIER
                       2026-08-10-12h00-01.jpg : DATE de publication, 12h00,
                       rang dans la sequence du jour
        manuel/     <- stories a poster A LA MAIN, le samedi, regroupees
                       2026-08-15-12h00-01-SONDAGE.jpg : le nom dit le sticker
        reserve/    <- surplus de la fournee, sans creneau cette semaine
                       sert de stock pour les semaines sans video
        description.txt

Le nom du fichier PORTE sa date : <AAAA-MM-JJ>-12h00-<rang>.jpg
UN SEUL rendez-vous par jour, a 12h00, avec la sequence entiere dedans.

Usage :
    python3 livraison.py <lot> [<lot> ...] --sujet <mot-cle> [--date AAAA-MM-JJ]
        [--video <id>] [--titre "<titre francais>"] [--note "<texte libre>"]
    python3 livraison.py --controle      # contrôle d'intégrité, code 1 si problème

⚠️ Le contrôle est OBLIGATOIRE avant le push. S'il signale un problème, on ne
pousse PAS en silence : on alerte Martin en première ligne.
"""
import argparse, datetime, json, pathlib, shutil, sys
from PIL import Image
from planning import GRILLE, jours_de_la_fournee, besoin_sticker
from stickers import bloc_texte

JOURS_SEMAINE = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

def creneaux_auto(jours, date_fournee):
    """Déroule la grille en (date réelle, rang), un rendez-vous par jour à 12h.

    Les fichiers portent leur DATE de publication, exactement comme
    programmation.py : une seule convention pour le robot Mac.
    """
    import datetime
    d0 = datetime.date.fromisoformat(date_fournee)
    plan = []
    for j in jours:
        # la date réelle de ce jour de la semaine, à partir de la fournée
        delta = (JOURS_SEMAINE.index(j) - d0.weekday()) % 7
        date = d0 + datetime.timedelta(days=delta)
        for _, n, _, mode in GRILLE[j]:
            if mode != "auto":
                continue
            for r in range(1, n + 1):
                plan.append((date, r))
    return plan

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

def samedis_deja_pris(sauf=None):
    """Les dates de samedi deja occupees par une livraison manuelle.

    Chaque fichier de `manuel/` porte sa date en tete (AAAA-MM-JJ-12h00-...).
    On relit TOUS les dossiers de `livraison/`, y compris la programmation du
    stock, pour ne jamais poser deux paquets manuels le meme jour.
    """
    pris = set()
    if not LIVRAISON.is_dir():
        return pris
    for d in LIVRAISON.iterdir():
        if not d.is_dir() or (sauf is not None and d == sauf):
            continue
        for p in d.glob("manuel/*.jpg"):
            pris.add(p.name[:10])
    return pris

def livrer(lots, sujet, date, video=None, titre=None, note=None, reveil='lundi'):
    lots = trier_lots(lots)
    jours = jours_de_la_fournee(reveil)
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
    (dossier / "auto").mkdir(parents=True)
    (dossier / "manuel").mkdir(parents=True)

    # SÉPARATION AUTO / MANUEL (exigence de Martin, 06/08/2026) :
    # une story qui promet un vote ne doit JAMAIS partir en programmation
    # sans son sticker, ce serait pire que de ne rien poster.
    auto, manuel = [], []
    for src in fichiers:
        besoin, sticker = besoin_sticker(src.stem)
        (manuel if besoin else auto).append((src, sticker))

    # Les stories automatiques suivent la grille : jour et heure dans le nom.
    # Une fournée riche produit souvent PLUS que ce que la semaine peut
    # absorber : le surplus part en `reserve/` (c'est le stock qui couvrira
    # les semaines sans vidéo). Le robot Mac ne programme QUE `auto/`.
    plan = creneaux_auto(jours, date)
    reserve = auto[len(plan):]
    for i, (src, _) in enumerate(auto[:len(plan)]):
        date_pub, rang = plan[i]
        shutil.copy2(src, dossier / "auto" / f"{date_pub}-12h00-{rang:02d}.jpg")
    if reserve:
        (dossier / "reserve").mkdir(exist_ok=True)
        for i, (src, _) in enumerate(reserve, 1):
            shutil.copy2(src, dossier / "reserve" / f"{i:02d}-{src.stem}.jpg")

    # Les stories manuelles sont toutes regroupées sur le samedi, et le nom
    # dit quel sticker poser.
    # ⚠️ On prend le premier samedi ENCORE LIBRE : un samedi deja reserve par
    # une autre fournee (ou par la programmation du stock) recevrait deux
    # paquets de stories a la fois, et Martin ne saurait pas lequel poster.
    # Erreur reperee par Martin le 08/08/2026.
    import datetime as _dt
    d0 = _dt.date.fromisoformat(date)
    samedi = d0 + _dt.timedelta(days=(5 - d0.weekday()) % 7)
    pris = samedis_deja_pris(sauf=dossier)
    while samedi.isoformat() in pris:
        print(f"  Samedi {samedi} deja pris par une autre fournee, on decale.", flush=True)
        samedi += _dt.timedelta(days=7)
    entrees = []
    for i, (src, sticker) in enumerate(manuel, 1):
        nom = f"{samedi}-12h00-{i:02d}-{sticker}.jpg"
        shutil.copy2(src, dossier / "manuel" / nom)
        entrees.append((nom, src.stem))
    # Le texte exact de chaque sticker voyage AVEC les images (Martin, 06/08) :
    # sans ca, il faut redemander la question et les options a chaque fois.
    if entrees:
        txt, manquants = bloc_texte(entrees)
        (dossier / "manuel" / "_STICKERS.txt").write_text(txt, encoding="utf-8")
        for m in manquants:
            print(f"  ALERTE : texte de sticker manquant pour {m}", flush=True)

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
        f"{len(fichiers)} stories au total. Format : JPEG 1080x1920.",
        "",
        "COMMENT LIRE CE DOSSIER :",
        "- auto/     : A PROGRAMMER. Le nom du fichier porte SA DATE de",
        "              publication : <AAAA-MM-JJ>-12h00-<rang>.jpg.",
        "              Les fichiers qui partagent une date forment UNE publication :",
        "              ils s'enchainent le meme jour a 12h00 (heure de Paris).",
        "- manuel/   : NE JAMAIS PROGRAMMER. Ces stories promettent un vote et le",
        "              sticker de sondage Instagram ne peut pas etre pose sur une",
        "              story programmee. Elles sont toutes regroupees le SAMEDI,",
        "              et le nom dit quel sticker poser : SONDAGE ou QUESTIONS.",
        "- reserve/  : surplus sans creneau cette semaine. Ne pas programmer, c'est",
        "              le stock qui couvrira les semaines sans video.",
    ]
    if note:
        lignes += ["", note]
    lignes += ["", "Détail des lots inclus :"]
    for lot in lots:
        lignes.append(f"- {lot} ({len(jpgs_du_lot(lot))} stories)")

    (dossier / "description.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    nres = len(list((dossier / "reserve").glob("*.jpg"))) if (dossier / "reserve").is_dir() else 0
    print(f"Livré : livraison/{dossier.name}  "
          f"({len(auto) - nres} programmables, {len(manuel)} manuel, {nres} en reserve)", flush=True)
    return dossier

def controle():
    """Contrôle d'intégrité. Code de sortie 1 si quoi que ce soit cloche."""
    if not LIVRAISON.is_dir():
        print("ALERTE : le dossier livraison/ n'existe pas.", flush=True)
        return 1
    # On controle TOUT ce que le robot Mac peut voir : les fournees de la
    # semaine (stories-...) ET la programmation du stock (programmation-...).
    dossiers = sorted(d for d in LIVRAISON.iterdir()
                      if d.is_dir() and not d.name.startswith("."))
    if not dossiers:
        print("ALERTE : aucune fournée dans livraison/.", flush=True)
        return 1

    # Deux dossiers ne doivent JAMAIS revendiquer la meme journee : le robot
    # programmerait deux paquets de stories le meme jour a 12h00, et Martin ne
    # saurait pas lequel poster. (Erreur reperee par Martin le 08/08/2026.)
    par_jour = {}
    for d in dossiers:
        for p in list(d.glob("auto/*.jpg")) + list(d.glob("manuel/*.jpg")):
            par_jour.setdefault(p.name[:10], set()).add(d.name)
    collisions = {j: sorted(s) for j, s in par_jour.items() if len(s) > 1}

    alertes = [f"le {j} est revendique par DEUX dossiers a la fois : {', '.join(s)}"
               for j, s in sorted(collisions.items())]
    for d in dossiers:
        images = (sorted(d.glob("auto/*.jpg")) + sorted(d.glob("manuel/*.jpg"))
                  + sorted(d.glob("reserve/*.jpg")))
        if not images:
            alertes.append(f"{d.name} : aucune image")
            continue
        if not (d / "description.txt").is_file() and not (d / "calendrier.txt").is_file():
            alertes.append(f"{d.name} : description.txt ou calendrier.txt manquant")
        # numérotation continue, sans trou
        if not (d / "auto").is_dir() or not (d / "manuel").is_dir():
            alertes.append(f"{d.name} : sous-dossiers auto/ et manuel/ attendus")
        if list(d.glob("manuel/*.jpg")) and not (d / "manuel" / "_STICKERS.txt").is_file():
            alertes.append(f"{d.name} : manuel/_STICKERS.txt manquant "
                           f"(le texte des stickers doit voyager avec les images)")
        # Dans une sequence manuelle, seules les QUESTIONS portent un sticker :
        # la couverture, les reponses et la cloture n'en ont pas, et c'est
        # normal. On verifie donc deux choses :
        #   - un suffixe present est un vrai nom de sticker ;
        #   - chaque journee manuelle compte au moins UNE story a sticker,
        #     sinon elle n'avait aucune raison d'echapper a la programmation.
        VALIDES = ("QUIZ", "SONDAGE", "QUESTIONS")
        avec_sticker = {}
        for p in d.glob("manuel/*.jpg"):
            suffixe = p.stem.rsplit("-", 1)[-1]
            porte = suffixe in VALIDES
            avec_sticker[p.name[:10]] = avec_sticker.get(p.name[:10], False) or porte
            if not porte and suffixe.isalpha() and suffixe.isupper():
                alertes.append(f"{d.name}/manuel/{p.name} : suffixe '{suffixe}' inconnu "
                               f"(attendu QUIZ, SONDAGE ou QUESTIONS)")
        for jour, porte in sorted(avec_sticker.items()):
            if not porte:
                alertes.append(f"{d.name}/manuel : le {jour} ne contient aucune story "
                               f"a sticker, elle aurait du partir en programmation")
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
        na = len(list(d.glob("auto/*.jpg")))
        nm = len(list(d.glob("manuel/*.jpg")))
        nr = len(list(d.glob("reserve/*.jpg")))
        print(f"OK  {d.name}  ({na} auto, {nm} manuel, {nr} reserve)", flush=True)

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
    ap.add_argument("--reveil", choices=["lundi", "jeudi"], default="lundi",
                    help="quelle fournee : lundi (lun-mer) ou jeudi (jeu-dim)")
    ap.add_argument("--controle", action="store_true")
    a = ap.parse_args()

    if a.controle:
        sys.exit(controle())
    if not a.lots or not a.sujet:
        ap.error("il faut au moins un lot et --sujet (ou alors --controle)")
    date = a.date or datetime.date.today().isoformat()
    d = livrer(a.lots, a.sujet, date, a.video, a.titre, a.note, a.reveil)
    sys.exit(0 if d else 1)

if __name__ == "__main__":
    main()
