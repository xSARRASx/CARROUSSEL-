#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 15 — video du 20/09/2026 : « Expatrie : le mythe des 183 jours va te
couter tres cher » (ID YouTube ZdEMuAtcJcE). Transcription fournie par Martin.

⚠️ ELAGAGE. La video repasse sur des choses deja sorties, et Sebastien y renvoie
lui-meme (« rappelez-vous de la video sur les trois signes »). ECARTE :
    - la fiche « Gerer mes biens immobiliers » -> banque-12 (AM) ;
    - l'exoneration de plus-value de la residence principale, le delai d'un an
      et l'arret des 17 mois -> banque-12 (AN) ;
    - les consommations d'electricite croisees -> banque-12 (AL) ;
    - les obligations declaratives LMNP, liasse et amortissements -> banque-06.
VERIFIE : banque-13 ne dit RIEN des expatries (le bonus de fin de video avait
ete ecarte a l'epoque). Le sujet est donc bien neuf.

    AU — les quatre criteres, et pourquoi 183 jours ne protegent pas (6, jeudi) ;
    AV — les deux changements de 2025 (5, vendredi) ;
    AW — teletravail et ancienne maison (5, reserve).

⚠️ TON, et c'est important sur ce sujet-la. Ces stories expliquent une regle et
poussent a PREPARER son depart proprement. Aucune n'explique comment passer
entre les mailles. Sebastien dit lui-meme qu'il n'est pas avocat fiscaliste et
qu'un accompagnement se justifie ici : la derniere story le rappelle, ce n'est
pas une precaution de forme.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : les trois outils maison cites dans
la video sont ECARTES.

Rendu : python3 render_stories.py banque-15
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         p_duo, p_vs, p_formula, acc, write_lot, accroche)

NUM_LOT = 15

# Les apostrophes ne passent pas dans une expression de f-string.
UN_SEUL = acc("un seul suffit")
PAS_BOUCLIER = acc("pas un bouclier")
OU_VIT = acc("où vit l'argent")
PRODUIRE = acc("produire des revenus")
AUGMENTE = acc("augmente")
DIX_ANS = acc("dix ans")
UNE_VOIX = acc("une voix")
ETABLISSEMENT = acc("un établissement stable")
REVIENT = acc("revient")
PREUVES = acc("tes preuves")
AVOCAT = acc("un avocat fiscaliste")

SEQUENCES = {

# ============================================================================
# SEQUENCE AU — Les quatre criteres (jeudi, 6 stories)
# Forme : cover > p_steps > focus > p_vs > focus > fin
# ============================================================================
"AU_quatre_criteres": [
    cover("bg_boites_lettres", "article 4B du code général des impôts",
          f'Les 183 jours, ce n\'est {PAS_BOUCLIER}.',
          sub="Il y a quatre critères de résidence fiscale, et un seul suffit "
              "à te ramener en France. Les jours n'en sont qu'un.",
          hand_bottom=accroche(NUM_LOT + 1)),

    p_steps("bg_table_bois", "les quatre, dans l'ordre du texte",
            f'Quatre critères, et {UN_SEUL}',
            [("Le foyer",
              "Là où vivent ton conjoint et tes enfants. Tu peux passer 300 "
              "jours à l'étranger : si ta famille est à Lyon, ton foyer est à "
              "Lyon."),
             ("Le lieu de séjour principal",
              "Ce sont les fameux 183 jours. Plus de la moitié de l'année en "
              "France, et c'est réglé."),
             ("L'activité professionnelle principale",
              "Là où tu exerces réellement tes fonctions, quel que soit le "
              "pays où tu dors."),
             ("Le centre de tes intérêts économiques",
              "D'où vient l'argent qui te fait vivre.")]),

    focus("bg_terrasse", "le piège de raisonnement",
          "Ce critère ne fonctionne que dans un sens.",
          "Passer plus de 183 jours en France te rend résident fiscal "
          "français, c'est vrai. Mais en passer moins ne te protège de rien "
          "si tu coches l'un des trois autres. Compter ses jours au plus juste "
          "ne sert à rien tant que le reste n'est pas au clair."),

    p_vs("bg_ciel_dore", "deux affaires, deux fois la même conclusion",
         "Ce que les juges ont regardé",
         "Le directeur général",
         ["Sa famille et sa maison étaient en Suisse.",
          "Il n'a passé que 144 jours en France.",
          "Mais le siège de son entreprise était à La Défense, et il y "
          "exerçait réellement ses fonctions."],
         "La cadre partie en Hongrie",
         ["Sa famille vivait là-bas, ses enfants y étaient scolarisés.",
          "Son contrat de travail y était même signé.",
          "Mais ses revenus venaient d'une entreprise française, et elle avait "
          "gardé un appartement à Paris."],
         "Résidence fiscale : la France, dans les deux cas. Le second a été "
         "tranché par la cour administrative d'appel de Paris en janvier 2025."),

    focus("bg_couloir_hotel", "le quatrième critère, le plus redoutable",
          f'Le fisc regarde {OU_VIT}.',
          f'Et le Conseil d\'État a précisé un point que presque personne ne '
          f'connaît : ce qui compte n\'est pas la TAILLE de ton patrimoine en '
          f'France, c\'est sa capacité à {PRODUIRE}. Un patrimoine qui dort ne '
          f'pose pas de problème. Un patrimoine qui te fait vivre, si.'),

    fin("bg_mer_calme", "Ce qui compte, c'est le tableau d'ensemble.",
        "ta famille, ton argent, ton activité : le fisc les regarde ensemble, jamais un seul à la fois"),
],

# ============================================================================
# SEQUENCE AV — Les deux changements de 2025 (vendredi, 5 stories)
# Forme : cover > p_timeline > p_bigstat > focus > fin
# ============================================================================
"AV_ce_qui_a_change_en_2025": [
    cover("bg_chambre_lumiere", "deux nouvelles dont on a très peu parlé",
          "Deux règles ont changé pour les expatriés.",
          sub="L'une allonge de sept ans le temps pendant lequel on peut "
              "contester ton départ. L'autre est passée à une voix près.",
          hand_bottom=accroche(NUM_LOT + 5)),

    p_timeline("bg_fenetre_pluie", "loi de finances 2025",
               "Le délai pour contester ton départ",
               [("Avant : environ trois ans",
                 "Passé ce délai sans nouvelle, l'affaire était close.", None),
                ("Depuis 2025 : dix ans",
                 "En cas de ce que l'administration appelle une fausse "
                 "domiciliation à l'étranger.", None),
                ("Ce que ça change concrètement",
                 f'Si tu pars en 2026, tu peux recevoir un courrier jusqu\'en '
                 f'2036. Garde {PREUVES} pendant {DIX_ANS} : baux, factures, '
                 f'billets d\'avion, relevés, inscriptions scolaires.', None)]),

    p_bigstat("bg_ruelle", "octobre 2025, amendement au budget",
              "L'impôt universel a failli passer",
              "1 voix", "d'écart sur 577 députés : 131 pour, 132 contre",
              ["Il proposait d'imposer les Français partis vers des pays à "
               "fiscalité faible pendant dix ans après leur départ, sur leurs "
               "revenus mondiaux.",
               "C'est le modèle américain, en place là-bas depuis plus d'un "
               "siècle.",
               "Il a été rejeté. Mais il revient chaque année depuis 2019, "
               "avec un peu plus de soutien à chaque fois."],
              numsize=170),

    focus("bg_salon_cosy", "ce que ça veut dire pour un projet de départ",
          f'Ce n\'est plus une hypothèse : ça {REVIENT} tous les ans.',
          "Vu l'état des finances publiques et le nombre de départs, c'est un "
          "paramètre à intégrer maintenant, pas dans cinq ans. Non pas pour "
          "renoncer, mais pour construire un départ qui tienne debout si la "
          "règle change."),

    fin("bg_neige_douce", f'Sur ce sujet, {AVOCAT} se justifie vraiment.',
        "Sébastien le dit lui-même : il partage son expérience, il ne remplace pas un conseil qui engage sa responsabilité"),
],

# ============================================================================
# SEQUENCE AW — Teletravail et ancienne maison (reserve, 5 stories)
# Forme : cover > p_duo > p_formula > focus > fin
# ============================================================================
"AW_teletravail_et_maison": [
    cover("bg_cuisine_matin", "deux situations très courantes",
          "Télétravailler depuis l'étranger, ou garder sa maison.",
          sub="Les deux sont possibles. Les deux sont des champs de mines si "
              "on les improvise.",
          hand_bottom=accroche(NUM_LOT + 9)),

    p_duo("bg_balcon", "le télétravail depuis l'étranger",
          "Le principe, et les trois pièges",
          "Ce qui est simple",
          ["Ton salaire est imposable là où le travail est physiquement "
           "exercé.",
           "Depuis Lisbonne, le travail est exercé au Portugal.",
           "Sous réserve de la convention fiscale entre les deux pays."],
          "Ce qui l'est beaucoup moins",
          ["Chaque jour travaillé en France est imposable en France, et ils "
           "sont comptés un par un.",
           "Si ton salaire français est ton seul revenu, tu retombes dans le "
           "centre des intérêts économiques.",
           f'Et ta présence peut créer {ETABLISSEMENT} pour ton employeur : '
           f'c\'est pour ça que beaucoup d\'entreprises refusent.']),

    p_formula("bg_escalier_bois", "l'ancienne résidence principale",
              "Elle change de statut le jour où tu pars",
              "Elle devient une résidence secondaire",
              "donc la taxe d'habitation revient, en plus de la taxe foncière",
              "majorée jusqu'à 60 %",
              "En zone tendue. « Je la garde au cas où je reviendrais » a donc "
              "un prix, et il tombe chaque année."),

    focus("bg_port", "et à la revente, le calcul change aussi",
          "Pour un non-résident, l'exonération est plafonnée.",
          "Il existe une exonération spécifique, mais elle s'arrête à "
          "150 000 € de plus-value et sous conditions. Au-delà, l'impôt "
          "s'applique. Sur un bien parisien avec 300 000 € de plus-value "
          "vendu deux ans après le départ, Sébastien chiffre la note autour "
          "de 50 000 €."),

    fin("bg_plage_aube", "Partir n'allège pas l'impôt sur tes loyers français.",
        "en non-résident, le taux part d'un minimum de 20 % et monte à 30 % au-delà d'environ 29 000 €"),
],

}

SLUG = "banque-15"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
