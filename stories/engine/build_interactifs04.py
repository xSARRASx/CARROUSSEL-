#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 04 — quiz et sondages tires de la video du 09/08/2026
« Bailleur meuble : ces obligations de septembre vont tout changer »
(ID YouTube JgFFL6no9OQ).

Le quiz porte sur les DEUX confusions que Sebastien corrige explicitement dans
la video, parce que ce sont celles qui circulent partout :
    1. « exonere de TVA, donc pas concerne » -> faux, assujetti n'est pas
       redevable, un SIREN suffit ;
    2. ce qui est reellement obligatoire au 1er septembre -> RECEVOIR, pas
       emettre ;
    3. ce que dit le rapport du 8 juillet -> plafonner les taux
       d'amortissement, PAS supprimer le statut.

⚠️ Chaque question a son entree dans stickers.py (regle de Martin du
06/08/2026) : type de sticker, question exacte, options exactes, bonne
reponse. Le sticker utilise est le SONDAGE, jamais le Quiz d'Instagram, qui
revelerait la reponse au moment du vote et viderait la story suivante.

Gabarits quiz_q / quiz_r / sondage : partages dans photo_style.py.
Fonds tous differents a l'interieur de la sequence.

Rendu : python3 render_stories.py interactifs-04
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

# ============================================================================
# QUIZ — la rentree du bailleur en meuble
# ============================================================================

STORIES["quiz04_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu es prêt pour<br>la {acc("rentrée 2026")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz04_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Tu es exonéré de TVA, donc la facturation électronique ne te concerne pas.")
STORIES["quiz04_03"] = quiz_r("bg_immeuble_dore", "Faux",
    "Être assujetti et être redevable, ce n'est pas la même chose. "
    "L'exonération porte sur tes loyers, pas sur ton statut d'opérateur "
    "économique. Un numéro de SIREN suffit à te mettre dans le circuit.")

STORIES["quiz04_04"] = quiz_q("bg_prairie", 2, 3, "Au 1er septembre",
    "Qu'est-ce qui devient vraiment obligatoire pour toi ?")
STORIES["quiz04_05"] = quiz_r("bg_ville_doree", "Recevoir",
    "Tu dois pouvoir RECEVOIR les factures de ta conciergerie, de tes "
    "artisans, de ton comptable. Émettre ne concerne que les redevables de "
    "la TVA. Inutile de payer un logiciel de facturation pour ça.")

STORIES["quiz04_06"] = quiz_q("bg_montagne", 3, 3, "Vrai ou faux ?",
    "Le rapport du 8 juillet recommande de supprimer le statut LMNP.")
STORIES["quiz04_07"] = quiz_r("bg_cles", "Faux",
    "Il recommande de plafonner les taux d'amortissement au régime réel. "
    "Ni le statut, ni le régime réel ne sont remis en cause. Et à ce jour, "
    "rien n'est voté : c'est un rapport, pas une loi.")

STORIES["quiz04_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Bien joué.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Tout est détaillé dans la vidéo sur la chaîne : ce qui est '
    'obligatoire, ce qui ne l\'est pas, et comment se mettre en règle.</div>'
    '</div></div>')

# --------------------------------------------------------------- sondages liés

FACTURATION = acc("facturation électronique")
REGIME = acc("régime")

STORIES["sondage04_01"] = sondage("bg_ble", "dis-nous où tu en es",
    f'Tu es enregistré pour la {FACTURATION}&nbsp;?')

STORIES["sondage04_02"] = sondage("bg_salon_vide", "question du jour",
    f'Tu es à quel {REGIME} aujourd\'hui&nbsp;?')

SLUG = "interactifs-04"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
