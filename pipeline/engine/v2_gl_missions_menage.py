#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Menage Airbnb : le business cache qui rapporte gros" (sWiie3c__Lo, 30/08/2026).

Angle produit : LE PILOTAGE DES MISSIONS DE MENAGE. Sebastien le dit lui-meme
dans cette video : le vrai probleme des conciergeries n'est pas de trouver des
proprietaires, c'est de trouver des equipes de menage fiables, et des missions
restent affectees a personne. Sujet neuf : aucun carrousel GL precedent ne parle
des missions de menage.

Fonctions citees explicitement par Sebastien dans CETTE video :
  - pilotage des missions de menage, cote conciergerie ET cote prestataire
  - un module qui evite d'imposer une nouvelle application au prestataire :
    il passe par une messagerie qu'il a deja, avec une intelligence artificielle
    qui dialogue avec lui
  - checklist obligatoire a valider avant de cloturer une mission
  - photos avant/apres, cloture impossible sans elles
  - declaration d'incident
  - reporting complet cote conciergerie
  - acces a la facturation electronique pour le prestataire

⛔ NOMS PROPRES ECARTES : la transcription deforme le nom du module ("Luy Clean"
/ "Lucky Clean") et le domaine de facturation. On decrit la FONCTION, jamais un
nom propre incertain. On ne nomme pas non plus la messagerie utilisee.
⛔ Le verbe "gerer" reste proscrit cote conciergerie (loi Hoguet, 24/08).
⛔ Mots bannis : beds24, mandat de gestion, garantie financiere.

⚠️ REGLE 13 : aucun appel a commenter. ⚠️ REGLE 15 : legende sous 2000 signes.

Usage : python3 v2_gl_missions_menage.py && python3 render.py v2_gl_missions_menage
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_missions_menage"

d = Deck("guestlucky")
d.set_bg_photo("gl_missions_menage_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Missions",
        'Ton vrai problème,<br>ce ne sont pas ' + acc("les propriétaires"),
        "Ce sont les missions de ménage que personne ne prend."),

    d.pincer(1, "Ce qu'on voit<br>dans les comptes", "Des centaines de conciergeries",
             ("Ce que tout le monde croit", "Que la difficulté d'une conciergerie, c'est de signer des propriétaires."),
             ("Ce qu'on observe vraiment", "Des missions à 60, 70, 80&nbsp;€ qui restent affectées à personne, faute d'avoir quelqu'un de fiable."),
             ("Et ça se paie tout de suite", "Un logement mal préparé, c'est un mauvais avis, et un mauvais avis en basse saison pèse double."),
             "Le vrai goulot", "Trouver des équipes de ménage fiables, puis les garder. Tout le reste vient après.",
             lead="La difficulté n'est pas là où on la cherche."),

    d.compare(2, "Deux façons<br>de faire tourner<br>une mission", "Le même prestataire, deux résultats",
              {"head": "Par messages, à la main", "items": [
                  "Les consignes se répètent à chaque fois",
                  "Les photos arrivent quand elles arrivent",
                  "Un incident se raconte, ou s'oublie",
                  "Tu recopies tout dans ton suivi le soir"]},
              {"head": "Par un circuit outillé", "items": [
                  "La checklist part avec la mission",
                  "La clôture est impossible sans les photos",
                  "L'incident se déclare depuis la mission",
                  "Le reporting arrive chez toi tout seul"]},
              "Le point clé", "Ce n'est pas une question de sérieux du prestataire. C'est une question de circuit.",
              lead="Le prestataire est le même. Ce qui change, c'est ce qu'on lui donne."),

    d.checklist(3, "Ce qui bloque<br>l'adoption", "Et comment on l'a levé",
                [(True, "Aucune nouvelle application à installer",
                  "Le prestataire passe par une messagerie qu'il a déjà, sans rien apprendre."),
                 (True, "Aucune formation à l'outil",
                  "Avec la checklist et une petite formation terrain, il démarre au pied levé."),
                 (True, "Les photos ne peuvent pas être oubliées",
                  "La mission ne se clôture pas tant qu'elles ne sont pas envoyées."),
                 (True, "Les réponses sont immédiates",
                  "Il dialogue avec l'assistant, qui lui renvoie les informations en quelques secondes.")],
                "Pourquoi ça compte", "Un prestataire renonce rarement au travail. Il renonce à installer une application de plus.",
                lead="La meilleure procédure du monde ne sert à rien si personne ne l'utilise."),

    d.flow(4, "Le déroulé<br>d'une mission", "De l'envoi à la clôture",
           [("La mission part avec tout ce qu'il faut",
             "Le lieu, la checklist, ce qui est attendu. Rien à redemander, rien à chercher."),
            ("Il indique le démarrage, puis envoie les photos",
             "Avant et après. C'est ce qui sépare l'amateur du professionnel, et c'est tracé."),
            ("Il signale ce qu'il a trouvé",
             "Dégât, réassort à prévoir, objet oublié. L'incident se déclare sur place, pas de mémoire.")],
           "Ce que tu récupères", "Tout le reporting dans ton interface, sans avoir à le reconstituer le soir.",
           lead="Trois moments, et chacun laisse une trace exploitable."),

    d.layers(5, "Ce que ça change<br>pour ton parc", "Trois effets, dans cet ordre",
             [("Effet 1", "Les missions trouvent preneur",
               "Un prestataire peut démarrer au pied levé, donc ton vivier s'élargit au lieu de se réduire."),
              ("Effet 2", "La qualité devient vérifiable",
               "Photos et checklist validée : tu constates au lieu de supposer, logement par logement."),
              ("Effet 3", "Le propriétaire voit le travail",
               "Ce qui a été fait, quand, et par qui. C'est ce qu'il te réclame à chaque bilan.")],
             "L'ordre compte", "Sans le premier effet, les deux autres n'existent pas. Tout part de la disponibilité.",
             lead="Trois effets qui s'enchaînent, et qui partent tous du même circuit."),

    d.mindmap(6, "Le prestataire<br>aussi y gagne", "Et ça change tout",
              "Un partenaire<br>equipé reste<br>plus longtemps",
              [("Il sait exactement quoi faire", "La checklist est explicite, il n'y a rien à deviner ni à redemander."),
               ("Il prouve son travail", "Les photos avant et après le protègent autant qu'elles te rassurent."),
               ("Il signale sans téléphoner", "Un incident se déclare depuis la mission, en quelques secondes."),
               ("Il accède à sa facturation", "Un prestataire qui travaille avec une conciergerie équipée y a droit automatiquement.")],
              "Le calcul", "Un prestataire bien outillé te coûte moins cher qu'un prestataire à remplacer.",
              lead="On parle beaucoup de son sérieux. On parle rarement de ce qu'on lui donne."),

    d.stats(7, "Les repères<br>du marché", "Ce que tu paies, en face",
            [("40 à 60 €", "Un studio ou un petit appartement"),
             ("60 à 90 €", "Un deux ou trois pièces"),
             ("90 à 150 €", "Une maison de grande capacité"),
             ("+30 à 50 %", "La majoration d'une intervention en urgence")],
            "À savoir", "La moitié des conciergeries veulent un forfait avec le linge, et cela se facture 20 à 30&nbsp;% de plus.",
            lead="Quatre repères observés sur le terrain, à ajuster selon ta ville."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Combien de tes missions<br>attendent ' + acc("quelqu\'un") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le pilotage des missions de ménage sur le site.",
        "Le meilleur moment pour outiller un prestataire, c'est avant d'en manquer."),

    d.closing("L'outil qui fait tourner les missions, pour que tes logements soient "
              + "<em>prêts à l'heure</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
