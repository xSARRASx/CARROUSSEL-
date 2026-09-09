#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Revenus reels vs revenus affiches : le grand mensonge" (v8fzA9JYTHM, 06/09/2026).

Angle produit FORCE (regle 14). Le pont est honnete et vient de la video
elle-meme : un chiffre sans contexte ne vaut rien, et les gens fiables sont
"les ennuyeux", ceux qui parlent de fiscalite, de revenue management et de
parametrage. C'est exactement le terrain d'un outil de conciergerie.
Applique a une conciergerie : le chiffre d'affaires annonce a un proprietaire
ne vaut rien s'il n'est pas date, rattache au logement et verifiable.

⛔ NE PAS pretendre que l'outil fait de la comptabilite ou du conseil financier.
⛔ Le verbe "gerer" reste proscrit cote conciergerie (loi Hoguet).
⛔ Mots bannis : beds24, mandat de gestion, garantie financiere.
⛔ Aucun denigrement : on vise une pratique, jamais un concurrent.

⚠️ REGLE 16 : couverture cover_duo, differente de celle du Sous Loueur.
⚠️ REGLE 13 : aucun appel a commenter. ⚠️ REGLE 15 : legende sous 2000 signes.

Usage : python3 v2_gl_chiffre_prouve.py && python3 render.py v2_gl_chiffre_prouve
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_gl_chiffre_prouve"

d = Deck("guestlucky")
d.set_bg_photo("gl_chiffre_prouve_bg.jpg", veil=0.82)

SLIDES = [
    d.cover_duo(
        "Guestlucky · Preuve",
        "Deux façons d'annoncer<br>un résultat",
        ("Le chiffre raconté", "?", "Un bon mois, de mémoire, sans rien derrière."),
        ("Le chiffre prouvé", "12", "Mois datés, logement par logement.")),

    d.pincer(1, "Ce qui vaut<br>pour eux vaut<br>pour toi", "Le miroir qui dérange",
             ("Ce qu'on dénonce chez les autres", "Un chiffre affiché sans contexte : brut ou net, meilleur mois ou moyenne, partagé ou non."),
             ("Ce qu'on fait parfois soi-même", "Annoncer un bon mois à un propriétaire, sans dire que le précédent était creux."),
             ("La différence", "Elle ne tient pas à l'honnêteté. Elle tient à ce qu'on est capable de sortir sur demande."),
             "Le test", "Ton dernier bilan, pourrais-tu le prouver ligne par ligne, logement par logement ?",
             lead="Un chiffre sans preuve ne vaut rien. Y compris le tien."),

    d.checklist(2, "Les questions<br>qu'un propriétaire<br>devrait poser", "Et auxquelles tu dois pouvoir répondre",
                [(True, "Est-ce du brut ou du net pour moi ?",
                  "Ce que la plateforme a prélevé, ce que le ménage a coûté, ce qui reste réellement."),
                 (True, "Est-ce un mois normal ou le meilleur ?",
                  "Un bon mois isolé ne dit rien de l'année. Douze mois datés, si."),
                 (True, "D'où vient exactement cette réservation ?",
                  "Le canal change le coût, donc le résultat. Ce n'est pas un détail comptable."),
                 (True, "Est-ce répétable l'an prochain ?",
                  "Sans historique conservé, personne ne peut répondre à cette question, ni toi ni lui.")],
                "Le renversement", "Ce ne sont pas des questions hostiles. Celui qui peut y répondre gagne le contrat.",
                lead="Quatre questions, et elles font le tri très vite."),

    d.layers(3, "Trois niveaux<br>d'un résultat", "Du chiffre à la preuve",
             [("Niveau 1", "Le chiffre",
               "Ce que le logement a encaissé. C'est ce que tout le monde annonce, et ça ne coûte rien à dire."),
              ("Niveau 2", "Le contexte",
               "La saison, le taux de remplissage réel, les nuits vides et leurs raisons, ce qui a été dépensé."),
              ("Niveau 3", "La preuve",
               "Des rapports mensuels horodatés et archivés, relisibles des mois plus tard, sans reconstitution.")],
             "Ce qui manque presque toujours", "Le troisième. Sans lui, le premier n'est qu'une affirmation.",
             lead="Trois niveaux, et un seul se vérifie."),

    d.flow(4, "Comment la preuve<br>se constitue", "Au fil de l'eau",
           [("À chaque réservation",
             "L'encaissement est rattaché au logement et au canal qui l'a produit, avec sa date."),
            ("À chaque intervention",
             "Ce qui a été fait, quand, par qui, avec la facture et les photos au bon endroit."),
            ("À chaque fin de mois",
             "Le rapport se clôture, horodaté et archivé. Rien à reconstituer douze mois plus tard.")],
           "Le principe", "Ce qui n'est pas tracé sur le moment ne se retrouve jamais après.",
           lead="Personne ne prouve une année en la racontant de mémoire."),

    d.mindmap(5, "Ce que l'outil<br>garde pour toi", "Logement par logement",
              "Montrer,<br>au lieu<br>d'affirmer",
              [("Les encaissements", "Rattachés au logement et à la réservation qui les a produits."),
               ("Les dépenses", "Interventions, prestataires, factures, chacune datée et au bon endroit."),
               ("Les rapports mensuels", "Horodatés et archivés, consultables des mois voire des années après."),
               ("L'interface propriétaire", "Il vérifie lui-même, quand il veut, sans passer par toi.")],
              "Le résultat", "Tu n'as plus à convaincre. Tu ouvres, et il regarde.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées."),

    d.compare(6, "Deux conciergeries<br>au bilan annuel", "Le même parc, deux réputations",
              {"head": "Celle qui raconte", "items": [
                  "Elle met en avant son meilleur mois",
                  "Elle explique les creux de mémoire",
                  "Elle rend un tableau fait à la main",
                  "Sa parole vaut ce que le propriétaire veut bien croire"]},
              {"head": "Celle qui montre", "items": [
                  "Elle présente les douze mois, tels quels",
                  "Chaque creux a sa raison documentée",
                  "Chaque ligne renvoie à une pièce datée",
                  "Sa parole n'a plus besoin d'être crue"]},
              "Ce qui se joue", "Un propriétaire ne renouvelle pas sur un chiffre. Il renouvelle sur ce qu'il a pu vérifier.",
              lead="Les deux peuvent avoir fait la même année."),

    d.pincer(7, "Le seul signal<br>qui ne se truque pas", "La durée",
             ("Ce qui s'affiche vite", "Un bon mois, une capture d'écran, une promesse. Tout cela se fabrique en une soirée."),
             ("Ce qui ne se fabrique pas", "Un historique de plusieurs années, daté au fil de l'eau, qu'on peut rouvrir n'importe quand."),
             ("Pourquoi ça compte pour toi", "C'est ce qui te distingue d'une conciergerie qui vient d'ouvrir et promet la même chose."),
             "À dire clairement", "Guestlucky conserve les traces de l'exploitation. Il ne fait ni comptabilité ni conseil financier.",
             lead="Le temps est la seule chose qu'on ne peut pas louer pour une vidéo."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Ton année, tu pourrais<br>la ' + acc("prouver") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre les rapports par logement sur le site.",
        "Un chiffre se raconte en dix secondes. Une preuve se construit toute l'année."),

    d.closing("L'outil qui garde la trace, pour que ton bilan "
              + "<em>se vérifie</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_duo")
