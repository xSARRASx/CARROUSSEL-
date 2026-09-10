#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Le fisc vous surveille : les 3 signes qui alertent sur votre residence"
(lc1huihoLio, 09/09/2026).

Angle produit FORCE (regle 14). Le pont est DIT PAR SEBASTIEN LUI-MEME dans la
video : "moi je te parle beaucoup de conciergerie, de loi Hoguet, c'est la meme
chose. Ce n'est pas parce que tu as un contrat que c'est la realite. Ce qu'on
regarde, c'est la realite du terrain." La couverture reprend cette phrase.
Angle retenu : le STATUT et les DATES d'occupation de chaque logement, sujet
neuf cote Guestlucky (les carrousels precedents portaient sur les preuves de
revenus, la gouvernance et les missions).

⛔ INTERDIT de laisser croire que l'outil remplit une declaration, corrige une
fiche d'occupation ou fait de la fiscalite. La slide 7 le dit noir sur blanc.
⛔ Le verbe "gerer" reste proscrit cote conciergerie (loi Hoguet).
⛔ Mots bannis : beds24, mandat de gestion, garantie financiere.
⛔ Ne PAS citer l'outil de verification de taxe fonciere de Sebastien : ce n'est
pas Guestlucky, et son domaine est mal rendu par la transcription.

⚠️ REGLE 16 : couverture cover_citation, differente de celle du Sous Loueur.
⚠️ REGLE 13 : aucun appel a commenter. ⚠️ REGLE 15 : legende sous 2000 signes.

Usage : python3 v2_gl_realite_terrain.py && python3 render.py v2_gl_realite_terrain
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_gl_realite_terrain"

d = Deck("guestlucky")
d.set_bg_photo("gl_realite_terrain_bg.jpg", veil=0.82)

SLIDES = [
    d.cover_citation(
        "Ce n'est pas parce que c'est écrit<br>dans le contrat que c'est la réalité.<br>"
        "Ce qu'on regarde, c'est la " + acc("réalité du terrain") + ".",
        "Sébastien More", "fondateur de deux conciergeries"),

    d.pincer(1, "La même logique<br>partout", "Et elle se durcit",
             ("Côté résidence principale", "Le fisc ne juge plus sur l'adresse déclarée. Il regarde la consommation, les mouvements, la vie réelle sur place."),
             ("Côté conciergerie", "Les juges ont fait pareil en 2025 : le contrat disait une chose, la pratique en disait une autre."),
             ("Le point commun", "Dans les deux cas, ce qui compte est ce qui s'est réellement passé dans le logement, et ce qu'on peut en montrer."),
             "À retenir", "Les papiers, ils savent que ça se fabrique. Une vie réelle, non.",
             lead="Sébastien fait lui-même le rapprochement dans la vidéo."),

    d.mindmap(2, "La fiche que<br>l'administration<br>tient sur chaque bien", "Depuis 2023",
              "Qui occupe,<br>à quel titre,<br>depuis quand",
              [("Ce qu'elle décide", "C'est d'elle que partent la taxe foncière et la taxe d'habitation du propriétaire."),
               ("Les statuts possibles", "Résidence principale, résidence secondaire, location, logement vacant."),
               ("Le durcissement", "Trois années de contrôle supplémentaires, spécifiquement sur les résidences secondaires."),
               ("La nouveauté 2026", "Même les occupants non propriétaires doivent déclarer les meublés qu'ils occupent.")],
              "Pourquoi ça te concerne", "Ton propriétaire remplit cette fiche. Mais c'est toi qui sais ce qui s'est passé dans le logement.",
              lead="Elle s'appelle la fiche d'occupation, et elle décide de sa fiscalité."),

    d.compare(3, "Deux réponses<br>à la même question", "Quand le propriétaire te la pose",
              {"head": "De mémoire", "items": [
                  "Le logement a été loué une bonne partie de l'année",
                  "Il y a eu des périodes creuses, je crois en février",
                  "Je peux te retrouver ça, laisse-moi quelques jours",
                  "Le reste du temps, il était vide je pense"]},
              {"head": "Avec les dates", "items": [
                  "Les nuits occupées, mois par mois, telles quelles",
                  "Chaque période creuse identifiée et datée",
                  "Sorti en quelques minutes, pas en trois jours",
                  "Et chaque intervention sur place qui le confirme"]},
              "Ce qui change", "Ton propriétaire ne te demande pas un avis. Il a besoin de dates pour remplir sa fiche correctement.",
              lead="La même année d'exploitation, deux niveaux de réponse."),

    d.layers(4, "Trois traces<br>qui datent<br>une occupation", "Ce que tu détiens déjà",
             [("Trace 1", "Les nuits réellement occupées",
               "Logement par logement, avec leurs dates, et pas une moyenne annuelle."),
              ("Trace 2", "Les interventions sur place",
               "Ménage, maintenance, passage d'un prestataire. Chacune datée, avec ses photos."),
              ("Trace 3", "Les rapports mensuels",
               "Horodatés et archivés, relisibles des années plus tard sans rien reconstituer.")],
             "Le point aveugle", "Ces trois traces existent chez presque toutes les conciergeries. Presque aucune ne les conserve assez longtemps.",
             lead="Trois traces, et c'est la durée de conservation qui fait la différence."),

    d.flow(5, "Pourquoi la durée<br>compte autant", "Le contrôle arrive tard",
           [("Le contrôle ne vient pas tout de suite",
             "Dans l'affaire du studio parisien, le jugement est tombé dix ans après la vente."),
            ("Les délais viennent d'être allongés",
             "Trois années de plus pour contrôler les résidences secondaires, spécifiquement."),
            ("Ce qui n'est pas archivé n'existe plus",
             "Une boîte mail se vide, un tableur se perd. Un rapport horodaté et archivé, non.")],
           "Le principe", "On ne conserve pas des traces pour aujourd'hui. On les conserve pour la question qui viendra dans cinq ans.",
           lead="Personne ne reconstitue une année d'occupation de mémoire."),

    d.checklist(6, "Ce qu'un propriétaire<br>devrait pouvoir<br>te demander", "Sans que ça te panique",
                [(True, "Les dates d'occupation de l'année écoulée",
                  "Pas un pourcentage de remplissage : les périodes, avec leur début et leur fin."),
                 (True, "Les périodes où le logement est resté vide",
                  "Elles comptent autant que les autres, et elles ont chacune une explication."),
                 (True, "Les interventions faites sur place",
                  "Ce qui prouve qu'il se passait quelque chose dans ce logement, et quand."),
                 (True, "Les documents du bien, au même endroit",
                  "Pour qu'il n'ait pas à te les redemander chaque année.")],
                "Le test", "Ces quatre éléments, tu les sortirais en combien de temps aujourd'hui ?",
                lead="Quatre demandes légitimes, et il finira par les faire."),

    d.pincer(7, "Où s'arrête<br>ton rôle", "La frontière, clairement",
             ("Ce qui est ton rôle", "Conserver et dater ce qui s'est passé dans le logement, et le rendre consultable."),
             ("Ce qui ne l'est pas", "Sa fiche d'occupation, sa taxe foncière, sa déclaration. Ça ne se remplit ni ne se corrige depuis un outil de conciergerie."),
             ("Ce que tu peux faire d'utile", "Lui dire que cette fiche existe, qu'elle est consultable en ligne, et le laisser la vérifier avec un professionnel du chiffre."),
             "À dire clairement", "Guestlucky garde les traces de l'exploitation. Il ne fait ni comptabilité ni fiscalité.",
             lead="La tenir te protège autant que lui."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Une année d\'occupation,<br>tu la ' + acc("daterais") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le suivi par logement sur le site.",
        "Le contrôle ne prévient pas. Les traces, elles, se conservent à l'avance."),

    d.closing("L'outil qui garde la trace, pour que la réalité du terrain "
              + "<em>reste consultable</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_citation")
