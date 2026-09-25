#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Location Airbnb : peut-on vraiment s'absenter 48h ?" (25/09/2026, 8hotJuvXPuM).

Angle produit : LE PARCOURS VOYAGEUR OUTILLE. C'est la video ou Sebastien montre
l'outil a l'ecran d'un bout a l'autre : livret d'accueil, sequence de messages,
canaux, IA voyageurs et mots-cles qui rendent la main a l'humain.

Fonctions citees, toutes issues de la banque produit (section A2) et montrees
dans la video :
  - Livret d'accueil digital, accessible au voyageur a tout instant
  - Precheckin et caution integree (l'acces au livret est donne apres)
  - Messages programmes / Auto Actions, templates a variables
  - Canaux : messagerie de la plateforme, SMS, lien WhatsApp depuis la reservation
  - Messagerie IA voyageurs, avec reprise en main manuelle
  - Mots-cles d'escalade vers l'humain + notifications
⛔ NE RIEN INVENTER au-dela de cette liste. L'outil ne remplace ni le relais
humain, ni l'organisation : Sebastien le dit lui-meme, un message programme
reste une consigne dont TU es responsable.

⚠️ VOCABULAIRE HOGUET : ni "gerer" ni "gestion", meme si la video en est pleine.
On ecrit ORGANISATION, PILOTAGE, PRISE EN CHARGE, EXPLOITATION.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Theme CLAIR, couverture cover_cadre, scene "ombres_stores"
(regle 18 : la semaine derniere GL etait en sombre avec cover_moities).

Usage : python3 v2_gl_parcours_voyageur.py && python3 render.py v2_gl_parcours_voyageur
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_gl_parcours_voyageur"

d = Deck("guestlucky", "clair")
d.set_bg_photo("gl_parcours_voyageur_bg.jpg", veil=0.80)

SLIDES = [
    d.cover_cadre(
        "Guestlucky · Parcours voyageur",
        'Il est 21h, et<br>ton téléphone ' + acc("sonne"),
        "Le code de la boîte à clés, la bonne porte, la télévision. Trois questions qui n'auraient jamais dû arriver jusqu'à toi."),

    d.pincer(1, "Les deux appels<br>qui cassent<br>une soirée", "Et ce qu'ils ont en commun",
             ("21h : le code introuvable", "L'information a bien été envoyée, trois jours avant, au milieu d'un message de vingt-cinq lignes."),
             ("19h : le départ tardif de demain", "Ce n'est pas urgent, mais ça doit être tranché avant la fin de la journée : le voyageur organise sa matinée."),
             ("Aucun des deux n'exige que ce soit TOI", "Le premier demande une information trouvable. Le second, une règle écrite et quelqu'un pour l'appliquer."),
             "Le vrai enjeu", "Ce n'est pas le nombre de messages, c'est de ne jamais savoir quand le prochain va tomber.",
             lead="Tu pars deux jours, et ton téléphone reste sur la table en permanence."),

    d.mindmap(2, "Le livret<br>d'accueil digital", "Tout au même endroit, consultable à tout instant",
              "ACCESSIBLE<br>DÈS LE<br>PRÉCHECKIN",
              [("L'accès", "L'adresse, l'emplacement exact de la boîte, la photo de la bonne entrée, le code valable pour le séjour."),
               ("Les équipements", "La télévision et sa source, la plaque, les rideaux à manivelle : les cas qui font vraiment appeler."),
               ("Le pratique", "Le wifi, la place de parking et son numéro, les commandes du chauffage, le chemin des poubelles."),
               ("Le départ", "Les consignes de fin de séjour, au moment où elles servent, pas trois jours avant.")],
              "Le principe", "Une rubrique « la télévision ne fonctionne pas » est plus utile qu'une longue présentation de tous les équipements.",
              lead="Le lien est communiqué au précheckin, après la caution : le voyageur l'a dans sa poche tout le séjour."),

    d.timeline(3, "La séquence<br>qui part<br>sans toi", "Écrite une fois, rejouée à chaque réservation",
               [("À la confirmation", "Le remerciement et le cadre",
                 "Les règles essentielles, le lien du livret, et la demande d'heure d'arrivée si elle est utile.", False),
                ("Quelques jours avant", "Le trajet",
                 "Les informations de parking ou de transport, au moment où le voyageur prépare sa venue.", False),
                ("La veille", "Les instructions d'accès",
                 "Séparées du reste, courtes, avec la photo de l'entrée et le contact en cas de difficulté.", True),
                ("Le jour J", "Un rappel court",
                 "Au bon moment, sans répéter à l'identique : un message déjà vu ne sera plus lu.", False),
                ("Le soir", "Le message d'installation",
                 "Envoyé quand quelqu'un peut répondre derrière, pas à 21h dans le vide.", False)],
               "Le cas à prévoir", "Une réservation de dernière minute ne doit pas recevoir d'un coup toute la série prévue pour un séjour réservé deux mois avant.",
               lead="Cinq moments, chacun avec un rôle. Certains peuvent être regroupés selon ton logement."),

    d.layers(4, "Ce qui rend<br>une réponse<br>vraiment utile", "L'IA voyageurs et la fiche du logement",
             [("Étage 1", "La fiche du logement",
               "Le sèche-cheveux dans le tiroir du bas, la deuxième couette dans le placard de l'entrée, la télévision sur telle source. C'est ce niveau de détail qui fait la différence."),
              ("Étage 2", "La réponse, 24 heures sur 24",
               "La messagerie IA répond dans la langue du voyageur, et tu peux reprendre la main à tout moment pour continuer l'échange toi-même."),
              ("Étage 3", "Le passage à l'humain",
               "Des mots-clés paramétrés font sortir l'IA de la conversation, et une notification prévient la personne qui doit prendre le relais.")],
             "À dire honnêtement", "Une fiche complète améliore les réponses, elle ne rend pas l'IA infaillible. Teste-la avec de vraies questions.",
             lead="Plus la fiche est précise, plus la réponse l'est. C'est maintenant qu'il faut l'écrire, pas le soir où la question arrive."),

    d.checklist(5, "Ce qui ne doit<br>JAMAIS rester<br>à la machine", "Les quatre sorties vers l'humain",
                [(False, "Une question sans réponse dans la fiche",
                  "Mieux vaut un humain qui met dix minutes qu'une réponse inventée en deux secondes."),
                 (False, "Un équipement cassé",
                  "Ce n'est plus une question d'information : quelqu'un doit décider et souvent se déplacer."),
                 (False, "Une insatisfaction exprimée",
                  "C'est le moment exact où un séjour bascule, et où un avis se joue."),
                 (False, "Une modification de réservation ou un remboursement",
                  "Ces demandes engagent ton argent et tes conditions : elles se tranchent, elles ne se répondent pas.")],
                "Le point de vigilance", "Le fait qu'un renseignement existe quelque part dans ton compte ne garantit pas qu'il servira à répondre. Vérifie ce qui est réellement accessible.",
                lead="Quatre situations où la bonne réponse automatique est : passer la main."),

    d.compare(6, "Quelle information<br>par quel canal", "Le voyageur doit retrouver, pas être submergé",
              {"head": "La messagerie de la plateforme", "items": [
                  "Le cadre du séjour et les règles essentielles",
                  "Le lien du livret d'accueil",
                  "Les échanges qui doivent rester tracés au même endroit",
                  "Les questions de préparation, sans urgence"]},
              {"head": "Le SMS et WhatsApp", "items": [
                  "Le code d'accès, court et retrouvable d'un coup d'œil",
                  "Le point de contact en cas de problème",
                  "Le message du soir après l'installation",
                  "Le lien WhatsApp du voyageur est sur la réservation, prêt à l'emploi"]},
              "La règle", "L'objectif est qu'il RETROUVE l'information, pas qu'il la reçoive partout en permanence.",
              lead="Un même message n'a pas la même portée selon l'endroit où il arrive."),

    d.flow(7, "Ce qui reste<br>à ta charge", "L'outil n'y changera rien",
           [("Relis tes messages en destinataire",
             "Est-ce clair ? Cohérent avec les horaires du séjour ? Le numéro indiqué fonctionne-t-il vraiment ?"),
            ("Teste l'IA avec de vraies questions",
             "Et vérifie surtout que les situations incertaines sont bien transmises à un humain."),
            ("Mets la fiche à jour quand quelque chose change",
             "Un appareil remplacé, une règle modifiée : sinon tu diffuses très efficacement une mauvaise information.")],
           "La phrase à retenir", "Un message programmé reste une consigne dont tu es le seul responsable.",
           lead="Trois vérifications que rien n'automatise, et qui décident de la qualité de tout le reste."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Combien de tes soirées<br>tiennent à ' + acc("un code") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le livret d'accueil et la séquence de messages sur le site.",
        "Écrit une fois pendant que tu es disponible, rejoué à chaque réservation."),

    d.closing("Le parcours voyageur se prépare, "
              + "<em>il ne s'improvise pas à 21 heures</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_cadre")
    noter_theme("guestlucky", "clair")
