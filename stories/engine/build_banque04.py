#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 04 — video du 09/08/2026 : les obligations de la rentree pour les
bailleurs en meuble (ID YouTube JgFFL6no9OQ).

⚠️ Le titre YouTube est traduit en anglais ("Furnished Property Landlords:
These September Requirements Will Change Everything") : seule la transcription
francaise fait foi. Vrai titre : « Bailleur meuble : ces obligations de
septembre vont tout changer ».

Video RICHE (4 210 mots) : trois blocs nets, donc trois sequences.
Contenu 100 % issu de la transcription : aucun chiffre, aucune date, aucun
numero de rapport invente.

    O — la facturation electronique au 1er septembre, et la confusion
        assujetti / redevable qui fait dire n'importe quoi (6 stories) ;
    P — la menace 2027 : le rapport parlementaire qui vise l'amortissement
        (5 stories) ;
    Q — les trois verifications de rentree (4 stories).

⚠️ LES TAILLES SUIVENT LA GRILLE, sinon livraison.py coupe les sequences.
La grille (planning.py) donne 6 creneaux le jeudi et 5 le vendredi : la
sequence du jeudi fait donc 6 stories, celle du vendredi 5. C'est l'ordre
alphabetique qui decide du jour, d'ou la facturation en O : son echeance est
le 1er septembre, elle passe en premier. Erreur commise puis corrigee le
13/08/2026 : des sequences de 7 et 6 avaient ete coupees en deux jours.

La sequence Q ne fait que 4 stories, volontairement : dans la video ce bloc
est un rappel rapide, et l'un de ses points (le reglement de copropriete) a
deja eu sa sequence complete dans banque-03. On ne remplit pas pour faire
du volume. Elle part en reserve, faute de creneau dans cette fournee.

⚠️ La marque ici est LE SOUS LOUEUR (@moresebastien). La video cite les outils
maison, on ne les reprend PAS dans les stories : on garde le conseil, qui est
la vraie valeur, et le cloisonnement des marques.

Rendu : python3 render_stories.py banque-04
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         p_duo, acc, write_lot)

o = acc

# Les apostrophes ne passent pas dans une expression de f-string : on sort les
# morceaux accentues ici (meme precaution que dans build_banque03.py).
AMORTISSEMENT = acc("amortissement")
IMPOSABLE = acc("imposable")
PAS_UNE_LOI = acc("pas une loi")
SIREN = acc("SIREN")
REDEVABLE = acc("redevable")
RECEVOIR = acc("recevoir")
DIX_MINUTES = acc("dix minutes")
FACTUREZ = acc("facturez")
TROIS_CHOSES = acc("Trois choses")
PERDU = acc("perdu")

SEQUENCES = {

# ============================================================================
# SEQUENCE O — La facturation electronique au 1er septembre (jeudi)
# ============================================================================
"O_facture_electronique": [
    cover("bg_boites_lettres", "au 1er septembre 2026",
          f'Si tu as un numéro de {SIREN}, tu es concerné.',
          sub="Beaucoup se croient hors du coup parce qu'ils ne facturent "
              "jamais de TVA. C'est l'erreur qui circule le plus.",
          hand_bottom="la subtilité, juste après"),

    focus("bg_cour", "la nuance que presque personne ne fait",
          f"Assujetti n'est pas {REDEVABLE}.",
          "Louer en meublé est une activité économique : tu es assujetti à la "
          "TVA. L'exonération porte sur tes loyers, pas sur ton statut "
          "d'opérateur économique. Le seul qui échappe à la réforme, c'est "
          "celui qui n'a aucun SIREN."),

    p_duo("bg_facade_pierre", "le tri entre les bêtises et le réel",
          "Ce qui circule, et ce qui est vrai",
          "Ce qu'on lit partout",
          ["Exonéré de TVA, donc pas concerné",
           "Il te faut un logiciel de facturation à 30 € par mois",
           "Tu vas devoir émettre des factures à tes voyageurs"],
          "Ce qui est vrai",
          ["Un SIREN suffit à te mettre dans le circuit",
           "L'émission ne concerne que les redevables de la TVA",
           "Toi, tu dois pouvoir recevoir, et c'est tout"]),

    p_steps("bg_salon_cosy", f'à faire en {DIX_MINUTES}',
            f'Se mettre en règle pour {RECEVOIR}',
            [("Choisis une plateforme agréée",
              "Il en existe beaucoup : des banques, des outils spécialisés, "
              "ou ton expert-comptable."),
             ("Enregistre-toi",
              "Tu signes un mandat et tu apparais dans l'annuaire national."),
             ("Vérifie que tu es joignable",
              "Sans raccordement, tes factures ne te parviennent plus : tu es "
              "injoignable dans le circuit.")]),

    focus("bg_hall_immeuble", "les conciergeries, c'est différent",
          f'Vous, vous {FACTUREZ}.',
          "Une conciergerie émet des factures, parfois avec de la TVA. Même "
          "en franchise de base, elle reste assujettie. Le sujet est donc "
          "bien plus urgent pour elle que pour le propriétaire qui loue à des "
          "particuliers."),

    fin("bg_ciel_dore", "Une tolérance est annoncée au démarrage.",
        "pas d'amende le 2 septembre, mais ça prend dix minutes"),
],

# ============================================================================
# SEQUENCE P — La menace 2027 sur l'amortissement (vendredi)
# ============================================================================
"P_amortissement_vise": [
    cover("bg_documents", "rapport déposé le 8 juillet 2026",
          f'Ton {AMORTISSEMENT} est dans le viseur.',
          sub="Une commission d'enquête de l'Assemblée nationale recommande "
              "noir sur blanc de s'attaquer à l'avantage numéro 1 du meublé.",
          hand_bottom="ce qu'il dit vraiment, juste après"),

    p_bigstat("bg_bureau_matin", "le constat qui a mis le feu",
              "Le chiffre qui a lancé la commission",
              "13 553", "ménages soumis à l'impôt sur la fortune immobilière",
              ["Aucun impôt sur le revenu payé en 2024.",
               "Politiquement, ça résonne : les députés cherchent comment "
               "c'est possible.",
               "En remontant les mécanismes d'optimisation, ils tombent sur "
               "la location meublée."],
              numsize=170),

    p_timeline("bg_escalier", "ce n'est pas un coup isolé",
               "Le tour de vis, étape par étape",
               [("Le micro-BIC durci",
                 "Plafond ramené à 15 000 €, abattement à 30 % au lieu de "
                 "50 %. Le meublé devient moins intéressant que la location "
                 "nue.", None),
                ("La loi Le Meur",
                 "Les amortissements sont réintégrés dans le calcul de la "
                 "plus-value à la revente, pour l'immobilier de tourisme.",
                 None),
                ("Le rapport du 8 juillet 2026",
                 "Il recommande de plafonner les taux d'amortissement "
                 "eux-mêmes, au régime réel.", None)]),

    focus("bg_terrasse", "si les taux sont plafonnés",
          f'Tu deviens {IMPOSABLE} des années plus tôt.',
          "L'amortissement est une charge qui ne sort jamais de ta poche : "
          "souvent 4 000 à 6 000 € par an pour un bien à 200 000 €. C'est lui "
          "qui met ton résultat fiscal à zéro les huit premières années. "
          "Plafonne les taux, et l'impôt arrive au bout de trois ou quatre."),

    p_duo("bg_lac", "garde la tête froide",
          f"C'est un rapport, {PAS_UNE_LOI}",
          "À ne pas faire",
          ["Tout arrêter ou tout restructurer dans l'urgence",
           "Se dépêcher de revendre avant qu'il soit trop tard",
           "Payer un abonnement à quelqu'un qui te vend la peur"],
          "À faire dès maintenant",
          ["Savoir combien d'amortissement tu passes par an",
           "Simuler ce que donneraient des taux plafonnés",
           "Attendre le budget : rien ne bouge avant fin décembre"]),
],

# ============================================================================
# SEQUENCE Q — Les verifications de rentree (reserve)
# ============================================================================
"Q_rentree_verifications": [
    cover("bg_chemin_aube", "rentrée 2026",
          f'{TROIS_CHOSES} à vérifier avant septembre.',
          sub="Elles n'ont rien à voir entre elles, et chacune peut te coûter "
              "cher si tu la laisses passer.",
          hand_bottom="la liste, juste après"),

    p_steps("bg_village", "la liste de rentrée",
            "Les trois vérifications",
            [("Ton numéro d'enregistrement national",
              "Obligatoire depuis mai 2026, auprès de ta mairie ou du site "
              "officiel. Beaucoup de communes ne sont pas encore prêtes, mais "
              "prends les devants."),
             ("Le plafond de nuitées de ta commune",
              "Il a pu passer de 120 à 90 nuits. La décision est locale : "
              "vérifie la tienne."),
             ("L'assemblée générale de ta copropriété",
              "Elles tombent fin août et début septembre, avec parfois une "
              "interdiction de louer en courte durée à l'ordre du jour.")]),

    focus("bg_salon_vide", "sur l'ordre du jour d'une assemblée",
          f'Mis au vote ne veut pas dire {PERDU}.',
          "Beaucoup lâchent dès qu'ils voient le sujet arriver. C'est une "
          "erreur : encore faut-il savoir lire et interpréter un règlement de "
          "copropriété. Il existe des sorties, même quand le vote est passé."),

    fin("bg_montagne", "Vouloir changer une vie c'est bien. Le faire, c'est mieux.",
        "tout est détaillé dans la vidéo, sur la chaîne"),
],

}

SLUG = "banque-04"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
