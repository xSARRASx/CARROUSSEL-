#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky de la semaine, a partir de la video
"7 choses a ne jamais dire quand tu commences a gagner de l'argent" (02/08/2026).

Angle produit : la discretion appliquee a une conciergerie, c'est le
CLOISONNEMENT DES ACCES. Chaque interlocuteur voit ce qui le concerne, et rien
d'autre. S'appuie uniquement sur des fonctions reelles de Guestlucky :
interface proprietaire, application prestataires, multi-utilisateurs et equipes.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_cloisonnement_acces.py && python3 render.py v2_gl_cloisonnement_acces
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_cloisonnement_acces"

d = Deck("guestlucky")
d.set_bg_photo("gl_cloisonnement_acces_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Accès",
        'Chacun voit son périmètre,<br>' + acc("personne ne voit le tien"),
        "Le cloisonnement des accès, pour que tes chiffres restent les tiens."),

    d.layers(1, "Trois regards<br>sur ton activité", "Et trois périmètres différents",
             [("Le propriétaire", "Son logement à lui",
               "Ses réservations, son planning, ses revenus. Pas ceux des autres propriétaires."),
              ("Le prestataire", "Son planning de ménages",
               "Les interventions à faire et les accès nécessaires, sans aucune donnée financière."),
              ("Toi", "L'ensemble du portefeuille",
               "Le tableau de bord complet, tes marges et ta rentabilité globale.")],
             "Le principe", "Chacun a ce dont il a besoin pour travailler, et rien de plus.",
             lead="Trois personnes, trois besoins, trois niveaux d'accès distincts."),

    d.compare(2, "Le tableur partagé<br>et l'accès dédié", "Deux façons de travailler",
              {"head": "Avec un fichier qui circule", "items": [
                  "Un document envoyé par courriel, copié et transféré",
                  "Toutes les lignes visibles, y compris celles des autres",
                  "Tes commissions lisibles par qui ouvre le fichier",
                  "Aucune idée de qui détient encore une ancienne version"]},
              {"head": "Avec un accès par personne", "items": [
                  "Chacun se connecte à son propre espace",
                  "Le périmètre est défini une fois, à la création du compte",
                  "Tes marges restent dans ton tableau de bord",
                  "Un accès se retire aussi simplement qu'il s'ouvre"]},
              "Le gain", "Tu arrêtes de choisir entre informer ton propriétaire et exposer tes chiffres.",
              lead="La différence se joue sur ce que l'autre peut voir en plus de ce qu'il cherche."),

    d.flow(3, "Ce qui se passe<br>quand tu ajoutes un bien", "Trois étapes",
           [("Tu crées le logement",
             "Le bien est rattaché à son propriétaire, avec son périmètre propre."),
            ("Tu ouvres les accès utiles",
             "Le propriétaire reçoit son interface, le prestataire son planning sur mobile."),
            ("Chacun suit son activité",
             "Les indicateurs se mettent à jour en temps réel, chacun dans son espace.")],
           "À retenir", "Le cloisonnement se règle à l'ouverture, pas après un incident.",
           lead="Le périmètre de chacun se décide au moment où tu crées le logement."),

    d.checklist(4, "Ce qui ne devrait<br>jamais circuler", "Dans un fichier ou un message",
                [(False, "Le détail de tes commissions",
                  "Ta marge par logement n'a aucune raison d'apparaître dans un document partagé."),
                 (False, "Les revenus des autres propriétaires",
                  "Chacun découvre ce que rapporte le bien du voisin, et les comparaisons commencent."),
                 (False, "La taille réelle de ton portefeuille",
                  "Le nombre exact de logements que tu gères ne regarde que toi."),
                 (False, "Les coordonnées bancaires dans un courriel",
                  "Une pièce jointe transférée reste lisible longtemps après l'envoi.")],
                "Le rappel", "Ce qui n'est pas partagé ne peut pas être utilisé contre toi.",
                lead="Quatre informations qui sortent souvent sans que personne ne l'ait décidé."),

    d.pincer(5, "Deux risques<br>qui se cumulent", "Quand tout circule en clair",
             ("Le risque de sécurité", "Des données regroupées finissent par dessiner un profil exploitable."),
             ("Le risque relationnel", "Un propriétaire qui voit ta marge cesse de regarder ton travail."),
             ("Les deux se règlent au même endroit", "Un accès défini par personne coupe les deux problèmes d'un coup."),
             "L'enjeu", "Tu protèges tes données et la qualité de ta relation avec le même réglage.",
             lead="Le fichier qui circule crée deux ennuis très différents en même temps."),

    d.mindmap(6, "Ce que le propriétaire<br>voit vraiment", "Son logement, en temps réel",
              "Son espace<br>à lui",
              [("Ses réservations", "Le calendrier de son bien, à jour au fil des séjours."),
               ("Ses revenus", "Ce que son logement a généré, sans les chiffres des autres."),
               ("Ses documents", "Les pièces qui le concernent, classées et consultables."),
               ("Rien d'autre", "Ni ton portefeuille, ni tes marges, ni tes autres clients.")],
              "Le résultat", "Il est mieux informé qu'avec un fichier, et tu en montres moins.",
              lead="Donner accès à son logement n'oblige pas à ouvrir toute ton activité."),

    d.stats(7, "Ce que ça change<br>au quotidien", "Sur ton organisation",
            [("Illimité", "Utilisateurs et équipes, sans surcoût par personne ajoutée"),
             ("1 espace", "Par propriétaire, avec ses indicateurs en temps réel"),
             ("0", "Fichier de suivi à envoyer, à mettre à jour et à retrouver"),
             ("2 logements", "Gratuits, de quoi tester le cloisonnement avant de t'engager")],
            "À retenir", "Sans engagement, résiliable en un clic.",
            lead="Le cloisonnement ne coûte pas plus cher : il remplace le fichier partagé."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Tes chiffres méritent<br>de rester ' + acc("les tiens"),
        "RENDEZ-VOUS SUR",
        "Enregistre ce post pour le retrouver, et teste le cloisonnement des accès sur le site.",
        "Gratuit jusqu'à deux logements, sans engagement."),

    d.closing("L'outil qui donne à chacun son périmètre, et "
              + "<em>rien de plus</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
