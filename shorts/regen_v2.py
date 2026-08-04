#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REGENERATION V2 des assets de montage recales par l'audit visuel.

Contexte : l'audit du 1er lot (shorts/audit-v1.json) a recale 23 assets sur 29.
Cause n1 et de loin : Gemini AJOUTE DU TEXTE tout seul, et il l'ecrit faux
("PROPRIETERE", "D'ENBEGRTEMENT", "Personelles", "JUNIE", "FEBRUER"...).
Cause n2 : objets deformes (doigts fusionnes, billets fondus, drapeau casse).

Regle appliquee ici : chaque prompt se termine par une clause anti-texte et
anti-deformation stricte. Les assets qui ONT BESOIN de mots lisibles ne
passent PAS par l'IA : ils sont fabriques en HTML (build_captures.py).

Usage : python3 regen_v2.py [nom-de-fichier ...]   (vide = tous)
"""
import importlib.util, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("g", ROOT / "gen_assets_shorts.py")
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

# Clause collee a la fin de CHAQUE prompt : c'est elle qui tue l'effet IA.
NET = (" Style icône flat vectoriel minimaliste, aplats de couleur unis, contours nets, "
       "composition centrée et symétrique, aucune ombre sale, fond blanc uni pur. "
       "Aucun texte, aucune lettre, aucun chiffre, aucun mot, aucune inscription, "
       "aucun watermark, aucune signature. Formes simples et géométriquement correctes, "
       "aucun objet déformé ou fondu.")

PHOTO_NET = (" Photographie professionnelle réaliste, lumière naturelle du jour, couleurs "
             "naturelles non saturées, mise au point nette, perspective correcte. "
             "Aucun texte, aucune lettre, aucun watermark, aucune personne.")

# Sujets reecrits : on retire tout ce qui poussait le modele a ecrire du texte
# (les mots "formulaire officiel", "badge avec texte", "calcul de rentabilite"...).
REGEN = {
    # --- Administratif
    "icone-mairie.png":
        "Façade d'une mairie française vue de face, parfaitement symétrique, toit sombre, "
        "clocheton central avec une horloge ronde bien dégagée, UN SEUL drapeau tricolore "
        "bleu blanc rouge d'un seul tenant entièrement attaché à son mât, fenêtres en "
        "arcade régulières." + NET,
    "icone-autorisation-proprietaire.png":
        "Une feuille de contrat rectangulaire avec quelques lignes grises abstraites, un "
        "stylo posé en diagonale dessus, et en dessous deux mains stylisées qui se serrent, "
        "chaque main ayant cinq doigts nettement séparés." + NET,
    "icone-numero-enregistrement.png":
        "Une feuille de papier administrative vierge vue de face, quelques lignes grises "
        "abstraites suggérant des champs, un tampon rond bleu parfaitement lisse et vide "
        "posé en bas à droite." + NET,
    "icone-changement-usage.png":
        "Une maison d'habitation simple à gauche, une flèche courbe orange au centre, une "
        "petite boutique commerciale avec store à droite." + NET,
    # --- Argent
    "icone-cashflow.png":
        "Une liasse de billets stylisée vue de face, billets vert clair parfaitement unis "
        "et vierges, ceinturés d'un bandeau blanc, avec une grande flèche verte montante "
        "placée derrière la liasse sans la traverser." + NET,
    "icone-rentabilite.png":
        "Un grand symbole pourcentage bleu marine et une flèche verte montante à côté." + NET,
    "icone-calculatrice.png":
        "Une calculatrice de bureau vue de face, corps bleu, écran rectangulaire vide, "
        "grille régulière de touches arrondies parfaitement unies et vierges, trois pièces "
        "de monnaie rondes lisses et vierges posées à côté." + NET,
    "icone-loyer.png":
        "Une enveloppe ouverte vue de face, d'où dépassent trois billets stylisés vert "
        "clair parfaitement unis et vierges, et un symbole euro bleu à côté." + NET,
    # --- Plateformes
    "icone-etoiles-avis.png":
        "Cinq étoiles pleines alignées horizontalement, toutes exactement de la même taille "
        "et de la même couleur jaune doré uni, sans reflet ni brillance." + NET,
    # --- Conciergerie
    "icone-linge.png":
        "Une pile de serviettes et de draps pliés, empilés bien à plat, chaque pièce d'une "
        "couleur différente et nettement contrastée : bleu clair, gris, beige, blanc cassé "
        "avec un contour gris visible." + NET,
    # --- Prospection
    "icone-proprietaire.png":
        "Deux mains stylisées qui se serrent, vues de profil, chaque main ayant cinq doigts "
        "nettement séparés et bien dessinés." + NET,
    "icone-agence.png":
        "Devanture d'une agence immobilière vue de face, vitrine rectangulaire, store droit, "
        "porte d'entrée simple, deux petits panneaux rectangulaires vierges en vitrine." + NET,
    "icone-contrat.png":
        "Une main stylisée tenant un stylo qui signe une feuille de contrat, la main ayant "
        "cinq doigts nettement séparés, quelques lignes grises abstraites sur la feuille et "
        "un trait de signature manuscrit stylisé." + NET,
    "icone-telephone.png":
        "Un smartphone vu de face, écran uni sans contenu, avec deux petites ondes courbes "
        "d'appel de chaque côté." + NET,
    # --- Ameublement
    "icone-meuble.png":
        "Un canapé trois places vu de face, une lampe sur pied à côté et une plante verte en "
        "pot, formes géométriques simples et proportions correctes." + NET,
    "icone-home-staging.png":
        "Une image séparée en deux moitiés par un trait vertical : à gauche une pièce vide "
        "aux murs gris, à droite la même pièce meublée avec un canapé, un tapis et une "
        "plante, en couleurs chaudes." + NET,
    # --- Fiscalite
    "icone-impots.png":
        "Une feuille de déclaration vierge vue de face avec des lignes grises abstraites et "
        "une petite case à cocher, un symbole euro bleu à côté." + NET,
    "icone-comptable.png":
        "Une personne stylisée vue de face assise à un bureau, avec une calculatrice vierge "
        "et une pile de documents, visage simplifié sans détail, mains à cinq doigts." + NET,
    # --- Marche
    "icone-saisonnalite.png":
        "Une grille de calendrier stylisée dont les cases sont colorées, moitié orange et "
        "moitié bleue, avec un petit soleil orange au-dessus à gauche et un flocon bleu à "
        "droite." + NET,
    # --- Mindset
    "icone-objectif.png":
        "Une cible de tir vue de face avec des anneaux concentriques réguliers alternant "
        "bleu marine et blanc, centre rouge, et une flèche plantée en plein centre." + NET,
    # --- Photo
    "photo-appartement.png":
        "Intérieur d'un appartement français meublé, moderne et lumineux, parquet en "
        "chevron, canapé clair, grandes fenêtres donnant sur une rue haussmannienne, "
        "décoration soignée." + PHOTO_NET,
}

def main():
    cibles = [a for a in sys.argv[1:] if not a.startswith("-")]
    todo = {k: v for k, v in REGEN.items() if not cibles or k in cibles}
    fails = []
    for name, prompt in todo.items():
        aspect = "4:3" if name.startswith("photo-") else "1:1"
        try:
            g.generate(name, prompt, aspect)
        except Exception as e:
            print(f"ECHEC {name}: {e}")
            fails.append(name)
        time.sleep(3)
    print(f"\nTermine. {len(todo) - len(fails)}/{len(todo)} regeneres" +
          (f" ; echecs : {', '.join(fails)}" if fails else ""))

if __name__ == "__main__":
    main()
