#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 02 — vidéo du 10 juillet 2026 : la conciergerie condamnée à 220 000 €
(ID YouTube YiAaGhoimhA).

⚠️ Le titre YouTube est traduit en anglais ("The Court Ruling Shaking Up
Property Management Agencies") : seule la transcription française fait foi.

Vidéo TRES riche (5 300 mots, sujet juridique concret) -> on en tire 3
séquences complètes, conformément à l'objectif STOCK de Martin. Contenu
100 % issu de la transcription, aucun chiffre inventé.

Style : celui de photo_style.py (photo fait main, logo partout), fonds tous
différents à l'intérieur d'une même séquence.

Rendu : python3 render_stories.py banque-02
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         p_duo, p_vs, p_cta, acc, write_lot)

o = acc

SEQUENCES = {

# ============================================================================
# SEQUENCE I — L'affaire des 220 000 € (le fait juridique)
# ============================================================================
"I_condamnation_220k": [
    cover("bg_immeuble_dore", "une première en France",
          f'{acc("220 000 €")} d\'amende. Pour le proprio ET pour la conciergerie.',
          sub="Tribunal judiciaire de Paris, 10 juillet 2026. Ce qui s'est vraiment "
              "passé, et ce que ça change pour toi.",
          hand_bottom="les faits, juste après"),
    p_bigstat("bg_ville_doree", "le verdict", f'La {o("double")} condamnation',
              "220 000 €", "pour le propriétaire. Et la même somme pour la conciergerie.",
              ["4 logements loués en courte durée dans les 7e et 8e arrondissements de Paris.",
               "Aucune autorisation de changement d'usage, alors qu'elle est exigée à Paris.",
               "Recettes estimées par la ville : environ 410 000 € entre 2022 et 2024."],
              numsize=150),
    focus("bg_bureau_matin", "la phrase qui change tout",
          f'Condamnée pour ce qu\'elle n\'a pas {acc("vérifié")}.',
          body="La conciergerie n'a pas été condamnée pour quelque chose qu'elle a fait. "
               "Elle a été condamnée pour quelque chose qu'elle n'a pas vérifié. Le "
               "tribunal a jugé qu'un professionnel de la location saisonnière ne peut "
               "pas ignorer la réglementation locale."),
    p_steps("bg_village", "le détail qui a plombé le dossier", f'Si tu es {o("contrôlé")} un jour',
            [("Les annonces étaient encore en ligne", "Au moment de l'audience, elles tournaient toujours. Ça a aggravé le dossier."),
             ("Le réflexe : tu coupes tout", "Dès le moindre courrier, tu coupes immédiatement. Ça ne sert à rien de se justifier."),
             ("Tu le précises par écrit", "Tu indiques que tu as préféré couper par précaution, en attendant la discussion. Ça montre ta bonne foi.")]),
    p_duo("bg_terrasse", "ce qui a changé", f'Avant et après la loi {o("Le Meur")}',
          "Avant 2024", ["Le texte protégeait les intermédiaires",
                         "L'amende visait uniquement celui qui louait",
                         "Le contrôle se faisait à la main, au hasard"],
          "Depuis", ["Les intermédiaires peuvent être sanctionnés, jusqu'à 100 000 €",
                     "Airbnb et Booking ne sont pas dans l'histoire : la responsabilité est sur toi",
                     "Téléservice national d'enregistrement depuis mai 2026 : détection quasi en temps réel"]),
    fin("bg_salon_cosy",
        "Paris a ouvert le bal. Les autres zones tendues vont suivre.",
        "la vidéo complète est sur la chaîne"),
],

# ============================================================================
# SEQUENCE J — La checklist avant de publier une annonce
# ============================================================================
"J_checklist_conformite": [
    cover("bg_bureau_matin", "aide gratuite",
          f'La {acc("checklist")} à faire avant de publier une annonce.',
          sub="Ce qu'une conciergerie doit vérifier pour chaque bien, avant la mise "
              "en ligne. Point par point.",
          hand_bottom="c'est cadeau, juste après"),
    p_steps("bg_lac", "les 3 premiers points", f'Le {o("statut")} et la commune',
            [("Résidence principale ou secondaire ?", "Le régime change complètement selon la réponse. C'est la toute première question."),
             ("La commune est-elle concernée ?", "Paris et les villes de plus de 200 000 habitants : oui pour le changement d'usage. En dessous : non pour le moment, mais ça bouge."),
             ("Exige la copie de l'autorisation", "Résidence secondaire en zone concernée : tu demandes le papier au propriétaire. Pas de papier, pas d'annonce.")]),
    p_steps("bg_montagne", "les 3 suivants", f'Le numéro et la {o("trace écrite")}',
            [("Le numéro d'enregistrement", "Il doit figurer sur chaque annonce et sur chaque plateforme, sans exception."),
             ("Le compteur de nuitées", "Résidence principale : 120 jours, et 90 jours à Paris. Un vrai compteur, pas un peu ici et un peu là."),
             ("La trace écrite", "Une clause du contrat qui liste les déclarations du propriétaire, plus les justificatifs et les attestations.")]),
    p_bigstat("bg_ciel_rose", "les deux étages de sanctions", f'Elles se {o("cumulent")}',
              "12 500 €", "d'amende pour l'intermédiaire sur le numéro d'enregistrement, et jusqu'à 50 000 € pour certains manquements.",
              ["Étage 1 : le changement d'usage. C'est l'affaire à 220 000 €.",
               "Étage 2 : la déclaration et le numéro. Côté loueur, jusqu'à 10 000 € pour défaut de déclaration.",
               "50 000 € pour dépassement des 120 jours en résidence principale.",
               "Le numéro ne protège pas du changement d'usage, et l'inverse non plus."],
              numsize=140),
    p_duo("bg_plage_aube", "les lignes rouges", f'Ce qu\'une conciergerie ne peut {o("pas")} faire',
          "Jamais", ["Encaisser le loyer pour le compte du propriétaire",
                     "Signer les contrats de location à sa place",
                     "Mettre les annonces sur ton propre compte Airbnb ou Booking",
                     "Te présenter comme gestionnaire ou administrateur de biens"],
          "À la place", ["Tu fais de la prestation de services : ménage, linge, voyageurs, communication",
                         "Le propriétaire reste pilote de son annonce, de ses prix et de son calendrier",
                         "Dans ton contrat et sur ton site : le mot prestation, pas le mot gestion"]),
    p_cta("bg_ciel_dore", "on regarde ton organisation ensemble", "Ta conciergerie est carrée ?",
          "GO", "Réponds GO et on fait le point sur ta structure."),
],

# ============================================================================
# SEQUENCE K — Le mythe de la carte G
# ============================================================================
"K_mythe_carte_g": [
    cover("bg_village", "on met les choses au clair",
          f'La carte G, ce {acc("bouclier")} qui n\'a servi à rien.',
          sub="Dans le premier grand procès du secteur, elle n'apparaît nulle part. "
              "Voici ce que dit vraiment le droit.",
          hand_bottom="calmement, juste après"),
    focus("bg_immeuble_dore", "dans l'affaire à 220 000 €",
          f'La carte G n\'apparaît {acc("nulle part")}.',
          body="La conciergerie n'a pas été condamnée pour avoir exercé sans carte. "
               "Elle a été condamnée pour avoir géré des locations sans autorisation "
               "de changement d'usage. Le tribunal ne lui reproche pas un défaut de "
               "statut : il lui reproche un défaut de vérification."),
    p_vs("bg_terrasse", "la vraie frontière", f'Quand la carte G est {o("obligatoire")}',
         "Elle l'est", ["Pour la gestion immobilière pour le compte d'autrui.",
                        "Encaisser les loyers, recevoir des fonds sur son compte, gérer les baux.",
                        "Sans elle, dans ce cadre, c'est illégal."],
         "Elle ne l'est pas", ["Pour un modèle de prestation de services.",
                               "Ménage, linge, voyageurs, communication, petits problèmes du logement.",
                               "Les outils de tarification restent sous contrôle du propriétaire."],
         "Dire que les conciergeries sans carte G sont dans l'illégalité est faux. "
         "La frontière a été posée par la loi elle-même."),
    p_steps("bg_prairie", "ce que le juge regarde vraiment", f'Les {o("3 briques")} d\'une conciergerie',
            [("Le contractuel et la documentation", "Le contrat, mais aussi tous les documents et attestations que le propriétaire te fournit."),
             ("Le mode opératoire", "En 2025, des juges ont regardé au-delà du contrat : ce que la conciergerie faisait vraiment au quotidien. Gérer les prix, les calendriers et les incidents tout seul, c'est condamnable."),
             ("L'outil", "On te demandera des preuves, pas des explications. Il faut pouvoir démontrer, avec du reporting.")]),
    fin("bg_chemin_aube",
        "« On ne gère pas le bien. On gère des prestations. C'est différent. »",
        "et toi, tu es organisé comment ?"),
],

}

SLUG = "banque-02"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
