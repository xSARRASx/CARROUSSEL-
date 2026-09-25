#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 17 — video du 24/09/2026 : « Gerer sa location sans etre interrompu »
(ID YouTube 8hotJuvXPuM). Transcription fournie par Martin.

⚠️ SUJET NEUF : c'est de l'ORGANISATION, pas de la fiscalite ni du marche. Les
cinq dernieres fournees etaient toutes l'un ou l'autre. Ca change franchement
de registre, et ca tombe bien.

⚠️ CETTE VIDEO EST EN GRANDE PARTIE UNE DEMONSTRATION DE L'OUTIL MAISON. Il est
cite une quinzaine de fois : le livret d'accueil, l'IA qui repond, les messages
programmes, le pre-checkin, le lien WhatsApp, le compte gratuit, le rendez-vous
avec Camille. TOUT CELA EST ECARTE, comme toujours (marque LE SOUS LOUEUR).
On garde les PRINCIPES, qui valent quel que soit l'outil.
Ecarte aussi : le QR code du livret d'accueil, deja dit dans banque-10 (AG).

⚠️ DEUX SEQUENCES SEULEMENT, la ou la video en donnerait six. Regle de Martin
du 10/09 : mieux vaut court et neuf. Garde ce qui est le plus actionnable et le
plus concret -- les trois niveaux de decision, et l'information qu'on rend
trouvable. Laisse de cote le registre d'observation, le plan sur 30 jours et la
sequence de messages, qui sont bons mais plus attendus.

    AY — les trois niveaux du relais (5 stories, mardi) ;
    AZ — rendre l'information trouvable (5, reserve).

⚠️ Formes differentes entre elles et des fournees precedentes.

Rendu : python3 render_stories.py banque-17
"""
from photo_style import (cover, focus, fin, p_steps, p_duo, p_timeline,
                         acc, write_lot, accroche)

NUM_LOT = 17

# Les apostrophes ne passent pas dans une expression de f-string.
QUARANTE_HUIT = acc("48 heures")
DEPLACE = acc("déplacé la conversation")
ENVELOPPE = acc("une enveloppe")
PAS_TES_ACCES = acc("pas tes accès")
VINGT_DEUX = acc("il est 22 h")
VINGT_CINQ = acc("vingt-cinq lignes")
TROUVABLE = acc("trouvable")
MEME_ENDROIT = acc("au même endroit")
PAS_LE_VOYAGEUR = acc("ce n'est pas le voyageur")

SEQUENCES = {

# ============================================================================
# SEQUENCE AY — Les trois niveaux du relais (mardi, 5 stories)
# Forme : cover > focus > p_steps > focus > fin
# ============================================================================
"AY_trois_niveaux_du_relais": [
    cover("bg_couloir_hotel", "la vraie question à se poser",
          f'Ton logement tourne-t-il {QUARANTE_HUIT} sans toi&nbsp;?',
          sub="Pas « est-ce que je reçois trop de messages ». Celle-là, et "
              "elle se répond avec une page de règles.",
          hand_bottom=accroche(NUM_LOT + 1)),

    focus("bg_table_bois", "l'erreur qu'on fait en déléguant",
          f'Un relais qui t\'appelle à chaque fois, tu as juste {DEPLACE}.',
          "Il est joignable, il est de bonne volonté, mais il demande ton "
          "accord pour tout. Tu restes indispensable à chaque décision. Ce "
          "qui manque, ce n'est pas la personne : c'est écrire noir sur blanc "
          "ce qu'elle peut trancher sans toi."),

    p_steps("bg_mur_beton", "une page, trois niveaux",
            "Ce que ton relais décide, et quand",
            [("Vert : il traite seul",
              "Retrouver une information, expliquer un équipement, appliquer "
              "une règle déjà écrite, remplacer une petite fourniture dans la "
              "limite convenue. Il agit et il garde une trace."),
             ("Orange : dans un créneau annoncé",
              "Une facture, des serviettes propres, du papier toilette pour "
              "demain. Ça ne compromet pas le séjour en cours, donc ça peut "
              "se regrouper."),
             ("Rouge : tout de suite",
              "Voyageur bloqué dehors sans solution, fuite importante, "
              "danger, panne qui rend le logement inutilisable. La procédure "
              "dit qui intervient, qui te prévient, et quand appeler les "
              "secours.")]),

    focus("bg_etagere", "ce qu'il faut lui donner, et ce qu'il ne faut pas",
          f'Une limite de dépense, les contacts. Surtout {PAS_TES_ACCES}.',
          f'Fixe-lui {ENVELOPPE} de cent euros par exemple, et donne-lui les '
          f'coordonnées des professionnels avec qui tu travailles. Il n\'a '
          f'besoin ni de tes identifiants, ni de ta banque. Et pense à '
          f'demander : quelqu\'un qui fait ton ménage n\'a pas '
          f'automatiquement accepté d\'être disponible le soir.'),

    fin("bg_champ_ete", f'Le test qui révèle tout : «&nbsp;{VINGT_DEUX}, le code ne marche pas.&nbsp;»',
        "pose la question à voix haute, tu verras aussitôt s'il lui manque une info, un contact ou une autorisation"),
],

# ============================================================================
# SEQUENCE AZ — Rendre l'information trouvable (reserve, 5 stories)
# Forme : cover > p_duo > p_timeline > focus > fin
# ============================================================================
"AZ_information_trouvable": [
    cover("bg_cafe_table", "avant de déléguer quoi que ce soit",
          "La moitié des appels du soir viennent d'une info mal placée.",
          sub="Elle a bien été envoyée. Elle n'était simplement pas "
              "retrouvable au moment où il en avait besoin.",
          hand_bottom=accroche(NUM_LOT + 5)),

    p_duo("bg_foret_automne", "le message d'accès",
          f'Transmis n\'est pas {TROUVABLE}',
          "Ce qu'on envoie d'habitude",
          [f'Un message de {VINGT_CINQ} envoyé trois jours avant.',
           "Le règlement, le parking, les restaurants, les consignes de "
           "départ. Et le code, quelque part au milieu.",
           "Le voyageur arrive fatigué, une valise dans une main, le "
           "téléphone dans l'autre. Il ne le retrouve pas."],
          "Ce qui marche",
          ["Un message court, séparé : l'adresse, l'heure, l'emplacement "
           "exact de la boîte.",
           "Une photo de la bonne entrée. Une photo plutôt qu'une vidéo : "
           "une vidéo, il faut la regarder en entier.",
           "Et le contact prévu en cas de difficulté."]),

    p_timeline("bg_toits_pluie", "la fiche du logement",
               "Ce que doit savoir celui qui répond à ta place",
               [("Les particularités qui surprennent",
                 "Le sèche-cheveux est dans le tiroir du bas. La deuxième "
                 "couette est dans le placard de l'entrée. La télévision doit "
                 "être sur telle source. C'est ce niveau de détail qui donne "
                 "une réponse utile.", None),
                (f'Et le sèche-cheveux revient toujours {MEME_ENDROIT}',
                 "Sinon la réponse est fausse. La personne qui fait le ménage "
                 "le repose à la même place, à chaque fois.", None),
                ("Ce qui doit sortir du périmètre",
                 "Un équipement cassé, une insatisfaction, une modification "
                 "de réservation, une demande de remboursement. Là, ça "
                 "remonte à un humain, et cet humain doit être prévenu.",
                 None)]),

    focus("bg_neige_douce", "le piège qui se retourne contre toi",
          "Changer un appareil sans changer la fiche.",
          "Tu diffuses alors une mauvaise information, et tu la diffuses très "
          "efficacement, à chaque voyageur. Mettre la fiche à jour fait partie "
          "de l'entretien du logement, au même titre que vérifier un "
          "équipement."),

    fin("bg_rideau", f'Si la même question revient chaque semaine, {PAS_LE_VOYAGEUR}.',
        "c'est l'organisation : un mot de passe mal imprimé, une consigne noyée, ou un vrai problème à réparer"),
],

}

SLUG = "banque-17"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
