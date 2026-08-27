#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Comment faire baisser sa taxe fonciere ?" (h0GZh51rtCk, 26/08/2026).

Angle produit FORCE (regle 14 : sujet hors theme conciergerie, on produit quand
meme les deux en forcant l'angle). Le pont honnete : l'avis de taxe fonciere
arrive a l'automne, le proprietaire decouvre sa premiere charge, et il se
retourne vers sa conciergerie en doutant de la rentabilite. La conciergerie qui
peut sortir l'annee entiere, logement par logement, ne subit pas cette
conversation.

⛔ INTERDIT ABSOLU d'insinuer que l'outil calcule, conteste ou fait baisser une
taxe fonciere. Ce n'est ni son role ni son metier. La slide 7 le dit noir sur
blanc, la legende aussi.
⛔ Ne PAS citer verifoncier.fr : c'est l'outil de Sebastien, pas Guestlucky.
⛔ Le verbe "gerer" est proscrit cote conciergerie (loi Hoguet, regle du 24/08).
⛔ Mots bannis : beds24, mandat de gestion, garantie financiere.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_automne_proprietaire.py && python3 render.py v2_gl_automne_proprietaire
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_automne_proprietaire"

d = Deck("guestlucky")
d.set_bg_photo("gl_automne_proprietaire_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Automne",
        'Son avis arrive,<br>et c\'est ' + acc("toi qu\'il appelle"),
        "30 millions de propriétaires reçoivent leur taxe foncière en ce moment."),

    d.pincer(1, "Ce qui se passe<br>vraiment en octobre", "La conversation annuelle",
             ("Ce qu'il découvre", "Sa taxe foncière, devenue l'une de ses premières charges, en hausse pour la quatrième année consécutive."),
             ("Ce qu'il en conclut", "Que le rendement de son bien n'est peut-être pas celui qu'on lui avait annoncé."),
             ("Et donc il t'appelle", "Pas pour parler d'impôts, mais pour te demander ce que son logement lui a réellement rapporté cette année."),
             "Le vrai enjeu", "Ce n'est pas une question fiscale. C'est une question de confiance, posée au mauvais moment.",
             lead="Sa charge augmente, et la seule personne qu'il a en face, c'est toi."),

    d.compare(2, "Deux façons<br>de répondre", "Le même parc, deux impressions",
              {"head": "Reconstituer", "items": [
                  "Remonter douze mois de conversations",
                  "Recompter les nuits une par une",
                  "Retrouver les factures d'intervention",
                  "Rendre un tableau fait à la main"]},
              {"head": "Ouvrir", "items": [
                  "L'année est déjà rangée par logement",
                  "Chaque mois a son rapport daté",
                  "Les interventions sont documentées",
                  "Il consulte lui-même quand il veut"]},
              "La différence", "Dans les deux cas tu réponds. Dans un seul, il te croit sur parole sans avoir à te croire.",
              lead="La question arrive toujours au moment où tu as le moins de temps."),

    d.checklist(3, "Ce que tu dois<br>pouvoir sortir", "Sans préavis",
                [(True, "Ce que le logement a encaissé, mois par mois",
                  "Le brut, et ce que les plateformes ont réellement prélevé au passage."),
                 (True, "Ce qui a été dépensé pour lui",
                  "Interventions, réparations, prestataires, chacune rattachée au bon bien et à la bonne date."),
                 (True, "Le taux de remplissage réel",
                  "Pas une moyenne de secteur : ses nuits à lui, sur ses douze derniers mois."),
                 (True, "Les documents de son bien",
                  "Au même endroit, pour qu'il n'ait pas à te les redemander chaque automne.")],
                "Le test", "Combien de temps te faudrait-il, là, tout de suite, pour sortir ces quatre éléments ?",
                lead="Quatre éléments, et il les demandera tous les quatre."),

    d.layers(4, "Trois niveaux<br>de lecture", "Ce qu'il veut vraiment savoir",
             [("Niveau 1", "Le chiffre",
               "Ce que son logement a rapporté cette année. C'est la question qu'il pose à voix haute."),
              ("Niveau 2", "L'explication",
               "Pourquoi ce chiffre-là : la saison, les prix pratiqués, les nuits vides et leurs raisons."),
              ("Niveau 3", "La preuve",
               "Des rapports mensuels datés qu'il peut relire lui-même, sans repasser par toi.")],
             "Ce qui manque presque toujours", "Le troisième. Sans lui, le premier niveau reste une affirmation.",
             lead="Il pose une question simple, mais il en attend trois réponses."),

    d.flow(5, "Comment l'automne<br>se prépare", "En janvier, pas en octobre",
           [("Chaque réservation laisse sa trace",
             "Rattachée au logement, avec sa date et ce que la plateforme a retenu."),
            ("Chaque intervention est documentée",
             "Ce qui a été fait, quand, par qui, avec les photos et la facture au bon endroit."),
            ("Chaque mois se clôture tout seul",
             "Le rapport est horodaté et archivé, consultable des mois plus tard sans rien reconstituer.")],
           "Le principe", "Ce qui n'est pas rangé sur le moment ne se retrouve jamais douze mois plus tard.",
           lead="Le dossier d'octobre se remplit tout au long de l'année, ou pas du tout."),

    d.mindmap(6, "Ce que l'outil<br>garde pour toi", "Logement par logement",
              "Répondre<br>en ouvrant,<br>pas en cherchant",
              [("Les encaissements", "Rattachés au logement et à la réservation qui les a produits."),
               ("Les interventions", "Documentées et datées, avec leurs reportings photo."),
               ("Les rapports mensuels", "Horodatés et archivés, relisibles des mois après."),
               ("L'interface propriétaire", "Il consulte son activité lui-même, quand la question lui vient.")],
              "Le résultat", "L'automne devient un rendez-vous, au lieu d'une mise en cause.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées au bon endroit."),

    d.pincer(7, "Ce qui est<br>ton rôle", "Et ce qui ne l'est pas",
             ("Ton rôle", "Montrer clairement ce que son logement a produit et ce qu'il a coûté, avec des pièces datées."),
             ("Pas ton rôle", "Sa fiscalité. Sa taxe foncière ne se calcule pas, ne se conteste pas et ne se corrige pas depuis un outil de conciergerie."),
             ("Ce que tu peux faire d'utile", "Lui dire qu'une fiche d'évaluation existe, qu'elle est gratuite, et le laisser voir cela avec un professionnel du chiffre."),
             "À dire clairement", "Guestlucky garde les traces de l'exploitation. Il ne fait ni comptabilité ni fiscalité.",
             lead="La frontière est nette, et la tenir te protège autant que lui."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Son année, tu la sortirais<br>en ' + acc("combien de temps") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post avant l'automne, et découvre le suivi par logement sur le site.",
        "Le meilleur moment pour ranger un justificatif, c'est le jour où il arrive."),

    d.closing("L'outil qui garde la trace, pour que l'automne soit "
              + "<em>un rendez-vous</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
