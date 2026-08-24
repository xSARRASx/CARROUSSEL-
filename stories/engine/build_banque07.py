#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 07 — video du 16/08/2026 : remplir son calendrier en basse saison sans
brader ses prix (ID YouTube iVd1TQ-GUYs).

⚠️ PROVENANCE : cette video n'a AUCUN sous-titre sur YouTube et le
telechargement de l'audio etait bloque. Elle est restee en retard une semaine.
C'est MARTIN qui a fourni la transcription complete le 24/08/2026.

⚠️ CE N'EST PAS UN DOUBLON. Le titre est presque identique a URH12GYwAuc,
deja traitee le 03/08 (banque-01/A_remplir_sans_baisser). Verifie en comparant
les deux transcriptions : 22 % de mots communs seulement, durees differentes,
sujets differents. URH12GYwAuc = dix techniques generales ; celle-ci = la
BASSE SAISON, d'octobre a mars, avec le bail mobilite en piece maitresse.

⚠️ SAISON : la video dit elle-meme « on est au mois d'aout » et vise octobre a
mars. On la publie fin aout : c'est le bon moment, exactement.

    V — pourquoi brader est un piege, et les remises chirurgicales (6) ;
    W — le bail mobilite, l'arme de l'hiver (5) ;
    X — l'annonce d'hiver et le calendrier des evenements (5, reserve).

⚠️ Tailles imposees par la grille : 6 le lundi, 5 le mardi.
⚠️ Le mot « mandat » est ecarte des textes publies (terme sensible) : on parle
de clients et de proprietaires.
⚠️ Contenu 100 % issu de la transcription. Aucun pourcentage, aucune duree,
aucune loi inventes.

Rendu : python3 render_stories.py banque-07
"""
from photo_style import (cover, focus, fin, p_steps, p_duo, p_bigstat,
                         acc, write_lot)

BRADER = acc("brader")
DES_MOIS = acc("des mois")
FILTRES = acc("filtres")
QUOTA = acc("quota")
DIX_MOIS = acc("dix mois")
COMPTE_DOUBLE = acc("compte double")
PAS_LE_MEME = acc("pas le même")

SEQUENCES = {

# ============================================================================
# SEQUENCE V — Le piege du bradage et les remises chirurgicales (lundi)
# ============================================================================
"V_basse_saison_sans_brader": [
    cover("bg_montagne", "octobre à mars",
          "Ton calendrier d'hiver est vide. Ne baisse pas tes prix.",
          sub="C'est le réflexe de tout le monde, et c'est celui qui coûte le "
              "plus cher. Il existe d'autres leviers.",
          hand_bottom="pourquoi c'est un piège, juste après"),

    focus("bg_bureau_matin", "le piège dont personne ne parle",
          f'Remonter tes prix ensuite prend {DES_MOIS}.',
          "Lissé sur l'année, ton prix moyen nourrit ton positionnement sur la "
          "plateforme. Une annonce qui brade tout l'hiver entraîne "
          "l'algorithme, et les voyageurs, à la voir comme une annonce pas "
          "chère. Ça se paie longtemps après l'hiver."),

    focus("bg_documents", "et le calcul ne tient pas non plus",
          "En basse saison, tu les aurais pris de toute façon.",
          "En août, baisser de 10 % déclenche des réservations parce qu'il y "
          "a du passage et que les gens comparent. En hiver, il y a déjà moins "
          "de monde qui cherche : la remise générale ne crée pas la demande, "
          "elle réduit juste ton prix."),

    p_steps("bg_chemin_aube", "à la place, des remises chirurgicales",
            "Le barème qui protège ton prix",
            [("Au-delà de 30 jours : plein tarif",
              "Ton prix de référence reste intact, c'est lui que la plateforme "
              "retient."),
             ("Entre 30 et 14 jours : remise modérée",
              "On commence à aller chercher les indécis, sans casser le prix "
              "affiché."),
             ("Sous 7 jours et toujours vide : remise agressive",
              "Cette nuit-là ne se louera pas de toute façon. La remise de "
              "dernière minute disparaît dès la date passée : elle ne marque "
              "pas ton prix de référence.")]),

    focus("bg_escalier", "le réglage laissé à zéro par la moitié des annonces",
          f'Les remises longue durée sont des {FILTRES}.',
          "Une remise à la semaine ou au mois n'est pas une ristourne : c'est "
          "ce qui te fait entrer dans les recherches de séjours longs, que "
          "l'algorithme pousse à part. Un mois loué en continu, c'est un seul "
          "ménage au lieu de six et zéro nuit vide."),

    fin("bg_lac", "Ton prix de référence, tu n'y touches pas.",
        "tu joues sur les remises ciblées, les règles de séjour et le type de contrat"),
],

# ============================================================================
# SEQUENCE W — Le bail mobilite (mardi)
# ============================================================================
"W_bail_mobilite": [
    cover("bg_hall_immeuble", "l'arme de l'hiver",
          "Le contrat que presque personne n'utilise.",
          sub="Il existe depuis 2018, il est fait pour la basse saison, et il "
              "ne touche pas à ton compteur de nuitées.",
          hand_bottom="ce que c'est, juste après"),

    focus("bg_facade_pierre", "créé par la loi Elan en 2018",
          "Le bail mobilité, de un à dix mois.",
          "C'est un bail d'habitation meublée, non renouvelable, réservé aux "
          "personnes en situation de mobilité : étudiants, stagiaires, "
          "apprentis, salariés en formation, en mission ou en mutation. "
          "Exactement ceux qui cherchent entre septembre et juin."),

    focus("bg_boites_lettres", "et voilà pourquoi il change tout",
          f'Il ne consomme pas ton {QUOTA}.',
          "En résidence principale, tes nuits en meublé de tourisme sont "
          "plafonnées à 120 jours, 90 dans les plus grandes villes. Un séjour "
          "d'un mois pris sur une plateforme reste du meublé de tourisme et "
          "mange ce quota. Le bail mobilité, lui, n'entre pas dans ce calcul."),

    p_steps("bg_cour", "où trouver ces locataires",
            "Ils ne sont pas sur les plateformes",
            [("Les écoles et les centres de formation",
              "Étudiants, apprentis et stagiaires cherchent de septembre à "
              "juin, pile ta période creuse."),
             ("Les agences d'intérim et les hôpitaux",
              "Missions temporaires, personnel de remplacement, familles de "
              "patients."),
             ("Les gros employeurs et le bâtiment",
              "Mutations, chantiers annoncés dans la presse locale, salariés "
              "en déplacement.")]),

    fin("bg_village", "L'hiver, c'est là que les propriétaires doutent.",
        "arrive avec ton plan déjà prêt plutôt qu'avec une baisse de prix"),
],

# ============================================================================
# SEQUENCE X — L'annonce d'hiver et les evenements (reserve)
# ============================================================================
"X_annonce_hiver": [
    cover("bg_salon_cosy", "ce que presque personne ne change",
          f'Ton client d\'hiver n\'est {PAS_LE_MEME}.',
          sub="Ton annonce, elle, est restée réglée pour l'été. C'est une "
              "partie du problème.",
          hand_bottom="la différence, juste après"),

    p_duo("bg_salon_vide", "deux clients, deux annonces",
          "Ce que tu mets en avant",
          "L'été, et qui ne sert plus",
          ["La terrasse, la plage à côté, le barbecue",
           "La climatisation et les ventilateurs",
           "Des photos lumineuses et estivales"],
          "L'hiver, et qui fait réserver",
          ["L'espace de travail, le parking, le lave-linge",
           "La cuisine équipée et le chauffage bien expliqué",
           "Des photos chaudes, un plaid, un coin lecture"]),

    focus("bg_terrasse", "et attention à la casse",
          f'En basse saison, chaque avis {COMPTE_DOUBLE}.',
          "Il y a moins de rotations, donc chaque avis pèse plus lourd dans ta "
          "moyenne. Un mauvais avis noyé dans quinze réservations d'été passe "
          "inaperçu. Le même en janvier, non. Mieux vaut refuser une arrivée "
          "trop juste que livrer un ménage bâclé."),

    p_steps("bg_ville_doree", "la technique que peu de gens font",
            "Le calendrier des événements de ta ville",
            [("Cherche dès septembre",
              "Salons professionnels, congrès, festivals d'hiver, matchs, "
              "concerts, marchés de Noël. Repère dix à quinze dates."),
             ("Pense aussi aux lieux qui remplissent",
              "Les hôpitaux, les tribunaux, les centres de formation, les gros "
              "chantiers annoncés dans la presse locale."),
             ("Sur ces dates, monte les prix",
              "Et parfois la durée minimum : une foire du mercredi au "
              "dimanche mérite un séjour de trois ou quatre nuits.")]),

    fin("bg_immeuble_dore", "Les outils de prix ne voient pas venir ces dates.",
        "quand ils sentent la demande monter, il est déjà trop tard"),
],

}

SLUG = "banque-07"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
