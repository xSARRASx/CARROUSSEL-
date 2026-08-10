#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE 03 — vidéo du dimanche : ta copropriété peut interdire ton Airbnb
(ID YouTube sICVVkMpSl4).

⚠️ Le titre YouTube est traduit en anglais ("Your HOA can block your Airbnb") :
seule la transcription française fait foi.

Vidéo TRES riche (24 000 caractères, sujet juridique très concret, avec deux
arrêts datés et deux checklists) -> 3 séquences complètes, conformément à
l'objectif STOCK de Martin. Contenu 100 % issu de la transcription : aucune
date, aucun chiffre, aucune juridiction inventés.

Le fil du raisonnement, tel que Sébastien le déroule :
    L — le nouveau pouvoir de la copropriété, et les deux détails que presque
        personne ne mentionne (le second vote, l'autodénonciation) ;
    M — la parade : la location courte durée n'est pas commerciale, donc la
        3e condition du vote tombe ;
    N — les deux checklists : investisseur avant d'acheter, conciergerie
        avant de signer.

Style : celui de photo_style.py (photo fait main, logo partout), fonds tous
différents à l'intérieur d'une même séquence.

Rendu : python3 render_stories.py banque-03
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bigstat,
                         p_duo, p_vs, acc, write_lot)

o = acc

# Les apostrophes ne passent pas dans une f-string : on sort les morceaux.
COMMERCIALE = acc("commerciale")
CIVILE = acc("civile")
DEUX_TIERS = acc("deux tiers")
TOI_MEME = acc("toi-même")
EXPLOITES = acc("exploites")
# Les mots accentues qui contiennent une apostrophe ne peuvent pas etre
# construits dans une f-string (Python refuse le backslash dedans).
TROMPE_OEIL = acc("trompe-l'oeil")
OPPOSABLE = acc("opposable")
ARGUMENT_VENTE = acc("argument de vente")
COMMERCIAL_MOT = acc("commercial")
UN_SEUL_MOT = acc("un seul mot")

SEQUENCES = {

# ============================================================================
# SEQUENCE L — Le nouveau pouvoir de la copropriété
# ============================================================================
"L_copro_peut_interdire": [
    cover("bg_facade_pierre", "validé le 19 mars 2026",
          f'Ta copropriété peut {acc("interdire")} ta location courte durée.',
          sub="Le Conseil constitutionnel a tranché. Le débat est clos. "
              "Mais il reste une parade, et elle tient à un seul mot.",
          hand_bottom="ce qui a changé, juste après"),

    p_duo("bg_escalier", "le rapport de force s'est inversé",
          f'Avant et après la loi {o("Le Meur")}',
          "Avant", ["Il fallait changer la destination complète de l'immeuble",
                    "Et ça demandait l'unanimité des copropriétaires",
                    "Toi, exploitant, tu votais contre : ça n'arrivait jamais"],
          "Depuis", ["L'assemblée générale peut interdire le meublé de tourisme",
                     "À la majorité des deux tiers des voix",
                     "Ton droit de veto de fait a disparu"]),

    p_steps("bg_hall_immeuble", "et elles sont cumulatives",
            f'Les {o("3 conditions")} du vote',
            [("Ce ne sont pas des résidences principales",
              "Les lots visés ne sont pas la résidence principale de leur occupant. "
              "Quand on investit, c'est donc a priori concerné."),
             ("Ils sont à usage d'habitation",
              "Deuxième condition, la plus simple à remplir."),
             ("Le règlement interdit toute activité commerciale",
              "C'est LA condition sur laquelle tout se joue. Retiens bien ce mot : "
              "commerciale. La parade est cachée dedans.")]),

    focus("bg_boites_lettres", "le détail n° 1",
          f"Les {DEUX_TIERS}, c'est un {TROMPE_OEIL}.",
          body="Si les deux tiers ne sont pas atteints au premier vote mais que la "
               "résolution obtient la majorité des voix de tous les copropriétaires, "
               "un second vote peut la faire passer à cette majorité. Autrement dit, "
               "en pratique, l'interdiction devient accessible à la majorité simple.",
          hand="et ce n'est pas le pire"),

    p_timeline("bg_documents", "le détail n° 2",
               f'La machine à {o("autodénonciation")}',
               [("Tu déclares ton meublé en mairie",
                 "C'est obligatoire. Le téléservice Déclaloc a été officialisé en mai 2026. "
                 "Beaucoup de petites communes n'y sont pas encore.", None),
                ("Tu dois informer ton syndic",
                 "Ce n'est pas une option, c'est prévu par le texte.", None),
                ("Le syndic inscrit un point à l'ordre du jour",
                 "Un point d'information sur ton activité, à la prochaine assemblée "
                 "générale.", None),
                ("Ta déclaration légale déclenche le débat",
                 "Tu te signales toi-même. Le sujet arrive sur la table sans que "
                 "personne dans l'immeuble ait eu à le demander.", None)]),

    fin("bg_cour",
        "Les AG de 2026 et 2027 vont voir une vague de résolutions. Pas parce que "
        "les copropriétaires se sont réveillés : parce que la machine a mis le sujet "
        "sur la table à leur place.",
        "la parade arrive demain"),
],

# ============================================================================
# SEQUENCE M — La parade : rester dans le civil
# ============================================================================
"M_parade_rester_civil": [
    cover("bg_cles", "presque personne n'en parle",
          f"La parade tient à {UN_SEUL_MOT}.",
          sub="La troisième condition du vote exige que le règlement interdise "
              "l'activité commerciale. Reste à savoir si la tienne en est une.",
          hand_bottom="la réponse est dans un arrêt"),

    focus("bg_salon_vide", "Cour de cassation, 25 janvier 2024",
          f"Non, ce n'est pas une activité {COMMERCIALE}.",
          body="La réponse est très claire : la location courte durée n'est pas une "
               "activité commerciale, tant que tu ne fournis pas de services "
               "para-hôteliers. Même à la nuitée. Même sur Airbnb. Ça reste une "
               "activité civile.",
          hand="alors qu'est-ce qui fait basculer ?"),

    p_vs("bg_terrasse", "la frontière exacte", f'Civil ou {o("commercial")} ?',
         "Commercial", ["Une réception permanente",
                        "Des prestations automatiques",
                        "Incluses pour tous les voyageurs",
                        "Bref : tu singes l'hôtel"],
         "Civil", ["Le ménage reste optionnel",
                   "La remise de clés",
                   "Le petit-déjeuner en option",
                   "Services en option, facturés à part"],
         "Ta protection ne dépend pas du vote de tes voisins. Elle dépend de la "
         "manière dont tu exploites."),

    focus("bg_village", "Cour d'appel d'Aix-en-Provence, 20 mars 2025",
          f"L'interdiction n'était pas {OPPOSABLE}.",
          body="Une location avec seulement deux prestations optionnelles, dépôt de "
               "bagages et petit-déjeuner, garde sa nature civile. Conséquence directe : "
               "l'interdiction votée sur le fondement des activités commerciales ne "
               "pouvait pas lui être opposée. Le vote existait, et il ne servait à rien."),

    p_duo("bg_ciel_dore", "le paradoxe qui pique",
          f'Ton argument {o("marketing")} devient une pièce à conviction',
          "Ce que le marché adore vendre",
          ["L'accueil personnalisé systématique",
           "Le petit-déjeuner inclus",
           "L'expérience hôtelière à domicile"],
          "Ce que ça produit vraiment",
          ["C'est exactement ce qui rend ton annonce interdisable",
           "Tu fournis toi-même la preuve au syndic",
           "Ceux qui vendent ces prestations n'ont aucun intérêt à te le dire"]),

    focus("bg_bureau_matin", "et relis ton règlement",
          f"S'il tolérait déjà le {COMMERCIAL_MOT}, tu es tranquille.",
          body="Si le règlement de copropriété autorisait à la base les activités "
               "commerciales ou libérales, un docteur, un huissier, alors on ne peut "
               "pas te reprocher la tienne. D'autant qu'on vient de le démontrer : "
               "la tienne est civile."),

    fin("bg_lac",
        "Une exploitation purement locative, services en option, facturés à part, "
        "sans réception : c'est ton bouclier juridique.",
        "la checklist arrive demain"),
],

# ============================================================================
# SEQUENCE N — Les deux checklists
# ============================================================================
"N_checklist_copro": [
    cover("bg_immeuble_dore", "avant d'acheter, avant de signer",
          f'La {acc("checklist")} que personne ne fait.',
          sub="Deux listes : une pour l'investisseur, une pour la conciergerie. "
              "Sors de quoi noter.",
          hand_bottom="on commence par l'investisseur"),

    p_steps("bg_documents", "si tu investis", f'Les {o("4")} vérifications',
            [("Lis le règlement de copropriété",
              "En entier. C'est là que se joue le futur de ton activité."),
             ("Récupère les PV des 3 dernières AG",
              "Des décisions ont pu être prises sans jamais être recopiées dans le "
              "règlement. Les procès-verbaux les rattrapent."),
             ("Regarde s'il est postérieur au 21 novembre 2024",
              "Depuis cette date, le règlement doit dire explicitement si le meublé de "
              "tourisme est autorisé ou non. Avant, l'activité n'existait pas dans les textes."),
             ("Vérifie le régime de changement d'usage",
              "Une autorisation préalable est-elle exigée dans cette commune ? "
              "En zone tendue, l'amende arrive vite.")]),

    focus("bg_hall_immeuble", "le piège classique",
          f'Deux contrôles {acc("cumulatifs")}, pas un.',
          body="La copropriété peut dire oui et la mairie dire non. Et l'inverse est "
               "vrai aussi. Ce sont deux étages différents, et ils s'additionnent : "
               "valider l'un ne dispense jamais de vérifier l'autre.",
          hand="et pour une conciergerie ?"),

    p_steps("bg_cour", "si tu es conciergerie", f'Les {o("4")} réflexes',
            [("Demande le règlement au propriétaire",
              "Le document lui-même, ou une attestation signée de sa part."),
             ("Demande les PV des assemblées générales",
              "Et l'information du syndic : est-ce qu'ils ont validé, ou pas ?"),
             ("Structure tes prestations",
              "Ne crée pas le risque commercial chez ton client. Proposer toi-même les "
              "petits-déjeuners, c'est fabriquer du service para-hôtelier."),
             ("Documente tout",
              "Une ligne dans ton contrat, les justificatifs archivés, la déclaration "
              "sur l'honneur du propriétaire. La preuve que tu as posé les questions.")]),

    focus("bg_ville_doree", "ce que personne ne voit venir",
          f"Cette checklist est un {ARGUMENT_VENTE}.",
          body="Un propriétaire qui compare deux conciergeries, dont une seule lui "
               "parle du règlement de copropriété : il voit tout de suite laquelle "
               "tient la route. C'est de la conformité, et c'est du commercial en "
               "même temps."),

    p_duo("bg_montagne", "si la copro vote alors que tu exploites déjà",
          f'La zone de {o("combat")} des prochaines années',
          "Ce que la loi ne prévoit pas",
          ["Aucune clause du grand-père",
           "Aucune protection des activités existantes",
           "Aucune indemnisation"],
          "Le garde-fou du Conseil constitutionnel",
          ["L'interdiction doit être justifiée par la destination de l'immeuble",
           "Sous le contrôle du juge",
           "Le vote seul ne suffit pas : ça se conteste"]),

    fin("bg_chemin_aube",
        "Si tu exploites déjà : va lire ton règlement et les PV dès maintenant. "
        "Et repasse en civil pur avant la prochaine convocation.",
        "tout est détaillé dans la vidéo"),
],

}

SLUG = "banque-03"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
