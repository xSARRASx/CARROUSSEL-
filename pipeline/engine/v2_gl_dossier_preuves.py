#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Un proprietaire Airbnb vient de gagner contre sa copropriete au tribunal" (13/08/2026).

Angle produit : LE DOSSIER DE PREUVES. Different du carrousel GL du 29/07, qui
portait sur la prevalidation AVANT de lancer un logement. Ici : ce qu'on doit
pouvoir PRODUIRE quand on est attaque. La phrase du jugement fait le pont :
"la justice ne juge pas des impressions, elle juge des pieces".

S'appuie uniquement sur des fonctions reelles : preanalyse du reglement de
copropriete (citee dans la video), rapports mensuels horodates et archives,
documents classes par logement, historique des echanges, interface proprietaire.
⛔ NE PAS pretendre que l'outil fait de la detection de bruit : les capteurs
cites par Sebastien sont des produits tiers.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Usage : python3 v2_gl_dossier_preuves.py && python3 render.py v2_gl_dossier_preuves
"""
from design_v2 import Deck, acc

SLUG = "v2_gl_dossier_preuves"

d = Deck("guestlucky")
d.set_bg_photo("gl_dossier_preuves_bg.jpg", veil=0.82)

SLIDES = [
    d.cover(
        "Guestlucky · Preuves",
        'La justice juge des pièces,<br>' + acc("pas des impressions"),
        "Ce que tu dois pouvoir produire le jour où ta copropriété t'attaque."),

    d.compare(1, "Deux dossiers<br>face au juge", "Le 23 juillet à Nice",
              {"head": "Celui de la copropriété", "items": [
                  "Des accusations de nuisances sonores",
                  "Du stationnement et des bouteilles évoqués",
                  "Aucun constat, aucune date, aucun témoignage",
                  "Une lettre jamais adressée au propriétaire"]},
              {"head": "Celui du propriétaire", "items": [
                  "Le règlement de copropriété lu et cité",
                  "L'activité déclarée en mairie, preuve à l'appui",
                  "Le décompte précis des prestations fournies",
                  "La règle de majorité vérifiée à la date du vote"]},
              "Le résultat", "Résolutions annulées, copropriété déboutée et condamnée à 2&nbsp;000&nbsp;€.",
              lead="Le dossier vide a perdu contre le dossier documenté."),

    d.layers(2, "Trois niveaux<br>de preuve", "Ce que tu dois pouvoir sortir",
             [("Niveau 1", "Le cadre",
               "Le règlement de copropriété, les procès-verbaux, la déclaration en mairie."),
              ("Niveau 2", "Le mode d'exploitation",
               "Quelles prestations sont réellement fournies, et lesquelles restent en option."),
              ("Niveau 3", "La trace dans le temps",
               "Des rapports datés qui montrent ce qui s'est passé, mois après mois.")],
             "Le principe", "Ce qui n'est pas documenté n'existe pas devant un tribunal.",
             lead="Trois couches, et c'est la troisième qui manque presque toujours."),

    d.flow(3, "Comment le dossier<br>se constitue", "Sans y penser",
           [("À l'ouverture du logement",
             "La préanalyse du règlement de copropriété est conservée avec ses éléments."),
            ("Pendant l'exploitation",
             "Les rapports mensuels sont horodatés et archivés, logement par logement."),
            ("Le jour où ça compte",
             "Tu sors un dossier daté au lieu de reconstituer trois ans de mémoire.")],
           "Le cadre", "Une préanalyse outillée ne remplace pas l'avis d'un professionnel du droit.",
           lead="Le dossier se construit au fil de l'eau, pas la veille de l'audience."),

    d.checklist(4, "Ce que tu dois<br>pouvoir produire", "Face à une accusation",
                [(True, "La liste exacte de tes prestations",
                  "Pour démontrer que tu n'en cumules pas trois sur les quatre qui font basculer."),
                 (True, "Des rapports datés",
                  "Un document horodaté vaut mieux qu'un souvenir, même sincère."),
                 (True, "L'historique de tes échanges",
                  "Les messages avec les voyageurs montrent le fonctionnement réel du logement."),
                 (True, "Les documents du logement classés",
                  "Règlement, procès-verbaux, déclaration : au même endroit, pas éparpillés.")],
                "Le réflexe", "Face à une accusation, exige des pièces. Et apporte les tiennes.",
                lead="Quatre éléments qui transforment ta parole en dossier."),

    d.pincer(5, "Deux moments<br>où ça se joue", "Et ils sont courts",
             ("Avant le vote", "Relire le règlement et les procès-verbaux, avant même la convocation."),
             ("Après le vote", "Deux mois pour contester une résolution hostile, pas un jour de plus."),
             ("Dans les deux cas, tout part des mêmes documents", "Le règlement de copropriété et l'historique des assemblées générales."),
             "L'enjeu", "Un dossier prêt à l'avance change complètement ta position de départ.",
             lead="Deux fenêtres, et aucune ne laisse le temps de tout reconstituer."),

    d.mindmap(6, "Ce qui reste<br>dans l'outil", "Logement par logement",
              "Un dossier<br>qui se remplit<br>tout seul",
              [("La préanalyse du règlement", "Conservée avec les éléments qui ont mené à son indicateur."),
               ("Les rapports mensuels", "Horodatés et archivés, consultables des mois plus tard."),
               ("Les documents du bien", "Classés au même endroit, accessibles quand tu en as besoin."),
               ("L'historique des échanges", "La trace de ce qui s'est réellement passé pendant les séjours.")],
              "Le résultat", "Tu montres, au lieu d'expliquer.",
              lead="Quatre traces qui existent déjà, à condition d'être conservées."),

    d.stats(7, "Les repères<br>du jugement", "À garder en tête",
            [("23 juil. 2026", "Le jugement du tribunal judiciaire de Nice"),
             ("3 sur 4", "Les prestations à cumuler pour basculer dans le commercial"),
             ("2 mois", "Le délai pour contester une résolution d'assemblée générale"),
             ("2 000 €", "Ce que la copropriété a été condamnée à payer")],
            "Honnêteté", "Jugement en premier ressort : un appel reste possible. Il applique la Cour de cassation.",
            lead="Quatre chiffres qui résument ce que cette décision a établi."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Ton dossier tiendrait-il<br>' + acc("devant un juge") + ' ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre la préanalyse de règlement sur le site.",
        "Le meilleur moment pour constituer un dossier, c'est avant d'en avoir besoin."),

    d.closing("L'outil qui garde la trace, pour que tu puisses "
              + "<em>montrer</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
