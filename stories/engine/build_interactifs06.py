#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 06 — quiz et sondages tires de « Comment remplir sa liasse fiscale
LMNP ». Transcription fournie par Martin le 20/08/2026 (voir
stories/robot/sources/liasse-fiscale-lmnp.md).

Les trois questions portent sur les erreurs que Sebastien designe lui-meme
comme les plus frequentes : le deficit qu'on croit deductible du revenu
global, l'amortissement qu'on croit capable de creuser un deficit, et le
depot de garantie qu'on oublie de declarer.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.
⚠️ Les deux sondages evitent les questions deja posees par les fournees
precedentes.

Rendu : python3 render_stories.py interactifs-06
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

STORIES["quiz06_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu maîtrises ta<br>{acc("déclaration")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz06_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "En location meublée non professionnelle, ton déficit se déduit de ton revenu global.")
STORIES["quiz06_03"] = quiz_r("bg_immeuble_dore", "Faux",
    "Il ne s'impute que sur tes futurs revenus de location meublée, pendant "
    "dix ans. Seul le loueur professionnel peut le déduire de son revenu "
    "global. C'est l'erreur la plus fréquente.")

STORIES["quiz06_04"] = quiz_q("bg_prairie", 2, 3, "L'amortissement",
    "Peut-il creuser un déficit quand tes charges dépassent déjà tes loyers ?")
STORIES["quiz06_05"] = quiz_r("bg_ville_doree", "Non",
    "L'article 39 C l'interdit : il est limité à tes loyers moins tes charges. "
    "Ce qui ne passe pas cette année est reporté sur les suivantes. Ce n'est "
    "pas perdu, c'est différé.")

STORIES["quiz06_06"] = quiz_q("bg_chemin_aube", 3, 3, "Vrai ou faux ?",
    "Un dépôt de garantie encaissé puis rendu au voyageur n'est pas à déclarer.")
STORIES["quiz06_07"] = quiz_r("bg_cles", "Faux",
    "S'il est passé sur ton compte, il entre dans tes recettes, même rendu. "
    "D'où l'intérêt de le bloquer par empreinte bancaire au lieu de "
    "l'encaisser.")

STORIES["quiz06_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Chapeau.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Le tutoriel complet est sur la chaîne : les formulaires un '
    'par un, l\'amortissement par composants, et les pièges du contrôle.</div>'
    '</div></div>')

DECLARATION = acc("déclaration")
JUSTIFICATIFS = acc("justificatifs")

STORIES["sondage06_01"] = sondage("bg_ble", "dis-nous comment tu fais",
    f'Ta {DECLARATION} de location meublée, tu la fais comment&nbsp;?')

STORIES["sondage06_02"] = sondage("bg_salon_vide", "question du jour",
    f'Tes {JUSTIFICATIFS} de l\'année, ils sont où&nbsp;?')

SLUG = "interactifs-06"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
