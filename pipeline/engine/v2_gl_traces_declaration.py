#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video d'archive
"Comment remplir sa liasse fiscale LMNP etape par etape" (1jBnvyCvSA0).

Angle produit FORCE (regle 14 : video hors theme conciergerie pure, on produit
quand meme les deux, en forcant l'angle). Ici : la liste de pieces que Sebastien
enumere dans la video est exactement ce qu'une conciergerie doit pouvoir sortir
pour ses proprietaires en avril. L'outil ne fait PAS la comptabilite : il garde
les traces qui la rendent possible.

⛔ NE JAMAIS pretendre que Guestlucky remplit la liasse, calcule un amortissement
ou remplace un expert comptable. La slide 7 le dit noir sur blanc.
Fonctions citees, toutes deja etablies : encaissements et reservations par
logement, factures proprietaires, factures prestataires, documents classes par
logement, rapports mensuels horodates et archives, historique des echanges,
interface proprietaire.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_traces_declaration.py && python3 render.py v2_gl_traces_declaration
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_traces_declaration"

d = Deck("guestlucky")
d.set_bg_photo("gl_traces_declaration_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Justificatifs",
        'En avril, ton propriétaire<br>' + acc("te demande tout"),
        "Et il le demande pour l'année entière, logement par logement."),

    d.compare(1, "Deux conciergeries<br>au mois d'avril", "Le même parc, deux semaines d'écart",
              {"head": "Celle qui cherche", "items": [
                  "Elle remonte douze mois de boîte mail",
                  "Elle recompte les commissions à la main",
                  "Elle ne retrouve plus la facture de l'artisan",
                  "Elle rend un tableau que personne ne peut vérifier"]},
              {"head": "Celle qui exporte", "items": [
                  "Ses encaissements sont déjà rangés par logement",
                  "Ses factures de gestion sont émises et datées",
                  "Les documents du bien sont au même endroit",
                  "Elle rend des pièces, pas une reconstitution"]},
              "Ce qui se joue", "Ton propriétaire ne juge pas ta bonne volonté. Il juge le délai et la précision.",
              lead="La même demande arrive aux deux. Une seule y répond dans la journée."),

    d.checklist(2, "Ce qu'on va<br>te réclamer", "La liste, telle quelle",
                [(True, "Les encaissements de l'année, logement par logement",
                  "Loyers, charges récupérables, ménage. Et les dépôts de garantie encaissés, même restitués."),
                 (True, "Les commissions prélevées par les plateformes",
                  "Le chiffre d'affaires affiché est brut : ce qui a été retenu se déduit, encore faut-il le retrouver."),
                 (True, "Tes propres factures de gestion",
                  "Les honoraires de conciergerie sont une charge pour ton propriétaire. Il lui faut la facture, pas un montant."),
                 (True, "Les factures des prestataires et des travaux",
                  "Entretien, réparations, interventions : chacune rattachée au bon logement et à la bonne date.")],
                "Le détail qui coince", "Un justificatif sans date ni logement rattaché ne sert à rien au moment de déclarer.",
                lead="Quatre familles de pièces, et elles se perdent toutes de la même façon."),

    d.flow(3, "Comment le dossier<br>se remplit tout seul", "Au fil de l'eau",
           [("À chaque réservation",
             "L'encaissement est rattaché au logement, avec sa date et ce que la plateforme a retenu."),
            ("À chaque intervention",
             "La facture du prestataire rejoint le bon logement au lieu de finir dans une conversation."),
            ("À chaque fin de mois",
             "Le rapport est horodaté et archivé : il reste consultable des mois plus tard, tel quel.")],
           "Le principe", "Rien à reconstituer en avril, parce que rien n'a été laissé de côté en janvier.",
           lead="Le travail d'avril, c'est douze mois de petits gestes ou trois semaines de fouille."),

    d.layers(4, "Trois niveaux<br>de trace", "Ce qu'un dossier complet contient",
             [("Niveau 1", "Ce qui est entré",
               "Les encaissements par logement et par date, avec ce que les plateformes ont prélevé."),
              ("Niveau 2", "Ce qui est sorti",
               "Les factures propriétaires et prestataires, rattachées au bon bien et au bon mois."),
              ("Niveau 3", "Ce qui le prouve",
               "Des rapports mensuels datés et archivés, et les documents du logement au même endroit.")],
             "Ce qui manque presque toujours", "Le troisième. Les deux premiers se retrouvent, le troisième se perd.",
             lead="Les deux premiers niveaux font un tableau. Le troisième en fait un dossier."),

    d.pincer(5, "Deux moments<br>où ça se joue", "Et ils sont très éloignés",
             ("Au printemps", "Ton propriétaire prépare sa déclaration et te demande l'année entière, d'un coup."),
             ("Six ans plus tard", "En cas de contrôle, l'administration peut réclamer les justificatifs de cette même année."),
             ("Les deux tapent au même endroit", "Ce que tu as conservé, daté et rattaché au bon logement. Rien d'autre."),
             "L'écart", "Six ans, c'est très long pour une pièce jointe restée dans une conversation.",
             lead="Le premier est prévisible. Le second ne prévient pas."),

    d.mindmap(6, "Ce que l'outil<br>garde pour toi", "Logement par logement",
              "Sortir les pièces,<br>pas les<br>reconstituer",
              [("Les encaissements", "Rattachés au logement et à la réservation qui les a produits."),
               ("Les factures", "Celles que tu émets pour tes propriétaires, celles que tes prestataires t'envoient."),
               ("Les documents du bien", "Classés au même endroit, retrouvables sans fouiller trois boîtes mail."),
               ("L'interface propriétaire", "Il consulte lui-même, au lieu de te relancer trois fois en avril.")],
              "Le résultat", "Tu réponds en montrant. C'est beaucoup plus court.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées au bon endroit."),

    d.stats(7, "Les repères<br>du printemps", "À garder en tête",
            [("5 mai 2026", "La date limite de la liasse, pour les revenus 2025"),
             ("6 ans", "La durée de conservation des justificatifs"),
             ("10 ans", "La durée de report d'un déficit en meublé non professionnel"),
             ("15 000 €", "Le seuil de recettes qui bascule un meublé non classé au régime réel")],
            "À dire clairement", "Guestlucky garde les traces. Il ne fait ni la comptabilité, ni la déclaration : ça reste le métier d'un professionnel du chiffre.",
            lead="Quatre repères issus de la vidéo de Sébastien, à vérifier pour ta situation."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Tu sortirais l\'année entière<br>en ' + acc("combien de temps") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post pour le retrouver en avril, et découvre le suivi par logement sur le site.",
        "Le meilleur moment pour ranger une facture, c'est le jour où elle arrive."),

    d.closing("L'outil qui garde la trace, pour que tu puisses "
              + "<em>répondre en une journée</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
