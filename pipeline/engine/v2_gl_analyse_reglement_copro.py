#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky de la semaine, a partir de la video
"Ta copropriete peut te bloquer sur Airbnb | Voici pourquoi" (29/07/2026).

Angle produit : l'analyse du reglement de copropriete integree a Guestlucky,
qui donne une prevalidation avant de lancer un logement.

Schemas differents de ceux du carrousel Le Sous Loueur.
Aucun mot banni, aucun concurrent nomme.

Usage : python3 v2_gl_analyse_reglement_copro.py && python3 render.py v2_gl_analyse_reglement_copro
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_analyse_reglement_copro"

d = Deck("guestlucky")
d.set_bg_photo("gl_analyse_reglement_copro_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Conformité",
        'Le règlement de copropriété<br>devient un ' + acc("point de contrôle"),
        "Analyse ton règlement avant de lancer un logement, et sache tout de suite si l'activité tient."),

    d.stats(1, "Ce qui change<br>pour un logement", "Depuis la loi Le Meur",
            [("2/3", "Des voix suffisent désormais pour interdire la location meublée de tourisme"),
             ("19 mars 2026", "Le Conseil constitutionnel valide le dispositif"),
             ("3", "Conditions cumulatives à réunir pour que le vote soit valable"),
             ("0", "Indemnisation prévue pour une activité déjà en cours")],
            "Le point clé", "La troisième condition porte sur un seul mot du règlement : commercial.",
            lead="Une assemblée générale peut maintenant fermer un logement au vote."),

    d.flow(2, "Comment marche<br>l'analyse", "Trois étapes",
           [("Tu déposes le règlement",
             "Le document de copropriété est chargé au moment de créer le logement."),
            ("Le module le lit",
             "Le texte est confronté à la loi en vigueur et aux décisions de justice connues."),
            ("Tu obtiens un indicateur",
             "Un feu vert de prévalidation, ou un signal rouge argumenté, documents à l'appui.")],
           "Le cadre", "Un indicateur outillé, qui ne remplace pas l'avis d'un professionnel du droit.",
           lead="Trois étapes entre le document et la décision de te lancer."),

    d.compare(3, "Avant<br>et avec le module", "Sur un nouveau logement",
              {"head": "Sans outil", "items": [
                  "Un règlement de copropriété lu en diagonale",
                  "Des clauses interprétées au feeling",
                  "Aucune trace de la vérification faite",
                  "Le doute qui reste jusqu'à l'assemblée générale"]},
              {"head": "Avec le module", "items": [
                  "Le texte confronté aux décisions de justice",
                  "Un indicateur clair avant de t'engager",
                  "Les éléments d'analyse conservés au dossier",
                  "Une décision prise avant la mise en ligne"]},
              "Le gain", "Tu sais où tu vas avant d'investir du temps et de l'argent.",
              lead="La différence se joue au moment où tu ouvres le logement."),

    d.layers(4, "Ce que le module<br>cherche dans le texte", "Les points sensibles",
             [("Point 1", "L'interdiction d'activité commerciale",
               "C'est la condition qui rend un vote d'interdiction possible."),
              ("Point 2", "Les activités déjà tolérées",
               "Un règlement qui admettait des professions libérales change la lecture."),
              ("Point 3", "La date du règlement",
               "Depuis le 21 novembre 2024, le meublé de tourisme doit être explicitement traité.")],
             "À retenir", "Trois angles de lecture, sur un document que personne ne lit jusqu'au bout.",
             lead="Le module cherche exactement ce qui décide de ton sort en assemblée générale."),

    d.pincer(5, "Deux contrôles<br>qui se cumulent", "Ne jamais n'en vérifier qu'un",
             ("La copropriété", "Le règlement et les votes de l'assemblée générale."),
             ("La commune", "Le changement d'usage, exigé en zone tendue."),
             ("L'un ne dispense jamais de l'autre", "La copropriété peut dire oui et la mairie non, ou l'inverse."),
             "Le réflexe", "Les deux se vérifient bien par bien, avant la première annonce.",
             lead="Deux autorités différentes, deux réponses possibles, deux risques distincts."),

    d.checklist(6, "Ce qu'une conciergerie<br>rassemble", "Pour chaque propriétaire",
                [(True, "Le règlement de copropriété",
                  "Fourni par le propriétaire, ou à défaut une attestation signée de sa part."),
                 (True, "Les procès-verbaux des assemblées générales",
                  "Ils révèlent des décisions qui n'ont jamais été reportées au règlement."),
                 (True, "La position du syndic",
                  "Savoir si le sujet a déjà été abordé, et dans quel sens."),
                 (True, "Les preuves archivées",
                  "Une clause au contrat, les justificatifs classés, la trace des questions posées.")],
                "Rappel", "Une conciergerie doit consulter le règlement pour s'assurer que l'activité est licite.",
                lead="Quatre pièces à réunir avant de signer un contrat de prestations."),

    d.mindmap(7, "Structurer<br>les prestations", "Sans créer de risque",
              "Rester<br>dans le civil",
              [("Les services en option", "Proposés au voyageur qui les demande, jamais imposés à tous."),
               ("La facturation à part", "Chaque prestation apparaît séparément, jamais incluse au séjour."),
               ("Pas de réception permanente", "L'accueil reste ponctuel et ne s'organise pas comme un hôtel."),
               ("La trace écrite", "Ce que tu fais vraiment doit correspondre à ce que dit le contrat.")],
              "L'enjeu", "Le mode d'exploitation compte autant que le règlement lui-même.",
              lead="La façon d'exploiter décide de la nature civile ou commerciale de l'activité."),

    d.cta("Action · 1 mot",
          'Ton règlement de copropriété<br>dit-il ' + acc("oui") + ' ?',
          "COPRO",
          "et on te montre l'analyse de règlement en démonstration gratuite de 30 minutes.",
          "Une réponse argumentée avant de lancer le logement, pas après le vote."),

    d.closing("L'outil qui prouve, logement par logement, que ton activité "
              + "<em>tient debout</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
