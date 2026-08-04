#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KIT V2 — VERSION PHOTO REELLE (decision de Martin, 03/08/2026 :
"je préfère largement le style réaliste, on refait tout").

Chaque icone du kit est refaite en PHOTO DE STUDIO (packshot) et enregistree
sous le MEME nom avec un tiret et un 2 : icone-menage.png -> icone-menage-2.png.
C'est la regle de nommage demandee par Martin, pour que Kilian retrouve ses
sujets et puisse comparer les deux styles.

Recette : objet reel photographie en studio, fond blanc, ombre douce. Ca se
detoure tout seul et ca s'integre dans n'importe quelle carte de montage.

Les sujets ABSTRAITS (rentabilite, changement d'usage, saisonnalite...) n'ont
pas d'objet evident a photographier : on leur a trouve un equivalent concret
et photographiable (piles de pieces en escalier, calendrier mural, carte
routiere...).

Ne sont PAS refaits ici, parce qu'ils sont deja au bon format :
  - les cartons a texte fabriques en HTML (logo-booking, logo-abritel,
    icone-lmnp, icone-experience) : un texte ne se "photographie" pas ;
  - la capture d'annonce Airbnb (deja une vraie interface) ;
  - les 5 photos d'interieur (deja des photographies).

Usage : python3 gen_kit_realiste.py [nom2.png ...]   (vide = tout)
"""
import importlib.util, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("g", ROOT / "gen_assets_shorts.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

# La recette packshot. "Aucun texte lisible" plutot que "aucun texte" : sur un
# document, une typo floue est credible, alors qu'une page blanche fait vide.
STUDIO = (" Photographie de produit en studio, objet réel photographié au reflex, "
          "fond blanc pur uniforme, éclairage doux de studio en lumière diffuse, "
          "ombre portée douce sous l'objet, très haute définition, matières et textures "
          "réelles bien visibles, couleurs naturelles, mise au point nette, rendu "
          "photographique professionnel de catalogue. Surtout PAS d'illustration, PAS de "
          "dessin, PAS de rendu 3D, PAS de style plat. Aucun texte lisible, aucune "
          "inscription nette, aucun logo de marque, aucun watermark, aucune personne "
          "identifiable.")

SCENE = (" Photographie réaliste prise au reflex, lumière naturelle douce, ombres réelles "
         "et dégradées, faible profondeur de champ, grain photographique fin, couleurs "
         "naturelles. Surtout PAS d'illustration, PAS de rendu 3D. Aucun texte lisible, "
         "aucun logo de marque, aucun watermark.")

KIT = {
    # ---------- Administratif / legal
    "icone-mairie-2.png":
        "Façade d'une mairie de village française en pierre claire, drapeau tricolore "
        "français accroché au-dessus de l'entrée, vue de face en plein jour." + SCENE,
    "icone-autorisation-proprietaire-2.png":
        "Un document contractuel imprimé posé à plat sur une table en bois clair, avec un "
        "stylo plume noir posé en diagonale dessus, texte du document volontairement flou "
        "et illisible, vue du dessus." + SCENE,
    "icone-numero-enregistrement-2.png":
        "Un formulaire administratif imprimé posé à plat sur un bureau, avec un tampon "
        "encreur en bois posé à côté, texte du formulaire volontairement flou et "
        "illisible, vue du dessus." + SCENE,
    "icone-changement-usage-2.png":
        "Une petite maison miniature en bois posée à côté d'un jeu de clés et d'un plan "
        "d'architecte roulé, sur une table claire." + STUDIO,
    # ---------- Argent
    "icone-cashflow-2.png":
        "Une liasse de billets de banque euros posée à plat, à côté de trois piles de "
        "pièces de monnaie de hauteur croissante formant un escalier montant." + STUDIO,
    "icone-rentabilite-2.png":
        "Quatre piles de pièces de monnaie euros de hauteur croissante formant un escalier "
        "montant, avec une petite plante verte qui pousse sur la pile la plus haute." + STUDIO,
    "icone-calculatrice-2.png":
        "Une calculatrice de bureau grise posée à plat, avec quelques pièces de monnaie "
        "euros éparpillées à côté, vue légèrement de trois quarts." + STUDIO,
    "icone-loyer-2.png":
        "Une enveloppe kraft ouverte d'où dépassent quelques billets de banque euros, "
        "posée à plat." + STUDIO,
    # ---------- Plateformes / avis
    "icone-etoiles-avis-2.png":
        "Cinq étoiles dorées en métal brillant, alignées horizontalement et posées à plat, "
        "toutes de la même taille." + STUDIO,
    # ---------- Conciergerie
    "icone-menage-2.png":
        "Un flacon spray de produit ménager blanc et une éponge jaune posés côte à côte." + STUDIO,
    "icone-checkin-2.png":
        "Une boîte à clés sécurisée à code, en métal gris, avec un trousseau de clés posé "
        "juste à côté." + STUDIO,
    "icone-linge-2.png":
        "Une pile de serviettes de bain et de draps blancs impeccablement pliés, empilés "
        "bien à plat, textures de coton visibles." + STUDIO,
    "icone-serrure-2.png":
        "Une serrure connectée moderne à clavier numérique, en métal noir mat, vue de "
        "trois quarts." + STUDIO,
    # ---------- Prospection / negociation
    "icone-proprietaire-2.png":
        "Gros plan sur deux mains d'adultes qui se serrent pour conclure un accord, "
        "manches de chemise visibles, cadrage serré sur les mains uniquement, aucun "
        "visage." + SCENE,
    "icone-agence-2.png":
        "Devanture vitrée d'une agence immobilière de quartier vue de face en plein jour, "
        "vitrine avec des annonces affichées floues et illisibles." + SCENE,
    "icone-contrat-2.png":
        "Gros plan sur une main qui signe un contrat papier avec un stylo, cadrage serré "
        "sur la main et la feuille, texte du contrat volontairement flou et illisible." + SCENE,
    "icone-telephone-2.png":
        "Un smartphone noir moderne posé à plat, écran allumé affichant un fond uni sans "
        "aucune icône ni texte, vu du dessus." + STUDIO,
    # ---------- Ameublement / deco
    "icone-meuble-2.png":
        "Un canapé trois places en tissu gris clair, avec deux coussins, vu de trois "
        "quarts." + STUDIO,
    "icone-home-staging-2.png":
        "Un salon d'appartement en cours d'aménagement : d'un côté un mur nu et un sol "
        "vide, de l'autre un canapé, un tapis et une plante verte déjà installés." + SCENE,
    "icone-jacuzzi-2.png":
        "Un jacuzzi spa extérieur rond en bois clair, eau bleue limpide avec des bulles en "
        "surface, vu de trois quarts." + STUDIO,
    # ---------- Fiscalite
    "icone-impots-2.png":
        "Un formulaire de déclaration de revenus imprimé posé à plat sur un bureau, avec "
        "une calculatrice et un stylo à côté, texte du formulaire volontairement flou et "
        "illisible, vue du dessus." + SCENE,
    "icone-comptable-2.png":
        "Un bureau de comptable vu du dessus : une calculatrice, une pile de documents "
        "papier au texte flou et illisible, un stylo et une tasse de café." + SCENE,
    # ---------- Marche
    "icone-france-carte-2.png":
        "Une carte routière papier de la France dépliée à plat sur une table en bois, vue "
        "du dessus, noms de villes volontairement flous et illisibles." + SCENE,
    "icone-saisonnalite-2.png":
        "Un calendrier mural papier ouvert sur une double page de mois, posé à plat, avec "
        "quelques cases entourées au feutre de couleur, chiffres et texte volontairement "
        "flous et illisibles." + SCENE,
    # ---------- Mindset
    "icone-objectif-2.png":
        "Une cible de tir à l'arc en paille avec des anneaux colorés, une flèche plantée "
        "en plein centre, vue de face." + STUDIO,
}

def main():
    cibles = [a for a in sys.argv[1:] if not a.startswith("-")]
    todo = {k: v for k, v in KIT.items() if not cibles or k in cibles}
    fails = []
    for name, prompt in todo.items():
        if (g.OUT / name).exists() and "--force" not in sys.argv and not cibles:
            print(f"{name}  deja present, saute", flush=True)
            continue
        try:
            g.generate(name, prompt, "1:1")
        except Exception as e:
            print(f"ECHEC {name}: {e}", flush=True)
            fails.append(name)
        time.sleep(3)
    print(f"\nTermine. {len(todo) - len(fails)} traites" +
          (f" ; echecs : {', '.join(fails)}" if fails else ""), flush=True)

if __name__ == "__main__":
    main()
