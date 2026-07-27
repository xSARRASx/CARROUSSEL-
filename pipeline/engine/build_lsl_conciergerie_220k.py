#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carrousel Le Sous Loueur (angle coaching / alerte journalistique) genere depuis
la video du 26/07/2026 : "220 000 EUR : le jugement qui fait trembler les
concierges" (transcription pipeline/output/transcripts/20260726_YiAaGhoimhA.txt).

Reutilise les gabarits du moteur build_lesousloueur.py.
Usage : python3 build_lsl_conciergerie_220k.py && python3 render.py lsl_conciergerie_220k
"""
import build_lesousloueur as ENGINE
from build_lesousloueur import (
    cover, content, content_ba, cta, closing, acc, ROOT, DASHES,
)

# Photo de fond de la semaine (generee par Martin sur Seedance, recadree 4:5).
# Doit etre activee AVANT de construire les slides.
ENGINE.set_bg_photo("lsl_conciergerie_220k_bg.jpg")

SLUG = "lsl_conciergerie_220k"

SLIDES = [
  cover("Le Sous Loueur",
        f'Une conciergerie<br>condamnée à {acc("220&nbsp;000&nbsp;€")}',
        "Ce que ce jugement change pour ton activité dès maintenant",
        "Décryptage terrain, sans panique : 11 ans de conciergerie."),

  content(1, "Les<br>faits", "Le jugement qui fait trembler le métier",
    [("Quatre logements à Paris","Loués en courte durée sans l'autorisation de changement d'usage exigée pour une résidence secondaire."),
     ("410&nbsp;000&nbsp;€ de recettes","C'est l'estimation de la ville pour la période 2022 à 2024."),
     ("Double condamnation","220&nbsp;000&nbsp;€ pour la propriétaire et 220&nbsp;000&nbsp;€ pour la conciergerie, une première en France."),
     ("Le détail qui a tout aggravé","Au jour de l'audience, les annonces étaient toujours en ligne.")],
    "À retenir", "Le tribunal juge qu'un professionnel ne peut pas ignorer la réglementation locale."),

  content(2, "Pourquoi c'est<br>historique", "La responsabilité a changé de camp",
    [("Avant la loi Le Meur","Seul le loueur risquait l'amende, les intermédiaires étaient épargnés."),
     ("Depuis 2024","Conciergeries et agences sont sanctionnables, jusqu'à 100&nbsp;000&nbsp;€ d'amende."),
     ("Les plateformes épargnées","Airbnb et Booking ne sont pas visés : la responsabilité repose sur toi."),
     ("Des contrôles automatisés","Le téléservice national et son API (connexion automatique entre systèmes) détectent les manquements quasi en temps réel.")],
    "À retenir", "Ce jugement n'est pas un accident : c'est le premier domino d'un système."),

  content(3, "Deux étages<br>de sanctions", "Et ils se cumulent : jamais l'un sans l'autre",
    [("Le changement d'usage","L'autorisation exigée en zone tendue pour une résidence secondaire : c'est l'affaire des 220&nbsp;000&nbsp;€."),
     ("Le numéro d'enregistrement","Obligatoire sur chaque annonce et sur chaque plateforme."),
     ("Ce que risque l'intermédiaire","Jusqu'à 12&nbsp;500&nbsp;€ par manquement, et 50&nbsp;000&nbsp;€ pour certains cas."),
     ("Ce que risque le loueur","10&nbsp;000&nbsp;€ pour défaut de déclaration, 50&nbsp;000&nbsp;€ au delà des 120 jours en résidence principale.")],
    "À retenir", "Vérifier les deux, bien par bien, avant toute mise en ligne."),

  content(4, "La checklist<br>avant l'annonce", "À vérifier pour chaque nouveau bien",
    [("Le statut du bien","Résidence principale ou secondaire : le régime change du tout au tout."),
     ("La commune","Au dessus de 200&nbsp;000&nbsp;habitants, le changement d'usage s'applique."),
     ("Le papier avant l'annonce","Copie de l'autorisation exigée au propriétaire : pas de papier, pas d'annonce."),
     ("Numéro et compteur","Numéro d'enregistrement sur chaque annonce, compteur de nuitées : 120 jours, 90 à Paris.")],
    "Réflexe", "Trace écrite : contrat, déclarations du propriétaire, justificatifs archivés."),

  content(5, "Le mythe<br>de la carte G", "Ce que cette affaire démontre vraiment",
    [("Nulle part au dossier","La carte G (carte professionnelle de gestion immobilière) n'apparaît pas dans cette affaire."),
     ("Le vrai reproche","Un défaut de vérification, pas un défaut de statut : la carte n'aurait rien changé."),
     ("Le modèle prestation","Ménages, linge, accueil voyageurs, communication : des prestations de services."),
     ("Pas d'illégalité","Exercer sans carte G dans ce cadre reste légal : c'est la frontière posée par la loi elle-même.")],
    "À retenir", "La carte G n'est ni un bouclier, ni une obligation pour le modèle prestation."),

  content(6, "Les lignes<br>rouges", "Ce qu'on ne fait jamais sans carte G",
    [("Encaisser les loyers","L'argent des séjours ne transite jamais par ton compte."),
     ("Signer à la place","Les contrats de location restent signés par le propriétaire."),
     ("Publier en ton nom","Jamais d'annonces sur ton propre compte Airbnb ou Booking."),
     ("Te dire gestionnaire","Ni dans ton contrat, ni sur ton site : mets en avant la prestation de services.")],
    "Réflexe contrôle", "Le moindre courrier reçu : tu coupes tout immédiatement, puis tu réponds."),

  content(7, "Les 3 briques<br>du pro", "Ce que le juge regarde vraiment",
    [("Contrat et documentation","Un bon contrat, plus les attestations et justificatifs recueillis auprès du propriétaire."),
     ("Le mode opératoire réel","Le juge regarde ce que tu fais au quotidien, au delà de ce qui est écrit."),
     ("Les preuves outillées","Des rapports et des traces qui démontrent, au lieu de simplement expliquer."),
     ("Le bon accompagnement","En cas de doute, un avocat local en droit immobilier ou commercial suffit.")],
    "À retenir", "On ne te demande pas d'expliquer : on te demande de prouver."),

  cta("Ta conciergerie est-elle vraiment en règle ?",
      "Vérifie ton activité point par point avant que le contrôle ne le fasse pour toi.",
      "LEMEUR",
      "et je t'envoie le guide de conformité loi Le Meur gratuitement."),

  closing("11 ans de terrain pour t'aider à bâtir une conciergerie solide, pas une loterie."),
]

DASHES_LOCAL = DASHES

def main():
    html_dir = ROOT / "output" / SLUG / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    td = 0
    for i, body in enumerate(SLIDES, 1):
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{ENGINE.COMMON_CSS}</style></head><body>{body}</body></html>')
        d = [c for c in html if c in DASHES_LOCAL]
        if d:
            print(f"  ALERTE tiret slide {i}: {set(d)}"); td += len(d)
        (html_dir / f"slide_{i:02d}.html").write_text(html, encoding="utf-8")
    print(f"{len(SLIDES)} slides HTML ecrites dans {html_dir}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
