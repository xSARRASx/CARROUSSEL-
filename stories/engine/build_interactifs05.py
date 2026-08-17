#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 05 — quiz et sondages tires de la video du 12/08/2026
« Un proprietaire Airbnb vient d'ECRASER sa copropriete au tribunal »
(ID YouTube keONb-XUtJY).

Le quiz porte sur les trois points du jugement qui se retiennent mal et qui
changent tout en assemblee generale : la nature civile, la regle des trois
prestations para-hotelieres, et le delai de contestation.

⚠️ Les deux sondages evitent volontairement les questions deja posees par
interactifs-03 (« as-tu lu ton reglement de copropriete », « que proposes-tu a
tes voyageurs ») : poser deux fois la meme question a la communaute est une
erreur relevee par Martin le 08/08/2026.

⚠️ Chaque question a son entree dans stickers.py. Sticker SONDAGE, jamais Quiz.

Rendu : python3 render_stories.py interactifs-05
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

# ============================================================================
# QUIZ — le jugement de Nice
# ============================================================================

STORIES["quiz05_01"] = (
    open_photo("bg_mer_calme") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu tiendrais face à<br>ta {acc("copropriété")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz05_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Louer en courte durée est une activité commerciale.")
STORIES["quiz05_03"] = quiz_r("bg_ciel_dore", "Faux",
    "Sans prestation para-hôtelière, l'activité est civile. La Cour de "
    "cassation l'a jugé le 25 janvier 2024. Être imposé en bénéfices "
    "industriels et commerciaux ne change rien à cette nature juridique.")

STORIES["quiz05_04"] = quiz_q("bg_prairie", 2, 3, "Article 261 D",
    "Combien de prestations para-hôtelières faut-il cumuler pour basculer dans le commercial ?")
STORIES["quiz05_05"] = quiz_r("bg_ville_doree", "Trois",
    "Petit-déjeuner, nettoyage régulier en cours de séjour, linge de maison, "
    "réception de la clientèle. Il en faut au moins trois pour basculer. Le "
    "ménage de fin de séjour, lui, n'est pas un critère.")

STORIES["quiz05_06"] = quiz_q("bg_chemin_aube", 3, 3, "Ton assemblée vote contre toi",
    "Tu as combien de temps pour contester la résolution ?")
STORIES["quiz05_07"] = quiz_r("bg_cles", "2 mois",
    "Passé ce délai, la résolution devient définitive. C'est court : dès "
    "qu'un procès-verbal d'assemblée arrive, lis-le tout de suite.")

STORIES["quiz05_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Solide.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Le jugement est décortiqué en entier dans la vidéo sur la '
    'chaîne, avec les cinq points sur lesquels la copropriété est tombée.</div>'
    '</div></div>')

# --------------------------------------------------------------- sondages liés

ORDRE_DU_JOUR = acc("ordre du jour")
PREUVES = acc("preuves")

STORIES["sondage05_01"] = sondage("bg_ble", "dis-nous franchement",
    f'La courte durée est déjà passée à l\'{ORDRE_DU_JOUR} chez toi&nbsp;?')

STORIES["sondage05_02"] = sondage("bg_salon_vide", "question du jour",
    f'Tu aurais des {PREUVES} si on t\'accusait de nuisances&nbsp;?')

SLUG = "interactifs-05"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
