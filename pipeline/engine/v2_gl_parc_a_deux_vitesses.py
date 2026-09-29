#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"LMNP 2027 : ce que le gouvernement prepare" (28/09/2026, U6vGmP7QX1k).

Angle produit : UN PARC OU CHAQUE LOGEMENT N'A PLUS LE MEME STATUT. La lettre du
23 septembre ne vise pas la France entiere : elle vise la courte duree
touristique dans les zones tendues. Classe ou non, zone tendue ou non, courte ou
longue duree : trois questions qui se posent desormais logement par logement.
Le pont est cite par Sebastien lui-meme, qui renvoie a l'outil pour ceux qui
pilotent des biens en courte duree.

Fonctions citees, toutes issues de la banque produit (section A2) :
  - Channel Manager natif, dashboard et KPIs
  - Documents classes par logement, historique des echanges, rapports archives
  - Planning menages + application mobile prestataires, equipes illimitees
  - Interface proprietaire
  - Module Market Intelligence (etude de marche courte duree ET longue duree)
⛔ NE RIEN INVENTER. L'outil ne fait ni la fiscalite, ni le classement, ni
l'enregistrement en mairie : il tient les informations et les preuves.

⚠️ VOCABULAIRE HOGUET : la video dit "logiciel de gestion de vos equipes". Nous
ecrivons PILOTAGE, COORDINATION, EXPLOITATION. Jamais "gerer" ni "gestion".

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

⛔ Meme prudence que le carrousel LSL : la lettre est un document politique, pas
un texte de loi ; rien n'est vote pour 2027.

Theme SOMBRE, couverture cover_trois, scene "velours_macro"
(regle 18 : la semaine derniere GL etait en clair avec cover_cadre).

Usage : python3 v2_gl_parc_a_deux_vitesses.py && python3 render.py v2_gl_parc_a_deux_vitesses
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_gl_parc_a_deux_vitesses"

d = Deck("guestlucky", "sombre")
d.set_bg_photo("gl_parc_a_deux_vitesses_bg.jpg", veil=0.84)

SLIDES = [
    d.cover_trois(
        "Guestlucky · Parc à deux vitesses",
        [("Classé ou pas", "Le plafond passe de 15 000 € à près de 78 000 €, l'abattement de 30 à 50&nbsp;%."),
         ("Zone tendue ou pas", "La lettre du 23 septembre ne vise que les centres-villes en zone tendue."),
         ("Courte ou longue durée", "C'est l'écart entre les deux que l'État dit vouloir réduire.")]),

    d.compare(1, "Un parc en bloc,<br>ou logement<br>par logement", "Ce que la lettre change pour une conciergerie",
              {"head": "Traité en bloc", "items": [
                  "Tous les biens sont supposés avoir le même régime",
                  "Le classement, on verra plus tard",
                  "La zone tendue, personne ne l'a vérifiée",
                  "Le propriétaire appelle en décembre pour savoir où il en est"]},
              {"head": "Traité bien par bien", "items": [
                  "Chaque logement a son statut écrit et daté",
                  "Le classement est suivi, avec sa date de fin de validité",
                  "La commune et son zonage sont connus avant l'arbitrage",
                  "Le propriétaire consulte au lieu d'appeler"]},
              "Le vrai sujet", "Un parc de dix logements peut désormais contenir quatre situations fiscales différentes.",
              lead="La lettre ne parle pas de toute la France : elle parle des centres-villes en zone tendue."),

    d.checklist(2, "Ce qui se tient<br>par logement", "Quatre informations, plus une moyenne de parc",
                [(True, "Le classement meublé de tourisme et sa validité",
                  "Une visite d'organisme agréé, quelques centaines d'euros, valable 5 ans. La date de fin se surveille comme une échéance de contrat."),
                 (True, "Le numéro d'enregistrement de la commune",
                  "Depuis mai 2026, les meublés de tourisme s'enregistrent sur la plateforme nationale. Toutes les communes n'y sont pas encore, mais ça se généralise."),
                 (True, "Le zonage de la commune",
                  "Zone tendue ou non : c'est ce qui dit si le bien est dans la cible décrite par la lettre, ou complètement à côté."),
                 (True, "Le mode d'exploitation retenu",
                  "Courte durée, longue durée meublée, ou combinaison : c'est l'arbitrage qui se rejoue bien par bien.")],
                "La règle", "Ces informations ne valent que si elles sont à jour et retrouvables. Une capture d'écran dans une boîte mail ne tient pas trois ans.",
                lead="Aucune de ces quatre lignes n'est une moyenne : elles changent d'un logement à l'autre."),

    d.mindmap(3, "Ce que l'outil<br>garde par<br>logement", "La mémoire du parc",
              "RETROUVABLE<br>DES MOIS<br>PLUS TARD",
              [("Les documents du bien", "Classés au même endroit, rattachés au logement, pas éparpillés dans trois boîtes mail."),
               ("L'historique des échanges", "La trace de ce qui s'est réellement passé, séjour par séjour."),
               ("Les rapports horodatés", "Archivés, consultables plus tard : c'est ce qui fait la différence le jour où on te demande des comptes."),
               ("L'interface propriétaire", "Il consulte ses indicateurs lui-même, au lieu de t'écrire pour savoir où en est son bien.")],
              "Ce que ça ne fait pas", "L'outil ne fait ni ta fiscalité, ni le classement, ni l'enregistrement en mairie. Il tient l'information et la preuve.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées au bon endroit."),

    d.flow(4, "L'arbitrage<br>se pose bien<br>par bien", "Courte ou longue durée",
           [("La question devient chiffrée",
             "Si l'écart fiscal entre courte et longue durée se resserre, c'est le rendement réel de CE logement qui tranche, pas une préférence générale."),
            ("L'étude compare les deux modes",
             "À partir de l'adresse et de la typologie, le module d'étude de marché donne le potentiel en courte durée et en longue durée meublée."),
            ("La décision se documente",
             "Tu gardes le rapport en face de ce que le bien a réellement fait ensuite.")],
           "La prudence", "Une étude de marché n'est pas une projection fiscale. Le calcul d'impôt reste l'affaire du propriétaire et de son comptable.",
           lead="Ce qui se décidait par habitude va devoir se décider logement par logement."),

    d.pincer(5, "Les deux erreurs<br>qui coûtent<br>en décembre", "Et elles se préparent maintenant",
             ("Traiter tout le parc pareil", "Un bien hors zone tendue et un bien en plein centre d'une métropole ne sont pas dans la même situation, et ne demandent pas les mêmes décisions."),
             ("Découvrir le sujet en décembre", "Un classement demande une visite et un délai. Il ne s'obtient pas la semaine où le texte est adopté."),
             ("Ce qui protège", "Un état du parc à jour, logement par logement, avant que les arbitrages ne se posent en urgence."),
             "Le calendrier", "Les débats se tiennent en octobre et novembre, l'adoption en décembre, l'application au 1er janvier 2027.",
             lead="Les deux se ressemblent : elles supposent qu'on aura le temps de regarder plus tard."),

    d.stats(6, "Ce que change<br>le classement", "Sur un meublé de tourisme",
            [("15 000 €", "Le plafond du micro pour un meublé de tourisme NON classé"),
             ("30&nbsp;%", "Son abattement, contre 50&nbsp;% pour un meublé classé"),
             ("78 000 €", "L'ordre de grandeur du plafond une fois le meublé classé"),
             ("5 ans", "La durée de validité du classement, après la visite d'un organisme agréé")],
            "Le calcul de Sébastien", "Sur 15 000 € de recettes, le classement représente environ 3 000 € de base imposable en moins, chaque année.",
            lead="Un meublé classé, aligné sur le régime de la longue durée, est précisément ce que la lettre ne vise pas."),

    d.layers(7, "Piloter un parc<br>à deux vitesses", "Trois étages, une seule base",
             [("Étage 1", "Les plateformes",
               "Le channel manager natif synchronise Airbnb, Booking et Abritel, logement par logement, sans ressaisie."),
              ("Étage 2", "Les équipes",
               "Planning ménages et application mobile prestataires : chacun voit ses missions, utilisateurs et équipes illimités."),
              ("Étage 3", "La restitution",
               "Dashboard et indicateurs par bien, interface propriétaire : l'état du parc se consulte au lieu de se reconstituer.")],
             "L'honnêteté", "Rien n'est voté pour 2027. Ce qui est décrit ici, c'est une lettre d'intention et un calendrier parlementaire.",
             lead="Un parc dont les logements divergent demande une base commune, pas dix tableurs."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Connais-tu le statut<br>de ' + acc("chacun") + ' de tes logements ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le pilotage du parc logement par logement sur le site.",
        "Les arbitrages se préparent en octobre, pas la semaine où le texte est adopté."),

    d.closing("Un parc, dix logements, "
              + "<em>et bientôt plusieurs régimes</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_trois")
    noter_theme("guestlucky", "sombre")
