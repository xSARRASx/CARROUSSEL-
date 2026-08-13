#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Un proprietaire Airbnb vient de gagner contre sa copropriete au tribunal" (13/08/2026).

Angle coaching : le miroir POSITIF de la video du 29/07. Tribunal judiciaire de
Nice, 23 juillet 2026 : les resolutions d'interdiction annulees, copropriete
deboutee et condamnee. Les 5 boucliers qu'un investisseur peut activer.

Usage : python3 v2_lsl_boucliers_copropriete.py && python3 render.py v2_lsl_boucliers_copropriete
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_boucliers_copropriete"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_boucliers_copropriete_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Une copropriété attaque<br>et ' + acc("perd"),
        "Tribunal judiciaire de Nice, 23 juillet 2026 : les cinq boucliers qui ont fait basculer le dossier",
        "Décryptage terrain. Je ne suis pas avocat : je lis la décision et je la relaie."),

    d.timeline(1, "Comment l'affaire<br>s'est déroulée", "Trois ans de procédure",
               [("Été 2023", "La mise en demeure",
                 "Le syndic exige l'arrêt immédiat de ce qu'il appelle une activité commerciale.", False),
                ("Novembre 2023", "Deux résolutions votées",
                 "Interdiction des locations de courte durée, et mandat pour attaquer en justice.", False),
                ("La demande", "500&nbsp;€ d'astreinte par infraction",
                 "L'avocat de la copropriété réclame une pénalité à chaque séjour.", False),
                ("23 juillet 2026", "Le jugement",
                 "Les deux résolutions annulées, la copropriété déboutée et condamnée à 2&nbsp;000&nbsp;€.", True)],
               "À retenir", "L'avocat de la copropriété est payé par les copropriétaires. Donc aussi par toi.",
               lead="Un propriétaire a refusé de se plier, et il est allé au bout."),

    d.pincer(2, "Le cœur<br>du jugement", "Bouclier numéro 1",
             ("Ce que disait la copropriété", "La location de courte durée est une activité commerciale, donc interdite par le règlement."),
             ("Ce qu'a répondu le tribunal", "Sans prestations para-hôtelières, l'activité reste civile. Cour de cassation du 25 janvier 2024."),
             ("Juridique et fiscal ne se confondent pas", "Être imposé aux bénéfices industriels et commerciaux ne rend pas ton activité commerciale."),
             "Le point clé", "Le tribunal a désamorcé noir sur blanc l'argument préféré des syndics.",
             lead="Toute l'affaire tenait sur un seul mot du règlement : commercial."),

    d.checklist(3, "Les quatre prestations<br>qui font basculer", "Bouclier numéro 2",
                [(False, "Le petit-déjeuner",
                  "Fourni à tous les voyageurs, il compte comme prestation para-hôtelière."),
                 (False, "Le nettoyage régulier des locaux",
                  "Pendant le séjour. Le ménage de fin de séjour n'est PAS un critère."),
                 (False, "La fourniture du linge de maison",
                  "Le renouvellement du linge en cours de séjour entre dans le décompte."),
                 (False, "La réception de la clientèle",
                  "Une réception organisée, même non personnalisée, pas un simple accueil.")],
                "La règle", "Il faut en cumuler au moins TROIS sur quatre pour basculer dans le commercial.",
                lead="Article 261 D du code général des impôts : ce sont ces quatre-là que le juge regarde."),

    d.compare(4, "L'accueil ne rend<br>pas commercial", "Ce que la copropriété a tenté",
              {"head": "Les preuves versées au dossier", "items": [
                  "Un constat d'huissier sur l'annonce en ligne",
                  "Des avis mentionnant un accueil des voyageurs",
                  "La remise des clés en main propre",
                  "Des conseils touristiques donnés sur place"]},
              {"head": "La réponse du tribunal", "items": [
                  "Cela ne suffit pas à requalifier l'activité",
                  "L'accueil reste dans le domaine civil",
                  "Un seul critère éventuel, pas trois sur quatre",
                  "Le ménage de fin de séjour ne compte pas"]},
              "Ce qui ferait basculer", "Un ensemble complet : petit-déjeuner, ménage quotidien, linge et réception réunis.",
              lead="Le check-in en personne et le mot d'accueil ne te font pas changer de camp."),

    d.layers(5, "Les trois autres<br>boucliers", "Ceux qu'on oublie de vérifier",
             [("Bouclier 3", "Le règlement lui-même",
               "L'avocat l'a lu. Il y était écrit que les locations meublées par appartement entier sont autorisées."),
              ("Bouclier 4", "Les troubles jamais prouvés",
               "Bouteilles, stationnement, bruit : aucun constat, aucune lettre, un dossier vide."),
              ("Bouclier 5", "Le vice de majorité",
               "Le vote de 2023 exigeait l'unanimité. Il est passé à la majorité simple : nul.")],
             "La phrase à retenir", "La justice ne juge pas des impressions, elle juge des pièces.",
             lead="Trois failles que presque personne ne pense à chercher dans son propre dossier."),

    d.mindmap(6, "Ce que la loi<br>Le Meur change", "Et ce qu'elle ne change pas",
              "Plus facile,<br>pas imparable",
              [("Le vote est facilité", "Deux tiers des voix suffisent désormais, au lieu de l'unanimité."),
               ("La justification reste exigée", "Un vote doit être fondé sur la destination réelle de l'immeuble."),
               ("Le règlement prime toujours", "S'il autorise le meublé, l'interdiction devient bien plus fragile."),
               ("Deux mois pour contester", "Le délai court dès qu'une résolution hostile est adoptée.")],
              "À retenir", "Un vote mal justifié contre une activité civile se conteste toujours.",
              lead="Le nouveau texte rend le vote plus simple, pas l'interdiction automatique."),

    d.flow(7, "Ce que tu fais<br>dès maintenant", "Sans attendre la convocation",
           [("Ressors tes documents",
             "Le règlement de copropriété et les procès-verbaux des dernières assemblées générales."),
            ("Construis ton dossier en parallèle",
             "Journal des accès, règlement intérieur, insonorisation, rapports de suivi du bruit."),
            ("Exige des pièces, produis les tiennes",
             "Face à une accusation de nuisance, demande dates et constats, et apporte tes preuves.")],
           "Honnêteté", "Ce jugement est rendu en premier ressort : un appel reste possible. Mais il applique la Cour de cassation.",
           lead="Le meilleur moment pour préparer ta défense, c'est avant qu'on t'attaque."),

    d.cta("Action · 1 mot",
          'Ton règlement te protège-t-il<br>vraiment ' + acc("aujourd'hui") + ' ?',
          "BOUCLIER",
          "et je t'envoie la grille de lecture pour vérifier ton règlement et tes procès-verbaux.",
          "Cinq boucliers ont suffi. Encore faut-il savoir qu'ils existent."),

    d.closing("11 ans de terrain pour t'aider à défendre ton activité "
              + "<em>avec des pièces</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
