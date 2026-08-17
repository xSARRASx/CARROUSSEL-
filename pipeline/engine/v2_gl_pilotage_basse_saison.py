#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Remplir son Airbnb sans baisser les prix ? C'est possible !" (17/08/2026, iVd1TQ-GUYs).

Angle produit : PILOTER LA BASSE SAISON ET GARDER SES MANDATS. Different du
carrousel GL du 03/08, qui portait sur l'audit d'annonce. Ici : le bonus
conciergerie de la video ("la basse saison, c'est le moment ou les proprietaires
doutent et ou les mandats se perdent"), et les reglages qui se rejouent logement
par logement.

Fonctions citees explicitement par Sebastien dans cette video :
  - channel manager (les reglages partent vers les plateformes)
  - revenue management : remises last minute
  - bouche-trou (gap fill) pour les nuits orphelines
Fonctions deja etablies dans les carrousels precedents :
  - rapports mensuels horodates et archives, documents classes par logement,
    historique des echanges, interface proprietaire.
⛔ NE RIEN INVENTER au-dela de cette liste. En particulier, l'outil ne fixe pas
les prix a ta place : il applique les regles que tu decides.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_pilotage_basse_saison.py && python3 render.py v2_gl_pilotage_basse_saison
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_pilotage_basse_saison"

d = Deck("guestlucky")
d.set_bg_photo("gl_pilotage_basse_saison_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Basse saison",
        'La saison creuse,<br>c\'est là que ' + acc("les mandats partent"),
        "Le propriétaire ne voit pas ta stratégie. Il voit un calendrier vide."),

    d.compare(1, "Deux conciergeries<br>au mois de novembre", "Le même parc, deux issues",
              {"head": "Celle qui subit", "items": [
                  "Elle découvre les trous quand ils sont là",
                  "Elle répond au propriétaire par une baisse de prix",
                  "Elle règle chaque logement à la main, quand elle y pense",
                  "Elle n'a rien à montrer quand le doute s'installe"]},
              {"head": "Celle qui pilote", "items": [
                  "Ses règles d'hiver sont posées dès septembre",
                  "Elle arrive avec un plan avant qu'on le lui demande",
                  "Un réglage décidé une fois s'applique partout",
                  "Elle sort un rapport daté au lieu d'un discours"]},
              "La bascule", "Le propriétaire ne compare pas deux prix. Il compare deux niveaux de maîtrise.",
              lead="La différence ne se joue pas sur le talent, mais sur ce qui est outillé."),

    d.flow(2, "Un réglage décidé<br>une fois", "Et rejoué partout",
           [("Tu décides la règle",
             "Durée minimum, paliers de remise, dates à protéger : c'est toi qui tranches, pas un algorithme."),
            ("Elle part vers tes plateformes",
             "Le channel manager pousse le réglage au lieu de te faire rouvrir chaque annonce une par une."),
            ("Elle se rejoue chaque semaine",
             "Les remises last minute et le bouche-trou tournent sur tes dates proches sans que tu y penses.")],
           "Le cadre", "L'outil n'invente pas ta stratégie de prix : il exécute celle que tu as posée.",
           lead="Vingt logements à régler à la main en octobre, c'est vingt occasions d'en oublier un."),

    d.checklist(3, "Ce qui se règle<br>avant octobre", "La liste de septembre",
                [(True, "Le calendrier ouvert le plus loin possible",
                  "Sinon tu es invisible pour tous ceux qui réservent longtemps à l'avance."),
                 (True, "Les paliers de remise, pas une baisse unique",
                  "Prix plein au loin, remise modérée à l'approche, remise franche sur les dates proches."),
                 (True, "La durée minimum remontée en semaine",
                  "Une nuit isolée coûte un ménage complet pour une seule recette."),
                 (True, "Le bouche-trou activé sur les nuits orphelines",
                  "La nuit seule coincée entre deux réservations est celle qu'on récupère le plus facilement.")],
                "Le bon moment", "Ces quatre réglages ne valent rien en janvier. Ils valent tout en septembre.",
                lead="Quatre décisions à prendre une fois, puis à laisser tourner tout l'hiver."),

    d.layers(4, "Trois étages<br>du pilotage", "De la date à la preuve",
             [("Étage 1", "Le calendrier",
               "Ce qui est ouvert, ce qui est bloqué, ce qui est déjà réservé, sur toutes tes plateformes."),
              ("Étage 2", "Les règles",
               "Durées minimum, remises last minute, bouche-trou : le comportement de ton parc en creux."),
              ("Étage 3", "La preuve",
               "Des rapports mensuels horodatés et archivés, consultables des mois plus tard.")],
             "Ce qui manque presque toujours", "Le troisième étage. C'est pourtant celui que le propriétaire réclame.",
             lead="Les deux premiers étages remplissent. Le troisième garde le mandat."),

    d.pincer(5, "Deux moments<br>où un mandat<br>se perd", "Et ils arrivent ensemble",
             ("Quand le calendrier se vide", "Le propriétaire regarde les mois à venir, ne voit rien, et commence à douter de toi."),
             ("Quand il n'a pas de nouvelles", "Le silence en basse saison ressemble beaucoup à de l'abandon, même quand tu travailles."),
             ("Le rapport mensuel répond aux deux", "Il montre ce qui a été fait, à quelle date, logement par logement, avant même qu'on te le demande."),
             "Le réflexe", "N'attends pas la question. Arrive avec le plan et les chiffres du mois.",
             lead="Un mandat ne se perd presque jamais sur un seul mois catastrophique."),

    d.mindmap(6, "Ce que l'outil<br>garde pour toi", "Logement par logement",
              "De quoi<br>montrer,<br>pas raconter",
              [("Les rapports mensuels", "Horodatés et archivés, ils tiennent lieu de mémoire du parc."),
               ("Les documents du bien", "Classés au même endroit, retrouvables sans fouiller trois boîtes mail."),
               ("L'historique des échanges", "La trace de ce qui s'est réellement passé pendant chaque séjour."),
               ("L'interface propriétaire", "Il regarde lui-même, au lieu de t'écrire pour savoir où ça en est.")],
              "Le résultat", "La confiance ne se plaide pas, elle se consulte.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées au bon endroit."),

    d.stats(7, "Les repères<br>de la basse saison", "À garder en tête",
            [("28 nuits", "Le seuil du marché de la moyenne durée"),
             ("90 à 120 j", "Le plafond annuel en résidence principale, selon la ville"),
             ("3 nuits", "La durée minimum qui protège tes semaines d'hiver"),
             ("7 jours", "La fenêtre où une remise franche reste sans effet sur ton prix de référence")],
            "Honnêteté", "Ces repères viennent de la vidéo de Sébastien. Vérifie toujours la règle applicable à ta ville.",
            lead="Quatre chiffres qui cadrent toutes les décisions d'octobre à mars."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Tes réglages d\'hiver<br>sont-ils ' + acc("déjà posés") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le pilotage de basse saison sur le site.",
        "Le meilleur moment pour préparer l'hiver, c'est pendant que l'été remplit encore."),

    d.closing("L'outil qui tient le parc quand la saison "
              + "<em>ne remplit plus toute seule</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
