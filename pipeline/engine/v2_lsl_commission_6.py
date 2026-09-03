#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Frais Airbnb : ce qui change vraiment pour les hotes" (ARDRtYtIgSk, 02/09/2026).

Angle coaching : DECRYPTER LA MANOEUVRE ET BATIR L'ENTONNOIR. Sujet neuf.

⚠️ REGLE 16 : couverture cover_chiffre (le 6 % plein cadre). La couverture
classique a servi le 31/08, on ne la reprend pas.
⚠️ REGLE 15 : legende sous 2000 signes.
⛔ Rappel : ce n'est PAS de la reservation en direct. La reservation reste sur
Airbnb. Ne jamais laisser croire l'inverse, c'est justement la rumeur que
Sebastien dement dans la video.
⛔ Le niveau "10 %" evoque dans la video est incertain (selon les sources) :
on ne le grave pas dans une slide.

Usage : python3 v2_lsl_commission_6.py && python3 render.py v2_lsl_commission_6
"""
from design_v2 import Deck, acc, noter_couverture

SLUG = "v2_lsl_commission_6"

d = Deck("lesousloueur")
d.set_bg_photo("lsl_commission_6_bg.jpg", veil=0.88)

SLIDES = [
    d.cover_chiffre(
        "Le Sous Loueur",
        "6", "%",
        "La commission qu'Airbnb<br>teste en ce moment",
        "Ce n'est pas un cadeau. C'est un aveu, et il vaut de l'or si tu le lis bien."),

    d.pincer(1, "Ce qui se passe<br>vraiment", "Et ce qui est faux",
             ("La rumeur", "Airbnb lancerait la réservation en direct. C'est faux, et il faut le dire clairement."),
             ("La réalité", "Un lien tracé, généré par Airbnb. Le voyageur qui passe par lui fait tomber ta commission à 6&nbsp;%."),
             ("Mais la réservation reste chez eux", "Messagerie, protection, avis : tout se passe sur Airbnb. C'est une réservation Airbnb à tarif réduit, parce que c'est toi qui amènes le client."),
             "À savoir", "Testé aux États-Unis seulement, rapporté fin août. Rien n'est annoncé en Europe à ce jour.",
             lead="Une nouvelle circule depuis une semaine, et elle est mal comprise."),

    d.stats(2, "Ce qu'Airbnb<br>vient d'avouer", "Le calcul qu'ils ont publié malgré eux",
            [("15,5 %", "Quand c'est Airbnb qui trouve le client"),
             ("6 %", "Quand c'est toi qui l'amènes"),
             ("9,5 points", "L'écart, soit le prix qu'ils mettent sur l'acquisition"),
             ("95 €", "Ce que ça représente sur une réservation de 1&nbsp;000&nbsp;€")],
            "La vraie information", "Ta base client, tes anciens voyageurs, tes abonnés : Airbnb vient de chiffrer ce que ça vaut.",
            lead="Pourquoi une société cotée accepterait-elle de gagner moins ?"),

    d.checklist(3, "Les trois pièges", "Avant de te réjouir",
                [(False, "Le client redevient celui d'Airbnb",
                  "Son email, son historique, sa fidélité repartent chez eux. Tu paies 6&nbsp;% pour céder un client qui était à toi."),
                 (False, "Le curseur qui rogne ton gain",
                  "Il reverse une partie de l'économie au voyageur. Tu entraînes ta clientèle à attendre des remises."),
                 (False, "Un taux qui n'est pas garanti",
                  "C'est un test, non standardisé, modifiable par un simple email. Comme les frais partagés avant lui.")],
                "La consigne", "Le jour où ça arrive, active le lien, mais ne touche pas au curseur.",
                lead="Trois pièges, et le premier coûte bien plus cher que la commission."),

    d.compare(4, "La question<br>a changé", "Et presque personne ne l'a vu",
              {"head": "Ce qu'on se demandait avant", "items": [
                  "Combien Airbnb me prend-il ?",
                  "Un taux unique pour tout le monde",
                  "Une ligne de coût que je subis",
                  "Je déduis 15,5&nbsp;% de toutes mes études"]},
              {"head": "Ce qu'il faut se demander", "items": [
                  "Combien me coûte un client, selon le canal ?",
                  "Un prix qui dépend de qui l'a trouvé",
                  "Un investissement que je pilote",
                  "Et combien ce client me rapporte dans le temps"]},
              "Le basculement", "Airbnb facture désormais le client, pas la réservation. Ça change toute la stratégie.",
              lead="Ce n'est plus le même métier de calcul."),

    d.layers(5, "Tes trois<br>voyageurs", "Le canal dépend de la relation",
             [("L'inconnu", "Tu paies 15,5&nbsp;%, sans discuter",
               "Airbnb l'a trouvé, rassuré, convaincu. C'est le prix d'un client que tu n'aurais jamais eu."),
              ("Le connecté", "Le lien tracé, à 6&nbsp;%",
               "Il te connaît mais n'a jamais dormi chez toi. Il veut encore la sécurité de la plateforme."),
              ("Le fidèle", "Le direct pur, sans commission",
               "Il a déjà séjourné, il te fait confiance. Airbnb n'apporte plus rien à cette relation.")],
             "Le seul objectif avec l'inconnu", "Qu'il ne reparte pas inconnu. Il arrive par Airbnb, il doit finir dans ta base.",
             lead="Un entonnoir, pas trois cases figées : 15,5 puis 6 puis 0."),

    d.flow(6, "Ton plan,<br>dès maintenant", "Rien n'est annoncé en Europe",
           [("Mesure où tu en es",
             "Combien de voyageurs des 12 derniers mois peux-tu recontacter sans Airbnb ? Si c'est zéro, tu es leur fournisseur à vie."),
            ("Installe la capture au bon moment",
             "L'enregistrement en ligne, quand il renseigne sa caution et consulte le livret. Avec consentement, dans les règles."),
            ("Donne une identité à ton logement",
             "Pas un trois pièces vue mer : un nom qu'on retient, des comptes, des avis. On fidélise un nom.")],
           "La fidélité", "En nature, jamais en prix : départ tardif, panier d'accueil, surclassement, priorité l'été.",
           lead="Trois gestes qui ne coûtent presque rien et changent tes marges."),

    d.mindmap(7, "Le pari<br>qu'ils font", "Et pourquoi il peut échouer",
              "Six vaut<br>mieux que<br>zéro",
              [("Leur calcul", "Un voyageur que tu envoies en direct pur leur rapporte 0. Par le lien réduit, il rapporte 6."),
               ("Ce qu'ils rachètent", "L'étage intermédiaire de ton entonnoir, celui du voyageur qui te connaît déjà."),
               ("Leur pari", "Que la majorité des hôtes ne franchiront jamais le pas du vrai direct."),
               ("Ce qui les inquiète", "La réservation en direct double chaque année. C'est ça qui a déclenché la manœuvre.")],
              "À retenir", "Ils ne baissent pas leurs prix par générosité. Ils négocient pour ne pas te perdre.",
              lead="Airbnb a fait ses comptes avant de te faire cette offre."),

    d.cta("Action · 1 mot",
          'Combien de tes voyageurs<br>peux-tu ' + acc("recontacter") + ' ?',
          "DIRECT",
          "et je t'envoie le plan pour construire ta base client, étape par étape.",
          "Le 13 octobre, tout le monde passe à 15,5&nbsp;%. Ta base, elle, ne dépend de personne."),

    d.closing("11 ans de terrain pour t'aider à posséder "
              + "<em>tes propres clients</em>."),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_chiffre")
