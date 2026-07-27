#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carrousel Guestlucky (angle produit : module conformite / gouvernance) genere
depuis la MEME video du 26/07/2026 (conciergerie condamnee a 220 000 EUR),
mais angle different du carrousel Le Sous Loueur (jamais les memes slides).

Aucun mot banni (beds24, mandat de gestion, garantie financiere). Aucun
denigrement de concurrent. Reutilise les gabarits de build_guestlucky.py.
Usage : python3 build_gl_conformite_lemeur.py && python3 render.py gl_conformite_lemeur
"""
import build_guestlucky as ENGINE
from build_guestlucky import (
    cover, content, content_ba, cta, closing, acc, ROOT,
    VIOLET, ROSE, check_dashes,
)

# Photo de fond de la semaine (generee par Martin sur Seedance, recadree 4:5).
ENGINE.set_bg_photo("gl_conformite_lemeur_bg.jpg")

SLUG = "gl_conformite_lemeur"

SLIDES = [
  cover("Guestlucky · Conformité",
        f'220&nbsp;000&nbsp;€ d\'amende :<br>la conformité n\'est plus {acc("une option",VIOLET)}',
        "Le module gouvernance qui prouve, bien par bien, que ta conciergerie travaille dans les règles."),

  content(1, "Le monde<br>a changé", "Ce que dit la condamnation de juillet 2026",
    [("Une première en France","Un tribunal condamne une conciergerie à 220&nbsp;000&nbsp;€, autant que la propriétaire."),
     ("La loi Le Meur","Depuis 2024, les intermédiaires sont sanctionnables, plus seulement les loueurs."),
     ("Des contrôles automatisés","Le téléservice national d'enregistrement détecte les manquements quasi en temps réel."),
     ("Des preuves exigées","Le juge ne se contente plus d'explications : il demande des traces concrètes.")],
    "Le constat", "Travailler dans les règles ne suffit plus : il faut pouvoir le démontrer."),

  content(2, "Le problème<br>d'échelle", "Impossible à suivre à la main",
    [("2 ou 3 biens, ça passe","Un tableur et de la rigueur peuvent encore suffire."),
     ("30 ou 50 biens, non","Vingt propriétaires, des statuts et des communes différents : le suivi manuel casse."),
     ("Chaque bien est un cas","Résidence principale ou secondaire, commune soumise ou non, plafonds de nuitées."),
     ("Un oubli coûte cher","Les amendes se comptent en dizaines de milliers d'euros par manquement.")],
    "À retenir", "La conformité est un travail de chaque jour, pas un dossier qu'on ouvre une fois."),

  content(3, "Le module<br>conformité", "La gouvernance intégrée à ton outil",
    [("Une fiche par bien","Statut, commune, autorisations, numéro d'enregistrement : tout est centralisé."),
     ("Des badges clairs","Vert ou rouge sur ton tableau de bord : tu vois d'un coup d'oeil qui est en règle."),
     ("Un rapport mensuel","Généré automatiquement et envoyé au propriétaire : une trace écrite permanente."),
     ("Pensé loi Le Meur","Le module suit les obligations issues de la loi, bien par bien.")],
    "Le gain", "Tu passes du classeur papier à la preuve générée automatiquement."),

  content(4, "Le compteur<br>de nuitées", "Les 120 jours surveillés tout seuls",
    [("Le plafond légal","120 jours par an en résidence principale, 90 jours à Paris."),
     ("Toutes plateformes","Le compteur additionne Airbnb, Booking, Abritel et le direct : un seul total fiable."),
     ("Alerte avant la limite","Tu vois arriver le plafond au lieu de le découvrir trop tard."),
     ("Fini le comptage à la main","Plus de tableur, plus d'approximation entre les calendriers.")],
    "À retenir", "Le dépassement peut coûter 50&nbsp;000&nbsp;€ : le compteur veille pour toi."),

  content_ba(5, "Expliquer<br>ou prouver", "Ce qui change devant un contrôle",
    "Classeurs, tableurs, captures d'écran : des explications difficiles à démontrer.",
    "Fiches, badges et rapports mensuels : des preuves générées automatiquement.",
    "Le cap", "Face à un contrôle, tout se joue sur les traces écrites."),

  content(6, "Le propriétaire<br>reste pilote", "Un accès avancé qui protège tout le monde",
    [("La main sur son bien","Calendrier et prix : le propriétaire garde le contrôle de son annonce."),
     ("Transparence totale","Il voit ses réservations et reçoit le rapport de conformité chaque mois."),
     ("Chacun son rôle","Toi tu délivres des prestations, lui pilote son bien : les rôles sont clairs."),
     ("Confiance renforcée","Un propriétaire informé et couvert reste un client fidèle.")],
    "À retenir", "Des rôles clairs et documentés : la meilleure protection pour les deux."),

  content(7, "Pourquoi<br>Guestlucky", "Un outil pensé par un conciergeur",
    [("Tout-en-un","Channel manager, PMS (logiciel de pilotage tout-en-un), messagerie et conformité réunis."),
     ("Fait par le métier","Conçu par un professionnel de la conciergerie, actif depuis 2014."),
     ("Support humain","Une vraie équipe te répond sur WhatsApp, pas un robot."),
     ("Sans risque","Gratuit jusqu'à 2 logements, sans engagement, résiliable en un clic.")],
    "À retenir", "L'outil suit la réglementation pour que tu puisses faire ton métier."),

  cta("Action · 1 mot", f'Envie de voir le module {acc("conformité",VIOLET)} en vrai ?', "DEMO",
      "Commente le mot DEMO et on te montre tout en 30 minutes, sans engagement."),

  closing(f'Le PMS qui transforme la conformité en {acc("routine automatique",VIOLET)}.'),
]


def main():
    html_dir = ROOT / "output" / SLUG / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    total_dash = 0
    for i, body in enumerate(SLIDES, 1):
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{ENGINE.COMMON_CSS}</style></head><body>{body}</body></html>')
        total_dash += len(check_dashes(html, i))
        (html_dir / f"slide_{i:02d}.html").write_text(html, encoding="utf-8")
    print(f"{len(SLIDES)} slides HTML ecrites dans {html_dir}. Tirets longs: {total_dash}")


if __name__ == "__main__":
    main()
