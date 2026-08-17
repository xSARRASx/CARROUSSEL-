#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Remplir son Airbnb sans baisser les prix ? C'est possible !" (17/08/2026, iVd1TQ-GUYs).

Angle coaching : la BASSE SAISON. Different du carrousel LSL du 03/08
("remplir sans baisser les prix"), qui portait sur les techniques de remplissage
en general. Ici l'axe est saisonnier : pourquoi brader l'hiver detruit le
positionnement, et les leviers qui remplissent octobre-mars sans toucher au prix
de reference. Point d'orgue : le bail mobilite (loi Elan 2018), qui ne consomme
pas le quota de 90/120 jours.

⛔ NE PAS presenter Sebastien comme juriste : il relaie un dispositif legal.

Usage : python3 v2_lsl_basse_saison_sans_brader.py && python3 render.py v2_lsl_basse_saison_sans_brader
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_basse_saison_sans_brader"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_basse_saison_sans_brader_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Ton hiver est vide,<br>et tu vas ' + acc("brader"),
        "Huit leviers pour remplir octobre à mars sans jamais toucher à ton prix de référence",
        "Décryptage terrain, après 11 ans de saisons basses."),

    d.pincer(1, "Pourquoi brader<br>est un piège", "Les deux pièges",
             ("Le piège économique", "En août, moins 10&nbsp;% déclenche des réservations que tu aurais prises de toute façon. En janvier, il y a simplement moins de monde qui cherche."),
             ("Le piège algorithmique", "Une annonce bradée tout l'hiver entraîne la plateforme ET les voyageurs à la percevoir comme une annonce pas chère."),
             ("Remonter ensuite prend des mois", "Je l'ai vécu sur mes logements thématiques : j'avais moi-même appris à mes clients un prix que je n'ai plus jamais pu reprendre."),
             "Le principe", "Le prix de référence reste intact. On joue sur tout le reste.",
             lead="Baisser les prix coûte bien plus cher que ce que tu mesures sur le moment."),

    d.flow(2, "Les remises<br>chirurgicales", "Levier 1 et 2",
           [("Ouvre ton calendrier le plus loin possible",
             "Beaucoup d'annonces s'arrêtent à 3 ou 6 mois : tu es invisible pour ceux qui réservent un an à l'avance."),
            ("Pose un early bird modeste",
             "Pas besoin de 30&nbsp;%. Du 5 à 10&nbsp;% sur des dates lointaines sécurise déjà ton chiffre d'affaires."),
            ("Descends par paliers, pas d'un bloc",
             "Prix plein au-delà de 30 jours, remise modérée entre 30 et 14, remise agressive sous 7 jours.")],
           "Pourquoi ça marche", "Une remise last minute est invisible dans ton prix de référence : elle disparaît dès la date passée.",
           lead="C'est exactement l'inverse de la baisse généralisée."),

    d.checklist(3, "Tes règles<br>de séjour d'hiver", "Levier 3",
                [(True, "Passe ta durée minimum à 3 nuits en semaine",
                  "Le ménage te coûte le même prix pour une nuit ou pour quatre."),
                 (True, "Active le remplissage des nuits orphelines",
                  "La nuit seule coincée entre deux réservations, tu vas la chercher. C'est le bouche-trou."),
                 (True, "Allonge ton délai de préparation",
                  "Mieux vaut refuser une arrivée à 4 heures de préavis que de récolter un avis sur un ménage bâclé."),
                 (True, "Traite chaque avis comme s'il pesait double",
                  "Moins de rotations l'hiver : un seul mauvais avis pèse beaucoup plus lourd dans ta moyenne.")],
                "L'objectif change", "L'hiver, tu ne maximises plus le prix de la nuit : tu minimises les trous et les rotations.",
                lead="Quatre réglages qui ne coûtent rien et que presque personne ne touche."),

    d.stats(4, "Le calcul<br>du mois plein", "Levier 4",
            [("28 nuits", "Le seuil à partir duquel on bascule sur le marché de la moyenne durée"),
             ("1 ménage", "Au lieu de six sur un mois de rotations courtes"),
             ("40 à 50 %", "Le taux d'occupation réel d'un hiver non préparé"),
             ("30 à 50 %", "La remise mensuelle qui reste plus rentable que ce scénario")],
            "À vérifier chez toi", "Moi je fais du 50&nbsp;%. Le chiffre paraît violent tant qu'on ne le compare pas au scénario réel.",
            lead="La moitié des annonces laissent leurs remises hebdo et mensuelles à zéro."),

    d.compare(5, "L'été et l'hiver<br>ne vendent pas<br>la même chose", "Levier 5",
              {"head": "Ce que tu mettais en avant l'été", "items": [
                  "La terrasse et le barbecue",
                  "La plage qui n'est pas très loin",
                  "La climatisation et les ventilateurs",
                  "Des voyageurs qui partent une fois par an"]},
              {"head": "Ce qui décide en hiver", "items": [
                  "Un vrai espace de travail et le parking",
                  "Lave-linge, sèche-linge, cuisine complète",
                  "Le chauffage clairement expliqué",
                  "Des professionnels et des télétravailleurs"]},
              "Le geste concret", "Refais des photos plus chaudes, ajoute des plaids, un coin lecture, une décoration de Noël en décembre.",
              lead="Ton annonce d'hiver n'est pas ton annonce d'été avec des prix en moins."),

    d.mindmap(6, "Le calendrier<br>des événements", "Levier 6",
              "Ce que le<br>revenue management<br>ne voit pas",
              [("Les rendez-vous de ta ville", "Salons professionnels, congrès, festivals d'hiver, matchs, concerts, marchés de Noël."),
               ("Les besoins permanents", "Hôpitaux et familles de patients, personnel de remplacement, tribunaux, centres de formation."),
               ("Les gros chantiers", "Souvent annoncés dans la presse locale des mois avant le premier ouvrier."),
               ("Ce que tu en fais", "Tu remontes les prix sur ces dates et tu allonges la durée minimum de séjour.")],
              "Le timing", "Un outil de tarification réagit quand la demande monte. C'est déjà trop tard.",
              lead="Dès septembre, repère 10 à 15 dates génératrices autour de chez toi."),

    d.layers(7, "Le pivot<br>moyenne durée", "Levier 7 et 8",
             [("Étage 1", "Un marché à part entière",
               "Au-delà de 28 nuits : ses propres sites, ses propres recherches, une demande d'hiver structurelle."),
              ("Étage 2", "Le bail mobilité",
               "Créé par la loi Elan en 2018 : de 1 à 10 mois, non renouvelable, réservé aux personnes en mobilité."),
              ("Étage 3", "Ton quota reste intact",
               "Un mois vendu via une plateforme consomme tes 90 ou 120 jours. Un bail mobilité, non.")],
             "Où tu vas les chercher", "Écoles et CFA, agences d'intérim, hôpitaux, entreprises du bâtiment, gros employeurs de ta ville.",
             lead="Étudiants, stagiaires, apprentis, salariés en mission ou en mutation : ils cherchent de septembre à juin."),

    d.cta("Action · 1 mot",
          'Ton calendrier d\'hiver<br>est-il déjà ' + acc("préparé") + ' ?',
          "HIVER",
          "et je t'envoie le plan de préparation de basse saison, levier par levier.",
          "Ceux qui se plaignent chaque année de l'hiver ne l'ont simplement pas préparé."),

    d.closing("11 ans de terrain pour remplir ton hiver "
              + "<em>sans brader</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
