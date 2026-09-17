#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Faut-il encore investir dans l'immobilier en 2026 ?" (17/09/2026, iIO-RH_doLo).

Angle coaching : LIRE LE MARCHE AVEC LES VRAIS CHIFFRES. Sebastien s'appuie sur
deux sources publiques qu'il cite nommement : le tableau de bord Credit Logement
d'aout et les courbes de Friggit. Le fil : le marche n'est pas mort, il est FIGE,
l'ajustement a deja commence en 2022 et il sera lent.

⛔ Prudences graves pour cette video :
  - Aucun krach annonce : Sebastien dit explicitement qu'un -35 % en deux ans
    n'est PAS dans les chiffres, et que la dette des menages exclut le scenario
    americain de 2008. Ne jamais durcir son propos.
  - Les trois scenarios sont des SCENARIOS, pas des previsions. Le scenario B est
    presente comme central par Sebastien, pas comme certain.
  - Sebastien n'est ni economiste ni conseiller financier : il lit des donnees
    publiques et raconte ce qu'il fait de sa propre maison, qu'il vend.

Couverture : cover_aplat (la question de la video, posee a plat).
Semaine derniere LSL = cover_chiffre, donc rotation respectee (regle 16).

Usage : python3 v2_lsl_immobilier_2026.py && python3 render.py v2_lsl_immobilier_2026
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_lsl_immobilier_2026"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_immobilier_2026_bg.jpg", veil=0.88)

SLIDES = [
    d.cover_aplat(
        "Le Sous Loueur · Marché 2026",
        "Faut-il encore acheter<br>de l'immobilier ?",
        "Les vrais chiffres du tableau de bord Crédit Logement et des courbes de Friggit. Le marché n'est pas mort : il est figé."),

    d.stats(1, "Le décor,<br>en quatre chiffres", "Août 2026",
            [("3,31&nbsp;%", "Le taux moyen relevé en août, contre 3,23&nbsp;% de février à juin"),
             ("1,55", "Le rapport prix sur revenus, quand le couloir historique est à 1"),
             ("0,91", "Le rapport loyers sur revenus : les loyers n'ont jamais quitté le couloir"),
             ("0,74", "Le pouvoir d'achat immobilier : 26&nbsp;% de logement en moins qu'en 2000")],
            "Le problème de l'investisseur", "Les prix ont fait plus 55&nbsp;% pendant que les loyers faisaient moins 9&nbsp;%. Le rendement s'est écrasé entre les deux.",
            lead="Deux sources publiques, reçues chaque mois : Crédit Logement et les courbes de Friggit."),

    d.flow(2, "Pourquoi les prix<br>sont montés<br>si haut", "Deux mots : les taux et la durée",
           [("En 2000, tu empruntais à 5&nbsp;% sur 15 ans",
             "Le montant que la banque acceptait de prêter était contraint par les deux bouts."),
            ("En 2021, à 1&nbsp;% sur 25 ans",
             "À mensualité égale, tu pouvais emprunter presque le double. Le crédit est devenu presque gratuit."),
            ("Aujourd'hui, les deux leviers sont bloqués",
             "3,31&nbsp;% et ça remonte depuis juin, et la moitié des prêts sont déjà à 25 ans, plafond fixé par la Banque de France.")],
           "Ce que ça veut dire", "Les prix n'ont pas monté parce que les Français se sont enrichis. La hausse des prix, c'est de la dette transformée en prix.",
           lead="Les deux réservoirs qui ont porté les prix pendant 20 ans sont vides aujourd'hui."),

    d.pincer(3, "Pourquoi le marché<br>bloque avant<br>de baisser", "Le bouchon",
             ("Le vendeur perd des deux côtés", "S'il vend 50 000 € de moins qu'espéré, il perd aussi 50 000 € d'apport pour son projet suivant. Alors il ne vend pas."),
             ("La chaîne s'arrête", "Celui qui devait lui vendre une maison ne vend pas non plus, et ne peut donc pas acheter à son tour."),
             ("954 000 ventes sur 12 mois", "Pour une normale un peu supérieure au million : le marché tourne à 91&nbsp;% de son régime, figé plutôt que mort."),
             "La conséquence", "Dans un marché figé, le prix est fixé par ceux qui DOIVENT vendre : succession, divorce, mutation, difficulté.",
             lead="Un seul maillon qui refuse de baisser, et c'est toute la chaîne qui s'immobilise."),

    d.compare(4, "Ce qu'on entend<br>et ce que<br>disent les chiffres", "Le tri",
              {"head": "Les vidéos catastrophe", "items": [
                  "Un krach de moins 35&nbsp;% arrive",
                  "L'effondrement est devant nous",
                  "Il faut attendre que ça reparte",
                  "Ce sera comme les États-Unis en 2008"]},
              {"head": "Ce qui est dans les données", "items": [
                  "Plutôt moins 2 à 4&nbsp;% par an, et très inégal selon les villes",
                  "La baisse a commencé en 2022 : le pic était à 1,84, on est à 1,55",
                  "Revenir au couloir par les seuls revenus prendrait plus de 15 ans",
                  "La dette des ménages est à 76&nbsp;% du revenu disponible, contre 200&nbsp;% aux Pays-Bas"]},
              "Ce qui en découle", "Pas de bombe de crédit en France, donc pas de ventes forcées massives, donc pas de krach à l'américaine.",
              lead="L'ajustement n'est pas devant nous : il est en cours depuis quatre ans, simplement très lent."),

    d.layers(5, "Les trois<br>scénarios", "Ce sont des scénarios, pas des prévisions",
             [("Scénario A", "Les taux baissent",
               "Le marché se débloque, les prix se stabilisent. Il faudrait que l'État réemprunte à 3&nbsp;%. Peu probable dans les deux ans."),
              ("Scénario B", "Les taux restent hauts",
               "Vers 4&nbsp;%, la capacité d'emprunt perd encore 5 à 7&nbsp;%. Moins 10 à 20&nbsp;% sur 3 à 5 ans, très inégal. Le scénario central."),
              ("Scénario C", "L'inflation fait le travail",
               "Si elle repart à 4 ou 5&nbsp;%, les salaires suivent en partie, les prix affichés stagnent, et le ratio baisse sans baisse visible.")],
             "Le point commun de B et C", "Attendre ne sert à rien à celui qui doit vendre, et acheter n'a de sens que si le prix a déjà intégré la baisse.",
             lead="L'État emprunte à 3,90&nbsp;% quand les banques te prêtent à 3,31&nbsp;% : elles vendent moins cher qu'elles n'achètent."),

    d.checklist(6, "Si tu vends<br>maintenant", "Ce que Sébastien fait sur sa propre maison",
                [(True, "Affiche le prix des ventes qui se font",
                  "Pas celui que tu espères. Sinon tu passes un an à baisser par paliers, et le délai finit par se voir."),
                 (True, "Compte ce que coûte l'attente",
                  "Un an d'attente, c'est 3 à 5&nbsp;% de prix, plus la taxe foncière, l'entretien, l'assurance et l'argent qui ne travaille pas."),
                 (True, "Vise les acheteurs hors du bouchon",
                  "Primo-accédants avec apport, investisseurs, expatriés avec du cash : peu nombreux, mais les seuls à pouvoir signer vite."),
                 (False, "Ne multiplie pas les baisses successives",
                  "Un bien qui a baissé trois fois se négocie beaucoup plus férocement qu'un bien affiché juste dès le départ.")],
                "La nuance", "Vendre maintenant n'est pas une erreur. Vendre lentement en est une.",
                lead="Accepter 5&nbsp;% aujourd'hui pour vendre en trois mois vaut mieux qu'espérer le prix plein dans 18 mois."),

    d.mindmap(7, "Si tu achètes<br>en 2026", "Trois projets, trois réponses",
              "La question<br>à poser<br>avant l'offre",
              [("Ta résidence principale", "Négocie fort sur ce qui traîne, reste plus de 10 ans, et n'emprunte pas sur 25 ans un bien qui peut perdre 10&nbsp;%."),
               ("Le locatif nu classique", "Rendement écrasé : ça ne marche que décoté, auprès d'un vendeur contraint, avec un cash-flow positif aux taux d'aujourd'hui."),
               ("Le meublé", "Commissions, copropriété, CFE, encadrement, amortissement discuté : ce n'est plus un placement, c'est un métier."),
               ("Ce qui plaide pour acheter", "297 000 logements commencés sur 12 mois : la pénurie locative arrive. Et les vendeurs sont fatigués.")],
              "Ne parie jamais sur la plus-value", "Parier sur la plus-value, c'est parier sur le scénario A, le moins probable des trois.",
              lead="Combien ce bien précis rapporte dans chaque mode de location : presque personne ne la pose avant de signer."),

    d.cta("Action · 1 mot",
          'Ton projet tient-il<br>aux taux ' + acc("d'aujourd'hui") + ' ?',
          "MARCHE",
          "et je t'envoie les 4 signaux à surveiller sur les 12 prochains mois, avec les seuils.",
          "Les meilleurs achats se font quand les volumes sont bas et les vendeurs fatigués."),

    d.closing("Les vrais chiffres, pas les <em>discours</em> "
              + "de ceux qui vendent des formations."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_aplat")
