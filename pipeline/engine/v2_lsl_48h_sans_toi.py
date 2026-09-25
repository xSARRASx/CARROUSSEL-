#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Location Airbnb : peut-on vraiment s'absenter 48h ?" (25/09/2026, 8hotJuvXPuM).

Angle coaching : L'ORGANISATION EN TROIS COUCHES. Prevenir les questions
evitables, programmer les reponses aux questions repetitives, deleguer les
situations qui demandent une decision. Plus le registre d'observation d'une
semaine et le plan en 30 jours.

⚠️ VOCABULAIRE HOGUET : la video dit "gestion" a chaque phrase. Nous ecrivons
ORGANISATION, PILOTAGE, PRISE EN CHARGE, EXPLOITATION. Jamais "gerer".

⛔ Prudences : l'astreinte de 50 a 100 € par mois est un ORDRE DE GRANDEUR donne
par Sebastien, pas un tarif. Le seuil des trois repetitions est un repere qu'il
relativise lui-meme quand il y a peu de sejours.

Theme SOMBRE, couverture cover_trois (les trois couches), scene "beton_soleil"
(regle 18 : la semaine derniere LSL etait en clair avec un bandeau).

Usage : python3 v2_lsl_48h_sans_toi.py && python3 render.py v2_lsl_48h_sans_toi
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_lsl_48h_sans_toi"

d = Deck("lesousloueur", "sombre")
d.set_bg_photo("lsl_48h_sans_toi_bg.jpg", veil=0.85)

SLIDES = [
    d.cover_trois(
        "Le Sous Loueur · 48 heures",
        [("Prévenir", "Les questions évitables ne doivent plus remonter jusqu'à toi."),
         ("Programmer", "Les questions répétitives méritent des réponses répétitives."),
         ("Déléguer", "Il reste les situations qui demandent une décision. Elles ont un responsable.")]),

    d.checklist(1, "Commence par<br>un registre", "Une semaine complète, avant de changer quoi que ce soit",
                [(True, "Note chaque sollicitation, ligne par ligne",
                  "Quand elle arrive, par quel canal, sur quel logement, le motif, et s'il fallait agir tout de suite."),
                 (True, "Ajoute la colonne qui change tout",
                  "Qu'est-ce qui aurait permis de la traiter sans toi ? C'est elle qui fait passer de « j'ai trop de messages » à « je sais ce qui manque »."),
                 (True, "Note aussi les interruptions que tu te provoques",
                  "Ouvrir l'application pour vérifier que le ménage est fait, relancer le voyageur parce que tu ignores son heure d'arrivée."),
                 (False, "Ne cherche pas une solution générale",
                  "« Je vais prendre quelqu'un pour tout ça » est la mauvaise réponse : chaque motif se règle différemment.")],
                "Le repère", "Un motif qui revient trois fois mérite ton attention. Avec un seul logement et peu de séjours, observe plutôt sur un mois.",
                lead="Sept jours d'observation valent mieux qu'un an d'impressions."),

    d.timeline(2, "Trois lignes,<br>trois réponses<br>différentes", "Ce que ton registre révèle",
               [("Mardi 21h", "Code introuvable",
                 "Ce n'est pas un problème de voyageur, c'est une information mal présentée. Sauf s'il est bloqué dehors : là, ça devient une urgence.", True),
                ("Mercredi 11h", "Peut-on arriver plus tôt ?",
                 "Ce n'est pas une urgence, c'est une règle qui manque, plus une vérification de disponibilité.", False),
                ("Vendredi 18h", "Fuite sous l'évier",
                 "Celle-là demande vraiment une action humaine sur place. Aucune information ne l'évitera.", False)],
               "L'erreur classique", "Mettre ces trois demandes dans le même panier, et chercher une seule solution pour les trois.",
               lead="Trois sollicitations d'une même semaine, et trois natures de problème complètement différentes."),

    d.compare(3, "Ce que tu envoies<br>et ce qu'il<br>retrouve", "Couche 1 : rendre l'information trouvable",
              {"head": "Le message de 25 lignes", "items": [
                  "Le règlement, le parking, les restaurants, les consignes de départ",
                  "Envoyé trois jours avant, au milieu de tout le reste",
                  "Le code est quelque part dedans",
                  "Le voyageur arrive fatigué, valise dans une main, téléphone dans l'autre"]},
              {"head": "Les instructions d'accès, à part", "items": [
                  "Un message court : adresse, heure, emplacement exact de la boîte",
                  "Une photo qui permet de reconnaître la bonne entrée",
                  "Un code dont l'envoi et la validité collent au séjour",
                  "Le contact prévu en cas de difficulté"]},
              "Le test qui ne trompe pas", "Fais essayer tes instructions par quelqu'un qui ne connaît pas les lieux. Chaque hésitation t'indique quoi rendre plus clair.",
              lead="Tu as bien transmis l'information. La vraie question est : est-elle retrouvable en trente secondes ?"),

    d.flow(4, "Ce qui se règle<br>dans le logement", "Et qui ne se rattrape pas par un message",
           [("Montre au lieu d'expliquer",
             "Photographie la télécommande et le bon bouton, la place de parking et son numéro, le chemin des poubelles."),
            ("Affiche le wifi en grand",
             "Le réseau et le mot de passe, lisibles dans le logement. Et prévois une petite box 4G de secours : le jour où la connexion tombe, aucune explication ne suffira."),
            ("Range toujours au même endroit",
             "Le sèche-cheveux dans le même tiroir, à chaque ménage. Sans ça, aucune réponse ne peut être précise.")],
           "Ce que ça change", "La moitié des appels du soir ne sont pas des problèmes de logement : ce sont des problèmes de repérage.",
           lead="Si la même question revient chaque semaine, le problème n'est pas le voyageur."),

    d.mindmap(5, "Ce que ton relais<br>peut décider<br>sans toi", "Couche 3 : la page de règles",
              "SINON TU<br>RESTES<br>INDISPENSABLE",
              [("Vert : il agit seul", "Retrouver une information, expliquer un équipement, appliquer une règle écrite, remplacer une petite fourniture dans la limite convenue. Il garde une trace."),
               ("Orange : dans un créneau annoncé", "Une facture demandée, des serviettes pour le lendemain. Ça se regroupe à certains moments de la journée."),
               ("Rouge : prise en charge immédiate", "Voyageur bloqué dehors, fuite importante, danger, panne qui rend le logement inutilisable."),
               ("Le test oral", "« Il est 22h, le code ne fonctionne pas, tu fais quoi ? » Tu verras tout de suite s'il manque une information, un contact ou une autorisation.")],
              "Le piège", "Un relais joignable qui t'appelle pour valider chaque décision n'a rien changé : tu as juste déplacé la conversation.",
              lead="Ces trois couleurs servent à réfléchir, pas à décider automatiquement à ta place."),

    d.layers(6, "Le relais humain,<br>concrètement", "Qui, par où, jusqu'où",
             [("Qui", "Souvent la personne qui fait déjà le ménage",
               "Avec une astreinte convenue, de l'ordre de 50 à 100 € par mois selon Sébastien, et un bonus quand il faut se déplacer. Mais elle n'a pas accepté d'avance : il faut lui demander."),
              ("Par où", "Une ligne dédiée, séparée de ton numéro personnel",
               "Commander un deuxième numéro ne suffit pas : sans routage ni transfert testé, tous les appels retombent sur toi."),
              ("Jusqu'où", "Une enveloppe de dépense écrite",
               "Une limite convenue, les contacts des professionnels, et surtout aucun accès à tes identifiants principaux ni à ta banque.")],
             "Le contrôle de cohérence", "L'ancien numéro ne doit pas continuer à orienter les voyageurs vers toi par habitude.",
             lead="Le point de contact annoncé aux voyageurs doit mener à quelqu'un, jamais à un répondeur écouté le lendemain."),

    d.stats(7, "Les quatre repères<br>du plan", "À tester, mesurer, corriger",
            [("1 semaine", "D'observation avant de changer quoi que ce soit"),
             ("3 fois", "Le nombre de répétitions qui désigne un motif à traiter"),
             ("2 heures", "La première plage de relais, avant d'élargir à une soirée puis à un week-end"),
             ("30 jours", "Registre, information, séquence et fiche, puis page de règles et premier test d'absence")],
            "L'honnêteté", "Tout ne sera pas réglé en 30 jours, et une semaine calme ne prouve rien. Le but est d'avoir une organisation testable.",
            lead="On commence petit, on mesure, on corrige. C'est la seule méthode qui tienne."),

    d.cta("Action · 1 mot",
          'Ton logement tournerait-il<br>' + acc("48 heures") + ' sans toi ?',
          "48H",
          "et je t'envoie le registre à remplir et le plan en 30 jours, semaine par semaine.",
          "La prochaine fois que tu règles un problème, demande-toi ce qui éviterait le prochain."),

    d.closing("Reprendre ses soirées ne se décrète pas. "
              + "<em>Ça s'organise.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_trois")
    noter_theme("lesousloueur", "sombre")
