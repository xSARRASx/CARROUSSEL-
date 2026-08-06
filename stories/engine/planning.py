#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LA GRILLE DE DIFFUSION — qui décide du jour et de l'heure de chaque story.

Demandé par Martin le 06/08/2026, avant de brancher la programmation
automatique dans Metricool.

DEUX PRINCIPES QUI COMMANDENT TOUT LE RESTE
-------------------------------------------
1. UNE SÉQUENCE NE SE COUPE PAS EN RONDELLES. Une séquence d'aide se lit
   d'une traite : la couverture donne envie, les stories suivantes livrent,
   la dernière conclut. Si on éparpille ses 6 stories sur 4 moments de la
   journée, la logique se casse et les gens décrochent. On poste donc par
   VAGUES de 2 à 3 stories qui s'enchaînent, pas story par story.

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
pioche dans le stock (104 stories d'avance au 06/08/2026) pour couvrir
jeudi -> dimanche.
"""

# Créneaux horaires, heure de Paris. Deux vagues par jour : le matin quand
# les gens ouvrent Instagram en se levant, le soir quand ils décompressent.
MATIN = "08:00"
SOIR = "18:30"
MIDI_WE = "11:00"     # le week-end, les gens se lèvent plus tard

GRILLE = {
    # jour: [(heure, nombre de stories, ce qu'on y met, mode)]
    "lundi": [
        (MATIN, 3, "Séquence d'aide de la vidéo du dimanche : couverture + 2 premières", "auto"),
        (SOIR,  3, "Fin de la séquence + la conclusion (sans CTA : on donne)", "auto"),
    ],
    "mardi": [
        (MATIN, 2, "Conseil terrain", "auto"),
        (SOIR,  2, "Le cadeau de la semaine + son mot-clé", "auto"),
    ],
    "mercredi": [
        (MATIN, 2, "Coulisses, histoire, parcours", "auto"),
        (SOIR,  1, "Annonce de la vidéo qui sort à 18h", "auto"),
        # + créneau témoignages de Pierre, qu'il poste quand il veut
    ],
    "jeudi": [
        (MATIN, 3, "Séquence d'aide de la vidéo du mercredi : couverture + 2", "auto"),
        (SOIR,  3, "Fin de la séquence (sans CTA : on donne)", "auto"),
    ],
    "vendredi": [
        (MATIN, 2, "Rappel de valeur", "auto"),
        (SOIR,  2, "Le cadeau de la semaine, mot-clé SIMULATEUR", "auto"),
    ],
    "samedi": [
        (MIDI_WE, 5, "QUIZ ET SONDAGES — le seul moment manuel de la semaine", "manuel"),
    ],
    "dimanche": [
        (MIDI_WE, 2, "Bilan de la semaine, mise en bouche", "auto"),
        (SOIR,    2, "Teaser + sortie de la vidéo à 18h", "auto"),
        # + créneau témoignages de Pierre
    ],
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
