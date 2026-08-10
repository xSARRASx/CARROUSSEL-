#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 03 — quiz et sondages tirés de la vidéo du dimanche
(ta copropriété peut interdire ton Airbnb, ID sICVVkMpSl4).

La story pose la question et laisse la moitié basse LIBRE : Martin y colle le
sticker SONDAGE Instagram. La story suivante révèle la réponse.

⚠️ Sticker SONDAGE, pas Quiz : le sticker Quiz d'Instagram révèle la bonne
réponse à l'instant du vote, ce qui viderait la story de réponse de son
intérêt. Erreur reperee par Martin le 08/08/2026, corrigee dans stickers.py.

Aucun CTA mot-clé sur ces formats (règle de Martin).
Style unique photo fait main, logo partout, fonds tous différents.

Rendu : python3 render_stories.py interactifs-03
"""
from photo_style import (open_photo, underline, acc, nb, BLANC, BLEU,
                         quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

STORIES["quiz03_01"] = (
    open_photo("bg_mer_calme") + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Ta copro peut-elle te {acc("couper")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions sur le vote<br>'
    'en assemblée générale. La réponse arrive après.</div>'
    '</div></div>')

STORIES["quiz03_02"] = quiz_q("bg_prairie", 1, 3, "Vrai ou faux ?",
    "Depuis la loi Le Meur, il faut l'unanimité de la copropriété pour interdire les meublés de tourisme.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz03_03"] = quiz_r("bg_plage_aube", "Faux",
    "C'était vrai AVANT : il fallait changer la destination de l'immeuble, à l'unanimité. "
    "Aujourd'hui l'assemblée générale peut interdire à la majorité des deux tiers. Et si "
    "les deux tiers ne sont pas atteints, un second vote peut faire passer la résolution "
    "à la majorité de tous les copropriétaires.")

STORIES["quiz03_04"] = quiz_q("bg_ble", 2, 3, "Vrai ou faux ?",
    "Pour la Cour de cassation, louer en courte durée sur Airbnb est une activité commerciale.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz03_05"] = quiz_r("bg_ciel_rose", "Faux",
    "La Cour de cassation a répondu le 25 janvier 2024, et c'est très clair : non, tant "
    "que tu ne fournis pas de services para-hôteliers. Ménage optionnel, remise de clés, "
    "petit-déjeuner en option : ça reste civil. Et c'est exactement là qu'est la parade.")

STORIES["quiz03_06"] = quiz_q("bg_salon_cosy", 3, 3, "Qui fait quoi ?",
    "Tu déclares ton meublé en mairie. Qui met ensuite le sujet à l'ordre du jour de l'assemblée générale ?",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz03_07"] = quiz_r("bg_montagne", "Le syndic",
    "Tu dois informer ton syndic, et le syndic doit inscrire un point d'information à "
    "l'ordre du jour de la prochaine assemblée générale. Autrement dit : ta déclaration "
    "légale déclenche toute seule le débat sur ton activité.")

STORIES["quiz03_08"] = (
    open_photo("bg_lac") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Solide.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Tout est détaillé dans la vidéo sur la chaîne : les trois conditions '
    'du vote, les deux arrêts qui changent tout, et la checklist à faire avant '
    'd\'acheter ou de signer.</div>'
    '</div></div>')

# --------------------------------------------------------------- sondages liés

REGLEMENT = acc("règlement de copropriété")
VOYAGEURS = acc("voyageurs")

STORIES["sondage03_01"] = sondage("bg_terrasse", "sois honnête",
    f"Tu as déjà lu le {REGLEMENT} de ton logement&nbsp;?",
    "vote juste en dessous")
STORIES["sondage03_02"] = sondage("bg_ville_doree", "question du jour",
    f"Tu proposes quoi à tes {VOYAGEURS}&nbsp;?",
    "vote juste en dessous")

SLUG = "interactifs-03"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
