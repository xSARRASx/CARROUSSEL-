#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 14 — tires de la video du 16/09/2026 « La verite sur le marche
immobilier en 2026 » (ID iIO-RH_doLo).

⚠️ Retour a TROIS questions apres les deux du lot 13 : le format alterne
volontairement d'une semaine a l'autre (Martin, 10/09/2026 : « tout le temps
des choses differentes »). L'ouverture et la cloture viennent des listes
tournantes de photo_style, indexees sur le numero du lot.

Les trois questions portent sur les trois chiffres qui renversent l'intuition :
    1. les prix ont fait +55 % depuis 2000, et les loyers ? -> -9 % ;
    2. l'Etat emprunte plus cher que toi -> 3,90 % contre 3,31 % ;
    3. le krach de 35 % annonce par la courbe -> il n'est pas dans les chiffres.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.

Rendu : python3 render_stories.py interactifs-14
"""
from photo_style import (open_photo, underline, acc, BLANC,
                         quiz_q, quiz_r, sondage, write_lot,
                         quiz_ouverture, quiz_cloture)

NUM_LOT = 14
CONSIGNE, MOT = quiz_ouverture(NUM_LOT)
SCORE, RENVOI = quiz_cloture(NUM_LOT)

STORIES = {}

MARCHE = acc("marché")
PROJET = acc("projet immobilier")
VENDRE = acc("vendre")

STORIES["quiz14_01"] = (
    open_photo("bg_toits_pluie") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:150px;line-height:1;">{MOT}</div>'
    '<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu lis vraiment<br>le {MARCHE} de 2026&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    f'<div class="hand" style="font-size:48px;line-height:1.3;">{CONSIGNE}</div>'
    '</div></div>')

STORIES["quiz14_02"] = quiz_q("bg_champ_ete", 1, 3, "Depuis 2000, les prix ont fait +55 %",
    "par rapport aux revenus. Et les loyers, ils ont fait quoi ?")
STORIES["quiz14_03"] = quiz_r("bg_couloir_hotel", "Moins 9 %",
    "Les loyers n'ont jamais quitté leur couloir historique, ils sont même "
    "passés en dessous. Entre des prix qui montent et des loyers qui baissent, "
    "c'est le rendement qui s'est écrasé.", chiffre="−9 %")

STORIES["quiz14_04"] = quiz_q("bg_neige_douce", 2, 3, "Tu empruntes à 3,31 %",
    "L'État français, lui, emprunte à combien ?")
STORIES["quiz14_05"] = quiz_r("bg_etagere", "3,90 %",
    "Ta banque te prête donc moins cher qu'elle n'emprunte. Historiquement "
    "elle prend un point au-dessus de l'État. La vraie question n'est pas "
    "quand les taux vont baisser, mais combien de temps les banques vont "
    "encore tenir cette marge négative.")

STORIES["quiz14_06"] = quiz_q("bg_foret_automne", 3, 3, "La courbe dit que les prix sont 55 % trop hauts",
    "Donc un krach de 35 % arrive ?")
STORIES["quiz14_07"] = quiz_r("bg_cafe_table", "Pas dans les chiffres",
    "L'ajustement a commencé en 2022 et un sixième de l'excès a déjà disparu. "
    "Ce que les données donnent, c'est moins 2 à 4 % par an pendant plusieurs "
    "années, très inégal selon les villes. Et la dette des ménages est saine : "
    "pas de ventes forcées massives.")

STORIES["quiz14_08"] = (
    open_photo("bg_port") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">{SCORE}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    f'{RENVOI} Les six indicateurs, les trois scénarios, et ce qu\'il a décidé '
    'de faire de sa propre maison.'
    '</div>'
    '</div></div>')

STORIES["sondage14_01"] = sondage("bg_mur_beton", "dis-nous où tu en es",
    f'Ton {PROJET} en ce moment, il en est où&nbsp;?')

STORIES["sondage14_02"] = sondage("bg_rideau", "question du jour",
    f'Tu devais {VENDRE} aujourd\'hui. Tu affiches quoi&nbsp;?')

SLUG = "interactifs-14"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
