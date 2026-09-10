#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 12 — quiz et sondages tires de la video du 09/09/2026
« Le fisc vous surveille : les 3 signes qui alertent sur votre residence »
(ID lc1huihoLio).

Le quiz porte sur les TROIS idees fausses que la video corrige :
    1. « j'ai tous mes papiers a cette adresse, donc c'est ma residence
       principale » -> non, c'est la facture d'electricite qui a tranche ;
    2. « il faut y habiter au moins six mois / un an » -> aucune duree
       minimale n'existe dans la loi (un amendement propose cinq ans, non vote) ;
    3. un couple divorce qui vend -> l'exoneration s'apprecie SEPAREMENT pour
       chaque vendeur.

⚠️ Chaque question a son entree dans stickers.py (regle de Martin du
06/08/2026). Le sticker utilise est le SONDAGE, jamais le Quiz d'Instagram,
qui revelerait la reponse au moment du vote et viderait la story suivante.

Gabarits quiz_q / quiz_r / sondage : partages dans photo_style.py.
Fonds tous differents a l'interieur de la sequence.

Rendu : python3 render_stories.py interactifs-12
"""
from photo_style import (open_photo, underline, acc, BLANC,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

# Les apostrophes ne passent pas dans une expression de f-string.
PRINCIPALE = acc("résidence principale")
BIEN_JOUE = acc("Bien joué.")
DEJA_OUVERTE = acc("déjà ouverte")
PROUVER = acc("prouver")

# ============================================================================
# QUIZ — la residence principale sous controle
# ============================================================================

STORIES["quiz12_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    '<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu connais les règles<br>de la {PRINCIPALE}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz12_02"] = quiz_q("bg_ciel_rose", 1, 3, "Déclaration, courriers, relevés bancaires",
    "Tous ses papiers étaient à cette adresse. Qu'est-ce qui l'a fait perdre ?")
STORIES["quiz12_03"] = quiz_r("bg_immeuble_dore", "Sa facture d'électricité",
    "Sur une année entière, sa consommation était inférieure à celle d'un "
    "simple réfrigérateur. Le juge en a conclu que personne ne vivait dans le "
    "logement. Exonération refusée, confirmée en appel.")

STORIES["quiz12_04"] = quiz_q("bg_prairie", 2, 3, "Combien de temps faut-il y habiter",
    "pour que le bien compte comme ta résidence principale ?")
STORIES["quiz12_05"] = quiz_r("bg_ville_doree", "Aucune durée",
    "La loi ne fixe ni durée minimale d'occupation ni seuil de consommation. "
    "Tout se juge sur un faisceau d'indices. Un amendement propose cinq ans de "
    "détention, mais il n'est pas voté.")

STORIES["quiz12_06"] = quiz_q("bg_montagne", 3, 3, "Un couple divorcé vend la maison",
    "L'un y vivait encore, l'autre était parti. Il se passe quoi ?")
STORIES["quiz12_07"] = quiz_r("bg_cles", "Deux traitements",
    "L'exonération s'apprécie séparément pour chaque vendeur. Celui qui "
    "habitait encore les lieux est exonéré sur sa moitié, celui qui était "
    "parti est taxé sur la sienne. Même maison, même acte notarié.")

STORIES["quiz12_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {BIEN_JOUE}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? La vidéo entière est sur la chaîne : les trois décisions de '
    'justice, la majoration de 40 %, et la fiche que le fisc tient sur ton bien.'
    '</div>'
    '</div></div>')

# --------------------------------------------------------------- sondages lies

STORIES["sondage12_01"] = sondage("bg_ble", "sois honnête",
    f'Ta fiche « Gérer mes biens immobiliers », tu l\'as {DEJA_OUVERTE}&nbsp;?')

STORIES["sondage12_02"] = sondage("bg_salon_vide", "question du jour",
    f'Pour {PROUVER} que tu vis chez toi, tu sortirais quoi&nbsp;?')

SLUG = "interactifs-12"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
