#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 10 — quiz et sondages tires de la video du 02/09/2026
« Frais Airbnb : Ce qui change vraiment pour les hotes » (ID ARDRtYtIgSk).

Le quiz porte sur les TROIS points que Sebastien corrige explicitement, parce
que ce sont ceux qui circulent faux dans les groupes :
    1. « Airbnb lance la reservation en direct » -> FAUX, la reservation reste
       entierement sur Airbnb, c'est un tarif reduit, pas du direct ;
    2. le curseur qui reverse l'economie au voyageur -> on n'y touche PAS ;
    3. ce que l'ecart 15,5 -> 6 revele -> 9,5 points, le prix qu'Airbnb met
       lui-meme sur « trouver le client ».

⚠️ Chaque question a son entree dans stickers.py (regle de Martin du
06/08/2026) : type de sticker, question exacte, options exactes, bonne
reponse. Le sticker utilise est le SONDAGE, jamais le Quiz d'Instagram, qui
revelerait la reponse au moment du vote et viderait la story suivante.

Gabarits quiz_q / quiz_r / sondage : partages dans photo_style.py.
Fonds tous differents a l'interieur de la sequence.

Rendu : python3 render_stories.py interactifs-10
"""
from photo_style import (open_photo, underline, acc, BLANC,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

# ============================================================================
# QUIZ — la commission a 6 %
# ============================================================================

STORIES["quiz10_01"] = (
    open_photo("bg_escalier") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    '<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu as suivi<br>l\'affaire des {acc("6 %")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz10_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Avec le lien à 6 %, Airbnb lance enfin la réservation en direct.")
STORIES["quiz10_03"] = quiz_r("bg_immeuble_dore", "Faux",
    "Tout reste sur Airbnb : la messagerie, la protection, les avis. Ce n'est "
    "pas du direct, c'est une réservation Airbnb à tarif réduit, parce que le "
    "client, c'est toi qui l'as amené.")

STORIES["quiz10_04"] = quiz_q("bg_prairie", 2, 3, "Le fameux curseur",
    "Il propose de reverser une partie de l'économie au voyageur. Tu en fais quoi ?")
STORIES["quiz10_05"] = quiz_r("bg_ville_doree", "Tu n'y touches pas",
    "Le gain, c'est ta marge, pas une réduction. Si tu en rends la moitié, "
    "l'économie fond et ta clientèle apprend à attendre des remises. Offre un "
    "service, jamais du prix.")

STORIES["quiz10_06"] = quiz_q("bg_montagne", 3, 3, "15,5 % d'un côté, 6 % de l'autre",
    "Cet écart, il chiffre quoi exactement ?")
STORIES["quiz10_07"] = quiz_r("bg_cles", "9,5 points",
    "C'est le prix qu'Airbnb met lui-même sur le fait de trouver le client. "
    "Sur une réservation de 1 000 €, 95 € d'acquisition et 60 € pour la "
    "transaction. Ta base client vaut donc 9,5 points.", chiffre="9,5")

STORIES["quiz10_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Bien joué.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Tout est décortiqué dans la vidéo sur la chaîne : ce que le '
    'test dit vraiment, les trois pièges, et quel canal pour quel voyageur.'
    '</div>'
    '</div></div>')

# --------------------------------------------------------------- sondages lies

# Les apostrophes ne passent pas dans une expression de f-string.
ANNEE = acc("l'année")
RESERVE = acc("réserve")

STORIES["sondage10_01"] = sondage("bg_ble", "dis-nous où tu en es",
    f'Tes voyageurs de {ANNEE}, tu peux en recontacter combien sans Airbnb&nbsp;?')

STORIES["sondage10_02"] = sondage("bg_salon_vide", "question du jour",
    f'Un ancien voyageur revient. Il {RESERVE} par où&nbsp;?')

SLUG = "interactifs-10"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
