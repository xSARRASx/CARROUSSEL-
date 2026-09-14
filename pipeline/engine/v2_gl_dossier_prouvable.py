#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Les 5 erreurs qui declenchent un controle fiscal pour les hotes Airbnb"
(14/09/2026, h0fE0L6d5QI).

Angle produit : LE DOSSIER QUI SE PROUVE. La video montre que l'administration
possede deja les chiffres des plateformes (DAC7) et qu'un ecart, une charge sans
facture ou un justificatif manquant suffisent a faire remonter un dossier. Le
pont honnete cote outil : ce qu'on doit pouvoir montrer ne se reconstruit pas au
printemps, il s'enregistre toute l'annee, logement par logement.

Fonctions citees, toutes issues de la banque produit (section A2 de carroussel.md) :
  - Channel Manager natif (Airbnb, Booking, Abritel, synchro temps reel)
  - Moteur de reservation directe (site direct 0 % commission)
  - Caution integree via Stripe, compte par proprietaire (conforme loi Hoguet)
  - Planning menages + application mobile prestataires
  - Facturation electronique conforme reforme 2026
  - Interface proprietaire avec KPIs temps reel, dashboard
⛔ NE RIEN INVENTER au-dela de cette liste. En particulier, l'outil ne fait PAS
la declaration fiscale, ne produit PAS de liasse et ne remplace PAS un comptable.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Couverture : cover_duo. Semaine derniere GL = cover_citation, et LSL prend
cover_chiffre cette semaine : rotation respectee (regle 16).

Usage : python3 v2_gl_dossier_prouvable.py && python3 render.py v2_gl_dossier_prouvable
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_gl_dossier_prouvable"

d = Deck("guestlucky")
d.set_bg_photo("gl_dossier_prouvable_bg.jpg", veil=0.82)

SLIDES = [
    d.cover_duo(
        "Guestlucky · Dossier prouvable",
        "Un contrôle ne se<br>prépare pas en avril",
        ("Au printemps", "Tu fouilles",
         "Trois boîtes mail, deux exports, des captures d'écran, une addition à la main."),
        ("Toute l'année", "Tu exportes",
         "Chaque réservation, chaque facture, chaque intervention, déjà rattachée au bon logement.")),

    d.compare(1, "Le même parc,<br>deux moments<br>de vérité", "Quand le propriétaire demande ses chiffres",
              {"head": "Celle qui reconstruit", "items": [
                  "Elle rouvre trois extranets pour un seul total",
                  "Elle additionne les plateformes à la main, une fois par an",
                  "Elle retrouve les factures de ménage si elle les a gardées",
                  "Elle répond « je te renvoie ça » et met deux semaines"]},
              {"head": "Celle qui exporte", "items": [
                  "Tout est déjà consolidé au même endroit",
                  "Chaque montant reste rattaché à son logement et à sa plateforme",
                  "Les interventions sont horodatées au moment où elles ont lieu",
                  "Elle répond le jour même, avec des chiffres datés"]},
              "La différence", "Ce n'est pas un travail de plus en avril. C'est le même travail, fait au moment où l'information existe.",
              lead="Ce que tu ne peux pas montrer, tu ne pourras pas le prouver non plus."),

    d.flow(2, "Un seul endroit<br>pour toutes<br>les recettes", "La consolidation",
           [("Les plateformes arrivent ensemble",
             "Le channel manager natif synchronise Airbnb, Booking et Abritel en temps réel, sans export manuel."),
            ("La réservation directe entre au même endroit",
             "Le moteur de réservation directe alimente le même calendrier : elle ne reste pas dans un coin de tableur."),
            ("Chaque montant reste attaché à son logement",
             "Le dashboard et les KPIs suivent le parc bien par bien, pas en un seul total indifférencié.")],
           "Le point de vigilance", "L'administration additionne toutes les plateformes. Un dossier qui n'en déclare qu'une crée un écart sans le vouloir.",
           lead="Trois canaux, un seul total : c'est exactement ce que le fichier reçu en face contient déjà."),

    d.checklist(3, "Ce qui n'est pas<br>du chiffre d'affaires", "La confusion la plus chère",
                [(True, "La caution reste à sa place",
                  "Encaissée via Stripe sur un compte par propriétaire, conforme à la loi Hoguet : elle ne se mélange jamais aux recettes."),
                 (True, "La taxe de séjour collectée n'est pas une recette",
                  "Elle est reversée à la commune. L'inclure dans les revenus, c'est payer de l'impôt sur un montant qui n'est pas à toi."),
                 (False, "Le montant versé n'est pas le montant déclaré",
                  "Ce qui arrive sur le compte est net de commission. Le montant de référence est le brut payé par le voyageur."),
                 (False, "Une plateforme oubliée ne passe pas inaperçue",
                  "Le total consolidé est déjà connu en face : c'est la déclaration qui doit s'y aligner, pas l'inverse.")],
                "Le réflexe", "Séparer les flux au moment de l'encaissement coûte zéro minute. Les démêler un an plus tard coûte une journée.",
                lead="Quatre montants qui se ressemblent sur un relevé et qui n'ont rien à faire au même endroit."),

    d.layers(4, "Trois étages<br>d'un dossier<br>qui tient", "De la recette à la preuve",
             [("Étage 1", "Les recettes",
               "Ce qui a été réservé, sur quelle plateforme, pour quel logement, sur quelles nuits."),
              ("Étage 2", "Les dépenses prouvées",
               "Le planning ménages et l'application prestataires horodatent les interventions ; la facturation électronique conforme à la réforme 2026 garde les pièces."),
              ("Étage 3", "La restitution",
               "L'interface propriétaire et ses KPIs temps réel : il consulte lui-même au lieu de te réclamer un récapitulatif.")],
             "Ce qui manque le plus souvent", "Le deuxième étage. Une charge sans pièce justificative ne se déduit pas, quel que soit le montant réellement payé.",
             lead="Les deux premiers étages font le chiffre. Le troisième fait la confiance."),

    d.mindmap(5, "Ce qu'on te<br>redemandera", "Les quatre pièces",
              "Sur trois<br>années<br>en arrière",
              [("Le total par logement", "Toutes plateformes confondues, période par période, sans recoupement à la main."),
               ("Les factures d'intervention", "Ménages, maintenance, prestataires : datées, rattachées au bien concerné."),
               ("Ce qui a été reversé", "Ce qui revient au propriétaire et ce qui reste ta rémunération, clairement séparés."),
               ("La période exacte", "Une date d'arrivée et une date de départ, pas un mois approximatif.")],
              "Le calendrier de l'administration", "Elle peut revenir trois ans en arrière sur une déclaration et réclamer les pièces sur six.",
              lead="Quatre éléments qui existent déjà, à condition d'avoir été enregistrés au bon moment."),

    d.pincer(6, "Deux demandes,<br>le même mois", "Et elles tombent ensemble",
             ("Le propriétaire", "Il veut ses chiffres pour sa propre déclaration, et il les veut maintenant."),
             ("L'administration", "Elle a déjà reçu les fichiers des plateformes et compare avec ce qui a été déclaré."),
             ("Tu es entre les deux", "Ta conciergerie n'est pas contrôlée à sa place, mais c'est chez toi que se trouvent ses justificatifs."),
             "La position confortable", "Répondre en consultant, pas en reconstituant. C'est ce qui fait la différence entre un prestataire et un partenaire.",
             lead="Chaque printemps, la même semaine, deux personnes attendent des chiffres de toi."),

    d.timeline(7, "L'année vue<br>du dossier", "Rien ne se joue en avril",
               [("Janvier", "Les rapports annuels tombent",
                 "Chaque plateforme envoie son récapitulatif : c'est la copie de ce qui part à l'administration.", True),
                ("Printemps", "La déclaration doit s'aligner",
                 "Le total consolidé se compare, plateforme par plateforme, à ce qui a été enregistré toute l'année.", False),
                ("Décembre", "La CFE arrive",
                 "La location meublée est une activité professionnelle au sens de la CFE, même pour un seul bien.", False),
                ("Toute l'année", "Les pièces s'accumulent",
                 "Interventions horodatées, factures conformes, flux séparés : c'est là que le dossier se fabrique.", False)],
               "L'honnêteté", "Ces repères viennent de la vidéo de Sébastien. Un outil de gestion ne remplace ni un comptable ni ta déclaration.",
               lead="Quatre moments, dont un seul est visible : les trois autres décident du résultat."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Ton parc serait-il<br>' + acc("prouvable") + ' demain matin ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le suivi consolidé du parc sur le site.",
        "Le meilleur moment pour construire un dossier propre, c'est pendant que la saison tourne."),

    d.closing("Le PMS qui garde la trace "
              + "<em>pendant que tu gères</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_duo")
