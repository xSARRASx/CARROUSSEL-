#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 14 — video du mercredi 16/09/2026 : « La verite sur le marche
immobilier en 2026 » (ID YouTube iIO-RH_doLo).

⚠️ SUJET 100 % NEUF, et ca fait du bien : les quatre dernieres fournees etaient
fiscales ou reglementaires. Aucune n'avait parle du marche lui-meme.

⚠️ La FIN de la video effleure des choses deja traitees -- commission Airbnb
(banque-10), copropriete qui interdit (banque-03 et 05), loi Le Meur et
amortissement menace (banque-04), CFE (banque-13). ECARTE. On n'en garde que la
conclusion, qui est neuve et forte : le meuble n'est plus un placement, c'est
un metier.

    AR — l'etat du marche, en six chiffres (6 stories, lundi) ;
    AS — pourquoi les taux ne baisseront pas, et les trois scenarios (5, mardi) ;
    AT — ce que Sebastien fait de sa propre maison (5, reserve).

⚠️ Formes toutes differentes, et differentes de banque-13 : p_bars est enfin
utilise pour ce a quoi il sert (des proportions comparees).

⚠️ Contenu 100 % issu de la transcription. Tous les chiffres viennent des deux
sources que Sebastien cite : le tableau de bord Credit Logement d'aout 2026 et
les courbes de Friggit. Aucune projection inventee : les trois scenarios sont
les siens, presentes comme des scenarios et non comme des certitudes. Il dit
lui-meme quel est le plus probable, on le dit comme lui.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : le module d'etude de marche cite en
fin de video est ECARTE.

Rendu : python3 render_stories.py banque-14
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bars,
                         p_bigstat, p_duo, p_formula, acc, write_lot, accroche)

NUM_LOT = 14

# Les apostrophes ne passent pas dans une expression de f-string.
DETTE = acc("de la dette")
FIGE = acc("figé")
BOUCHON = acc("bouchon")
DEJA = acc("a déjà commencé")
MOINS_CHER = acc("moins cher")
SUBVENTIONNER = acc("subventionner")
DOIVENT = acc("doivent vendre")
METIER = acc("un métier")
LENTEMENT = acc("lentement")
FATIGUES = acc("fatigués")
ESPERE = acc("le prix des ventes qui se font")

SEQUENCES = {

# ============================================================================
# SEQUENCE AR — L'etat du marche (lundi, 6 stories)
# Forme : cover > p_bars > focus > p_timeline > p_bigstat > fin
# ============================================================================
"AR_marche_fige": [
    cover("bg_facade_pierre", "les vrais chiffres, pas les avis",
          f'Le marché n\'est pas mort. Il est {FIGE}.',
          sub="Tableau de bord Crédit Logement d'août, courbes de Friggit. "
              "Deux sources publiques, et un constat qui ne plaira à personne.",
          hand_bottom=accroche(NUM_LOT + 1)),

    p_bars("bg_documents", "on emprunte plus long que jamais",
           "La durée des prêts, hier et aujourd'hui",
           [("25 ans ou plus, aujourd'hui", 49),
            ("25 ans ou plus, en 2019", 38),
            ("Moins de 20 ans, en 2019", 31),
            ("Moins de 20 ans, aujourd'hui", 16)],
           note="La Banque de France interdit d'aller au-delà de 25 ans. Ce "
                "réservoir-là est vide."),

    focus("bg_immeuble_dore", "l'écart que personne ne regarde",
          "Les prix ont fait +55 %. Les loyers, −9 %.",
          "Depuis 2000, rapportés aux revenus des ménages. Les loyers n'ont "
          "jamais quitté le couloir historique, ils sont même en dessous. "
          "Entre les deux, c'est le rendement qui s'est écrasé. C'est pour ça "
          "que tant d'investisseurs sont allés chercher la courte durée."),

    p_timeline("bg_hall_immeuble", "comment on en est arrivé là",
               f'La hausse des prix, c\'était {DETTE}',
               [("En 2000 : 5 % sur 15 ans",
                 "Les prix tenaient dans un couloir étroit depuis 1965.", None),
                ("En 2021 : 1 % sur 25 ans",
                 "À mensualité égale, tu pouvais emprunter presque le double. "
                 "Les Français ne sont pas devenus plus riches : le crédit est "
                 "devenu presque gratuit et presque infini.", None),
                ("Aujourd'hui : 3,31 % et ça remonte",
                 "Depuis juin, trois points de base par mois. Les deux "
                 "réservoirs qui ont porté les prix pendant vingt ans sont "
                 "vides.", None)]),

    p_bigstat("bg_cour", "et pourtant, presque personne ne baisse",
              f'Le {BOUCHON}',
              "954 000", "ventes sur douze mois, contre un peu plus d'un "
                         "million en régime normal",
              ["Un couple vend son appartement 50 000 € sous son espérance : "
               "il perd aussi 50 000 € d'apport pour la maison d'après. Il "
               "perd des deux côtés, donc il ne vend pas.",
               "Le vendeur de la maison ne vend pas non plus, et ne peut donc "
               "pas acheter à son tour.",
               "Un seul maillon qui refuse de baisser arrête toute la chaîne."],
              numsize=140),

    fin("bg_lac", "Un marché figé ne dure pas éternellement.",
        "à un moment quelqu'un doit vendre, et c'est lui qui fixera le prix"),
],

# ============================================================================
# SEQUENCE AS — Les taux et les scenarios (mardi, 5 stories)
# Forme : cover > focus > p_steps > p_duo > fin
# ============================================================================
"AS_taux_et_scenarios": [
    cover("bg_bureau_matin", "la croyance qui fait attendre tout le monde",
          "« Les taux vont rebaisser. » Regarde ce que paie l'État.",
          sub="C'est le chiffre qui règle la question, et il est public.",
          hand_bottom=accroche(NUM_LOT + 5)),

    focus("bg_ville_doree", "l'anomalie du moment",
          f'Ta banque te prête {MOINS_CHER} qu\'elle n\'emprunte.',
          "L'État français emprunte à 3,90 %. Toi, tu empruntes à 3,31 %. "
          "Historiquement, les banques prennent un point au-dessus de l'État. "
          "Crédit Logement l'écrit : elles ont choisi de ne pas répercuter la "
          "hausse, quitte à dégrader leur marge, pour garder de l'activité."),

    p_steps("bg_montagne", "trois chemins possibles",
            "Ce que les chiffres rendent probable",
            [("A. Les taux baissent",
              "Le marché se débloque, ceux qui ont attendu gagnent. Il "
              "faudrait que l'État réemprunte à 3 %. Avec une dette publique "
              "à 118 % du PIB, Sébastien n'y croit pas d'ici deux ans."),
             ("B. Les taux restent hauts, les prix s'ajustent",
              "Vers 4 %, la capacité d'emprunt perd 5 à 7 %. Ceux qui DOIVENT "
              "vendre acceptent de baisser, et leurs ventes deviennent la "
              "référence. Moins 10 à 20 % sur trois à cinq ans. C'est le "
              "scénario central."),
             ("C. L'inflation fait le travail",
              "Les salaires suivent en partie, les prix affichés stagnent, "
              "l'écart se résorbe sans que personne ne voie de baisse. Le "
              "moins douloureux si tu as un crédit à taux fixe.")]),

    p_duo("bg_village", "ce que B et C disent en commun",
          "Et c'est la seule chose à retenir",
          "Ce qui ne sert à rien",
          [f'Attendre, quand tu {DOIVENT}.',
           "Espérer le prix plein dans dix-huit mois.",
           "Parier sur une plus-value pour rendre l'opération viable."],
          "Ce qui a du sens",
          ["Acheter, si le prix a déjà intégré la baisse.",
           "Viser un bien décoté, bien placé, au cash-flow qui tient.",
           "Et le vendre par quelqu'un qui, lui, doit vendre."]),

    fin("bg_ble", "Le krach à 35 % n'est pas dans les chiffres.",
        "ce qui y est : moins 2 à 4 % par an pendant plusieurs années, et très inégal selon les villes"),
],

# ============================================================================
# SEQUENCE AT — Ce qu'il fait de sa propre maison (reserve, 5 stories)
# Forme : cover > focus > p_formula > p_steps > fin
# ============================================================================
"AT_vendre_dans_un_marche_fige": [
    cover("bg_salon_vide", "il vend une maison en ce moment",
          "Deux agents lui ont dit : ça va être difficile.",
          sub="Voilà exactement ce qu'il a décidé de faire, et pourquoi.",
          hand_bottom=accroche(NUM_LOT + 9)),

    focus("bg_escalier", "la première décision, et elle est contre-intuitive",
          f'Il affiche {ESPERE}, pas celui qu\'il espère.',
          "Dans un marché figé, le prix est fixé par ceux qui doivent vendre. "
          "Afficher son espérance, c'est passer un an à baisser par paliers. "
          "Et ça se voit : un bien qui a baissé trois fois se négocie bien "
          "plus férocement qu'un bien affiché juste dès le départ."),

    p_formula("bg_prairie", "il a chiffré ce que coûte d'attendre",
              "Attendre un an, si le scénario central est le bon",
              "3 à 5 % de prix en moins",
              "plus la taxe foncière, l'entretien, l'assurance, et l'argent qui dort",
              "vendre vite coûte moins cher",
              "Accepter 5 % aujourd'hui pour signer dans trois mois vaut mieux "
              "qu'espérer le prix plein dans dix-huit. S'il se trompe et que "
              "les taux baissent, il aura perdu 5 %."),

    p_steps("bg_cles", "et il change de cible",
            "Les seuls acheteurs qui peuvent signer vite",
            [("Ceux qui n'ont rien à vendre",
              "Les primo-accédants avec un apport, les investisseurs, les "
              "expatriés qui arrivent avec du cash. Ils ne sont pas dans le "
              "bouchon, donc ils ne dépendent de personne."),
             ("Ils sont peu nombreux",
              "Mais dans un marché où plus rien ne bouge, ce sont eux qui "
              "font les ventes."),
             ("Le meublé, lui, a changé de nature",
              f'Il reste rentable là où la demande est structurelle et la '
              f'gestion au cordeau. Mais ce n\'est plus un placement : c\'est '
              f'{METIER}.')]),

    fin("bg_chemin_aube", f'Vendre maintenant n\'est pas une erreur. Vendre {LENTEMENT}, si.',
        f'et les meilleurs achats se font quand les volumes sont bas et les vendeurs {FATIGUES}'),
],

}

SLUG = "banque-14"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
