#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Frais Airbnb : ce qui change vraiment pour les hotes" (ARDRtYtIgSk, 02/09/2026).

Angle produit : CONSTRUIRE LA BASE CLIENT DU PROPRIETAIRE. Sebastien le dit
mot pour mot : "nous construisons la base client de vos biens" est la promesse
la plus differenciante du marche en ce moment. Sujet neuf cote Guestlucky.

Fonctions citees dans CETTE video : moteur de reservation integre (site pret,
couleurs et logo, strategies tarifaires propres au direct), enregistrement en
ligne avec caution et livret d'accueil, couverture des dommages activable,
channel manager pour eviter la double reservation.

⛔ NOM PROPRE ECARTE : la couverture des dommages porte un nom commercial que la
transcription rend de facon incertaine. On decrit la fonction, comme d'habitude.
⛔ Le verbe "gerer" reste proscrit cote conciergerie (loi Hoguet).
⛔ Mots bannis : beds24, mandat de gestion, garantie financiere.
⛔ NE PAS promettre de contourner la protection des donnees : la slide 7 pose la
frontiere, consentement et propriete de la base cote proprietaire.

⚠️ REGLE 16 : couverture cover_aplat, differente de celle du Sous Loueur.
⚠️ REGLE 13 : aucun appel a commenter. ⚠️ REGLE 15 : legende sous 2000 signes.

Usage : python3 v2_gl_base_client.py && python3 render.py v2_gl_base_client
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_gl_base_client"

d = Deck("guestlucky")
d.set_bg_photo("gl_base_client_bg.jpg", veil=0.82)

SLIDES = [
    d.cover_aplat(
        "Guestlucky · Base client",
        "À qui appartiennent<br>tes voyageurs&nbsp;?",
        "Airbnb vient de chiffrer la réponse : 9,5 points de commission."),

    d.stats(1, "Le chiffre<br>qu'Airbnb a lâché", "Sans vouloir le dire",
            [("15,5 %", "Quand la plateforme trouve le voyageur"),
             ("6 %", "Quand c'est la conciergerie qui l'amène"),
             ("9,5 points", "L'écart, soit le prix de l'acquisition"),
             ("x 2", "La réservation en direct double chaque année")],
            "Ce que ça dit", "Une base client, ce n'est pas un fichier. C'est presque 10&nbsp;% de chaque réservation.",
            lead="Un test américain, rapporté fin août. Rien n'est annoncé en Europe."),

    d.compare(2, "Deux conciergeries<br>face au même<br>propriétaire", "La promesse qui décide",
              {"head": "Celle qui remplit", "items": [
                  "Elle amène des voyageurs, mois après mois",
                  "Chaque séjour repart avec la plateforme",
                  "Rien ne reste quand le contrat s'arrête",
                  "Sa valeur est refaite à zéro chaque année"]},
              {"head": "Celle qui construit", "items": [
                  "Elle amène des voyageurs ET les garde",
                  "Chaque séjour nourrit la base du bien",
                  "Le propriétaire garde un actif à son nom",
                  "Sa valeur s'accumule saison après saison"]},
              "La phrase qui fait la différence", "Nous construisons la base client de vos biens. C'est la promesse la plus rare du marché aujourd'hui.",
              lead="Les deux facturent pareil. Une seule laisse quelque chose derrière elle."),

    d.flow(3, "Où la base<br>se construit", "Trois moments, pas un de plus",
           [("À l'enregistrement en ligne",
             "Il renseigne sa caution et consulte le livret d'accueil. Ça passe par ton outil, pas par la messagerie de la plateforme."),
            ("Pendant le séjour",
             "Il scanne pour retrouver le livret, te joindre, réserver un service. Chaque geste est une occasion."),
            ("Au départ",
             "Il repart avec ton nom et une raison de revenir directement la prochaine fois.")],
           "Le cadre", "Consentement du voyageur et respect de la protection des données. Il n'y a pas de raccourci sur ce point.",
           lead="Le moment légitime existe. Encore faut-il être équipé pour le saisir."),

    d.layers(4, "Trois voyageurs,<br>trois canaux", "Le canal suit la relation",
             [("L'inconnu", "La plateforme, à plein tarif",
               "Elle l'a trouvé et rassuré. C'est le prix d'un client que le bien n'aurait pas eu."),
              ("Le connecté", "Le lien à tarif réduit",
               "Il connaît le logement mais n'y a jamais dormi. Il veut encore la sécurité de la plateforme."),
              ("Le fidèle", "Le direct, sans commission",
               "Il a déjà séjourné et fait confiance. C'est là que le moteur de réservation prend tout son sens.")],
             "Le but", "Faire monter chaque voyageur d'un étage, saison après saison.",
             lead="Un entonnoir : plein tarif, puis tarif réduit, puis zéro."),

    d.mindmap(5, "Ce qu'il faut<br>pour tenir le direct", "Autrement ça casse",
              "Une boutique<br>sans client<br>ne sert à rien",
              [("Un moteur de réservation", "Le site est prêt, tu poses tes couleurs et ton logo, et tu encaisses en direct."),
               ("Des prix propres au direct", "Tu peux appliquer une stratégie différente de celle des plateformes."),
               ("Un calendrier synchronisé", "Le channel manager évite la double réservation, qui coûte bien plus qu'une commission."),
               ("Une couverture des dommages", "Activable, sur le même principe que celle de la plateforme.")],
              "L'ordre", "On équipe le direct quand la base existe, pas avant. Sinon c'est une vitrine vide.",
              lead="Quatre briques, et elles ne servent qu'ensemble."),

    d.checklist(6, "Ce que tu peux<br>mesurer, là", "Le vrai diagnostic",
                [(True, "Les voyageurs recontactables sans plateforme",
                  "Sur les douze derniers mois, logement par logement. C'est le seul chiffre qui compte."),
                 (True, "La part des séjours de clients déjà venus",
                  "Si elle est à zéro, le bien reste fournisseur de la plateforme à plein tarif."),
                 (True, "Ce que chaque canal coûte réellement",
                  "Plein tarif, tarif réduit, direct. Par logement et sur l'année, pas au ressenti."),
                 (True, "Ce qu'un voyageur rapporte dans le temps",
                  "Une deuxième venue change complètement le calcul de la première.")],
                "Le renversement", "La question n'est plus combien coûte la plateforme, mais combien coûte un client selon le canal.",
                lead="Quatre indicateurs qu'aucun propriétaire ne connaît aujourd'hui."),

    d.pincer(7, "Le point<br>de vigilance", "À régler dans le contrat",
             ("La question à trancher", "À qui appartient la base client que tu construis : à ta conciergerie, ou au propriétaire du bien ?"),
             ("La réponse prudente", "Au propriétaire. C'est son bien, ses voyageurs, et c'est ce qui te protège."),
             ("La frontière à ne pas franchir", "Tu n'es pas un intermédiaire entre propriétaires. Relogement et surclassement se pensent dans ce cadre, avec un professionnel du droit."),
             "À dire clairement", "Guestlucky outille la relation. Il ne décide ni du contrat, ni de la conformité.",
             lead="La promesse est forte, donc elle doit être écrite avant d'être vendue."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Tes voyageurs, tu peux<br>les ' + acc("recontacter") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le moteur de réservation en direct sur le site.",
        "Le meilleur moment pour construire une base client, c'était il y a un an."),

    d.closing("L'outil qui construit la base client de tes biens, "
              + "<em>séjour après séjour</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_aplat")
