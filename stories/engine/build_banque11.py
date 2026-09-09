#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 11 — video du 08/09/2026 : « Revenus reels vs revenus affiches : Le
grand mensonge » (ID YouTube v8fzA9JYTHM).

⚠️ Le titre s'affiche traduit sur YouTube (« Actual Income vs. Reported Income:
The Big Lie »). Seule la transcription francaise fait foi. Transcription
fournie par Martin.

⚠️ RECOUVREMENT VERIFIE avec _OOxN_7bZWI (« 7 choses a ne jamais dire quand tu
commences a gagner de l'argent », traitee le 03/08 via semaine-01). Ce sont
DEUX videos differentes. Le seul angle commun est « les 4 reactions quand tu
dis combien tu gagnes » (moquerie, jalousie, attente, calcul) : il est
DELIBEREMENT ECARTE ici. Tout le reste est neuf.

Quatre sequences, la video fait 27 minutes et chaque bloc a sa matiere propre :
    AH — le chiffre affiche est une publicite (6 stories, jeudi) ;
    AI — decortiquer un chiffre annonce (5 stories, vendredi) ;
    AJ — les vrais riches sont invisibles (6 stories, reserve) ;
    AK — actifs plutot que passifs (5 stories, reserve).

AJ et AK partent en reserve VOLONTAIREMENT : contenu intemporel, c'est le stock
des semaines sans video.

⚠️ TAILLES IMPOSEES PAR LA GRILLE : 6 stories le jeudi, 5 le vendredi.

⚠️ Contenu 100 % issu de la transcription. Sebastien parle lui-meme, en public
et depuis longtemps, de son depot de bilan et de son divorce (« j'en ai deja
parle sur internet ») : la story qui l'evoque reste factuelle et sobre, comme
lui. Aucun chiffre de revenu n'est avance -- ce serait contredire le propos
meme de la video.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : l'application citee en fin de video
est ECARTEE, comme toujours.

Rendu : python3 render_stories.py banque-11
"""
from photo_style import (cover, focus, fin, p_steps, p_duo, acc, write_lot)

# Les apostrophes ne passent pas dans une expression de f-string.
PUBLICITE = acc("publicité")
DONNE = acc("donné")
PERTES = acc("pertes")
MOINS = acc("moins")
PRODUIT = acc("produit")
CINQ_QUESTIONS = acc("cinq questions")
RECURRENT = acc("récurrent")
CONFORT = acc("confort de vie")
INVISIBLES = acc("invisibles")
TEMPS = acc("temps")
TELEPHONE = acc("téléphone")
ENNUYEUX = acc("ennuyeux")
ARRETE = acc("arrêté")
PETITS = acc("des petits")
CREDIT = acc("crédit")
LONG = acc("plus c'est long")
INDEPENDANCE = acc("indépendance")

SEQUENCES = {

# ============================================================================
# SEQUENCE AH — Le chiffre affiche (jeudi, 6 stories)
# ============================================================================
"AH_le_chiffre_affiche": [
    cover("bg_ville_doree", "la question qu'on lui pose tout le temps",
          f'Un chiffre affiché n\'est pas un résultat. C\'est une {PUBLICITE}.',
          sub="Sébastien ne dit jamais combien il gagne. Ce n'est pas de la "
              "modestie, c'est un calcul. Le voilà.",
          hand_bottom="le raisonnement, juste après"),

    focus("bg_immeuble_dore", "la seule question à se poser",
          f'Cet argent, c\'est celui que tu lui as {DONNE}.',
          "Quand quelqu'un t'annonce ce qu'il gagne, demande-toi pourquoi il "
          "te le dit. La belle voiture, la villa, l'addition à 20 000 € : tu "
          "crois voir le fruit de son travail. Tu vois le résultat de ses "
          "ventes. Et ce que tu achètes, c'est cette démonstration."),

    focus("bg_escalier", "l'angle mort de tous les comptes affichés",
          f'Personne ne montre jamais ses {PERTES}.',
          "Toujours les gains, jamais les échecs. Sébastien a raconté "
          "publiquement son dépôt de bilan, la perte de tout, et les dîners "
          "de famille où on le regardait comme un perdant. Être transparent "
          "sur ses pertes dessert commercialement. C'est justement pour ça "
          "que ça vaut quelque chose."),

    p_duo("bg_salon_vide", "le décor et les coulisses",
          "Ce qu'on te montre, ce qu'on te cache",
          "Ce qui passe à l'écran",
          ["La voiture, souvent louée. La villa, souvent louée.",
           "Le meilleur mois, jamais la moyenne.",
           "« Tout est à crédit », dit parfois en riant."],
          "Ce qui n'y passe jamais",
          ["Les mois creux et les années blanches.",
           "Les charges, l'impôt, ce qui reste vraiment.",
           "Ce qu'il a fallu arrêter pour en arriver là."]),

    focus("bg_cour", "le piège se referme sur celui qui parle",
          f'Le jour où tu annonces un chiffre, tu ne peux plus jamais faire {MOINS}.',
          "S'il fait moins l'année suivante, il n'est plus crédible. Alors il "
          "ne peut plus ralentir, plus prendre de vacances, plus changer de "
          "vie. Il doit charbonner pour tenir le décor. Ce n'est pas la "
          "liberté, c'est une prison qu'on se fabrique."),

    fin("bg_lac", f'Devant un chiffre affiché, tu es le {PRODUIT}.',
        "ce n'est pas de la méchanceté, c'est de la comptabilité : ce marketing-là se paie"),
],

# ============================================================================
# SEQUENCE AI — Decortiquer un chiffre (vendredi, 5 stories)
# ============================================================================
"AI_decortiquer_un_chiffre": [
    cover("bg_documents", "la boîte à outils",
          f'{CINQ_QUESTIONS} à poser devant n\'importe quel chiffre.',
          sub="Un chiffre tout seul ne veut rien dire. Avec ces questions, il "
              "commence à parler.",
          hand_bottom="les cinq, juste après"),

    p_steps("bg_bureau_matin", "les trois premières",
            "Ce qu'il faut demander tout de suite",
            [("Brut ou net ?",
              "Un chiffre d'affaires n'est pas un revenu. Entre les deux il y "
              "a les charges, les cotisations, l'impôt."),
             ("Le meilleur mois, ou la moyenne ?",
              "Presque tout le monde annonce son record. Ce n'est pas ce "
              "qu'il fait d'habitude."),
             ("Partagé avec qui ?",
              "« Mon restaurant » quand on en détient quelques pour cent, ce "
              "n'est pas la même phrase. Comme dire qu'on possède Apple parce "
              "qu'on en a des parts.")]),

    focus("bg_facade_pierre", "la quatrième, celle qu'on oublie",
          f'Depuis combien de temps ? Et est-ce {RECURRENT} ?',
          "Quelqu'un lancé il y a trois mois peut avoir fait un excellent "
          "mois et être incapable de le refaire. La durée dit bien plus que "
          "le montant : c'est elle qui sépare un coup de chance d'un métier."),

    focus("bg_prairie", "et la question qu'on lui pose en retour",
          f'« Combien je peux gagner ? » ne veut rien dire.',
          f'Entre la fiscalité de l\'entreprise, la tienne, les cotisations et '
          f'ce qu\'on choisit de passer en charges, deux personnes au même '
          f'chiffre ne vivent pas pareil. La vraie question, c\'est quel '
          f'{CONFORT} tu veux.'),

    fin("bg_montagne", "Un chiffre sans ces questions ne vaut rien.",
        "ce n'est pas un mensonge en soi, c'est juste une information vide"),
],

# ============================================================================
# SEQUENCE AJ — Les vrais riches sont invisibles (reserve, 6 stories)
# ============================================================================
"AJ_vrais_riches_invisibles": [
    cover("bg_mer_calme", "ce qu'il a vu en les côtoyant",
          f'Les vrais riches sont {INVISIBLES}.',
          sub="Pas de voiture de sport, pas de villa filmée. Souvent un "
              "t-shirt et des tongs. On ne paie le paraître que quand il "
              "rapporte quelque chose.",
          hand_bottom="les signes, juste après"),

    focus("bg_chemin_aube", "le marqueur numéro un",
          f'La vraie richesse, c\'est le {TEMPS}.',
          "Face à quelqu'un qui semble aisé, regarde s'il en a. Celui qui "
          "court en permanence, qui doit filer travailler, qui répète qu'il "
          "charbonne : il court après l'argent. Ce n'est pas la même chose "
          "que d'en avoir."),

    focus("bg_terrasse", "le test le plus simple",
          f'Regarde son {TELEPHONE}.',
          "Celui qui ne le consulte jamais a probablement tout organisé et "
          "gagne réellement de l'argent. Celui qui répète que son agenda est "
          "plein et qu'il n'a pas une minute te dit exactement l'inverse de "
          "ce qu'il croit te dire."),

    p_duo("bg_hall_immeuble", "deux profils qu'on confond",
          "Celui qui court, celui qui a construit",
          "Il court encore",
          ["Filme dans sa voiture plusieurs fois par jour.",
           "Agenda plein, aucune disponibilité.",
           "Doit refournir le même effort chaque mois pour tenir son train de vie."],
          "Il a construit",
          ["On ne sait pas ce qu'il possède.",
           "Du temps libre en pleine semaine.",
           "Ses revenus ne dépendent plus entièrement de son activité."]),

    p_steps("bg_boites_lettres", "quand tu cherches quelqu'un pour t'aider",
            "Trois signes qui ne trompent pas",
            [("La durée",
              "Depuis combien de temps parle-t-il de ce sujet ? Depuis "
              "combien de temps le fait-il vraiment ?"),
             ("Il est ennuyeux",
              "Il te parle de TVA, de règlement de copropriété, de fiscalité, "
              "de gestion. C'est pénible, et c'est exactement pour ça qu'il "
              "sait de quoi il parle."),
             ("Il ne met aucune urgence",
              "Celui qui a réussi n'a pas besoin que tu achètes. Il sait même "
              "refuser des gens.")]),

    fin("bg_ciel_dore", f'Ne demande plus combien il gagne. Demande ce qu\'il a {ARRETE}.',
        "c'est ce qu'on arrête qui est instructif, jamais ce qu'on affiche"),
],

# ============================================================================
# SEQUENCE AK — Des actifs, pas des passifs (reserve, 5 stories)
# ============================================================================
"AK_actifs_pas_passifs": [
    cover("bg_ble", "après le décryptage, le concret",
          "Ce que tu fais de l'argent compte plus que le montant.",
          sub="C'est la partie dont personne ne parle sur les réseaux, et "
              "c'est la seule qui change une vie.",
          hand_bottom="le raisonnement, juste après"),

    focus("bg_cles", "le même billet, deux destins",
          f'20 000 € au restaurant, ou 20 000 € qui font {PETITS}.',
          "L'addition impressionne un soir et disparaît. Placée, la même "
          "somme travaille chaque mois et finit par financer les sorties "
          "elle-même. Ce n'est pas une leçon de morale, c'est juste deux "
          "usages du même argent."),

    focus("bg_village", "la phrase qui devrait alerter",
          f'« De toute façon, tout est à {CREDIT}. »',
          "Certains le disent eux-mêmes, presque fièrement. Mais celui qui "
          "consomme tout doit refournir le même effort le mois suivant pour "
          "conserver le décor. Il n'est pas libre : il est dépendant de son "
          "activité, et il ne peut plus s'arrêter."),

    p_duo("bg_ciel_rose", "où va ton argent",
          "Deux directions possibles",
          "Ce qui brille tout de suite",
          ["La voiture, la montre, l'addition photographiée.",
           "Ça se voit, ça ne rapporte rien.",
           "Et il faut recommencer pour l'entretenir."],
          "Ce qui rapporte dans dix ans",
          ["De l'immobilier, des placements, du temps devant soi.",
           "Ça ne se voit pas, ça travaille tout seul.",
           "Plus tu es jeune, plus tu as le temps de le construire."]),

    fin("bg_plage_aube", f'{LONG}, plus c\'est bon.',
        f'le but n\'est pas le train de vie, c\'est l\'{INDEPENDANCE} vis-à-vis de son activité'),
],

}

SLUG = "banque-11"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
