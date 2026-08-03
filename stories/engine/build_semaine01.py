#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEMAINE 01 (HTML 1080x1920) — VERSION STYLE UNIQUE (03/08/2026).

Decision de Martin : toutes les stories dans le style "photo fait main"
(photo_style.py), LOGO partout, fonds tous differents (les 15 fonds chauds :
un fond different pour chacune des 15 stories de la semaine).

Seules les stories "texte sur fond" sont generees ici : les faces camera,
captures et screenshots restent a filmer/faire par Martin. Les stickers
Instagram (sondage, question, lien...) s'ajoutent DANS l'app au moment de
poster : les visuels laissent la place prevue.

Rendu : python3 render_stories.py semaine-01
"""
from photo_style import (open_photo, underline, arrow_down, acc, nb,
                         BLANC, BLEU, write_lot)

def basic(bg, kicker, title, sub=None, items=None, top=False):
    """Kicker manuscrit + titre serif ; liste sur voile blanc ; sous-titre serif."""
    body = open_photo(bg) + f'<div class="pad"{"" if top else " style=justify-content:center;"}>'
    if kicker:
        body += f'<div class="hand" style="font-size:54px;margin-bottom:24px;{"margin-top:30px;" if top else ""}">{nb(kicker)}</div>'
    body += f'<div class="serif" style="font-size:66px;line-height:1.16;">{nb(title)}</div>'
    if items:
        lis = "".join(
            f'<div class="vnote" style="margin-bottom:{0 if i == len(items) - 1 else 16}px;'
            f'font-size:29px;"><span class="ar">→</span><span>{nb(t)}</span></div>'
            for i, t in enumerate(items))
        body += f'<div class="veil" style="margin-top:48px;">{lis}</div>'
    if sub:
        body += f'<div class="serif t3" style="margin-top:44px;font-weight:700;">{nb(sub)}</div>'
    return body + '</div></div>'

def quote(bg, text, sub=None, top=False):
    body = open_photo(bg) + f'<div class="pad"{"" if top else " style=justify-content:center;"}>'
    body += (f'<div class="serif" style="font-size:62px;line-height:1.22;{"margin-top:40px;" if top else ""}">'
             f'{acc("«")}&nbsp;{nb(text)}&nbsp;{acc("»")}</div>')
    if sub:
        body += f'<div class="serif t3" style="margin-top:44px;font-weight:700;">{nb(sub)}</div>'
    return body + '</div></div>'

def cta(bg, toptext, keyword, bottom):
    size = 64 if len(keyword) >= 12 else (84 if len(keyword) >= 8 else 120)
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            f'<div class="serif" style="font-size:54px;line-height:1.22;text-align:center;">{nb(toptext)}</div>'
            f'<div class="pctacard" style="margin-top:56px;"><div class="lbl">RÉPONDS</div>'
            f'<div class="kw" style="font-size:{size}px;">{keyword}</div>'
            f'<div style="margin-top:22px;">{underline(150, "#2F7EC4", cls="inline")}</div></div>'
            f'<div class="hand" style="font-size:46px;text-align:center;margin-top:38px;">{nb(bottom)}</div>'
            '</div></div>')

SLUG = "semaine-01"
STORIES = {
    # ---- LUNDI : diagnostic + recyclage video du dimanche (parler d'argent)
    "lundi_02_sondage": basic("bg_ciel_dore", "Question du lundi",
        f'Et en ce moment, ta plus grosse {acc("galère")}, c\'est quoi ?',
        sub="Vote juste en dessous.", top=True),
    "lundi_03_questions": basic("bg_bureau_matin", "On répond à tout le monde",
        f'Raconte ta {acc("situation")} en une phrase.', top=True),
    "lundi_05_reactions": basic("bg_salon_cosy", "Parler d'argent",
        f'Quand tu dis {acc("combien tu gagnes")}, il n\'y a que 4 réactions possibles :',
        items=["La moquerie", "La jalousie", "L'attente", "Le calcul"],
        sub="Sébastien les a toutes vécues en 26 ans d'entrepreneuriat."),
    "lundi_06_citation": quote("bg_chemin_aube",
        f'Les gens voient ton {acc("résultat")}. Ils ne voient jamais ton {acc("chemin")}.',
        sub="La 7e chose à ne jamais dire est la plus contre-intuitive. La vidéo complète est juste là :",
        top=True),
    # ---- MARDI : conseil terrain rendez-vous proprietaire
    "mardi_02_erreur": basic("bg_immeuble_dore", "Rendez-vous propriétaire",
        f'L\'erreur : arriver et {acc("dérouler")}. Tes services, tes tarifs, ton fonctionnement.',
        sub="Le propriétaire, lui, se pose une seule question : son logement est-il entre de bonnes mains."),
    "mardi_03_conseil": basic("bg_terrasse", "Fais l'inverse",
        f'{acc("Écoute")} d\'abord. Vends {acc("après")}.',
        sub="Ses locataires actuels, ses galères, ce qui l'empêche de dormir.", top=True),
    "mardi_04_argumentaire": cta("bg_village",
        "Les arguments qui font signer un propriétaire dès le premier rendez-vous.",
        "ARGUMENTAIRE", "On te l'envoie en message."),
    # ---- MERCREDI : parcours + question
    "mercredi_02_parcours": basic("bg_montagne", "Le chemin",
        f'À 40 ans : {acc("dépôt de bilan")}. Retombé à zéro.',
        sub="Aujourd'hui : 11 ans de conciergerie et de sous-location, plus de 3 000 élèves accompagnés."),
    "mercredi_03_question": basic("bg_lac", "Et toi ?",
        f'Tu en es où de ton {acc("chemin")} ?', sub="Raconte, on lit tout.", top=True),
    # ---- JEUDI : CTA GO
    "jeudi_04_go": cta("bg_prairie",
        "Tu veux qu'on échange ensemble sur ton projet ?",
        "GO", "On fait le point ensemble, tout simplement."),
    # ---- VENDREDI : CTA SIMULATEUR
    "vendredi_03_simulateur": cta("bg_ble",
        "L'outil qu'on utilise avec nos élèves avant chaque signature.",
        "SIMULATEUR", "On te l'envoie en message."),
    # ---- SAMEDI : radar + rappel GO
    "samedi_01_radar": basic("bg_ciel_rose", "Le point du samedi",
        f'Tu en es {acc("où")} dans ton projet aujourd\'hui ?',
        sub="Réponds en une phrase. On lit tout.", top=True),
    "samedi_03_go": cta("bg_ville_doree", "Si tu veux avancer plus vite :",
        "GO", "On fait le point sur ton projet ensemble."),
    # ---- DIMANCHE : teaser + apres la video
    "dimanche_01_teaser": basic("bg_mer_calme", "Ce soir, 18h",
        f'Nouvelle {acc("vidéo")} sur la chaîne.', sub="Reste dans le coin.", top=True),
    "dimanche_03_avis": basic("bg_plage_aube", "Tu l'as vue ?",
        f'Dis-moi ce que tu en {acc("retiens")}.', sub="Réponds à cette story."),
}

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
