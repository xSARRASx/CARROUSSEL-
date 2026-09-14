#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Les 5 erreurs qui declenchent un controle fiscal pour les hotes Airbnb"
(14/09/2026, h0fE0L6d5QI).

Angle coaching : les CINQ ERREURS qui font remonter un dossier LMNP dans la pile
des controles, et ce qui protege. Different du carrousel LSL du 10/09 (les
signaux sur la RESIDENCE PRINCIPALE) : ici on est cote loueur meuble, DAC7,
URSSAF, amortissement, justificatifs, petites taxes.

⛔ Prudences graves pour cette video :
  - Le plafonnement des taux d'amortissement est une RECOMMANDATION d'un rapport
    du 8 juillet 2026. Aucun taux ni aucune date n'est arrete. Le dire ainsi.
  - Ne pas nommer l'outil de declaration cite dans la video : le nom est
    incertain dans la transcription.
  - Sebastien n'est pas juriste ni fiscaliste : il relaie des regles publiques.

Couverture : cover_chiffre (les 54 % de dossiers orientes par l'IA en 2025).
Semaine derniere LSL = cover_aplat, donc rotation respectee (regle 16).

Usage : python3 v2_lsl_controle_fiscal_lmnp.py && python3 render.py v2_lsl_controle_fiscal_lmnp
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_lsl_controle_fiscal_lmnp"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_controle_fiscal_lmnp_bg.jpg", veil=0.88)

SLIDES = [
    d.cover_chiffre(
        "Le Sous Loueur · Contrôle fiscal",
        "54", "%",
        "des dossiers de particuliers ont été orientés vers un contrôle par l'IA en 2025",
        "Le fisc ne te surveille pas : il a déjà tes chiffres. Les 5 erreurs qui te font remonter dans la pile."),

    d.timeline(1, "Comment ils ont<br>déjà tes chiffres", "La directive DAC7",
               [("2023", "La directive entre en vigueur",
                 "Le 1er janvier. Les plateformes deviennent collectrices d'informations pour l'administration.", False),
                ("2024", "Les premières transmissions",
                 "Airbnb, Booking, Abritel, Leboncoin transmettent automatiquement.", False),
                ("Janvier", "Le rapport annuel part en double",
                 "Le mail « voici le rapport annuel de vos revenus » est la copie exacte de ce qu'ils reçoivent.", False),
                ("2025", "Le croisement devient automatique",
                 "2042 C Pro, fichiers DAC7, relevés bancaires et années antérieures, recoupés par l'IA.", True)],
               "Le seuil", "2 000 € encaissés ou 30 transactions dans l'année : la transmission est automatique.",
               lead="Tu n'as rien à déclencher : la transmission existe déjà depuis trois ans."),

    d.mindmap(2, "Ce que la plateforme<br>envoie avec tes chiffres", "Le contenu du fichier",
              "Le même<br>mail<br>qu'à toi",
              [("Ton identité complète", "Nom, adresse, numéro fiscal : le dossier est nominatif avant même ta déclaration."),
               ("Ton IBAN", "Le compte sur lequel les versements arrivent, donc le relevé qu'ils peuvent recouper."),
               ("Le montant total versé", "Avec le nombre de transactions et les commissions retenues par la plateforme."),
               ("L'adresse du bien", "Le logement est identifié, pas seulement le loueur.")],
              "À retenir", "Ce n'est pas un récapitulatif pour toi : c'est une copie de ce qui part à l'administration.",
              lead="Quatre informations que tu n'as jamais transmises toi-même et qu'ils ont pourtant."),

    d.checklist(3, "Erreur 1<br>L'écart entre<br>leurs chiffres et les tiens", "La plus fréquente",
                [(True, "Déclare le montant BRUT, avant la commission",
                  "Si 20 000 € ont été payés par les voyageurs et que tu déclares les 17 000 € reçus, l'écart de 3 000 € te fait remonter."),
                 (True, "Additionne TOUTES les plateformes",
                  "Deux réservations oubliées sur Booking suffisent : eux consolident les fichiers, toi aussi."),
                 (False, "Ne saute pas une année parce qu'elle est petite",
                  "Une activité démarrée en octobre reste au-dessus du seuil de 2 000 € ou 30 transactions."),
                 (False, "Ne gonfle pas non plus tes recettes",
                  "La taxe de séjour collectée et la caution ne sont pas des revenus : les ajouter, c'est payer de l'impôt pour rien.")],
                "Le geste de janvier", "Tu prends le rapport annuel de chaque plateforme, tu les additionnes, et ce total tombe dans ta déclaration.",
                lead="L'algorithme fait la chose la plus simple du monde : il compare deux montants."),

    d.stats(4, "Erreur 2<br>Le seuil des<br>23 000 €", "L'actualité 2026",
            [("23 000 €", "De recettes BRUTES : au-delà, l'affiliation à l'URSSAF est obligatoire"),
             ("35 à 45 %", "Les cotisations d'indépendant, calculées sur le bénéfice BIC net"),
             ("1 200 €", "Le minimum forfaitaire annuel, même avec un bénéfice à zéro"),
             ("3 ans", "Le rattrapage possible, majorations comprises")],
            "La confusion à éviter", "Les 23 000 € déclenchent les cotisations. Le statut LMP, lui, demande en plus que tes recettes dépassent les autres revenus du foyer. Deux seuils, deux courriers.",
            lead="L'URSSAF a lancé une campagne de régularisation massive, questionnaires à l'appui, sur la base des DAC7 2024 et 2025."),

    d.layers(5, "Erreur 3<br>L'amortissement<br>bricolé", "Là où ils concentrent leurs vérifications",
             [("Bricolage 1", "Le terrain amorti",
               "Le terrain ne s'use pas, il ne s'amortit jamais. Il faut sortir 10 à 20 % du prix d'achat, 30 à 40 % en zone très dense."),
              ("Bricolage 2", "La durée calquée sur le crédit",
               "On amortit par composant : gros œuvre 40 à 50 ans, toiture 25 ans, électricité et plomberie 15 à 20 ans, mobilier 5 à 10 ans."),
              ("Bricolage 3", "Le mobilier mélangé au bâti",
               "Depuis 2025 les amortissements de l'immobilier sont réintégrés dans la plus-value. Pas le mobilier, à condition qu'il soit séparé.")],
             "À surveiller, sans s'affoler", "Un rapport du 8 juillet 2026 recommande un plafonnement des taux d'amortissement. Aucun taux ni aucune date n'est arrêté à ce jour.",
             lead="Un tableau propre n'est pas de la comptabilité pour le plaisir : c'est ta pièce à conviction et ton calcul de sortie."),

    d.pincer(6, "Erreur 4<br>Les charges<br>sans justificatif", "Déduire ce que tu ne peux pas prouver",
             ("3 ans", "Le délai pendant lequel l'administration peut revenir sur une déclaration déjà déposée."),
             ("6 ans", "La profondeur sur laquelle elle peut te réclamer les pièces justificatives correspondantes."),
             ("Pas de facture, pas de charge", "Le ménage payé en liquide, les travaux sans facture, l'assurance sans attestation : tout cela saute."),
             "La charge qu'on oublie", "La commission de la plateforme est déductible au réel, et les factures sont téléchargeables depuis ton compte hôte. Ne la calcule pas de tête.",
             lead="Une charge déduite n'existe que si la pièce qui la prouve existe aussi."),

    d.flow(7, "Erreur 5<br>Les petites taxes<br>qui deviennent<br>des signaux", "Les portes d'entrée",
           [("La CFE tombe en décembre",
             "Tu loues en meublé, donc tu exerces une activité professionnelle au sens de la CFE. Même en micro, même pour un seul bien."),
            ("La taxe de séjour n'est pas toujours collectée",
             "Quand la plateforme ne la collecte pas, ou en direct, c'est toi qui la collectes et qui la reverses à la commune."),
            ("Le dossier qui les oublie appelle le reste",
             "L'inspecteur qui voit deux manquements simples se demande ce que vaut le reste de la déclaration.")],
           "Le vrai objectif", "Le but n'est pas de payer moins que ce que tu dois. C'est de payer exactement ce que tu dois, avec un dossier que tu peux démontrer.",
           lead="Ce ne sont pas les montants qui comptent ici, c'est ce qu'ils racontent sur ta rigueur."),

    d.cta("Action · 1 mot",
          'Et si tu régularisais<br>' + acc("avant eux") + ' ?',
          "CONTROLE",
          "et je t'envoie le point de contrôle des 5 erreurs, avec les seuils et les délais.",
          "Une régularisation spontanée coûte 10 % de majoration. Un redressement, entre 40 et 80 %."),

    d.closing("Le fisc a tes chiffres avant toi. "
              + "<em>Ta déclaration doit tomber juste.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_chiffre")
