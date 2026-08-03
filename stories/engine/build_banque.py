#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE DE SEQUENCES V3 : stories "aide gratuite" auto-suffisantes, construites
a partir des transcriptions des videos YouTube de Sebastien (@moresebastien).

Direction validee avec Martin (03/08/2026, apres rejet V1 "navy vide" et V2
"trop template a trous") :
  - CHAQUE story est complete et prete a poster : AUCUNE photo/screenshot a
    rajouter par Martin
  - le contenu donne de la VRAIE aide : conseils concrets, chiffres, methodes
    tires des videos (jamais inventes)
  - style visuel : fonds photo chauds Gemini + serif blanche + listes noires
    sur voile blanc + touches dessinees (fleches, soulignes) + annotations
    manuscrites

Gabarits : cover / steps / focus / duo / fin.
Rendu : python3 render_stories.py banque-01
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[0]
FONTS = REPO / "pipeline" / "assets" / "fonts"
BGS = ROOT / "assets" / "backgrounds"

BLEU   = "#4E9FE0"
BLEUF  = "#2F7EC4"
ROUGE  = "#C94F43"
NOIR   = "#161616"
BLANC  = "#ffffff"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font_face(family, file, weight):
    data = b64(FONTS / file, "font/woff2")
    return (f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")

FONT_FACES = "".join([
    font_face("Montserrat", "montserrat-latin-500-normal.woff2", 500),
    font_face("Montserrat", "montserrat-latin-600-normal.woff2", 600),
    font_face("Montserrat", "montserrat-latin-700-normal.woff2", 700),
    font_face("Montserrat", "montserrat-latin-800-normal.woff2", 800),
    font_face("Playfair", "playfair-display-latin-700-normal.woff2", 700),
    font_face("Playfair", "playfair-display-latin-800-normal.woff2", 800),
    font_face("Caveat", "caveat-latin-600-normal.woff2", 600),
])

COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;
   text-rendering:geometricPrecision;}}
.story{{width:1080px;height:1920px;position:relative;overflow:hidden;color:{BLANC};
  background:#888;font-family:'Playfair',serif;}}
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:center;}}
.pad{{position:absolute;inset:0;padding:270px 76px 380px;z-index:2;display:flex;
  flex-direction:column;}}

.serif{{font-family:'Playfair',serif;font-weight:800;color:{BLANC};
  text-shadow:0 2px 22px rgba(0,0,0,0.45), 0 1px 4px rgba(0,0,0,0.35);}}
.serif .b{{color:{BLEU};}}
.t1{{font-size:80px;line-height:1.14;}}
.t2{{font-size:56px;line-height:1.2;}}
.t3{{font-size:44px;line-height:1.25;}}

.hand{{font-family:'Caveat',cursive;font-weight:600;color:{BLANC};
  text-shadow:0 2px 14px rgba(0,0,0,0.5);}}

.veil{{background:rgba(255,255,255,0.72);border-radius:26px;padding:40px 38px;
  backdrop-filter:blur(7px);box-shadow:0 14px 44px rgba(0,0,0,0.18);}}
.step{{display:flex;gap:24px;margin-bottom:30px;align-items:flex-start;}}
.step:last-child{{margin-bottom:0;}}
.stepn{{flex-shrink:0;width:58px;height:58px;border-radius:50%;background:{BLEUF};
  color:{BLANC};font-family:'Montserrat',sans-serif;font-weight:800;font-size:30px;
  display:flex;align-items:center;justify-content:center;margin-top:2px;}}
.steph{{font-family:'Montserrat',sans-serif;font-weight:800;font-size:31px;
  line-height:1.25;color:{NOIR};}}
.stept{{font-family:'Montserrat',sans-serif;font-weight:500;font-size:26px;
  line-height:1.38;color:#333;margin-top:6px;}}
.stept .b{{color:{BLEUF};font-weight:700;}}
.steph .b{{color:{BLEUF};}}

.duohead{{font-family:'Montserrat',sans-serif;font-weight:800;font-size:29px;
  text-transform:uppercase;letter-spacing:1px;margin-bottom:18px;}}
.duoli{{font-family:'Montserrat',sans-serif;font-weight:600;font-size:26px;
  line-height:1.4;color:{NOIR};margin-bottom:12px;}}
.duoli:last-child{{margin-bottom:0;}}

.abs{{position:absolute;}}
"""

def acc(w):
    return f'<span class="b">{w}</span>'

def nb(text):
    if not text:
        return text
    for p in ("?", "!", ":", ";"):
        text = text.replace(f" {p}", f"&nbsp;{p}")
    return text.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")

def open_story(bg):
    img = b64(BGS / f"{bg}.jpg", "image/jpeg")
    return f'<div class="story"><div class="bgimg" style="background-image:url({img});"></div>'

def underline(width=430, color=BLEU, x=0, y=0):
    w = width
    path = f"M 8 11 C {w*0.22:.0f} 3, {w*0.4:.0f} 15, {w*0.58:.0f} 9 S {w*0.85:.0f} 5, {w-8:.0f} 10"
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;" width="{w}" height="20" '
            f'viewBox="0 0 {w} 20" fill="none"><path d="{path}" stroke="{color}" '
            f'stroke-width="8" stroke-linecap="round"/></svg>')

def arrow_down(x, y, w=220, h=280, color=BLANC, flip=False):
    sx, c1x, c2x, ex = (w*0.15, w*0.75, w*0.95, w*0.55) if not flip else \
                       (w*0.85, w*0.25, w*0.05, w*0.45)
    path = f"M {sx:.0f} 18 C {c1x:.0f} {h*0.25:.0f}, {c2x:.0f} {h*0.6:.0f}, {ex:.0f} {h-26:.0f}"
    a1x = ex - 34 if not flip else ex + 34
    a2x = ex + 26 if not flip else ex - 26
    head = (f'<path d="M {a1x:.0f} {h-92:.0f} L {ex:.0f} {h-22:.0f}" stroke="{color}" stroke-width="11" stroke-linecap="round"/>'
            f'<path d="M {a2x:.0f} {h-86:.0f} L {ex:.0f} {h-22:.0f}" stroke="{color}" stroke-width="11" stroke-linecap="round"/>')
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" fill="none">'
            f'<path d="{path}" stroke="{color}" stroke-width="11" stroke-linecap="round"/>{head}</svg>')

# ------------------------------------------------------------------ gabarits

def cover(bg, hand_top, title, sub=None, hand_bottom="la suite juste après"):
    """Ouverture de sequence : promesse claire."""
    h = (f'<div class="hand" style="font-size:56px;margin-bottom:26px;">{nb(hand_top)}</div>'
         if hand_top else '')
    s = (f'<div class="serif t3" style="margin-top:40px;font-weight:700;">{nb(sub)}</div>'
         if sub else '')
    return (open_story(bg) + '<div class="pad" style="justify-content:center;">'
            + h + f'<div class="serif t1">{nb(title)}</div>' + s
            + f'<div class="hand" style="font-size:50px;position:absolute;right:230px;bottom:430px;">'
            f'{nb(hand_bottom)}</div>'
            + arrow_down(940, 1330, 120, 170, BLANC)
            + '</div></div>')

def steps(bg, title, items, start=1, title_size="t2"):
    """Etapes/conseils numerotes sur voile blanc. items = [(label, texte)]."""
    rows = ""
    for i, (label, texte) in enumerate(items, start):
        t = f'<div class="stept">{nb(texte)}</div>' if texte else ''
        rows += (f'<div class="step"><div class="stepn">{i}</div>'
                 f'<div><div class="steph">{nb(label)}</div>{t}</div></div>')
    return (open_story(bg) + '<div class="pad">'
            f'<div class="serif {title_size}">{nb(title)}</div>'
            f'<div class="veil" style="margin-top:44px;">{rows}</div>'
            '</div></div>')

def focus(bg, kicker, big, body=None, hand=None):
    """Une idee forte : gros serif + explication sur voile."""
    k = (f'<div class="hand" style="font-size:52px;margin-bottom:24px;">{nb(kicker)}</div>'
         if kicker else '')
    b = ''
    if body:
        b = (f'<div class="veil" style="margin-top:46px;">'
             f'<div class="stept" style="font-size:28px;line-height:1.45;margin-top:0;">{nb(body)}</div></div>')
    h = (f'<div class="hand" style="font-size:50px;position:absolute;right:100px;bottom:410px;">{nb(hand)}</div>'
         if hand else '')
    return (open_story(bg) + '<div class="pad" style="justify-content:center;">'
            + k + f'<div class="serif t1">{nb(big)}</div>' + b + h
            + '</div></div>')

def duo(bg, title, bad_head, bad_items, good_head, good_items):
    """A eviter / a faire, deux cartes empilees."""
    def card(head, items, color):
        lis = "".join(f'<div class="duoli"><span style="color:{color};font-weight:800;">'
                      f'{"×" if color == ROUGE else "→"}</span>&nbsp; {nb(t)}</div>' for t in items)
        return (f'<div class="veil" style="margin-top:34px;padding:34px 36px;">'
                f'<div class="duohead" style="color:{color};">{nb(head)}</div>{lis}</div>')
    return (open_story(bg) + '<div class="pad">'
            f'<div class="serif t2">{nb(title)}</div>'
            + card(bad_head, bad_items, ROUGE)
            + card(good_head, good_items, BLEUF)
            + '</div></div>')

def fin(bg, title, hand, keyword=None):
    """Fin de sequence : CTA."""
    kw = ''
    if keyword:
        kw = (f'<div class="serif" style="font-size:50px;margin-top:44px;">Réponds</div>'
              f'<div class="serif" style="font-size:84px;margin-top:8px;">'
              f'«&nbsp;{acc(keyword)}&nbsp;»</div>')
    return (open_story(bg) + '<div class="pad" style="justify-content:center;">'
            f'<div class="serif t2">{nb(title)}</div>' + kw
            + underline(560, BLANC, x=80, y=1150)
            + f'<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1190px;">{nb(hand)}</div>'
            + '</div></div>')

# ------------------------------------------------------- les sequences (contenu)
# Contenu 100 % tire des transcriptions YouTube de Sebastien (rien d'invente).

SEQUENCES = {

# ============================================================================
# SEQUENCE A — Remplir son Airbnb sans baisser les prix (video URH12GYwAuc)
# ============================================================================
"A_remplir_sans_baisser": [
    cover("bg_mer_calme", "aide gratuite",
          f'Remplir ton Airbnb {acc("sans baisser")} tes prix.',
          sub="Airbnb ne classe pas par prix : il met en avant ce qui convertit. "
              "Voici les leviers concrets.",
          hand_bottom="du concret, juste après"),
    focus("bg_mer_calme", "levier 1 : le tarif par voyageur",
          f'Affiche {acc("95 € pour 2")}, pas 120 € pour tous.',
          body="La majorité des recherches se font avec le réglage par défaut, 1-2 "
               "voyageurs. Un T3 affiché 95 € pour 2 + 12 € par voyageur en plus passe "
               "devant les concurrents à 120 €. Le couple paie 95 €, la famille de 4 "
               "paie 119 €. Tu n'as rien bradé."),
    focus("bg_ciel_dore", "levier 2 : ignoré par 90 % des hôtes",
          f'Le tarif {acc("non remboursable")} à -10 %.',
          body="Ton annonce s'affiche moins chère dans les résultats, donc mieux "
               "classée. Et la remise ne s'applique qu'aux voyageurs qui acceptent le "
               "non remboursable : ceux qui n'auraient jamais annulé de toute façon."),
    steps("bg_mer_calme",
          f'Les équipements sont des {acc("filtres de recherche")}',
          [("Coche TOUT ce que tu as", "Non coché = invisible pour celui qui filtre. Pense au sèche-cheveux, au fer, au détecteur de fumée."),
           ("Le combo famille", "Lit parapluie + chaise haute : tu ressors dans les filtres famille plusieurs fois."),
           ("Le canal télétravail", "Un vrai espace de travail, et le débit wifi mesuré écrit dans l'annonce.")]),
    steps("bg_ciel_dore",
          f'Ta vitrine : la {acc("photo")} et le {acc("titre")}',
          [("La couverture, jamais le salon", "Montre le distinctif : la vue, le jacuzzi, la terrasse. En miniature, un salon ressemble à tous les salons."),
           ("Le titre en 50 caractères", "Capacité + atout star + lieu : « 6 personnes, jacuzzi, 5 min de la plage »."),
           ("Les avis à mots-clés", "L'algorithme lit le texte des avis. Invite tes voyageurs à citer le jacuzzi, le check-in... pendant 6 mois.")]),
    fin("bg_mer_calme",
        "Tu veux savoir ce que vaut TON annonce ?",
        "et on t'envoie l'outil d'audit gratuit", keyword="AUDIT"),
],

# ============================================================================
# SEQUENCE B — Trouver des proprios : les 5 canaux (video Kjml8l9gNwg)
# ============================================================================
"B_trouver_clients": [
    cover("bg_ciel_dore", "la méthode des pros",
          f'Trouver des proprios : les {acc("5 canaux")}, classés.',
          sub="Du moins au plus efficace. Ce que font les property managers "
              "américains, adapté à la France.",
          hand_bottom="le classement arrive"),
    steps("bg_ciel_dore",
          f'Du moins au plus {acc("puissant")}',
          [("La prospection ciblée", "Airbnb affiche la région où habite l'hôte : vise les proprios loin de leur bien."),
           ("Les apporteurs d'affaires", "Ménage, artisans, gardiens d'immeuble : liste 10 entreprises locales, propose un vrai deal."),
           ("Les agents immobiliers", "Échange gagnant-gagnant : tes proprios vendeurs contre ses investisseurs."),
           ("La référence locale", "Fiche Google + avis de PROPRIOS. 15 avis et tu écrases la concurrence."),
           ("L'audit chiffré", "Le canal le plus redoutable. Détail juste après.")],
          title_size="t3"),
    focus("bg_ville_doree", "le canal n°1",
          f'Fais un {acc("audit")}, pas un pitch.',
          body="Repère une annonce qui sous-performe : mauvaises notes, trous en "
               "juillet, prix qui ne bougent jamais. Chiffre son manque à gagner avec "
               "un outil de data : « tu perds peut-être 8 000 € par an ». Tu offres "
               "l'info, tu ne vends rien : le proprio voit le chiffre tout seul."),
    duo("bg_ciel_dore", f'Deux {acc("pièges")} à éviter',
        "Jamais", ["Prospecter via la messagerie Airbnb : bannissement possible",
                   "Le pitch commercial direct : valeur perçue zéro"],
        "À la place", ["Retrouve le proprio ailleurs : son site, sa fiche Google, Le Bon Coin",
                       "Offre l'audit et laisse les chiffres parler"]),
    focus("bg_ville_doree", "l'astuce que personne ne fait",
          f'Demande des avis Google à tes {acc("proprios")}, pas à tes voyageurs.',
          body="Celui qui tape « conciergerie + ta ville » est un prospect chaud. "
               "15 avis de propriétaires satisfaits et tu écrases la concurrence "
               "locale. Bonus : crée une page par quartier, même par rue. Sur "
               "« conciergerie + nom de ta rue », il n'y a personne."),
    fin("bg_ciel_dore",
        "On regarde ensemble ton plan pour trouver des proprios ?",
        "réponds à cette story", keyword="GO"),
],

# ============================================================================
# SEQUENCE C — Recuperer les proprios decus (video t_sxyIULJEQ)
# ============================================================================
"C_proprios_decus": [
    cover("bg_ville_doree", "aide gratuite du jour",
          f'Ton meilleur client&nbsp;? Le proprio {acc("déçu")} d\'une autre conciergerie.',
          sub="Comment le trouver avant tout le monde, légalement.",
          hand_bottom="la méthode juste après"),
    steps("bg_ville_doree",
          f'Les {acc("5 phases")} d\'un proprio qui va quitter sa conciergerie',
          [("Mois 1 à 3 : la lune de miel", "Il vient de déléguer, il est soulagé, tout va bien."),
           ("Mois 4 à 8 : le doute", "Communication lente, tarifs qui semblent bas, avis moyens."),
           ("Mois 8 à 12 : la comparaison", "Il regarde les autres conciergeries et parle aux voisins proprios."),
           ("Mois 12 à 18 : la frustration", "Il fait ses comptes : la rentabilité promise n'est pas là."),
           ("La rupture", "Lettre recommandée, ou il attend la fin de saison et il part.")],
          title_size="t3"),
    focus("bg_ville_doree", "le vrai secret, c'est le timing",
          f'Tout se joue entre le {acc("mois 4")} et le {acc("mois 12")}.',
          body="En phase de doute, il tape déjà ses questions sur Google. Si ton contenu "
               "répond à ses douleurs à ce moment-là, tu deviens sa référence. Une fois la "
               "rupture décidée, tout le monde se bat pour lui : c'est la guerre du moins cher."),
    steps("bg_ville_doree",
          f'3 {acc("aimants")} qui font venir les proprios déçus à toi',
          [("L'audit gratuit en 48 h", "Il t'envoie son annonce, tu réponds sous 48 h. Bonus : tu vois le bien et la gestion AVANT de t'engager."),
           ("Le calculateur de revenus", "Il entre son adresse et découvre ce que son bien devrait vraiment rapporter."),
           ("La checklist des 10 questions", "« Les 10 questions à poser à votre conciergerie. » Tu éduques, tu ne vends pas.")]),
    duo("bg_ville_doree", f'Côté légal, la ligne est {acc("claire")}',
        "Jamais", ["Dénigrer un concurrent par son nom",
                   "Démarcher les clients d'un concurrent au téléphone",
                   "Récupérer des emails sur les annonces (RGPD)"],
        "Toujours", ["Éduquer avec du contenu qui répond à leurs douleurs",
                     "Une transition clé en main, comme un changement d'opérateur",
                     "Des avant/après chiffrés de proprios qui ont changé"]),
    fin("bg_ville_doree",
        "Tu veux qu'on regarde ensemble ta stratégie d'acquisition ?",
        "réponds à cette story", keyword="GO"),
],

# ============================================================================
# SEQUENCE D — De 0 a 30 logements en 1 an (video Mq4pGuah050)
# ============================================================================
"D_30_logements": [
    cover("bg_prairie", "la méthode complète 2026",
          f'De {acc("0 à 30 logements")} en 1 an.',
          sub="Les 4 piliers, et les 3 erreurs qui condamnent 90 % des conciergeries.",
          hand_bottom="c'est cadeau, juste après"),
    steps("bg_prairie",
          f'Les {acc("3 erreurs")} qui plafonnent 90 % des conciergeries',
          [("Le mode bricolage", "Contrat trouvé sur internet, annonces sur TON compte Airbnb. À 10 logements, tout est à refaire."),
           ("Vendre de la « gestion »", "« Gérer », « mandat » : ces mots te font tomber sous la loi Hoguet. Dis pilotage, coordination, prestation."),
           ("Empiler les contrats", "À 8-10 contrats sans système, tu es devenu le salarié de ta propre boîte.")]),
    steps("bg_prairie",
          f'La roadmap des {acc("4 piliers")}',
          [("Contrats 1 à 5 : les fondations", "Contrat conforme, UNE ville et 30 km max, des prix jamais bradés."),
           ("5 à 12 : le système", "Channel manager, messages automatiques, onboarding standardisé, ménage sous-traité."),
           ("10 à 20 : les leviers", "Parrainage structuré, proprios déçus, référencement local. Premier city manager."),
           ("20 à 30 : l'industrialisation", "Tu pilotes aux chiffres : occupation, prix moyen par nuit, satisfaction proprio.")],
          title_size="t3"),
    focus("bg_prairie", "la règle qui change tout en 2026",
          f'Tout au nom du {acc("propriétaire")}.',
          body="Comptes Airbnb et Booking, revenue management : c'est le proprio qui pilote "
               "et qui valide. En 2025, des conciergeries ont été condamnées pour avoir géré "
               "les prix sans validation. Et les juges vérifient l'opérationnel, pas juste le contrat."),
    focus("bg_prairie", "le canal que personne ne structure",
          f'Le bouche à oreille, ça se {acc("fabrique")}.',
          body="Offre 1 mois de prestation au proprio qui t'amène un nouveau client. Même "
               "mécanique avec les agents immobiliers et les experts-comptables LMNP. "
               "C'est un canal d'acquisition, pas de la chance."),
    fin("bg_prairie",
        "La méthode complète est en vidéo sur la chaîne.",
        "et pour en parler, réponds GO"),
],

# ============================================================================
# SEQUENCE E — L'algorithme Airbnb 2026 (video 9pTFTNPkf-g)
# ============================================================================
"E_algo_2026": [
    cover("bg_ville_doree", "info chaude 2026",
          f'L\'algorithme Airbnb a {acc("changé")}. Voici les nouvelles règles.',
          sub="Airbnb ne montre plus les « meilleurs » logements : il montre le plus "
              "adapté à chaque voyageur.",
          hand_bottom="les vrais chiffres arrivent"),
    focus("bg_ville_doree", "ce qui pèse vraiment",
          f'Ton séjour pèse {acc("50 %")}. Ta photo, {acc("8 %")}.',
          body="Haut du tunnel (photo, titre, prix) : 20 %. Milieu (clics, messages, "
               "favoris) : 30 %. Bas (réservation, séjour réel, avis, problèmes) : "
               "50 %. La plupart optimisent dans le mauvais sens : un séjour en béton "
               "d'abord, la photo ensuite."),
    steps("bg_ville_doree",
          f'Les nouveaux {acc("poids")} du classement',
          [("Guest Favorite : 25 %", "Le nouveau Graal, le Superhost est obsolète. Critères : 4,9+ et au moins 5 avis en 2 ans."),
           ("Les avis récents : 20 %", "L'algorithme lit le TEXTE. Un 4,8 enthousiaste bat un 5 étoiles « correct »."),
           ("Propreté, exactitude, check-in", "Pondérés 2 fois plus. Un seul mauvais avis propreté = 10 à 20 places perdues."),
           ("La réponse : moins d'1 h", "Les meilleurs répondent en moins de 30 minutes.")],
          title_size="t3"),
    duo("bg_mer_calme", f'Ce qui ne {acc("marche plus")} en 2026',
        "Oublie", ["Le boost nouvelle annonce : quasi nul désormais",
                   "Tes bons avis de 2023 : seuls les 30-60 derniers jours comptent",
                   "Le Superhost et la course aux 5 étoiles"],
        "À la place", ["Instant Book activé : 15 à 25 % de boost",
                       "Une photo qui tranche : couleurs vives, photo saisonnière",
                       "Viser TES voyageurs, pas tous les voyageurs"]),
    focus("bg_ville_doree", "le levier le plus rapide",
          f'Changer la photo de couverture : jusqu\'à {acc("+35 %")}.',
          body="80 % des voyageurs décident en 2 ou 3 secondes. Démarque-toi de la "
               "concurrence locale : des couleurs vives quand tout le monde est en gris "
               "pastel, une photo de Noël dès fin novembre. Une annonce qui vit, "
               "l'algorithme le voit."),
    fin("bg_ville_doree",
        "Le plan d'action complet sur 30 jours est en vidéo.",
        "et pour le guide, réponds", keyword="ALGO"),
],

# ============================================================================
# SEQUENCE F — Le piege de la caution (video 4Dlw1_c593k)
# ============================================================================
"F_caution": [
    cover("bg_salon_cosy", "l'erreur qui coûte cher",
          f'La {acc("caution")} : le piège que 80 % découvrent trop tard.',
          sub="Caution, assurance, loi Hoguet : ce qu'il faut savoir AVANT l'incident.",
          hand_bottom="explication simple juste après"),
    focus("bg_salon_cosy", "la base que tout le monde confond",
          f'Caution et assurance, ce n\'est {acc("pas pareil")}.',
          body="La caution récupère l'argent DU voyageur : montant limité, litige "
               "possible. L'assurance fait payer un tiers : c'est l'assureur qui gère "
               "le sinistre. La vraie protection, c'est les deux couches empilées."),
    focus("bg_salon_cosy", "conciergeries : le test en une question",
          f'Qui {acc("déclenche")} le débit&nbsp;?',
          body="Si c'est la conciergerie, c'est du maniement de fonds pour le compte "
               "de tiers : illégal au sens de la loi Hoguet, même avec des "
               "sous-comptes. La solution propre : la caution part du compte de "
               "paiement DU propriétaire, jamais du tien."),
    steps("bg_salon_cosy",
          f'Les règles qui {acc("sauvent")}',
          [("Chèque, virement, espèces : terminé", "On ne demande plus jamais ça à un voyageur."),
           ("L'empreinte bancaire expire vite", "7 jours de garantie sur une empreinte classique : un dégât découvert tard, et il n'y a plus rien."),
           ("Débiter ne règle rien", "Le voyageur peut contester. Un sinistre bien documenté, photos à l'appui, change tout."),
           ("AirCover ne couvre qu'Airbnb", "Sur Booking et les résas en direct, sans solution dédiée, tu n'es couvert par rien.")],
          title_size="t3"),
    focus("bg_salon_cosy", "la stratégie des pros",
          f'Le {acc("double filet")} : caution + assurance.',
          body="La caution dissuade et couvre les petits dégâts. L'assurance prend le "
               "relais sur les gros sinistres et quand le débit échoue. Une assurance "
               "dédiée coûte environ 100 € par an, pour jusqu'à 50 000 € couverts."),
    fin("bg_salon_cosy",
        "Et toi, tu gères les cautions comment ?",
        "raconte en réponse, on te dit si c'est carré"),
],

# ============================================================================
# SEQUENCE G — Pourquoi ta conciergerie ne decolle pas (video CREH-yTwa1s)
# ============================================================================
"G_pourquoi_ca_bloque": [
    cover("bg_chemin_aube", "la vérité qui pique",
          f'{acc("90 %")} des conciergeries ferment en moins de 2 ans.',
          sub="Les 5 erreurs qui les tuent, et comment être dans les 10 %.",
          hand_bottom="check les 5, honnêtement"),
    steps("bg_chemin_aube",
          f'Les {acc("5 erreurs")} fatales',
          [("Pas de positionnement", "« Je fais de la conciergerie » = généraliste choisi sur le prix. Le spécialiste, lui, fixe ses tarifs."),
           ("Tout à la main", "Tableurs, messages copiés-collés, prix fixes toute l'année. Les pros automatisent et gèrent 3 fois plus."),
           ("Croire que le client, c'est le voyageur", "Le vrai client, c'est le proprio : c'est lui qui donne les clés, et qui peut les reprendre."),
           ("Ignorer ses chiffres", "Certains paient plus de ménage qu'ils n'encaissent, et le découvrent au bilan."),
           ("Tout faire tout seul", "Mois 1-3 : facile. Mois 7-9 : plus de vie. Mois 10-12 : j'arrête.")],
          title_size="t3"),
    focus("bg_chemin_aube", "le mythe du volume",
          f'50 biens à 15 %, c\'est travailler {acc("gratuitement")}.',
          body="Le volume est une vanité : ménage mal maîtrisé, occupation à 30-40 %, "
               "prix bradés... il ne reste rien. 10 logements bien choisis rapportent "
               "autant que 50 subis, avec beaucoup moins de stress."),
    focus("bg_chemin_aube", "la formule que personne ne calcule",
          f'Ton {acc("coût par nuitée")}, tu le connais&nbsp;?',
          body="Coût par nuitée = (ménage + linge + consommables + ton temps) divisé "
               "par le nombre de nuitées. Si ta commission est en dessous, tu refuses "
               "le bien. Savoir dire non, c'est la clé de la survie."),
    steps("bg_chemin_aube",
          f'Le reporting mensuel qui {acc("retient")} les proprios',
          [("Les revenus du mois", "Avec la variation vs le mois dernier et vs l'an dernier."),
           ("Le taux d'occupation", "Comparé au marché local."),
           ("La note voyageurs", "La moyenne, et le nombre d'avis."),
           ("Le prix moyen, expliqué", "« On a fait mieux que le marché grâce au pricing dynamique. »")]),
    fin("bg_chemin_aube",
        "« Un propriétaire bien informé ne part jamais. »",
        "la vidéo complète est sur la chaîne"),
],

# ============================================================================
# SEQUENCE H — Le plan de relance de zero (video N7aN4jh9ebw)
# ============================================================================
"H_plan_de_zero": [
    cover("bg_prairie", "s'il repartait de zéro",
          f'Le {acc("plan exact")} de Sébastien pour relancer une conciergerie.',
          sub="12 mois, 3 phases, objectifs chiffrés. Après 10 ans de terrain et près "
              "de 100 biens pilotés.",
          hand_bottom="phase par phase, juste après"),
    steps("bg_prairie",
          f'Phase 1 : les {acc("fondations")} (semaines 1 à 4)',
          [("Une zone de 15-20 minutes", "Une seule. Tu deviens la référence locale, pas un généraliste dispersé."),
           ("Le 1er client = preuve sociale", "1 ou 2 biens pilotés gratuitement 2 mois (le ménage reste payé) contre témoignages et photos."),
           ("Des process dès le début", "Checklists, protocoles, modèles de messages : structure comme si tu avais déjà une équipe.")]),
    steps("bg_mer_calme",
          f'Phase 2 : l\'{acc("accélération")} (mois 2 à 6)',
          [("Les outils au 5e bien", "Channel manager + logiciel de pilotage : environ 50 h par mois gagnées à 10 biens."),
           ("2-3 agents de ménage + 1 artisan", "La qualité de ton réseau, c'est ta réputation."),
           ("Le pricing dynamique", "Environ +15 % de revenus en moyenne."),
           ("Ta fiche Google", "43 % des proprios choisissent leur conciergerie via un avis Google.")],
          title_size="t3"),
    focus("bg_prairie", "phase 3 : la montée en gamme",
          f'À 30 € la nuit, tu gagnes {acc("6 €")}.',
          body="Vise les beaux biens : 400 à 500 € de gain par mois et par bien, et 10 "
               "biens font 5 000 € par mois. Une maison à 3 000 € de chiffre "
               "d'affaires demande le même travail qu'un appart à 700 €."),
    duo("bg_mer_calme", f'Ce qu\'il ne {acc("referait plus")}',
        "Fini", ["Accepter tous les biens, même les galères",
                 "Casser les prix à 12-15 % de commission",
                 "Le local et le site web dès le départ"],
        "À la place", ["L'audit gratuit sous 48 h : conversion triplée",
                       "3 offres au lieu d'un tarif unique",
                       "Un nouveau bien par semaine après le mois 3"]),
    fin("bg_prairie",
        "Objectif à 12 mois : 30 biens, 4 500 à 7 500 € par mois.",
        "et pour TON plan à toi, réponds GO"),
],

}

SLUG = "banque-01"
DASHES = "—–‒―⎯﹣－─"

def main():
    out = ROOT / "output" / SLUG / "html"
    out.mkdir(parents=True, exist_ok=True)
    n, td = 0, 0
    for seq, stories in SEQUENCES.items():
        for i, body in enumerate(stories, 1):
            name = f"{seq}_{i:02d}"
            html = f'<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body>{body}</body></html>'
            d = [c for c in html if c in DASHES]
            if d: print(f"  ALERTE tiret {name}: {set(d)}"); td += len(d)
            (out / f"{name}.html").write_text(html, encoding="utf-8")
            n += 1
    print(f"{n} stories ecrites dans {out}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
