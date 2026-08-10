#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Loueurs en meuble : ces obligations de septembre vont tout changer" (09/08/2026).

Angle coaching : trois echeances de rentree, ce qui est VRAIMENT obligatoire,
et la menace 2027 sur l'amortissement (rapport parlementaire 3056).
Ton : sans panique, on separe ce qui est vote de ce qui ne l'est pas.

Usage : python3 v2_lsl_rentree_fiscale.py && python3 render.py v2_lsl_rentree_fiscale
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_rentree_fiscale"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_rentree_fiscale_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Ta rentrée de bailleur<br>en ' + acc("meublé"),
        "Ce qui devient obligatoire au 1er septembre, et ce qui se prépare pour 2027",
        "Sans panique : on sépare ce qui est voté de ce qui ne l'est pas."),

    d.layers(1, "Trois échéances<br>pour la rentrée", "Par ordre d'urgence",
             [("1er septembre", "La facturation électronique",
               "Tu dois pouvoir RECEVOIR des factures électroniques. C'est le seul vrai geste à faire."),
              ("Automne 2026", "Le projet de loi de finances 2027",
               "C'est là qu'une recommandation sur l'amortissement peut devenir un article de loi."),
              ("Fin août, septembre", "Les assemblées générales de copropriété",
               "La saison des votes, et parfois des demandes d'interdiction de la courte durée.")],
             "À retenir", "Une seule de ces trois échéances demande une action immédiate.",
             lead="Trois sujets arrivent en même temps, mais ils n'ont pas la même urgence."),

    d.compare(2, "Ce qu'on te raconte<br>sur la facturation", "Deux discours, deux erreurs",
              {"head": "Les deux intox qui circulent", "items": [
                  "Tu n'es pas concerné parce que tu es exonéré de taxe sur la valeur ajoutée",
                  "Il te faut vite un logiciel à 20 ou 30&nbsp;€ par mois",
                  "Tu vas devoir émettre des factures pour chaque séjour",
                  "Tu risques une amende dès le 2 septembre"]},
              {"head": "Ce qui est vrai", "items": [
                  "Si tu as un numéro SIREN, tu es concerné, point",
                  "Aucun logiciel obligatoire : l'enregistrement suffit",
                  "Aucune facture à émettre si tu loues à des particuliers",
                  "L'administration a annoncé une tolérance au démarrage"]},
              "Le vrai geste", "T'enregistrer sur une plateforme agréée pour pouvoir recevoir. C'est tout.",
              lead="Beaucoup vendent de la peur pour vendre un abonnement."),

    d.pincer(3, "Assujetti<br>ou redevable", "La subtilité que tout le monde rate",
             ("Assujetti", "Ta location meublée est une activité économique : avoir un SIREN suffit."),
             ("Redevable", "Tu ne paies la taxe que si tu fournis les services de para-hôtellerie."),
             ("Tu es assujetti sans être redevable", "L'exonération porte sur tes loyers, jamais sur ton statut d'opérateur économique."),
             "La conséquence", "Tu n'as jamais collecté un centime, et tu es quand même dans le champ de la réforme.",
             lead="Deux mots que l'on confond, et qui décident si tu es concerné."),

    d.flow(4, "Se mettre en règle<br>en dix minutes", "Pour le 1er septembre",
           [("Choisis une plateforme agréée",
             "Ta banque, ton expert comptable, ton outil de gestion : il y en a partout."),
            ("Enregistre ton numéro SIREN",
             "C'est ce qu'on appelle s'enrôler : tu entres dans l'annuaire national."),
            ("Tu peux recevoir",
             "Les factures de ta conciergerie, de tes artisans, de ton comptable arrivent.")],
           "Le rappel", "Une facture électronique n'est pas un PDF envoyé par courriel : c'est un fichier structuré.",
           lead="Trois étapes, et le sujet est réglé pour de bon."),

    d.timeline(5, "Comment l'étau<br>s'est resserré", "En trois temps",
               [("Micro-BIC", "Le régime simplifié durci",
                 "Plafond ramené à 15&nbsp;000&nbsp;€, abattement passé de 50 à 30 pour cent.", False),
                ("Loi Le Meur", "Les amortissements réintégrés",
                 "Ils reviennent dans le calcul de la plus-value à la revente pour le tourisme.", False),
                ("8 juillet 2026", "Le rapport parlementaire 3056",
                 "Il recommande de plafonner les taux d'amortissement au régime réel.", True),
                ("Automne", "Le budget 2027",
                 "La recommandation peut devenir un amendement, puis un article de loi.", False)],
               "Le schéma", "On nous a poussés vers le réel, et c'est le réel qu'on regarde maintenant.",
               lead="Chaque étape est un petit ajustement technique. Mises bout à bout, elles changent tout."),

    d.stats(6, "Ce que le plafonnement<br>changerait", "Sur un bien à 200 000 €",
            [("4 à 6 000 €", "L'amortissement déductible par an aujourd'hui, sans sortir de ta poche"),
             ("8 ans", "La durée pendant laquelle beaucoup affichent un résultat fiscal à zéro"),
             ("3 ou 4 ans", "Ce que cette durée pourrait devenir si les taux étaient plafonnés"),
             ("13 553", "Les ménages soumis à l'impôt sur la fortune immobilière qui ont déclenché le rapport")],
            "Ce qui change vraiment", "Pas la viabilité de l'investissement, mais sa rentabilité nette sur toute sa durée.",
            lead="Ton résultat imposable n'apparaîtrait pas plus fort, mais bien plus tôt."),

    d.checklist(7, "Ce qu'il faut faire<br>et ne pas faire", "Face à la menace 2027",
                [(False, "Tout restructurer dans l'urgence",
                  "Rien n'est voté. C'est un rapport, pas une loi, et même pas encore un projet de loi."),
                 (False, "Revendre avant qu'il soit trop tard",
                  "Il ne se passera rien avant le vote du budget, fin décembre au plus tôt."),
                 (True, "Connaître tes chiffres",
                  "Combien d'amortissement tu passes par an, et ce que ça donnerait avec des taux plafonnés."),
                 (True, "Raisonner en rentabilité nette",
                  "Sur l'ensemble du projet, de la date d'entrée à la date de sortie, pas au cash-flow annuel.")],
                "Le réflexe", "Une simulation avec ton expert comptable vaut mieux que dix avis sur un groupe Facebook.",
                lead="La bonne réaction n'est ni de paniquer, ni d'ignorer le sujet."),

    d.cta("Action · 1 mot",
          'Ta rentrée est-elle<br>vraiment ' + acc("prête") + ' ?',
          "RENTREE",
          "et je t'envoie la checklist des trois échéances, point par point.",
          "Dix minutes suffisent pour être en règle au 1er septembre."),

    d.closing("11 ans de terrain pour t'aider à décider "
              + "<em>sur des faits</em>, pas sur des rumeurs."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
