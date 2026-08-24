#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 07 — quiz et sondages tires de la video du 16/08/2026
« Comment remplir son calendrier en basse saison sans brader ses prix »
(ID YouTube iVd1TQ-GUYs). Transcription fournie par Martin le 24/08/2026.

Les trois questions portent sur ce qui surprend le plus dans la video : que
brader l'hiver se paie bien apres l'hiver, que le quota de nuitees se mange
meme sur un sejour d'un mois, et la duree reelle du bail mobilite.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.
⚠️ Les deux sondages ne repetent aucune question deja posee.

Rendu : python3 render_stories.py interactifs-07
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

STORIES["quiz07_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu es prêt pour la<br>{acc("basse saison")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz07_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Baisser tes prix tout l'hiver, ça n'a de conséquence que sur l'hiver.")
STORIES["quiz07_03"] = quiz_r("bg_ciel_dore", "Faux",
    "Ton prix moyen sur l'année nourrit ton positionnement. Brader tout "
    "l'hiver entraîne l'algorithme et les voyageurs à voir ton annonce comme "
    "pas chère, et remonter cette perception prend des mois.")

STORIES["quiz07_04"] = quiz_q("bg_prairie", 2, 3, "Résidence principale",
    "Un séjour d'un mois réservé sur une plateforme mange-t-il ton quota de nuitées ?")
STORIES["quiz07_05"] = quiz_r("bg_ville_doree", "Oui",
    "Il reste du meublé de tourisme, donc il compte dans tes 120 jours, ou 90 "
    "dans les grandes villes. Le bail mobilité, lui, n'entre pas dans ce "
    "calcul : ton compteur reste intact.")

STORIES["quiz07_06"] = quiz_q("bg_cles", 3, 3, "Le bail mobilité",
    "Il peut durer au maximum combien de temps ?")
STORIES["quiz07_07"] = quiz_r("bg_facade_pierre", "Dix mois",
    "De un à dix mois, non renouvelable, pour des personnes en mobilité : "
    "étudiants, stagiaires, apprentis, salariés en formation ou en mission. "
    "Créé par la loi Elan en 2018.")

STORIES["quiz07_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Solide.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Les huit techniques sont détaillées dans la vidéo sur la '
    'chaîne, de la plus simple à la plus puissante.</div>'
    '</div></div>')

CALENDRIER = acc("calendrier d'hiver")
BAIL = acc("bail mobilité")

STORIES["sondage07_01"] = sondage("bg_ble", "dis-nous franchement",
    f'Ton {CALENDRIER}, il ressemble à quoi&nbsp;?')

STORIES["sondage07_02"] = sondage("bg_salon_vide", "question du jour",
    f'Tu as déjà signé un {BAIL}&nbsp;?')

SLUG = "interactifs-07"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
