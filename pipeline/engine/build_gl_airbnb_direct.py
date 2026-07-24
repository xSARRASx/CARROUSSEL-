#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carrousel Guestlucky (angle produit : reservation directe 0 % commission) genere
a partir de la MEME video "Airbnb tue le micro BIC", mais angle different du
carrousel Le Sous Loueur (jamais les memes slides).

Reutilise les gabarits de build_guestlucky.py (aucune duplication de l'engine).
Aucune mention de concurrent nomme (regle mots bannis cote Guestlucky respectee).

Usage : python3 build_gl_airbnb_direct.py && python3 render.py gl_airbnb_direct
"""
import pathlib
from build_guestlucky import (
    cover, content, content_ba, cta, closing, acc, COMMON_CSS, ROOT,
    VIOLET, ROSE, check_dashes,
)

SLUG = "gl_airbnb_direct"

SLIDES = [
  cover("Guestlucky · Réservation directe",
        f'Airbnb passe à 15,5 %.<br>{acc("Reprends le contrôle",VIOLET)}',
        "La réservation directe à 0 % de commission, sans dépendre des plateformes."),

  content(1, "Ce qui<br>change", "La nouvelle commission Airbnb",
    [("Commission unique","Dès le 13 octobre 2026, une seule commission de 15,5 %, à ta charge."),
     ("Le vrai coût","Avec la TVA (taxe sur la valeur ajoutée) à 20 %, tu supportes en réalité 18,6 %."),
     ("Sur chaque réservation","Plus tu dépends d'une seule plateforme, plus cette commission pèse lourd."),
     ("Une dépendance risquée","Une plateforme change ses règles, et toute ta marge bouge avec.")],
    "Le constat", "Chaque réservation Airbnb te coûte 18,6 % de ton chiffre."),

  content(2, "La réponse :<br>le direct", "Ton propre canal, sans commission",
    [("Moteur de réservation","Guestlucky transforme ton site en canal de réservation directe."),
     ("Zéro commission","Le voyageur réserve chez toi, tu ne partages ta marge avec personne."),
     ("Tes clients, tes règles","Tu fidélises et tu offres un avantage pour le prochain séjour."),
     ("En plus des plateformes","Tu gardes Airbnb, mais tu ne dépends plus uniquement de lui.")],
    "Le gain", "0 % de commission sur chaque réservation en direct."),

  content(3, "Tout reste<br>synchro", "Un seul outil pour tous tes canaux",
    [("Channel manager natif","Le channel manager, l'outil qui synchronise tes annonces, relie Airbnb, Booking et Abritel en temps réel."),
     ("Zéro double réservation","Les calendriers se mettent à jour tout seuls, sur tous les canaux."),
     ("Une seule interface","Tu pilotes tes annonces et ton direct au même endroit."),
     ("Le direct au centre","Tes réservations sans commission passent avant tout le reste.")],
    "À retenir", "Tu synchronises tout, tu ne saisis plus rien deux fois."),

  content(4, "La factu<br>2026", "La réforme gérée pour toi",
    [("Facturation électronique","La réforme 2026 rend la facture électronique obligatoire pour ton activité."),
     ("Conforme d'office","Guestlucky génère des factures aux normes, sans que tu t'en occupes."),
     ("Loi Hoguet native","La conformité de ton activité est intégrée, pas vendue en option."),
     ("Tout au même endroit","Réservations, factures et caution : une plateforme, une facture.")],
    "À retenir", "La conformité 2026, sans stress et sans logiciel en plus."),

  content_ba(5, "Dépendance<br>ou contrôle", "Deux façons de vivre la réforme",
    "Tout sur Airbnb : tu subis chaque hausse de commission, sans alternative.",
    "Direct plus plateformes : tu encaisses sans commission et tu gardes le choix.",
    "Le cap", "Moins de dépendance, plus de marge conservée."),

  content(6, "Pourquoi<br>Guestlucky", "Pensé par un conciergeur",
    [("Tout-en-un","Réservation directe, channel manager, messagerie et caution réunis."),
     ("Une seule facture","Tu remplaces une pile d'outils par une seule plateforme."),
     ("Support humain","Une équipe qui te répond sur WhatsApp, pas un robot."),
     ("Migration rapide","Tu bascules ton activité en moins de 48 heures.")],
    "À retenir", "Un outil bâti par quelqu'un qui gère vraiment des logements."),

  content(7, "Par où<br>commencer", "Trois pas pour reprendre la main",
    [("Active ton moteur direct","Ton site devient un canal de réservation sans commission."),
     ("Connecte tes plateformes","Airbnb, Booking et Abritel synchronisés en quelques clics."),
     ("Oriente tes voyageurs","Invite chaque client à réserver en direct la prochaine fois.")],
    "À retenir", "La première réservation directe change tout ton modèle."),

  cta("Action · 1 mot", f'Envie de réserver {acc("sans commission",VIOLET)} ?', "DIRECT",
      "Commente le mot DIRECT et je t'envoie le plan pour lancer ta réservation directe."),

  closing(f'La plateforme qui remet ta marge {acc("du bon côté",VIOLET)} en 2026.'),
]


def main():
    html_dir = ROOT / "output" / SLUG / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    total_dash = 0
    for i, body in enumerate(SLIDES, 1):
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{COMMON_CSS}</style></head><body>{body}</body></html>')
        total_dash += len(check_dashes(html, i))
        (html_dir / f"slide_{i:02d}.html").write_text(html, encoding="utf-8")
    print(f"{len(SLIDES)} slides HTML ecrites dans {html_dir}. Tirets longs: {total_dash}")


if __name__ == "__main__":
    main()
