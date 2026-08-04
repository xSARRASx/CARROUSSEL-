#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""photo-cuisine : le 1er rendu faisait image de synthese 3D (lumiere plate,
surfaces lisses, aucune ombre). Prompt de l'audit v2 : vraie photo au reflex,
ombres reelles, grain, micro-textures."""
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("g", "gen_assets_shorts.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

PROMPT = (
    "Photographie d'intérieur authentique d'une petite cuisine d'appartement lumineuse : "
    "façades blanches mates, plan de travail en chêne clair, crédence en carrelage métro "
    "blanc, évier, plaque à induction, four encastré, deux étagères en bois avec vaisselle "
    "simple, petite table ronde en bois et deux chaises, suspension métallique, fenêtre à "
    "gauche donnant sur des toits. Vraie photo prise au reflex, objectif 24 mm, lumière "
    "naturelle douce du matin entrant par la fenêtre, ombres réelles et dégradées, légère "
    "profondeur de champ, grain photographique fin, micro-textures visibles (veinage du "
    "bois, joints du carrelage, reflets discrets sur l'inox). Rendu photographique de "
    "reportage de décoration, surtout PAS de rendu 3D ni d'image de synthèse : pas de "
    "surfaces plastiques, pas d'éclairage plat et uniforme, pas de perfection artificielle. "
    "Aucun texte, aucun watermark, aucune personne.")

g.generate("photo-cuisine.png", PROMPT, "4:3")
