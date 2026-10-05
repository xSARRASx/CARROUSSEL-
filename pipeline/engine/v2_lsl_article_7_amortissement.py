#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Budget 2027 : la fin du regime reel ?" (05/10/2026, bysfkU90VQI).

Angle coaching : L'ARTICLE 7 DU PROJET DE LOI DE FINANCES 2027, chiffre. Ce que
dit le texte, quatre cas calcules, la frontiere micro/reel qui bouge, le stock
d'amortissement, le calendrier, et ce qu'il ne faut surtout PAS faire.

⛔ PRUDENCES, c'est la video la plus sensible de toute la serie :
  - RIEN N'EST VOTE. C'est un texte DEPOSE le 1er octobre. Sebastien le repete
    du debut a la fin, nous aussi, sur la couverture et dans la legende.
  - Un plafond a 2 % avait deja ete REJETE le 21 novembre 2025 : le precedent
    est rappele, il protege contre la panique.
  - Les trois points qui pourraient bouger sont l'ANALYSE PERSONNELLE de
    Sebastien, pas une prevision. C'est dit tel quel.
  - Les cas chiffres reposent sur des HYPOTHESES explicites : tranche a 30 %,
    prelevements sociaux a 18,6 %, amortissement des murs seulement.
  - Juridiquement, ce n'est PAS une retroactivite : le texte ne vise que les
    revenus 2027. Sebastien le precise, nous aussi.
  - L'appel a ecrire aux deputes, present dans la video, n'est PAS repris : un
    carrousel de marque n'est pas le bon support pour un appel politique. Les
    dates du debat, elles, sont factuelles et restent.
  - Le nom de l'outil de declaration et celui du regime pour la location NUE ne
    sont pas graves : la transcription les ecorche. Ils sont decrits.
  - Aucun commentaire politique : des chiffres, un calendrier, des reserves.

Theme SOMBRE, couverture cover_chiffre (le plafond de 7 000 € porte le sujet),
scene "ardoise" (regle 18 : LSL etait en clair avec une citation le 28/09).

Usage : python3 v2_lsl_article_7_amortissement.py && python3 render.py v2_lsl_article_7_amortissement
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_lsl_article_7_amortissement"

d = Deck("lesousloueur", "sombre")
d.set_bg_photo("lsl_article_7_amortissement_bg.jpg", veil=0.85)

SLIDES = [
    d.cover_chiffre(
        "Le Sous Loueur · Projet de loi de finances",
        "7 000", "€",
        "le plafond annuel d'amortissement envisagé, par FOYER fiscal et non par bien",
        "Article 7 du projet de loi de finances 2027, déposé le 1er octobre. Rien n'est voté."),

    d.checklist(1, "Ce que dit<br>le texte", "Quatre points, et le troisième est le plus discret",
                [(False, "L'amortissement plafonné à 2,5&nbsp;% par an",
                  "De la valeur du bien, et surtout 7 000 € maximum par an et par foyer fiscal. Trois appartements, c'est 7 000 € pour les trois."),
                 (False, "1,5&nbsp;% et 5 000 € pour les meublés de tourisme",
                  "Dans sa rédaction actuelle, le texte ne fait aucune différence entre un meublé classé et un meublé non classé."),
                 (False, "La fin du report",
                  "L'amortissement non utilisé dans l'année serait perdu. Le stock accumulé jusqu'à fin 2026 resterait utilisable jusqu'en 2036, à hauteur de la moitié du bénéfice annuel seulement."),
                 (False, "Aucune exception pour les biens déjà achetés",
                  "Le texte s'appliquerait à tout le monde, y compris à ceux qui ont investi il y a dix ans en comptant sur l'amortissement.")],
                "Qui n'est pas concerné", "Les loueurs au micro, qui n'amortissent pas, les loueurs professionnels, et les résidences étudiantes, seniors et EHPAD.",
                lead="Ce ne sont pas des mesures en vigueur : c'est un texte déposé, qui entre en débat."),

    d.stats(2, "Quatre situations,<br>quatre factures", "Ce que ça coûterait, par an",
            [("0 €", "Un T2 avec un crédit en cours : rien ne change aujourd'hui, mais la réserve disparaît"),
             ("+ 680 €", "Un appartement payé, bien loué, sans crédit"),
             ("+ 1 652 €", "Un seul meublé de tourisme, à cause du taux réduit à 1,5&nbsp;%"),
             ("+ 3 600 €", "Un couple avec trois appartements : c'est le plafond par foyer qui frappe")],
            "Les hypothèses", "Tranche d'imposition à 30&nbsp;% et prélèvements sociaux à 18,6&nbsp;%, soit 48,6&nbsp;%, sur l'amortissement des murs seulement.",
            lead="Ceux qui disent « c'est la fin du meublé » et ceux qui disent « ça ne change rien » ont tort tous les deux."),

    d.flow(3, "Le cas qui<br>fait le plus mal", "Trois appartements dans un même foyer",
           [("450 000 € de base amortissable",
             "27 000 € de loyers, 9 000 € de charges, donc 18 000 € de bénéfice avant amortissement."),
            ("Le taux donnerait 11 250 €",
             "2,5&nbsp;% de 450 000 €. Sauf que le plafond par foyer s'arrête à 7 000 €, et pas un euro de plus."),
            ("L'impôt passe de 1 750 à 5 346 €",
             "L'amortissement est divisé par deux. C'est 3 600 € de plus chaque année, à revenus identiques.")],
           "Ce qui fait la différence", "Ce n'est pas le prix du bien, c'est le NOMBRE de biens dans le foyer. Le plafond ne se multiplie pas.",
           lead="Ceux qui ont construit un petit patrimoine en meublé sont les plus exposés."),

    d.compare(4, "Micro ou réel :<br>la frontière<br>a bougé", "La règle d'il y a huit jours ne tient plus",
              {"head": "Le réel reste devant si", "items": [
                  "Tu as un crédit en cours",
                  "Tes charges réelles sont élevées",
                  "Dans les quatre cas calculés, le réel reste gagnant malgré le plafond",
                  "Le réel, ce n'est pas que l'amortissement : ce sont aussi les intérêts et les charges"]},
              {"head": "Le micro peut repasser devant si", "items": [
                  "Le bien est déjà payé",
                  "Tu as peu de charges et pas de travaux",
                  "Exemple : 150 000 € amortissables loués 1 000 € par mois, le micro redevient meilleur",
                  "Un seul logement, une situation simple"]},
              "La nouvelle règle", "Ce n'est plus « passe au réel systématiquement ». C'est « fais le calcul avec TES chiffres ».",
              lead="Dimanche dernier la réponse était simple. Avec ce texte, elle ne l'est plus."),

    d.pincer(5, "Ce que personne<br>ne regarde", "Le stock et la plus-value",
             ("Ton stock d'amortissement", "Ce que tu n'as jamais consommé ne serait utilisable que jusqu'en 2036, et chaque année à hauteur de la moitié de ton bénéfice. Le reste disparaîtrait."),
             ("La reprise à la revente", "Depuis 2025, les amortissements des murs réellement déduits sont réintégrés dans la plus-value. Amortir moins aujourd'hui, c'est donc aussi se faire reprendre moins demain."),
             ("Le coût réel dépend de la durée", "Sur une revente rapide, le plafond coûte beaucoup moins cher qu'il n'y paraît. Sur une détention longue, il coûte plein tarif."),
             "Le paradoxe", "La mesure pèse surtout sur ceux qui gardent leur bien longtemps, c'est-à-dire exactement ce que l'État dit vouloir encourager.",
             lead="Seuls les amortissements réellement déduits sont repris : pas ceux des meubles, pas le stock inutilisé."),

    d.timeline(6, "Le calendrier<br>du texte", "Et le précédent qui rassure",
               [("1er octobre", "Le texte est déposé",
                 "Le projet de loi de finances pour 2027 arrive au Parlement. Rien n'est voté.", False),
                ("12 au 19 octobre", "La partie recettes est débattue",
                 "C'est là que l'article 7 se joue, amendement par amendement.", True),
                ("20 octobre", "Le vote sur cette partie",
                 "On saura ce que l'Assemblée fait de l'article.", False),
                ("Mi-décembre", "L'adoption espérée",
                 "Après le Sénat. Les deux dernières années, le budget n'a été publié qu'en février suivant.", False)],
               "Le précédent", "Il y a un an, un plafond à 2&nbsp;% avait été proposé, puis rejeté le 21 novembre 2025.",
               lead="Le gouvernement n'a pas de majorité, et sa porte-parole a elle-même parlé d'une copie de départ."),

    d.mindmap(7, "Ce qu'il ne faut<br>surtout PAS faire", "Dix semaines, ça laisse le temps de réfléchir",
              "FAIS LE<br>CALCUL<br>D'ABORD",
              [("Ne revends pas dans la précipitation", "Vendre pour éviter quelques milliers d'euros d'impôt, c'est payer tout de suite une plus-value alourdie, sur un marché déjà grippé."),
               ("Ne change pas de régime maintenant", "Tu auras jusqu'au printemps 2027 pour choisir entre micro et réel, texte voté en main."),
               ("Ne monte pas une société dans l'urgence", "Frais d'immatriculation, suivi comptable : ça coûte cher et ça ne se défait pas vite."),
               ("Fais le calcul en cinq minutes", "Valeur hors terrain multipliée par 2,5&nbsp;% ou 1,5&nbsp;%, additionnée sur tous tes biens, comparée au plafond de 7 000 ou 5 000 €.")],
              "L'autre chose à retrouver", "Ton stock d'amortissement, sur ta dernière liasse fiscale. C'est lui qui dira ce que tu risques de perdre.",
              lead="Sébastien est lui-même concerné : plusieurs biens en meublé, dont de la courte durée."),

    d.cta("Action · 1 mot",
          'Dans lequel<br>des ' + acc("quatre cas") + ' es-tu ?',
          "ARTICLE7",
          "et je t'envoie le calcul à faire avec tes chiffres, plus les dates du débat.",
          "Les trois points qui pourraient bouger sont l'analyse personnelle de Sébastien, pas une prévision."),

    d.closing("Rien n'est voté. "
              + "<em>Mais tout se calcule déjà.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_chiffre")
    noter_theme("lesousloueur", "sombre")
