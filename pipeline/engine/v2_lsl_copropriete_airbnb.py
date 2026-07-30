#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur de la semaine, a partir de la video
"Ta copropriete peut te bloquer sur Airbnb | Voici pourquoi" (29/07/2026).

Angle coaching : le nouveau pouvoir de la copropriete depuis la loi Le Meur,
et surtout LA PARADE (rester dans le domaine civil, pas commercial).

Chaque slide de contenu est un SCHEMA, jamais une liste de texte.

Usage : python3 v2_lsl_copropriete_airbnb.py && python3 render.py v2_lsl_copropriete_airbnb
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_copropriete_airbnb"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_copropriete_airbnb_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Ta copropriété peut<br>désormais te ' + acc("bloquer"),
        "Ce qui a changé, et la parade que presque personne ne connaît",
        "Décryptage terrain, sans panique : 11 ans de courte durée."),

    d.timeline(1, "Ce qui vient<br>de basculer", "La mécanique",
               [("Avant", "Il fallait l'unanimité",
                 "Interdire supposait de changer la destination de tout l'immeuble : autant dire jamais.", False),
                ("Loi Le Meur", "Deux tiers des voix suffisent",
                 "L'assemblée générale peut interdire la location meublée de tourisme.", False),
                ("19 mars 2026", "Le Conseil constitutionnel valide",
                 "Le recours sur le droit de propriété est rejeté : le débat est clos.", True),
                ("2026-2027", "La vague de votes",
                 "Les assemblées générales vont se saisir du sujet en série.", False)],
               "À retenir", "Ton droit de veto d'hier n'existe plus.",
               lead="Le rapport de force s'est inversé en une seule réforme."),

    d.layers(2, "Les 3 conditions<br>du vote", "Elles sont cumulatives",
             [("Condition 1", "Ce n'est pas une résidence principale",
               "Les lots visés sont forcément des résidences secondaires."),
              ("Condition 2", "Les lots sont à usage d'habitation",
               "L'immeuble doit être destiné au logement."),
              ("Condition 3", "Le règlement interdit toute activité commerciale",
               "C'est ici, dans ce seul mot, que se cache toute la parade.")],
             "Le détail qui compte", "Les trois doivent être réunies. Une seule qui manque, et le vote tombe.",
             lead="Sans ces trois conditions réunies, l'interdiction ne tient pas."),

    d.pincer(3, "Le piège<br>qu'on te cache", "Deux détails rarement expliqués",
             ("Le second vote", "Si les deux tiers ne sont pas atteints, un deuxième vote peut passer à la majorité simple."),
             ("L'autodéclaration", "Déclarer ton meublé oblige le syndic à inscrire ton activité à l'ordre du jour."),
             ("Le système se déclenche seul", "Ta démarche légale met elle-même le sujet sur la table de l'assemblée."),
             "À retenir", "Ce ne sont pas tes voisins qui se réveillent : c'est la machine qui les convoque.",
             lead="Deux mécanismes rendent l'interdiction bien plus accessible qu'annoncé."),

    d.compare(4, "Civil<br>ou commercial", "Là se joue tout",
              {"head": "Ce qui te met en danger", "items": [
                  "Une réception permanente sur place",
                  "Le petit-déjeuner inclus pour tous",
                  "Des prestations automatiques systématiques",
                  "Une expérience qui imite l'hôtel"]},
              {"head": "Ce qui te protège", "items": [
                  "Une exploitation purement locative",
                  "Des services proposés en option",
                  "Une facturation à part, jamais incluse",
                  "Aucun accueil systématisé"]},
              "Les décisions", "Cour de cassation du 25 janvier 2024, cour d'appel d'Aix-en-Provence du 20 mars 2025.",
              lead="La Cour de cassation a tranché le 25 janvier 2024 : louer en meublé reste civil."),

    d.mindmap(5, "Le paradoxe<br>qui pique", "Ce que le marché te vend",
              "Le premium<br>te fragilise",
              [("L'accueil systématique", "Présenté comme un gage de qualité, il ressemble à une réception d'hôtel."),
               ("Le petit-déjeuner inclus", "Inclus pour tous, il devient une prestation automatique."),
               ("L'expérience hôtelière", "L'argument marketing devient une pièce à conviction pour le syndic."),
               ("Le réflexe à prendre", "Garde les mêmes services, mais en option et facturés à part.")],
              "À retenir", "Ce qui fait vendre ton annonce peut la rendre interdisable.",
              lead="Les prestations les plus valorisées sont celles qui te font basculer."),

    d.checklist(6, "Avant d'acheter<br>ou de te lancer", "La checklist investisseur",
                [(True, "Lire le règlement de copropriété",
                  "Cherche s'il interdit vraiment toute activité commerciale, et s'il tolérait déjà des professions libérales."),
                 (True, "Récupérer les trois derniers procès-verbaux",
                  "Des décisions ont pu être votées sans jamais être reportées dans le règlement."),
                 (True, "Vérifier la date du règlement",
                  "Depuis le 21 novembre 2024, il doit dire explicitement si le meublé de tourisme est autorisé."),
                 (True, "Contrôler le changement d'usage",
                  "La copropriété peut dire oui et la mairie non : les deux contrôles se cumulent.")],
                "Réflexe", "Un doute sérieux ? Un professionnel du droit de la copropriété tranchera.",
                lead="Quatre vérifications avant de signer quoi que ce soit."),

    d.flow(7, "Si ta copropriété<br>vote demain", "Tu exploites déjà",
           [("Regarde où tu en es",
             "Relis le règlement et les procès-verbaux avant même la prochaine convocation."),
            ("Repasse en civil pur",
             "Arrête toute prestation automatique de type hôtelier, dès maintenant."),
            ("Sache que le vote se conteste",
             "L'interdiction doit être justifiée par la destination de l'immeuble, sous le contrôle du juge.")],
           "À retenir", "Il n'y a ni protection des activités existantes, ni indemnisation : la préparation est ta seule assurance.",
           lead="Aucune clause du grand-père ne protège les activités en cours."),

    d.cta("Action · 1 mot",
          'Ton règlement de copropriété<br>te laisse-t-il ' + acc("exploiter") + ' ?',
          "COPRO",
          "et je t'envoie la checklist complète pour vérifier ton règlement point par point.",
          "Vérifie avant l'assemblée générale, pas après le vote."),

    d.closing("11 ans de terrain pour t'aider à bâtir une activité "
              + "<em>solide</em>, pas une loterie."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
