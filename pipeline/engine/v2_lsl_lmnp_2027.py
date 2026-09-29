#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"LMNP 2027 : ce que le gouvernement prepare" (28/09/2026, U6vGmP7QX1k).

Angle coaching : TRIER AVANT DE DECIDER. Ce qui est deja vote et applique, ce
que dit vraiment la lettre du 23 septembre, ce qui a ete rejete, ce qui n'est
qu'une rumeur, et les quatre decisions a prendre avant decembre.

⛔ PRUDENCES, c'est la video la plus sensible de la serie :
  - La lettre du 23 septembre est un DOCUMENT POLITIQUE, pas un texte de loi.
    Sebastien n'a pas eu le texte integral : il cite les passages relayes par
    la presse. On le dit sur la slide.
  - Le Premier ministre n'est PAS nomme : la transcription automatique ecorche
    son nom, et la lettre se suffit a elle-meme.
  - L'amendement plafonnant l'amortissement a 2 % a ete REJETE (21/11/2025) et
    non repris dans le texte final du 19/02/2026. Jamais le presenter autrement.
  - L'abattement micro qui passerait de 50 a 40 % est une RUMEUR : evoquee,
    jamais ecrite ni adoptee.
  - Le scenario de rapprochement courte duree / longue duree est donne par
    Sebastien comme SON analyse personnelle, pas comme un fait.
  - Le nom du nouveau regime d'amortissement pour la location NUE n'est pas
    grave : la transcription le rend de trois facons differentes. On le decrit.
  - Aucun commentaire politique : on rapporte des faits et un calendrier.

Theme CLAIR, couverture cover_citation, scene "kraft_studio"
(regle 18 : la semaine derniere LSL etait en sombre avec cover_trois).

Usage : python3 v2_lsl_lmnp_2027.py && python3 render.py v2_lsl_lmnp_2027
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_lsl_lmnp_2027"

d = Deck("lesousloueur", "clair")
d.set_bg_photo("lsl_lmnp_2027_bg.jpg", veil=0.83)

SLIDES = [
    d.cover_citation(
        "Le soutien fiscal à la<br>location meublée doit être " + acc("réorienté"),
        "Lettre du 23 septembre aux acteurs du logement",
        "passage cité par la presse"),

    d.stats(1, "Ce qui est déjà<br>voté et appliqué", "La vraie réforme est derrière nous",
            [("18,6&nbsp;%", "Les prélèvements sociaux sur les revenus meublés, contre 17,2&nbsp;% avant"),
             ("15 fév. 2025", "Depuis cette date, les amortissements sont réintégrés dans la plus-value"),
             ("30&nbsp;%", "L'abattement du micro pour un meublé de tourisme NON classé, plafond 15 000 €"),
             ("20 mai 2026", "L'enregistrement des meublés de tourisme sur la plateforme nationale")],
            "Le détail qui pique", "La hausse des prélèvements sociaux s'applique aux revenus perçus depuis le 1er janvier 2025 : la déclaration de ce printemps est déjà concernée.",
            lead="Avant de parler de 2027, regardons ce qui s'applique aujourd'hui, et dont personne n'a parlé."),

    d.flow(2, "La plus-value,<br>en un exemple", "La mesure la plus lourde, et elle est déjà là",
           [("Tu achètes 200 000 €",
             "Au régime réel, tu amortis. Sur la durée de détention, tu as déduit 60 000 € d'amortissement."),
            ("Tu revends 250 000 €",
             "Avant la réforme, la plus-value imposable était la différence : 50 000 €."),
            ("La base devient 110 000 €",
             "Les 60 000 € amortis sont réintégrés. Avec 19&nbsp;% d'impôt et les prélèvements sociaux, on dépasse 36&nbsp;%.")],
           "Ce qui heurte", "La règle s'applique à des investissements faits sous la fiscalité d'avant. C'est ce que beaucoup ont du mal à digérer.",
           lead="Ce n'est pas un projet : c'est en vigueur depuis février 2025."),

    d.compare(3, "La lettre :<br>ce qu'elle dit,<br>ce qu'elle ne dit pas", "Deux phrases, pas une de plus",
              {"head": "Ce qu'on lit partout", "items": [
                  "« C'est la fin du LMNP »",
                  "« Le statut est supprimé »",
                  "« Le régime réel est menacé »",
                  "« Ça s'applique à toute la France »"]},
              {"head": "Ce qui est écrit", "items": [
                  "Le soutien fiscal à la location meublée doit être réorienté",
                  "La courte durée touristique en zone tendue ne doit pas être fiscalement plus avantageuse que la longue durée",
                  "Aucun chiffre, aucune date, jamais le mot supprimé",
                  "La cible nommée, ce sont les centres-villes en zone tendue"]},
              "À lire correctement", "C'est un document politique, pas un texte de loi. Sébastien n'a pas eu le texte intégral : ces passages sont ceux relayés par la presse.",
              lead="Le gouvernement ne dit pas que le meublé doit être moins avantageux. Il dit que la courte durée ne doit pas l'être plus que la longue durée."),

    d.mindmap(4, "Trier en<br>trois colonnes", "Avant de prendre la moindre décision",
              "VOTÉ,<br>REJETÉ,<br>OU RUMEUR",
              [("Voté", "Prélèvements sociaux à 18,6&nbsp;%, amortissements réintégrés dans la plus-value, micro à 30&nbsp;% pour le non classé, enregistrement national."),
               ("Rejeté", "L'amendement qui plafonnait l'amortissement à 2&nbsp;% par an : rejeté le 21 novembre 2025, non repris dans le texte final du 19 février 2026."),
               ("Rumeur", "L'abattement du micro qui passerait de 50 à 40&nbsp;% : évoqué dans des discussions, écrit et adopté nulle part."),
               ("À côté", "Un nouveau régime d'amortissement existe depuis février, mais pour la location NUE seulement. C'est un régime concurrent, pas un remplaçant.")],
              "Ce qu'il faut en retenir", "L'amortissement au réel a déjà survécu à un assaut, et il en est sorti intact.",
              lead="Les titres mélangent les trois colonnes. C'est exactement ce qui pousse à décider trop vite."),

    d.timeline(5, "Le calendrier<br>qui compte", "Rien ne peut arriver avant décembre",
               [("1er octobre", "Présentation du projet de loi de finances",
                 "Le texte pour 2027 est présenté en conseil des ministres.", False),
                ("Octobre et novembre", "Les débats",
                 "C'est là que le contenu réel se décide, amendement par amendement.", True),
                ("Décembre", "L'adoption",
                 "Le vote, ou le recours au 49.3, tombe en fin d'année.", False),
                ("1er janvier 2027", "L'application",
                 "Ce qui aura été adopté, et seulement cela, commence à produire ses effets.", False)],
               "Ce que ça te laisse", "Dix semaines pour agir en connaissance de cause, au lieu de réagir à un titre.",
               lead="Quatre étapes, et aucune ne te touche avant la fin de l'année."),

    d.layers(6, "Micro ou réel :<br>le calcul", "Sur 15 000 € de loyers en meublé longue durée",
             [("Au micro", "Environ 3 650 € par an",
               "Abattement de 50&nbsp;%, donc 7 500 € imposables. Avec une tranche à 30&nbsp;% et 18,6&nbsp;% de prélèvements sociaux, voilà la facture annuelle."),
              ("Au réel", "Souvent zéro pendant des années",
               "Tu déduis les charges réelles, les intérêts d'emprunt, la taxe foncière, et tu amortis le bien. Ce n'est pas une optimisation exotique : c'est le régime normal du meublé."),
              ("Pourquoi si peu y sont", "L'expert-comptable",
               "Pendant des années, le réel voulait dire une liasse fiscale et 500 à 900 € d'honoraires par an. C'est ce coût qui a retenu beaucoup de loueurs au micro.")],
             "Le sens de l'histoire", "Le régime attaqué, c'est le micro. Le régime défendu jusqu'ici, c'est le réel.",
             lead="Le passage au réel est une simple option à formuler auprès des impôts."),

    d.checklist(7, "Les quatre<br>décisions", "À prendre avant décembre",
                [(True, "Si tu es au micro, passe au réel",
                  "C'est le micro qui est dans le viseur, et le réel est de toute façon plus intéressant dans l'immense majorité des cas."),
                 (True, "Si tu fais de la courte durée, fais classer ton meublé",
                  "Quelques centaines d'euros, valable 5 ans : tu passes de 15 000 € et 30&nbsp;% à près de 78 000 € et 50&nbsp;%."),
                 (True, "Vérifie si ta commune est en zone tendue",
                  "La liste est fixée par décret. Deux minutes sur le simulateur du service public suffisent pour le savoir."),
                 (True, "Si tu penses vendre sous 5 ans, calcule ta plus-value maintenant",
                  "Elle dépend du montant amorti et de la durée de détention : exonération d'impôt après 22 ans, de prélèvements sociaux après 30 ans.")],
                "L'angle mort", "Un meublé classé, aligné sur le régime de la longue durée, est précisément ce que la lettre ne vise pas.",
                lead="Quatre décisions, dix semaines, et aucune ne dépend de ce qui sera voté."),

    d.cta("Action · 1 mot",
          'Es-tu dans la cible<br>ou ' + acc("à côté") + ' ?',
          "2027",
          "et je t'envoie le tri en trois colonnes, avec le calendrier et les 4 décisions.",
          "Sébastien donne son analyse du scénario 2027 comme une analyse personnelle, pas comme un fait."),

    d.closing("La réforme du meublé n'est pas devant nous. "
              + "<em>Elle a déjà commencé.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_citation")
    noter_theme("lesousloueur", "clair")
