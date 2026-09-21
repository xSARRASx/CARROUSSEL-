#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 15 — tires de la video du 20/09/2026 « Expatrie : le mythe des
183 jours va te couter tres cher » (ID ZdEMuAtcJcE).

⚠️ ENCORE UN FORMAT DIFFERENT (Martin, 10/09/2026). Le lot 13 avait deux
questions, le 14 en avait trois classiques, celui-ci est en VRAI OU FAUX : le
mot en gros et la consigne viennent de quiz_ouverture(15), qui tombe sur cette
variante. Trois affirmations, et volontairement PAS trois « faux » d'affilee --
une seule est fausse, les deux autres sont vraies et contre-intuitives.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.

Rendu : python3 render_stories.py interactifs-15
"""
from photo_style import (open_photo, underline, acc, BLANC,
                         quiz_q, quiz_r, sondage, write_lot,
                         quiz_ouverture, quiz_cloture)

NUM_LOT = 15
CONSIGNE, MOT = quiz_ouverture(NUM_LOT)
SCORE, RENVOI = quiz_cloture(NUM_LOT)

STORIES = {}

EXPATRIER = acc("t'expatrier")
PENSES = acc("y penses")
FERAIS = acc("ferais")

STORIES["quiz15_01"] = (
    open_photo("bg_toits_pluie") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:110px;line-height:1.05;">{MOT}</div>'
    '<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu saurais vraiment<br>{EXPATRIER}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    f'<div class="hand" style="font-size:48px;line-height:1.3;">{CONSIGNE}</div>'
    '</div></div>')

STORIES["quiz15_02"] = quiz_q("bg_etagere", 1, 3, "Vrai ou faux ?",
    "Passer moins de 183 jours en France suffit à ne plus être résident fiscal français.")
STORIES["quiz15_03"] = quiz_r("bg_foret_automne", "Faux",
    "Ce critère ne joue que dans un sens. Il y en a quatre, et un seul suffit : "
    "le foyer, les jours, l'activité principale, et d'où vient ton argent. Un "
    "directeur général n'a passé que 144 jours en France et a quand même été "
    "jugé résident fiscal français.")

STORIES["quiz15_04"] = quiz_q("bg_bureau_papiers", 2, 3, "Vrai ou faux ?",
    "En partant vivre à l'étranger, l'impôt sur tes loyers français augmente souvent.")
STORIES["quiz15_05"] = quiz_r("bg_champ_ete", "Vrai",
    "En non-résident, le taux part d'un minimum de 20 % et monte à 30 % au-delà "
    "d'environ 29 000 € imposables. Un résident aux revenus modestes paierait "
    "0 ou 11 %. Partir n'allège pas cette facture-là.")

STORIES["quiz15_06"] = quiz_q("bg_mur_beton", 3, 3, "Vrai ou faux ?",
    "Depuis 2025, le fisc a dix ans pour contester ton départ à l'étranger.")
STORIES["quiz15_07"] = quiz_r("bg_cafe_table", "Vrai",
    "La loi de finances 2025 a porté le délai de reprise de trois à dix ans en "
    "cas de fausse domiciliation. Pars en 2026, tu peux recevoir un courrier "
    "jusqu'en 2036. D'où l'intérêt de garder ses preuves.", chiffre="10 ans")

STORIES["quiz15_08"] = (
    open_photo("bg_rideau") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">{SCORE}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    f'{RENVOI} Les quatre critères, les deux nouveautés de 2025, et ce qui '
    'arrive à la maison qu\'on garde « au cas où ».'
    '</div>'
    '</div></div>')

STORIES["sondage15_01"] = sondage("bg_ciel_rose", "dis-nous franchement",
    f'T\'expatrier, tu {PENSES} vraiment&nbsp;?')

STORIES["sondage15_02"] = sondage("bg_village", "question du jour",
    f'Si tu partais, ton bien en France, tu en {FERAIS} quoi&nbsp;?')

SLUG = "interactifs-15"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
