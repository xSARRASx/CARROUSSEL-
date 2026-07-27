#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 (mise en page visuelle) du carrousel Guestlucky de la semaine : le module
conformite / gouvernance, a partir de la video "220 000 EUR : le jugement qui
fait trembler les concierges".

Angle produit, schemas differents de ceux du carrousel Le Sous Loueur.
Aucun mot banni, aucun concurrent nomme.

Usage : python3 v2_gl_conformite_lemeur.py && python3 render.py v2_gl_conformite_lemeur
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_conformite_lemeur"

d = Deck("guestlucky")
d.set_bg_photo("gl_conformite_lemeur_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Conformité",
        '220&nbsp;000&nbsp;€ d\'amende :<br>la conformité n\'est plus ' + acc("une option"),
        "Le module gouvernance qui prouve, bien par bien, que ta conciergerie travaille dans les règles."),

    d.stats(1, "Ce que risque<br>une conciergerie", "Juillet 2026",
            [("220&nbsp;000&nbsp;€", "L'amende infligée à une conciergerie, une première en France"),
             ("100&nbsp;000&nbsp;€", "Le plafond prévu pour un intermédiaire depuis la loi Le Meur"),
             ("12&nbsp;500&nbsp;€", "Par manquement au numéro d'enregistrement"),
             ("50&nbsp;000&nbsp;€", "En cas de dépassement du plafond de nuitées")],
            "Le constat", "Être en règle ne suffit plus : il faut pouvoir le prouver.",
            lead="Les sanctions ne visent plus seulement le propriétaire du logement."),

    d.flow(2, "Comment arrive<br>un contrôle", "La chaîne automatisée",
           [("Le téléservice", "Chaque logement doit être enregistré au niveau national."),
            ("La détection", "La commune compare les annonces et les déclarations, quasi en temps réel."),
            ("La sanction", "Le manquement est constaté, l'amende tombe sur les deux parties.")],
           "À retenir", "Le contrôle n'est plus une visite : c'est un croisement de données.",
           lead="Plus personne ne passe entre les mailles par simple discrétion."),

    d.mindmap(3, "Le module<br>conformité", "La gouvernance intégrée",
              "Conformité<br>Guestlucky",
              [("Une fiche par bien", "Statut, commune, autorisations et numéro d'enregistrement centralisés."),
               ("Des badges clairs", "Vert ou rouge sur ton tableau de bord : tu vois qui est en règle."),
               ("Un rapport mensuel", "Généré et envoyé au propriétaire : une trace écrite permanente."),
               ("Le compteur de nuitées", "120 jours, 90 à Paris, tous canaux additionnés automatiquement.")],
              "Le gain", "Tu passes du classeur papier à la preuve générée automatiquement.",
              lead="Quatre briques qui transforment la conformité en routine automatique."),

    d.compare(4, "Expliquer<br>ou prouver", "Ce qui change devant un contrôle",
              {"head": "Sans outil", "items": [
                  "Des tableurs et des classeurs éparpillés",
                  "Des captures d'écran difficiles à dater",
                  "Un suivi qui casse dès 20 logements",
                  "Des explications, jamais des preuves"]},
              {"head": "Avec le module", "items": [
                  "Une fiche de conformité par logement",
                  "Un rapport mensuel horodaté et archivé",
                  "Un tableau de bord qui tient à l'échelle",
                  "Des documents opposables immédiatement"]},
              "Le cap", "Face à un contrôle, tout se joue sur les traces écrites.",
              lead="La même activité, mais une capacité à démontrer radicalement différente."),

    d.checklist(5, "Ce que l'outil<br>surveille", "Bien par bien, en continu",
                [(True, "Le statut du logement", "Résidence principale ou secondaire, avec le régime qui va avec."),
                 (True, "Les autorisations", "Changement d'usage et numéro d'enregistrement rattachés au bien."),
                 (True, "Le plafond de nuitées", "Le compteur additionne tous les canaux et alerte avant la limite."),
                 (True, "La trace écrite", "Le rapport mensuel part au propriétaire, sans que tu y penses.")],
                "À retenir", "Ce qui est surveillé automatiquement ne s'oublie jamais.",
                lead="Quatre points de contrôle qui tournent sans intervention de ta part."),

    d.layers(6, "Chacun<br>son rôle", "Des responsabilités documentées",
             [("Le propriétaire", "Il reste pilote", "Calendrier et prix restent sous sa main, avec un accès dédié."),
              ("La conciergerie", "Elle délivre des prestations", "Ménages, linge, accueil voyageurs : un périmètre clair et écrit."),
              ("L'outil", "Il fournit les preuves", "Fiches, badges et rapports qui documentent qui fait quoi.")],
             "À retenir", "Des rôles clairs et tracés protègent les deux parties.",
             lead="La répartition des rôles est ce que le juge regarde en premier."),

    d.stats(7, "Pourquoi<br>Guestlucky", "Pensé par un conciergeur",
            [("1", "Une seule plateforme : channel manager, messagerie, caution et conformité"),
             ("2012", "L'année où le fondateur a commencé à gérer ses propres logements"),
             ("48 h", "Le temps d'une migration complète depuis ton outil actuel"),
             ("0 €", "Jusqu'à 2 logements, sans engagement, résiliable en un clic")],
            "À retenir", "L'outil suit la réglementation pour que tu fasses ton métier.",
            lead="Un outil bâti par quelqu'un qui gère vraiment des logements."),

    d.cta("Action · 1 mot",
          'Envie de voir le module<br>' + acc("conformité") + ' en vrai ?',
          "DEMO",
          "et on te montre tout en 30 minutes, sans engagement.",
          "Une démonstration en visio, sur tes propres logements."),

    d.closing("Le PMS qui transforme la conformité en "
              + "<em>routine automatique</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
