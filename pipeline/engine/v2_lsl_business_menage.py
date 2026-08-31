#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Menage Airbnb : le business cache qui rapporte gros" (sWiie3c__Lo, 30/08/2026).

Angle coaching : CREER SON ENTREPRISE DE MENAGE pour les conciergeries. Sujet
jamais traite. Different du carrousel du 24/08 (scaler une conciergerie) : ici
on se place de l'autre cote, chez le prestataire.

⛔ NOMS PROPRES ECARTES : la transcription deforme le nom du module de missions
("Luy Clean" / "Lucky Clean") et le domaine de l'outil de facturation
("lukifacture.fr" / "luckifacture.fr"). On ne grave jamais un nom propre
incertain : on decrit la fonction. Meme regle que pour les nombres.
⛔ On ne nomme pas la messagerie utilisee : la transcription est claire sur
l'usage, pas sur le detail contractuel.

⚠️ REGLE 15 : legende de 2000 caracteres maximum.

Usage : python3 v2_lsl_business_menage.py && python3 render.py v2_lsl_business_menage
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_business_menage"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_business_menage_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Des missions à 70&nbsp;€<br>que ' + acc("personne ne prend"),
        "Le métier que les conciergeries s'arrachent, sans diplôme, sans local, sans capital",
        "Décryptage terrain, vu des deux côtés : conciergerie et prestataire."),

    d.pincer(1, "Le manque<br>que personne<br>ne comble", "Les deux côtés du problème",
             ("Ce que vivent les conciergeries", "Leur difficulté n'est pas de trouver des propriétaires. C'est de trouver des équipes de ménage fiables."),
             ("Ce qu'on voit dans les outils", "Des missions à 60, 70, 80&nbsp;€ qui restent affectées à personne, faute de trouver quelqu'un."),
             ("Et en face", "Des gens qui cherchent une activité rentable vite, sans apport, sans diplôme et sans local à payer."),
             "Le constat", "Les deux se cherchent et ne se trouvent pas. Tout le sujet est là.",
             lead="Un marché en pénurie, ce n'est pas un slogan : ce sont des missions vides."),

    d.compare(2, "Ce n'est pas<br>un ménage classique", "Quatre différences de fond",
              {"head": "Chez un particulier", "items": [
                  "Tu vends de l'heure, à un taux horaire",
                  "Une prestation, un client, une fois",
                  "Tu t'organises à peu près comme tu veux",
                  "Tu fais le ménage, et c'est tout"]},
              {"head": "Pour une conciergerie", "items": [
                  "Tu vends un résultat, au forfait",
                  "Un départ égale une mission, toute l'année",
                  "Fenêtre de 11h à 16h, souvent le dimanche",
                  "Tu deviens ses yeux dans le logement"]},
              "La conséquence", "Un seul contrat n'est pas une mission : c'est un flux de missions qui ne s'arrête plus.",
              lead="Le mot ménage est le même. Le métier n'a rien à voir."),

    d.stats(3, "Les prix<br>réellement pratiqués", "Relevés chez des conciergeries",
            [("40 à 60 €", "Un studio ou un petit appartement"),
             ("60 à 90 €", "Un deux ou trois pièces, en 1h30 à 2h30"),
             ("90 à 150 €", "Une maison de grande capacité, 3 heures et plus"),
             ("15 à 30 €", "Le linge de maison, environ 15&nbsp;€ par chambre")],
            "Le supplément qu'on oublie", "Une urgence se majore de 30 à 50&nbsp;%&nbsp;: être disponible au pied levé te rend unique.",
            lead="Quatre repères, et ils varient surtout selon la ville et la surface."),

    d.flow(4, "Le calcul<br>d'un seul client", "Une conciergerie de 20 logements",
           [("8 départs par logement et par mois",
             "C'est une moyenne annuelle. En haute saison, on monte plutôt vers 12."),
            ("Soit 160 missions dans le mois",
             "À 70&nbsp;€ de moyenne, cela fait 11&nbsp;200&nbsp;€ de chiffre d'affaires."),
            ("Il t'en reste 6 000 à 7 000 €",
             "Une fois les salaires, les déplacements et les cotisations passés.")],
           "Honnêteté", "C'est physique, exigeant, et ça sacrifie des week-ends. Ce n'est pas de l'argent passif.",
           lead="Un seul contrat, et le portefeuille entier d'une conciergerie avec lui."),

    d.checklist(5, "Ce qu'une conciergerie<br>regarde vraiment", "Avant même ton prix",
                [(True, "La fiabilité",
                  "Si tu ne viens pas un dimanche, le voyageur trouve un logement sale. Mauvaise note, et c'est fini."),
                 (True, "La réactivité",
                  "Départs tardifs, pannes, urgences : elle jongle en permanence. Le rapide récupère la mission."),
                 (True, "La preuve",
                  "Photos avant et après, systématiques. Dégâts signalés, réassorts à prévoir, objets oubliés."),
                 (True, "Le service complet",
                  "Linge, consommables, petite maintenance signalée. Chaque service en plus te rend irremplaçable.")],
                "Le vrai différenciant", "La photo avant-après est ce qui sépare l'amateur du professionnel. Rien d'autre.",
                lead="Quatre critères, et le prix n'arrive qu'après les quatre."),

    d.layers(6, "Comment tu<br>décroches", "Plus simple qu'on ne croit",
             [("Étape 1", "Tu les contactes une par une",
               "Une carte en ligne, le mot conciergerie, ta ville. Tu dis que tu es disponible."),
              ("Étape 2", "Tu prends même chez celles qui ont une équipe",
               "Elles auront toujours besoin d'un renfort fiable. C'est là que tu entres."),
              ("Étape 3", "Tu laisses le bouche à oreille travailler",
               "Les conciergeries se parlent entre elles. C'est ton meilleur argument commercial.")],
             "Le proposer avec le linge", "La moitié d'entre elles veulent un forfait tout inclus, et cela se facture 20 à 30&nbsp;% de plus.",
             lead="Trois étapes, et la première tient en une après-midi de messages."),

    d.mindmap(7, "Le deuxième<br>goulot", "Recruter, après avoir trouvé",
              "Ce qui bloque<br>quand ça<br>commence à marcher",
              [("Où chercher", "Groupes locaux, sites d'annonces, cooptation payée 50 à 100&nbsp;€, étudiants, personnel hôtelier en reconversion."),
               ("Le message filtrant", "Disponible le week-end ? Un moyen de transport ? Prêt pour une mission d'essai payée ?"),
               ("Le test réel", "Une mission en binôme, payée normalement : ponctualité, rythme, souci du détail."),
               ("Ce qu'on oublie de vérifier", "Sous le lit, les joints, l'intérieur du micro-ondes, le pourtour de la poubelle.")],
              "Ce qui t'évite de reformer", "Une checklist illustrée, pièce par pièce. Sans elle, tu recommences à chaque personne.",
              lead="Trouver des clients est le premier obstacle. Recruter est le second."),

    d.cta("Action · 1 mot",
          'Ce marché en pénurie,<br>tu le laisses à ' + acc("qui") + ' ?',
          "MENAGE",
          "et je t'envoie la grille de tarifs et la checklist de formation, pièce par pièce.",
          "Dans deux ans le marché sera structuré, par ceux qui commencent maintenant."),

    d.closing("11 ans de terrain pour t'aider à ouvrir "
              + "<em>la bonne porte</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
