#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"10 techniques pour remplir ton Airbnb sans baisser les prix" (rattrapage 06/08/2026).

Angle produit : l'audit d'annonce du module Market Intelligence. Sebastien le
presente lui-meme dans la video : lien de l'annonce, analyse complete, medianes
de marche, positionnement prix, liste d'opportunites, export PDF.
S'appuie aussi sur la messagerie IA (delai de reponse) et le bouche-trou 7 jours.
Aucune fonctionnalite inventee : tout figure dans la banque produit ou la video.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_audit_annonce.py && python3 render.py v2_gl_audit_annonce
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_audit_annonce"

d = Deck("guestlucky")
d.set_bg_photo("gl_audit_annonce_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Audit",
        'Avant de baisser tes prix,<br>' + acc("regarde tes chiffres"),
        "L'audit d'annonce te dit où tu te situes face au marché, et quoi corriger en premier."),

    d.stats(1, "Ce que l'audit<br>te sort", "Sur une annonce",
            [("P50", "La médiane de ton marché : la moitié des annonces comparables"),
             ("P75", "Le quart qui performe le mieux, la cible à viser"),
             ("12 mois", "Ta performance réelle sur un an glissant, mise face au marché"),
             ("PDF", "Le rapport complet exportable, pour le garder ou le transmettre")],
            "Le principe", "Des verdicts chiffrés, pas une impression.",
            lead="Tu colles le lien de ton annonce, et tu obtiens une position, pas un avis."),

    d.flow(2, "Comment on<br>obtient l'audit", "Trois étapes",
           [("Tu colles le lien",
             "L'adresse de ton annonce suffit, rien d'autre à préparer."),
            ("L'analyse tourne",
             "Une à deux minutes : titre, description, photos, cohérence, positionnement."),
            ("Tu reçois la liste",
             "Les opportunités classées, que tu coches au fur et à mesure que tu les traites.")],
           "Le cadre", "Gratuit, avec un compte à créer, sans engagement.",
           lead="Trois étapes entre ton annonce et un plan d'action chiffré."),

    d.compare(3, "Au feeling<br>ou sur des chiffres", "Face à un mois creux",
              {"head": "Sans audit", "items": [
                  "Tu baisses le prix parce que ça ne réserve pas",
                  "Tu ne sais pas si le problème est le titre ou la photo",
                  "Tu changes trois choses à la fois, sans rien mesurer",
                  "Tu recommences le mois suivant, un peu plus bas"]},
              {"head": "Avec l'audit", "items": [
                  "Tu vois où tu te situes face à la médiane du marché",
                  "Les points faibles sont notés et classés par priorité",
                  "Tu traites une opportunité, tu la coches, tu mesures",
                  "Ton prix reste le tien"]},
              "Le gain", "Tu arrêtes de deviner ce qui cloche dans ton annonce.",
              lead="La différence se joue sur ce que tu sais avant d'agir."),

    d.layers(4, "Ce que l'analyse<br>passe en revue", "Point par point",
             [("Le contenu", "Titre, description, structure",
               "Les abréviations, les paragraphes trop longs, les points clés absents."),
              ("Les visuels", "Photos et mise en scène",
               "L'éclairage, la postproduction, la mise en valeur des atouts distinctifs."),
              ("Le positionnement", "Prix face au marché",
               "Ton tarif comparé à des biens équivalents de ta ville, avec la marge disponible.")],
             "À retenir", "Chaque point sort avec une note et une action concrète à mener.",
             lead="Trois familles de critères, notées séparément."),

    d.pincer(5, "Deux leviers<br>qui se pilotent seuls", "Une fois réglés",
             ("Le délai de réponse", "La messagerie intelligente répond en continu, sans que tu tiennes l'heure toi-même."),
             ("Les trous du calendrier", "Le bouche-trou à sept jours remise uniquement les nuits qui allaient être perdues."),
             ("Ton prix de référence ne bouge pas", "Tu gagnes sur le délai et sur les creux, jamais sur ton tarif affiché."),
             "L'effet", "Deux des taux mesurés par l'algorithme s'améliorent sans intervention quotidienne.",
             lead="Deux réglages qui travaillent pendant que tu fais autre chose."),

    d.checklist(6, "Ce que l'audit<br>fait remonter", "Les manques les plus fréquents",
                [(False, "Des abréviations dans l'annonce",
                  "Elles cassent la lecture et desservent la première impression."),
                 (False, "Des équipements non valorisés",
                  "Présents dans le logement, absents de la fiche, donc absents des filtres."),
                 (False, "Une description en bloc",
                  "Sans paragraphes courts ni points clés, les trois premières lignes ne qualifient personne."),
                 (False, "Un prix décroché du marché",
                  "Trop bas parce que la qualité perçue est basse : les deux se corrigent ensemble.")],
                "Le rappel", "Onze opportunités relevées sur une seule annonce, dans l'exemple montré en vidéo.",
                lead="Quatre défauts qui reviennent presque à chaque analyse."),

    d.mindmap(7, "À quoi sert<br>la médiane", "Se situer, pas se comparer",
              "Viser le<br>quart de tête",
              [("Sous la médiane", "Ton annonce se vend moins bien que la moitié du marché local."),
               ("Autour de la médiane", "Tu es dans la moyenne, avec de la marge devant toi."),
               ("Dans le quart de tête", "La zone visée : le positionnement des annonces qui performent."),
               ("La marge chiffrée", "L'écart entre ton prix et le haut du marché apparaît en euros.")],
              "L'usage", "Tu sais combien tu peux aller chercher, et à quelle condition.",
              lead="Un chiffre seul ne dit rien : c'est la position dans ton marché qui compte."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Ton annonce se situe<br>' + acc("où") + ' exactement ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et lance l'audit de ton annonce depuis le site.",
        "Gratuit, sans engagement, avec le rapport complet exportable."),

    d.closing("L'outil qui te dit quoi corriger, "
              + "<em>chiffres à l'appui</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
