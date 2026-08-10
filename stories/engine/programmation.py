#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROGRAMMATION DE TOUT LE STOCK — un rendez-vous par jour, à 12h00.

Décision de Martin (06/08/2026) : « les stories c'est à 12h, une seule fois
par jour, donc là toutes les stories qu'on a d'avance, on les programme pour
toutes les prochaines semaines ».

CE QUE FAIT CE SCRIPT
    Il prend TOUT le stock disponible, le range par jour de publication, et
    produit un dossier prêt pour le robot Mac où chaque fichier porte SA DATE :

        2026-08-07-12h00-01.jpg
        2026-08-07-12h00-02.jpg     <- même jour, la séquence s'enchaîne
        2026-08-08-12h00-01.jpg     <- jour suivant

UN POINT IMPORTANT SUR LE DÉCOUPAGE
    Une séquence d'aide est écrite pour se lire d'une traite : la couverture
    promet (« du concret, juste après »), les stories suivantes livrent, la
    dernière conclut. Si on la coupait en six et qu'on postait une image par
    jour, la couverture promettrait une suite qui n'arriverait que le
    lendemain : le contenu ne tiendrait plus debout.
    Donc : UN rendez-vous par jour à 12h00, et ce rendez-vous contient la
    séquence complète du jour (3 à 6 stories qui s'enchaînent). C'est le
    format habituel d'Instagram, et c'est ce que le contenu exige.

TROIS JOURS SONT RÉSERVÉS, LA PROGRAMMATION LES SAUTE
    - MERCREDI et DIMANCHE : ce sont les créneaux de Pierre. Il y poste ses
      témoignages à 12h00, avec la story « Réponds GO » derrière.
    - SAMEDI : les quiz et sondages, que Martin poste à la main parce qu'ils
      réclament un sticker de vote qu'Instagram interdit sur une story
      programmée.
    La production automatique n'alimente donc que LUNDI, MARDI, JEUDI et
    VENDREDI.

Usage :
    python3 programmation.py [--debut AAAA-MM-JJ] [--dossier <nom>]
"""
import argparse, datetime, pathlib, shutil, sys
from collections import OrderedDict
from planning import besoin_sticker
from stickers import bloc_texte, est_doublon

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parent
OUT = ROOT / "output"
LIVRAISON = REPO / "livraison"

HEURE = "12h00"

# Les lots qui alimentent la programmation. Les gabarits de témoignage en sont
# exclus : c'est Pierre qui les poste, avec son propre screenshot.
LOTS = ["banque-01", "banque-02", "semaine-01", "interactifs-01", "interactifs-02"]
EXCLUS = ("temoin",)          # gabarits de Pierre, jamais programmés

def sequences():
    """Regroupe le stock en séquences (le préfixe du nom fait la séquence)."""
    seqs = OrderedDict()
    for lot in LOTS:
        d = OUT / lot / "jpg"
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.jpg")):
            if any(x in f.stem.lower() for x in EXCLUS):
                continue
            # Une question deja posee ailleurs ne repart pas une 2e fois
            # (Martin, 08/08/2026 : deux samedis posaient la meme question).
            if est_doublon(f.stem):
                continue
            # A_remplir_sans_baisser_03 -> A_remplir_sans_baisser
            # quiz02_04 -> quiz02 ; lundi_02_sondage -> jour isolé
            tige = f.stem.rsplit("_", 1)[0] if f.stem.rsplit("_", 1)[-1].isdigit() else f.stem
            seqs.setdefault(f"{lot}/{tige}", []).append(f)
    return seqs

def est_manuel(fichiers):
    """Une séquence part en manuel dès qu'une de ses stories réclame un sticker."""
    return any(besoin_sticker(f.stem)[0] for f in fichiers)

def jours_a_partir_de(debut, n):
    return [debut + datetime.timedelta(days=i) for i in range(n)]

def programmer(debut, nom_dossier):
    seqs = sequences()
    if not seqs:
        print("ECHEC : aucun stock trouvé.", flush=True)
        return None

    # On sépare ce qui se programme de ce qui demande un sticker.
    auto = OrderedDict((k, v) for k, v in seqs.items() if not est_manuel(v))
    manuel = OrderedDict((k, v) for k, v in seqs.items() if est_manuel(v))

    # Les stories isolées de semaine-01 sont regroupées par 3 pour former
    # des rendez-vous d'une taille correcte.
    isolees, groupes = [], OrderedDict()
    for k, v in auto.items():
        (isolees if len(v) == 1 else groupes).setdefault(k, v) if len(v) > 1 else isolees.append((k, v[0]))
    for i in range(0, len(isolees), 3):
        paquet = isolees[i:i + 3]
        groupes[f"melange-{i // 3 + 1}"] = [f for _, f in paquet]

    dossier = LIVRAISON / nom_dossier
    if dossier.exists():
        shutil.rmtree(dossier)
    (dossier / "auto").mkdir(parents=True)
    (dossier / "manuel").mkdir(parents=True)

    # Les journees deja servies par une fournee de la semaine sont intouchables :
    # la programmation du stock se range AUTOUR d'elles. L'actualite passe en
    # premier, le stock comble les trous. (Martin, 08/08/2026.)
    from livraison import jours_deja_pris
    occupes = (jours_deja_pris(sauf=dossier, sous_dossier="auto")
               | jours_deja_pris(sauf=dossier, sous_dossier="manuel"))
    if occupes:
        print(f"  {len(occupes)} journee(s) deja servie(s) par une fournee, on les saute.",
              flush=True)

    calendrier = []
    jour = debut
    # Les séquences programmables prennent les jours ordinaires ; on saute les
    # samedis, qui sont réservés aux quiz et sondages.
    # 2 = mercredi et 6 = dimanche appartiennent a Pierre (ses temoignages),
    # 5 = samedi a Martin (quiz et sondages, a la main). La production
    # automatique ne prend que lundi, mardi, jeudi, vendredi.
    RESERVES = {2, 5, 6}
    for nom, fichiers in groupes.items():
        while jour.weekday() in RESERVES or jour.isoformat() in occupes:
            jour += datetime.timedelta(days=1)
        for i, src in enumerate(fichiers, 1):
            shutil.copy2(src, dossier / "auto" / f"{jour}-{HEURE}-{i:02d}.jpg")
        calendrier.append((jour, "auto", nom, len(fichiers)))
        jour += datetime.timedelta(days=1)

    # Les séquences manuelles prennent les samedis. On les REGROUPE en blocs
    # de taille correcte : un samedi qui ne recevrait qu'une seule story
    # gâcherait le créneau, et étalerait le stock sur des mois pour rien.
    # Une séquence de quiz reste entière (elle s'enchaîne), les stories
    # isolées se rassemblent pour compléter.
    entieres = [(k, v) for k, v in manuel.items() if len(v) >= 4]
    petites = [(k, v) for k, v in manuel.items() if len(v) < 4]
    blocs = [(k, v) for k, v in entieres]
    tampon, noms = [], []
    for k, v in petites:
        tampon += v
        noms.append(k.split("/")[-1])
        if len(tampon) >= 4:
            blocs.append((" + ".join(noms), tampon))
            tampon, noms = [], []
    if tampon:
        # Un samedi qui ne recevrait que 1 ou 2 stories gache le creneau :
        # on recolle ce reste au bloc precedent plutot que d'ouvrir un samedi
        # pour si peu (Martin, 08/08/2026).
        if len(tampon) < 3 and blocs:
            nom_prec, contenu = blocs[-1]
            blocs[-1] = (f"{nom_prec} + {' + '.join(noms)}", contenu + tampon)
        else:
            blocs.append((" + ".join(noms), tampon))

    samedi = debut
    while samedi.weekday() != 5 or samedi.isoformat() in occupes:
        samedi += datetime.timedelta(days=1)
    entrees = []
    for nom, fichiers in blocs:
        for i, src in enumerate(fichiers, 1):
            besoin, sticker = besoin_sticker(src.stem)
            suffixe = f"-{sticker}" if sticker else ""
            fnom = f"{samedi}-{HEURE}-{i:02d}{suffixe}.jpg"
            shutil.copy2(src, dossier / "manuel" / fnom)
            if besoin:
                entrees.append((fnom, src.stem))
        calendrier.append((samedi, "manuel", nom, len(fichiers)))
        samedi += datetime.timedelta(days=7)
        while samedi.isoformat() in occupes:
            samedi += datetime.timedelta(days=7)
    # Le texte exact de chaque sticker voyage AVEC les images (Martin, 06/08).
    if entrees:
        txt, manquants = bloc_texte(entrees)
        (dossier / "manuel" / "_STICKERS.txt").write_text(txt, encoding="utf-8")
        for m in manquants:
            print(f"  ALERTE : texte de sticker manquant pour {m}", flush=True)

    calendrier.sort(key=lambda x: (x[0], x[1]))
    ecrire_calendrier(dossier, calendrier, debut)
    n_auto = len(list((dossier / "auto").glob("*.jpg")))
    n_man = len(list((dossier / "manuel").glob("*.jpg")))
    fin = max(c[0] for c in calendrier)
    print(f"Programmé : livraison/{dossier.name}", flush=True)
    print(f"  {n_auto} stories automatiques + {n_man} manuelles", flush=True)
    print(f"  du {debut} au {fin}  ({(fin - debut).days + 1} jours couverts)", flush=True)
    return dossier

def ecrire_calendrier(dossier, calendrier, debut):
    JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    lignes = [
        "CALENDRIER DE PROGRAMMATION DES STORIES",
        f"Rendez-vous quotidien : 12h00, heure de Paris. Un seul par jour.",
        "",
        "Chaque fichier porte SA DATE de publication :",
        "    AAAA-MM-JJ-12h00-NN.jpg",
        "Les stories qui partagent la meme date forment UNE seule publication :",
        "elles s'enchainent dans l'ordre des numeros, le meme jour a 12h00.",
        "",
        "auto/    : a programmer tel quel.",
        "manuel/  : NE JAMAIS PROGRAMMER. Ces stories promettent un vote, et le",
        "           sticker de sondage Instagram ne peut pas etre pose sur une",
        "           story programmee. Elles tombent toujours un SAMEDI, et le nom",
        "           du fichier dit quel sticker poser (SONDAGE ou QUESTIONS).",
        "",
        "-" * 62,
        "",
    ]
    for date, mode, nom, n in calendrier:
        marque = "  [A LA MAIN]" if mode == "manuel" else ""
        lignes.append(f"{JOURS[date.weekday()]:9s} {date}  {n} stories{marque}  — {nom}")
    lignes += ["", "-" * 62, ""]
    total = sum(c[3] for c in calendrier)
    fin = max(c[0] for c in calendrier)
    lignes.append(f"{total} stories, du {debut} au {fin}.")
    lignes.append(f"Soit {(fin - debut).days + 1} jours de contenu programmes d'avance.")
    (dossier / "calendrier.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--debut", help="AAAA-MM-JJ (defaut : demain)")
    ap.add_argument("--dossier", default=None)
    a = ap.parse_args()
    debut = (datetime.date.fromisoformat(a.debut) if a.debut
             else datetime.date.today() + datetime.timedelta(days=1))
    nom = a.dossier or f"programmation-{debut}"
    sys.exit(0 if programmer(debut, nom) else 1)

if __name__ == "__main__":
    main()
