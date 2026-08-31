#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 09 — video du 30/08/2026 : « Menage Airbnb : le business cache qui
rapporte gros » (ID YouTube sWiie3c__Lo). Transcription fournie par Martin le
31/08/2026 (quatrieme video d'affilee sans aucun sous-titre sur YouTube).

Sujet en or : Sebastien constate a travers son logiciel que le vrai probleme
des conciergeries n'est PAS de trouver des proprietaires ni des clients, mais
de trouver des equipes de menage fiables -- et en face, des gens cherchent un
business sans capital. La video connecte les deux. Elle parle donc aux DEUX
audiences a la fois : les conciergeries et ceux qui veulent se lancer.

    AA — le marche et les chiffres (6 stories, lundi) ;
    AB — ce qu'une conciergerie regarde vraiment (5 stories, mardi) ;
    AC — le recrutement, le second goulot (5 stories, reserve).

⚠️ CE QUI N'EST PAS REPRIS, VOLONTAIREMENT :
- Les outils maison cites dans la video (le logiciel, le module WhatsApp, le
  logiciel de facturation). Marque LE SOUS LOUEUR : on garde le conseil, qui
  est la vraie valeur. Regle appliquee depuis banque-04.
- Le passage sur la facturation electronique : deja traite en entier dans
  banque-04 (O_facture_electronique, publiee les 13 et 14/08). On ne repete pas.

⚠️ HONNETETE CONSERVEE : Sebastien nuance lui-meme ses chiffres (« au debut tu
demarres seul », « metier physique », « ce n'est pas de l'argent passif »). Les
stories gardent cette nuance -- une sequence qui ne promettrait que 11 200 €
serait malhonnete.

⚠️ Tailles imposees par la grille : 6 le lundi, 5 le mardi.

Rendu : python3 render_stories.py banque-09
"""
from photo_style import (cover, focus, fin, p_steps, p_duo, p_bigstat,
                         acc, write_lot)

FIABLE = acc("fiable")
UN_SEUL = acc("un seul client")
NON_NEGOCIABLE = acc("non négociable")
PAS_PASSIF = acc("pas passif")
AVANT_LE_PRIX = acc("avant le prix")
LES_YEUX = acc("les yeux")
PENURIE = acc("pénurie")
OUBLIE = acc("oublie")

SEQUENCES = {

# ============================================================================
# SEQUENCE AA — Le marche et les chiffres (lundi)
# ============================================================================
"AA_menage_business_cache": [
    cover("bg_salon_vide", "vu depuis des centaines de comptes conciergerie",
          f'Leur problème n\'est pas les clients. C\'est de trouver du ménage {FIABLE}.',
          sub="Des missions à 60, 70, 80 € restent sans personne pour les "
              "prendre. Pendant que d'autres cherchent un business sans "
              "capital.",
          hand_bottom="pourquoi c'est un autre métier, juste après"),

    p_duo("bg_salon_cosy", "ce n'est pas le même travail",
          "Ménage classique et ménage Airbnb",
          "Chez un particulier",
          ["Tu vends des heures, au taux horaire",
           "Un client, une prestation, à re-prospecter",
           "Les horaires s'arrangent entre vous"],
          "Pour une conciergerie",
          ["Tu vends un résultat : le logement prêt à photographier",
           "Un contrat, c'est un flux de missions toute l'année",
           "Une conciergerie de 30 logements, c'est un portefeuille entier"]),

    p_bigstat("bg_bureau_matin", "l'exemple que donne Sébastien",
              f'Ce que peut peser {UN_SEUL}',
              "11 200 €", "de chiffre d'affaires par mois",
              ["Une conciergerie de 20 logements, environ 160 missions par "
               "mois en moyenne annuelle.",
               "À 70 € la mission en moyenne.",
               "Charges déduites, il reste de l'ordre de 6 000 à 7 000 €."],
              numsize=130),

    p_steps("bg_documents", "les prix qu'il observe sur le terrain",
            "Ce que ça se facture",
            [("Studio ou petit appartement",
              "Entre 40 et 60 €, selon le lieu et la surface."),
             ("T2 ou T3",
              "Entre 60 et 90 €, pour une prestation d'une heure trente à "
              "deux heures trente."),
             ("Maison grande capacité",
              "De 90 à 150 €, voire plus. Trois heures de travail, parfois à "
              "deux. Le linge se compte à part, environ 15 € par chambre.")]),

    focus("bg_cour", "la contrainte que personne ne peut négocier",
          f'Entre 11h et 16h, et c\'est {NON_NEGOCIABLE}.',
          "Ce sont les heures de départ et d'arrivée des voyageurs. Tout se "
          "joue dans cette fenêtre de quatre à cinq heures, et très souvent le "
          "dimanche. Celui qui ne peut pas venir le week-end ne peut pas faire "
          "ce métier."),

    fin("bg_escalier", f'Et disons-le : c\'est {PAS_PASSIF}.',
        "métier physique, week-ends sacrifiés ; la marge vient quand tu montes une équipe"),
],

# ============================================================================
# SEQUENCE AB — Ce qu'une conciergerie regarde vraiment (mardi)
# ============================================================================
"AB_decrocher_contrats": [
    cover("bg_boites_lettres", "si tu veux travailler avec elles",
          "Ce qu'une conciergerie regarde vraiment.",
          sub="Ce n'est pas ce que la plupart des prestataires mettent en "
              "avant dans leur devis.",
          hand_bottom="les quatre critères, juste après"),

    p_steps("bg_facade_pierre", "dans cet ordre précis",
            "Les quatre critères",
            [("La fiabilité, avant le prix",
              "Si tu ne viens pas un dimanche, le voyageur arrive dans un "
              "logement sale. Mauvaise note, et c'est terminé."),
             ("La réactivité",
              "Elles jonglent avec des imprévus permanents : départs tardifs, "
              "pannes, urgences. Qui répond vite récupère la mission."),
             ("La preuve",
              "Photos avant et après, systématiquement. C'est ce qui sépare "
              "l'amateur du professionnel.")]),

    focus("bg_hall_immeuble", "le quatrième, et le plus sous-estimé",
          f'Tu deviens {LES_YEUX} dans le logement.',
          "Signaler un dégât, un consommable à racheter, un objet oublié : "
          "pour une conciergerie qui ne peut pas être partout, ça vaut de "
          "l'or. Ajoute le linge et le réassort, et tu deviens difficile à "
          "remplacer."),

    p_steps("bg_village", "et pour les trouver",
            "Comment décrocher les premiers",
            [("Google Maps, tout simplement",
              "Tape « conciergerie » dans ta ville et contacte-les une à une "
              "en disant que tu es disponible."),
             ("Même celles qui ont déjà une équipe",
              "Elles auront toujours besoin de renfort : c'est là que se "
              "prennent les premières missions."),
             ("Puis laisse-les parler de toi",
              "Les conciergeries se parlent entre elles. Le bouche-à-oreille "
              "est ton meilleur argument commercial.")]),

    fin("bg_lac", f'Le marché est en {PENURIE}.',
        "dans deux ans il sera structuré, et les places prises par ceux qui commencent maintenant"),
],

# ============================================================================
# SEQUENCE AC — Le recrutement (reserve)
# ============================================================================
"AC_recruter_menage": [
    cover("bg_terrasse", "le second goulot d'étranglement",
          "Trouver des clients, c'est la première marche. Recruter, c'est la deuxième.",
          sub="Celui qui sait recruter fait grossir son activité. Les autres "
              "restent seuls, à faire les missions eux-mêmes.",
          hand_bottom="où chercher, juste après"),

    p_steps("bg_chemin_aube", "les canaux qui marchent",
            "Où trouver du personnel",
            [("Les groupes locaux et les petites annonces",
              "Dépose des annonces, fais savoir que tu existes et que tu es "
              "flexible."),
             ("La cooptation",
              "Ceux qui travaillent déjà bien avec toi connaissent d'autres "
              "personnes. Prévois 50 à 100 € pour celui qui t'amène quelqu'un."),
             ("L'hôtellerie en reconversion",
              "Ces personnes sont déjà formées aux standards. C'est le profil "
              "à cibler en priorité.")]),

    p_steps("bg_ville_doree", "avant de faire perdre du temps à tout le monde",
            "Les trois questions qui filtrent",
            [("Es-tu disponible le samedi et le dimanche ?",
              "C'est là que tombent les missions. Une réponse floue est déjà "
              "une réponse."),
             ("As-tu un moyen de transport ?",
              "Sans ça, les logements éloignés sont hors de portée."),
             ("Peux-tu faire une mission d'essai payée cette semaine ?",
              "Puis une vraie mission en binôme avec quelqu'un de formé, payée "
              "normalement. Tu vérifies la ponctualité, le rythme, et le souci "
              "du détail.")]),

    focus("bg_immeuble_dore", "ce que le souci du détail veut dire",
          f'Les endroits que presque tout le monde {OUBLIE}.',
          "Sous le lit. Les joints. L'intérieur du micro-ondes. L'intérieur de "
          "la poubelle une fois le sac retiré, et le tour de la poubelle. Les "
          "poignées du réfrigérateur. C'est là qu'on voit un professionnel."),

    fin("bg_montagne", "Sans checklist précise, tu reformes à chaque fois.",
        "des photos pièce par pièce, le process du linge : la personne devient autonome"),
],

}

SLUG = "banque-09"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
