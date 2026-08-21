#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 06 — « Comment remplir sa liasse fiscale LMNP » (formulaires 2031 et
2033). Video jamais utilisee jusqu'ici.

⚠️ PROVENANCE PARTICULIERE (20/08/2026) : YouTube n'avait ni sous-titres ni
sous-titres automatiques sur cette video, et le telechargement de l'audio
etait bloque par un mur de 429. C'est MARTIN qui a fourni la transcription
directement dans la conversation. Les faits sont conserves dans
`stories/robot/sources/liasse-fiscale-lmnp.md` : si la video redevient
inaccessible, la matiere reste.

⚠️ ANGLE EDITORIAL, ET C'EST UNE DECISION : cette video est un tutoriel de
SAISON FISCALE (la liasse se depose vers le 5 mai). On est en aout, la date
limite est passee depuis longtemps. On l'exploite donc sous l'angle
PREPARATION — ce qui se joue pendant l'annee et qu'on ne rattrape plus en mai
— et JAMAIS sous l'angle « la date limite approche », qui serait faux.

    T — les cinq erreurs qui coutent cher (5 stories) ;
    U — ce qui se prepare toute l'annee (5 stories).

⚠️ Tailles imposees par la grille : 5 stories pour un creneau mardi/vendredi.

⚠️ Contenu 100 % issu de la transcription. Aucun montant, aucun pourcentage,
aucun numero de formulaire invente. Les cases 2042 C Pro sont citees sans dire
laquelle s'applique : la transcription est ambigue sur ce point, on ne devine
pas. Sebastien n'est pas conseiller fiscal et les stories ne promettent rien.

Rendu : python3 render_stories.py banque-06
"""
from photo_style import (cover, focus, fin, p_steps, p_bigstat, acc, write_lot)

DEFICIT = acc("déficit")
REVENU_GLOBAL = acc("revenu global")
TERRAIN = acc("terrain")
DIX_QUINZE = acc("10 à 15 ans")
SIX_ANS = acc("six ans")
MAINTENANT = acc("maintenant")

SEQUENCES = {

# ============================================================================
# SEQUENCE T — Les cinq erreurs (vendredi)
# ============================================================================
"T_cinq_erreurs_lmnp": [
    cover("bg_documents", "location meublée au régime réel",
          "Cinq erreurs qui coûtent cher sur ta déclaration.",
          sub="Elles se jouent pendant l'année, pas au mois de mai. En mai, "
              "il est déjà trop tard pour la plupart.",
          hand_bottom="la première, juste après"),

    focus("bg_bureau_matin", "l'erreur numéro 1, article 39 C",
          f"L'amortissement ne peut pas créer de {DEFICIT}.",
          "Il est limité à tes loyers moins tes charges hors amortissement. "
          "Si tes charges dépassent déjà tes loyers, l'amortissement de "
          "l'année n'est pas déduit : il est reporté. Ce n'est pas perdu, "
          "c'est différé."),

    focus("bg_escalier", "l'erreur numéro 2, la plus fréquente",
          f'Ton déficit ne descend pas dans ton {REVENU_GLOBAL}.',
          "En location meublée non professionnelle, le déficit ne s'impute "
          "que sur tes futurs revenus de location meublée, pendant dix ans. "
          "Seul le loueur professionnel peut le déduire de son revenu global. "
          "C'est du BIC, pas du foncier."),

    p_steps("bg_cour", "les trois autres",
            "Celles qu'on découvre trop tard",
            [("Ne pas ventiler par composant",
              "L'administration attend une décomposition : gros oeuvre, "
              "toiture, électricité, mobilier. Un amortissement global sur la "
              "durée totale du bien n'est pas conforme."),
             ("Oublier l'espace professionnel",
              "Il se crée sur le site des impôts, et l'activation de la "
              "liasse peut prendre plusieurs jours. À faire bien avant."),
             ("Déclarer en retard",
              "De 10 à 40 % de majoration, plus 150 € par formulaire "
              "manquant.")]),

    fin("bg_lac", "Total actif égale total passif.",
        "si les deux ne tombent pas pareil, l'erreur est dans ta comptabilité"),
],

# ============================================================================
# SEQUENCE U — Ce qui se prépare toute l'année (réserve)
# ============================================================================
"U_preparer_toute_annee": [
    cover("bg_salon_cosy", "on est en août, et c'est le bon moment",
          f'Ta déclaration de mai se prépare {MAINTENANT}.',
          sub="Ce qui n'a pas été gardé pendant l'année ne se rattrape pas au "
              "moment de remplir les formulaires.",
          hand_bottom="la liste, juste après"),

    p_steps("bg_boites_lettres", "ce que tu dois garder",
            "Les trois familles de pièces",
            [("Tes recettes",
              "Tous les loyers encaissés, charges récupérables comprises, sur "
              "toutes les plateformes. Le ménage encaissé compte aussi."),
             ("Tes charges",
              "Intérêts d'emprunt, taxe foncière, charges de copropriété, "
              "assurance, CFE, travaux, frais de conciergerie, commissions "
              "des plateformes."),
             ("Tes amortissements",
              "L'acte d'achat, les factures de mobilier avec leurs dates, et "
              "les tableaux de l'année précédente.")]),

    focus("bg_village", "celui que presque tout le monde oublie",
          "Le dépôt de garantie encaissé se déclare.",
          "Même si tu l'as rendu au voyageur, s'il est passé sur ton compte, "
          "il entre dans tes recettes. C'est pour ça qu'il vaut mieux le "
          "bloquer par empreinte bancaire plutôt que de l'encaisser."),

    focus("bg_facade_pierre", "là où l'administration attend les investisseurs",
          f'Le {TERRAIN} ne s\'amortit pas.',
          "Il fait partie du prix du bien, mais il ne rentre pas dans "
          "l'amortissement. Beaucoup minimisent sa part pour grossir le "
          "reste : c'est exactement ce que le contrôle regarde. Un terrain à "
          "10 % dans une grande ville n'est pas crédible."),

    fin("bg_montagne", f'Tes justificatifs se gardent {SIX_ANS}.',
        "six ans après la dernière année où tu utilises l'amortissement"),
],

}

SLUG = "banque-06"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
