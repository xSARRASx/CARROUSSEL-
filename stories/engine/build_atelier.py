#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATELIER EN LIVE DU DIMANCHE 23/08/2026, 10H — DEUX IMAGES, PAS PLUS.

Pierre (WhatsApp du 17/08/2026) : « cette semaine tu peux en faire pour
dimanche, on est en live, on fait un atelier, comme un webinaire, a 10h, sur
la conciergerie et sous loc ».

⚠️ CADRAGE DE MARTIN, apres une premiere version trop lourde (17/08/2026) :
« il me faut juste deux images, une que je poste mercredi et une autre
dimanche, c'est juste pour prevenir qu'il y a un live ».
La premiere version faisait 7 stories, avec sequence d'annonce, sondage,
boite a questions et cartes d'appel a l'action. C'etait hors sujet : prevenir
qu'il y a un live, ca tient en une image par jour.

DONC, REGLE POUR LA PROCHAINE FOIS : une annonce d'evenement n'est pas une
sequence d'aide. Une image le jour de l'annonce, une image le jour J. Chaque
image se suffit a elle-meme : le jour, l'heure, le sujet, et comment
rejoindre. Rien d'autre.

Les deux images portent le mot-cle ATELIER directement dessus : pas besoin
d'une story supplementaire pour l'appel a l'action.

Ce pack N'EST PAS dans livraison/ : ce n'est pas une fournee du robot, Martin
poste ces deux images a la main. Elles vivent ici, dans stories/output/.

⚠️ On n'invente pas le programme de l'atelier. Ce qui est connu et rien de
plus : en direct, dimanche a 10h, conciergerie et sous-location.

Rendu : python3 render_stories.py atelier-23-08
"""
from photo_style import cover, acc, write_lot

DIX_HEURES = acc("10h")
AUJOURDHUI = acc("aujourd'hui")

STORIES = {}

# --------------------------------------------------------- MERCREDI 19/08
STORIES["01_mercredi_annonce"] = cover(
    "bg_terrasse", "dimanche, en direct",
    f'Atelier conciergerie et sous-location, à {DIX_HEURES}.',
    sub="Une heure en direct, avec vos questions.",
    hand_bottom="réponds ATELIER, je t'envoie le lien")

# --------------------------------------------------------- DIMANCHE 23/08
STORIES["02_dimanche_jour_j"] = cover(
    "bg_plage_aube", "c'est aujourd'hui",
    f'On est en direct à {DIX_HEURES}.',
    sub="Atelier conciergerie et sous-location. Il est encore temps de nous "
        "rejoindre.",
    hand_bottom="réponds ATELIER, je t'envoie le lien")

SLUG = "atelier-23-08"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
