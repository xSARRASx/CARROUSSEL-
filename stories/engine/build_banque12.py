#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 12 — video du mercredi 09/09/2026 : « Le fisc vous surveille : les 3
signes qui alertent sur votre residence » (ID YouTube lc1huihoLio).

⚠️ RECOUVREMENT AVEC BANQUE-08 (taxe fonciere, h0GZh51rtCk, traitee le 27/08).
Sebastien renvoie lui-meme a cette video dans celle-ci. Toute la partie
« verifier et contester sa taxe fonciere » (surface ponderee, categorie de
confort, dependances, valeur locative cadastrale, les 5 erreurs, la
reclamation) est donc DELIBEREMENT ECARTEE : elle est deja sortie.
Ce qui est neuf, et qui seul justifie la fournee :
    - trois decisions de justice datees (9 juillet 2025, Marseille 29 janvier
      2026, Bordeaux fin 2025) ;
    - la majoration de 40 % pour manquement delibere, une nouveaute ;
    - le delai « normal » d'un an entre le depart et la vente ;
    - l'exoneration qui s'apprecie separement pour chaque vendeur en cas de
      divorce ;
    - la fiche d'occupation « Gerer mes biens immobiliers », jamais traitee ;
    - les trois ans de controle supplementaires sur les residences secondaires
      et l'obligation 2026 des occupants non proprietaires.

    AL — comment le fisc prouve que tu n'y vivais pas (6 stories, lundi) ;
    AM — la fiche que l'administration tient sur ton bien (5, mardi) ;
    AN — le calendrier de la vente (6, reserve).

⚠️ TAILLES IMPOSEES PAR LA GRILLE : 6 stories le lundi, 5 le mardi.

⚠️ TON. Le sujet est la fraude a la residence principale. Ces stories
INFORMENT sur un risque et invitent a verifier sa propre fiche ; elles ne
donnent AUCUN moyen de passer entre les mailles. Sebastien n'est ni avocat ni
fiscaliste et le dit : aucune story ne promet un resultat, et les decisions de
justice sont citees comme telles, avec leur date.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : le site de verification cite en
fin de video est ECARTE, comme tous les outils maison.

Rendu : python3 render_stories.py banque-12
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         p_duo, p_vs, acc, write_lot)

# Les apostrophes ne passent pas dans une expression de f-string.
TA_VIE = acc("ta vie")
ELECTRICITE = acc("électricité")
DECLAREE = acc("déclarée")
MISE_EN_SCENE = acc("mise en scène")
DELIBERE = acc("délibéré")
FAISCEAU = acc("faisceau d'indices")
FICHE = acc("fiche")
DECIDE = acc("décide")
DEUX_SENS = acc("dans les deux sens")
CAPTURES = acc("captures d'écran")
RESSERRE = acc("se resserre")
DECISION = acc("décision fiscale")
SEPAREMENT = acc("séparément")
TOLERANCES = acc("tolérances")
UN_AN = acc("un an")
CINQ_ANS = acc("cinq ans")
VENT = acc("d'où souffle le vent")

SEQUENCES = {

# ============================================================================
# SEQUENCE AL — Comment le fisc prouve (lundi, 6 stories)
# ============================================================================
"AL_fisc_traque_residence": [
    cover("bg_documents", "trois décisions de justice, 2025 et 2026",
          f'Le fisc ne regarde plus tes papiers. Il regarde {TA_VIE}.',
          sub="Revendre sa résidence principale échappe à l'impôt sur la "
              "plus-value. Encore faut-il prouver qu'on y vivait.",
          hand_bottom="les trois affaires, juste après"),

    p_timeline("bg_facade_pierre", "un studio de 13 m² à Paris",
               "Jugé le 9 juillet 2025",
               [("Le dossier paraissait béton",
                 "Déclaration de revenus à l'adresse, courriers de "
                 "l'administration, relevés bancaires, appels de charges. "
                 "Sur le papier, tout collait.", None),
                ("Le fisc a regardé derrière",
                 "Un crédit renouvelable, un compte inactif, un livret : "
                 "aucun mouvement. Les comptes ne racontaient aucune vie.",
                 None),
                (f'Les factures d\'{ELECTRICITE} ont tranché',
                 "La consommation d'une année entière était inférieure à "
                 "celle d'un simple réfrigérateur. Exonération refusée, "
                 "confirmée en appel.", None)]),

    focus("bg_boites_lettres", "le raisonnement qui tombe à plat",
          f'Ton courrier arrive à l\'adresse que tu as {DECLAREE}.',
          "C'est tout le problème : tu déclares une adresse, tu y reçois donc "
          "du courrier, et tu voudrais que ce courrier prouve que tu y "
          "habites. Le raisonnement tourne en rond, et l'administration ne "
          "s'y laisse plus prendre."),

    p_steps("bg_hall_immeuble", "cour administrative d'appel de Marseille",
            "Le portrait-robot du 29 janvier 2026",
            [("Un retour au dernier moment",
              "Le propriétaire revient habiter son bien et change sa "
              "domiciliation alors que la vente est déjà engagée."),
             ("Une autre résidence restée disponible",
              "Le logement d'à côté n'a jamais cessé d'être habitable. Le "
              "juge regarde le tableau entier, pas une case."),
             ("Des meubles sommaires, aucune vie familiale",
              "Le strict minimum, une consommation d'énergie dérisoire, "
              "aucune trace du quotidien dans les lieux.")]),

    p_bigstat("bg_bureau_matin", "la nouveauté qui change tout",
              f'Une {MISE_EN_SCENE} coûte désormais plus cher',
              "+40 %", f'de majoration pour manquement {DELIBERE}',
              ["Sur 100 000 € de plus-value taxable, l'impôt et les "
               "prélèvements sociaux représentent déjà 36 000 €.",
               "La majoration vient s'ajouter par-dessus.",
               "Le juge a estimé que le propriétaire ne pouvait pas ignorer "
               "que ce logement n'était pas sa résidence principale."],
              numsize=150),

    fin("bg_escalier", f'Aucun seuil légal n\'existe : c\'est un {FAISCEAU}.',
        "la loi ne fixe ni durée minimale d'occupation ni niveau de consommation, tout se juge ensemble"),
],

# ============================================================================
# SEQUENCE AM — La fiche d'occupation (mardi, 5 stories)
# ============================================================================
"AM_fiche_occupation": [
    cover("bg_salon_vide", "elle existe depuis 2023",
          f'Il y a une {FICHE} sur chacun de tes biens. Tu ne l\'as jamais lue.',
          sub="C'est elle qui décide de ce que tu paies, et c'est elle que le "
              "fisc regardera le jour où tu vendras.",
          hand_bottom="ce qu'il y a dedans, juste après"),

    focus("bg_cour", "sur ton espace impots.gouv",
          f'« Gérer mes biens immobiliers » {DECIDE} de tout.',
          "Pour chaque bien, l'administration note qui l'occupe et à quel "
          "titre : résidence principale, secondaire, location ou logement "
          "vacant. Elle note aussi depuis quand. C'est de là que partent tes "
          "avis de taxe foncière et de taxe d'habitation."),

    p_duo("bg_ville_doree", "une fiche fausse fait mal",
          f'Et elle se trompe {DEUX_SENS}',
          "Fausse en ta défaveur",
          ["Un logement noté secondaire alors que c'est ta principale.",
           "Une surface erronée, une dépendance comptée à tort.",
           "Tu paies trop, chaque année, en silence."],
          "Fausse en ta faveur",
          ["Tout va bien jusqu'au jour de la vente.",
           "Là, c'est le contrôle et le redressement.",
           "Avec la majoration de 40 % au bout."]),

    p_steps("bg_immeuble_dore", "ce qui se fait en vingt minutes",
            "Trois étapes, dans cet ordre",
            [("Ouvre ta fiche et fige-la",
              f'Connecte-toi, lis chaque ligne : nature d\'occupation, '
              f'occupants, dates. Prends des {CAPTURES} : si tu contestes un '
              f'jour, tu seras content de les avoir.'),
             ("Compare avec la réalité",
              "Certaines données sont figées depuis les années 1970 et se "
              "transmettent d'un propriétaire à l'autre. Une anomalie se "
              "paie tous les ans."),
             ("Agis avant la date limite",
              "Pour un dégrèvement sur la taxe foncière 2026, tu as jusqu'au "
              "31 décembre 2027. Après, c'est perdu même si tu avais "
              "raison, et rien n'est rétroactif.")]),

    fin("bg_montagne", f'Le filet {RESSERRE}.',
        "trois ans de contrôle en plus sur les secondaires, et depuis 2026 même les occupants non propriétaires déclarent"),
],

# ============================================================================
# SEQUENCE AN — Le calendrier de la vente (reserve, 6 stories)
# ============================================================================
"AN_calendrier_de_la_vente": [
    cover("bg_chemin_aube", "le détail que personne ne calcule",
          f'Quand tu vends est une {DECISION} avant d\'être une décision immobilière.',
          sub="Quelques mois d'écart peuvent valoir des dizaines de milliers "
              "d'euros. Voilà les trois moments qui comptent.",
          hand_bottom="les trois, juste après"),

    p_vs("bg_salon_cosy", "un couple se sépare, l'un part, l'autre reste",
         "Deux ans plus tard, ils vendent",
         "Celui qui est parti",
         ["Il n'habitait plus les lieux au jour de la vente.",
          "Sa moitié de plus-value est taxée."],
         "Celui qui est resté",
         ["Il y vivait encore au moment de vendre.",
          "Sa moitié est exonérée."],
         f'L\'exonération s\'apprécie {SEPAREMENT} pour chaque vendeur. Même '
         f'maison, même acte notarié, deux traitements fiscaux opposés.'),

    focus("bg_village", "ce qu'il faut en retenir si tu te sépares",
          f'Il existe des {TOLERANCES}, mais elles tiennent au délai.',
          "Quand la vente intervient dans un délai raisonnable après la "
          "séparation, la situation s'apprécie autrement. Autrement dit, dans "
          "une séparation avec un bien à vendre, le moment où l'on signe "
          "n'est pas un détail d'organisation."),

    focus("bg_cles", "cour administrative d'appel de Bordeaux, fin 2025",
          f'Après le départ, le délai « normal » tourne autour d\'{UN_AN}.',
          "Tu as le droit de déménager avant de vendre : personne n'exige que "
          "tu restes jusqu'à la signature. Mais un bien resté inoccupé "
          "dix-sept mois avant la vente a fait perdre l'exonération. Au-delà "
          "du délai normal, elle s'évapore."),

    focus("bg_terrasse", "et ce qui se prépare pour la suite",
          f'Un amendement propose {CINQ_ANS} de détention minimum.',
          "Il a été déposé au budget 2026, avec des exceptions prévues pour "
          "les mutations, les divorces et les décès. Ce n'est pas voté, et "
          "ça peut disparaître. Mais c'est la deuxième fois qu'on en entend "
          "parler."),

    fin("bg_lac", f'Aujourd\'hui, aucune durée minimale n\'existe. Regarde {VENT}.',
        "rien n'oblige à habiter six mois ou un an, mais la tendance ne va pas vers plus de souplesse"),
],

}

SLUG = "banque-12"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
