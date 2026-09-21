#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 du carrousel Le Sous Loueur, a partir de la video
"Expatrie : le mythe des 183 jours va te couter tres cher"
(21/09/2026, ZdEMuAtcJcE).

Angle coaching : LES QUATRE CRITERES DE LA RESIDENCE FISCALE. Les 183 jours ne
sont qu'un critere sur quatre, et le plus dangereux est le dernier : le centre
des interets economiques, celui qui rattrape les proprietaires bailleurs.

⛔ Prudences graves pour cette video :
  - Sebastien n'est ni avocat fiscaliste ni conseiller : il le dit lui-meme
    dans la video (les fiscalistes s'engagent, pas lui). Il parle de son
    experience, il est expatrie en Thailande, et de faits publics.
  - L'IMPOT UNIVERSEL A ETE REJETE. L'amendement d'octobre 2025 n'est PAS en
    vigueur : 131 voix pour, 132 contre. Ne jamais le presenter autrement.
  - Sur les prelevements sociaux a la revente, Sebastien hesite lui-meme et
    renvoie au notaire : on garde la reserve telle quelle.
  - Les noms de ses outils de declaration ne sont PAS repris : la
    transcription automatique les ecrit de plusieurs facons.

Theme CLAIR, couverture cover_bandeau, scene de fond "rebord_fenetre"
(regle 18 : la semaine derniere LSL etait en sombre avec un sommaire).

Usage : python3 v2_lsl_mythe_183_jours.py && python3 render.py v2_lsl_mythe_183_jours
"""
from design_v2 import Deck, acc, noter_couverture, noter_theme

SLUG = "v2_lsl_mythe_183_jours"

d = Deck("lesousloueur", "clair")
d.set_bg_photo("lsl_mythe_183_jours_bg.jpg", veil=0.82)

SLIDES = [
    d.cover_bandeau(
        "Le Sous Loueur · Expatriation",
        "Le mythe des<br>183 jours",
        "Quatre critères déterminent ta résidence fiscale, et un seul suffit. "
        "144 jours en France ont déjà suffi à requalifier un directeur général."),

    d.mindmap(1, "Les quatre vrais<br>critères", "Article 4 B du code général des impôts",
              "UN SEUL<br>SUFFIT",
              [("Ton foyer", "Là où vivent ton conjoint et tes enfants. Tu peux passer 300 jours à Dubaï : si ta famille est à Lyon, ton foyer est à Lyon."),
               ("Ton lieu de séjour", "Plus de la moitié de l'année en France. C'est ici que vivent les fameux 183 jours, et nulle part ailleurs."),
               ("Ton activité principale", "Là où tu exerces réellement tes fonctions, pas là où tu dors."),
               ("Tes intérêts économiques", "D'où vient l'argent qui te fait vivre. Le plus dangereux des quatre.")],
              "Le piège du deuxième", "Le critère des jours ne fonctionne que dans un sens : rester sous 183 jours ne te protège pas si tu coches un des trois autres.",
              lead="Ce n'est pas une moyenne ni un total de points : un seul critère coché fait de toi un résident fiscal français."),

    d.pincer(2, "144 jours<br>ont suffi", "L'affaire du directeur général",
             ("Ce qui jouait pour lui", "Il vivait en Suisse, dans sa maison, avec sa famille. Il passait bien plus de la moitié de l'année hors de France."),
             ("Ce qui a tout emporté", "Son entreprise avait son siège à La Défense, et c'est là qu'il exerçait réellement ses fonctions."),
             ("Le Conseil d'État l'a tranché", "Résident fiscal français, donc imposable en France sur l'ensemble de ses revenus mondiaux."),
             "Ce qu'il faut en retenir", "Compter ses jours ne sert à rien si le reste du tableau désigne la France.",
             lead="144 jours, c'est très en dessous du seuil dont tout le monde parle. Ça n'a pas pesé une seconde."),

    d.checklist(3, "Tu pars et tu gardes<br>ton appartement loué", "Le cas le plus fréquent",
                [(False, "Tes loyers français restent imposés en France",
                  "Ce sont des revenus de source française : toutes les conventions fiscales internationales le prévoient. Il n'y a pas d'échappatoire."),
                 (False, "Le taux d'imposition monte au lieu de baisser",
                  "Taux minimum de 20&nbsp;% pour un non-résident, 30&nbsp;% au-delà de 29 000 € de revenus imposables, quand un résident modeste serait à 0 ou 11&nbsp;%."),
                 (True, "Les prélèvements sociaux peuvent tomber à 7,5&nbsp;%",
                  "Au lieu de 17,2&nbsp;%, si tu es affilié à un régime de sécurité sociale de l'Union européenne, de Suisse ou du Royaume-Uni."),
                 (False, "Tes obligations déclaratives te suivent partout",
                  "En meublé, la liasse, les amortissements, le formulaire 2031 et l'immatriculation continuent intégralement, à 10 000 kilomètres comme à Paris.")],
                "Le vrai danger", "Si ces loyers font l'essentiel de tes revenus, le fisc peut considérer que le centre de tes intérêts est resté en France, et imposer TOUT ce que tu gagnes.",
                lead="Une cadre partie en Hongrie avec sa famille a été jugée résidente fiscale française en janvier 2025."),

    d.flow(4, "Tu télétravailles<br>depuis l'étranger", "Le champ de mines",
           [("Le principe de base",
             "Le salaire est imposable là où le travail est physiquement exercé. Tu travailles depuis Lisbonne, le travail est exercé au Portugal."),
            ("Chaque retour se compte",
             "Un séminaire, une semaine au bureau, une mission chez un client : ces jours sont imposables en France et ils sont comptés un par un."),
            ("Le risque que personne n'anticipe",
             "Si tu exerces des fonctions importantes depuis l'étranger, ta présence peut créer un établissement stable pour ton employeur.")],
           "Faire les choses proprement", "Un accord écrit de l'employeur, la convention fiscale vérifiée, et un comptage rigoureux des jours réellement passés en France.",
           lead="Ce sont les allers-retours qui coulent les dossiers, jamais le départ lui-même."),

    d.layers(5, "Tu gardes ton<br>ancienne résidence<br>principale", "Trois conséquences immédiates",
             [("Conséquence 1", "Elle devient une résidence secondaire",
               "Dès le départ, automatiquement. La taxe d'habitation revient, et elle peut être majorée jusqu'à 60&nbsp;% dans les zones tendues."),
              ("Conséquence 2", "L'exonération de plus-value disparaît",
               "L'administration tolère en pratique jusqu'à la fin de l'année qui suit le départ. Une revente 17 mois après a déjà été redressée."),
              ("Conséquence 3", "La surveillance se resserre",
               "Depuis 2023, la déclaration d'occupation est annuelle. Le fisc croise consommations d'eau et d'électricité, déclarations et passages aux frontières.")],
             "À vérifier avec ton notaire", "Il existe une exonération spécifique aux non-résidents, plafonnée à 150 000 € de plus-value et sous conditions. Le détail se règle avec lui, pas sur internet.",
             lead="Un appartement parisien vendu avant le départ peut coûter zéro impôt, et des dizaines de milliers d'euros deux ans plus tard."),

    d.compare(6, "Ce qui a changé,<br>et ce qui n'a<br>PAS changé", "Deux nouvelles de 2025",
              {"head": "Ce qui est bel et bien entré en vigueur", "items": [
                  "Le délai de reprise passe de 3 ans à 10 ans en cas de fausse domiciliation à l'étranger",
                  "Parti en 2025, tu peux devoir justifier ton départ jusqu'en 2035",
                  "Donc : baux, factures, billets d'avion, relevés, inscriptions scolaires, gardés dix ans"]},
              {"head": "Ce qui a été REJETÉ", "items": [
                  "L'impôt universel sur les expatriés, amendement d'octobre 2025",
                  "131 voix pour, 132 contre : une seule voix d'écart",
                  "Il n'est donc PAS applicable aujourd'hui",
                  "Mais il revient chaque année depuis 2019"]},
              "L'honnêteté", "Un amendement rejeté n'est pas une règle. C'est un paramètre à garder en tête, pas une raison de paniquer.",
              lead="La première change ta façon d'archiver. La seconde n'a rien changé du tout, à une voix près."),

    d.checklist(7, "Avant de partir", "Les cinq points",
                [(True, "Passe tes quatre critères en revue",
                  "Foyer, séjour, activité, intérêts économiques. Si tu en coches un, tu as un sujet à régler avant de faire tes cartons."),
                 (True, "Décide du sort de ta résidence principale AVANT le départ",
                  "Vendue avant, l'exonération s'applique. Vendue longtemps après, la facture se compte en dizaines de milliers d'euros."),
                 (True, "Mets à jour ta déclaration d'occupation",
                  "Et vérifie ta situation foncière : une seule incohérence entre tes déclarations suffit à déclencher un contrôle."),
                 (True, "Inscris-toi au consulat et garde tes preuves",
                  "Bail, factures, inscriptions scolaires : le fisc ne te croit pas sur parole, il demande des papiers.")],
                "Le cinquième", "Ne compte jamais sur les 183 jours. Ce qui compte, c'est le tableau d'ensemble : ta famille, ton argent, ton activité.",
                lead="Cinq vérifications à faire maintenant, pas le jour du départ."),

    d.cta("Action · 1 mot",
          'Ton départ tient-il<br>aux ' + acc("quatre critères") + ' ?',
          "EXPAT",
          "et je t'envoie la checklist des 5 points à vérifier avant de partir.",
          "Sébastien est lui-même expatrié. Il partage son expérience, pas un conseil de fiscaliste."),

    d.closing("Les 183 jours ne sont pas un bouclier. "
              + "<em>Ils ne l'ont jamais été.</em>"),
]

if __name__ == "__main__":
    d.write(SLUG, SLIDES)
    noter_couverture("lesousloueur", "cover_bandeau")
    noter_theme("lesousloueur", "clair")
