#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 (nouvelle mise en page visuelle) du carrousel Le Sous Loueur de la semaine :
"220 000 EUR : le jugement qui fait trembler les concierges".

Chaque slide de contenu est un SCHEMA (chiffres, timeline, tenaille, carte
mentale, comparatif, checklist, etages) au lieu d'une liste de texte.

Usage : python3 v2_lsl_conciergerie_220k.py && python3 render.py v2_lsl_conciergerie_220k
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_conciergerie_220k"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_conciergerie_220k_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Une conciergerie<br>condamnée à ' + acc("220&nbsp;000&nbsp;€"),
        "Ce que ce jugement change pour ton activité dès maintenant",
        "Décryptage terrain, sans panique : 11 ans de conciergerie."),

    d.stats(1, "Les chiffres<br>du jugement", "Tribunal de Paris",
            [("220&nbsp;000&nbsp;€", "L'amende infligée à la conciergerie, une première en France"),
             ("220&nbsp;000&nbsp;€", "La même somme pour la propriétaire des logements"),
             ("4", "Logements loués dans les 7e et 8e arrondissements"),
             ("410&nbsp;000&nbsp;€", "Les recettes estimées par la ville entre 2022 et 2024")],
            "Le motif", "Aucune autorisation de changement d'usage.",
            lead="Le tribunal judiciaire de Paris a frappé deux fois pour la même affaire."),

    d.timeline(2, "Comment on<br>en est arrivé là", "La mécanique",
               [("2024", "La loi Le Meur", "Les intermédiaires deviennent sanctionnables, jusqu'à 100&nbsp;000&nbsp;€.", False),
                ("Mai 2026", "Le téléservice national", "L'enregistrement se centralise : les communes détectent quasi en temps réel.", False),
                ("Juillet 2026", "Le jugement", "Une conciergerie condamnée pour ce qu'elle n'a pas vérifié.", True),
                ("Ensuite", "Les autres villes", "Paris ouvre le bal, les zones tendues vont suivre.", False)],
               "À retenir", "Ce n'est pas un accident : c'est un système qui se met en place.",
               lead="Trois textes et un outil de contrôle ont préparé ce jugement."),

    d.pincer(3, "Deux étages<br>de sanctions", "Et ils se cumulent",
             ("Le changement d'usage", "Autorisation exigée en zone tendue pour une résidence secondaire."),
             ("Le numéro d'enregistrement", "Obligatoire sur chaque annonce et sur chaque plateforme."),
             ("Jamais l'un sans l'autre", "L'un ne dispense pas de l'autre : la conciergerie vérifie les deux, bien par bien."),
             "Le risque", "Jusqu'à 12&nbsp;500&nbsp;€ par manquement pour l'intermédiaire.",
             lead="Deux obligations distinctes, deux régimes, deux amendes possibles."),

    d.mindmap(4, "La checklist<br>avant l'annonce", "Pour chaque nouveau bien",
              "Avant de publier",
              [("Le statut", "Résidence principale ou secondaire : le régime change du tout au tout."),
               ("La commune", "Au dessus de 200&nbsp;000 habitants, le changement d'usage s'applique."),
               ("Le papier", "Copie de l'autorisation exigée : pas de papier, pas d'annonce."),
               ("Le compteur", "Numéro sur l'annonce et suivi des nuitées : 120 jours, 90 à Paris.")],
              "Réflexe", "Contrat, déclarations du propriétaire, justificatifs archivés.",
              lead="Quatre vérifications à faire avant de mettre le moindre logement en ligne."),

    d.compare(5, "Le mythe<br>de la carte G", "Ce que l'affaire démontre",
              {"head": "Ce qu'on entend", "items": [
                  "La carte G protégerait des sanctions",
                  "Sans carte G, on serait dans l'illégalité",
                  "Elle aurait sauvé cette conciergerie"]},
              {"head": "Ce que dit le dossier", "items": [
                  "La carte G n'apparaît nulle part dans l'affaire",
                  "Le modèle prestation de services reste légal",
                  "Le reproche porte sur un défaut de vérification"]},
              "À retenir", "Ni bouclier, ni obligation pour le modèle prestation.",
              lead="On la présente comme un bouclier : le dossier dit tout le contraire."),

    d.checklist(6, "Les lignes<br>rouges", "Ce qu'une conciergerie ne fait jamais",
                [(False, "Encaisser les loyers", "L'argent des séjours ne transite jamais par ton compte."),
                 (False, "Signer à la place du propriétaire", "Les contrats de location restent les siens."),
                 (False, "Publier sur ton propre compte", "Jamais d'annonces sous ton nom Airbnb ou Booking."),
                 (False, "Te présenter comme gestionnaire", "Ni au contrat, ni sur ton site : parle de prestations.")],
                "Réflexe contrôle", "Le moindre courrier reçu : tu coupes tout, puis tu réponds.",
                lead="Franchir une seule de ces limites te fait basculer dans la gestion immobilière."),

    d.layers(7, "Les 3 briques<br>du professionnel", "Ce que le juge regarde",
             [("Brique 1", "Contrat et documentation", "Le contrat, mais aussi les attestations et justificatifs du propriétaire."),
              ("Brique 2", "Le mode opératoire réel", "Le juge compare ce qui est écrit et ce que tu fais vraiment au quotidien."),
              ("Brique 3", "Les preuves outillées", "Des rapports et des traces qui démontrent, au lieu d'expliquer.")],
             "À retenir", "On ne te demande pas d'expliquer : on te demande de prouver.",
             lead="Le contrat seul ne suffit plus : trois piliers tiennent ton activité."),

    d.cta("Action · 1 mot",
          'Ta conciergerie est-elle<br>vraiment ' + acc("en règle") + ' ?',
          "LEMEUR",
          "et je t'envoie le guide de conformité loi Le Meur gratuitement.",
          "Vérifie ton activité point par point avant que le contrôle ne le fasse pour toi."),

    d.closing("11 ans de terrain pour t'aider à bâtir une conciergerie "
              + "<em>solide</em>, pas une loterie."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
