#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Comment faire baisser sa taxe fonciere ?" (h0GZh51rtCk, 26/08/2026).

Angle coaching : LE TUTORIEL DE VERIFICATION. Sujet jamais traite.

⛔ CHIFFRE ECARTE : Sebastien cite "le document 665" pour la fiche d'evaluation.
Le numero est manifestement deforme par la transcription automatique (les
formulaires reels sont 6675 / 6676). On parle donc de "la fiche d'evaluation"
SANS numero : mieux vaut une information juste et incomplete qu'un numero faux.
⛔ Sebastien n'est ni avocat ni fiscaliste : il partage sa methode. Slide 7.
⛔ verifoncier.fr est SON outil : on ne le cite pas ici, le CTA reste le systeme
habituel du Sous Loueur.

Usage : python3 v2_lsl_taxe_fonciere.py && python3 render.py v2_lsl_taxe_fonciere
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_taxe_fonciere"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_taxe_fonciere_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Ta taxe foncière est<br>peut-être ' + acc("fausse"),
        "Elle repose sur une fiche des années 70 que tu n'as jamais vue",
        "Décryptage terrain. Je ne suis pas fiscaliste : je partage ma méthode."),

    d.pincer(1, "Une base de 1970,<br>une addition de 2026", "Le décalage",
             ("Ce qui sert de base", "Le loyer théorique que ton bien aurait généré en 1970, comparé à des logements témoins de ta commune."),
             ("Ce qui bouge chaque année", "Un coefficient national appliqué à tout le monde, aveuglément. Plus 7&nbsp;% en 2023, plus 3,9&nbsp;% en 2024, plus 3,4&nbsp;% l'an dernier."),
             ("Et dans certaines communes", "Plus 20, plus 25, voire plus 30&nbsp;% cette année seulement."),
             "Le problème", "La base est archaïque, mais l'addition est parfaitement à jour.",
             lead="30 millions de propriétaires reçoivent leur avis en ce moment."),

    d.mindmap(2, "Les cinq maillons<br>du calcul", "Ce que personne ne t'explique",
              "Aucun<br>ne part de<br>ta surface réelle",
              [("La valeur locative", "Une photographie du marché locatif d'il y a plus de cinquante ans."),
               ("La surface pondérée", "Tes mètres carrés réels transformés en mètres carrés fiscaux par des coefficients."),
               ("Les mètres carrés fantômes", "Chaque équipement de confort ajoute de la surface forfaitaire."),
               ("La catégorie et le correctif", "Un classement de 1 à 8, puis quatre coefficients cachés dans un seul chiffre.")],
              "À retenir", "Cinq étages de calcul, et une erreur à n'importe lequel se paie tous les ans, à vie.",
              lead="Ta taxe n'est pas calculée sur ce que tu crois."),

    d.stats(3, "Les chiffres<br>qui surprennent", "Relevés sur de vraies fiches",
            [("20 %", "Ce que compte ta cave, en part de sa surface"),
             ("60 %", "Ce que comptent ton garage et ta buanderie"),
             ("37 m²", "De surface fictive ajoutée sur un bien de 81&nbsp;m² réels"),
             ("0,40 €", "L'écart au mètre carré entre catégorie 6 et catégorie 5")],
            "L'effet de levier", "Un garage de 16&nbsp;m², c'est presque 10&nbsp;m² fiscaux ajoutés à ta surface.",
            lead="Quarante centimes au mètre carré, multipliés par toute ta surface, tous les ans."),

    d.checklist(4, "Les cinq erreurs<br>les plus fréquentes", "À chercher sur ta fiche",
                [(False, "La catégorie surclassée",
                  "Un appartement banal classé confortable au lieu d'ordinaire. C'est l'erreur la plus chère."),
                 (False, "Les équipements fantômes",
                  "Une baignoire remplacée par une douche il y a 15 ans, un bidet disparu, un WC compté deux fois."),
                 (False, "Les annexes surpondérées",
                  "Une cave inutilisable comptée comme saine, une dépendance démolie il y a 10 ans."),
                 (False, "Le coefficient d'entretien figé",
                  "Façade fatiguée et installation d'origine, mais la fiche dit toujours bon état.")],
                "La cinquième", "La situation obsolète : ta vue dégagée a un immeuble devant depuis 2010, ta rue calme est devenue passante.",
                lead="Aucune ne se corrige toute seule. Il faut aller les chercher."),

    d.flow(5, "Comment tu vérifies", "Et ça ne coûte rien",
           [("Réclame ta fiche d'évaluation",
             "Elle n'arrive jamais avec ton avis. Elle dort au centre des finances publiques depuis les années 70."),
            ("Compare-la à ton bien réel",
             "Catégorie, équipements, annexes, état, situation. Ligne par ligne, sans rien supposer."),
            ("Constitue ton dossier",
             "Photos, plans, diagnostics. Une réclamation écrite et argumentée, appuyée sur la fiche.")],
           "Le chiffre fou", "99&nbsp;% des propriétaires n'ont jamais vu cette fiche. Elle est pourtant gratuite et de droit.",
           lead="Trois étapes, et la première tient en un message au centre des impôts."),

    d.timeline(6, "Le calendrier<br>de la réclamation", "Les délais à connaître",
               [("Jusqu'au 31 décembre", "De l'année qui suit ton avis",
                 "C'est ta fenêtre pour contester. Passé ce délai, l'année est perdue.", False),
                ("Pendant l'examen", "Tu paies quand même",
                 "Réclamer ne dispense pas de payer. Tu es remboursé ensuite par dégrèvement.", False),
                ("6 mois", "Le délai de réponse de l'administration",
                 "C'est le temps dont elle dispose pour se prononcer sur ta demande.", False),
                ("2 mois", "Pour saisir le tribunal administratif",
                 "En cas de refus, ou d'absence de réponse au bout des six mois.", True)],
               "Pour un investisseur", "Une erreur de catégorie à 200&nbsp;€ par an, sur 3 lots, pendant 10 ans : 6&nbsp;000&nbsp;€ partis en fumée.",
               lead="Quatre dates, et la première est la seule qui ne se rattrape pas."),

    d.compare(7, "Avant de réclamer,<br>vérifie bien", "Ça marche dans les deux sens",
              {"head": "Ce qui joue pour toi", "items": [
                  "Un équipement disparu encore facturé",
                  "Une annexe démolie toujours pondérée",
                  "Un état d'entretien qui n'est plus le bon",
                  "Une situation qui s'est dégradée"]},
              {"head": "Ce qui joue contre toi", "items": [
                  "Une véranda ajoutée depuis l'évaluation",
                  "Une piscine construite entre-temps",
                  "Une salle de bain supplémentaire",
                  "Tout aménagement jamais déclaré"]},
              "Honnêteté", "La révision va dans les deux sens, et ceci n'est pas un conseil fiscal personnalisé. Vérifie avant de déposer.",
              lead="Une réclamation rouvre le dossier entier, pas seulement la ligne qui t'arrange."),

    d.cta("Action · 1 mot",
          'Sais-tu en quelle catégorie<br>ton bien est ' + acc("classé") + ' ?',
          "FONCIER",
          "et je t'envoie la grille de lecture pour décoder ta fiche d'évaluation ligne par ligne.",
          "Le document qui fixe ta taxe depuis 50 ans, tu ne l'as jamais lu."),

    d.closing("11 ans de terrain pour t'aider à vérifier "
              + "<em>ce que tu paies vraiment</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
