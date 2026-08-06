#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LE PACK DE PIERRE — gabarits de témoignages + stories CTA.

Organisation validée avec Martin (06/08/2026) :
  - Pierre poste DEUX fois par semaine : mercredi et dimanche, ses témoignages.
  - Martin (avec Claude) PRÉPARE et LUI ENVOIE ces stories ; Pierre n'a plus
    qu'à coller son screenshot réel dedans et publier.
  - Martin s'occupe des cinq autres jours.

Pourquoi 10 gabarits et pas 3 : à deux par semaine, trois modèles se
répéteraient au bout de dix jours. Avec dix modèles, Pierre tourne pendant
plus d'un mois sans jamais reposter la même mise en page.

Ces gabarits sont les SEULS du projet avec une zone en pointillés : le vrai
témoignage (message WhatsApp, annonce, résultat) est collé par Pierre dans
Instagram via le sticker photo. On n'invente JAMAIS un témoignage.

Rendu : python3 render_stories.py temoignages-pierre
"""
from photo_style import (open_photo, underline, arrow_down, acc, nb,
                         BLANC, BLEUF, write_lot)

STORIES = {}

def case(x, y, w, h, note):
    """Zone en pointillés où Pierre colle son screenshot."""
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            'border:5px dashed rgba(255,255,255,0.85);border-radius:26px;"></div>'
            f'<div class="hand" style="font-size:42px;position:absolute;left:{x + 44}px;'
            f'top:{y + h // 2 - 34}px;color:rgba(255,255,255,0.95);line-height:1.25;">{nb(note)}</div>')

def fleche_gauche(x, y, w=190, h=230):
    path = f"M {w*0.85:.0f} 18 C {w*0.3:.0f} {h*0.25:.0f}, {w*0.1:.0f} {h*0.55:.0f}, {w*0.4:.0f} {h-26:.0f}"
    head = (f'<path d="M {w*0.4-32:.0f} {h-88:.0f} L {w*0.4:.0f} {h-22:.0f}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>'
            f'<path d="M {w*0.4+28:.0f} {h-82:.0f} L {w*0.4:.0f} {h-22:.0f}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>')
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" fill="none">'
            f'<path d="{path}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>{head}</svg>')

def gabarit(bg, kicker, titre, note_case, hand_bas=None, large=False):
    """Gabarit standard : accroche en haut, grande zone à coller, mot manuscrit."""
    x, y, w, h = (150, 640, 780, 700) if large else (190, 620, 700, 760)
    bas = (f'<div class="hand" style="font-size:56px;position:absolute;right:110px;'
           f'bottom:415px;">{nb(hand_bas)}</div>') if hand_bas else ''
    k = (f'<div class="hand" style="font-size:54px;margin-top:10px;">{nb(kicker)}</div>'
         if kicker else '')
    return (open_photo(bg) + '<div class="pad">' + k +
            f'<div class="serif" style="font-size:62px;line-height:1.16;margin-top:20px;">{nb(titre)}</div>'
            + case(x, y, w, h, note_case) + bas + '</div></div>')

# ============================================================================
# LES 10 GABARITS — accroches et mises en page toutes différentes
# ============================================================================

STORIES["temoin_p01"] = (
    open_photo("bg_mer_calme") + '<div class="pad">'
    f'<div class="serif" style="font-size:80px;line-height:1.1;text-align:right;margin-top:20px;">'
    f'+&nbsp;1 pour {acc("[Prénom]")}</div>'
    + fleche_gauche(700, 470)
    + case(110, 650, 560, 690, "colle l'annonce<br>de l'élève ici")
    + '<div class="hand" style="font-size:58px;position:absolute;right:100px;bottom:420px;">'
    'Bravo [Prénom]&nbsp;!</div>'
    '</div></div>')

STORIES["temoin_p02"] = gabarit(
    "bg_plage_aube", "tombé ce matin",
    f'La {acc("dernière annonce")} de nos élèves.',
    "le screenshot ici", large=True)

STORIES["temoin_p03"] = gabarit(
    "bg_lac", "le message du jour",
    f'Ce qu\'on a reçu de {acc("[Prénom]")}.',
    "le message<br>WhatsApp ici", hand_bas="fiers d'eux")

STORIES["temoin_p04"] = gabarit(
    "bg_ciel_dore", "encore un",
    f'{acc("[Prénom]")} vient de signer son premier contrat.',
    "sa capture ici", hand_bas="ça continue")

STORIES["temoin_p05"] = gabarit(
    "bg_terrasse", "reçu hier soir",
    f'Le {acc("résultat")} du mois de [Prénom].',
    "les chiffres ici", large=True)

CITATION = acc("J'ai enfin franchi le pas.")
STORIES["temoin_p06"] = gabarit(
    "bg_village", "on adore ces messages",
    f"« {CITATION} »",
    "la conversation ici")

STORIES["temoin_p07"] = gabarit(
    "bg_montagne", "un de plus",
    f'{acc("[Prénom]")} a rempli son calendrier.',
    "son calendrier ici", large=True, hand_bas="bien joué")

STORIES["temoin_p08"] = gabarit(
    "bg_immeuble_dore", "la fierté du jour",
    f'Son {acc("premier logement")} est en ligne.',
    "l'annonce ici")

STORIES["temoin_p09"] = gabarit(
    "bg_bureau_matin", "ils l'ont fait",
    f'Ce que [Prénom] a changé en {acc("3 mois")}.',
    "l'avant / après ici", large=True)

STORIES["temoin_p10"] = gabarit(
    "bg_prairie", "merci pour ce message",
    f'Un retour qui fait {acc("plaisir")}.',
    "le message ici", hand_bas="merci [Prénom]")

# ============================================================================
# LES STORIES CTA — à poster JUSTE DERRIÈRE le témoignage
# ============================================================================

def cta_go(bg, titre, sous):
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            f'<div class="serif" style="font-size:58px;line-height:1.2;text-align:center;">{nb(titre)}</div>'
            f'<div class="pctacard" style="margin-top:56px;"><div class="lbl">RÉPONDS</div>'
            f'<div class="kw" style="font-size:130px;">GO</div>'
            f'<div style="margin-top:22px;">{underline(150, BLEUF, cls="inline")}</div></div>'
            f'<div class="hand" style="font-size:46px;text-align:center;margin-top:38px;">{nb(sous)}</div>'
            '</div></div>')

STORIES["cta_go_01"] = cta_go("bg_ciel_rose",
    "Toi aussi tu veux en être ?",
    "on échange ensemble sur ton projet")
STORIES["cta_go_02"] = cta_go("bg_salon_cosy",
    "Et toi, tu en es où de ton projet ?",
    "réponds, on regarde ça ensemble")
STORIES["cta_go_03"] = cta_go("bg_chemin_aube",
    "On peut faire pareil avec toi.",
    "dis-nous où tu en es")

SLUG = "temoignages-pierre"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
