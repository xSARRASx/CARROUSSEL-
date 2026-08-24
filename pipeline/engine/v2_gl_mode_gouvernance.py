#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Conciergerie 30 logements en 1 an : la methode complete en 2026" (Mq4pGuah050).

Angle produit : LE MODE GOUVERNANCE, nomme explicitement par Sebastien dans
cette video. Le sujet : prouver a tout instant que c'est le PROPRIETAIRE qui
decide, parce que les juges ont regarde la pratique reelle et pas seulement le
contrat. Distinct du carrousel GL du 29/07 (conformite loi Le Meur, cote
declaration) : ici c'est la loi Hoguet et la question "qui decide".

⛔ MOTS BANNIS respectes : jamais "mandat de gestion", jamais "garantie
financiere", jamais "beds24". On n'emploie pas non plus le verbe "gerer" au
sujet de la conciergerie : c'est precisement le mot qui pose probleme.
⛔ NE PAS presenter la delegation de carte G comme une fonction de l'outil :
la video parle d'un PARTENAIRE. Sujet ecarte.
⛔ Aucun denigrement : aucune conciergerie condamnee n'est nommee.

Fonctions citees, toutes issues de la video ou deja etablies : mode gouvernance,
channel manager, interface proprietaire avec acces au calendrier, reportings
photo des interventions, rapports mensuels horodates et archives, documents
classes par logement.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_mode_gouvernance.py && python3 render.py v2_gl_mode_gouvernance
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_mode_gouvernance"

d = Deck("guestlucky")
d.set_bg_photo("gl_mode_gouvernance_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Gouvernance",
        'Le juge ne lit pas<br>ton contrat, il regarde<br>' + acc("ta pratique"),
        "Deux conciergeries l'ont appris en 2025. Leur contrat n'a pas suffi."),

    d.timeline(1, "Ce qui a changé<br>en 2025", "Deux décisions, un même motif",
               [("Le point de départ", "Un propriétaire conteste",
                 "Il constate que tout est décidé sans lui, et il porte l'affaire devant le juge.", False),
                ("Ce qui a été relevé", "Les loyers encaissés au nom de la conciergerie",
                 "Les flux financiers ne passaient pas par le propriétaire.", False),
                ("Ce qui a pesé le plus", "Les prix fixés sans validation",
                 "Le calendrier et la tarification tenus à la place du propriétaire, pas pour son compte.", False),
                ("La décision", "Deux conciergeries condamnées",
                 "L'activité relevait de la loi Hoguet sans en respecter le cadre.", True)],
               "Le point clé", "Les juges ont examiné la pratique réelle, pas seulement ce qui était écrit au contrat.",
               lead="Aucune de ces deux entreprises ne pensait être hors cadre."),

    d.compare(2, "Le contrat dit<br>une chose", "La pratique en dit une autre",
              {"head": "Ce qui est écrit", "items": [
                  "Une prestation de services clairement décrite",
                  "Le propriétaire décide de sa tarification",
                  "Les encaissements lui reviennent",
                  "La conciergerie coordonne et exécute"]},
              {"head": "Ce qu'on peut prouver", "items": [
                  "Qui a réellement validé chaque changement de prix",
                  "À quelle date, et sur quel logement",
                  "Ce que le propriétaire a consulté lui-même",
                  "Ce qui a été fait sur le terrain, avec photos"]},
              "L'écart", "Un contrat conforme sans trace d'exécution ne prouve rien le jour où on te le demande.",
              lead="Les deux colonnes doivent se rejoindre. C'est là que tout se joue."),

    d.checklist(3, "Ce qui doit être<br>au nom du propriétaire", "La liste, sans exception",
                [(True, "Les comptes sur les plateformes de réservation",
                  "Ouverts à son nom, pas sur le compte historique de ta conciergerie."),
                 (True, "L'outil de tarification",
                  "C'est lui qui pilote ses prix. Le contrat de tarification n'est pas signé par toi."),
                 (True, "Les flux financiers",
                  "Les encaissements passent par le propriétaire, pas par ton compte bancaire."),
                 (True, "Les validations, une par une",
                  "Chaque décision structurante doit porter une trace de son accord.")],
                "La nuance", "Ton outil de coordination interne, lui, reste au nom de ta société : c'est un instrument de travail.",
                lead="Quatre points, et le troisième est celui qui a été relevé le plus souvent."),

    d.layers(4, "Trois niveaux<br>de gouvernance", "Du cadre à la preuve",
             [("Niveau 1", "Le cadre écrit",
               "Un contrat et des annexes séparées, pour faire évoluer les règles sans tout réécrire."),
              ("Niveau 2", "La décision tracée",
               "Qui a validé quoi, à quelle date, sur quel logement. Pas un souvenir : une trace."),
              ("Niveau 3", "L'exécution documentée",
               "Reportings photo des interventions, rapports mensuels horodatés et archivés.")],
             "Ce qui manque presque toujours", "Le deuxième. Le cadre est écrit, l'exécution existe, mais rien ne dit qui a décidé.",
             lead="Trois étages, et c'est celui du milieu qui a fait tomber les deux dossiers de 2025."),

    d.flow(5, "Comment la preuve<br>se constitue", "Sans y penser",
           [("À l'entrée d'un logement",
             "Le parcours d'accueil suit toujours les mêmes étapes, et chacune laisse sa trace."),
            ("À chaque décision",
             "La validation du propriétaire est enregistrée au moment où elle a lieu, pas reconstituée après."),
            ("À chaque intervention",
             "Le reporting photo montre ce qui a été fait, quand, et par qui.")],
           "Le principe", "Ce qui n'est pas tracé au moment où ça arrive ne se retrouve jamais deux ans plus tard.",
           lead="La gouvernance n'est pas un document : c'est ce que ton activité laisse derrière elle."),

    d.mindmap(6, "Ce que l'outil<br>garde pour toi", "Logement par logement",
              "Prouver<br>qui a décidé,<br>et quand",
              [("Le mode gouvernance", "La trace des validations du propriétaire, au moment où elles sont données."),
               ("L'interface propriétaire", "Il consulte son calendrier et son activité lui-même, ce qui vaut preuve d'accès."),
               ("Les reportings photo", "Ce que le personnel de ménage et les techniciens ont réellement fait."),
               ("Les rapports mensuels", "Horodatés et archivés, consultables des années plus tard.")],
              "Le résultat", "Le jour où on te demande de prouver, tu ouvres au lieu de reconstituer.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées."),

    d.pincer(7, "Les mots<br>ont leur poids", "Le détail qui décide",
             ("Ce qu'il faut éviter", "Le vocabulaire de la gestion immobilière, dans ton contrat comme sur ton site."),
             ("Ce qui décrit ton métier", "Pilotage, coordination, prestation de services. Trois mots, et ils sont exacts."),
             ("Pourquoi ça compte autant", "Le vocabulaire employé publiquement est examiné au même titre que ta pratique."),
             "Honnêteté", "Ce sont des décisions de première instance. Fais valider ton montage par un professionnel du droit.",
             lead="Ce n'est pas de la sémantique : c'est la qualification juridique de ton activité."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Pourrais-tu prouver<br>' + acc("qui a décidé") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le mode gouvernance sur le site.",
        "Le meilleur moment pour tracer une validation, c'est l'instant où elle est donnée."),

    d.closing("L'outil qui garde la trace, pour que tu puisses "
              + "<em>prouver au lieu d'expliquer</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
