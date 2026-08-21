#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video d'archive
"Comment remplir sa liasse fiscale LMNP etape par etape" (1jBnvyCvSA0).

Angle coaching : le TUTORIEL. Sebastien montre qu'on peut remplir sa liasse
soi-meme, sans expert comptable. Sujet jamais traite dans les carrousels
precedents (qui portaient sur la copropriete, les obligations de septembre,
la discretion financiere et le remplissage de calendrier).

⛔ Sebastien n'est ni avocat ni expert comptable : il partage sa methode
d'investisseur. La slide 7 le dit explicitement.
⛔ NE PAS reprendre le plafond "117 700 EUR" entendu dans la transcription :
c'est un artefact de transcription. Le meuble classe est a 50 % et 77 700 EUR.
On s'appuie sur le chiffre non ambigu : non classe, 30 % et 15 000 EUR.

Usage : python3 v2_lsl_liasse_fiscale_lmnp.py && python3 render.py v2_lsl_liasse_fiscale_lmnp
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_liasse_fiscale_lmnp"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_liasse_fiscale_lmnp_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Ta liasse fiscale,<br>' + acc("sans comptable"),
        "Formulaires 2031 et 2033 : la méthode complète, étape par étape",
        "Je ne suis pas expert comptable : je partage ma méthode d'investisseur."),

    d.pincer(1, "Pourquoi tu vas<br>y passer cette année", "Le basculement",
             ("Ce qui a changé", "Le meublé de tourisme non classé est tombé à 30&nbsp;% d'abattement, contre 50&nbsp;% avant, et son plafond à 15&nbsp;000&nbsp;€."),
             ("Ce que ça déclenche", "Au-delà de 15&nbsp;000&nbsp;€ de recettes en non classé, tu bascules automatiquement au régime réel. Ce n'est pas une option."),
             ("Et le réel garde tous ses avantages", "Charges réelles déduites, amortissement du bien et du mobilier sans plafond, déficit reportable 10 ans."),
             "Le vrai chiffre", "La majorité des loueurs au réel ne paient aucun impôt sur leurs loyers pendant 10 à 15 ans.",
             lead="Le micro était confortable : pas de comptabilité. C'est fini pour beaucoup."),

    d.mindmap(2, "Ce qu'il y a<br>vraiment dedans", "La liasse démystifiée",
              "Un bilan<br>comptable<br>de ton activité",
              [("La 2031", "La déclaration de résultat. Le récapitulatif, qui reprend ce que tu as calculé ailleurs."),
               ("La 2033&nbsp;A", "Le bilan simplifié au 31 décembre : ce que tu possèdes face à ce que tu dois."),
               ("La 2033&nbsp;B", "Le compte de résultat : recettes, charges, amortissements. Le plus important."),
               ("Les 2033&nbsp;C et D", "Les immobilisations et amortissements, puis le suivi de tes déficits reportables.")],
              "Bonne nouvelle", "Les E, F et G ne concernent pas le meublé classique. À valider, pas à remplir.",
              lead="Sept annexes, ça fait peur. En pratique tu en remplis quatre."),

    d.checklist(3, "Ce que tu rassembles<br>avant de commencer", "Prévois un dimanche",
                [(True, "Tous tes encaissements de l'année",
                  "Exports des plateformes, loyers, charges récupérables, ménage. Et le dépôt de garantie, même restitué."),
                 (True, "Les charges, pièce par pièce",
                  "Intérêts d'emprunt, assurance emprunteur, taxe foncière, charges de copropriété, assurance propriétaire non occupant."),
                 (True, "Ce que les plateformes t'ont prélevé",
                  "Ton chiffre d'affaires est brut : les commissions se déduisent, encore faut-il les relever."),
                 (True, "De quoi calculer tes amortissements",
                  "Acte d'achat, factures de mobilier datées, tableaux de l'année précédente, déficits antérieurs.")],
                "À garder", "Six ans après la dernière année d'amortissement utilisée. En cas de contrôle, on te les demande.",
                lead="Le jour où tu remplis, tout doit déjà être sous la main."),

    d.flow(4, "Dans quel ordre<br>tu remplis", "Et pas dans celui des numéros",
           [("Tu commences par la 2033&nbsp;B",
             "Recettes moins charges moins amortissements. C'est elle qui produit ton résultat."),
            ("Puis la 2033&nbsp;C, ensuite la A",
             "Le détail des amortissements par composant, puis le bilan actif contre passif."),
            ("Tu finis par la 2031",
             "Le récapitulatif ne fait que reprendre le résultat déjà calculé. Case C7 : le résultat fiscal.")],
           "Ton autocontrôle", "Total actif doit égaler total passif. Si les deux diffèrent, il y a une erreur en amont.",
           lead="On remonte de la fin vers le début, parce que chaque formulaire nourrit le suivant."),

    d.stats(5, "L'amortissement<br>par composants", "Le cœur du dispositif",
            [("40 à 50 %", "Le gros œuvre, amorti sur 50 à 80 ans"),
             ("5 à 10 %", "Toiture, électricité, plomberie : 25 ans chacun"),
             ("10 à 15 %", "Les agencements intérieurs, sur 15 ans"),
             ("0 %", "Le terrain, qui ne s'amortit jamais")],
            "Le piège", "Sous-évaluer le terrain gonfle le reste. Des propriétaires se sont fait redresser là-dessus.",
            lead="Un amortissement global sur la durée du bien n'est pas conforme : il faut ventiler."),

    d.compare(6, "Les erreurs<br>qui coûtent cher", "Les cinq classiques",
              {"head": "Ce que beaucoup font", "items": [
                  "Amortir jusqu'à créer un déficit",
                  "Reporter le déficit sur le revenu global",
                  "Amortir le bien en un seul bloc",
                  "Créer son espace professionnel en avril"]},
              {"head": "Ce que dit la règle", "items": [
                  "L'article 39 C l'interdit : l'excédent est différé",
                  "Il ne s'impute que sur tes futurs loyers meublés",
                  "L'administration attend une décomposition",
                  "L'activation prend plusieurs jours"]},
              "Le retard", "10 à 40&nbsp;% de majoration, plus 150&nbsp;€ par formulaire manquant.",
              lead="Aucune n'est compliquée à éviter. Toutes sont chères à réparer."),

    d.timeline(7, "Ton calendrier<br>de l'année", "Rien ne se fait en avril",
               [("Dès maintenant", "Crée ton espace professionnel",
                 "L'activation de la liasse sur le site des impôts prend plusieurs jours.", False),
                ("Janvier à mars", "Rassemble les justificatifs",
                 "Un suivi des loyers et des charges tenu à l'année t'évite les erreurs de saisie.", False),
                ("Avant le 5 mai 2026", "Télétransmets la liasse",
                 "Deuxième jour ouvré suivant le 1er mai, obligatoirement par voie électronique.", True),
                ("Fin mai, début juin", "Reporte sur la 2042-C-PRO",
                 "Le déficit au réel se déclare le plus souvent en case 5NY.", False)],
               "Honnêteté", "Ceci n'est pas un conseil fiscal personnalisé. En cas de doute sur ta situation, fais-toi accompagner.",
               lead="À l'automne, il restera la cotisation foncière des entreprises."),

    d.cta("Action · 1 mot",
          'Ta liasse te ferait-elle<br>vraiment ' + acc("peur") + ' ?',
          "LIASSE",
          "et je t'envoie la liste des pièces à rassembler et l'ordre de remplissage.",
          "Un dimanche par an contre des honoraires chaque année."),

    d.closing("11 ans de terrain pour t'aider à reprendre la main "
              + "<em>sur ta fiscalité</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
