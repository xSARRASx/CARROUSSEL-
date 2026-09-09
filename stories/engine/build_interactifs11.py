#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 11 — quiz et sondages tires de la video du 08/09/2026
« Revenus reels vs revenus affiches : Le grand mensonge » (ID v8fzA9JYTHM).

Le quiz porte sur les TROIS renversements que Sebastien opere dans la video,
parce que ce sont ceux qui vont a l'encontre du reflexe naturel :
    1. d'ou vient l'argent qu'on te montre -> de ceux qui ont achete, c'est du
       marketing, tu es le produit ;
    2. annoncer son chiffre n'est pas de la transparence -> c'est s'interdire
       de faire moins un jour ;
    3. a quoi se reconnait quelqu'un qui a reussi -> a son temps libre, pas a
       son agenda plein.

⚠️ Chaque question a son entree dans stickers.py (regle de Martin du
06/08/2026). Le sticker utilise est le SONDAGE, jamais le Quiz d'Instagram,
qui revelerait la reponse au moment du vote et viderait la story suivante.

Gabarits quiz_q / quiz_r / sondage : partages dans photo_style.py.
Fonds tous differents a l'interieur de la sequence.

Rendu : python3 render_stories.py interactifs-11
"""
from photo_style import (open_photo, underline, acc, BLANC,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

# Les apostrophes ne passent pas dans une expression de f-string.
AFFICHES = acc("affichés")
BIEN_JOUE = acc("Bien joué.")
REFLEXE = acc("réflexe")
ANNEE = acc("cette année")

# ============================================================================
# QUIZ — revenus reels contre revenus affiches
# ============================================================================

STORIES["quiz11_01"] = (
    open_photo("bg_salon_cosy") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    '<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu sais lire les revenus<br>{AFFICHES}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz11_02"] = quiz_q("bg_ciel_rose", 1, 3, "Une addition à 20 000 € postée en story",
    "Cet argent-là, il vient d'où ?")
STORIES["quiz11_03"] = quiz_r("bg_immeuble_dore", "De ceux qui ont acheté",
    "Tu crois voir le fruit de son travail. Tu vois le résultat de ses ventes. "
    "Cette démonstration est une publicité, et ce que tu achètes ensuite, "
    "c'est elle. Devant un chiffre affiché, tu es le produit.")

STORIES["quiz11_04"] = quiz_q("bg_prairie", 2, 3, "Vrai ou faux ?",
    "Annoncer publiquement combien on gagne, c'est un gage de transparence.")
STORIES["quiz11_05"] = quiz_r("bg_ville_doree", "Faux",
    "C'est surtout s'interdire de faire moins un jour. S'il annonce moins "
    "l'année suivante, il n'est plus crédible. Alors il ne peut plus ralentir, "
    "plus prendre de vacances : il doit tenir le décor.")

STORIES["quiz11_06"] = quiz_q("bg_montagne", 3, 3, "Devant quelqu'un qui a vraiment réussi",
    "À quoi tu le reconnais ?")
STORIES["quiz11_07"] = quiz_r("bg_cles", "À son temps",
    "Pas à sa voiture, et surtout pas à son agenda plein. Celui qui répète "
    "qu'il n'a pas une minute court après l'argent. Celui qui ne regarde "
    "jamais son téléphone a déjà tout organisé.")

STORIES["quiz11_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {BIEN_JOUE}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? La vidéo entière est sur la chaîne : pourquoi il ne dit jamais '
    'combien il gagne, et les cinq questions à poser devant n\'importe quel chiffre.'
    '</div>'
    '</div></div>')

# --------------------------------------------------------------- sondages lies

STORIES["sondage11_01"] = sondage("bg_ble", "dis-nous franchement",
    f'Un chiffre affiché sur les réseaux : ton premier {REFLEXE}&nbsp;?')

STORIES["sondage11_02"] = sondage("bg_salon_vide", "question du jour",
    f'L\'argent que tu as gagné {ANNEE}, il est parti où&nbsp;?')

SLUG = "interactifs-11"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
