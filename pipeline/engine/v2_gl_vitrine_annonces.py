#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Airbnb choisit maintenant votre photo a votre place" (12/10/2026, soj5bEyLcKE).

Angle produit : LA VITRINE QUE TU NE CONTROLES PLUS, ET CELLE QUE TU CONTROLES
ENCORE. Depuis le 20 mai, la plateforme choisit elle-meme la photo de couverture
parmi les cinq premieres. Sur ton canal direct, tu gardes la main entiere.

Fonctions citees, toutes issues de la banque produit (section A2) :
  - Channel Manager natif : une annonce tenue a jour sur toutes les plateformes
  - Moteur de reservation directe (site direct, 0 % de commission)
  - Module Market Intelligence : audit d'annonce, ce qui bloque la visibilite
  - Dashboard et KPIs par logement
⛔ NE RIEN INVENTER. Guestlucky ne retouche PAS les photos et ne choisit pas a
la place de l'algorithme. L'outil de retouche presente dans la video est un
AUTRE produit de Sebastien : il n'est pas repris ici, et surtout il ne doit
jamais etre presente comme une fonction Guestlucky.

⚠️ VOCABULAIRE HOGUET : ni "gerer" ni "gestion". On ecrit PILOTAGE, EXPLOITATION.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

⛔ Les chiffres cites viennent d'etudes AMERICAINES relayees dans la video.
C'est dit sur la slide.

Theme SOMBRE, couverture cover_chiffre, scene "verre_reflets"
(regle 18 : GL etait en clair avec cover_citation le 05/10).

Usage : python3 v2_gl_vitrine_annonces.py && python3 render.py v2_gl_vitrine_annonces
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_gl_vitrine_annonces"

d = Deck("guestlucky", "sombre")
# ⚠️ FOND CSS DE SECOURS (12/10/2026) : la generation d'image a renvoye 401
# UNAUTHENTICATED sur les quatre modeles de la cascade. La variable
# GEMINI_API_KEY est bien presente mais son format n'est pas celui attendu par
# l'API (elle commence par "AQ." au lieu de "AIza"). Ce n'est donc ni une
# saturation ni un probleme de prompt : la cle doit etre refaite cote Martin.
# Des qu'elle sera valide : generer la scene prevue et decommenter la ligne.
# d.set_bg_photo("gl_vitrine_annonces_bg.jpg", veil=0.84)

SLIDES = [
    d.cover_chiffre(
        "Guestlucky · Vitrine",
        "61", "%",
        "de revenu par nuit disponible en plus pour le quart des annonces les mieux classées",
        "Près de 16 000 annonces suivies à Lisbonne. Même ville, même type de bien. Ce n'est pas le prix qui fait l'écart."),

    d.compare(1, "Deux vitrines,<br>deux niveaux<br>de contrôle", "Ce que change la couverture automatique",
              {"head": "Sur les plateformes", "items": [
                  "La couverture est choisie parmi tes cinq premières photos",
                  "Elle varie selon la recherche du voyageur",
                  "Le réglage manuel n'existe pas sur tous les comptes",
                  "Et quand il existe, l'automatique peut reprendre la main"]},
              {"head": "Sur ton canal direct", "items": [
                  "C'est toi qui décides de la photo d'ouverture",
                  "Elle ne change pas d'un visiteur à l'autre",
                  "Aucune commission sur la réservation",
                  "La même annonce, mais une vitrine que personne ne réarrange"]},
              "Ce que ça implique", "Le canal direct ne remplace pas les plateformes. Il devient la seule vitrine dont tu gardes entièrement la main.",
              lead="Depuis le 20 mai, la photo que voit un voyageur sur les plateformes n'est plus forcément celle que tu as choisie."),

    d.flow(2, "Cinq photos<br>à tenir partout", "Une annonce, plusieurs plateformes",
           [("Chaque plateforme a sa vitrine",
             "Airbnb, Booking, Abritel : les mêmes photos, mais pas les mêmes règles d'affichage ni le même recadrage."),
            ("Le channel manager tient l'ensemble",
             "L'annonce et son contenu se mettent à jour depuis un seul endroit, au lieu d'être repris une par une."),
            ("Le direct suit le même mouvement",
             "Le moteur de réservation directe affiche la même annonce, sans commission et sans arbitrage automatique.")],
           "Le principe", "Si tes cinq premières photos peuvent toutes devenir la couverture, elles doivent toutes être à jour partout en même temps.",
           lead="Changer une photo sur un seul canal ne protège qu'un seul canal."),

    d.mindmap(3, "Ce qu'un audit<br>d'annonce<br>regarde", "Avant de toucher aux photos",
              "CE QUI<br>BLOQUE LA<br>VISIBILITÉ",
              [("L'ordre des premières photos", "Puisque la couverture se joue parmi elles, leur ordre n'est plus un détail esthétique."),
               ("La cohérence de l'annonce", "Titre, équipements, description : ce que le voyageur attend doit correspondre à ce qu'il trouve."),
               ("Le positionnement tarifaire", "Comparé aux annonces comparables de la même zone, pas à une moyenne de ville."),
               ("Les écarts avec le marché local", "Un rapport chiffré vaut mieux qu'une impression, surtout quand on hésite à tout refaire.")],
              "La limite honnête", "Un audit dit ce qui cloche. Il ne retouche pas tes photos et ne décide pas à la place de l'algorithme.",
              lead="Quatre points qui se vérifient avant d'investir du temps dans une séance photo."),

    d.layers(4, "Trois étages<br>d'une vitrine<br>tenue", "De la publication à la mesure",
             [("Étage 1", "La publication",
               "Une annonce à jour sur toutes les plateformes connectées, sans ressaisie, logement par logement."),
              ("Étage 2", "Le canal direct",
               "Le moteur de réservation directe : la vitrine que tu contrôles, sans commission sur le séjour."),
              ("Étage 3", "La mesure",
               "Le tableau de bord et les indicateurs par logement : ce qui a réellement changé après une modification.")],
             "Ce qui manque le plus souvent", "Le troisième étage. Sans mesure, on change cinq choses à la fois et on ne sait jamais laquelle a marché.",
             lead="Une vitrine qui se tient à trois endroits à la fois ne se tient pas à la main."),

    d.checklist(5, "Ce qui se vérifie<br>sur chaque annonce", "Maintenant, pas au printemps",
                [(True, "L'ordre des cinq premières photos",
                  "Elles peuvent toutes se retrouver en couverture. La cinquième mérite autant d'attention que la première."),
                 (True, "Le réglage d'affichage, quand il existe",
                  "Et sa vérification régulière : des hôtes rapportent que l'automatique reprend la main au bout de quelques jours."),
                 (True, "La même annonce sur tous les canaux",
                  "Une photo remplacée sur une plateforme et pas sur les autres crée trois vitrines différentes."),
                 (False, "Ne change pas tout d'un coup",
                  "Une photo à la fois, deux semaines d'observation, puis on garde ou on revient en arrière.")],
                "Le réflexe", "Garde toujours tes originaux, même quand tu retouches. C'est aussi ce qui protège en cas de réclamation.",
                lead="Quatre vérifications par logement, et aucune ne demande de refaire une séance photo."),

    d.pincer(6, "Deux dépendances<br>qui coûtent cher", "Et elles se cumulent",
             ("L'algorithme choisit à ta place", "Sur les plateformes, ta meilleure photo et ta plus faible ont désormais la même chance d'ouvrir ton annonce."),
             ("L'écart se paie en avis", "Une annonce qui promet plus que la réalité se sanctionne le soir même, dans les commentaires, et pour des années."),
             ("Ce qui reste à toi", "Le canal direct, où la vitrine ne bouge pas, et la qualité réelle du logement, que personne ne réarrange."),
             "Le bon arbitrage", "Soigner les cinq photos pour les plateformes, et construire en parallèle un canal qui ne dépend d'aucun arbitrage.",
             lead="On ne reprend pas la main sur un algorithme. On réduit sa part dans son chiffre d'affaires."),

    d.stats(7, "Les repères<br>de la vidéo", "Des études américaines, relayées par Sébastien",
            [("2 à 3 s", "Le temps qu'un voyageur passe sur ta première photo"),
             ("5 photos", "Le nombre de couvertures possibles, depuis le 20 mai"),
             ("+ 28&nbsp;%", "De réservations attribuées à des photos professionnelles"),
             ("+ 17,5&nbsp;%", "De réservations pour les annonces aux photos de qualité vérifiée")],
            "L'honnêteté", "Ces chiffres viennent d'études menées aux États-Unis. Ils donnent un ordre de grandeur, pas une garantie sur ton parc.",
            lead="Quatre repères qui expliquent pourquoi la vitrine est redevenue un sujet sérieux."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Tes cinq premières photos<br>tiennent-elles ' + acc("toutes") + ' la route ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre l'audit d'annonce et la réservation directe sur le site.",
        "Soigner les plateformes, et construire en parallèle la vitrine dont tu gardes la main."),

    d.closing("La vitrine a changé de mains. "
              + "<em>Pas partout.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_chiffre")
    noter_theme("guestlucky", "sombre")
