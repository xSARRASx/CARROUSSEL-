#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur de la semaine, a partir de la video
"7 choses a ne jamais dire quand tu commences a gagner de l'argent" (02/08/2026).

Angle coaching : quand ta conciergerie ou ta sous-location commence a rapporter,
la discretion devient une competence. Les 7 silences et ce qu'ils protegent.

Chaque slide de contenu est un SCHEMA, jamais une liste de texte.

Usage : python3 v2_lsl_discretion_financiere.py && python3 render.py v2_lsl_discretion_financiere
"""
from design_v2 import Deck, acc

SLUG = "v2_lsl_discretion_financiere"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_discretion_financiere_bg.jpg", veil=0.88)

SLIDES = [
    d.cover(
        "Le Sous Loueur",
        'Quand ton activité<br>commence à ' + acc("rapporter"),
        "Les 7 choses à ne plus dire à personne, et ce qu'elles protègent",
        "30 ans d'entreprise, un dépôt de bilan à 40 ans, et ce que ça m'a appris."),

    d.mindmap(1, "Ce qui se passe<br>quand tu donnes un chiffre", "Quatre réactions, jamais une de plus",
              "Tu annonces<br>ce que tu gagnes",
              [("La moquerie", "C'est moins que ce qu'ils imaginaient, alors ils te rabaissent."),
               ("La jalousie", "C'est plus que ce qu'ils imaginaient, et la relation se tend."),
               ("L'attente", "Il gagne bien, donc il peut avancer, prêter, payer le restaurant."),
               ("Le calcul", "La personne cherche comment récupérer une part de ce que tu as.")],
              "Le problème", "Tu ne sais jamais à l'avance dans quelle catégorie se range celui qui t'écoute.",
              lead="Aucune de ces quatre réactions ne te rend service."),

    d.compare(2, "Ce qu'ils voient<br>et ce qu'ils ignorent", "La comparaison qui abîme",
              {"head": "Ce qu'ils regardent", "items": [
                  "Ton chiffre d'affaires, confondu avec ton bénéfice",
                  "Le résultat d'aujourd'hui, hors de son contexte",
                  "Ta réussite, comparée à leur propre situation",
                  "Ce que tu montres, jamais ce que tu portes"]},
              {"head": "Ce qu'ils ne voient pas", "items": [
                  "Les charges, les impôts, les mois sans rien",
                  "Les années de galère avant que ça décolle",
                  "Ton âge, tes choix, ton niveau de risque assumé",
                  "Le chemin, y compris les chutes"]},
              "À retenir", "Ils comparent leur intérieur avec ton extérieur : personne n'y gagne.",
              lead="Un chiffre sorti de son contexte ne veut plus rien dire."),

    d.layers(3, "Les 3 premiers<br>silences", "Ceux qui coûtent le plus cher",
             [("Silence 1", "Ta situation financière complète",
               "Ce que tu gagnes, ce qu'il y a sur le compte, le montant du dernier virement."),
              ("Silence 2", "Tes objectifs pas encore atteints",
               "Le projet que tu lances, le bien que tu vises, la date à laquelle tu quittes ton emploi."),
              ("Silence 3", "Le cash dont tu disposes",
               "Ton épargne de précaution devient un service que les autres attendent de toi.")],
             "Le glissement", "Dès qu'ils savent que tu as, tu passes de il a bien géré à il peut m'aider.",
             lead="Trois informations qui changent de nature dès qu'elles sortent de ta bouche."),

    d.pincer(4, "Pourquoi annoncer<br>un projet le tue", "Deux mécanismes, pas de la superstition",
             ("Le doute des autres", "Tu t'exposes au scepticisme au moment précis où ton projet est le plus fragile."),
             ("La récompense volée", "Les félicitations arrivent avant le travail, et ton cerveau a déjà touché sa part."),
             ("Un projet germe en silence", "Une graine, on ne la déterre pas chaque semaine pour vérifier qu'elle pousse."),
             "À retenir", "Travaille en silence et laisse le résultat faire le bruit à ta place.",
             lead="Deux effets se cumulent dès que tu annonces un objectif trop tôt."),

    d.checklist(5, "Les 4 autres<br>silences", "Du psychologique au concret",
                [(False, "Où se trouve ton argent",
                  "Ta banque, ton courtier, tes placements : chaque détail est une pièce de puzzle pour un malhonnête."),
                 (False, "Où tu habites et quand tu n'y es pas",
                  "Publie tes vacances au retour, jamais pendant. Ta maison est l'endroit où ta garde est baissée."),
                 (False, "Comment ton patrimoine est organisé",
                  "Un patrimoine se transmet devant notaire, pas en fin de repas de famille."),
                 (False, "Combien tu donnes",
                  "Un don rendu public change de nature : il devient une transaction contre de l'admiration.")],
                "Le principe", "Ce que les gens ne savent pas, ils ne peuvent pas l'utiliser.",
                lead="Quatre informations qui ouvrent la porte à des ennuis très concrets."),

    d.flow(6, "À qui tu peux<br>encore parler", "Le silence n'est pas l'isolement",
           [("Un mentor",
             "Quelqu'un qui est déjà passé par là et qui juge le projet, pas la personne."),
            ("Un associé ou un cercle très restreint",
             "Deux ou trois personnes qui te tirent vers le haut et dont le retour est constructif."),
            ("Personne d'autre",
             "Il y a une différence entre partager avec quelqu'un d'utile et diffuser à toute personne équipée de deux oreilles.")],
           "Le réflexe", "Choisis tes interlocuteurs à l'avance, avant d'être emporté par l'enthousiasme.",
           lead="Garder pour toi ne veut pas dire ne parler à personne."),

    d.stats(7, "Sept silences,<br>sept protections", "Le fil rouge",
            [("Ta paix", "Tu tais ta situation complète et tes chiffres exacts"),
             ("Ta vision", "Tu tais tes objectifs tant qu'ils ne sont pas atteints"),
             ("Ta sécurité", "Tu tais le montant de ton matelas de précaution"),
             ("Ton cœur", "Tu tais ce que tu donnes, et le geste redevient sincère")],
            "Le constat", "Aucune de ces sept choses ne t'apporte quoi que ce soit quand tu la racontes.",
            lead="Au mieux il ne se passe rien, au pire tu crées un problème qui mettra des années à exploser."),

    d.cta("Action · 1 mot",
          'La discrétion est<br>une ' + acc("compétence"),
          "SILENCE",
          "et je t'explique comment protéger ton activité quand elle commence à rapporter.",
          "Ceux qui durent financièrement sont presque toujours les plus discrets."),

    d.closing("11 ans de terrain pour t'aider à bâtir une activité "
              + "<em>solide</em>, pas une vitrine."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
