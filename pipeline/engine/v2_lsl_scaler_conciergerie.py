#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Conciergerie 30 logements en 1 an : la methode complete en 2026" (Mq4pGuah050).

Angle coaching : LA CROISSANCE STRUCTUREE. Les 3 erreurs de depart, puis les
4 piliers, palier par palier. Sujet jamais traite : les carrousels precedents
portaient sur la copropriete, la fiscalite, la discretion financiere et le
remplissage de calendrier.

⛔ Sebastien n'est pas juriste : il relaie des decisions de justice et sa
pratique. La slide 7 le dit.
⛔ Nom exact de la loi : loi HOGUET (transcrite "loi OG" / "loi Ague" par
l'outil de transcription automatique).
⛔ Aucun denigrement : on ne nomme aucune conciergerie condamnee.

Usage : python3 v2_lsl_scaler_conciergerie.py && python3 render.py v2_lsl_scaler_conciergerie
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_scaler_conciergerie"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_scaler_conciergerie_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'De 0 à 30 logements,<br>' + acc("sans t'épuiser"),
        "Les trois erreurs qui font plafonner, et les quatre paliers qui font passer",
        "Décryptage terrain. Je ne suis pas juriste : je relaie ce que les juges ont retenu."),

    d.compare(1, "Deux façons<br>de démarrer", "Et une seule tient dans le temps",
              {"head": "Le bricolage", "items": [
                  "Un contrat gratuit trouvé quelque part sur internet",
                  "Les annonces créées sur ton propre compte",
                  "On verra plus tard pour structurer",
                  "Tu cours après chaque nouveau propriétaire"]},
              {"head": "Le système", "items": [
                  "Un contrat et des annexes pensés pour ton cadre",
                  "Chaque compte ouvert au nom du propriétaire",
                  "Le processus posé avant d'accélérer",
                  "Un canal qui ramène les propriétaires vers toi"]},
              "La bascule", "Arrête de chercher des clients. Construis ce que les propriétaires viendront choisir.",
              lead="À dix logements, l'une des deux ne peut plus se restructurer sans tout casser."),

    d.checklist(2, "Les trois erreurs<br>qui plafonnent", "Vues sur 90 % des créations",
                [(False, "Démarrer en mode bricolage",
                  "Contrat improvisé, comptes à ton nom : à quinze logements, tout est à refaire."),
                 (False, "Vendre de la gestion",
                  "Le mot te fait tomber sous la loi Hoguet. Le bon vocabulaire : pilotage, coordination, prestation."),
                 (False, "Signer les contrats un par un",
                  "Tu arrives à dix, épuisé, et tu as simplement recréé un emploi salarié.")],
                "Le vrai test", "Travailles-tu DANS ton entreprise, ou SUR ton entreprise ?",
                lead="Une seule de ces erreurs te bloque. Deux, et tu fermes dans les mois qui viennent."),

    d.stats(3, "Les quatre paliers", "Dans cet ordre, jamais en même temps",
            [("1 à 5", "Les fondations, la phase que tout le monde saute"),
             ("5 à 12", "Le système, les outils et l'accueil standardisé"),
             ("10 à 20", "L'effet de levier, là où la plupart restent bloquées"),
             ("20 à 30", "L'industrialisation, quand on mesure pour piloter")],
            "L'erreur classique", "Vouloir brancher les outils avant même d'avoir signé le premier contrat.",
            lead="Quatre phases à dérouler à la suite. En sauter une coûte toujours plus cher."),

    d.layers(4, "Palier 1<br>les fondations", "De 1 à 5 contrats",
             [("Fondation 1", "Ta proposition contractuelle",
               "Un contrat et des annexes séparées, pour faire évoluer le cadre sans tout réécrire."),
              ("Fondation 2", "Ta zone",
               "Une ville et 30 km autour, pas davantage. Idéalement là où tu connais déjà du monde."),
              ("Fondation 3", "Ton prix",
               "Démarrer au plus bas pour rentrer, c'est se condamner à ne jamais remonter.")],
             "Le premier geste", "Dis simplement autour de toi que tu fais ce métier. Beaucoup n'osent même pas.",
             lead="Cinq contrats posés proprement valent mieux que quinze à reconstruire."),

    d.flow(5, "Palier 2<br>le système", "De 5 à 12 contrats",
           [("Tout ouvrir au nom du propriétaire",
             "Comptes de plateformes et outils de tarification. C'est lui qui pilote ses prix, pas toi."),
            ("Standardiser l'accueil d'un nouveau bien",
             "Un parcours documenté étape par étape, au point que quelqu'un d'autre puisse le dérouler."),
            ("Organiser la sous-traitance du ménage",
             "Ménage et linge : le premier vrai levier opérationnel, et celui qui te libère du temps.")],
           "La nuance", "L'outil de coordination peut rester au nom de ta société. Les comptes commerciaux, non.",
           lead="Un bien qui prenait quinze jours à lancer doit finir par en prendre trois."),

    d.mindmap(6, "Palier 3<br>l'acquisition", "De 10 à 20 contrats",
              "Trois canaux,<br>et un recrutement",
              [("Le bouche à oreille structuré", "Un parrainage clair : un mois de prestation offert pour un propriétaire apporté."),
               ("Les propriétaires insatisfaits", "Ils cherchent une conciergerie qui respecte le cadre. Ils vont être de plus en plus nombreux."),
               ("Le référencement local", "Fiche d'établissement, réseaux sociaux. Lent, un an parfois, mais durable."),
               ("Le responsable local", "Il lance et suit les contrats que tu ramènes. Ce n'est pas un assistant.")],
              "Pourquoi ça bloque ici", "Sans canal construit, tu restes en prospection permanente et tu plafonnes à douze.",
              lead="C'est le palier où la plupart des conciergeries s'arrêtent."),

    d.pincer(7, "Palier 4<br>et le sujet<br>qui fâche", "De 20 à 30 contrats",
             ("Ce que tu mesures", "Taux d'occupation, prix moyen par nuit, revenu par contrat, délai de lancement, satisfaction du propriétaire."),
             ("Ce que les juges ont retenu", "En 2025, deux conciergeries condamnées : loyers encaissés à leur nom, comptes tenus à leur place, prix fixés sans validation du propriétaire."),
             ("Le contrat ne suffit pas", "Les juges ont regardé la pratique réelle, pas seulement ce qui était écrit."),
             "Honnêteté", "Décisions de première instance. Fais valider ton montage par un professionnel du droit.",
             lead="On ne mesure bien que ce qu'on a d'abord rendu conforme."),

    d.cta("Action · 1 mot",
          'À quel palier<br>es-tu ' + acc("bloqué") + ' ?',
          "PILIERS",
          "et je t'envoie le plan de lancement, phase par phase, avec la grille de tarification.",
          "Six mois à construire avant de récolter. C'est la phase que tout le monde abandonne."),

    d.closing("11 ans de terrain pour construire une conciergerie "
              + "<em>qui tient</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
