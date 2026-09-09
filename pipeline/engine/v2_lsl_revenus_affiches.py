#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Revenus reels vs revenus affiches : le grand mensonge" (v8fzA9JYTHM, 06/09/2026).

Angle coaching : DECODER LES CHIFFRES QU'ON T'AFFICHE. Sujet hors theme location
courte duree, donc regle 14 : Le Sous Loueur, on produit TOUJOURS.

⚠️ REGLE 16 : couverture cover_citation. La derniere LSL etait cover_chiffre.
⚠️ REGLE 15 : legende sous 2000 signes.
⛔ Aucun denigrement nominatif : Sebastien vise des pratiques, jamais des
personnes. On garde exactement cette distance.
⛔ Il dit lui-meme ne pas etre conseiller financier : la slide 7 le reprend.
⛔ Les phrases de la slide de couverture sont REELLEMENT prononcees dans la
video. On n'invente jamais une citation.

Usage : python3 v2_lsl_revenus_affiches.py && python3 render.py v2_lsl_revenus_affiches
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_lsl_revenus_affiches"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_revenus_affiches_bg.jpg", veil=0.88)

SLIDES = [
    d.cover_citation(
        "Les vrais riches,<br>ceux que j'ai pu rencontrer,<br>sont " + acc("invisibles") + ".",
        "Sébastien More", "11 ans d'entrepreneuriat, un dépôt de bilan compris"),

    d.pincer(1, "Un chiffre affiché<br>est une publicité", "La question à se poser",
             ("Ce que tu crois voir", "Le résultat de son travail, la preuve que sa méthode fonctionne."),
             ("Ce que c'est vraiment", "De l'argent que tu lui as donné. La démonstration était le produit, et tu l'as acheté."),
             ("Le test imparable", "Personne ne montre jamais ses pertes. Tu verras toujours les gains, jamais l'autre colonne."),
             "À retenir", "Ce n'est pas de la méchanceté, c'est de la comptabilité.",
             lead="Quand quelqu'un te dit combien il gagne, demande-toi pourquoi il te le dit."),

    d.checklist(2, "Cinq questions<br>qui vident<br>un chiffre", "À poser avant d'y croire",
                [(True, "Est-ce du brut ou du net ?",
                  "Entre les deux, il y a la fiscalité de l'entreprise, la fiscalité personnelle et les charges sociales."),
                 (True, "Est-ce un mois normal, ou LE meilleur mois ?",
                  "Beaucoup annoncent leur record, qui n'a rien à voir avec leur ordinaire."),
                 (True, "Cette somme est-elle partagée ?",
                  "Il y a une différence énorme entre dire que c'est son restaurant et en détenir quelques pour cent."),
                 (True, "Depuis combien de temps ?",
                  "Un excellent mois trois mois après le lancement ne dit rien de ce qui sera répétable.")],
                "La cinquième", "Est-ce récurrent ? Un chiffre seul, sans ces questions, ne veut pas dire grand-chose.",
                lead="Quatre questions, et presque aucun chiffre affiché n'y survit."),

    d.compare(3, "Ce qu'on te montre<br>et ce qui libère", "Deux colonnes qu'on confond",
              {"head": "Ce qu'on exhibe", "items": [
                  "Une voiture, souvent louée pour la vidéo",
                  "Une villa qu'on peut réserver à la nuit",
                  "Une addition de restaurant à 20&nbsp;000&nbsp;€",
                  "Un train de vie qu'il faut refinancer chaque mois"]},
              {"head": "Ce qui rend indépendant", "items": [
                  "Des actifs qui produisent tous les mois",
                  "Un patrimoine qui travaille sans toi",
                  "Des revenus qui financent le train de vie",
                  "Le droit de ralentir sans que rien ne s'écroule"]},
              "La confusion", "Les gens te jugent sur ce que tu possèdes, mais ils ne regardent que les passifs.",
              lead="Ceux qui dépensent tout doivent refournir le même effort chaque mois."),

    d.timeline(4, "Le cercle<br>du paraître", "Il ne s'arrête jamais",
               [("Tu annonces un chiffre", "Le point de non-retour",
                 "À partir de là, tu ne pourras plus jamais faire moins sans perdre ta crédibilité.", False),
                ("L'année suivante", "Il faut au moins l'égaler",
                 "Comment justifier une baisse ? Le marché bouge, mais ton discours ne peut plus bouger.", False),
                ("Tu ne peux plus ralentir", "Ni changer de vie, ni partir",
                 "Si tu cesses de montrer, on trouvera ça bizarre. Alors tu restes au charbon.", False),
                ("Le vrai coût", "Tu es devenu dépendant",
                 "De ton business, de ton image, et de l'effort qu'il faut refaire chaque mois.", True)],
               "L'objectif oublié", "On entreprend pour être indépendant, pas pour se rendre prisonnier d'une image.",
               lead="Quatre étapes, et personne n'en parle avant d'y être."),

    d.layers(5, "Les signes<br>du vrai riche", "Ils ne se voient pas",
             [("Signe 1", "Il a du temps",
               "Celui qui court en permanence et doit aller charbonner n'est pas dans la situation qu'il décrit."),
              ("Signe 2", "Il ne regarde pas son téléphone",
               "Fais le test. Celui qui a tout organisé n'a pas besoin d'être joignable en continu."),
              ("Signe 3", "Il est invisible",
               "Scooter, tongs, tee-shirt. Rien ne laisse deviner ce qu'il possède, parce qu'il n'a rien à prouver.")],
             "La règle", "Le paraître, on ne le paie que quand il rapporte quelque chose.",
             lead="Trois signes, et aucun ne s'affiche sur un profil."),

    d.mindmap(6, "Reconnaître<br>quelqu'un<br>qui a de la valeur", "Sans regarder ses chiffres",
              "Cherche<br>l'ennuyeux,<br>pas l'excitant",
              [("La durée", "Depuis combien de temps il fait vraiment ça, pas depuis quand il en parle."),
               ("Les sujets ennuyeux", "Taxe sur la valeur ajoutée, juridique, règlement de copropriété, fiscalité, paramétrage."),
               ("L'absence d'urgence", "Celui qui a réussi n'a pas besoin que tu achètes. Il ne te met pas la pression."),
               ("L'emploi du temps", "Celui qui filme dans sa voiture trois fois par jour, il travaille quand ?")],
              "Le renversement", "Celui qui ne te parle que de liberté t'excite. Celui qui t'ennuie détient les vraies informations.",
              lead="Quatre signaux, et le plus fiable est le plus ennuyeux."),

    d.flow(7, "La bonne<br>question", "Et quoi faire ensuite",
           [("Arrête de demander combien il gagne",
             "Demande-lui plutôt ce qu'il a arrêté de faire. C'est là que se trouve ce qui te sera utile."),
            ("Ne dépense pas tout",
             "L'erreur à ne surtout pas faire. Le business change, il marchera peut-être moins bien, et la vie a des aléas."),
            ("Place ce que tu gagnes dans le temps",
             "Dans ce qui rapporte dans cinq ou dix ans, pas dans ce qui rapporte vite.")],
           "Honnêteté", "Sébastien le dit lui-même : il n'est pas conseiller financier. Fais tes choix avec un professionnel.",
           lead="Plus tu es jeune, plus tu as le temps de construire."),

    d.cta("Action · 1 mot",
          'Le prochain chiffre qu\'on t\'affiche,<br>tu le ' + acc("crois") + ' ?',
          "INVISIBLE",
          "et je t'envoie la grille de questions à poser avant de croire un chiffre annoncé.",
          "Ne demande plus combien il gagne. Demande ce qu'il a arrêté de faire."),

    d.closing("11 ans de terrain, un dépôt de bilan compris, pour te parler "
              + "<em>sans filtre</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_citation")
