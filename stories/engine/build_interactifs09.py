#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 09 — quiz et sondages tires de « Menage Airbnb : le business cache
qui rapporte gros » (sWiie3c__Lo). Transcription fournie par Martin le
31/08/2026.

Les trois questions portent sur les idees a contre-courant de la video : le
vrai probleme des conciergeries, le critere numero un du choix d'un
prestataire, et ce que rapporte le fait d'ajouter le linge.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.

Rendu : python3 render_stories.py interactifs-09
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

STORIES["quiz09_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu connais le marché<br>du {acc("ménage Airbnb")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz09_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Le principal problème des conciergeries, c'est de trouver des propriétaires.")
STORIES["quiz09_03"] = quiz_r("bg_ciel_dore", "Faux",
    "Vu depuis des centaines de comptes, c'est de trouver des équipes de "
    "ménage fiables. Des missions à 60, 70, 80 € restent sans personne pour "
    "les prendre.")

STORIES["quiz09_04"] = quiz_q("bg_prairie", 2, 3, "Une conciergerie choisit",
    "Son prestataire de ménage, elle le choisit d'abord sur quoi ?")
STORIES["quiz09_05"] = quiz_r("bg_cles", "La fiabilité",
    "Avant le prix, et de loin. Un logement pas fait un dimanche, c'est un "
    "voyageur qui arrive dans la saleté, une mauvaise note, et la relation "
    "qui s'arrête là.")

STORIES["quiz09_06"] = quiz_q("bg_lac", 3, 3, "Le linge en plus du ménage",
    "Ceux qui proposent les deux facturent combien de plus ?")
STORIES["quiz09_07"] = quiz_r("bg_village", "20 à 30 %",
    "La moitié des conciergeries cherchent une prestation tout inclus. "
    "Proposer le linge en plus du ménage, c'est le moyen le plus simple de "
    "monter son tarif sans discussion.")

STORIES["quiz09_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Impeccable.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Les tarifs, la fenêtre horaire et la façon de décrocher les '
    'premiers contrats sont détaillés dans la vidéo sur la chaîne.</div>'
    '</div></div>')

MENAGE = acc("ménage")
FIABLE = acc("fiable")

STORIES["sondage09_01"] = sondage("bg_ble", "dis-nous comment tu fais",
    f'Le {MENAGE} de tes logements, c\'est qui&nbsp;?')

STORIES["sondage09_02"] = sondage("bg_cour", "question du jour",
    f'Trouver quelqu\'un de {FIABLE}, c\'est dur chez toi&nbsp;?')

SLUG = "interactifs-09"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
