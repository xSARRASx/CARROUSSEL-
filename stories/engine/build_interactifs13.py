#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 13 — tires de la video du 13/09/2026 « Les 5 erreurs qui
declenchent un controle fiscal pour les hotes Airbnb » (ID h0fE0L6d5QI).

⚠️ FORMAT VOLONTAIREMENT DIFFERENT (Martin, 10/09/2026 : « tout le temps des
choses differentes »). Les douze lots precedents suivaient tous le meme moule :
couverture, TROIS questions, cloture, deux sondages, dix stories. Martin voit
ce lot TOUS LES SAMEDIS -- c'est la ou la repetition se voit le plus.
Ici : DEUX questions au lieu de trois, UN seul sondage, sept stories au lieu de
dix. Moins, mais pas le meme.

Les deux questions portent sur les deux idees fausses les plus repandues, celles
que Sebastien corrige explicitement :
    1. « je declare ce que j'ai recu sur mon compte » -> non, c'est le montant
       BRUT, avant commission ;
    2. au-dela de 23 000 € de recettes, ce qui se declenche -> les cotisations
       d'indepenant (35 a 45 % du benefice), pas le statut professionnel.

⚠️ Chaque question a son entree dans stickers.py (regle de Martin du
06/08/2026). Sticker SONDAGE, jamais Quiz.

Rendu : python3 render_stories.py interactifs-13
"""
from photo_style import (open_photo, underline, acc, BLANC,
                         quiz_q, quiz_r, sondage, write_lot, quiz_cloture)

NUM_LOT = 13
SCORE, RENVOI = quiz_cloture(NUM_LOT)

STORIES = {}

CONTROLE = acc("contrôle")
DECLARES = acc("déclares")

# ---------------------------------------------------------------- couverture
# ⚠️ Consigne ecrite pour DEUX questions : les listes tournantes de
# photo_style annoncent toutes « trois questions ». Elle est propre a ce lot.
STORIES["quiz13_01"] = (
    open_photo("bg_cuisine_matin") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div class="serif" style="font-size:150px;line-height:1;">2 QUESTIONS</div>'
    '<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Ta déclaration tiendrait<br>face à un {CONTROLE}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">Deux seulement, mais ce sont<br>'
    'les deux qui coûtent le plus cher.</div>'
    '</div></div>')

STORIES["quiz13_02"] = quiz_q("bg_champ_ete", 1, 2, "Airbnb te verse 17 000 €",
    "après avoir retenu sa commission. Tu déclares combien ?")
STORIES["quiz13_03"] = quiz_r("bg_foret_automne", "Le montant brut",
    "C'est la somme payée par le voyageur, avant commission et frais de ménage "
    "inclus, qui se déclare. La commission devient ensuite une charge "
    "déductible au réel. Déclarer le net reçu crée un écart avec ce que la "
    "plateforme a transmis.")

STORIES["quiz13_04"] = quiz_q("bg_neige_douce", 2, 2, "Au-delà de 23 000 € de recettes",
    "dans l'année, qu'est-ce qui se déclenche ?")
STORIES["quiz13_05"] = quiz_r("bg_rideau", "Les cotisations",
    "L'affiliation devient obligatoire, avec des cotisations d'indépendant "
    "entre 35 et 45 % du bénéfice, et un minimum forfaitaire même à zéro. Ce "
    "n'est pas le statut de loueur professionnel : celui-ci demande en plus "
    "que tes recettes dépassent les autres revenus du foyer.")

STORIES["quiz13_06"] = (
    open_photo("bg_ruelle") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">{SCORE}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    f'{RENVOI} La transmission automatique des plateformes, le seuil de '
    '23 000 € et les petites taxes qui ouvrent un contrôle.'
    '</div>'
    '</div></div>')

# ------------------------------------------------------------- un seul sondage
STORIES["sondage13_01"] = sondage("bg_balcon", "dis-nous où tu en es",
    f'Ce que tu {DECLARES}, tu le prends où&nbsp;?')

SLUG = "interactifs-13"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
