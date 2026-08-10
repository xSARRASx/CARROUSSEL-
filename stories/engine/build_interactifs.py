#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FORMATS INTERACTIFS (voix de Martin, 04/08/2026 au soir) :
  - "pas toujours des trucs a repondre" -> CTA legers, pas de mot-cle partout
  - "des questionnaires, des questions-reponses" -> sequences QUIZ (la story
    pose la question, Martin ajoute le sticker sondage Instagram dans la zone
    libre ; la story suivante donne la reponse et l'explication)
  - "garder des trucs pour les temoignages, la derniere annonce de nos eleves,
    avec case vide pour mettre des photos" -> gabarits temoignage a zone
    pointillee (les SEULS avec placeholder, volontairement)

MISES A JOUR (03/08/2026, decisions de Martin) :
  - STYLE UNIQUE "photo fait main" partout (plus de theme navy pour les quiz)
  - LOGO sur toutes les stories, quiz et sondages inclus (l'ancienne regle
    "pas de logo" est annulee par Martin : "le logo absolument partout")
  - FONDS VARIES : jamais deux fois le meme fond dans une sequence

Rendu : python3 render_stories.py interactifs-01
"""
from photo_style import (open_photo, underline, arrow_down, acc, nb,
                         BLANC, BLEU, BLEUF, quiz_q, quiz_r, sondage, write_lot)

STORIES = {}

# ============================================================================
# QUIZ — la story pose la question et laisse la moitie basse LIBRE :
# Martin y colle le sticker sondage Instagram (vrai/faux ou QCM).
# La story suivante revele la reponse. Contenu tire des videos (algo, caution).
#
# Les gabarits quiz_q / quiz_r / sondage viennent de photo_style.py depuis le
# 10/08/2026 : une correction de style profite ainsi a TOUTES les fournees,
# anciennes comprises (avant, chaque build en gardait sa copie et les
# corrections ne se propageaient pas).
# ============================================================================

STORIES["quiz_01"] = (
    open_photo("bg_bureau_matin") + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:54px;line-height:1.2;margin-top:36px;">'
    f'T\'es à jour sur<br>{acc("Airbnb 2026")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions. Vote à chaque fois,<br>'
    'la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz_02"] = quiz_q("bg_ciel_rose", 1, 3, "Vrai ou faux ?",
    "Le badge Superhost booste ton classement en 2026.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz_03"] = quiz_r("bg_lac", "Faux",
    "Le Superhost est obsolète. Le nouveau Graal, c'est Guest Favorite : "
    "25 % du classement. Critères : note 4,9+ et au moins 5 avis en 2 ans.")

STORIES["quiz_04"] = quiz_q("bg_terrasse", 2, 3, "8, 15 ou 30 ?",
    "Combien pèse ta photo de couverture dans ton classement (en %) ?",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz_05"] = quiz_r("bg_montagne", "8 %",
    "Et le séjour réel pèse 50 %. Réservations, avis, zéro problème : c'est ça "
    "que l'algorithme regarde en premier. La photo vient après.")

STORIES["quiz_06"] = quiz_q("bg_village", 3, 3, "Vrai ou faux ?",
    "Ta conciergerie peut débiter elle-même la caution du voyageur.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz_07"] = quiz_r("bg_immeuble_dore", "Faux",
    "Si la conciergerie déclenche le débit, c'est du maniement de fonds pour "
    "le compte de tiers : illégal au sens de la loi Hoguet. La caution part "
    "toujours du compte du propriétaire.")

STORIES["quiz_08"] = (
    open_photo("bg_plage_aube") + '<div class="scrim"></div>'
    + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Respect.")}</div>'
    '<div class="libre" style="max-width:830px;margin-top:52px;">'
    'Moins&nbsp;? Tout est expliqué en détail dans les vidéos de la chaîne. '
    'On en refait un bientôt.</div>'
    '</div></div>')

# ============================================================================
# SONDAGES DIAGNOSTIC — zones libres pour les stickers Instagram
# (sondage / boite a questions). Aucun CTA mot-cle.
# Gabarit sondage() partage : voir photo_style.py.
# ============================================================================

STORIES["sondage_01"] = sondage("bg_ciel_dore", "dis-nous tout",
    f'Tu es plutôt {acc("conciergerie")} ou {acc("sous-location")}&nbsp;?',
    "vote juste en dessous")
STORIES["sondage_02"] = sondage("bg_prairie", "question du jour",
    f'Ta plus grosse {acc("galère")} en ce moment&nbsp;?',
    "vote juste en dessous")
STORIES["sondage_03"] = sondage("bg_ville_doree", "on lit tout",
    f'Raconte ta {acc("situation")} en une phrase.',
    "la boîte à questions est juste là")

# ============================================================================
# TEMOIGNAGES — les SEULS gabarits avec case vide (pointilles) :
# Martin colle l'annonce / le screenshot de l'eleve dans Instagram
# (sticker photo). Ne jamais inventer un temoignage.
# ============================================================================

def fleche_temoin(x, y, w=200, h=240):
    path = f"M {w*0.85:.0f} 18 C {w*0.3:.0f} {h*0.25:.0f}, {w*0.1:.0f} {h*0.55:.0f}, {w*0.4:.0f} {h-26:.0f}"
    head = (f'<path d="M {w*0.4-32:.0f} {h-88:.0f} L {w*0.4:.0f} {h-22:.0f}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>'
            f'<path d="M {w*0.4+28:.0f} {h-82:.0f} L {w*0.4:.0f} {h-22:.0f}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>')
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" fill="none">'
            f'<path d="{path}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>{head}</svg>')

def case_vide(x, y, w, h, note):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            'border:5px dashed rgba(255,255,255,0.8);border-radius:26px;"></div>'
            f'<div class="hand" style="font-size:44px;position:absolute;left:{x+50}px;'
            f'top:{y+h//2-30}px;color:rgba(255,255,255,0.95);">{nb(note)}</div>')

STORIES["temoin_01"] = (
    open_photo("bg_mer_calme") + '<div class="pad">'
    f'<div class="serif" style="font-size:80px;line-height:1.1;text-align:right;margin-top:20px;">'
    f'+&nbsp;1 pour {acc("[Prénom]")}</div>'
    + fleche_temoin(700, 460) + case_vide(110, 640, 540, 700, "colle l'annonce<br>de l'élève ici")
    + '<div class="hand" style="font-size:60px;position:absolute;right:100px;bottom:420px;">'
    'Bravo [Prénom]&nbsp;!</div>'
    '</div></div>')

STORIES["temoin_02"] = (
    open_photo("bg_plage_aube") + '<div class="pad">'
    '<div class="hand" style="font-size:56px;margin-top:10px;">tombé ce matin</div>'
    f'<div class="serif" style="font-size:64px;line-height:1.15;margin-top:20px;">'
    f'La {acc("dernière annonce")} de nos élèves.</div>'
    + case_vide(190, 620, 700, 760, "le screenshot ici")
    + '</div></div>')

STORIES["temoin_03"] = (
    open_photo("bg_lac") + '<div class="pad">'
    '<div class="hand" style="font-size:56px;margin-top:10px;">le message du jour</div>'
    f'<div class="serif" style="font-size:64px;line-height:1.15;margin-top:20px;">'
    f'Ce qu\'on a reçu de {acc("[Prénom]")}.</div>'
    + case_vide(190, 600, 700, 720, "le message<br>WhatsApp ici")
    + '<div class="hand" style="font-size:54px;position:absolute;right:120px;bottom:410px;">'
    'fiers d\'eux</div>'
    '</div></div>')

SLUG = "interactifs-01"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
