#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 18 — video du 27/09/2026 : « LMNP 2027 : ce que le gouvernement prepare »
(ID YouTube U6vGmP7QX1k). Sous-titres recuperes le 28/09, lus en entier.

⚠️ CETTE VIDEO EST ELLE-MEME UN DEMENTI. Depuis 48 heures les titres annoncent
« la fin du LMNP » a partir d'une lettre du premier ministre qui contient DEUX
phrases sur le meuble. Les stories doivent donc etre l'inverse d'alarmistes :
elles citent mot pour mot, et elles separent proprement VOTE / REJETE / RUMEUR.
Quand Sebastien donne son pronostic, il precise « une analyse personnelle, pas
comme un fait » : cette nuance est gardee telle quelle.

⚠️ ECARTE, comme toujours (marque LE SOUS LOUEUR) : declarationlmnp.fr, le
logiciel de declaration au reel, la lettre d'option preparee par l'outil, le
simulateur maison, et guestlucky.com cite pour la courte duree. Les DECISIONS
restent (passer au reel, faire classer) : ce sont des conseils, pas des outils.

⚠️ CHEVAUCHEMENTS EVITES. banque-04 a deja traite le rapport du 8 juillet qui
recommandait de plafonner l'amortissement, et le « le statut n'est PAS
supprime ». banque-06 a traite la liasse et l'expert-comptable. banque-12 a
traite la plus-value de la residence principale. Ici on garde ce qui est NEUF :
la lettre du 23 septembre, le tri en trois colonnes, et le calendrier a dix
semaines.

    BA — la lettre, mot pour mot (6 stories, jeudi) ;
    BB — ce que tu as deja perdu (4, vendredi) ;
    BC — les quatre decisions avant decembre (5, reserve).

⚠️ Trois tailles differentes, trois formes differentes, quinze fonds differents,
aucun repris aux fournees 15, 16 et 17.

Rendu : python3 render_stories.py banque-18
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_vs,
                         p_formula, p_bigstat, acc, write_lot, accroche)

NUM_LOT = 18

# Les apostrophes ne passent pas dans une expression de f-string.
DEUX_PHRASES = acc("deux phrases")
REORIENTE = acc("réorienté")
PAS_SUPPRIME = acc("le mot « supprimé » n'y est pas")
PLUS_AVANTAGEUSE = acc("plus avantageuse")
CONCURRENT = acc("un régime concurrent")
LOCATION_NUE = acc("la location nue")
POLITIQUE = acc("un document politique")
DEJA_EU_LIEU = acc("a déjà eu lieu")
RETROACTIF = acc("rétroactif")
DIX_SEMAINES = acc("dix semaines")
TOUTE_LA_FRANCE = acc("toute la France")
DEUX_MINUTES = acc("deux minutes")
MAINTENANT = acc("maintenant")

SEQUENCES = {

# ============================================================================
# SEQUENCE BA — La lettre du 23 septembre, mot pour mot (jeudi, 6 stories)
# Forme : cover > focus > p_vs > p_steps > focus > fin
# ============================================================================
"BA_la_lettre_mot_pour_mot": [

    cover("bg_documents", "lettre du 23 septembre",
          f'Sur le meublé, la lettre contient {DEUX_PHRASES}. Pas une de plus.',
          sub="Depuis, les titres annoncent la fin du LMNP. On va les lire "
              "mot pour mot, puis trier ce qui est voté, ce qui a été rejeté "
              "et ce qui n'est qu'une rumeur.",
          hand_bottom=accroche(NUM_LOT * 3)),

    focus("bg_facade_pierre", "citées par Le Monde et BFM Business",
          "Les deux phrases, sans en changer un mot.",
          "« Le soutien fiscal à la location meublée doit être réorienté. » "
          "Et : « Le mitage des centres-villes dans les zones tendues par des "
          "locations de courte durée à vocation touristique ne doit pas être "
          "fiscalement plus avantageux que les locations de longue durée. » "
          "C'est tout."),

    p_vs("bg_hall_immeuble", "ce qu'on lit / ce qui est écrit",
         "Deux lectures de la même lettre",
         "Les titres depuis 48 h",
         ["« Le statut est supprimé »",
          "« C'est la fin du LMNP »",
          "« L'amortissement saute »"],
         "Le texte, lui",
         ["Un seul verbe : réorienté",
          "Une cible nommée : la courte durée touristique en zone tendue",
          "Un point de comparaison : la longue durée"],
         "Pas un chiffre, pas une date, et le mot « supprimé » n'apparaît "
         "nulle part."),

    p_steps("bg_bureau_papiers", "trois colonnes, pas une",
            "Voté, rejeté, ou simple rumeur",
            [("Voté, et déjà en vigueur",
              "Prélèvements sociaux à 18,6 %. Amortissements réintégrés dans "
              "le calcul de la plus-value. Micro-BIC à 30 % pour le meublé de "
              "tourisme non classé. Téléservice national d'enregistrement."),
             ("Rejeté, noir sur blanc",
              "L'amendement qui plafonnait l'amortissement à 2 % par an a été "
              "rejeté par l'Assemblée nationale le 21 novembre 2025, et il "
              "n'a pas été repris dans le texte final du 49.3, le 19 février "
              "2026. L'amortissement a déjà survécu à un assaut."),
             ("Rumeur, rien d'autre",
              "L'abattement du micro qui passerait de 50 à 40 % en 2027 : "
              "évoqué dans des discussions, écrit et adopté nulle part. « La "
              "fin du LMNP » : une lecture de la lettre, pas son contenu.")]),

    focus("bg_village", "le dispositif créé par la loi de finances 2026",
          f'Le Jeanbrun est {CONCURRENT}, pas un remplaçant.',
          f'Disponible depuis le 21 février, il ouvre un amortissement à '
          f'{LOCATION_NUE} uniquement, 3 à 4 % par an, plafonné, avec un '
          f'engagement et des loyers plafonnés. Il ne te concerne donc pas si '
          f'tu loues en meublé. L\'État ne remplace pas ton régime : il '
          f'construit une allée à côté pour attirer l\'épargne vers le vide.'),

    fin("bg_lac", f'Une lettre reste {POLITIQUE}, pas un texte de loi.',
        "ne la sous-estime pas, mais ne la lis pas comme si elle était déjà votée"),
],

# ============================================================================
# SEQUENCE BB — Ce que tu as deja perdu (vendredi, 4 stories)
# Forme : cover > p_timeline > p_formula > fin
# ============================================================================
"BB_ce_que_tu_as_deja_perdu": [

    cover("bg_escalier", "avant de regarder 2027",
          f'La vraie réforme du meublé {DEJA_EU_LIEU}.',
          sub="Elle n'est pas devant toi, elle est derrière. Quatre choses "
              "s'appliquent déjà à tes revenus, et deux d'entre elles sont "
              "passées presque sans un article.",
          hand_bottom=accroche(NUM_LOT * 3 + 1)),

    p_timeline("bg_ville_doree", "ce qui est acté",
               "Quatre couches posées en dix-huit mois",
               [("15 février 2025",
                 "Les amortissements déduits au réel sont réintégrés dans le "
                 "calcul de la plus-value à la revente.", None),
                ("Revenus 2025",
                 "Meublé de tourisme non classé : plafond de micro à 15 000 € "
                 "et abattement ramené à 30 %, contre 50 % et environ "
                 "78 000 € pour la longue durée et le classé.", None),
                ("Loi de financement de la Sécurité sociale 2026",
                 "Les prélèvements sociaux passent de 17,2 % à 18,6 %. "
                 "C'est rétroactif : ça vise les revenus perçus depuis le "
                 "1er janvier 2025, donc la déclaration faite ce printemps.", None),
                ("20 mai 2026",
                 "Tous les meublés de tourisme doivent être enregistrés sur "
                 "le téléservice national. Ce n'est pas de la fiscalité, mais "
                 "l'État sait désormais qui loue, où, et combien de nuits.", None)]),

    p_formula("bg_cour", "l'exemple qui fait le plus mal",
              "Acheté 200 000 €, revendu 250 000 €",
              "50 000 € de plus-value, comme avant",
              "plus 60 000 € d'amortissements réintégrés",
              "110 000 € imposables au lieu de 50 000 €",
              "À plus de 36 % entre l'impôt et les prélèvements sociaux, la "
              "facture plus que double. Et ça s'applique à des "
              "investissements faits sous l'ancienne règle."),

    fin("bg_montagne", f'1,4 point de plus, et c\'est {RETROACTIF}.',
        "sur 20 000 € de bénéfice imposable, ça fait 280 € de plus par an, chaque année"),
],

# ============================================================================
# SEQUENCE BC — Les quatre decisions avant decembre (reserve, 5 stories)
# Forme : cover > p_steps > p_bigstat > focus > fin
# ============================================================================
"BC_quatre_decisions_avant_decembre": [

    cover("bg_ble", "le calendrier, c'est lui qui compte",
          f'Rien ne peut t\'arriver avant décembre. Ça te laisse {DIX_SEMAINES}.',
          sub="Projet de loi de finances 2027 présenté le 1er octobre, débats "
              "en octobre et novembre, vote ou 49.3 en décembre, application "
              "au 1er janvier 2027.",
          hand_bottom=accroche(NUM_LOT * 3 + 2)),

    p_steps("bg_prairie", "dix semaines, quatre décisions",
            "Ce qui se décide avant le vote",
            [("Au micro-BIC ? Passe au réel",
              "C'est le micro qui est visé depuis le début, et c'est le réel "
              "avec son amortissement qui vient d'être défendu. Sur 15 000 € "
              "de loyers en longue durée, le micro laisse 7 500 € imposables, "
              "soit environ 3 650 € d'impôt et de prélèvements par an."),
             ("En courte durée ? Fais classer le logement",
              "Une visite d'un organisme agréé, quelques centaines d'euros, "
              "valable 5 ans."),
             ("Vérifie si ta commune est en zone tendue",
              "Le gouvernement n'a jamais parlé de la France entière. La "
              "liste est fixée par décret."),
             ("Tu penses vendre dans les cinq ans ? Calcule la plus-value",
              "Avec la réintégration des amortissements, le moment de la "
              "vente change la facture de plusieurs dizaines de milliers "
              "d'euros.")]),

    p_bigstat("bg_cles", "la deuxième décision, en chiffres",
              "Ce que change le classement",
              "78 000", "€ de plafond environ, au lieu de 15 000",
              ["Non classé : 15 000 € de recettes, abattement de 30 %. Tu "
               "paies donc de l'impôt sur 70 % de ce que tu encaisses.",
               "Classé : environ 78 000 € de plafond et 50 % d'abattement, "
               "le même régime que la longue durée.",
               "Sur 15 000 € de recettes, ça fait 3 000 € de base imposable "
               "en moins, chaque année.",
               f'Et un meublé classé aligné sur la longue durée, c\'est '
               f'précisément ce que la lettre ne vise pas : elle vise ce qui '
               f'est {PLUS_AVANTAGEUSE} que la longue durée.']),

    focus("bg_chemin_aube", "la troisième décision, souvent oubliée",
          f'Le gouvernement n\'a jamais parlé de {TOUTE_LA_FRANCE}.',
          f'Il a toujours dit : les centres-villes, dans les zones tendues. '
          f'C\'est une liste de communes fixée par décret, les grandes '
          f'agglomérations, le littoral et certaines zones touristiques. Si '
          f'ton bien n\'est pas dedans, tu n\'es pas dans la cible décrite '
          f'par cette lettre. Le simulateur de service-public.fr te répond en '
          f'{DEUX_MINUTES} avec le nom de la commune.'),

    fin("bg_ciel_rose", f'Si tu penses vendre, fais le calcul {MAINTENANT}.',
        "il dépend du montant amorti, de la durée de détention (22 ans pour l'impôt, 30 pour les prélèvements sociaux) et de la date de vente"),
],

}

# ⚠️ DEUX LOTS, ET C'EST VOULU.
# La fournee du jeudi n'ouvre que DEUX journees automatiques (jeudi 6 + vendredi
# 5 = 11 creneaux) et il y a 15 stories. Sans rien faire, BC partait entiere en
# reserve -- or c'est la sequence la plus perissable des trois : elle parle de
# « dix semaines avant decembre ». La laisser dormir pendant que le stock
# recycle banque-01 aurait ete un gachis.
# Elle a donc son propre lot, livre sur le mardi libre qui suit.
LOTS = {
    "banque-18":  ["BA_la_lettre_mot_pour_mot", "BB_ce_que_tu_as_deja_perdu"],
    "banque-18b": ["BC_quatre_decisions_avant_decembre"],
}

def main():
    for slug, noms in LOTS.items():
        stories = {}
        for seq in noms:
            for i, body in enumerate(SEQUENCES[seq], 1):
                stories[f"{seq}_{i:02d}"] = body
        write_lot(slug, stories)

if __name__ == "__main__":
    main()
