#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 13 — video du dimanche 13/09/2026 : « Les 5 erreurs qui declenchent un
controle fiscal pour les hotes Airbnb » (ID YouTube h0fE0L6d5QI).

⚠️ PREMIERE FOURNEE SOUS LA REGLE DE MARTIN DU 10/09/2026 :
    « Tout le temps des choses differentes. Si tu fais moins de storie c'est
      pas grave mais je veux des choses differentes. »
Donc : 13 stories au lieu des 22-27 des dernieres fournees. Trois sequences
courtes (5 / 4 / 4), trois formes DIFFERENTES, 13 fonds tous NEUFS (generes le
14/09), et deux gabarits qu'on n'utilisait presque jamais : p_formula et p_vs.

⚠️ GROS TRAVAIL D'ELAGAGE — la video recoupe TROIS fournees deja sorties.
Sebastien le dit lui-meme : « cette semaine je t'ai fait deja une video ou je
te parlais des trois signes ». ECARTE, parce que deja traite :
    - le terrain non amortissable et l'amortissement par composant -> banque-06 ;
    - les formulaires 2031 / 2033 / 2042-C-PRO -> banque-06 ;
    - le rapport du 8 juillet sur le plafonnement des amortissements -> banque-04 ;
    - la residence principale et la fiche d'occupation -> banque-12 (jeudi dernier).
Il ne reste donc QUE du neuf, et c'est tres bien ainsi :
    AO — la DAC7 : le fisc a les chiffres avant toi (5 stories, jeudi) ;
    AP — le seuil de 23 000 € et la vague URSSAF 2026 (4, vendredi) ;
    AQ — les petites taxes qui ouvrent un controle (4, reserve).

⚠️ Contenu 100 % issu de la transcription. Sujet sensible : ces stories
INFORMENT sur un risque et poussent a declarer juste. Aucune n'explique comment
passer entre les mailles, et aucune ne promet un resultat.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : le logiciel de declaration cite six
fois dans la video est ECARTE, comme tous les outils maison.

Rendu : python3 render_stories.py banque-13
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         p_duo, p_vs, p_formula, acc, write_lot, accroche)

# ⚠️ VARIETE : les bas de couverture tournent avec le numero du lot.
NUM_LOT = 13

# Les apostrophes ne passent pas dans une expression de f-string.
AVANT_TOI = acc("avant toi")
BRUT = acc("brut")
COPIE = acc("copie exacte")
PILE = acc("tomber pile")
QUESTIONNAIRE = acc("questionnaire")
BRUTES = acc("recettes brutes")
BENEFICE = acc("bénéfice")
PAS_LMP = acc("pas le statut")
PORTE = acc("porte d'entrée")
SIX_ANS = acc("six ans")
TOI_MEME = acc("toi-même")

SEQUENCES = {

# ============================================================================
# SEQUENCE AO — La DAC7 (jeudi, 5 stories)
# Forme : cover > p_bigstat > p_steps > p_duo > fin
# ============================================================================
"AO_le_fisc_a_tes_chiffres": [
    cover("bg_bureau_papiers", "ce que presque personne sait",
          f'Le fisc a tes chiffres Airbnb {AVANT_TOI}.',
          sub="Il ne te surveille pas : il n'en a pas besoin. Les plateformes "
              "les lui envoient toutes seules, chaque mois de janvier.",
          hand_bottom=accroche(NUM_LOT + 1)),

    p_bigstat("bg_fenetre_pluie", "les chiffres de 2025",
              "C'est une machine qui choisit les dossiers",
              "54 %", "des dossiers de particuliers orientés vers un contrôle "
                      "l'ont été par l'intelligence artificielle",
              ["Elle croise ta déclaration, les données transmises par les "
               "plateformes, tes relevés bancaires et tes années précédentes.",
               "Le seuil de transmission est bas : 2 000 € ou 30 transactions "
               "dans l'année, et c'est automatique.",
               "Airbnb, Booking, Abritel, Leboncoin : toutes sont concernées."],
              numsize=160),

    p_steps("bg_cafe_table", "le mail de janvier",
            "Ce que ton « rapport annuel » contient vraiment",
            [("Ce n'est pas un récapitulatif pour toi",
              f'C\'est la {COPIE} de ce qui part à l\'administration. Le même '
              f'document, au même moment.'),
             ("Tout y est",
              "Ton identité, ton adresse, ton numéro fiscal, ton IBAN, le "
              "montant total versé, le nombre de transactions, les "
              "commissions retenues, l'adresse du bien."),
             ("La règle est devenue simple",
              f'En janvier, additionne le rapport de CHAQUE plateforme. Ce '
              f'total doit {PILE} dans ta déclaration.')]),

    p_duo("bg_etagere", "quatre façons de créer un écart sans le vouloir",
          "Et l'écart, c'est ce que la machine cherche",
          "Ce qui te fait déclarer trop peu",
          [f'Déclarer ce qui est arrivé sur ton compte au lieu du montant '
           f'{BRUT}, avant commission.',
           "Oublier la plateforme secondaire où tu n'as fait que deux "
           "réservations dans l'année.",
           "Se dire « c'est trop petit pour compter ». Le seuil est à 2 000 €."],
          "Ce qui te fait déclarer trop",
          ["Ajouter la taxe de séjour au chiffre d'affaires.",
           "Ajouter les cautions encaissées.",
           "Ni l'une ni l'autre n'est un revenu : là, tu paies de l'impôt "
           "pour rien."]),

    fin("bg_ruelle", "Un écart vérifié finit en redressement.",
        "ce n'est plus un contrôle au hasard, c'est une comparaison automatique entre deux chiffres"),
],

# ============================================================================
# SEQUENCE AP — Le seuil de 23 000 € (vendredi, 4 stories)
# Forme : cover > p_formula > p_timeline > fin
# ============================================================================
"AP_seuil_23000_urssaf": [
    cover("bg_couloir_hotel", "l'actualité de 2026 dont on parle peu",
          "L'URSSAF écrit aux loueurs qui ont dépassé 23 000 €.",
          sub="Une campagne de régularisation, bâtie sur les chiffres que les "
              "plateformes ont transmis pour 2024 et 2025.",
          hand_bottom=accroche(NUM_LOT + 5)),

    p_formula("bg_chambre_lumiere", "le mécanisme, en une ligne",
              "Ce qui se déclenche au-delà du seuil",
              f'Plus de 23 000 € de {BRUTES} en meublé de tourisme',
              f'cotisations calculées sur ton {BENEFICE}',
              "35 à 45 %",
              "Ce ne sont pas les prélèvements sociaux : ce sont les "
              "cotisations d'indépendant. Et il existe un minimum forfaitaire "
              "d'environ 1 200 € par an, même avec un bénéfice à zéro."),

    p_timeline("bg_port", "comment ça arrive concrètement",
               "Le courrier, puis la suite",
               [("Tu reçois un questionnaire",
                 "Il part aux loueurs repérés par les données des "
                 "plateformes. Le seuil porte sur les recettes brutes, pas "
                 "sur ce que tu as gagné.", None),
                ("Le rattrapage peut remonter",
                 "Jusqu'à trois années en arrière, majorations comprises.",
                 None),
                ("Ne confonds pas les deux seuils",
                 f'Les 23 000 € déclenchent les cotisations, {PAS_LMP} de '
                 f'loueur professionnel. Celui-ci exige en plus que tes '
                 f'recettes dépassent les autres revenus du foyer : on peut '
                 f'cotiser en restant non professionnel.', None)]),

    fin("bg_balcon", "Deux mécanismes, deux seuils, deux courriers.",
        "les confondre coûte cher, et le questionnaire arrive sans prévenir"),
],

# ============================================================================
# SEQUENCE AQ — Les petites taxes (reserve, 4 stories)
# Forme : cover > p_vs > p_steps > fin
# ============================================================================
"AQ_petites_taxes_gros_signaux": [
    cover("bg_escalier_bois", "le détail qui ouvre la porte",
          f'Une petite taxe oubliée est une {PORTE}.',
          sub="Ce n'est pas son montant qui compte. C'est ce qu'elle raconte "
              "de ton dossier à celui qui le lit.",
          hand_bottom=accroche(NUM_LOT + 9)),

    p_vs("bg_toits_pluie", "deux dossiers, même chiffre d'affaires",
         "Ce que l'inspecteur en déduit",
         "Le dossier bancal",
         ["La CFE n'a pas été payée.",
          "La taxe de séjour n'a pas été reversée.",
          "Il se dit que le reste doit être approximatif aussi."],
         "Le dossier propre",
         ["La CFE est due même en micro, même pour un seul bien.",
          "Elle tombe en décembre : ce n'est pas une erreur.",
          "La taxe de séjour, Airbnb la collecte ; en direct ou ailleurs, "
          "c'est à toi de le faire."],
         "Une petite taxe ne coûte presque rien. Ce qu'elle déclenche, si."),

    p_steps("bg_table_bois", "les justificatifs",
            "Ce que tu ne peux pas prouver, tu ne peux pas déduire",
            [("Le fisc a trois ans, mais regarde plus loin",
              f'Il peut revenir sur une déclaration pendant trois ans, et '
              f'réclamer des justificatifs sur les {SIX_ANS} précédentes.'),
             ("Ce qui saute au premier contrôle",
              "Le ménage payé en liquide, les travaux arrangés sans facture, "
              "l'assurance dont tu n'as pas l'attestation."),
             ("Et la charge que beaucoup oublient",
              "La commission de la plateforme est déductible au régime réel. "
              "Les factures sont téléchargeables depuis ton compte hôte : ne "
              "la calcule pas de tête.")]),

    fin("bg_mur_beton", f'Régulariser {TOI_MEME} coûte 10 %.',
        "si c'est le contrôle qui trouve, la majoration monte de 40 à 80 %, sur trois ans"),
],

}

SLUG = "banque-13"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
