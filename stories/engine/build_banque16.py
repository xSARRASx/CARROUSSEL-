#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 16 — le complement de banque-14, meme video : « La verite sur le marche
immobilier en 2026 » (ID YouTube iIO-RH_doLo).

⚠️ POURQUOI UNE FOURNEE EN PLUS SUR LA MEME VIDEO. La video fait 29 minutes.
banque-14 en a tire trois sequences et j'ai coupe le reste pour respecter la
regle de variete de Martin (« si tu fais moins de storie c'est pas grave »).
Quand je lui ai dit franchement ce que j'avais laisse de cote, il a demande de
le reprendre. Ce sont donc les morceaux ECARTES le 17/09, et eux seuls :
    - la construction qui s'effondre et la penurie locative a venir ;
    - la dette des menages, qui exclut le krach a l'americaine ;
    - les maisons qui gagnent sur les appartements depuis 2020 ;
    - les trois conditions pour acheter sa residence principale ;
    - les quatre chiffres a surveiller sur douze mois.

⚠️ AUCUN RECOUVREMENT avec banque-14, verifie ligne a ligne : les six
indicateurs, le bouchon, les taux, les trois scenarios et la vente de sa propre
maison sont deja sortis les 21 et 22/09, rien n'est repris ici.

⚠️ C'est le CONTREPOIDS de banque-14, qui etait sombre. Cette sequence dit ce
que les videos catastrophe ignorent. Elle reste factuelle : Sebastien n'invite
pas a acheter, il liste ce qui plaide dans l'autre sens.

⚠️ Forme differente des trois sequences de banque-14 (cover > p_bigstat >
p_bars > focus > p_steps > fin), et six fonds qu'elle n'utilisait pas.

⚠️ Marque LE SOUS LOUEUR (@moresebastien) : le module d'etude de marche cite en
fin de video reste ECARTE.

Rendu : python3 render_stories.py banque-16
"""
from photo_style import (cover, fin, focus, p_steps, p_bars, p_bigstat,
                         acc, write_lot, accroche)

NUM_LOT = 16

# Les apostrophes ne passent pas dans une expression de f-string.
IGNORENT = acc("ignorent")
MOITIE = acc("moitié moins")
PENURIE = acc("pénurie")
PAS_DE_KRACH = acc("pas de bombe de crédit")
MAISONS = acc("les maisons")
NEGOCIE = acc("négocie fort")
SURVEILLER = acc("à surveiller")

SEQUENCES = {

# ============================================================================
# SEQUENCE AX — Ce que les videos catastrophe ignorent (lundi, 6 stories)
# Forme : cover > p_bigstat > p_bars > focus > p_steps > fin
# ============================================================================
"AX_ce_que_les_catastrophistes_ignorent": [
    cover("bg_champ_ete", "l'autre moitié du dossier",
          f'Trois choses que les vidéos catastrophe {IGNORENT}.',
          sub="Elles sont dans le même document que les chiffres qui font "
              "peur. Simplement, personne ne les regarde.",
          hand_bottom=accroche(NUM_LOT + 1)),

    p_bigstat("bg_mur_beton", "la construction s'effondre",
              "Et ça ne se voit pas tout de suite",
              "297 000", "logements commencés sur douze mois, contre plus de "
                         "500 000 en 2017",
              [f'On construit {MOITIE} qu\'il y a dix ans.',
               "Aujourd'hui ça ne soutient pas les prix : le problème du "
               "moment, c'est la solvabilité, pas le manque de logement.",
               f'Mais dans cinq ans, ça fait une {PENURIE}. Et une pénurie '
               f'pousse les loyers, qui sont justement au plus bas.'],
              numsize=130),

    p_bars("bg_foret_automne", "pourquoi le krach américain n'aura pas lieu ici",
           "La dette des ménages, rapportée au revenu disponible",
           [("Pays-Bas", 200),
            ("Royaume-Uni", 100),
            ("France", 76)],
           note="En France elle baisse même depuis son pic. Pas de bombe de "
                "crédit, donc pas de ventes forcées massives, donc pas de 2008 "
                "à l'américaine."),

    focus("bg_cafe_table", "le déplacement que personne n'avait vu venir",
          f'Depuis 2020, {MAISONS} ont gagné sur les appartements.',
          "Le télétravail, la fuite des copropriétés, le diagnostic énergie, "
          "les charges, les règles qui encadrent la courte durée en "
          "copropriété. Autant de contraintes qui ne touchent pas une maison. "
          "L'écart s'est creusé sans bruit."),

    p_steps("bg_etagere", "et si tu achètes ta résidence principale",
            "Trois conditions, pas deux",
            [("Négocie vraiment",
              "On est sur un marché acheteur : des offres à 10 ou 15 % en "
              "dessous sur un bien qui traîne ne sont pas déplacées."),
             ("Reste plus de dix ans",
              "Le pouvoir d'achat immobilier est au plus bas depuis 1980 : "
              "avec le même effort qu'en 2000, on achète 26 % de logement en "
              "moins. Il faut du temps pour absorber ça."),
             ("N'emprunte pas sur 25 ans un bien qui peut perdre 10 %",
              "Sinon tu dois plus que ce que vaut ta maison, pendant des "
              "années. Et si tu n'es pas pressé, louer deux ans de plus n'est "
              "pas une hérésie.")]),

    fin("bg_toits_pluie", f'Quatre chiffres {SURVEILLER} sur douze mois.',
        "le taux de la dette de l'État au-dessus de 4 %, le taux moyen des crédits à 3,5 %, les ventes sous 900 000, et le budget 2027"),
],

}

SLUG = "banque-16"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
