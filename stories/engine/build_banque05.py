#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 05 — video du 12/08/2026 : un proprietaire gagne contre sa copropriete
(ID YouTube keONb-XUtJY).

⚠️ Le titre YouTube change et se traduit tout seul ("The ruling that will give
all Airbnb hosts ideas" le 17/08, apres avoir affiche autre chose le 13) :
seule la transcription francaise fait foi. Vrai titre : « Un proprietaire
Airbnb vient d'ECRASER sa copropriete au tribunal ».

C'est le MIROIR de banque-03 (sICVVkMpSl4, « ta copropriete peut interdire ton
Airbnb ») : la meme matiere juridique, mais vue du cote de celui qui gagne. Le
recouvrement est assume et volontairement limite au strict necessaire : on ne
refait NI la loi Le Meur, NI le vote aux deux tiers, NI les checklists, deja
traites. Ce qui est neuf ici, et qui seul justifie la fournee :
    - un jugement date et chiffre (Nice, 23 juillet 2026) avec son issue ;
    - les 5 boucliers, c'est-a-dire une defense actionnable ;
    - les 4 prestations para-hotelieres de l'article 261 D et la regle des
      trois cumulees, jamais detaillees jusqu'ici ;
    - le constat d'huissier sur les avis Airbnb, ecarte par le tribunal ;
    - le delai de deux mois pour contester une resolution.

    R — le jugement, de la mise en demeure a la condamnation (6 stories) ;
    S — les cinq boucliers a activer (5 stories).

⚠️ TAILLES IMPOSEES PAR LA GRILLE (piege du 13/08) : 6 stories le lundi,
5 le mardi. C'est l'ordre alphabetique qui donne le jour.

⚠️ Contenu 100 % issu de la transcription. Aucune juridiction, aucune date,
aucun montant invente. Sebastien precise lui-meme qu'il n'est pas avocat :
les stories gardent cette prudence et ne promettent jamais un resultat.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : les outils maison cites dans la
video ne sont pas repris ici.

Rendu : python3 render_stories.py banque-05
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         acc, write_lot)

o = acc

# Les apostrophes ne passent pas dans une expression de f-string.
ECRASE = acc("gagné")
CIVILE = acc("civile")
COMMERCIALE = acc("commerciale")
TROIS = acc("trois")
PIECES = acc("pièces")
DEUX_MOIS = acc("deux mois")
CINQ_BOUCLIERS = acc("cinq boucliers")
ANNULEES = acc("annulées")

SEQUENCES = {

# ============================================================================
# SEQUENCE R — Le jugement (lundi, 6 stories)
# ============================================================================
"R_proprio_gagne": [
    cover("bg_facade_pierre", "tribunal judiciaire de Nice, 23 juillet 2026",
          f'Un propriétaire a {ECRASE} contre sa copropriété.',
          sub="Elle avait voté l'interdiction et réclamé 500 € d'astreinte "
              "par infraction. Elle repart déboutée de tout.",
          hand_bottom="le déroulé, juste après"),

    p_timeline("bg_escalier", "trois ans de bras de fer",
               "Comment l'affaire s'est déroulée",
               [("Été 2023 : la mise en demeure",
                 "Le syndic écrit au propriétaire : arrêtez immédiatement "
                 "votre activité commerciale.", None),
                ("Novembre 2023 : l'assemblée générale",
                 "Résolution 6, l'interdiction des locations à la nuitée. "
                 "Résolution 7, mandat au syndic pour attaquer en justice.",
                 None),
                ("23 juillet 2026 : le jugement",
                 "Les deux résolutions sont annulées. La copropriété est "
                 "déboutée et condamnée aux frais.", None)]),

    p_bigstat("bg_documents", "l'addition pour la copropriété",
              "Ce que le tribunal a décidé",
              "2 000 €", "à payer au propriétaire par la copropriété",
              [f'Les deux résolutions de l\'assemblée sont {ANNULEES}.',
               "L'astreinte de 500 € par infraction tombe.",
               "Ce sont les copropriétaires qui paient : l'avocat du syndic, "
               "c'était déjà leur argent."],
              numsize=150),

    focus("bg_cour", "l'argument préféré des syndics, désamorcé",
          f'Juridiquement {CIVILE}, fiscalement {COMMERCIALE}.',
          "« Vos loyers sont imposés en bénéfices industriels et commerciaux, "
          "donc votre activité est commerciale. » Le tribunal l'écrit noir sur "
          "blanc : les deux n'ont rien à voir. Le régime fiscal ne change pas "
          "la nature juridique de l'activité."),

    focus("bg_hall_immeuble", "ce que la copropriété avait versé au dossier",
          "Accueillir tes voyageurs ne te rend pas commercial.",
          "Elle avait fait constater par huissier les avis Airbnb citant "
          "quelqu'un qui accueille, remet les clés et donne des conseils. "
          "Réponse du tribunal : cela ne suffit pas à requalifier l'activité."),

    fin("bg_lac", "Le jugement est rendu en premier ressort.",
        "la copropriété peut faire appel, mais la décision s'appuie sur la Cour de cassation"),
],

# ============================================================================
# SEQUENCE S — Les cinq boucliers (mardi, 5 stories)
# ============================================================================
"S_cinq_boucliers": [
    cover("bg_immeuble_dore", "ce qu'on peut en tirer",
          f'Les {CINQ_BOUCLIERS} du propriétaire qui a gagné.',
          sub="Ce n'est pas un mode d'emploi et ça ne remplace pas un avocat. "
              "Ce sont les cinq points sur lesquels la copropriété est tombée.",
          hand_bottom="les cinq, juste après"),

    p_steps("bg_boites_lettres", "les trois premiers",
            "Sur quoi la copropriété est tombée",
            [("La nature civile",
              "Sans prestation para-hôtelière, la courte durée n'est pas une "
              "activité commerciale. Cour de cassation, 25 janvier 2024."),
             ("Le règlement, lu vraiment",
              "Il autorisait de louer comme bon semble et la location meublée "
              "par appartement entier. Presque personne ne le lit."),
             ("Le vice de majorité",
              "Modifier la destination de l'immeuble exigeait l'unanimité à "
              "la date du vote. L'assemblée a voté à la majorité simple.")]),

    focus("bg_bureau_matin", "le vrai critère, article 261 D",
          f'Il faut en cumuler {TROIS} pour basculer.',
          "Les quatre prestations para-hôtelières : le petit-déjeuner, le "
          "nettoyage régulier en cours de séjour, la fourniture du linge de "
          "maison, la réception de la clientèle. Le ménage de fin de séjour "
          "n'en fait pas partie. En dessous de trois, tu restes civil."),

    focus("bg_village", "le quatrième bouclier",
          f'La justice juge des {PIECES}, pas des impressions.',
          "Va-et-vient, nuisances sonores, bouteilles par la fenêtre : le "
          "dossier était vide. Pas de constat, pas même une lettre adressée "
          "au propriétaire. Face à une accusation, exige des preuves datées."),

    fin("bg_montagne", f'Une résolution hostile se conteste sous {DEUX_MOIS}.',
        "ressors ton règlement et tes procès-verbaux d'assemblée, et prépare tes preuves"),
],

}

SLUG = "banque-05"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
