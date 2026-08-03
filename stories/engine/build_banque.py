#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE DE SEQUENCES V5 : stories "aide gratuite" auto-suffisantes, construites
a partir des transcriptions des videos YouTube de Sebastien (@moresebastien).

DECISION DE MARTIN (03/08/2026, sur capture de la cover sequence A) :
  - TOUTES les stories dans le style "photo fait main" (fond photo chaud,
    serif blanche + bleu, annotations manuscrites, voile blanc pour le dense).
    La famille "marque" navy/orange est ABANDONNEE pour les stories.
  - LOGO sur toutes les stories, sans exception.
  - FONDS VARIES : jamais deux fois le meme fond dans une sequence
    (15 fonds chauds en rotation, voir gen_background.py).

Le style vit dans photo_style.py (socle commun a tous les builds).
Chaque story reste complete et prete a poster. Contenu 100 % tire des
transcriptions (rien d'invente).
Rendu : python3 render_stories.py banque-01
"""
from photo_style import (cover, focus, fin, p_steps, p_timeline, p_bars,
                         p_bigstat, p_duo, p_vs, p_formula, p_cta,
                         acc, write_lot)

o = acc      # dans l'ancien style, o() = accent orange ; desormais tout est bleu

SEQUENCES = {

# ============================================================================
# SEQUENCE A — Remplir son Airbnb sans baisser les prix (video URH12GYwAuc)
# fonds : mer_calme / plage_aube / ciel_dore / lac / terrasse / montagne
# ============================================================================
"A_remplir_sans_baisser": [
    cover("bg_mer_calme", "aide gratuite",
          f'Remplir ton Airbnb {acc("sans baisser")} tes prix.',
          sub="Airbnb ne classe pas par prix : il met en avant ce qui convertit. "
              "Voici les leviers concrets.",
          hand_bottom="du concret, juste après"),
    p_vs("bg_plage_aube", "levier 1", f'Le {o("tarif par voyageur")}',
         "Ce que tout le monde fait", ["120 € la nuit,", "pour tout le monde,", "quel que soit le nombre de voyageurs."],
         "Ce que font les pros", ["95 € pour 2 voyageurs", "+ 12 € par voyageur en plus.", "Couple : 95 €. Famille de 4 : 119 €."],
         "La majorité des recherches se font en réglage par défaut (1-2 voyageurs) : "
         "tu t'affiches à 95 € et tu passes devant les annonces à 120 €."),
    p_bigstat("bg_ciel_dore", "levier 2, ignoré par 90 % des hôtes", f'Le tarif {o("non remboursable")}',
              "-10&nbsp;%", "affiché dans les résultats de recherche.",
              ["Ton annonce paraît moins chère, donc mieux classée.",
               "La remise ne s'applique qu'à ceux qui acceptent le non remboursable.",
               "Ceux-là n'auraient jamais annulé : tu offres 10 % à des résas en béton."]),
    p_steps("bg_lac", "levier 3", f'Les équipements sont des {o("filtres")}',
            [("Coche TOUT ce que tu as", "Non coché = invisible pour celui qui filtre. Sèche-cheveux, fer, détecteur de fumée : pense aux oubliés."),
             ("Le combo famille", "Lit parapluie + chaise haute : tu ressors dans les filtres famille plusieurs fois."),
             ("Le canal télétravail", "Un vrai espace de travail, et le débit wifi mesuré écrit dans l'annonce.")]),
    p_steps("bg_terrasse", "leviers 4 et 5", f'Ta {o("vitrine")} : photo, titre, avis',
            [("La couverture, jamais le salon", "Montre le distinctif : la vue, le jacuzzi, la terrasse. En miniature, un salon ressemble à tous les salons."),
             ("Le titre en 50 caractères", "Capacité + atout star + lieu : « 6 personnes, jacuzzi, 5 min de la plage »."),
             ("Les avis à mots-clés", "L'algorithme lit le texte des avis. Invite tes voyageurs à citer le jacuzzi, le check-in... pendant 6 mois.")]),
    p_cta("bg_montagne", "on te dit ce que vaut ton annonce", "Tu veux ton audit ?",
          "AUDIT", "On t'envoie l'outil d'audit gratuit en DM."),
],

# ============================================================================
# SEQUENCE B — Trouver des proprios : les 5 canaux (video Kjml8l9gNwg)
# fonds : ciel_dore / ville_doree / village / bureau_matin / immeuble_dore / prairie
# ============================================================================
"B_trouver_clients": [
    cover("bg_ciel_dore", "la méthode des pros",
          f'Trouver des proprios : les {acc("5 canaux")}, classés.',
          sub="Du moins au plus efficace. Ce que font les property managers "
              "américains, adapté à la France.",
          hand_bottom="le classement arrive"),
    p_bars("bg_ville_doree", "du moins au plus efficace", f'Les 5 canaux, {o("classés")}',
           [("5. Prospection ciblée", 20),
            ("4. Apporteurs d'affaires", 40),
            ("3. Agents immobiliers", 60),
            ("2. Référence locale (Google)", 80),
            ("1. L'audit chiffré", 100)],
           note="Les % = efficacité relative d'après le classement de la vidéo. "
                "Le n°1 est détaillé juste après."),
    focus("bg_village", "le canal n°1",
          f'Fais un {acc("audit")}, pas un pitch.',
          body="Repère une annonce qui sous-performe : mauvaises notes, trous en "
               "juillet, prix qui ne bougent jamais. Chiffre son manque à gagner avec "
               "un outil de data : « tu perds peut-être 8 000 € par an ». Tu offres "
               "l'info, tu ne vends rien : le proprio voit le chiffre tout seul."),
    p_duo("bg_bureau_matin", "côté légal", f'Les {o("pièges")} à éviter',
          "Jamais", ["Prospecter via la messagerie Airbnb : bannissement possible",
                     "Le pitch commercial direct : valeur perçue zéro"],
          "À la place", ["Retrouve le proprio ailleurs : son site, sa fiche Google, Le Bon Coin",
                         "Offre l'audit et laisse les chiffres parler"]),
    p_bigstat("bg_immeuble_dore", "l'astuce que personne ne fait", f'Les avis Google de {o("proprios")}',
              "15", "avis de propriétaires satisfaits, et tu écrases la concurrence locale.",
              ["Celui qui tape « conciergerie + ta ville » est un prospect chaud.",
               "Demande les avis à tes PROPRIOS, pas à tes voyageurs.",
               "Bonus : une page par quartier, même par rue. Sur « conciergerie + ta rue », il n'y a personne."],
              numsize=210),
    p_cta("bg_prairie", "acquisition", "On regarde ton plan ensemble ?",
          "GO", "Réponds GO et on fait le point sur ta stratégie."),
],

# ============================================================================
# SEQUENCE C — Recuperer les proprios decus (video t_sxyIULJEQ)
# fonds : ville_doree / salon_cosy / ciel_rose / immeuble_dore / ble / chemin_aube
# ============================================================================
"C_proprios_decus": [
    cover("bg_ville_doree", "aide gratuite du jour",
          f'Ton meilleur client&nbsp;? Le proprio {acc("déçu")} d\'une autre conciergerie.',
          sub="Comment le trouver avant tout le monde, légalement.",
          hand_bottom="la méthode juste après"),
    p_timeline("bg_salon_cosy", "psychologie du proprio", f'Les {o("5 phases")} avant la rupture',
               [("Mois 1 à 3 : la lune de miel", "Il vient de déléguer, il est soulagé, tout va bien.", False),
                ("Mois 4 à 8 : le doute", "Communication lente, tarifs qui semblent bas, avis moyens.", False),
                ("Mois 8 à 12 : la comparaison", "Il regarde les autres et parle aux voisins proprios.", False),
                ("Mois 12 à 18 : la frustration", "Il fait ses comptes : la rentabilité promise n'est pas là.", False),
                ("La rupture", "Lettre recommandée, ou il part à la fin de saison.", True)]),
    p_bigstat("bg_ciel_rose", "le vrai secret, c'est le timing", f'La {o("fenêtre de tir")}',
              "4 → 12", "c'est entre le mois 4 et le mois 12 que tout se joue.",
              ["En phase de doute, il tape déjà ses questions sur Google.",
               "Si ton contenu répond à ses douleurs, tu deviens sa référence.",
               "Une fois la rupture décidée, c'est la guerre du moins cher."],
              numsize=170),
    p_steps("bg_immeuble_dore", "lead magnets", f'3 {o("aimants")} à proprios déçus',
            [("L'audit gratuit en 48 h", "Il t'envoie son annonce, tu réponds sous 48 h. Bonus : tu vois le bien et la gestion AVANT de t'engager."),
             ("Le calculateur de revenus", "Il entre son adresse et découvre ce que son bien devrait vraiment rapporter."),
             ("La checklist des 10 questions", "« Les 10 questions à poser à votre conciergerie. » Tu éduques, tu ne vends pas.")]),
    p_duo("bg_ble", "la ligne est claire", f'Côté {o("légal")}',
          "Jamais", ["Dénigrer un concurrent par son nom",
                     "Démarcher les clients d'un concurrent au téléphone",
                     "Récupérer des emails sur les annonces (RGPD)"],
          "Toujours", ["Éduquer avec du contenu qui répond aux douleurs",
                       "Une transition clé en main, comme un changement d'opérateur",
                       "Des avant/après chiffrés de proprios qui ont changé"]),
    fin("bg_chemin_aube",
        "Tu veux qu'on regarde ensemble ta stratégie d'acquisition ?",
        "réponds à cette story", keyword="GO"),
],

# ============================================================================
# SEQUENCE D — De 0 a 30 logements en 1 an (video Mq4pGuah050)
# fonds : prairie / montagne / ble / village / lac / ciel_dore
# ============================================================================
"D_30_logements": [
    cover("bg_prairie", "la méthode complète 2026",
          f'De {acc("0 à 30 logements")} en 1 an.',
          sub="Les 4 piliers, et les 3 erreurs qui condamnent 90 % des conciergeries.",
          hand_bottom="c'est cadeau, juste après"),
    p_steps("bg_montagne", "d'abord, ce qui tue", f'Les {o("3 erreurs")} fatales',
            [("Le mode bricolage", "Contrat trouvé sur internet, annonces sur TON compte Airbnb. À 10 logements, tout est à refaire."),
             ("Vendre de la « gestion »", "« Gérer », « mandat » : ces mots te font tomber sous la loi Hoguet. Dis pilotage, coordination, prestation."),
             ("Empiler les contrats", "À 8-10 contrats sans système, tu es devenu le salarié de ta propre boîte.")]),
    p_timeline("bg_ble", "la roadmap", f'Les {o("4 piliers")} de 0 à 30',
               [("Contrats 1 à 5 : les fondations", "Contrat conforme, UNE ville et 30 km max, des prix jamais bradés.", False),
                ("5 à 12 : le système", "Channel manager, messages automatiques, onboarding standardisé, ménage sous-traité.", False),
                ("10 à 20 : les leviers", "Parrainage structuré, proprios déçus, référencement local. Premier city manager.", False),
                ("20 à 30 : l'industrialisation", "Tu pilotes aux chiffres : occupation, prix moyen, satisfaction proprio.", True)]),
    p_bigstat("bg_village", "la règle qui change tout", f'{o("2026")} : tout au nom du proprio',
              "100&nbsp;%", "des comptes au nom du propriétaire : Airbnb, Booking, revenue management.",
              ["C'est le proprio qui pilote et qui valide les prix.",
               "En 2025, des conciergeries ont été condamnées pour avoir géré sans validation.",
               "Les juges vérifient l'opérationnel, pas juste le contrat."],
              numsize=170),
    focus("bg_lac", "le canal que personne ne structure",
          f'Le bouche à oreille, ça se {acc("fabrique")}.',
          body="Offre 1 mois de prestation au proprio qui t'amène un nouveau client. "
               "Même mécanique avec les agents immobiliers et les experts-comptables "
               "LMNP. C'est un canal d'acquisition, pas de la chance."),
    p_cta("bg_ciel_dore", "la méthode complète est en vidéo", "Et pour TON plan ?",
          "GO", "Réponds GO, on en parle. La vidéo t'attend sur la chaîne."),
],

# ============================================================================
# SEQUENCE E — L'algorithme Airbnb 2026 (video 9pTFTNPkf-g)
# fonds : bureau_matin / mer_calme / ciel_rose / terrasse / plage_aube / village
# ============================================================================
"E_algo_2026": [
    cover("bg_bureau_matin", "info chaude 2026",
          f'L\'algorithme Airbnb a {acc("changé")}. Voici les nouvelles règles.',
          sub="Airbnb ne montre plus les « meilleurs » logements : il montre le plus "
              "adapté à chaque voyageur.",
          hand_bottom="les vrais chiffres arrivent"),
    p_bars("bg_mer_calme", "ce qui pèse vraiment", f'Ton classement, {o("décomposé")}',
           [("Haut : photo, titre, prix", 20),
            ("Milieu : clics, favoris", 30),
            ("Bas : séjour réel, avis", 50)],
           note="90 % des loueurs optimisent dans le mauvais sens : le séjour "
                "d'abord, la photo ensuite."),
    p_bars("bg_ciel_rose", "les 7 facteurs mesurés", f'Les nouveaux {o("poids")} 2026',
           [("Guest Favorite", 25),
            ("Avis récents (le texte)", 20),
            ("Temps de réponse", 10),
            ("Taux de conversion", 10),
            ("Photos", 8),
            ("Instant Book", 7),
            ("Prix vs marché", 5)],
           note="Le Superhost est obsolète : Guest Favorite = 4,9+ et 5 avis en 2 ans."),
    p_duo("bg_terrasse", "mise à jour", f'Ce qui ne {o("marche plus")}',
          "Oublie", ["Le boost nouvelle annonce : quasi nul désormais",
                     "Tes bons avis de 2023 : seuls les 30-60 derniers jours comptent",
                     "Le Superhost et la course aux 5 étoiles"],
          "À la place", ["Instant Book activé : 15 à 25 % de boost",
                         "Une photo qui tranche : couleurs vives, photo saisonnière",
                         "Viser TES voyageurs, pas tous les voyageurs"]),
    p_bigstat("bg_plage_aube", "le levier le plus rapide", f'La {o("photo de couverture")}',
              "+35&nbsp;%", "de revenus possibles en changeant UNE photo.",
              ["80 % des voyageurs décident en 2-3 secondes.",
               "Couleurs vives quand tout le monde est en gris pastel.",
               "Photo de Noël dès fin novembre : une annonce qui vit, l'algorithme le voit."],
              numsize=190),
    p_cta("bg_village", "le plan 30 jours est en vidéo", "Tu veux le guide complet ?",
          "ALGO", "Réponds ALGO et on t'envoie le pack Airbnb 2026 en DM."),
],

# ============================================================================
# SEQUENCE F — Le piege de la caution (video 4Dlw1_c593k)
# fonds : salon_cosy / bureau_matin / terrasse / lac / montagne / mer_calme
# ============================================================================
"F_caution": [
    cover("bg_salon_cosy", "l'erreur qui coûte cher",
          f'La {acc("caution")} : le piège que 80 % découvrent trop tard.',
          sub="Caution, assurance, loi Hoguet : ce qu'il faut savoir AVANT l'incident.",
          hand_bottom="explication simple juste après"),
    p_vs("bg_bureau_matin", "la base que tout le monde confond", f'Caution {o("vs")} assurance',
         "La caution", ["Tu récupères l'argent DU voyageur.", "Montant limité à la caution fixée.", "Le litige, c'est toi qui le gères."],
         "L'assurance", ["Un tiers paie à ta place.", "Montant limité par la garantie.", "L'assureur gère sinistre ET litige."],
         "Elles ne se remplacent pas : la vraie protection, c'est les deux couches empilées."),
    focus("bg_terrasse", "conciergeries : le test en une question",
          f'Qui {acc("déclenche")} le débit&nbsp;?',
          body="Si c'est la conciergerie, c'est du maniement de fonds pour le compte "
               "de tiers : illégal au sens de la loi Hoguet, même avec des "
               "sous-comptes. La solution propre : la caution part du compte de "
               "paiement DU propriétaire, jamais du tien."),
    p_steps("bg_lac", "les règles qui sauvent", f'4 réflexes {o("caution")}',
            [("Chèque, virement, espèces : terminé", "On ne demande plus jamais ça à un voyageur."),
             ("L'empreinte expire en 7 jours", "Un dégât découvert tard, et il n'y a plus rien à débiter."),
             ("Débiter ne règle rien", "Le voyageur peut contester. Un sinistre documenté, photos à l'appui, change tout."),
             ("AirCover ne couvre qu'Airbnb", "Sur Booking et les résas en direct, sans solution dédiée, tu n'es couvert par rien.")]),
    p_bigstat("bg_montagne", "la stratégie des pros", f'Le {o("double filet")}',
              "50 000 €", "couverts par une assurance dédiée, pour environ 100 € par an.",
              ["La caution dissuade et couvre les petits dégâts.",
               "L'assurance prend le relais sur les gros sinistres.",
               "Et quand le débit de la caution échoue : ça arrive vraiment."],
              numsize=150),
    fin("bg_mer_calme",
        "Et toi, tu gères les cautions comment ?",
        "raconte en réponse, on te dit si c'est carré"),
],

# ============================================================================
# SEQUENCE G — Pourquoi ta conciergerie ne decolle pas (video CREH-yTwa1s)
# fonds : chemin_aube / ciel_rose / ble / bureau_matin / salon_cosy / montagne
# ============================================================================
"G_pourquoi_ca_bloque": [
    cover("bg_chemin_aube", "la vérité qui pique",
          f'{acc("90 %")} des conciergeries ferment en moins de 2 ans.',
          sub="Les 5 erreurs qui les tuent, et comment être dans les 10 %.",
          hand_bottom="check les 5, honnêtement"),
    p_steps("bg_ciel_rose", "auto-diagnostic", f'Les {o("5 erreurs")} fatales',
            [("Pas de positionnement", "« Je fais de la conciergerie » = généraliste choisi sur le prix. Le spécialiste fixe ses tarifs."),
             ("Tout à la main", "Tableurs, messages copiés-collés, prix fixes. Les pros automatisent et gèrent 3 fois plus."),
             ("Le client, c'est le voyageur ?", "Non : le vrai client, c'est le proprio. C'est lui qui donne les clés, et qui peut les reprendre."),
             ("Ignorer ses chiffres", "Certains paient plus de ménage qu'ils n'encaissent, et le découvrent au bilan."),
             ("Tout faire tout seul", "Mois 1-3 : facile. Mois 7-9 : plus de vie. Mois 10-12 : j'arrête.")]),
    p_bigstat("bg_ble", "le mythe du volume", f'50 biens à 15 %&nbsp;? Tu bosses {o("gratuitement")}',
              "10 = 50", "10 logements bien choisis rapportent autant que 50 subis.",
              ["Ménage mal maîtrisé, occupation à 30-40 %, prix bradés : il ne reste rien.",
               "Le volume, c'est une vanité. La marge, c'est la survie.",
               "Et en prime : beaucoup moins de stress."],
              numsize=150),
    p_formula("bg_bureau_matin", "la formule que personne ne calcule", f'Ton {o("coût par nuitée")}',
              "ménage + linge + consommables + ton temps",
              "nombre de nuitées",
              "= ton coût par nuitée",
              "Si ta commission est en dessous, tu refuses le bien. Savoir dire "
              "non, c'est la clé de la survie."),
    p_steps("bg_salon_cosy", "rétention proprios", f'Le {o("reporting")} qui les retient',
            [("Les revenus du mois", "Avec la variation vs le mois dernier et vs l'an dernier."),
             ("Le taux d'occupation", "Comparé au marché local."),
             ("La note voyageurs", "La moyenne, et le nombre d'avis."),
             ("Le prix moyen, expliqué", "« On a fait mieux que le marché grâce au pricing dynamique. »")]),
    fin("bg_montagne",
        "« Un propriétaire bien informé ne part jamais. »",
        "la vidéo complète est sur la chaîne"),
],

# ============================================================================
# SEQUENCE H — Le plan de relance de zero (video N7aN4jh9ebw)
# fonds : plage_aube / chemin_aube / ville_doree / immeuble_dore / ble / lac
# ============================================================================
"H_plan_de_zero": [
    cover("bg_plage_aube", "s'il repartait de zéro",
          f'Le {acc("plan exact")} de Sébastien pour relancer une conciergerie.',
          sub="12 mois, 3 phases, objectifs chiffrés. Après 10 ans de terrain et près "
              "de 100 biens pilotés.",
          hand_bottom="phase par phase, juste après"),
    p_timeline("bg_chemin_aube", "la roadmap 12 mois", f'Les {o("3 phases")}',
               [("Semaines 1-4 : les fondations", "Une zone de 15-20 min max. Premier client gratuit 2 mois (ménage payé) contre témoignages. Process documentés dès le début.", False),
                ("Mois 2-6 : l'accélération", "Outils pro au 5e bien (50 h/mois gagnées à 10 biens). 2-3 agents de ménage + 1 artisan. Pricing dynamique : +15 %.", False),
                ("Mois 6-12 : le scale", "Coordinateur AVANT commercial. Montée en gamme : 20-25 % de commission sur les beaux biens.", True)]),
    p_bigstat("bg_ville_doree", "l'acquisition sans site web", f'Ta fiche {o("Google")}',
              "43&nbsp;%", "des proprios choisissent leur conciergerie via un avis Google.",
              ["Au début : une fiche Google + LinkedIn suffisent, pas de site.",
               "L'audit gratuit sous 48 h à la place du démarchage : conversion triplée.",
               "3 offres au lieu d'un tarif unique : panier presque doublé."],
              numsize=190),
    p_bigstat("bg_immeuble_dore", "la sélection des biens", f'À 30 € la nuit, tu gagnes {o("6 €")}',
              "400-500 €", "de gain par mois et par bien, c'est la cible.",
              ["10 biens dans la cible = 5 000 € par mois.",
               "Une maison à 3 000 € de CA demande le même travail qu'un appart à 700 €.",
               "Moins de volume, plus de valeur."],
              numsize=150),
    p_duo("bg_ble", "l'expérience parle", f'Ce qu\'il ne {o("referait plus")}',
          "Fini", ["Accepter tous les biens, même les galères",
                   "Casser les prix à 12-15 % de commission",
                   "Le local et le site web dès le départ"],
          "À la place", ["Refuser un bien (et parfois un proprio) non rentable",
                         "Démarrer à 18-20 %, à la hauteur du travail",
                         "Chez soi 1 an, charges fixes minimales"]),
    p_cta("bg_lac", "objectif 12 mois : 30 biens, 4 500-7 500 €/mois", "Et TON plan à toi ?",
          "GO", "Réponds GO et on le construit ensemble."),
],

}

SLUG = "banque-01"

def main():
    stories = {}
    for seq, seq_stories in SEQUENCES.items():
        for i, body in enumerate(seq_stories, 1):
            stories[f"{seq}_{i:02d}"] = body
    write_lot(SLUG, stories)

if __name__ == "__main__":
    main()
