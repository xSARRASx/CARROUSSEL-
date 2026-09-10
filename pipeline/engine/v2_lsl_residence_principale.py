#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Le fisc vous surveille : les 3 signes qui alertent sur votre residence"
(lc1huihoLio, 09/09/2026).

Angle coaching : LES TROIS DECISIONS DE JUSTICE et ce qu'elles changent.
Sujet neuf : aucun carrousel n'a traite l'exoneration de plus-value.

⚠️ REGLE 16 : couverture cover_aplat. La derniere LSL etait cover_citation.
⚠️ REGLE 15 : legende sous 2000 signes.
⛔ L'amendement des 5 ans de detention n'est PAS VOTE. La slide 7 le dit
explicitement : on ne presente jamais un projet comme du droit en vigueur.
⛔ Il n'existe AUCUN seuil legal de consommation d'electricite. C'est un indice
parmi d'autres, jamais une regle. Ne pas laisser croire l'inverse.
⛔ Sebastien n'est ni avocat ni fiscaliste. La slide 7 le rappelle.
⛔ Le domaine de son outil de verification est rendu de facon incertaine par la
transcription : on ne le cite pas, on garde le CTA habituel.

Usage : python3 v2_lsl_residence_principale.py && python3 render.py v2_lsl_residence_principale
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_lsl_residence_principale"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_residence_principale_bg.jpg", veil=0.88)

SLIDES = [
    d.cover_aplat(
        "Le Sous Loueur",
        "Ta résidence principale,<br>tu pourrais la prouver&nbsp;?",
        "Ses papiers étaient tous en règle. Sa facture d'électricité l'a trahi."),

    d.timeline(1, "Un dossier parfait<br>sur le papier", "Jugé le 9 juillet 2025",
               [("La vente", "Un studio de 13&nbsp;m² à Paris",
                 "Vendu en novembre 2016, déclaré en résidence principale, exonération demandée.", False),
                ("Ce qu'il présente", "Absolument tout",
                 "Déclaration de revenus à l'adresse, courriers de l'administration, relevés bancaires, appels de charges.", False),
                ("Ce que le fisc regarde", "Les mouvements réels",
                 "Un crédit renouvelable, un compte inactif, un livret. Aucun mouvement sur les comptes.", False),
                ("Le coup de grâce", "La consommation d'électricité",
                 "Moins que ce que consomme un réfrigérateur seul. Occupation occasionnelle, exonération refusée.", True)],
               "Le point important", "Il n'existe AUCUN seuil légal de consommation. C'est un indice parmi d'autres, pas une règle.",
               lead="Le jugement est tombé dix ans après la vente."),

    d.checklist(2, "Le portrait-robot<br>de la mise en scène", "Marseille, 29 janvier 2026",
                [(False, "Une autre résidence restée disponible",
                  "Le juge regarde si tu avais un autre endroit où vivre pendant cette période."),
                 (False, "Un changement d'adresse au dernier moment",
                  "La domiciliation modifiée alors que la vente était déjà engagée."),
                 (False, "Une consommation d'énergie ridicule",
                  "Encore elle. C'est le point qui revient dans presque toutes les décisions."),
                 (False, "Des meubles sommaires, aucune vie de famille",
                  "Le strict minimum pour faire semblant, et aucune trace d'une vie réelle sur place.")],
                "Le verdict", "Ce n'est pas votre résidence principale, c'est une mise en scène.",
                lead="Six éléments réunis, et le juge n'a même pas eu besoin du calendrier."),

    d.stats(3, "La nouveauté<br>qui change tout", "Ce n'est plus un pari perdu",
            [("40 %", "La majoration pour manquement délibéré, ajoutée par la cour"),
             ("36 000 €", "L'impôt et les prélèvements sur 100&nbsp;000&nbsp;€ de plus-value"),
             ("17 mois", "Le bien inoccupé qui a fait perdre un vendeur à Bordeaux"),
             ("1 an", "Le délai considéré comme normal entre le départ et la vente")],
            "Ce qui a changé", "Avant, tenter le coup et perdre coûtait l'impôt. Maintenant, ça coûte l'impôt plus une amende.",
            lead="Le juge a estimé que ce monsieur ne pouvait pas ignorer la situation."),

    d.pincer(4, "Le divorce<br>qui coupe<br>l'exonération", "La troisième histoire",
             ("Celui qui est resté", "Il vivait encore dans la maison au jour de la vente. Il est exonéré sur sa moitié."),
             ("Celui qui est parti", "Il avait quitté le logement deux ans plus tôt. Il est taxé sur la sienne."),
             ("Même maison, même acte notarié", "L'exonération s'apprécie pour chaque vendeur séparément. Deux traitements opposés."),
             "La leçon", "Si tu te sépares et qu'il y a un bien à vendre, le calendrier de la vente est une décision fiscale.",
             lead="Il existe des tolérances quand la vente suit rapidement la séparation."),

    d.mindmap(5, "Comment le fisc<br>croise tes données", "Depuis 2023",
              "Une fiche<br>par bien,<br>et elle décide",
              [("Ce qu'elle contient", "Qui occupe le logement, à quel titre, et depuis quand."),
               ("Ce qu'elle déclenche", "C'est d'elle que partent la taxe foncière et la taxe d'habitation."),
               ("Le durcissement", "Trois années de contrôle supplémentaires, spécifiquement sur les résidences secondaires."),
               ("La nouveauté 2026", "Même les occupants non propriétaires doivent déclarer les meublés qu'ils occupent.")],
              "La sanction du manquement", "10&nbsp;% de majoration, avec un minimum de 150&nbsp;€.",
              lead="Elle s'appelle la fiche d'occupation, et presque personne ne l'a lue."),

    d.compare(6, "Ta fiche peut<br>être fausse", "Dans les deux sens",
              {"head": "Fausse en ta défaveur", "items": [
                  "Un logement noté secondaire alors qu'il est principal",
                  "Une dépendance comptée qui n'existe plus",
                  "Une catégorie de confort trop élevée",
                  "Une taxe foncière gonflée année après année"]},
              {"head": "Fausse en ta faveur", "items": [
                  "Tu ne remarques rien pendant des années",
                  "Tu comptes sur l'exonération à la revente",
                  "Le contrôle arrive au moment de la vente",
                  "Et la majoration de 40&nbsp;% avec"]},
              "Dans les deux cas", "Tu dois savoir ce qu'il y a sur cette fiche. Va la lire, elle est en ligne.",
              lead="Une erreur en ta défaveur, tu la paies tous les ans, en silence."),

    d.flow(7, "Ce que tu fais<br>cette semaine", "Trois étapes, la première est gratuite",
           [("Va lire ta fiche",
             "Sur ton espace en ligne, la rubrique de gestion de tes biens immobiliers. Nature d'occupation, occupants, dates."),
            ("Fige l'état actuel",
             "Prends des captures d'écran. Le jour où tu contestes, tu seras content de les avoir."),
            ("Compare à la réalité",
             "Surface pondérée, catégorie de confort, dépendances. Des données parfois figées depuis les années 1970.")],
           "Honnêteté", "L'amendement des 5 ans de détention n'est PAS voté, ce n'est qu'une proposition. Et je ne suis pas fiscaliste.",
           lead="La taxe foncière se paie à la mi-octobre, et se conteste jusqu'à fin de l'année suivante."),

    d.cta("Action · 1 mot",
          'Ce qu\'il y a sur ta fiche,<br>tu le ' + acc("sais") + ' ?',
          "FICHE",
          "et je t'envoie la marche à suivre pour lire ta fiche d'occupation et repérer les anomalies.",
          "Chaque année sans vérifier, c'est une année de trop-payé qui s'envole définitivement."),

    d.closing("11 ans de terrain pour t'aider à vérifier "
              + "<em>avant qu'on te contrôle</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_aplat")
