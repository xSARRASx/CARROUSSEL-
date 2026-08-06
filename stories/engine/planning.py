#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LA GRILLE DE DIFFUSION — qui décide du jour et de l'heure de chaque story.

Demandé par Martin le 06/08/2026, avant de brancher la programmation
automatique dans Metricool.

DEUX PRINCIPES QUI COMMANDENT TOUT LE RESTE
-------------------------------------------
1. UNE SÉQUENCE NE SE COUPE PAS EN RONDELLES. Une séquence d'aide se lit
   d'une traite : la couverture promet (« du concret, juste après »), les
   stories suivantes livrent, la dernière conclut. Si on la coupait pour en
   poster une par jour, la couverture promettrait une suite qui n'arriverait
   que le lendemain. D'où UN rendez-vous quotidien à 12h00 qui contient la
   séquence ENTIÈRE du jour.

2. UNE STORY QUI DIT « VOTE JUSTE EN DESSOUS » NE PART JAMAIS SANS SON
   STICKER. Instagram ne permet pas de poser un sticker de vote sur une
   story programmée : aucun outil au monde ne peut le faire à la place de
   Martin. Ces stories sont donc isolées dans un dossier `manuel/` et
   regroupées sur le SAMEDI, pour qu'il n'ait qu'un seul moment dans la
   semaine à y consacrer.

LES DEUX FOURNÉES NE SE CHEVAUCHENT PAS
---------------------------------------
    Fournée du LUNDI  (vidéo du dimanche) -> couvre lundi, mardi, mercredi
    Fournée du JEUDI  (vidéo du mercredi) -> couvre jeudi, vendredi, samedi, dimanche

Chaque fournée alimente la période qui la sépare de la suivante. Aucun jour
n'est servi deux fois, aucun jour n'est laissé vide.

⚠️ Le jeudi est conditionnel : s'il n'y a pas eu de vidéo le mercredi, on
pioche dans le stock pour couvrir jeudi -> dimanche.

POUR PROGRAMMER TOUT LE STOCK D'AVANCE : `programmation.py`, qui date chaque
story (AAAA-MM-JJ-12h00-NN.jpg) et écrit le calendrier complet.
"""

# UN SEUL rendez-vous par jour, à 12h00 heure de Paris.
# Décision de Martin (06/08/2026) : « les stories c'est à 12h, une seule fois
# par jour ». Ce rendez-vous contient la séquence complète du jour : les
# stories s'y enchaînent, elles ne sont pas éparpillées sur la journée.
MIDI = "12:00"

GRILLE = {
    # jour: [(heure, nombre de stories, ce qu'on y met, mode)]
    "lundi":    [(MIDI, 6, "Séquence d'aide de la vidéo du dimanche, en entier", "auto")],
    "mardi":    [(MIDI, 5, "Séquence conseil terrain, ou cadeau de la semaine", "auto")],
    "mercredi": [(MIDI, 5, "Coulisses, parcours, puis annonce de la vidéo de 18h", "auto")],
    "jeudi":    [(MIDI, 6, "Séquence d'aide de la vidéo du mercredi, en entier", "auto")],
    "vendredi": [(MIDI, 5, "Cadeau de la semaine, mot-clé SIMULATEUR", "auto")],
    "samedi":   [(MIDI, 6, "QUIZ ET SONDAGES — le seul moment manuel de la semaine", "manuel")],
    "dimanche": [(MIDI, 5, "Bilan, teaser de la vidéo qui sort à 18h", "auto")],
}

# Quels jours chaque fournée alimente
FOURNEE_LUNDI = ["lundi", "mardi", "mercredi"]
FOURNEE_JEUDI = ["jeudi", "vendredi", "samedi", "dimanche"]

def jours_de_la_fournee(jour_de_reveil):
    return FOURNEE_LUNDI if jour_de_reveil == "lundi" else FOURNEE_JEUDI

def capacite(jours):
    """Combien de stories il faut produire pour couvrir ces jours."""
    return sum(n for j in jours for _, n, _, _ in GRILLE[j])

# ---------------------------------------------------------------- classement

# Une story part en `manuel/` si elle promet une interaction que seul un
# sticker Instagram peut tenir. On se base sur son nom de fichier.
MOTIFS_MANUELS = ("sondage", "radar", "questions", "question")

def besoin_sticker(nom):
    """(bool, type de sticker) pour une story donnée, d'après son nom."""
    n = nom.lower()
    # Dans une séquence de quiz, SEULE la question a besoin du sticker :
    # la couverture, les réponses et la clôture se programment normalement.
    if n.startswith("quiz"):
        num = "".join(c for c in n.split("_")[-1] if c.isdigit())
        if num in ("02", "04", "06"):
            return True, "SONDAGE"
        return False, ""
    if any(m in n for m in MOTIFS_MANUELS):
        # « raconte ta situation », « tu en es où » -> boîte à questions
        if "question" in n or "radar" in n:
            return True, "QUESTIONS"
        return True, "SONDAGE"
    return False, ""

if __name__ == "__main__":
    print("GRILLE DE DIFFUSION — heures de Paris\n")
    total = 0
    for jour, creneaux in GRILLE.items():
        for h, n, quoi, mode in creneaux:
            marque = "  [MANUEL]" if mode == "manuel" else ""
            print(f"{jour:9s} {h}  {n} stories{marque}  — {quoi}")
            total += n
        print()
    print(f"Total sur la semaine : {total} stories")
    print(f"Fournée du lundi : {capacite(FOURNEE_LUNDI)} stories (lundi -> mercredi)")
    print(f"Fournée du jeudi : {capacite(FOURNEE_JEUDI)} stories (jeudi -> dimanche)")
