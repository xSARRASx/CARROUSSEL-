#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 08 — quiz et sondages tires de la video du 26/08/2026
« Comment faire baisser sa taxe fonciere » (h0GZh51rtCk).
Transcription fournie par Martin le 27/08/2026.

Les trois questions portent sur ce qui surprend vraiment : la surface qui n'est
pas la surface reelle, la fiche gratuite que presque personne ne reclame, et
le piege de la revision qui marche dans les deux sens.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.

Rendu : python3 render_stories.py interactifs-08
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

STORIES["quiz08_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu connais ta<br>{acc("taxe foncière")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz08_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Ta taxe foncière est calculée sur la surface réelle de ton logement.")
STORIES["quiz08_03"] = quiz_r("bg_ciel_dore", "Faux",
    "Elle est calculée sur une surface pondérée. Ta cave compte pour 20 %, ton "
    "garage pour 60 %, et chaque équipement de confort ajoute des mètres "
    "carrés fictifs. Tu peux payer bien plus de mètres que tu n'en habites.")

STORIES["quiz08_04"] = quiz_q("bg_prairie", 2, 3, "La fiche d'évaluation",
    "Ce document sur lequel repose tout le calcul, il coûte combien ?")
STORIES["quiz08_05"] = quiz_r("bg_ville_doree", "Rien",
    "Elle est gratuite, c'est ton droit, il suffit de la demander au centre "
    "des impôts. Elle n'arrive jamais avec ton avis, et 99 % des "
    "propriétaires ne l'ont jamais vue.")

STORIES["quiz08_06"] = quiz_q("bg_chemin_aube", 3, 3, "Vrai ou faux ?",
    "Réclamer ne peut que faire baisser ta taxe, jamais monter.")
STORIES["quiz08_07"] = quiz_r("bg_cles", "Faux",
    "La révision marche dans les deux sens. Si tu as ajouté une véranda, une "
    "piscine ou une salle de bain, elle peut être réévaluée à la hausse. "
    "Vérifie que l'écart joue pour toi avant de réclamer.")

STORIES["quiz08_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Bravo.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Le calcul est décortiqué maillon par maillon dans la vidéo '
    'sur la chaîne, avec les cinq erreurs les plus fréquentes.</div>'
    '</div></div>')

FICHE = acc("fiche d'évaluation")
AUGMENTE = acc("augmenté")

STORIES["sondage08_01"] = sondage("bg_ble", "dis-nous où tu en es",
    f'Tu as déjà demandé ta {FICHE}&nbsp;?')

STORIES["sondage08_02"] = sondage("bg_montagne", "question du jour",
    f'Ta taxe foncière a {AUGMENTE} de combien cette année&nbsp;?')

SLUG = "interactifs-08"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
