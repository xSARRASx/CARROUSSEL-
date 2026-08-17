#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATELIER EN LIVE DU DIMANCHE 23/08/2026, 10H — demande de Pierre (17/08/2026).

Pierre, par WhatsApp : « cette semaine tu peux en faire pour dimanche, on est
en live, on fait un atelier, comme un webinaire, a 10h, sur la conciergerie et
sous loc, il faut faire plein de call to action pour ca ».

DECISIONS DE MARTIN (17/08/2026, avant construction)
    - On rejoint par MOT-CLE EN DM : « Reponds ATELIER ». C'est le systeme qui
      existe deja (comme GO et SIMULATEUR) et il marche meme si le lien n'est
      pas encore pret.
    - Jours utilises : MERCREDI 19 et DIMANCHE 23. Ce sont les deux jours de
      Pierre, donc rien de deja programme n'est deplace.

⚠️ CE PACK NE PASSE PAS PAR LA PROGRAMMATION, ET C'EST VOLONTAIRE
    1. La grille reserve mercredi et dimanche a Pierre : `livraison.py` ne sait
       pas y placer de creneaux (ces jours sont en mode "pierre", pas "auto").
    2. Surtout, l'atelier est a 10H. La grille poste a 12h00 : un rappel
       programme a midi arriverait APRES le debut de l'atelier. Le dimanche
       doit donc partir a la main, dans la matinee.
    Le pack est donc range en `manuel/`, avec le fichier des stickers, et
    c'est Pierre qui poste.

⚠️ ON N'INVENTE PAS LE PROGRAMME DE L'ATELIER. Ce qui est certain : c'est en
direct, dimanche 10h, ca parle de conciergerie et de sous-location, et on peut
poser ses questions. Aucune promesse chiffree, aucun contenu invente.

Rendu : python3 render_stories.py atelier-23-08
"""
from photo_style import (cover, focus, fin, p_cta, sondage, acc, write_lot)

o = acc

DIMANCHE = acc("dimanche 10h")
EN_DIRECT = acc("en direct")
AUJOURDHUI = acc("aujourd'hui")
ATELIER_MOT = acc("ATELIER")

STORIES = {}

# ============================================================================
# MERCREDI 19/08 — l'annonce
# ============================================================================

STORIES["mer_01_annonce"] = cover(
    "bg_terrasse", "on se retrouve dimanche",
    f'Atelier {EN_DIRECT}, dimanche à 10h.',
    sub="Une heure sur la conciergerie et la sous-location, en direct, "
        "avec vos questions.",
    hand_bottom="comment y assister, juste après")

STORIES["mer_02_pourquoi"] = focus(
    "bg_bureau_matin", "pourquoi en direct plutôt qu'une vidéo",
    "Tu peux poser tes questions.",
    "C'est toute la différence avec une vidéo : on répond aux situations "
    "réelles, celles que vous nous envoyez en message toute la semaine. "
    "Conciergerie, sous-location, les deux sujets sont au programme.")

STORIES["mer_03_sondage_SONDAGE"] = sondage(
    "bg_ciel_rose", "dis-nous si on t'attend",
    f'Tu seras là {DIMANCHE}&nbsp;?')

STORIES["mer_04_cta"] = p_cta(
    "bg_ciel_dore", "pour recevoir le lien et le rappel",
    "Réponds à cette story",
    "ATELIER",
    "Je t'envoie le lien et un rappel avant le début.")

# ============================================================================
# DIMANCHE 23/08 — le jour J (a poster LE MATIN, avant 10h)
# ============================================================================

STORIES["dim_01_jour_j"] = cover(
    "bg_plage_aube", "c'est aujourd'hui",
    f'Rendez-vous à 10h, {EN_DIRECT}.',
    sub="Atelier conciergerie et sous-location. Il est encore temps de "
        "nous rejoindre.",
    hand_bottom="dis-nous ce que tu veux qu'on aborde")

STORIES["dim_02_questions_QUESTIONS"] = sondage(
    "bg_mer_calme", "avant de commencer",
    "Une question pour l'atelier&nbsp;?",
    note="pose-la ici, on y répond en direct")

STORIES["dim_03_dernier_rappel"] = p_cta(
    "bg_village", "dernier rappel avant le début",
    "Tu n'as pas encore le lien ?",
    "ATELIER",
    "Réponds maintenant, je te l'envoie tout de suite.")

SLUG = "atelier-23-08"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
