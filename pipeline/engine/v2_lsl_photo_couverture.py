#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Airbnb choisit maintenant votre photo a votre place" (12/10/2026, soj5bEyLcKE).

Angle coaching : TES CINQ PREMIERES PHOTOS SONT DESORMAIS CINQ COUVERTURES.
Depuis le 20 mai, la plateforme pioche elle-meme dans les cinq premieres photos.
Ce que ca change, ce que valent vraiment les photos, et jusqu'ou on a le droit
de retoucher.

⛔ Prudences :
  - Les chiffres viennent d'ETUDES AMERICAINES citees par Sebastien, pas de la
    France. C'est dit sur la slide et dans la legende.
  - Les regles californiennes et celle de Milwaukee sont AMERICAINES. Sebastien
    pense qu'elles arriveront chez nous ; c'est son analyse, pas une regle
    francaise. Ne jamais laisser croire qu'elles s'appliquent ici.
  - Le reglage manuel n'existe pas sur tous les comptes, et des hotes rapportent
    que l'automatique reprend la main. C'est dit tel quel.
  - L'outil de retouche de Sebastien (Studio Annonce) n'est PAS repris dans les
    slides : ce robot produit pour DEUX marques, Le Sous Loueur et Guestlucky.
    Pousser un troisieme produit n'est pas dans la commande. La methode, elle,
    est gardee : elle tient debout sans l'outil.

Theme CLAIR, couverture cover_moities (avant / depuis le 20 mai), scene
"appartement" (regle 18 : LSL etait en sombre avec cover_chiffre le 05/10).

Usage : python3 v2_lsl_photo_couverture.py && python3 render.py v2_lsl_photo_couverture
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_lsl_photo_couverture"

d = Deck("lesousloueur", "clair")
# ⚠️ FOND CSS DE SECOURS (12/10/2026) : la generation d'image a renvoye 401
# UNAUTHENTICATED sur les quatre modeles de la cascade. La variable
# GEMINI_API_KEY est bien presente mais son format n'est pas celui attendu par
# l'API (elle commence par "AQ." au lieu de "AIza"). Ce n'est donc ni une
# saturation ni un probleme de prompt : la cle doit etre refaite cote Martin.
# Des qu'elle sera valide : generer la scene prevue et decommenter la ligne.
# d.set_bg_photo("lsl_photo_couverture_bg.jpg", veil=0.84)

SLIDES = [
    d.cover_moities(
        ("Avant le 20 mai", "Tu choisissais",
         "Ta photo de couverture était celle que tu avais décidée, et elle ne bougeait pas."),
        ("Depuis le 20 mai", "Elle est choisie",
         "Une intelligence artificielle pioche dans tes cinq premières photos et montre celle qu'elle juge la meilleure.")),

    d.flow(1, "Ce qui a changé<br>sans prévenir", "Une mise à jour de 220 nouveautés",
           [("La couverture devient variable",
             "La plateforme choisit, parmi tes cinq premières photos, celle qu'elle montre à chaque voyageur selon sa recherche."),
            ("L'idée n'est pas idiote",
             "Un couple qui cherche une vue verra le balcon, une famille verra la chambre. Sur le papier, c'est logique."),
            ("Mais tu ne contrôles plus rien",
             "Des hôtes ont vu remonter en couverture la photo qu'ils trouvaient la plus faible, et le support a confirmé que l'IA alterne entre les cinq.")],
           "La conséquence directe", "Tu n'as plus une photo de couverture. Tu en as cinq, et chacune peut se retrouver en première position.",
           lead="Beaucoup ne l'ont pas vue passer : elle était noyée parmi des centaines d'autres nouveautés."),

    d.checklist(2, "Reprendre la main", "Le réglage que personne ne trouve",
                [(True, "Va dans les photos de ton annonce",
                  "Le premier bouton laisse faire la plateforme. Un second lien, discret, te rend le choix de l'ordre."),
                 (True, "Repasse en manuel",
                  "C'est toi qui replaces les photos, et tu peux suivre dans les statistiques celles qui fonctionnent."),
                 (False, "Ne considère pas que c'est réglé une fois pour toutes",
                  "Des hôtes rapportent que l'automatique reprend la main quelques jours plus tard. Il faut revérifier régulièrement."),
                 (False, "Ne compte pas sur ce réglage partout",
                  "Certains comptes ne l'ont tout simplement pas. Dans ce cas, la seule parade est que les cinq photos tiennent toutes la route.")],
                "Le changement de regard", "Ta cinquième photo n'est plus « juste la salle de bain ». C'est une couverture potentielle.",
                lead="Une option existe, mais elle n'est pas mise en avant, et elle n'est pas définitive."),

    d.stats(3, "Ce que valent<br>vraiment<br>tes photos", "Des études américaines, pas des impressions",
            [("+ 17,5&nbsp;%", "De réservations pour les annonces aux photos de qualité vérifiée"),
             ("2 100 $", "De revenus supplémentaires par an, sur la même étude"),
             ("82&nbsp;%", "Des voyageurs jugent la fiabilité de l'hôte sur les photos, avant même de lire la description"),
             ("+ 61&nbsp;%", "De revenu par nuit disponible pour le quart des annonces les mieux classées, à Lisbonne")],
            "Ce qui compte vraiment", "Les chercheurs ont isolé la clarté et les couleurs. Pas le mobilier, pas la surface. La lumière.",
            lead="Ces chiffres viennent d'études menées aux États-Unis, sur des dizaines de milliers d'annonces."),

    d.pincer(4, "Pourquoi le clic<br>décide de tout", "Le premier levier de classement en 2026",
             ("Une couverture faible", "Moins de clics sur ton annonce quand elle apparaît, donc moins de visibilité, donc moins de réservations."),
             ("Une couverture forte", "Plus de clics, donc une meilleure position, donc encore plus de passage. La mécanique s'auto-entretient."),
             ("C'est un commerce de rue", "Le meilleur produit mal placé ne vend pas. Le produit banal très bien placé vend beaucoup. Ici, le placement se gagne au clic."),
             "Le temps dont tu disposes", "Deux à trois secondes. C'est ce que dure le regard d'un voyageur sur ta première photo.",
             lead="Si la plateforme mesure les clics et publie les statistiques, c'est qu'ils comptent dans le classement."),

    d.layers(5, "Jusqu'où on a<br>le droit d'aller", "Trois paliers, et une ligne rouge",
             [("Vert", "La lumière, le cadrage, le rangement",
               "Redresser une ligne, éclaircir, recadrer, ranger la pièce avant la photo. À faire sur toutes tes photos : personne ne te le reprochera jamais."),
              ("Orange", "Remplacer un objet, repeindre un mur",
               "À ne publier QUE si tu le fais réellement dans la pièce. Sinon, c'est un outil pour décider d'une déco, pas pour publier une annonce."),
              ("Rouge", "Redécorer entièrement et publier",
               "Jamais sur une annonce de location. Sur un bien avant rénovation, seulement avec la mention et l'original à côté.")],
             "La règle de base", "Garde toujours tes originaux, même quand tu retouches. Toujours.",
             lead="Embellis tant que tu veux, mais n'invente rien : c'est la seule frontière qui tienne."),

    d.compare(6, "Retouche permise<br>ou tromperie", "La question que personne n'ose poser",
              {"head": "Ce qui change la réalité", "items": [
                  "Ajouter ou enlever un meuble",
                  "Changer un sol, un mur, une vue par la fenêtre",
                  "Verdir un jardin, effacer un poteau électrique",
                  "Une pièce sombre qui devient lumineuse : ça se verra à l'arrivée"]},
              {"head": "Ce qui ne la change pas", "items": [
                  "La lumière et l'exposition",
                  "La netteté",
                  "Le recadrage, à hauteur de poitrine plutôt qu'en vue plongeante",
                  "Le rangement de la pièce avant la prise de vue"]},
              "Ce que dit la plateforme", "Sa politique de contenu couvre explicitement le fait de générer ou modifier à l'aide de l'IA. L'annonce doit correspondre à ce que le voyageur trouve en ouvrant la porte.",
              lead="La déception ne se discute pas : elle se lit dans les commentaires le soir même."),

    d.timeline(7, "Ce qui se durcit<br>ailleurs", "Et ce que ça annonce",
               [("1er janvier 2026", "La Californie encadre",
                 "Une photo d'annonce immobilière modifiée numériquement doit porter une mention claire, et l'original rester accessible. Sans ça, c'est un délit.", False),
                ("1er septembre", "Une bourse d'annonces va plus loin",
                 "À Milwaukee, une photo principale retouchée sans son original peut coûter 10 dollars par jour jusqu'à son remplacement.", False),
                ("20 avril 2026", "La plateforme ferme une porte",
                 "Une photo générée, améliorée ou retouchée par IA n'est plus recevable comme preuve dans une réclamation de dommages.", True),
                ("Janvier 2027", "D'autres communes suivraient",
                 "Ce sont des règles américaines. Sébastien pense qu'elles arriveront chez nous : c'est son analyse, pas une règle française.", False)],
               "La conséquence pratique", "Si un voyageur casse quelque chose et que ta photo du dégât est passée par un filtre, elle peut être rejetée.",
               lead="Rien de tout cela ne s'applique en France aujourd'hui. Mais la direction est lisible."),

    d.cta("Action · 1 mot",
          'Laquelle de tes<br>cinq photos est la plus ' + acc("faible") + ' ?',
          "PHOTOS",
          "et je t'envoie les 5 règles pour tes 5 premières photos, pensées pour un écran de 10 centimètres.",
          "Change une seule photo à la fois, attends deux semaines, regarde ton taux de clic. Si ça monte, tu gardes."),

    d.closing("La lumière vaut des milliers d'euros par an. "
              + "<em>Bien plus que le mobilier.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_moities")
    noter_theme("lesousloueur", "clair")
