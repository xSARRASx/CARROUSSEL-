#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur du PACK ELEVES CONCIERGERIE : visuels Instagram "templates" que chaque
eleve (conciergerie deja lancee) personnalise avec SES couleurs, SON logo, SES
offres, puis poste tel quel. Objectif des posts : donner envie aux PROPRIETAIRES
de confier leur bien a la conciergerie.

Regles specifiques au pack :
- 1 visuel = 1 post (pas de carrousel) : 30 visuels = 30 posts.
- Style clair / editorial (fond creme), volontairement NEUTRE : chaque zone de
  marque est marquee "A personnaliser" (logo, couleur, ville, contact).
- Les contenus d'exemple sont prefixes "Exemple :" quand l'eleve doit les
  remplacer par ses propres infos.
- INTERDIT : le mot "gestion" (et derives), les emojis, les tirets longs.

Genere les 4 premiers visuels de demo dans output/pack_demo/html/slide_XX.html,
rendus ensuite par render.py ("python3 render.py pack_demo").
"""
import pathlib, re, base64, json, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS = ROOT / "assets" / "fonts"

# ---------- PROFIL ELEVE ----------
# Mode "template" (defaut) : zones pointillees "Ton logo ici", "Exemple :"...
# Mode "perso" : le pack est GENERE avec les infos de l'eleve (questionnaire
# pipeline/FORMULAIRE_ELEVE.md) : couleur, nom, ville, histoire, services...
# -> 30 eleves = 30 packs differents, personne ne modifie rien a la main.
PROFILE = {"mode": "template"}

def load_profile(path):
    global PROFILE
    PROFILE = {"mode": "perso", **json.loads(pathlib.Path(path).read_text(encoding="utf-8"))}

def is_perso():
    return PROFILE.get("mode") == "perso"

import hashlib
def pick(key, options):
    """Variation automatique anti-doublons : chaque eleve recoit une des
    formulations, choisie de facon stable a partir du nom de sa conciergerie.
    Deux eleves ne postent donc pas les memes titres. En mode template : la 1re."""
    if not is_perso():
        return options[0]
    h = int(hashlib.md5((PROFILE["nom"] + key).encode()).hexdigest(), 16)
    return options[h % len(options)]

def rotate(key, items):
    """Meme principe pour l'ORDRE des points d'un post (quand il est libre)."""
    if not is_perso():
        return items
    h = int(hashlib.md5((PROFILE["nom"] + key).encode()).hexdigest(), 16)
    k = h % len(items)
    return items[k:] + items[:k]

# ---------- Palette du template (l'eleve remplace l'accent par SA couleur) ----------
CREAM  = "#F6F3EC"   # fond clair editorial
INK    = "#17222F"   # texte principal (encre)
ACCENT = "#C4633C"   # accent terracotta : zone "ta couleur de marque ici"
MUTED  = "#6E7683"   # texte secondaire
ANNOT  = "#8B8578"   # annotations "a personnaliser" (gris chaud, pointilles)
CARD   = "#FFFFFF"   # cartes / encadres

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font_face(weight):
    data = b64(FONTS / f"montserrat-latin-{weight}-normal.woff2", "font/woff2")
    return (f"@font-face{{font-family:'Montserrat';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")
FONT_FACES = "".join(font_face(w) for w in (400,500,600,700,800,900))

COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
   -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
.slide{{width:1080px;height:1350px;background:{CREAM};position:relative;overflow:hidden;color:{INK};}}
.bg{{position:absolute;inset:0;background:
  radial-gradient(120% 70% at 90% -8%, rgba(196,99,60,0.09) 0%, rgba(246,243,236,0) 55%),
  radial-gradient(110% 70% at -10% 108%, rgba(23,34,47,0.06) 0%, rgba(246,243,236,0) 50%),
  {CREAM};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:8px;background:{ACCENT};z-index:5;}}
.pad{{position:absolute;inset:0;padding:64px 76px 150px;z-index:2;display:flex;flex-direction:column;}}

/* Bandeau haut : logo a remplacer + poignee du compte */
.brandrow{{display:flex;justify-content:space-between;align-items:center;margin-bottom:44px;}}
.logobox{{border:2.5px dashed {ANNOT};border-radius:12px;padding:16px 30px;color:{ANNOT};
  font-weight:700;font-size:21px;letter-spacing:2px;text-transform:uppercase;}}
.handle{{border:2.5px dashed {ANNOT};border-radius:40px;padding:12px 24px;color:{ANNOT};
  font-weight:600;font-size:20px;font-style:italic;}}

.eyebrow{{color:{ACCENT};font-weight:800;font-size:24px;letter-spacing:5px;text-transform:uppercase;margin-bottom:20px;}}
.title{{color:{INK};font-weight:900;font-size:58px;line-height:1.04;letter-spacing:-1.5px;text-transform:uppercase;}}
.title .acc{{color:{ACCENT};}}
.lede{{color:{MUTED};font-weight:500;font-size:26px;line-height:1.4;margin-top:22px;}}

.points{{display:flex;flex-direction:column;gap:24px;flex:1;justify-content:center;}}
.card{{background:{CARD};border-radius:16px;padding:26px 30px;box-shadow:none;border:1.5px solid rgba(23,34,47,0.08);}}
.card .cl{{color:{ACCENT};font-weight:800;font-size:29px;line-height:1.15;}}
.card .cl .n{{display:inline-block;min-width:44px;color:{INK};font-weight:900;}}
.card .ct{{color:{INK};font-weight:500;font-size:24px;line-height:1.35;margin-top:8px;opacity:0.9;}}
.card .ex{{color:{MUTED};font-weight:600;font-style:italic;font-size:21px;margin-top:8px;}}
.card .ex b{{color:{ANNOT};font-weight:800;font-style:normal;}}

/* Note "a personnaliser" : la consigne pour l'eleve, bien visible mais discrete */
.custom{{border:2.5px dashed {ANNOT};border-radius:14px;padding:18px 26px;margin-top:26px;
  color:{ANNOT};font-weight:600;font-size:21px;line-height:1.35;font-style:italic;}}
.custom b{{font-style:normal;font-weight:800;text-transform:uppercase;letter-spacing:1px;}}

/* Pied de page : contact a remplacer */
.footer{{position:absolute;bottom:44px;left:76px;right:76px;display:flex;justify-content:space-between;
  align-items:center;z-index:6;color:{ANNOT};font-weight:600;font-size:20px;font-style:italic;}}
.footer .pill{{border:2.5px dashed {ANNOT};border-radius:40px;padding:12px 26px;}}
"""

SIG_CSS = f"""
.sig{{background:{ACCENT};border-radius:14px;padding:18px 26px;margin-top:26px;text-align:center;
  color:#fff;font-weight:800;font-size:22px;letter-spacing:0.5px;}}
"""

def page(body):
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}{SIG_CSS}</style></head>'
            f'<body>{body}</body></html>')
    if is_perso():
        # 1) les notes "A personnaliser" deviennent la signature de la conciergerie
        sig = PROFILE.get("signature") or f'{PROFILE["nom"]} · {PROFILE["ville"]}'
        html = re.sub(r'<div class="custom"([^>]*)>.*?</div>',
                      lambda m: f'<div class="sig"{m.group(1)}>{sig}</div>', html, flags=re.S)
        # 2) les etiquettes "Exemple :" disparaissent (le contenu EST le sien)
        html = re.sub(r'<div class="ex"[^>]*>.*?</div>', '', html, flags=re.S)
        # 3) la couleur accent du template est remplacee par SA couleur de marque
        html = html.replace(ACCENT, PROFILE.get("couleur", ACCENT))
    return html

def slide_open():
    return '<div class="slide"><div class="bg"></div><div class="topbar"></div>'

def brandrow():
    if is_perso():
        return ('<div class="brandrow">'
                f'<div style="background:{ACCENT};color:#fff;font-weight:900;font-size:25px;'
                f'padding:14px 28px;border-radius:12px;letter-spacing:1px;text-transform:uppercase;">{PROFILE["nom"]}</div>'
                f'<div style="border:2.5px solid {ACCENT};color:{ACCENT};border-radius:40px;'
                f'padding:12px 24px;font-weight:700;font-size:20px;">{PROFILE["instagram"]}</div></div>')
    return ('<div class="brandrow"><div class="logobox">Ton logo ici</div>'
            '<div class="handle">@ta.conciergerie</div></div>')

def footer(left="Ta ville + ta zone", right="Ton site ou ton contact"):
    if is_perso():
        style = (f'border:2px solid rgba(23,34,47,0.18);border-radius:40px;padding:12px 26px;'
                 f'color:{INK};font-weight:700;font-style:normal;')
        return (f'<div class="footer"><div style="{style}">{PROFILE["ville"]}</div>'
                f'<div style="{style}">{PROFILE["contact"]}</div></div></div>')
    return (f'<div class="footer"><div class="pill">{left}</div>'
            f'<div class="pill">{right}</div></div></div>')

def acc(w):
    return f'<span class="acc">{w}</span>'

# =====================================================================
# VISUEL 1 : CONVERSION PROPRIETAIRE : pourquoi confier son bien
# =====================================================================
def visuel_01():
    cards = [
        ("1", "Vous récupérez votre temps",
         "Voyageurs, ménage, linge, imprévus : la conciergerie s'occupe de tout, du premier message au départ.", None),
        ("2", "Votre logement est entretenu",
         "Un passage professionnel après chaque séjour : votre bien reste impeccable, séjour après séjour.", None),
        ("3", "Vos revenus sont optimisés",
         "Prix ajustés selon la saison et la demande locale : votre bien travaille au bon tarif toute l'année.", None),
        ("4", "Des voyageurs vérifiés",
         "Profils contrôlés, règlement du logement, caution : votre bien est confié à de bonnes mains.", None),
    ]
    pts = ""
    for n, label, text, ex in cards:
        pts += (f'<div class="card"><div class="cl"><span class="n">{n}.</span>{label}</div>'
                f'<div class="ct">{text}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Propriétaires</div>'
        f'<div class="title">Pourquoi confier votre bien à une {acc("conciergerie")} ?</div>'
        f'<div class="points" style="margin-top:34px;">{pts}</div>'
        '<div class="custom"><b>À personnaliser :</b> remplace la couleur terracotta par TA couleur de marque, '
        'mets ton logo en haut et ta ville en bas. Le texte peut rester tel quel.</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUEL 2 : OFFRES / SERVICES (zones "Exemple :" a remplacer)
# =====================================================================
def visuel_02():
    cards = PROFILE.get("services") or [
        ("Annonce", "Création et optimisation de votre annonce",
         "Photos mises en valeur, titre travaillé, description qui donne envie de réserver."),
        ("Sejours", "Accueil des voyageurs et départs",
         "Arrivées autonomes ou en personne, état du logement vérifié à chaque départ."),
        ("Entretien", "Ménage professionnel et linge hôtelier",
         "Logement remis à neuf entre chaque séjour, linge blanc qualité hôtel."),
        ("Revenus", "Prix ajustés toute l'année",
         "Tarifs adaptés à la saison, aux événements et à la demande de votre secteur."),
    ]
    pts = ""
    for tag, label, text in cards:
        pts += (f'<div class="card"><div class="cl">{label}</div>'
                f'<div class="ct">{text}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Nos services</div>'
        f'<div class="title">On s\'occupe de {acc("tout")}, vous profitez des revenus</div>'
        f'<div class="points" style="margin-top:34px;">{pts}</div>'
        '<div class="custom"><b>À personnaliser :</b> ces 4 services sont des <b>exemples</b> : '
        'remplace-les par TES prestations réelles (garde 4 blocs maximum pour rester lisible).</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUEL 3 : ASTUCE AIRBNB (conseil a valeur, publiable tel quel)
# =====================================================================
def visuel_03():
    cards = [
        ("1", "Ouvrez tout, lumière naturelle",
         "Rideaux ouverts, lumières allumées : shootez en fin de matinée, jamais au flash."),
        ("2", "Appareil à hauteur de hanche",
         "Pliez les genoux, tenez le téléphone droit à 1,20 m du sol : les pièces paraissent plus grandes."),
        ("3", "Shootez depuis un angle",
         "Placez-vous dans un coin de la pièce pour donner de la profondeur, pas face au mur."),
        ("4", "Zéro objet personnel",
         "Câbles, produits, chaussures : tout disparaît. Linge blanc tiré, serviettes pliées."),
        ("5", "La couverture, c'est la meilleure pièce",
         "Votre photo principale doit être la pièce la plus séduisante, pas la façade."),
    ]
    pts = ""
    for n, label, text in cards:
        pts += (f'<div class="card" style="padding:20px 28px;"><div class="cl" style="font-size:27px;">'
                f'<span class="n">{n}.</span>{label}</div>'
                f'<div class="ct" style="font-size:23px;">{text}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Astuce propriétaire</div>'
        f'<div class="title">Des photos qui font {acc("réserver")} votre bien</div>'
        f'<div class="points" style="margin-top:26px;gap:16px;">{pts}</div>'
        '<div class="custom" style="margin-top:18px;padding:14px 24px;"><b>À personnaliser :</b> ce conseil se poste tel quel. '
        'Ajoute juste tes couleurs, ton logo et signe avec le nom de ta conciergerie.</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUEL 4 : NOTRE HISTOIRE (texte "Exemple :" a remplacer par la sienne)
# =====================================================================
def visuel_04():
    paras = PROFILE.get("histoire") or [
        "Tout est parti d'un constat simple : autour de moi, des propriétaires laissaient "
        "leur logement vide une partie de l'année, faute de temps pour s'en occuper.",
        "J'ai commencé avec un seul logement, celui d'un proche. Annonce refaite, accueil "
        "soigné, ménage impeccable : les réservations ont suivi, et les avis 5 étoiles aussi.",
        "Aujourd'hui, j'accompagne des propriétaires qui veulent que leur bien rapporte, "
        "sans y consacrer leurs soirées ni leurs week-ends.",
    ]
    cards = ""
    for i, p in enumerate(paras):
        ex = '<div class="ex" style="margin-top:0;"><b>Exemple :</b></div>' if i == 0 else ''
        mt = 'margin-top:12px;' if i == 0 else ''
        cards += (f'<div class="card">{ex}'
                  f'<div class="ct" style="font-size:26px;line-height:1.5;{mt}">{p}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Notre histoire</div>'
        f'<div class="title">Pourquoi j\'ai créé ma {acc("conciergerie")}</div>'
        f'<div class="points" style="margin-top:36px;justify-content:center;gap:30px;">{cards}</div>'
        '<div class="custom"><b>À personnaliser :</b> remplace ce récit par TON histoire : '
        'ton déclic, ta ville, ton premier logement, ce qui te rend fier aujourd\'hui.</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUELS 5 a 8 : posts conseils bases sur la banque YouTube
# (sources/youtube/BANQUE_CONSEILS.md, videos business Airbnb de Sebastien)
# =====================================================================

def conseil_slide(eyebrow, title_html, cards, note, numbered=True, ct_size=23, cl_size=27):
    pts = ""
    for i, (label, text) in enumerate(cards, 1):
        num = f'<span class="n">{i}.</span>' if numbered else ''
        pts += (f'<div class="card" style="padding:20px 28px;">'
                f'<div class="cl" style="font-size:{cl_size}px;">{num}{label}</div>'
                f'<div class="ct" style="font-size:{ct_size}px;">{text}</div></div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        f'<div class="eyebrow">{eyebrow}</div>'
        f'<div class="title">{title_html}</div>'
        f'<div class="points" style="margin-top:26px;gap:16px;">{pts}</div>'
        f'<div class="custom" style="margin-top:18px;padding:14px 24px;">{note}</div>'
        '</div>' + footer())

NOTE_TEL_QUEL = ('<b>À personnaliser :</b> ce conseil se poste tel quel. '
                 'Ajoute juste tes couleurs, ton logo et signe avec le nom de ta conciergerie.')

# VISUEL 5 (post 18) : le titre d'annonce
def visuel_05():
    return conseil_slide(
        "Astuce propriétaire",
        f'Le titre d\'annonce qui arrête le {acc("scroll")}',
        [
            ("La formule qui marche",
             "Capacité + équipement star + localisation. Exemple : 6 personnes, jacuzzi, 5 min à pied de la plage."),
            ("50 caractères maximum",
             "Un titre est une publicité, pas un inventaire de votre logement."),
            ("Zéro bourrage de mots-clés",
             "Wifi, parking, Netflix, clim : ça marchait en 2020. Aujourd'hui, ça fait annonce au rabais."),
            ("Un nom mémorable",
             "L'Atelier du Confluent bat T2 centre-ville wifi : on s'en souvient et on le recherche."),
            ("Les 3 premières lignes comptent",
             "Avant le bouton lire la suite : capacité, atout numéro 1, localisation. Le reste vient après."),
        ],
        NOTE_TEL_QUEL)

# VISUEL 6 (post 19) : l'algorithme Airbnb
def visuel_06():
    return conseil_slide(
        "Comprendre Airbnb",
        f'Ce que l\'algorithme Airbnb regarde {acc("vraiment")}',
        [
            ("Le taux de conversion d'abord",
             "Airbnb pousse les annonces qui transforment les vues en réservations, pas les moins chères."),
            ("Répondre en moins d'une heure",
             "Les meilleurs hôtes répondent en 30 minutes. Au-delà de 24 heures, l'annonce recule."),
            ("Le badge Guest Favorite",
             "Note 4,9 et plus, avis excellents et réguliers : c'est le nouveau graal, devant le statut Superhost."),
            ("La réservation instantanée",
             "Activée avec le filtre voyageurs vérifiés : plus de visibilité, sans mauvaises surprises."),
            ("Une annonce vivante",
             "Photo ajoutée, description mise à jour, calendrier frais : autant de signaux positifs envoyés."),
        ],
        NOTE_TEL_QUEL)

# VISUEL 7 (post 20) : les prix
def visuel_07():
    return conseil_slide(
        "Astuce revenus",
        f'Un prix fixe toute l\'année vous fait {acc("perdre")} de l\'argent',
        [
            ("Le tarif par voyageur",
             "95 euros pour 2 personnes puis 12 euros par voyageur en plus : vous apparaissez à 95 euros dans les recherches, sans rien perdre."),
            ("Le tarif non remboursable à -10%",
             "9 hôtes sur 10 l'ignorent : votre annonce s'affiche moins chère et ces réservations sont en béton."),
            ("Les mini-saisons",
             "Salons, vacances scolaires, week-ends fériés : chaque événement local a son prix, comme à l'hôtel."),
            ("La basse saison se joue tôt",
             "La fenêtre de réservation se ferme 30 à 45 jours avant. Ajuster la semaine d'avant, c'est trop tard."),
        ],
        NOTE_TEL_QUEL, ct_size=24)

# VISUEL 8 (post 25) : les 3 chiffres a surveiller
def visuel_08():
    return conseil_slide(
        "Suivi de votre annonce",
        f'Les 3 chiffres qui disent si votre annonce va {acc("bien")}',
        [
            ("Le taux d'impression",
             "Au-dessus de 55 : bonne visibilité. Sous 35 : votre annonce est quasi invisible dans les recherches."),
            ("Le taux de clic",
             "Plus de 30% : excellent. Sous 15% : c'est la photo principale ou le titre qu'il faut revoir."),
            ("Le taux de conversion",
             "Plus de 5% : excellent. Sous 2% : alerte rouge, l'annonce ne transforme pas ses visites."),
            ("La lecture croisée",
             "Des vues sans clics : photo ou prix. Des clics sans réservation : description, conditions ou avis."),
        ],
        '<b>À personnaliser :</b> ce conseil se poste tel quel (chiffres visibles dans les '
        'statistiques Airbnb, profil professionnel activé). Ajoute tes couleurs et ton logo.',
        ct_size=24)

# =====================================================================
# VISUELS 9 a 11 : templates RICHES EN ZONES A MODIFIER (demande Martin) :
# temoignage, chiffres cles, lieux d'intervention. Chaque zone pointillee
# est un rectangle propre, facile a recouvrir dans Canva avec son logo,
# sa photo ou son texte.
# =====================================================================

# VISUEL 9 : TEMOIGNAGE PROPRIETAIRE (avis + prenom + photo a remplacer)
def visuel_09():
    quote = (f'<div class="card" style="padding:40px 44px;position:relative;">'
             f'<div style="color:{ACCENT};font-weight:900;font-size:110px;line-height:0.5;margin-bottom:26px;">»</div>'
             f'<div class="ex" style="margin-top:0;"><b>Exemple :</b></div>'
             f'<div style="color:{INK};font-weight:600;font-style:italic;font-size:29px;line-height:1.5;margin-top:12px;">'
             f'Depuis que j\'ai confié mon appartement, je ne m\'occupe plus de rien : '
             f'je reçois mes revenus, les avis 5 étoiles, et je dors tranquille. '
             f'J\'aurais dû le faire deux ans plus tôt.</div></div>')
    author = ('<div style="display:flex;align-items:center;gap:24px;margin-top:30px;">'
              f'<div style="width:120px;height:120px;border:2.5px dashed {ANNOT};border-radius:50%;'
              f'display:flex;align-items:center;justify-content:center;text-align:center;color:{ANNOT};'
              f'font-weight:700;font-size:16px;line-height:1.2;flex-shrink:0;">Sa photo<br>(option)</div>'
              f'<div><div style="border:2.5px dashed {ANNOT};border-radius:40px;padding:12px 26px;color:{ANNOT};'
              f'font-weight:700;font-size:22px;font-style:italic;display:inline-block;">Prénom du propriétaire</div>'
              f'<div style="color:{MUTED};font-weight:600;font-size:20px;margin-top:10px;">'
              f'propriétaire à <span style="border:2px dashed {ANNOT};border-radius:8px;padding:2px 10px;'
              f'color:{ANNOT};font-style:italic;">ta ville</span> depuis '
              f'<span style="border:2px dashed {ANNOT};border-radius:8px;padding:2px 10px;color:{ANNOT};'
              f'font-style:italic;">X années</span></div></div></div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Ils nous font confiance</div>'
        f'<div class="title" style="font-size:50px;">Ce que disent les {acc("propriétaires")}</div>'
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">{quote}{author}</div>'
        '<div class="custom"><b>À personnaliser :</b> colle un VRAI avis d\'un de tes propriétaires '
        '(ou voyageurs), son prénom, ta ville, l\'ancienneté. Photo optionnelle.</div>'
        '</div>' + footer())

# VISUEL 10 : CHIFFRES CLES + SLOGAN (stats et slogan a remplacer)
def visuel_10():
    def stat(num, label):
        return (f'<div style="flex:1;background:{CARD};border:2.5px dashed {ANNOT};border-radius:16px;'
                f'padding:30px 20px;text-align:center;">'
                f'<div style="color:{ACCENT};font-weight:900;font-size:64px;line-height:1;">{num}</div>'
                f'<div style="color:{INK};font-weight:600;font-size:21px;line-height:1.25;margin-top:12px;">{label}</div></div>')
    stats = ('<div style="display:flex;gap:18px;">'
             + stat("12", "logements accompagnés") + stat("4,9", "de note moyenne")
             + stat("98%", "de calendriers remplis l'été") + '</div>')
    slogan = (f'<div style="border:2.5px dashed {ANNOT};border-radius:40px;padding:20px 34px;margin-top:30px;'
              f'text-align:center;color:{ANNOT};font-weight:700;font-size:24px;font-style:italic;">'
              f'Ton slogan ici. Exemple : votre bien entre de bonnes mains, vos revenus au sommet</div>')
    ex = (f'<div class="ex" style="margin-top:26px;text-align:center;"><b>Exemple :</b> '
          f'remplace chaque chiffre par les tiens (vrais chiffres uniquement)</div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">En quelques chiffres</div>'
        f'<div class="title" style="font-size:50px;">Notre conciergerie en {acc("chiffres")}</div>'
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">{stats}{ex}{slogan}</div>'
        '<div class="custom"><b>À personnaliser :</b> tes 3 chiffres (logements, note, remplissage, '
        'années...), ton slogan, tes couleurs, ton logo. Reste honnête : ce sont TES vrais chiffres.</div>'
        '</div>' + footer())

# VISUEL 11 : LIEUX D'INTERVENTION (villes + photo de la region a remplacer)
def visuel_11():
    pin = (f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;">'
           f'<path d="M12 21s-7-6.1-7-11a7 7 0 1 1 14 0c0 4.9-7 11-7 11z" stroke="{ACCENT}" stroke-width="2" '
           f'stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6" stroke="{ACCENT}" stroke-width="2"/></svg>')
    def place(txt, main=False):
        w = 800 if main else 700
        return (f'<div style="display:flex;align-items:center;gap:16px;border:2.5px dashed {ANNOT};'
                f'border-radius:40px;padding:{"18px 30px" if main else "14px 26px"};margin-top:16px;'
                f'max-width:{w}px;">{pin}'
                f'<div style="color:{ANNOT};font-weight:{800 if main else 600};font-size:{25 if main else 22}px;'
                f'font-style:italic;">{txt}</div></div>')
    places = (place("Ta ville principale (exemple : Annecy)", main=True)
              + place("Commune voisine 1 (exemple : Sévrier)")
              + place("Commune voisine 2 (exemple : Talloires)")
              + place("Et jusqu'à... (exemple : 30 min autour du lac)"))
    photo = (f'<div style="border:2.5px dashed {ANNOT};border-radius:16px;height:250px;margin-top:28px;'
             f'display:flex;align-items:center;justify-content:center;text-align:center;color:{ANNOT};'
             f'font-weight:700;font-size:23px;font-style:italic;line-height:1.4;">'
             f'Ta photo ici : ta région, ta ville,<br>un de tes logements (paysage)</div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Zone d\'intervention</div>'
        f'<div class="title" style="font-size:50px;">Là où nous prenons soin de votre {acc("bien")}</div>'
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">{places}{photo}</div>'
        '<div class="custom"><b>À personnaliser :</b> tes villes et ton rayon d\'action, une belle photo '
        'de ta région, tes couleurs, ton logo. Les propriétaires doivent se dire : c\'est chez moi.</div>'
        '</div>' + footer())

# =====================================================================
# VARIANTES GRAPHIQUES (demande Martin) : memes conseils, mises en page
# differentes : carte mentale, entonnoir, avant/apres, schema annote.
# Sorties dans output/pack_variantes/.
# =====================================================================
REDL   = "#B94A44"   # rouge sombre lisible sur fond clair
GREENL = "#2F7D57"   # vert sombre lisible sur fond clair

def head_block(eyebrow, title_html, tsize=46):
    return (f'<div class="eyebrow">{eyebrow}</div>'
            f'<div class="title" style="font-size:{tsize}px;">{title_html}</div>')

# ---- VARIANTE A (post 19) : CARTE MENTALE de l'algorithme ----
def variante_mindmap():
    C = (464, 300)   # centre du noeud dans le conteneur 928x660
    spots = [
        (135, 75,  "Conversion", "Des vues qui deviennent des réservations", 0, 0),
        (793, 75,  "Réponse rapide", "Moins d'1 heure, les meilleurs font 30 min", 658, 0),
        (135, 545, "Guest Favorite", "Note 4,9 et avis excellents réguliers", 0, 480),
        (464, 545, "Résa instantanée", "Avec le filtre voyageurs vérifiés", 329, 480),
        (793, 545, "Annonce vivante", "Photos et calendrier mis à jour", 658, 480),
    ]
    lines = "".join(
        f'<line x1="{C[0]}" y1="{C[1]}" x2="{x}" y2="{y}" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" opacity="0.55"/>'
        for x, y, *_ in spots)
    boxes = "".join(
        f'<div style="position:absolute;left:{bx}px;top:{by}px;width:270px;background:{CARD};'
        f'border:1.5px solid rgba(23,34,47,0.10);border-radius:14px;padding:16px 18px;z-index:2;">'
        f'<div style="color:{ACCENT};font-weight:800;font-size:22px;">{label}</div>'
        f'<div style="color:{INK};font-weight:500;font-size:19px;line-height:1.3;margin-top:6px;opacity:0.9;">{txt}</div></div>'
        for x, y, label, txt, bx, by in spots)
    node = (f'<div style="position:absolute;left:354px;top:190px;width:220px;height:220px;'
            f'background:{ACCENT};border-radius:50%;display:flex;align-items:center;justify-content:center;'
            f'text-align:center;z-index:2;">'
            f'<div style="color:#fff;font-weight:900;font-size:27px;line-height:1.15;text-transform:uppercase;">Votre<br>annonce</div></div>')
    schema = (f'<div style="flex:1;display:flex;align-items:center;">'
              f'<div style="position:relative;width:928px;height:660px;">'
              f'<svg width="928" height="660" style="position:absolute;inset:0;z-index:1;">{lines}</svg>'
              f'{node}{boxes}</div></div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        head_block("Comprendre Airbnb", f'L\'algorithme Airbnb en une {acc("carte")}') +
        schema +
        '<div class="custom" style="margin-top:auto;padding:14px 24px;">'
        '<b>À personnaliser :</b> ce schéma se poste tel quel. Tes couleurs, ton logo, et signe '
        'avec le nom de ta conciergerie.</div>'
        '</div>' + footer())

# ---- VARIANTE B (post 25) : ENTONNOIR du scroll a la reservation ----
def variante_funnel():
    bars = [
        ("1. VU", "taux d'impression", "55+", "#17222F", 928),
        ("2. CLIQUÉ", "taux de clic", "30%", "#4E5D6E", 686),
        ("3. RÉSERVÉ", "taux de conversion", "5%", ACCENT, 464),
    ]
    rows = ""
    for i, (stage, metric, goal, bg, w) in enumerate(bars):
        rows += (f'<div style="width:{w}px;margin:0 auto;background:{bg};border-radius:16px;'
                 f'padding:24px 34px;display:flex;justify-content:space-between;align-items:center;">'
                 f'<div><div style="color:#fff;font-weight:900;font-size:28px;text-transform:uppercase;">{stage}</div>'
                 f'<div style="color:rgba(255,255,255,0.75);font-weight:600;font-size:20px;">{metric}</div></div>'
                 f'<div style="text-align:right;"><div style="color:#fff;font-weight:900;font-size:42px;">{goal}</div>'
                 f'<div style="color:rgba(255,255,255,0.75);font-weight:600;font-size:17px;text-transform:uppercase;letter-spacing:1px;">objectif</div></div></div>')
        if i < 2:
            rows += f'<div style="text-align:center;color:{ACCENT};font-weight:900;font-size:30px;line-height:1;margin:12px 0;">▼</div>'
    diag = ('<div style="display:flex;gap:16px;margin-top:30px;">'
            f'<div style="flex:1;background:{CARD};border:1.5px solid rgba(23,34,47,0.10);border-radius:14px;padding:18px 22px;">'
            f'<div style="color:{REDL};font-weight:800;font-size:21px;">Des vues, pas de clics ?</div>'
            f'<div style="color:{INK};font-weight:500;font-size:20px;margin-top:6px;">Photo principale ou prix à revoir.</div></div>'
            f'<div style="flex:1;background:{CARD};border:1.5px solid rgba(23,34,47,0.10);border-radius:14px;padding:18px 22px;">'
            f'<div style="color:{REDL};font-weight:800;font-size:21px;">Des clics, pas de résa ?</div>'
            f'<div style="color:{INK};font-weight:500;font-size:20px;margin-top:6px;">Description, conditions ou avis.</div></div></div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        head_block("Suivi de votre annonce", f'Du scroll à la {acc("réservation")} : l\'entonnoir Airbnb') +
        f'<div style="margin-top:34px;">{rows}</div>' + diag +
        '<div class="custom" style="margin-top:auto;padding:14px 24px;">'
        '<b>À personnaliser :</b> chiffres visibles dans les statistiques Airbnb (profil '
        'professionnel activé). Ajoute tes couleurs et ton logo, puis poste tel quel.</div>'
        '</div>' + footer())

# ---- VARIANTE C (post 20) : AVANT / APRES sur les prix ----
def variante_avant_apres():
    def col(color, bg, title_txt, glyph, items):
        lis = "".join(
            f'<div style="display:flex;gap:14px;margin-top:22px;align-items:flex-start;">'
            f'<div style="color:{color};font-weight:900;font-size:24px;line-height:1.2;flex-shrink:0;">{glyph}</div>'
            f'<div style="color:{INK};font-weight:500;font-size:24px;line-height:1.35;">{t}</div></div>'
            for t in items)
        return (f'<div style="flex:1;border:2px solid {color};border-radius:16px;padding:24px 24px;background:{bg};">'
                f'<div style="color:{color};font-weight:900;font-size:25px;text-transform:uppercase;letter-spacing:1px;">{title_txt}</div>{lis}</div>')
    avant = col(REDL, "rgba(185,74,68,0.07)", "Prix fixe", "×", [
        "120 euros, toute l'année, pour tout le monde",
        "Invisible dans les recherches 2 voyageurs",
        "Basse saison ajustée au dernier moment",
        "Calendrier troué, revenus en dents de scie",
    ])
    apres = col(GREENL, "rgba(47,125,87,0.07)", "Prix piloté", "✓", [
        "95 euros pour 2, puis 12 euros par voyageur",
        "Tarif non remboursable affiché à -10%",
        "Mini-saisons : salons, vacances, fériés",
        "Prix calés 30 à 45 jours avant la basse saison",
    ])
    arrow = f'<div style="align-self:center;color:{ACCENT};font-weight:900;font-size:52px;padding:0 4px;">→</div>'
    strip = (f'<div style="background:{CARD};border:1.5px solid rgba(23,34,47,0.10);border-radius:14px;'
             f'padding:24px 30px;margin-top:30px;text-align:center;">'
             f'<div style="color:{INK};font-weight:700;font-size:25px;line-height:1.4;">Même logement, même confort : '
             f'seule la façon d\'afficher le prix change. <span style="color:{ACCENT};">Et le classement suit.</span></div></div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        head_block("Astuce revenus", f'Prix fixe ou prix {acc("piloté")} : le match') +
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">'
        f'<div style="display:flex;gap:12px;align-items:stretch;">{avant}{arrow}{apres}</div>' +
        strip + '</div>' +
        '<div class="custom" style="margin-top:auto;padding:14px 24px;">'
        '<b>À personnaliser :</b> adapte les montants d\'exemple à ton marché, mets tes couleurs '
        'et ton logo. Le reste se poste tel quel.</div>'
        '</div>' + footer())

# ---- VARIANTE D (post 18) : ANATOMIE d'un titre d'annonce ----
def variante_anatomie():
    good = (f'<div style="background:{CARD};border:1.5px solid rgba(23,34,47,0.10);border-radius:16px;padding:34px 34px;">'
            f'<div style="color:{MUTED};font-weight:700;font-size:19px;text-transform:uppercase;letter-spacing:2px;">Le bon titre</div>'
            f'<div style="font-weight:800;font-size:36px;line-height:1.6;color:{INK};margin-top:16px;">'
            f'<span style="border-bottom:7px solid {ACCENT};">6 personnes</span> · '
            f'<span style="border-bottom:7px solid {GREENL};">jacuzzi</span> · '
            f'<span style="border-bottom:7px solid {REDL};">5 min à pied de la plage</span></div>'
            f'<div style="display:flex;gap:12px;margin-top:22px;flex-wrap:wrap;">'
            f'<div style="background:{ACCENT};color:#fff;font-weight:800;font-size:18px;padding:8px 16px;border-radius:30px;text-transform:uppercase;letter-spacing:1px;">Capacité</div>'
            f'<div style="background:{GREENL};color:#fff;font-weight:800;font-size:18px;padding:8px 16px;border-radius:30px;text-transform:uppercase;letter-spacing:1px;">Équipement star</div>'
            f'<div style="background:{REDL};color:#fff;font-weight:800;font-size:18px;padding:8px 16px;border-radius:30px;text-transform:uppercase;letter-spacing:1px;">Localisation</div>'
            f'</div></div>')
    bad = (f'<div style="background:rgba(185,74,68,0.07);border:2px solid {REDL};border-radius:16px;padding:28px 34px;margin-top:26px;">'
           f'<div style="color:{REDL};font-weight:900;font-size:19px;text-transform:uppercase;letter-spacing:2px;">× Le titre inventaire</div>'
           f'<div style="color:{INK};font-weight:600;font-size:27px;margin-top:10px;text-decoration:line-through;opacity:0.65;">'
           f'Joli T2 cosy wifi parking Netflix clim balcon</div>'
           f'<div style="color:{REDL};font-weight:600;font-size:20px;margin-top:10px;font-style:italic;">'
           f'Le bourrage de mots-clés de 2020 : aujourd\'hui, ça fait annonce au rabais.</div></div>')
    rules = ('<div style="display:flex;gap:16px;margin-top:26px;">'
             f'<div style="flex:1;border:2px solid {ACCENT};border-radius:40px;padding:16px 22px;text-align:center;'
             f'color:{ACCENT};font-weight:800;font-size:21px;">50 caractères maximum</div>'
             f'<div style="flex:1;border:2px solid {ACCENT};border-radius:40px;padding:14px 22px;text-align:center;'
             f'color:{ACCENT};font-weight:800;font-size:21px;">Un titre = une promesse</div></div>')
    return page(slide_open() +
        '<div class="pad">' + brandrow() +
        head_block("Astuce propriétaire", f'L\'anatomie d\'un titre qui fait {acc("cliquer")}') +
        f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">{good}{bad}{rules}</div>' +
        '<div class="custom" style="margin-top:auto;padding:14px 24px;">'
        '<b>À personnaliser :</b> remplace l\'exemple par le titre de TON annonce en gardant la '
        'formule capacité + équipement star + localisation. Tes couleurs, ton logo.</div>'
        '</div>' + footer())

# =====================================================================
GROUPS = {
    "pack_demo": [visuel_01, visuel_02, visuel_03, visuel_04,
                  visuel_05, visuel_06, visuel_07, visuel_08,
                  visuel_09, visuel_10, visuel_11],
    "pack_variantes": [variante_mindmap, variante_funnel,
                       variante_avant_apres, variante_anatomie],
}

def check_no_forbidden(html, name):
    # mot "gestion" interdit (et derives), tirets longs interdits, emojis interdits.
    # Glyphes sobres autorises par la charte (colorises en CSS) : ✓ × ▼ ▲ → ↓ ★ ·
    text = re.sub(r'data:[^"\']+', '', html)
    text = re.sub(r'[✓×▼▲→↓★·»]', '', text)
    for pat, label in [(r'(?i)gestion', 'mot "gestion"'),
                       (r'[‒–—―─﹣－]', 'tiret long'),
                       (r'[\U0001F000-\U0001FAFF☀-➿]', 'emoji')]:
        m = re.search(pat, text)
        assert not m, f"{name} : {label} detecte ({m.group(0)!r})"

def write_group(slug, builders):
    out = ROOT / "output" / slug / "html"
    out.mkdir(parents=True, exist_ok=True)
    for i, build in enumerate(builders, 1):
        html = build()
        name = f"slide_{i:02d}.html"
        check_no_forbidden(html, f"{slug}/{name}")
        (out / name).write_text(html, encoding="utf-8")
        print(f"OK {slug}/{name}")
    print(f"HTML dans {out}")

def main():
    if len(sys.argv) > 1:
        # usage : python3 build_pack_conciergerie.py profiles/eleve.json
        # -> genere le pack PERSONNALISE de l'eleve (toutes les mises en page)
        load_profile(ROOT / sys.argv[1] if not pathlib.Path(sys.argv[1]).is_absolute() else sys.argv[1])
        slug = PROFILE.get("slug") or "pack_perso"
        write_group(slug, GROUPS["pack_demo"] + GROUPS["pack_variantes"])
    else:
        for slug, builders in GROUPS.items():
            write_group(slug, builders)

if __name__ == "__main__":
    main()
