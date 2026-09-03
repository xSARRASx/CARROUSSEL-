#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 10 — video du mercredi 02/09/2026 : Airbnb teste une commission a 6 %
(ID YouTube ARDRtYtIgSk).

⚠️ Le titre YouTube s'affiche traduit (« Airbnb Fees: What Really Changes for
Hosts ») : le vrai titre francais est « Frais Airbnb : Ce qui change vraiment
pour les hotes ». Seule la transcription francaise fait foi.

Sujet ENTIEREMENT NEUF cote stories : aucune fournee n'avait encore traite les
commissions Airbnb ni la reservation en direct. Aucun recouvrement a elaguer,
sauf le point « a qui appartient la base client » qui frole la conformite deja
vue en banque-02 : on n'en garde QUE ce qui est neuf (la propriete de la base
de voyageurs), une seule story.

Quatre sequences, parce que la video est dense (25 min) et que chaque bloc a sa
matiere propre — jamais de remplissage :
    AD — la nouvelle decryptee (6 stories, lundi) ;
    AE — les trois pieges (5 stories, mardi) ;
    AF — l'entonnoir inconnu / connecte / fidele (6 stories, reserve) ;
    AG — construire sa base client (5 stories, reserve).

AF et AG partent en reserve VOLONTAIREMENT : leur contenu est intemporel, c'est
du stock pour les semaines sans video. AD et AE, eux, collent a une actualite
qui bouge (un test americain) : ils passent en premier.

⚠️ TAILLES IMPOSEES PAR LA GRILLE : 6 stories le lundi, 5 le mardi. L'ordre
alphabetique donne le jour, la sequence la plus chaude prend la premiere lettre.

⚠️ Contenu 100 % issu de la transcription. Aucun chiffre, aucune source, aucune
date inventes. Sebastien parle d'un TEST americain : les stories gardent ce
conditionnel et ne promettent jamais que ca arrivera en France.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : les outils maison cites dans la
video (le moteur de reservation integre, l'assurance maison, le pre-checkin)
sont ECARTES. On garde le principe, jamais le produit.

Rendu : python3 render_stories.py banque-10
"""
from photo_style import (cover, focus, fin, p_steps, p_bigstat, p_duo,
                         p_formula, acc, write_lot)

# Les apostrophes ne passent pas dans une expression de f-string.
SIX = acc("6 %")
CEDER = acc("céder")
TOUCHE = acc("touche pas")
TEST = acc("test")
RELATION = acc("relation")
JAMAIS_EU = acc("jamais eu")
SECURITE = acc("sécurité")
NATURE = acc("en nature")
RACHETE = acc("rachète")
DEUX_QUESTIONS = acc("deux questions")
UN_NOM = acc("un nom")
PROPRIETAIRE = acc("propriétaire")
AVANT = acc("avant")

SEQUENCES = {

# ============================================================================
# SEQUENCE AD — La nouvelle decryptee (lundi, 6 stories)
# ============================================================================
"AD_airbnb_teste_6": [
    cover("bg_facade_pierre", "l'information vient de tomber",
          f'Airbnb teste une commission à {SIX}.',
          sub="Pas 15,5 %. Six. Mais uniquement si c'est toi qui amènes le "
              "voyageur, et il y a une contrepartie.",
          hand_bottom="on décortique, juste après"),

    p_bigstat("bg_documents", "ce qu'on sait vraiment",
              "Un test, aux États-Unis, depuis fin août",
              "6 %", "au lieu de 15,5 % sur la réservation",
              ["Rapporté par Skift le 29 août, puis par Bloomberg.",
               "Des hôtes américains ont reçu un e-mail : « partagez votre "
               "lien, vous paierez moins cher ».",
               "Un nouveau bouton est apparu dans l'éditeur d'annonce : un "
               "lien de réservation tracé."],
              numsize=170),

    focus("bg_hall_immeuble", "la rumeur qui circule dans les groupes",
          "Non, Airbnb ne lance pas la réservation en direct.",
          "La réservation reste entièrement sur Airbnb : la messagerie, la "
          "protection, les avis. Ce n'est pas du direct, c'est une "
          "réservation Airbnb à tarif réduit, parce que le client, c'est toi "
          "qui l'as trouvé."),

    p_steps("bg_boites_lettres", "trois détails qui changent tout",
            "Ce que le test dit exactement",
            [("Un curseur est prévu",
              "Il propose de reverser une partie de l'économie au voyageur. "
              "Il est facultatif."),
             ("Seul le lien tracé compte",
              "Le lien classique de ton annonce ne déclenche rien. Si tu fais "
              "de la publicité, c'est le lien généré qu'il faut utiliser."),
             ("Le taux n'est pas figé",
              "Airbnb le dit lui-même : ce n'est pas standardisé et il peut "
              "le changer quand il veut.")]),

    p_formula("bg_bureau_matin", "la vraie information est là",
              "Airbnb vient de chiffrer son propre travail",
              "15,5 %", "6 %", "9,5 points d'écart",
              "Sur une réservation de 1 000 €, Airbnb estime donc que trouver "
              "le client vaut 95 € et que gérer la transaction en vaut 60."),

    fin("bg_lac", "Airbnb ne baisse pas ses prix par générosité.",
        "chaque année, le nombre de réservations en direct double : il négocie pour ne pas te perdre"),
],

# ============================================================================
# SEQUENCE AE — Les trois pieges (mardi, 5 stories)
# ============================================================================
"AE_les_trois_pieges": [
    cover("bg_cour", "avant de sauter dessus",
          "6 %, ça ressemble à une bonne affaire. Il y a trois pièges.",
          sub="Le lien sert, mais dans un cas précis seulement. Voilà ce que "
              "personne ne regarde.",
          hand_bottom="les trois, juste après"),

    focus("bg_ville_doree", "premier piège",
          f'Tu paies 6 % pour {CEDER} un client qui était à toi.',
          "Le voyageur reste un client Airbnb : son e-mail, son historique, "
          "sa fidélité. Airbnb lui recommandera d'autres annonces, et tu "
          "n'auras rien dessus. Tu as fait le travail de le trouver, tu le "
          "rends au moment de la réservation."),

    p_duo("bg_salon_vide", "deuxième piège", "Le curseur",
          "Ce qu'Airbnb te suggère",
          ["Reverser une partie de l'économie au voyageur.",
           "Sur 9,5 points gagnés, en rendre 5.",
           "Ton économie fond, et ta clientèle apprend à attendre des remises."],
          "Ce qu'il vaut mieux faire",
          [f'On n\'y {TOUCHE} pas.',
           "Le gain de 9,5 points, c'est ta marge, pas une réduction.",
           "Si tu veux offrir quelque chose, offre un service, pas du prix."]),

    focus("bg_village", "troisième piège",
          f'C\'est un {TEST}, pas une règle.',
          "Airbnb l'écrit : le taux n'est pas standardisé et peut changer à "
          "tout moment. Bâtir une stratégie dessus, c'est refaire exactement "
          "l'erreur de ceux qui avaient tout construit sur les frais partagés "
          "à 3 % et qui se sont réveillés à 15,5 %."),

    fin("bg_montagne", "La question a changé de forme.",
        "ce n'est plus « combien coûte Airbnb », c'est « combien me coûte un client selon le canal »"),
],

# ============================================================================
# SEQUENCE AF — L'entonnoir des trois voyageurs (reserve, 6 stories)
# ============================================================================
"AF_entonnoir_voyageurs": [
    cover("bg_chemin_aube", "la vraie stratégie",
          f'Le canal dépend de la {RELATION}, pas du prix.',
          sub="Trois types de voyageurs, trois canaux, trois taux. Une fois "
              "que tu vois la grille, tu ne la quittes plus.",
          hand_bottom="les trois étages, juste après"),

    p_steps("bg_immeuble_dore", "l'entonnoir en trois étages",
            "À qui tu parles décide de ce que tu paies",
            [("L'inconnu : 15,5 %",
              "Il ne te connaît pas. Airbnb l'a trouvé, rassuré, convaincu. "
              "Tu paies le prix d'un client que tu n'aurais jamais eu."),
             ("Le connecté : 6 %",
              "Il te connaît mais n'a jamais dormi chez toi. Il veut encore "
              "la sécurité de la plateforme."),
             ("Le fidèle : 0 %",
              "Il est déjà venu, il te fait confiance. Airbnb n'apporte plus "
              "rien à cette relation.")]),

    focus("bg_prairie", "l'inconnu",
          f'15,5 %, c\'est le prix d\'un client que tu n\'aurais {JAMAIS_EU}.',
          "Ce n'est pas une taxe, c'est une acquisition. Comme une publicité. "
          "Le seul objectif avec lui : qu'il ne reparte pas inconnu. Il arrive "
          "par Airbnb, il doit repartir dans ta base."),

    focus("bg_cles", "le connecté",
          f'Lui, il veut encore la {SECURITE}.',
          "Il t'a découvert sur les réseaux, par un ami, par ta liste de "
          "contacts. Mais virer 1 500 € à quelqu'un chez qui il n'a jamais "
          "dormi, ça le freine. De toute façon tu lui aurais envoyé le lien "
          "de ton annonce : autant que ce soit le lien à 6 %."),

    p_duo("bg_salon_cosy", "le fidèle", f'On le garde {NATURE}, pas au prix',
          "Ce qui ne marche pas",
          ["Lui rendre l'économie en réduction.",
           "Il s'habitue, et la remise devient le nouveau prix.",
           "Tu as récupéré 15,5 points pour les redonner aussitôt."],
          "Ce qui marche",
          ["Une arrivée dès 9 h, un départ tardif.",
           "Un panier d'accueil, un surclassement.",
           "La 21e nuit offerte au bout de 20, la priorité sur l'été."]),

    fin("bg_ciel_dore", "Pour Airbnb, 6 vaut mieux que 0.",
        "il rachète l'étage du milieu en pariant que tu n'iras jamais jusqu'au direct"),
],

# ============================================================================
# SEQUENCE AG — Construire sa base client (reserve, 5 stories)
# ============================================================================
"AG_construire_sa_base": [
    cover("bg_mer_calme", "ce que ça vaut, chiffré par Airbnb",
          "Ta base client vaut 9,5 points sur chaque réservation.",
          sub="C'est Airbnb qui vient de mettre ce prix-là dessus. Reste à "
              "savoir si tu en as une.",
          hand_bottom="le plan, juste après"),

    focus("bg_plage_aube", "commence par te mesurer",
          f'{DEUX_QUESTIONS} qui disent tout.',
          "Combien de voyageurs des douze derniers mois es-tu capable de "
          "recontacter sans passer par Airbnb ? Et quelle part de tes "
          "réservations vient de gens déjà venus ? Si les deux réponses sont "
          "zéro, tu es fournisseur de la plateforme à 15,5 % à vie."),

    p_steps("bg_ble", "trois gestes concrets",
            "Où se capture une base client",
            [("Au moment du check-in en ligne",
              "C'est là que le voyageur donne naturellement ses coordonnées. "
              "Pas dans le chat de la plateforme. Avec son consentement, et "
              "dans le respect de la protection des données."),
             ("Dans le logement, par un QR code",
              "Le livret d'accueil, un service à commander, un bonus pour la "
              "prochaine fois : autant de raisons légitimes de scanner."),
             ("En donnant un nom à ton logement",
              f'Pas « T3 vue mer » : {UN_NOM} qu\'on retient, un compte, une '
              "fiche d'établissement, des avis.")]),

    focus("bg_terrasse", "le point que les conciergeries oublient",
          f'Écris dans le contrat à qui appartient la base.',
          f'« Nous construisons la base client de vos biens » est un argument '
          f'commercial très fort aujourd\'hui. Mais cette base revient au '
          f'{PROPRIETAIRE}, et l\'intermédiation entre deux clients reste '
          f'encadrée. Réglé en amont, c\'est un atout ; réglé après, un litige.'),

    fin("bg_ciel_rose", f'La base {AVANT} le moteur.',
        "un site de réservation sans contacts qualifiés, c'est une boutique sans clients"),
],

}

SLUG = "banque-10"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
