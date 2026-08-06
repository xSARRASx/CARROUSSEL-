#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"10 techniques pour remplir ton Airbnb sans baisser les prix" (rattrapage 06/08/2026).

Angle coaching : Airbnb classe par taux de conversion, pas par prix. Baisser le
prix est un aveu de probleme de conversion. Les leviers qui n'y touchent pas.

Chaque slide de contenu est un SCHEMA, jamais une liste de texte.

Usage : python3 v2_lsl_remplir_sans_baisser_prix.py && python3 render.py v2_lsl_remplir_sans_baisser_prix
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_remplir_sans_baisser_prix"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_remplir_sans_baisser_prix_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Remplir ton annonce<br>sans ' + acc("baisser tes prix"),
        "Airbnb ne classe pas les moins chers, mais ceux qui convertissent le mieux",
        "Onze ans de terrain, et des leviers que presque personne n'active."),

    d.layers(1, "Le tunnel<br>que l'algorithme mesure", "Quatre étages, quatre taux",
             [("Étage 1", "Les impressions",
               "Combien de fois ton annonce apparaît dans les résultats de recherche."),
              ("Étage 2", "Les clics et le temps passé",
               "Combien ouvrent ton annonce, et combien de temps ils la font défiler."),
              ("Étage 3", "Les enregistrements en favoris",
               "Le petit cœur : un signal de désir fort, mesuré et pris en compte."),
              ("Étage 4", "La réservation",
               "Une réservation en déclenche d'autres : le cercle vertueux du classement.")],
             "À retenir", "Ces taux sont visibles dans ton interface. Ils n'y sont pas par hasard.",
             lead="Airbnb gagne quand la réservation se fait, et son moteur ne cherche que ça."),

    d.compare(2, "Baisser le prix<br>ou travailler la conversion", "Deux réflexes opposés",
              {"head": "Ce que font la plupart", "items": [
                  "Baisser le prix quand le mois est vide",
                  "Recommencer le mois suivant, un peu plus bas",
                  "Perdre en rentabilité sans regagner de visibilité",
                  "Finir par croire que le marché est saturé"]},
              {"head": "Ce qui fait remonter", "items": [
                  "Traiter chaque étage du tunnel séparément",
                  "Débloquer les filtres de recherche qui manquent",
                  "Rendre l'annonce lisible en vignette de 300 pixels",
                  "Garder son prix et gagner sur le taux de clic"]},
              "La vérité qui pique", "Baisser ses prix n'est pas une stratégie : c'est l'aveu d'un problème de conversion.",
              lead="Le prix est un levier parmi d'autres, et c'est celui qui coûte le plus cher."),

    d.checklist(3, "Les deux réflexes<br>immédiats", "Applicables aujourd'hui",
                [(True, "Répondre en moins d'une heure",
                  "Le délai de réponse est mesuré. Répondre non tout de suite vaut mieux que ne pas répondre."),
                 (True, "Accepter toutes les demandes que tu peux",
                  "Chaque refus est un signal négatif, et une annulation fait dégringoler le classement."),
                 (True, "Activer la réservation instantanée",
                  "Ton taux d'acceptation passe mécaniquement à cent pour cent."),
                 (True, "Activer le filtre voyageur d'Airbnb",
                  "Avis positifs et pièce d'identité vérifiée : il n'est pas actif par défaut.")],
                "Le réflexe", "Des messages automatiques, ou une réponse assistée, tiennent le délai à ta place.",
                lead="Deux réglages que beaucoup laissent de côté, et qui pèsent lourd."),

    d.mindmap(4, "Tes équipements<br>sont des filtres", "Pas de la décoration",
              "Chaque case<br>cochée te rend<br>visible",
              [("Le lave-linge oublié", "Non coché, tu n'apparais pas dans ce filtre, même si tu l'as."),
               ("Lit parapluie et chaise haute", "Tu entres dans le filtre famille, et tu y ressors souvent."),
               ("Espace de travail dédié", "Une table, une chaise correcte, une multiprise : tu captes le télétravail."),
               ("Le débit mesuré", "Indique la fibre et le débit réel : ceux qui télétravaillent le cherchent.")],
              "L'effet", "Plus de filtres cochés, plus d'apparitions, donc plus de clics.",
              lead="Un équipement non coché est un équipement qui n'existe pas pour la recherche."),

    d.pincer(5, "Deux façons<br>de paraître moins cher", "Sans toucher à ton tarif",
             ("Le tarif par voyageur", "Au lieu de 120&nbsp;€ pour quatre, affiche 95&nbsp;€ pour deux, plus 12&nbsp;€ par voyageur."),
             ("La réduction non remboursable", "Une option à dix pour cent qu'Airbnb affiche dans les résultats de recherche."),
             ("Le prix affiché baisse, pas le tien", "La plupart des recherches se font avec le réglage par défaut d'un ou deux voyageurs."),
             "L'effet", "Tu passes devant un concurrent au même tarif réel, uniquement sur l'affichage.",
             lead="Deux réglages qui changent le prix vu, jamais le prix encaissé."),

    d.stats(6, "Les trois leviers<br>du haut du tunnel", "Là où tout se gagne",
            [("La photo", "Montre ce qui te distingue, jamais le salon : il ressemble à dix-neuf autres"),
             ("Le titre", "Capacité, équipement phare, ancre géographique. Une publicité, pas un inventaire"),
             ("Les avis", "L'algorithme lit le texte : oriente sans dicter, sur ce que tu veux voir ressortir"),
             ("Les favoris", "Des vues qui montent et des favoris qui stagnent annoncent le problème des semaines à l'avance")],
            "Le test", "Cherche ta ville en navigation privée et regarde ton annonce deux secondes, comme un voyageur.",
            lead="Trois éléments décident si l'on clique, et un quatrième te prévient avant la chute."),

    d.flow(7, "Traiter ton annonce<br>comme un produit", "La vraie différence",
           [("Mesurer chaque semaine",
             "Les taux sont dans ton interface : impressions, clics, favoris, réservations."),
            ("Changer une seule chose par mois",
             "Ce mois la photo de couverture, le suivant le titre, puis un équipement oublié."),
            ("Laisser les gains s'additionner",
             "Dix pour cent de clic en plus, dix pour cent de conversion en plus : sur un an, l'écart devient massif.")],
           "Le constat", "Ceux qui se plaignent de la concurrence n'ont rien changé à leur annonce depuis 2021.",
           lead="L'algorithme favorise aussi les annonces vivantes, mises à jour régulièrement."),

    d.cta("Action · 1 mot",
          'Ton annonce est-elle<br>vraiment ' + acc("optimisée") + ' ?',
          "AUDIT",
          "et je t'explique comment analyser ton annonce point par point, gratuitement.",
          "Avant de retoucher tes prix, regarde ce que l'algorithme voit de toi."),

    d.closing("11 ans de terrain pour t'aider à remplir ton logement "
              + "<em>au bon prix</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
