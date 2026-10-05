#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Budget 2027 : la fin du regime reel ?" (05/10/2026, bysfkU90VQI).

Angle produit : CONNAITRE SON CHIFFRE LOGEMENT PAR LOGEMENT. Le pont est dit mot
pour mot par Sebastien dans la video : "si vous louez en courte duree, c'est le
moment de connaitre votre chiffre logement par logement", et il renvoie a
l'outil juste apres. Le plafond envisage pour les meubles de tourisme etant par
FOYER et non par bien, le detail par logement devient la seule base de calcul
utilisable.

Fonctions citees, toutes issues de la banque produit (section A2) :
  - Channel Manager natif : les reservations des plateformes au meme endroit
  - Dashboard et KPIs par logement
  - Documents classes par logement, rapports horodates et archives
  - Interface proprietaire
⛔ NE RIEN INVENTER. L'outil ne calcule PAS l'amortissement, ne fait PAS la
liasse et ne dit PAS quel regime choisir. Il donne les recettes et les charges,
bien par bien. C'est ecrit noir sur blanc sur une slide et dans la legende.

⚠️ VOCABULAIRE HOGUET : ni "gerer" ni "gestion". On ecrit SUIVI, PILOTAGE,
EXPLOITATION.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

⛔ Meme prudence que le carrousel LSL : RIEN N'EST VOTE, c'est l'article 7 d'un
projet de loi depose le 1er octobre. Ne jamais l'ecrire autrement.

Theme CLAIR, couverture cover_citation (phrase reellement prononcee), scene
"plexi_rose" (regle 18 : GL etait en sombre avec cover_trois le 28/09).

Usage : python3 v2_gl_chiffre_par_logement.py && python3 render.py v2_gl_chiffre_par_logement
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_gl_chiffre_par_logement"

d = Deck("guestlucky", "clair")
d.set_bg_photo("gl_chiffre_par_logement_bg.jpg", veil=0.80)

SLIDES = [
    d.cover_citation(
        "C'est le moment de connaître<br>votre chiffre " + acc("logement par logement"),
        "Sébastien More",
        "à propos de l'article 7 du projet de loi de finances 2027"),

    d.compare(1, "Le total du parc<br>ne dit plus rien", "Ce que change un plafond par foyer",
              {"head": "Suivi en bloc", "items": [
                  "Un chiffre d'affaires global pour tout le parc",
                  "Des charges mélangées, réparties au jugé en fin d'année",
                  "Les commissions de plateformes noyées dans la masse",
                  "Impossible de dire ce que rapporte VRAIMENT un logement donné"]},
              {"head": "Suivi bien par bien", "items": [
                  "Les recettes de chaque logement, plateforme par plateforme",
                  "Les charges rattachées au bien qui les a générées",
                  "Ménage, énergie, commissions : identifiables ligne par ligne",
                  "Un chiffre par logement, disponible sans reconstitution"]},
              "Pourquoi maintenant", "Le plafond envisagé s'applique par foyer fiscal, pas par bien. Pour savoir où tu te situes, il faut additionner des chiffres fiables.",
              lead="Tant que l'amortissement suivait la valeur du bien, le détail par logement était confortable. Il devient nécessaire."),

    d.stats(2, "Pourquoi la courte<br>durée est la plus<br>exposée", "Les chiffres du texte déposé",
            [("1,5&nbsp;%", "Le taux envisagé pour les meublés de tourisme, contre 2,5&nbsp;% ailleurs"),
             ("5 000 €", "Le plafond annuel par foyer fiscal, contre 7 000 € ailleurs"),
             ("+ 1 652 €", "Le surcoût annuel calculé sur UN seul meublé de tourisme"),
             ("Classé ou non", "Dans sa rédaction actuelle, le texte ne fait aucune différence entre les deux")],
            "À dire clairement", "Rien n'est voté : l'article 7 a été déposé le 1er octobre et entre en débat. Ces chiffres sont ceux du texte présenté.",
            lead="Deux plafonds différents, et c'est la courte durée qui prend le taux le plus bas."),

    d.mindmap(3, "Ce qu'il faut<br>savoir par<br>logement", "Les quatre lignes du calcul",
              "SANS<br>RECONSTITUER<br>EN AVRIL",
              [("Les recettes encaissées", "Toutes plateformes confondues, et la réservation directe avec elles."),
               ("Les commissions", "Ce que prennent les plateformes, rattaché au séjour et au logement concerné."),
               ("Les charges d'exploitation", "Ménage, énergie, consommables : ce qui sort réellement pour CE bien."),
               ("Le résultat avant amortissement", "C'est sur lui que se calcule tout le reste, et c'est lui que tu dois connaître bien par bien.")],
              "La limite", "L'outil donne ces quatre lignes. Il ne calcule pas ton amortissement et ne dit pas quel régime choisir.",
              lead="Quatre lignes par logement, qui existent déjà dans ton exploitation mais rarement au même endroit."),

    d.flow(4, "Comment ce chiffre<br>se construit", "Toute l'année, pas en avril",
           [("Les réservations arrivent au même endroit",
             "Le channel manager natif consolide Airbnb, Booking et Abritel, chaque réservation rattachée à son logement."),
            ("Les indicateurs se lisent par bien",
             "Le tableau de bord suit le parc logement par logement, pas en un seul total indifférencié."),
            ("Les pièces restent attachées",
             "Documents classés par logement et rapports horodatés : ce qui justifie le chiffre reste à côté du chiffre.")],
           "Le principe", "Un chiffre qu'on reconstitue au printemps est une estimation. Un chiffre enregistré au fil de l'eau est une donnée.",
           lead="Trois mécanismes, et aucun ne demande de travail supplémentaire au moment de la déclaration."),

    d.layers(5, "Trois étages<br>d'un parc<br>lisible", "De la recette à la restitution",
             [("Étage 1", "Les recettes",
               "Ce qui a été réservé, sur quelle plateforme, pour quel logement, sur quelles nuits."),
              ("Étage 2", "Les charges",
               "Ménage planifié, interventions tracées par l'application prestataires, consommables : rattachés au bien."),
              ("Étage 3", "La restitution",
               "Dashboard, indicateurs par logement, interface propriétaire : chacun consulte au lieu de réclamer.")],
             "Ce qui manque le plus souvent", "Le deuxième étage. Sans charges rattachées au bon logement, le chiffre par logement reste faux.",
             lead="Les trois existent déjà séparément chez la plupart des conciergeries. Le sujet, c'est de les tenir ensemble."),

    d.pincer(6, "Les deux pièges<br>du printemps", "Et ils se préparent maintenant",
             ("Le total qui cache tout", "Un parc rentable en moyenne peut contenir un logement qui ne l'est plus du tout. La moyenne ne se déclare pas."),
             ("La reconstitution d'avril", "Trois extranets, deux boîtes mail et des captures d'écran : c'est long, et c'est là que les erreurs entrent."),
             ("Ce qui protège", "Des chiffres enregistrés au moment où ils se produisent, rattachés au bon logement."),
             "Le calendrier", "Les débats sur la partie recettes se tiennent à partir du 12 octobre, l'adoption est espérée mi-décembre.",
             lead="Les deux se ressemblent : elles supposent qu'on fera le tri plus tard."),

    d.checklist(7, "Ce qui se prépare<br>d'ici le printemps", "Sans rien décider dans l'urgence",
                [(True, "Connaître le chiffre de chaque logement",
                  "Recettes, commissions, charges, résultat avant amortissement : c'est la base de n'importe quel calcul."),
                 (True, "Rattacher les charges au bon bien",
                  "Une charge mal affectée fausse deux logements à la fois : celui qui la porte et celui qui ne la porte plus."),
                 (False, "Ne rien changer dans la précipitation",
                  "Changer de régime ou monter une société maintenant, c'est décider sans connaître le texte final."),
                 (False, "Ne pas confondre suivi et fiscalité",
                  "Le suivi donne les chiffres. Le calcul d'impôt reste l'affaire du propriétaire et de son comptable.")],
                "L'honnêteté", "Rien n'est voté. Ce qui est décrit ici, c'est un texte déposé le 1er octobre et un calendrier parlementaire.",
                lead="Quatre gestes qui ne dépendent d'aucun vote, et qui serviront quel que soit le texte final."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Sais-tu ce que rapporte<br>' + acc("chaque") + ' logement de ton parc ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le suivi logement par logement sur le site.",
        "Un chiffre enregistré au fil de l'eau vaut mieux qu'une reconstitution au printemps."),

    d.closing("Le parc se pilote au détail, "
              + "<em>plus à la moyenne</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_citation")
    noter_theme("guestlucky", "clair")
