#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Loueurs en meuble : ces obligations de septembre vont tout changer" (09/08/2026).

Angle produit : l'enregistrement a la facturation electronique depuis Guestlucky.
Sebastien l'annonce lui-meme dans la video : deux mois de chantier, integration
d'une plateforme agreee, enrolement en 10 minutes depuis l'interface.
S'appuie aussi sur la preanalyse de reglement de copropriete, citee dans la video.
Aucune fonctionnalite inventee.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().
⚠️ Mots bannis evites : beds24, mandat de gestion, garantie financiere.

Usage : python3 v2_gl_facturation_electronique.py && python3 render.py v2_gl_facturation_electronique
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_facturation_electronique"

d = Deck("guestlucky")
d.set_bg_photo("gl_facturation_electronique_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Facturation",
        'Au 1er septembre, il faut<br>pouvoir ' + acc("recevoir"),
        "L'enregistrement à la facturation électronique se fait depuis ton interface, en dix minutes."),

    d.pincer(1, "Qui est concerné<br>exactement", "La règle tient en un mot",
             ("Assujetti", "Louer en meublé est une activité économique : un numéro SIREN suffit."),
             ("Redevable", "Tu ne paies la taxe que dans les cas de para-hôtellerie."),
             ("Un SIREN, et tu es dans le circuit", "L'exonération porte sur tes loyers, pas sur ton statut d'opérateur économique."),
             "Le seul cas exclu", "Celui qui n'a aucun numéro SIREN, donc une activité non déclarée.",
             lead="Deux mots que l'on confond, et qui décident si la réforme te concerne."),

    d.compare(2, "Ce qu'on te vend<br>et ce dont tu as besoin", "Avant le 1er septembre",
              {"head": "Ce qu'on essaie de te vendre", "items": [
                  "Un abonnement à 20 ou 30&nbsp;€ par mois",
                  "Un outil d'édition de factures",
                  "L'urgence d'émettre pour chaque séjour",
                  "La peur d'une amende immédiate"]},
              {"head": "Ce dont tu as réellement besoin", "items": [
                  "Être enregistré pour pouvoir recevoir",
                  "Figurer dans l'annuaire national",
                  "Aucune facture à émettre pour des particuliers",
                  "Dix minutes, une seule fois"]},
              "Le geste utile", "L'enrôlement. Tout le reste ne concerne que les redevables de la taxe.",
              lead="La différence entre ce qui est obligatoire et ce qui est commercial."),

    d.flow(3, "S'enregistrer<br>depuis Guestlucky", "Trois étapes",
           [("Tu ouvres ton interface",
             "L'enregistrement se fait depuis ton espace, sans outil supplémentaire."),
            ("Tu signes l'autorisation",
             "Elle permet de te raccorder à la plateforme agréée intégrée."),
            ("Ton SIREN entre dans l'annuaire",
             "Tu deviens joignable dans le circuit officiel, et le sujet est réglé.")],
           "Le contexte", "Deux mois de chantier pour intégrer une plateforme agréée à l'outil.",
           lead="Dix minutes entre ton interface et l'annuaire national."),

    d.layers(4, "Ce qu'est vraiment<br>une facture électronique", "Trois différences",
             [("Ce n'est pas", "Un PDF envoyé par courriel",
               "Le fichier joint à un message ne vaut pas facture électronique au sens légal."),
              ("C'est", "Un fichier structuré",
               "Un format lisible par les machines, du type Factur-X, avec des données normées."),
              ("Ça circule", "De plateforme à plateforme",
               "Via un circuit officiel et un annuaire national, jamais de boîte à boîte.")],
             "La conséquence", "Un SIREN raccordé à aucune plateforme est simplement injoignable.",
             lead="Le mot facture ne veut plus dire la même chose qu'avant."),

    d.checklist(5, "Qui doit agir<br>en priorité", "Selon ton activité",
                [(True, "Une conciergerie",
                  "Tu émets des factures à tes propriétaires : c'est le cas le plus urgent."),
                 (True, "Un propriétaire en meublé",
                  "Tu vas recevoir les factures de ta conciergerie, de tes artisans, de ton comptable."),
                 (False, "Émettre pour chaque voyageur",
                  "Aucune obligation si tu loues à des particuliers. Le voyageur reçoit sa facture comme avant."),
                 (True, "Louer à un professionnel",
                  "Là oui, tu dois lui rédiger une facture, puisqu'il doit pouvoir la recevoir.")],
                "Le rappel", "Même en franchise en base, une conciergerie reste assujettie.",
                lead="Tout le monde est concerné par la réception, peu de monde par l'émission."),

    d.stats(6, "Les chiffres<br>de la rentrée", "À garder en tête",
            [("1er sept.", "La date d'entrée en vigueur de l'obligation de réception"),
             ("10 min", "Le temps réel de l'enrôlement depuis ton interface"),
             ("0 €", "Le coût d'un outil d'édition de factures dont tu n'as pas besoin"),
             ("Mai 2026", "Depuis cette date, le numéro d'enregistrement national est obligatoire")],
            "À retenir", "Une tolérance au démarrage a été annoncée, mais elle ne dispense pas de s'enregistrer.",
            lead="Quatre repères pour situer ce qui compte vraiment."),

    d.mindmap(7, "Les autres sujets<br>de la rentrée", "Dans le même outil",
              "Ta conformité<br>au même endroit",
              [("Le règlement de copropriété", "Une préanalyse te dit si l'activité est risquée avant l'assemblée générale."),
               ("Le plafond de nuitées", "Vérifie s'il est passé de 120 à 90 dans ta commune."),
               ("Le numéro d'enregistrement", "Obligatoire depuis mai, auprès de ta mairie ou du site officiel."),
               ("La facturation", "L'enrôlement se fait depuis la même interface, en dix minutes.")],
              "L'idée", "Les échéances arrivent ensemble : autant les suivre au même endroit.",
              lead="La rentrée ne se limite pas à la facturation électronique."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Ton numéro SIREN est-il<br>' + acc("dans l'annuaire") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post pour le retrouver, et fais ton enrôlement depuis le site.",
        "Dix minutes, une seule fois, avant le 1er septembre."),

    d.closing("L'outil qui te met en règle "
              + "<em>sans te vendre la peur</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
