#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 19 — video du dimanche 04/10/2026 : « Budget 2027 : La fin du regime
reel ? » (ID YouTube bysfkU90VQI). Sous-titres recuperes par le robot.

⚠️ C'EST LA SUITE DIRECTE DE banque-18, ET ELLE LA CORRIGE. La semaine derniere
Sebastien disait « passe au reel, c'est le micro qui est vise ». Cette
semaine, l'article 7 du PLF 2027 s'attaque a l'amortissement, donc au reel.
Il le dit lui-meme : « la regle n'est plus passe au reel systematiquement ».
Cette correction est le coeur de la fournee -- c'est ce qu'il y a de plus
honnete et de plus utile, et ca passe avant les chiffres.

⚠️ URGENCE DATEE. Sebastien demande d'ecrire a son depute AVANT LE 12 OCTOBRE
(c'est en commission des finances que ca se joue). On est le 05/10 : les
stories partent donc le 08 et le 09, soit juste avant. C'est pour ca que cette
fournee prend les jours du reveil du jeudi : les siens (05 et 06) etaient deja
servis, et ce conseil perime le 12.

⚠️ ECARTE, comme toujours (marque LE SOUS LOUEUR) : le channel manager cite
pour le suivi logement par logement, et le logiciel de declaration au reel.

⚠️ CHEVAUCHEMENTS AVEC banque-18, soigneusement evites. Deja traites la-bas :
la lettre du 23 septembre, le tri vote / rejete / rumeur, les prelevements a
18,6 %, la reintegration des amortissements dans la plus-value expliquee de
zero, le micro-BIC a 30 %, le teleservice, et le Jeanbrun en detail. On ne
garde ici que le NEUF : l'article 7 lui-meme, les quatre cas chiffres, le
renversement du conseil, le stock d'amortissement, et le paradoxe de la duree.

    CA — l'article 7, et ce qu'il change (6 stories, jeudi 08/10) ;
    CB — « passe au reel » n'est plus automatique (5, vendredi 09/10) ;
    CC — le detail que personne ne dit (4, reserve).

⚠️ TON. Rien n'est vote, le gouvernement n'a pas de majorite, et Sebastien
donne son pronostic comme « une analyse personnelle ». Les stories le disent
clairement : on informe pour que les gens calculent, pas pour qu'ils vendent.

Rendu : python3 render_stories.py banque-19
"""
from photo_style import (cover, focus, fin, p_steps, p_bars, p_vs, p_duo,
                         p_formula, p_bigstat, p_timeline, acc, write_lot,
                         accroche)

NUM_LOT = 19

# Les apostrophes ne passent pas dans une expression de f-string.
SEPT_MILLE = acc("7 000 € par foyer")
PAR_FOYER = acc("par foyer, pas par bien")
PAS_UN_REFUGE = acc("pas un refuge")
AVANT_LE_12 = acc("avant le 12 octobre")
RIEN_N_EST_VOTE = acc("rien n'est voté")
PLUS_AUTOMATIQUE = acc("n'est plus automatique")
TES_CHIFFRES = acc("tes chiffres")
CINQ_MINUTES = acc("cinq minutes")
PAS_DANS_L_URGENCE = acc("pas dans l'urgence")
MOINS_REPRIS = acc("on t'en reprendra moins")
CEUX_QUI_GARDENT = acc("ceux qui gardent longtemps")
PERDU_EN_2036 = acc("perdu en 2036")

SEQUENCES = {

# ============================================================================
# SEQUENCE CA — L'article 7, et ce qu'il change (jeudi 08/10, 6 stories)
# Forme : cover > p_steps > focus > p_bars > focus > fin
# ============================================================================
"CA_article_7_ce_qui_change": [

    cover("bg_bureau_matin", "budget 2027, déposé le 1er octobre",
          "Cette fois, ce n'est plus le micro qui est visé. C'est le réel.",
          sub="L'article 7 plafonne l'amortissement, c'est-à-dire le cœur même "
              "de l'avantage du meublé. Voici ce que le texte dit, et ce que "
              "ça change pour toi.",
          hand_bottom=accroche(NUM_LOT * 3)),

    p_steps("bg_boites_lettres", "ce que dit le texte",
            "Quatre points, et le troisième est le plus discret",
            [("L'amortissement plafonné à 2,5 % par an",
              f'Et surtout à {SEPT_MILLE} fiscal. Donc {PAR_FOYER} : trois '
              f'appartements, c\'est 7 000 € pour les trois.'),
             ("Meublé de tourisme : 1,5 % et 5 000 €",
              "Plus sévère encore. Et dans sa rédaction actuelle, le texte ne "
              "fait aucune différence entre un meublé classé et un non classé."),
             ("La fin du report",
              "Aujourd'hui, l'amortissement que tu n'utilises pas une année, "
              "tu le gardes pour plus tard, sans limite. Demain, ce qui n'est "
              "pas utilisé dans l'année est perdu."),
             ("Aucune exception pour les biens déjà achetés",
              "Ça s'appliquerait aussi à ceux qui ont investi il y a dix ans "
              "en comptant dessus. Revenus 2027, déclaration au printemps 2028.")]),

    focus("bg_immeuble_dore", "qui n'est pas concerné",
          f'Le statut professionnel échappe au plafond. Ce n\'est pas '
          f'{PAS_UN_REFUGE} pour autant.',
          "Sont exclus du texte : ceux qui sont au micro, puisqu'ils "
          "n'amortissent pas, les loueurs professionnels, et les résidences "
          "étudiantes, senior et EHPAD. Mais le loueur professionnel paie des "
          "cotisations sociales nettement plus lourdes que les 18,6 % de "
          "prélèvements. Basculer pour fuir le plafond peut coûter plus cher "
          "que le plafond."),

    p_bars("bg_escalier_bois", "ce que ça coûte vraiment",
           "Quatre situations, quatre factures",
           [("Petit bien, crédit en cours", 0),
            ("Bien payé, bon loyer", 680),
            ("Courte durée, un seul logement", 1652),
            ("Trois appartements dans le foyer", 3600)],
           note="Impôt supplémentaire par an, tranche à 30 % et prélèvements "
                "à 18,6 %. Ceux qui disent « c'est la fin du meublé » et ceux "
                "qui disent « ça ne change rien » ont tort tous les deux.",
           unite="€/an"),

    focus("bg_fenetre_pluie", "le calendrier, et la seule fenêtre qui compte",
          f'Si tu veux peser, c\'est {AVANT_LE_12}.',
          "Le texte a été déposé le 1er octobre. La partie qui contient "
          "l'article 7 se débat à l'Assemblée du 12 au 19 octobre, avec un "
          "vote le 20. Le budget entier se vote le 17 novembre, puis le Sénat, "
          "pour une adoption espérée mi-décembre. Tout se joue d'abord en "
          "commission des finances : écrire à son député avant le 12 a du "
          "poids quand ça vient de sa circonscription."),

    fin("bg_ciel_dore", f'Et surtout : {RIEN_N_EST_VOTE}.',
        "le gouvernement n'a pas de majorité, sa porte-parole parle d'une « copie de départ » et le ministre de l'économie d'un budget négociable"),
],

# ============================================================================
# SEQUENCE CB — « Passe au reel » n'est plus automatique (vendredi 09/10, 5)
# Forme : cover > p_vs > p_formula > p_duo > fin
# ============================================================================
"CB_le_reel_n_est_plus_automatique": [

    cover("bg_salon_vide", "on se corrige, et c'est important",
          f'« Passe au réel » {PLUS_AUTOMATIQUE}.',
          sub="Dimanche dernier c'était le conseil, parce que seul le micro "
              "était attaqué. Avec l'article 7, la frontière bouge. Le calcul "
              "a été refait, et la réponse surprend.",
          hand_bottom=accroche(NUM_LOT * 3 + 1)),

    p_vs("bg_cuisine_matin", "la frontière a bougé",
         "Quand le réel garde l'avantage, et quand il le perd",
         "Le micro passe devant",
         ["Bien déjà payé",
          "Peu de charges",
          "Un seul logement"],
         "Le réel reste devant",
         ["Un crédit en cours",
          "Des charges élevées",
          "Plusieurs biens"],
         "Parce que le réel, ce n'est pas que l'amortissement : ce sont aussi "
         "tes charges réelles et tes intérêts. Même raboté, il reste gagnant "
         "dans la plupart des cas."),

    p_formula("bg_terrasse", "le calcul qui tranche",
              "Cinq minutes, et tu sais dans quel cas tu es",
              "La valeur de ton bien hors terrain × 2,5 %",
              "ou × 1,5 % si c'est de la courte durée",
              "à comparer au plafond de 7 000 € (ou 5 000 €)",
              "Additionne sur TOUS tes biens avant de comparer : le plafond "
              "est par foyer fiscal. C'est là que ça fait mal pour ceux qui "
              "en ont plusieurs."),

    p_duo("bg_balcon", "dix semaines devant toi",
          "Ce qui se décide maintenant, et ce qui attend",
          "À ne pas faire",
          ["Revendre dans la précipitation : le marché est déjà difficile à la revente, et vendre réveille une plus-value alourdie par les amortissements repris.",
           "Changer de régime tout de suite : tu as jusqu'au printemps 2027 pour choisir, texte voté en main.",
           "Monter une société dans l'urgence : frais, comptabilité, et ça ne se défait pas vite."],
          "À faire",
          ["Le calcul ci-dessus, avec tes vrais chiffres.",
           "Retrouver ton stock d'amortissement sur ta dernière liasse.",
           "Comparer micro et réel pour TON cas, pas en général.",
           "Suivre le vote du 20 octobre."]),

    fin("bg_port", f'La règle, maintenant, c\'est : fais le calcul avec {TES_CHIFFRES}.',
        "plus de conseil qui marche pour tout le monde, la frontière passe désormais au milieu des situations"),
],

# ============================================================================
# SEQUENCE CC — Le detail que personne ne dit (reserve, 4 stories)
# Forme : cover > p_bigstat > p_timeline > fin
# ============================================================================
"CC_le_detail_que_personne_ne_dit": [

    cover("bg_chambre_lumiere", "soufflé par un commentaire, et c'est juste",
          f'Si on te laisse amortir moins, {MOINS_REPRIS}.',
          sub="Les amortissements déduits reviennent dans la plus-value à la "
              "revente. Donc un plafond qui te coûte aujourd'hui te rend une "
              "partie plus tard. Le vrai chiffre est plus petit qu'annoncé.",
          hand_bottom=accroche(NUM_LOT * 3 + 2)),

    p_bigstat("bg_ruelle", "le cas du bien payé avec un bon loyer",
              "Ce que le plafond coûte vraiment",
              "173", "€ par an si tu revends dans les cinq ans, pas 680",
              ["Le plafond te fait amortir 1 400 € de moins par an, donc "
               "680 € d'impôt en plus tout de suite.",
               "Mais c'est aussi 1 400 € de plus-value en moins à la revente, "
               "soit environ 507 € d'impôt économisé.",
               "Seuls les amortissements des murs réellement déduits sont "
               "repris : ceux des meubles et ceux laissés en réserve, non.",
               f'Et plus tu gardes, plus les abattements effacent la '
               f'plus-value : au bout de trente ans, le plafond coûte son '
               f'plein tarif. Cette réforme frappe donc {CEUX_QUI_GARDENT}.']),

    p_timeline("bg_salon_cosy", "l'autre point discret",
               "Ton stock d'amortissement a maintenant une date de péremption",
               [("Jusqu'à fin 2026",
                 "Tout ce que tu n'as pas pu déduire s'empile sans limite de "
                 "durée. C'est ta réserve pour le jour où le crédit est "
                 "remboursé et où le bénéfice apparaît.", None),
                ("À partir de 2027",
                 "Ce stock reste utilisable, mais seulement à hauteur de la "
                 "moitié de ton bénéfice chaque année. Sur 30 000 € de "
                 "réserve et 4 000 € de bénéfice, ça fait 2 000 € par an.", None),
                ("En 2036",
                 "Ce qui n'a pas été utilisé disparaît. Dans l'exemple "
                 "ci-dessus, 20 000 € auront servi, et les 10 000 € restants "
                 "sont perdus.", None)]),

    fin("bg_mer_calme", f'Va vérifier ta dernière liasse : ton stock y est écrit, et il peut être {PERDU_EN_2036}.',
        "c'est l'impôt que tu pensais ne jamais payer, et presque personne n'en parle"),
],

}

SLUG = "banque-19"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
