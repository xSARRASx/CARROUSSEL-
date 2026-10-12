#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 20 — video du dimanche 11/10/2026 : « Airbnb choisi maintenant votre
photo a votre place » (ID YouTube soj5bEyLcKE). Sous-titres recuperes par le
robot.

⚠️ SUJET 100 % NEUF, et ca fait du bien : les cinq dernieres fournees etaient
fiscales ou budgetaires. Celle-ci est operationnelle, et Sebastien l'annonce
lui-meme comme « plus legere ». Elle touche pourtant directement le chiffre
d'affaires.

⚠️ FOURNEE COURTE, ET C'EST ASSUME (11 stories au lieu de 15). La banque de
fonds est a sec : sur 45 fonds, 30 sont passes a l'ecran dans les deux
dernieres fournees et 4 sont trop sombres. Il n'en restait que 11 utilisables
sans remontrer une image vue la semaine derniere. Plutot que de recycler, on
fait plus court -- c'est exactement la regle de Martin du 10/09 (« si tu fais
moins de storie c'est pas grave »). Les six fonds de DA n'ont pas ete vus
depuis le 28-29/09 ; les cinq de DB depuis le 05/10.
⚠️ LA VRAIE REPARATION N'A PAS PU SE FAIRE : la vague 4 de fonds est ecrite
dans gen_background.py mais Gemini repond 401. La variable GEMINI_API_KEY de
l'environnement ne contient pas une cle Gemini (elle commence par « AQ.A » au
lieu de « AIza »). A signaler a Martin.

⚠️ ECARTE, comme toujours (marque LE SOUS LOUEUR) : l'outil de retouche de
photos presente dans toute la seconde moitie de la video (la demonstration,
l'import d'annonce, la video de visite, la 3D). Sebastien dit lui-meme « c'est
mon outil ». On garde les PRINCIPES, qui valent avec n'importe quel telephone.

⚠️ REPORTE FAUTE DE FONDS, a reprendre en complement : la ligne rouge de la
retouche (Californie au 1er janvier 2026, Milwaukee au 1er septembre, Airbnb
qui refuse depuis le 20 avril 2026 une photo retouchee comme preuve de
dommage, et les trois paliers vert / orange / rouge). L'essentiel tient dans
la cloture de DB, le detail attend.

    DA — Airbnb choisit ta photo a ta place (6 stories, lundi 12/10) ;
    DB — cinq regles pour cinq photos (5, mardi 13/10).

Rendu : python3 render_stories.py banque-20
"""
from photo_style import (cover, focus, fin, p_steps, p_bars, p_duo,
                         p_bigstat, acc, write_lot, accroche)

NUM_LOT = 20

# Les apostrophes ne passent pas dans une expression de f-string.
PLUS_TOI = acc("ce n'est plus toi")
CINQ_PREMIERES = acc("tes cinq premières")
UN_PETIT_LIEN = acc("un petit lien")
TOUTES_LA_UNE = acc("toutes tenir la une")
DEUX_SECONDES = acc("deux à trois secondes")
MEME_VILLE = acc("même ville, même type de bien")
AVANT_DE_LIRE = acc("avant même de lire la description")
GARDE_TES_ORIGINAUX = acc("garde toujours tes originaux")
UNE_SEULE = acc("une seule photo à la fois")

SEQUENCES = {

# ============================================================================
# SEQUENCE DA — Airbnb choisit ta photo a ta place (lundi 12/10, 6 stories)
# Forme : cover > focus > p_duo > p_bigstat > focus > fin
# ============================================================================
"DA_airbnb_choisit_ta_photo": [

    cover("bg_couloir_hotel", "depuis le 20 mai, et presque personne ne l'a vu",
          f'La photo de couverture de ton annonce, {PLUS_TOI} qui la choisis.',
          sub="Une intelligence artificielle pioche dans tes cinq premières "
              "photos et montre à chaque voyageur celle qu'elle juge la "
              "meilleure. Il existe un réglage pour reprendre la main.",
          hand_bottom=accroche(NUM_LOT * 3)),

    focus("bg_table_bois", "noyé dans 220 nouveautés",
          "L'idée n'est pas idiote. Le problème, c'est que tu ne contrôles plus rien.",
          "Un couple qui cherche une vue mer verra peut-être le balcon, une "
          "famille verra la chambre. Sauf que des hôtes ont découvert que "
          "l'algorithme mettait en avant leur plus mauvaise photo. L'un d'eux "
          "voyait son jacuzzi, celle qu'il trouvait ratée, revenir en "
          "couverture à chaque fois qu'il la changeait. Le support a confirmé "
          "que l'IA alterne entre les cinq premières, et c'est tout."),

    p_duo("bg_etagere", "remets-toi à jour",
          "Ce que la plupart croient encore, et ce qui se passe vraiment",
          "Ce qu'on croit encore",
          ["Ma photo de couverture, c'est celle que j'ai placée en premier.",
           "Si je réordonne mes photos, l'ordre tient.",
           "Au fond, une seule photo compte vraiment."],
          "Ce qui se passe depuis le 20 mai",
          [f'L\'IA choisit dans {CINQ_PREMIERES}, selon la recherche du voyageur.',
           "En mode automatique, elle reprend la main même après ton changement.",
           "Chacune des cinq peut se retrouver en couverture."]),

    p_bigstat("bg_champ_ete", "Lisbonne, près de 16 000 annonces actives",
              "L'écart ne vient pas du tarif",
              "61", "% de revenu en plus par nuit disponible",
              [f'C\'est l\'écart entre le quart des annonces les mieux '
               f'classées et l\'annonce médiane. {MEME_VILLE}.',
               "Ce qui sépare les deux, c'est la tarification et la "
               "présentation de l'annonce.",
               f'Et la présentation commence par la première photo : le '
               f'voyageur lui accorde {DEUX_SECONDES} avant de cliquer, ou de '
               f'passer au suivant.',
               "Ces clics sont mesurés. Moins de clics, moins de visibilité, "
               "moins de réservations : la boucle est bouclée."]),

    focus("bg_mur_beton", "la conséquence qu'on oublie",
          f'Tu n\'as plus une photo de couverture. Tu en as cinq, et elles '
          f'doivent {TOUTES_LA_UNE}.',
          "Si ta cinquième photo est une salle de bain prise au flash, en "
          "vertical, vite fait parce que « ce n'est qu'une salle de bain », "
          "c'est peut-être elle que verra le prochain voyageur."),

    fin("bg_plage_aube", f'Dans les photos de ton annonce, {UN_PETIT_LIEN} te rend la main.',
        "le bouton bien visible laisse faire Airbnb ; repasse en manuel, et reviens vérifier de temps en temps, des hôtes rapportent que l'automatique reprend le dessus"),
],

# ============================================================================
# SEQUENCE DB — Cinq regles pour cinq photos (mardi 13/10, 5 stories)
# Forme : cover > p_bars > p_steps > focus > fin
# ============================================================================
"DB_cinq_regles_cinq_photos": [

    cover("bg_cafe_table", "on dit que les photos comptent",
          "D'accord. Mais ça vaut combien, exactement&nbsp;?",
          sub="Des études américaines récentes ont mis des chiffres dessus. "
              "Ils sont plus gros qu'on ne l'imagine, et ce n'est pas le "
              "mobilier qui fait la différence.",
          hand_bottom=accroche(NUM_LOT * 3 + 1)),

    p_bars("bg_foret_automne", "deux sources, des ordres de grandeur",
           "Ce que gagnent les annonces bien photographiées",
           [("Réservations, étude sur 13 000 annonces", 17.5),
            ("Nuits réservées, photos professionnelles", 26),
            ("Réservations, photos professionnelles", 28),
            ("Revenus, jusqu'à", 40)],
           note="Sur 25 000 € de recettes par an, 17,5 % de réservations en "
                "plus font 4 375 €, et 26 % de nuits en plus font 6 500 €. "
                "Même en divisant par deux, ça reste plusieurs milliers "
                "d'euros. Les chercheurs ont isolé ce qui compte : la clarté "
                "et les couleurs, pas le mobilier ni la surface."),

    p_steps("bg_neige_douce", "elles viennent des hôtes américains",
            "Cinq règles pour tes cinq premières photos",
            [("Pense téléphone",
              "La plupart des recherches se font sur un écran de dix "
              "centimètres, et la vignette est recadrée. Un seul sujet par "
              "photo, centré, avec de l'air autour."),
             ("Lumière naturelle",
              "Rideaux ouverts, le matin ou en fin d'après-midi. Jamais en "
              "plein soleil. Et photographie à hauteur de poitrine, pas en "
              "plongée."),
             ("Jamais de texte sur une photo",
              "Ni promo, ni badge, ni « wifi ». Ça se recadre mal, ça devient "
              "illisible sur un téléphone, et ça fait perdre confiance."),
             ("Un détail qui te distingue",
              "Un lit fait, un canapé orienté vers quelque chose, et ce que "
              "les autres n'ont pas : la terrasse, la vue, la cheminée."),
             ("Teste, ne devine pas",
              "Change une seule photo, attends deux semaines, regarde ton "
              "taux de clic dans les statistiques Airbnb. Si ça monte, tu "
              "gardes. Sinon, tu remets l'ancienne.")]),

    focus("bg_rideau", "école hôtelière de Cornell",
          f'82 % des voyageurs jugent la fiabilité de l\'hôte à la qualité '
          f'des photos, {AVANT_DE_LIRE}.',
          "Autrement dit, la photo ne vend pas seulement le logement : elle "
          "dit si on peut te faire confiance. C'est pour ça qu'aucun autre "
          "levier de ton annonce n'a ce rapport entre le temps investi et ce "
          "que ça rapporte."),

    fin("bg_toits_pluie", f'Retouche la lumière et le cadrage, mais {GARDE_TES_ORIGINAUX}.',
        "la lumière et le cadrage ne changent pas le logement ; déplacer un meuble ou repeindre un mur, si"),
],

}

SLUG = "banque-20"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
