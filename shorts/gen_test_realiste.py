#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ECHANTILLON REALISTE (question de Martin, 03/08/2026 : "tu aurais pas pu faire
des choses vraiment realistes ?").

Le kit v1 est en style icone flat parce que c'est ce que demandait le tableau
de Kilian ("style flat, fond blanc" a chaque ligne). Ici on refait 6 sujets en
PHOTO REELLE facon packshot studio, pour que Martin compare et tranche.

Sortie : shorts/test-realiste/ (on n'ecrase PAS le kit actuel).
"""
import importlib.util, pathlib, time

ROOT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("g", ROOT / "gen_assets_shorts.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
g.OUT = ROOT / "test-realiste"

# Recette packshot : objet reel photographie en studio sur fond blanc, ombre
# douce -> se detoure tout seul et s'integre dans n'importe quelle carte de montage.
STUDIO = (" Photographie de produit en studio, objet réel photographié au reflex, "
          "fond blanc pur uniforme, éclairage doux de studio en lumière diffuse, "
          "ombre portée douce sous l'objet, très haute définition, matières et "
          "textures réelles bien visibles, couleurs naturelles, mise au point nette, "
          "rendu photographique professionnel de catalogue. Surtout PAS d'illustration, "
          "PAS de dessin, PAS de rendu 3D. Aucun texte, aucune lettre, aucune "
          "inscription, aucun logo, aucun watermark, aucune personne.")

TESTS = {
    "menage-realiste.png":
        "Un flacon spray de produit ménager blanc et une éponge jaune posés côte à côte." + STUDIO,
    "checkin-realiste.png":
        "Une boîte à clés sécurisée à code, en métal gris, avec un trousseau de clés posé "
        "juste à côté." + STUDIO,
    "serrure-realiste.png":
        "Une serrure connectée moderne à clavier numérique, en métal noir mat, vue de "
        "trois quarts." + STUDIO,
    "linge-realiste.png":
        "Une pile de serviettes de bain et de draps blancs impeccablement pliés, empilés "
        "bien à plat, textures de coton visibles." + STUDIO,
    "jacuzzi-realiste.png":
        "Un jacuzzi spa extérieur rond en bois clair, eau bleue limpide avec des bulles en "
        "surface, vu de trois quarts." + STUDIO,
    "cles-maison-realiste.png":
        "Un trousseau de clés de maison posé à plat, avec un porte-clés en cuir marron en "
        "forme de petite maison." + STUDIO,
}

for name, prompt in TESTS.items():
    try:
        g.generate(name, prompt, "1:1")
    except Exception as e:
        print(f"ECHEC {name}: {e}", flush=True)
    time.sleep(3)
print("\nTermine.", flush=True)
