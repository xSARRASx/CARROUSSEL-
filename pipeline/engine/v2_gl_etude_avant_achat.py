#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Guestlucky, a partir de la video
"Faut-il encore investir dans l'immobilier en 2026 ?" (17/09/2026, iIO-RH_doLo).

Angle produit : CHIFFRER UN BIEN AVANT DE SIGNER. Le pont n'est pas force, il est
DIT PAR SEBASTIEN dans la video : apres avoir montre que le rendement s'est
ecrase, il conclut que tout repose sur une seule question, "combien ce bien
precis va rapporter dans chaque mode de location", et cite le module Market
Intelligence de Guestlucky, qui s'appuie sur des donnees publiques (ANIL,
observatoires des loyers, loyers de reference dans les villes encadrees).

Fonctions citees, toutes issues de la banque produit (section A2) et de la video :
  - Module Market Intelligence : etude de marche, audit d'annonce, rapport chiffre,
    en location courte duree ET en location longue duree meublee
  - Channel Manager natif, Auto Actions, planning menages + app prestataires
  - Dashboard et KPIs, interface proprietaire
⛔ NE RIEN INVENTER au-dela de cette liste. L'outil ne predit pas le marche, ne
donne aucun conseil d'investissement et ne garantit aucun rendement.

⚠️ VOCABULAIRE HOGUET (lecon du 14/09) : ni "gerer" ni "gestion". La video dit
"la gestion est au cordeau" : on ecrit EXPLOITATION, PILOTAGE, COORDINATION.

⚠️ REGLE 13 : aucun appel a commenter. Slide finale = cta_sans_commentaire().

Couverture : cover_mot, sur THEME CLAIR (papier blanc casse, encre et accents
violet/rose) et scene de fond "marbre_violet". Refonte du 18/09 : Martin voulait
"du fond blanc avec les ecritures violettes rose et inversement". Voir la regle
18 dans carroussel.md.

Usage : python3 v2_gl_etude_avant_achat.py && python3 render.py v2_gl_etude_avant_achat
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_gl_etude_avant_achat"

d = Deck("guestlucky", "clair")
d.set_bg_photo("gl_etude_avant_achat_bg.jpg", veil=0.80)

SLIDES = [
    d.cover_mot(
        "Guestlucky · Avant de signer",
        "Combien ?",
        "« Combien ce bien précis va rapporter dans chaque mode de location ? » "
        "C'est la seule question qui compte, et presque personne ne la pose."),

    d.compare(1, "Deux façons<br>d'estimer un bien<br>avant de signer", "Le marché ne pardonne plus l'à-peu-près",
              {"head": "Au ressenti", "items": [
                  "Un rendement estimé d'après le bien du voisin",
                  "Un prix de nuit copié sur trois annonces de la même rue",
                  "Un taux d'occupation supposé, jamais vérifié",
                  "Une rentabilité qui ne tient que si la plus-value arrive"]},
              {"head": "Sur données", "items": [
                  "L'adresse exacte et la typologie du bien comme point de départ",
                  "Des données publiques : observatoires des loyers, loyers de référence",
                  "Le potentiel chiffré en courte durée ET en longue durée meublée",
                  "Un rapport qui se relit à froid, avant l'offre"]},
              "Pourquoi maintenant", "Les prix ont pris 55&nbsp;% par rapport aux revenus quand les loyers en perdaient 9. Le rendement s'est écrasé entre les deux.",
              lead="Tant que le crédit était presque gratuit, l'à-peu-près passait. Plus maintenant."),

    d.flow(2, "Comment se construit<br>une étude<br>de marché", "Le module Market Intelligence",
           [("Tu donnes l'adresse et la typologie",
             "Pas une moyenne de ville : le bien précis que tu regardes, avec son nombre de pièces et sa capacité."),
            ("Les données publiques sont croisées",
             "Observatoires des loyers, loyers de référence dans les villes encadrées, données du marché local."),
            ("Tu obtiens un rapport chiffré",
             "Ce que le bien peut générer en location longue durée meublée, et ce qu'il peut générer en courte durée.")],
           "Ce que ça ne fait pas", "L'étude ne prédit pas le marché et ne garantit aucun rendement. Elle remplace une intuition par un ordre de grandeur documenté.",
           lead="Trois étapes, avant l'offre, pas après la signature."),

    d.mindmap(3, "Ce que le rapport<br>met en face<br>de ton projet", "Les quatre lectures",
              "Un ordre<br>de grandeur<br>documenté",
              [("La longue durée meublée", "Le loyer que la zone porte réellement, encadrement compris quand la ville y est soumise."),
               ("La courte durée", "Le potentiel saisonnier du bien, à sa vraie adresse, pas à celle du centre-ville."),
               ("L'audit de l'annonce", "Pour un bien déjà exploité : ce qui bloque la visibilité et ce qui se rattrape."),
               ("Le rapport chiffré", "Le document que tu poses devant un propriétaire ou devant ton banquier.")],
              "Le vrai arbitrage", "Le bon mode d'exploitation n'est pas le même d'une rue à l'autre. C'est ce que l'étude tranche.",
              lead="Quatre lectures du même bien, pour choisir avant de s'engager plutôt qu'après."),

    d.pincer(4, "Les deux paris<br>qui coûtent<br>le plus cher", "À éviter en 2026",
             ("Parier sur la plus-value", "Acheter en comptant sur la revente, c'est miser sur une baisse des taux que les chiffres ne donnent pas."),
             ("Parier sur la baisse des taux", "L'État emprunte à 3,90&nbsp;% quand les banques prêtent à 3,31&nbsp;% : la marge est déjà négative."),
             ("Ce qui reste solide", "Un cash-flow qui tient aux taux d'aujourd'hui, sur un bien acheté décoté à quelqu'un qui doit vendre."),
             "La conséquence pratique", "Si le calcul ne tient qu'avec une hypothèse favorable, ce n'est pas un calcul : c'est un pari.",
             lead="Les deux se ressemblent : dans les deux cas, la rentabilité dépend de quelque chose qui n'est pas encore arrivé."),

    d.checklist(5, "Ce qui se vérifie<br>avant de signer", "La liste courte",
                [(True, "Le potentiel dans les DEUX modes de location",
                  "Longue durée meublée et courte durée : c'est l'écart entre les deux qui décide de ton exploitation."),
                 (True, "Les règles locales qui s'appliquent au bien",
                  "Encadrement des loyers, règlement de copropriété, autorisations de changement d'usage : ça se vérifie avant l'offre."),
                 (True, "Le point mort, charges et commissions comprises",
                  "Commission des plateformes, ménages, CFE, taxe foncière : le rendement brut ne dit presque rien.")],
                "Le principe", "Ce qui se vérifie avant l'offre coûte une heure. Ce qui se découvre après la signature coûte des années.",
                lead="Trois vérifications que presque personne ne fait dans l'ordre."),

    d.timeline(6, "L'année d'un bien<br>qu'on vient<br>d'acheter", "De l'étude au réalisé",
               [("Avant l'offre", "L'étude de marché",
                 "Le potentiel chiffré par mode de location devient l'argument de négociation, pas seulement une projection.", True),
                ("À la signature", "Le mode d'exploitation est déjà choisi",
                 "Tu sais si le bien part en courte durée, en meublé à l'année, ou en combinaison des deux.", False),
                ("Les 90 premiers jours", "La mise en route",
                 "Channel manager, auto actions, planning ménages et application prestataires : l'exploitation se cadre dès le début.", False),
                ("À 12 mois", "Le réalisé face à l'estimation",
                 "Le dashboard et les KPIs disent ce que le bien a réellement fait, et ce qu'il faut corriger.", False)],
               "Ce qui change", "Une estimation ne vaut que si tu la compares au réalisé un an plus tard. Sinon c'est une promesse.",
               lead="Quatre moments, un seul fil : le chiffre annoncé et le chiffre obtenu."),

    d.stats(7, "Le marché<br>dans lequel<br>tu achètes", "Les repères de la vidéo",
            [("954 000", "Ventes sur 12 mois, soit 91&nbsp;% du régime normal du marché"),
             ("297 000", "Logements commencés sur 12 mois : la pénurie locative se prépare"),
             ("3,31&nbsp;%", "Le taux moyen d'août, en hausse de trois points de base par mois depuis juin"),
             ("0,91", "Le rapport loyers sur revenus : les loyers sont au plus bas du couloir historique")],
            "L'honnêteté", "Ces repères viennent de la vidéo de Sébastien, d'après Crédit Logement et les courbes de Friggit. Un outil de pilotage ne donne aucun conseil d'investissement.",
            lead="Un marché figé récompense celui qui sait exactement ce qu'il achète."),

    d.cta_sans_commentaire(
        "Action · sans commentaire",
        'Sais-tu ce que ton<br>prochain bien peut ' + acc("vraiment") + ' faire ?',
        "RENDEZ-VOUS SUR",
        "Enregistre ce post, et découvre le module d'étude de marché sur le site.",
        "Dans un marché lent, la différence se joue avant l'offre, pas après."),

    d.closing("Le chiffre avant la signature, "
              + "<em>pas la surprise après</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("guestlucky", "cover_mot")
    noter_theme("guestlucky", "clair")
