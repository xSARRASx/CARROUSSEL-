#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Expatrie : le mythe des 183 jours va te couter tres cher"
(21/09/2026, ZdEMuAtcJcE).

Angle produit : PILOTER SON MEUBLE DEPUIS L'AUTRE BOUT DU MONDE. Le pont est
DIT PAR SEBASTIEN dans la video : beaucoup d'expatries gardent leur bien et le
mettent en courte duree depuis l'etranger ; il cite guestlucky.com comme outil
de pilotage a distance, juste apres avoir parle d'arrivees autonomes et de
menage organise.

Fonctions citees, toutes issues de la banque produit (section A2) :
  - Messagerie IA voyageurs 24/7, multilingue
  - Auto Actions (10 declencheurs, 14 conditions, 9 actions)
  - Templates de messages a variables
  - Planning menages + application mobile prestataires
  - Livret d'accueil digital avec QR code
  - Channel Manager natif, dashboard et KPIs, interface proprietaire
  - Equipes et utilisateurs illimites
⛔ NE RIEN INVENTER. En particulier, les SERRURES CONNECTEES evoquees dans la
video ne sont PAS une fonction Guestlucky : ne jamais les presenter comme telle.
L'outil ne fait ni la comptabilite, ni la declaration, ni la fiscalite.

⚠️ VOCABULAIRE HOGUET : ni "gerer" ni "gestion", meme si la video dit "gerer a
distance". On ecrit PILOTER, PILOTAGE, COORDINATION, EXPLOITATION.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Theme SOMBRE, couverture cover_moities, scene de fond "etagere"
(regle 18 : la semaine derniere GL etait en clair avec cover_mot).

Usage : python3 v2_gl_piloter_a_distance.py && python3 render.py v2_gl_piloter_a_distance
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_gl_piloter_a_distance"

d = Deck("guestlucky", "sombre")
d.set_bg_photo("gl_piloter_a_distance_bg.jpg", veil=0.84)

SLIDES = [
    d.cover_moities(
        ("À 10 000 km", "Tu subis le décalage",
         "Tu réponds à trois heures du matin, tu relances ton ménage par messages, et tu espères."),
        ("À 10 000 km", "Tu pilotes",
         "Les messages, les arrivées et les interventions tournent pendant que tu dors.")),

    d.compare(1, "Le même logement,<br>deux façons<br>de partir", "Ce qui change une fois là-bas",
              {"head": "Sans outil de pilotage", "items": [
                  "Chaque question de voyageur attend ton réveil",
                  "Le ménage se cale par messages, au fil de l'eau",
                  "Les plateformes se mettent à jour une par une, à la main",
                  "Tu ne sais ce qui s'est passé qu'en le demandant"]},
              {"head": "Avec un outil de pilotage", "items": [
                  "La messagerie répond 24 heures sur 24, dans la langue du voyageur",
                  "Les interventions partent au prestataire dès la réservation",
                  "Un seul calendrier synchronise Airbnb, Booking et Abritel",
                  "Le tableau de bord dit ce qui s'est passé sans rien demander"]},
              "La vraie différence", "Ce n'est pas le talent ni la présence. C'est ce qui a été écrit dans l'outil avant le départ.",
              lead="Le décalage horaire ne pardonne pas l'improvisation : il la multiplie par le nombre de nuits."),

    d.mindmap(2, "Ce qui tourne<br>pendant que<br>tu dors", "Le décalage horaire",
              "Le voyageur<br>n'attend pas<br>ton réveil",
              [("La messagerie IA", "Disponible 24 heures sur 24, multilingue, formée sur tes annonces : elle répond quand tu n'es pas réveillé."),
               ("Les Auto Actions", "Dix déclencheurs, quatorze conditions, neuf actions empilables : la réservation déclenche la suite toute seule."),
               ("Les templates", "Des messages prêts, avec les variables déjà remplies : le bon texte, au bon moment, sans toi."),
               ("Le livret d'accueil digital", "Un QR code, et le voyageur trouve le code d'accès, le fonctionnement du chauffage et les consignes de départ.")],
              "Ce que ça change", "Une nuit sans réponse, c'est un avis moyen. Sur un parc en courte durée, ça se paie vite.",
              lead="Quatre automatismes qui remplacent le réflexe de regarder son téléphone à trois heures du matin."),

    d.flow(3, "Un séjour qui<br>se déroule<br>sans toi", "Avant, pendant, après",
           [("Avant l'arrivée",
             "La confirmation, les informations pratiques et le livret partent automatiquement dès la réservation."),
            ("Pendant le séjour",
             "Le voyageur pose ses questions à la messagerie, et l'intervention urgente arrive au prestataire sur son application mobile."),
            ("Après le départ",
             "Le ménage est déjà planifié, la remise en état est tracée, et la nuit suivante peut être vendue.")],
           "Le point de bascule", "Tu n'es plus le maillon obligatoire entre le voyageur et le logement. C'est exactement ce qu'il faut pour partir.",
           lead="Trois moments, et aucun qui exige que tu sois réveillé au même fuseau horaire."),

    d.layers(4, "Qui fait quoi,<br>quand tu n'es<br>plus sur place", "Les accès cloisonnés",
             [("Étage 1", "Tes prestataires",
               "Application mobile dédiée : ils voient leurs missions, pas tes chiffres. Utilisateurs et équipes illimités."),
              ("Étage 2", "Ton propriétaire, si tu es conciergerie",
               "Interface dédiée avec ses indicateurs en temps réel : il consulte au lieu de t'écrire à l'heure où tu dors."),
              ("Étage 3", "Toi",
               "Le tableau de bord complet, les réservations, les performances, consultables depuis n'importe quel fuseau horaire.")],
             "La règle", "Chacun voit ce dont il a besoin, et rien d'autre. C'est ce qui permet de déléguer sans se déposséder.",
             lead="À distance, le problème n'est pas de travailler : c'est de savoir qui peut faire quoi sans toi."),

    d.pincer(5, "Les deux illusions<br>du départ", "Ce qu'on se raconte avant de partir",
             ("« Je piloterai depuis là-bas »", "Sauf qu'entre le décalage horaire et la vie sur place, le téléphone ne suit pas. Ce qui n'est pas automatisé retombe sur toi, à la mauvaise heure."),
             ("« Une personne sur place suffira »", "Elle suffit pour le ménage. Elle ne tient ni le calendrier, ni les prix, ni les réponses aux voyageurs."),
             ("Ce qui tient vraiment", "Ce qui a été écrit dans l'outil avant le départ : les règles, les automatismes et les accès."),
             "Le bon moment", "Ces réglages se posent pendant que tu es encore sur place, jamais depuis l'aéroport.",
             lead="Les deux se ressemblent : elles supposent qu'on aura le temps, une fois là-bas."),

    d.checklist(6, "À verrouiller<br>avant de partir", "La liste courte",
                [(True, "Les plateformes sur un seul calendrier",
                  "Le channel manager natif synchronise Airbnb, Booking et Abritel en temps réel : plus une seule mise à jour manuelle."),
                 (True, "Les messages automatiques écrits et testés",
                  "Arrivée, séjour, départ : tu les relis pendant que tu es encore là, pas depuis un autre continent."),
                 (True, "Les accès prestataires créés et essayés",
                  "Une mission envoyée une fois pour de vrai vaut tous les tutoriels."),
                 (True, "La caution encaissée proprement",
                  "Via Stripe, sur un compte par propriétaire, conforme à la loi Hoguet : elle ne se mélange jamais aux recettes.")],
                "Le réflexe", "Tout ce qui n'est pas réglé avant le départ deviendra un message urgent au milieu de ta nuit.",
                lead="Quatre réglages qui prennent une journée sur place, et qui tiennent toute l'année."),

    d.stats(7, "Ce que l'outil<br>ne fait PAS", "Le rappel honnête",
            [("20&nbsp;%", "Le taux minimum d'imposition de tes loyers français en non-résident"),
             ("29 000 €", "Le seuil au-delà duquel ce taux passe à 30&nbsp;%"),
             ("7,5&nbsp;%", "Les prélèvements sociaux au lieu de 17,2&nbsp;%, si tu relèves d'un régime de l'Union européenne"),
             ("10 ans", "Le délai de reprise en cas de fausse domiciliation, depuis la loi de finances 2025")],
            "À dire clairement", "Piloter en courte durée depuis l'étranger ne change rien à la fiscalité : ce sont des revenus de source française, et les obligations déclaratives suivent. L'outil pilote l'exploitation, pas ta déclaration.",
            lead="Ces chiffres viennent de la vidéo de Sébastien. Ils ne dépendent d'aucun logiciel."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Ton logement tournerait-il<br>' + acc("sans toi") + ' demain ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le pilotage à distance sur le site.",
        "Le bon moment pour tout régler, c'est pendant que tu es encore sur place."),

    d.closing("Le logement tourne, "
              + "<em>même quand tu dors à l'autre bout du monde</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_moities")
    noter_theme("guestlucky", "sombre")
