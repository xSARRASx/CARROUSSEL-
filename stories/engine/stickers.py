#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LE TEXTE EXACT DE CHAQUE STICKER INSTAGRAM.

Manque signalé par Martin le 06/08/2026 : la livraison disait QUELLES images
réclament un sticker, mais pas QUOI TAPER dedans. Il devait redemander à
chaque fois. Ce fichier est la source de vérité : l'info voyage désormais
avec les images, dans `manuel/_STICKERS.txt`.

⚠️ RÈGLE : toute nouvelle story qui promet un vote DOIT avoir son entrée ici,
au moment où elle est écrite. Sans entrée, `_STICKERS.txt` signale le trou et
le contrôle de livraison échoue.

LES TROIS STICKERS INSTAGRAM
    "Sondage"   : 2 à 4 options, pas de bonne réponse. Pour les diagnostics.
    "Quiz"      : 2 à 4 options AVEC une bonne réponse à cocher. Pour les quiz.
    "Questions" : boîte à questions ouverte, sans option. Pour « raconte-moi ».

⚠️ POURQUOI NOS QUIZ UTILISENT LE STICKER "SONDAGE" ET NON "QUIZ"
(erreur repérée par Martin le 08/08/2026, corrigée le jour même)
    Le sticker "Quiz" d'Instagram révèle la bonne réponse À L'INSTANT du vote.
    Or nos séquences de quiz sont construites autrement : la question est une
    story, et la RÉPONSE est la story suivante — l'image dit d'ailleurs
    « vote avec le sondage, la réponse arrive ». Avec un sticker Quiz, la
    réponse serait donnée deux fois et la story suivante n'aurait plus
    d'intérêt : le suspense tombe.
    Donc : question de quiz -> sticker SONDAGE. Le champ `reponse` reste noté
    ici pour mémoire, mais il ne se coche nulle part.
"""

# nom du fichier source (sans .jpg) -> ce qu'il faut taper dans le sticker
STICKERS = {

    # ===================== interactifs-01 : le quiz Airbnb 2026 ==============
    "quiz_02": {
        "type": "Sondage",
        "question": "Le badge Superhost booste ton classement en 2026.",
        "options": ["Vrai", "Faux"],
        "reponse": "Faux",
    },
    "quiz_04": {
        "type": "Sondage",
        "question": "Combien pèse ta photo de couverture dans ton classement ?",
        "options": ["8 %", "15 %", "30 %"],
        "reponse": "8 %",
    },
    "quiz_06": {
        "type": "Sondage",
        "question": "Ta conciergerie peut débiter elle-même la caution du voyageur.",
        "options": ["Vrai", "Faux"],
        "reponse": "Faux",
    },

    # ===================== interactifs-01 : les sondages diagnostic ==========
    "sondage_01": {
        "type": "Sondage",
        "question": "Tu es plutôt conciergerie ou sous-location ?",
        "options": ["Conciergerie", "Sous-location"],
    },
    "sondage_02": {
        "type": "Sondage",
        "question": "Ta plus grosse galère en ce moment ?",
        "options": ["Trouver des proprios", "Remplir mon calendrier",
                    "M'organiser", "Le juridique"],
    },
    "sondage_03": {
        "type": "Questions",
        "question": "Raconte-moi ta situation en une phrase",
        "options": [],
    },

    # ===================== interactifs-02 : le quiz condamnation =============
    "quiz02_02": {
        "type": "Sondage",
        "question": "Avoir la carte G aurait évité la condamnation de la conciergerie.",
        "options": ["Vrai", "Faux"],
        "reponse": "Faux",
    },
    "quiz02_04": {
        "type": "Sondage",
        "question": "Qui a été condamné à 220 000 € ?",
        "options": ["Le propriétaire", "La conciergerie", "Les deux"],
        "reponse": "Les deux",
    },
    "quiz02_06": {
        "type": "Sondage",
        "question": "Le numéro d'enregistrement dispense de l'autorisation de changement d'usage.",
        "options": ["Vrai", "Faux"],
        "reponse": "Faux",
    },

    # ===================== interactifs-02 : les sondages =====================
    "sondage02_01": {
        "type": "Sondage",
        "question": "Tu vérifies l'autorisation de changement d'usage avant de publier ?",
        "options": ["Toujours", "Parfois", "Jamais", "C'est quoi ?"],
    },
    "sondage02_02": {
        "type": "Sondage",
        "question": "Ton contrat conciergerie, il date de quand ?",
        "options": ["Moins d'un an", "1 à 3 ans", "Plus de 3 ans", "Je n'en ai pas"],
    },

    # ===================== semaine-01 : les diagnostics isolés ===============
    # ⚠️ Ces deux-la posent EXACTEMENT la meme question que sondage_02 et
    # sondage_03. Repere par Martin le 08/08/2026 : le calendrier les
    # programmait a une semaine d'intervalle, on posait deux fois la meme
    # question a la communaute. Ils restent ici (l'image existe, elle peut
    # servir de rechange) mais `DOUBLONS` les tient hors de la programmation.
    "lundi_02_sondage": {
        "type": "Sondage",
        "question": "Ta plus grosse galère en ce moment ?",
        "options": ["Trouver des proprios", "Remplir mon calendrier",
                    "M'organiser", "Le juridique"],
    },
    "lundi_03_questions": {
        "type": "Questions",
        "question": "Raconte-moi ta situation en une phrase",
        "options": [],
    },
    "mercredi_03_question": {
        "type": "Questions",
        "question": "Tu en es où de ton projet ?",
        "options": [],
    },
    "samedi_01_radar": {
        "type": "Questions",
        "question": "Tu en es où aujourd'hui ?",
        "options": [],
    },
}

# Stories qui posent la MEME question qu'une autre : on n'en programme qu'une.
# La valeur dit de quelle story elle est le doublon (celle qu'on garde).
DOUBLONS = {
    "lundi_02_sondage":   "sondage_02",
    "lundi_03_questions": "sondage_03",
}

def fiche(nom_source):
    """Renvoie la fiche du sticker, ou None si la story n'en a pas besoin."""
    return STICKERS.get(nom_source)

def est_doublon(nom_source):
    """Vrai si cette story repete une question deja posee ailleurs."""
    return nom_source in DOUBLONS

def bloc_texte(entrees):
    """Compose le contenu de `manuel/_STICKERS.txt`.

    `entrees` = liste de (nom du fichier livré, nom de la story source).
    """
    lignes = [
        "CE QU'IL FAUT TAPER DANS CHAQUE STICKER",
        "=" * 62,
        "",
        "Ces stories ne peuvent pas etre programmees : Instagram interdit de",
        "poser un sticker sur une story planifiee. Tu les postes a la main, et",
        "tu recopies exactement la question et les options ci-dessous.",
        "",
        "Les trois stickers Instagram :",
        "  Sondage    : 2 a 4 options, pas de bonne reponse.",
        "  Quiz       : 2 a 4 options AVEC une bonne reponse a cocher.",
        "  Questions  : boite a questions ouverte, sans option.",
        "",
        "=" * 62,
        "",
    ]
    manquants = []
    for fichier, source in entrees:
        f = fiche(source)
        if not f:
            manquants.append(fichier)
            continue
        lignes.append(f"--- {fichier}")
        lignes.append(f"    Sticker  : {f['type']}")
        lignes.append(f"    Question : {f['question']}")
        if f.get("options"):
            for i, o in enumerate(f["options"], 1):
                lignes.append(f"    Option {i} : {o}")
        if f.get("reponse"):
            if f["type"] == "Quiz":
                lignes.append(f"    Bonne reponse a cocher : {f['reponse']}")
            else:
                # Sondage : rien a cocher. La reponse est la story SUIVANTE.
                lignes.append(f"    (La bonne reponse est \"{f['reponse']}\", mais ne la")
                lignes.append(f"     coche PAS : elle est revelee dans la story suivante.)")
        lignes.append("")
    if manquants:
        lignes += [
            "!" * 62,
            "ATTENTION : texte de sticker MANQUANT pour :",
        ] + [f"  - {m}" for m in manquants] + [
            "Ajoute leur entree dans stories/engine/stickers.py.",
            "!" * 62, "",
        ]
    return "\n".join(lignes) + "\n", manquants

if __name__ == "__main__":
    print(f"{len(STICKERS)} stickers documentes :\n")
    for nom, f in STICKERS.items():
        opts = " / ".join(f["options"]) if f["options"] else "(boite ouverte)"
        print(f"  {nom:22s} {f['type']:10s} {f['question']}")
        print(f"  {'':22s} {'':10s} {opts}")
