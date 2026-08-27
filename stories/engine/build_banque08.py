#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 08 — video du 26/08/2026 : comment faire baisser sa taxe fonciere
(ID YouTube h0GZh51rtCk).

⚠️ PROVENANCE : troisieme video d'affilee sans aucun sous-titre sur YouTube,
audio bloque par le mur de 429. Transcription fournie par MARTIN le 27/08/2026.
C'est devenu le canal fiable ; voir le journal d'acces dans stories.md.

⚠️ SAISON : la video dit « je te fais cette video en pleine periode ou la taxe
fonciere est en train d'arriver », environ 30 millions d'avis cette semaine.
Publiee le 27 et 28 aout, elle tombe pile au moment ou les gens ouvrent leur
avis. Elle passe donc AVANT les sequences de reserve, qui sont intemporelles.

    Y — pourquoi ta taxe est peut-etre fausse (6 stories, jeudi) ;
    Z — les cinq erreurs et comment reclamer (5 stories, vendredi).

⚠️ CE QUI N'EST PAS REPRIS, VOLONTAIREMENT :
- le NUMERO de la fiche d'evaluation. La transcription dit « 665 », mais elle
  contient beaucoup d'erreurs de retranscription ailleurs (« lias fiscale »,
  « decrevement »). On dit donc « la fiche d'evaluation », qui est exact et
  sans ambiguite, plutot que de propager un numero peut-etre faux.
- le QUATRIEME coefficient du correctif d'ensemble. La video annonce quatre
  coefficients mais n'en nomme clairement que trois. On ne devine pas.
- l'outil maison cite en fin de video. Comme pour les fournees precedentes, on
  garde le conseil, qui est la vraie valeur.

⚠️ Le reste est 100 % issu de la transcription : aucun pourcentage, aucun
coefficient, aucun delai invente.

Rendu : python3 render_stories.py banque-08
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         acc, write_lot)

ANNEES_70 = acc("années 1970")
FANTOMES = acc("fantômes")
GRATUITE = acc("gratuite")
DEUX_SENS = acc("deux sens")
CATEGORIE = acc("catégorie")
JAMAIS_VUE = acc("jamais vue")

SEQUENCES = {

# ============================================================================
# SEQUENCE Y — Pourquoi ta taxe est peut-etre fausse (jeudi)
# ============================================================================
"Y_taxe_fonciere_fausse": [
    cover("bg_boites_lettres", "les avis arrivent cette semaine",
          "Ta taxe foncière est peut-être fausse.",
          sub="Environ 30 millions de propriétaires reçoivent leur avis en ce "
              "moment. Il repose sur une fiche que presque personne n'a lue.",
          hand_bottom="sur quoi elle est calculée, juste après"),

    focus("bg_documents", "le point de départ de tout le calcul",
          f'Une photo du marché locatif des {ANNEES_70}.',
          "L'administration a estimé, à l'époque, le loyer théorique de ton "
          "bien en le comparant à des logements de référence de ta commune. "
          "Depuis, plus rien n'a été réévalué. Seul un coefficient national "
          "s'applique chaque année, à tout le monde, aveuglément."),

    p_timeline("bg_facade_pierre", "la base est figée, l'addition non",
               "Ce que tu as payé en plus",
               [("En 2023", "Environ 7 % d'augmentation.", None),
                ("En 2024", "Environ 4 % de plus.", None),
                ("L'an dernier",
                 "3,4 % en moyenne. Et certaines communes sont montées à 20, "
                 "25, voire 30 % cette année.", None)]),

    p_bigstat("bg_salon_vide", "sur la fiche de Sébastien",
              f'Les mètres carrés {FANTOMES}',
              "37 m²", "de surface fictive ajoutée, sur un bien de 81 m²",
              ["Chaque équipement de confort ajoute des mètres carrés : eau "
               "courante, électricité, tout-à-l'égout.",
               "Le chauffage central en ajoute par pièce. Chaque baignoire, "
               "douche, lavabo et WC compte séparément.",
               "En 1970 c'était du confort rare. En 2026 tout le monde l'a, "
               "et tout le monde le paie."],
              numsize=140),

    p_steps("bg_escalier", "et le nid à erreurs, ce sont les annexes",
            "Tes mètres carrés ne valent pas tous pareil",
            [("La cave compte pour 20 %",
              "Une cave de 3 m² devient 0,6 m² fiscal, arrondi à 1."),
             ("Le garage et la buanderie, 60 %",
              "Un garage de 16 m², c'est presque 10 m² fiscaux ajoutés à ta "
              "surface."),
             ("Dans les grandes agglomérations, c'est pire",
              "Le coefficient des caves et greniers peut monter à 0,4 voire "
              "0,5. Et la dépendance démolie il y a dix ans, si elle est "
              "encore sur la fiche, tu la paies toujours.")]),

    fin("bg_bureau_matin", f'La fiche d\'évaluation, 99 % ne l\'ont {JAMAIS_VUE}.',
        "elle n'arrive pas avec ton avis, mais elle est gratuite et c'est ton droit"),
],

# ============================================================================
# SEQUENCE Z — Les cinq erreurs et la reclamation (vendredi)
# ============================================================================
"Z_cinq_erreurs_taxe": [
    cover("bg_hall_immeuble", "ce qu'on trouve le plus souvent",
          "Cinq erreurs classiques sur ta fiche.",
          sub="Demande-la au centre des impôts, c'est gratuit, puis compare-la "
              "à ton logement réel.",
          hand_bottom="les cinq, juste après"),

    p_steps("bg_cour", "les trois premières",
            "Celles qui coûtent le plus cher",
            [("La catégorie surclassée",
              "Chaque bien est classé de 1 à 8. Un appartement ordinaire "
              "classé confortable, c'est un tarif au mètre carré plus élevé, "
              "sur tous tes mètres carrés, tous les ans."),
             ("Les équipements fantômes",
              "Une baignoire remplacée par une douche il y a quinze ans, un "
              "bidé disparu, un WC compté deux fois."),
             ("Les annexes surpondérées",
              "Une cave inondée comptée comme saine, un grenier non "
              "aménageable compté comme exploitable.")]),

    focus("bg_village", "les deux dernières, que personne ne pense à vérifier",
          "Ton logement a vieilli, ta fiche non.",
          "Le coefficient d'entretien peut être resté à « bon état » alors que "
          "la façade est fatiguée et l'installation d'origine. Et ta vue "
          "dégagée est peut-être bouchée par un immeuble, ta rue calme devenue "
          "un axe passant. Ces deux-là se contestent, photos à l'appui."),

    p_steps("bg_immeuble_dore", "comment ça se passe concrètement",
            "La réclamation, étape par étape",
            [("Tu découvres l'anomalie toi-même",
              "L'administration ne refait pas l'évaluation spontanément : "
              "l'erreur joue en sa faveur."),
             ("Tu réclames par écrit, avec des preuves",
              "Photos, plans, diagnostics, en t'appuyant sur ta fiche. Tu as "
              "jusqu'au 31 décembre de l'année qui suit ton avis."),
             ("L'administration a six mois pour répondre",
              "Sans réponse ou en cas de refus, le tribunal administratif dans "
              "les deux mois. Et réclamer ne te dispense pas de payer : tu es "
              "remboursé après.")]),

    fin("bg_lac", f'Attention, la révision marche dans les {DEUX_SENS}.',
        "véranda, piscine, salle de bain ajoutée : ta taxe peut monter, vérifie avant de réclamer"),
],

}

SLUG = "banque-08"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
