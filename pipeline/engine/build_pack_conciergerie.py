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
# =====================================================================
# PACK COMPLET : les 19 visuels restants du plan (PACK_CONCIERGERIE_30_POSTS.md)
# Chaque visuel a une STRUCTURE differente + des zones a modifier.
# =====================================================================

def wrap_center(inner):
    return f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">{inner}</div>'

def custom_note(txt):
    return f'<div class="custom" style="margin-top:auto;padding:14px 24px;"><b>À personnaliser :</b> {txt}</div>'

def base(eyebrow, title_html, inner, note, tsize=48):
    return page(slide_open() + '<div class="pad">' + brandrow() +
        head_block(eyebrow, title_html, tsize) + wrap_center(inner) +
        custom_note(note) + '</div>' + footer())

def dz(txt, extra=""):
    """Zone pointillee a remplacer (dashed zone)."""
    return (f'<div style="border:2.5px dashed {ANNOT};border-radius:12px;padding:10px 18px;'
            f'color:{ANNOT};font-weight:600;font-size:20px;font-style:italic;display:inline-block;{extra}">{txt}</div>')

# ---- P02 : QUI S'OCCUPE DE VOTRE BIEN (portrait + parcours) ----
def p02_equipe():
    photo = (f'<div style="width:360px;height:440px;border:2.5px dashed {ANNOT};border-radius:20px;'
             f'display:flex;align-items:center;justify-content:center;text-align:center;color:{ANNOT};'
             f'font-weight:700;font-size:22px;font-style:italic;line-height:1.4;flex-shrink:0;">'
             f'Ta photo ici<br>(toi ou ton équipe,<br>souriants, en situation)</div>')
    pts = "".join(f'<div style="display:flex;gap:12px;margin-top:18px;align-items:flex-start;">'
                  f'<div style="color:{ACCENT};font-weight:900;font-size:24px;">→</div>'
                  f'<div style="color:{INK};font-weight:600;font-size:23px;line-height:1.3;">{t}</div></div>'
                  for t in ["Joignable 7 jours sur 7 pendant les séjours",
                            "Sur place : on connaît chaque rue du secteur",
                            "Une obsession : les avis 5 étoiles de vos voyageurs"])
    right = (f'<div style="flex:1;">{dz("Ton prénom + ton rôle. Exemple : Julie, fondatrice")}'
             f'<div style="margin-top:16px;">{dz("Une phrase sur ton parcours. Exemple : 8 ans dans l&#39;hôtellerie avant de créer ma conciergerie", "font-size:19px;")}</div>'
             f'{pts}</div>')
    inner = f'<div style="display:flex;gap:36px;align-items:center;">{photo}{right}</div>'
    return base("Qui sommes-nous", f'La personne qui veille sur votre {acc("bien")}', inner,
        "ta photo, ton prénom, ton parcours en une phrase. Les 3 points peuvent rester.")

# ---- P03 : NOS VALEURS (3 colonnes + pictos SVG) ----
def p03_valeurs():
    ic = {
      "oeil": f'<svg width="54" height="54" viewBox="0 0 24 24" fill="none"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="12" r="3" stroke="{ACCENT}" stroke-width="1.8"/></svg>',
      "etoile": f'<svg width="54" height="54" viewBox="0 0 24 24" fill="none"><path d="M12 3l2.7 5.6 6.1.8-4.5 4.2 1.1 6-5.4-3-5.4 3 1.1-6L3.2 9.4l6.1-.8L12 3z" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"/></svg>',
      "maison": f'<svg width="54" height="54" viewBox="0 0 24 24" fill="none"><path d="M3 11l9-7 9 7" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 10v10h14V10" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    }
    vals = [(ic["oeil"], "Transparence", "Vous savez tout, tout le temps : séjours, revenus, état du logement."),
            (ic["etoile"], "Exigence", "Une qualité hôtelière à chaque séjour, sans exception."),
            (ic["maison"], "Proximité", "Une personne du coin qui décroche, pas une plateforme anonyme.")]
    cols = "".join(f'<div style="flex:1;background:{CARD};border:1.5px solid rgba(23,34,47,0.08);'
                   f'border-radius:18px;padding:34px 26px;text-align:center;">{svg}'
                   f'<div style="color:{ACCENT};font-weight:900;font-size:27px;text-transform:uppercase;margin-top:18px;">{v}</div>'
                   f'<div style="color:{INK};font-weight:500;font-size:21px;line-height:1.4;margin-top:14px;">{t}</div></div>'
                   for svg, v, t in vals)
    inner = (f'<div style="display:flex;gap:20px;align-items:stretch;">{cols}</div>'
             f'<div style="margin-top:28px;text-align:center;">{dz("Ta promesse en une phrase. Exemple : votre bien traité comme si c&#39;était le nôtre")}</div>')
    return base("Nos valeurs", f'Ce qu\'on {acc("promet")} à chaque propriétaire', inner,
        "garde ou remplace ces 3 valeurs par les TIENNES, et écris ta promesse en bas.")

# ---- P04 : UNE JOURNEE TYPE (timeline verticale) ----
def p04_journee():
    steps = [("9h", "Contrôle après le départ", "État du logement vérifié pièce par pièce"),
             ("11h", "Ménage et linge hôtelier", "Le logement redevient impeccable"),
             ("15h", "Annonce et prix à jour", "Calendrier, tarifs, photos : rien ne dort"),
             ("18h", "Accueil des nouveaux voyageurs", "Arrivée fluide, consignes claires"),
             ("21h", "Réponses aux messages", "Moins d'une heure, même le soir")]
    rows = ""
    for i, (h, t, d) in enumerate(steps):
        rows += (f'<div style="display:flex;gap:24px;align-items:flex-start;position:relative;padding-bottom:{26 if i<4 else 0}px;">'
                 f'<div style="width:86px;flex-shrink:0;text-align:right;color:{ACCENT};font-weight:900;font-size:28px;">{h}</div>'
                 f'<div style="width:14px;height:14px;border-radius:50%;background:{ACCENT};margin-top:10px;flex-shrink:0;"></div>'
                 f'<div><div style="color:{INK};font-weight:800;font-size:25px;">{t}</div>'
                 f'<div style="color:{MUTED};font-weight:500;font-size:20px;margin-top:4px;">{d}</div></div></div>')
    inner = (f'<div style="position:relative;padding-left:6px;">'
             f'<div style="position:absolute;left:132px;top:14px;bottom:14px;width:3px;background:{ACCENT};opacity:0.3;"></div>{rows}</div>')
    return base("Les coulisses", f'Une journée au service de votre {acc("bien")}', inner,
        "adapte les horaires et les étapes à TA vraie journée : c'est ça qui rassure.")

# ---- P06 : ZOOM ANNONCE (checklist coches vertes) ----
def p06_annonce():
    items = ["Photos retravaillées, ou refaites par un pro",
             "Titre construit avec la formule qui fait cliquer",
             "Description qui répond aux questions des voyageurs",
             "Équipements TOUS déclarés : chaque case est un filtre",
             "Calendrier et prix tenus à jour chaque semaine"]
    rows = "".join(f'<div style="display:flex;gap:18px;align-items:flex-start;background:{CARD};'
                   f'border:1.5px solid rgba(23,34,47,0.08);border-radius:14px;padding:20px 26px;margin-top:16px;">'
                   f'<div style="color:{GREENL};font-weight:900;font-size:30px;line-height:1;">✓</div>'
                   f'<div style="color:{INK};font-weight:600;font-size:24px;line-height:1.3;">{t}</div></div>'
                   for t in items)
    strip = (f'<div style="background:{ACCENT};border-radius:14px;padding:18px 26px;margin-top:24px;text-align:center;'
             f'color:#fff;font-weight:800;font-size:23px;">Résultat : plus de vues, plus de clics, plus de réservations.</div>')
    return base("Zoom service", f'Votre annonce, prise en main de {acc("A à Z")}', inner=rows+strip,
        note="ajuste la liste à ce que TU fais vraiment sur les annonces. Tes couleurs, ton logo.")

# ---- P07 : ZOOM ACCUEIL (2 colonnes arrivee / depart) ----
def p07_accueil():
    def col(title_txt, items):
        lis = "".join(f'<div style="display:flex;gap:12px;margin-top:18px;align-items:flex-start;">'
                      f'<div style="color:{ACCENT};font-weight:900;font-size:22px;">→</div>'
                      f'<div style="color:{INK};font-weight:500;font-size:22px;line-height:1.35;">{t}</div></div>' for t in items)
        return (f'<div style="flex:1;background:{CARD};border:1.5px solid rgba(23,34,47,0.08);border-radius:18px;padding:30px 28px;">'
                f'<div style="color:{ACCENT};font-weight:900;font-size:26px;text-transform:uppercase;letter-spacing:1px;">{title_txt}</div>{lis}</div>')
    inner = ('<div style="display:flex;gap:20px;align-items:stretch;">'
             + col("À l'arrivée", ["Toutes les infos envoyées la veille : code, parking, wifi",
                                   "Check-in autonome ou accueil en personne, au choix",
                                   "Logement vérifié et à température avant chaque entrée"])
             + col("Au départ", ["État du logement contrôlé dans la journée",
                                 "Ménage et linge lancés aussitôt",
                                 "L'avis du voyageur sollicité au bon moment"]) + '</div>')
    return base("Zoom service", f'Des séjours {acc("fluides")}, de l\'arrivée au départ', inner,
        "arrivée autonome, en personne, les deux ? Adapte les points à TON accueil.")

# ---- P08 : ZOOM MENAGE (grille 2x2 avec pictos) ----
def p08_menage():
    ic = {
      "lit": f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none"><path d="M3 18v-6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v6" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round"/><path d="M3 18h18M6 10V7h12v3" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      "spray": f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none"><path d="M9 8h6l-1 12H10L9 8z" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"/><path d="M11 8V5h3M17 4l2-1M18 6l2 0M17 8l2 1" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round"/></svg>',
      "loupe": f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none"><circle cx="10.5" cy="10.5" r="6" stroke="{ACCENT}" stroke-width="1.8"/><path d="M15 15l6 6" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round"/></svg>',
      "photo": f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none"><rect x="3" y="7" width="18" height="13" rx="2" stroke="{ACCENT}" stroke-width="1.8"/><path d="M9 7l1.5-2.5h3L15 7" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="13.5" r="3.2" stroke="{ACCENT}" stroke-width="1.8"/></svg>',
    }
    tiles = [(ic["lit"], "Linge blanc hôtelier", "Draps et serviettes qualité hôtel, fournis et pliés"),
             (ic["spray"], "Consommables refaits", "Savon, papier, café : rien ne manque jamais"),
             (ic["loupe"], "Contrôle pièce par pièce", "Une checklist passée après chaque ménage"),
             (ic["photo"], "Photos de contrôle", "La preuve visuelle envoyée après chaque passage")]
    grid = "".join(f'<div style="width:calc(50% - 10px);background:{CARD};border:1.5px solid rgba(23,34,47,0.08);'
                   f'border-radius:18px;padding:28px 26px;">{svg}'
                   f'<div style="color:{ACCENT};font-weight:800;font-size:24px;margin-top:14px;">{t}</div>'
                   f'<div style="color:{INK};font-weight:500;font-size:20px;line-height:1.35;margin-top:8px;">{d}</div></div>'
                   for svg, t, d in tiles)
    inner = f'<div style="display:flex;flex-wrap:wrap;gap:20px;">{grid}</div>'
    return base("Zoom service", f'Un logement {acc("impeccable")}, séjour après séjour', inner,
        "adapte les 4 tuiles à TON process ménage (prestataire, linge, contrôles...).")

# ---- P11 : 5 SIGNES (checklist a cocher) ----
def p11_signes():
    items = ["Vous répondez encore aux voyageurs à 23h",
             "Le ménage entre deux séjours est un casse-tête",
             "Votre calendrier a des trous inexpliqués",
             "Vos prix n'ont pas bougé depuis des mois",
             "Vous n'osez plus partir en week-end"]
    rows = "".join(f'<div style="display:flex;gap:18px;align-items:center;background:{CARD};'
                   f'border:1.5px solid rgba(23,34,47,0.08);border-radius:14px;padding:19px 24px;margin-top:15px;">'
                   f'<div style="width:34px;height:34px;border:3px solid {ACCENT};border-radius:8px;flex-shrink:0;"></div>'
                   f'<div style="color:{INK};font-weight:600;font-size:23px;line-height:1.3;">{t}</div></div>'
                   for t in items)
    strip = (f'<div style="background:{ACCENT};border-radius:14px;padding:16px 26px;margin-top:22px;text-align:center;'
             f'color:#fff;font-weight:800;font-size:22px;">3 cases cochées ou plus ? Écrivez-nous, on en parle.</div>')
    return base("Propriétaires", f'5 signes qu\'il est temps de {acc("déléguer")}', rows+strip,
        "ce post se poste tel quel : tes couleurs, ton logo, ton contact en bas.")

# ---- P12 : IDEE RECUE COUT (calcul) ----
def p12_calcul():
    def calc(color, bg, title_txt, lines, total):
        lis = "".join(f'<div style="color:{INK};font-weight:600;font-size:22px;line-height:1.5;">{l}</div>' for l in lines)
        return (f'<div style="flex:1;border:2px solid {color};border-radius:16px;padding:26px 28px;background:{bg};">'
                f'<div style="color:{color};font-weight:900;font-size:23px;text-transform:uppercase;">{title_txt}</div>'
                f'<div style="margin-top:14px;">{lis}</div>'
                f'<div style="color:{color};font-weight:900;font-size:34px;margin-top:14px;">{total}</div></div>')
    seul = calc(REDL, "rgba(185,74,68,0.07)", "Seul", ["100 € la nuit", "× 12 nuits réservées", "+ vos soirées et week-ends"], "= 1 200 €")
    avec = calc(GREENL, "rgba(47,125,87,0.07)", "Avec conciergerie", ["110 € la nuit, optimisée", "× 18 nuits réservées", "- 20% de commission"], "= 1 584 €")
    punch = (f'<div style="background:{ACCENT};border-radius:16px;padding:22px 30px;margin-top:26px;text-align:center;">'
             f'<div style="color:#fff;font-weight:900;font-size:30px;">+ 384 € par mois, sans lever le petit doigt</div>'
             f'<div style="color:rgba(255,255,255,0.85);font-weight:600;font-size:19px;margin-top:8px;font-style:italic;">'
             f'Exemple illustratif : chaque marché est différent</div></div>')
    inner = f'<div style="display:flex;gap:18px;align-items:stretch;">{seul}{avec}</div>{punch}'
    return base("Idée reçue", f'« Une conciergerie, ça coûte cher » : faisons le {acc("calcul")}', inner,
        "remplace par TES chiffres réels (tarif, nuits, commission) : le calcul doit être honnête.", tsize=44)

# ---- P13 : TEMPS RECUPERE (addition des heures) ----
def p13_temps():
    rows = [("5 h", "Messages et demandes voyageurs"),
            ("6 h", "Ménages, linge, contrôles"),
            ("4 h", "Arrivées, départs, imprévus"),
            ("3 h", "Annonce, prix, calendrier")]
    lis = "".join(f'<div style="display:flex;align-items:center;gap:22px;background:{CARD};'
                  f'border:1.5px solid rgba(23,34,47,0.08);border-radius:14px;padding:18px 26px;margin-top:14px;">'
                  f'<div style="color:{ACCENT};font-weight:900;font-size:34px;width:96px;text-align:right;flex-shrink:0;">{h}</div>'
                  f'<div style="color:{INK};font-weight:600;font-size:23px;">{t}</div></div>' for h, t in rows)
    total = (f'<div style="display:flex;align-items:center;gap:22px;background:{INK};border-radius:14px;'
             f'padding:22px 26px;margin-top:20px;">'
             f'<div style="color:#fff;font-weight:900;font-size:40px;width:130px;text-align:right;flex-shrink:0;">18 h</div>'
             f'<div style="color:#fff;font-weight:800;font-size:24px;">rendues chaque mois. Deux week-ends entiers.</div></div>')
    return base("Propriétaires", f'Ce que vous {acc("récupérez")} : votre temps, chiffré', lis+total,
        "ajuste les heures à la réalité de TES propriétaires (c'est souvent plus).")

# ---- P14 : PROPRIETAIRE A DISTANCE (objection / reponse) ----
def p14_distance():
    pairs = [("« Je suis à 600 km »", "Nous, on est sur place. C'est justement le principe."),
             ("« Et s'il y a un souci à 22h ? »", "C'est notre téléphone qui sonne, jamais le vôtre."),
             ("« Je veux garder un œil »", "Photos et compte rendu après chaque séjour, revenus suivis en temps réel.")]
    rows = ""
    for q, r in pairs:
        rows += (f'<div style="margin-top:22px;">'
                 f'<div style="display:inline-block;background:rgba(23,34,47,0.06);border-radius:30px;'
                 f'padding:12px 24px;color:{MUTED};font-weight:700;font-size:22px;font-style:italic;">{q}</div>'
                 f'<div style="background:{CARD};border-left:5px solid {ACCENT};border-radius:0 14px 14px 0;'
                 f'padding:18px 24px;margin-top:10px;margin-left:34px;color:{INK};font-weight:600;font-size:23px;line-height:1.35;">{r}</div></div>')
    return base("Propriétaires", f'Louer sans être sur place, {acc("sereinement")}', rows,
        "remplace « 600 km » par un vrai cas de chez toi, et poste tel quel.")

# ---- P15 : LES 4 ETAPES (escalier) ----
def p15_etapes():
    steps = [("1", "On se rencontre", "Visite de votre bien, échange sur vos objectifs. Gratuit."),
             ("2", "On prépare", "Annonce, photos, équipement, tarifs : tout est calé."),
             ("3", "On lance", "Voyageurs, séjours, ménage : votre bien travaille."),
             ("4", "Vous suivez", "Revenus et comptes rendus. Le reste, c'est pour nous.")]
    rows = ""
    for i, (n, t, d) in enumerate(steps):
        rows += (f'<div style="display:flex;gap:22px;align-items:flex-start;margin-left:{i*56}px;margin-top:{0 if i==0 else 18}px;'
                 f'background:{CARD};border:1.5px solid rgba(23,34,47,0.08);border-radius:16px;padding:20px 26px;max-width:760px;">'
                 f'<div style="color:{ACCENT};font-weight:900;font-size:52px;line-height:0.9;flex-shrink:0;">{n}</div>'
                 f'<div><div style="color:{INK};font-weight:800;font-size:25px;">{t}</div>'
                 f'<div style="color:{MUTED};font-weight:500;font-size:20px;line-height:1.35;margin-top:6px;">{d}</div></div></div>')
    zone = f'<div style="margin-top:26px;text-align:center;">{dz("Délai moyen chez toi. Exemple : votre bien en ligne en 2 semaines")}</div>'
    return base("Comment ça se passe", f'Nous confier votre bien, en {acc("4 étapes")}', rows+zone,
        "adapte les étapes et le délai à TON process. Tes couleurs, ton logo.")

# ---- P16 : LES BONNES QUESTIONS (Q fixes / reponses a remplir) ----
def p16_questions():
    qs = ["Qui entre chez moi, et quand ?",
          "Comment sont fixés mes prix ?",
          "Que se passe-t-il en cas de casse ?",
          "Comment je suis mes revenus ?"]
    rows = ""
    for q in qs:
        rows += (f'<div style="margin-top:18px;">'
                 f'<div style="color:{INK};font-weight:800;font-size:24px;"><span style="color:{ACCENT};font-weight:900;">Q.</span> {q}</div>'
                 f'<div style="border:2.5px dashed {ANNOT};border-radius:12px;padding:12px 20px;margin-top:8px;'
                 f'color:{ANNOT};font-weight:600;font-size:19px;font-style:italic;">Ta réponse, en une phrase claire</div></div>')
    intro = (f'<div style="color:{MUTED};font-weight:600;font-size:22px;font-style:italic;">'
             f'Les questions que vous DEVRIEZ poser à toute conciergerie. Voici nos réponses :</div>')
    return base("Transparence", f'Les {acc("4 questions")} à nous poser (et nos réponses)', intro+rows,
        "réponds à chaque question avec TON process réel : c'est le post qui crée la confiance.", tsize=44)

# ---- P21 : AVIS 5 ETOILES (3 temps) ----
def p21_avis():
    stars = f'<div style="text-align:center;color:{ACCENT};font-size:44px;letter-spacing:10px;margin-bottom:24px;">★★★★★</div>'
    cols = [("Avant", "Une annonce exacte, des infos claires : zéro mauvaise surprise à l'arrivée."),
            ("Pendant", "Réponse en moins d'une heure et un petit plus mémorable dans le logement."),
            ("Après", "Un message de fin qui oriente l'avis, et une réponse à chaque commentaire.")]
    row = "".join(f'<div style="flex:1;background:{CARD};border-top:6px solid {ACCENT};border-radius:16px;'
                  f'padding:26px 24px;">'
                  f'<div style="color:{ACCENT};font-weight:900;font-size:24px;text-transform:uppercase;letter-spacing:1px;">{t}<span style="color:{MUTED};font-weight:700;font-size:18px;text-transform:none;"> le séjour</span></div>'
                  f'<div style="color:{INK};font-weight:500;font-size:21px;line-height:1.4;margin-top:12px;">{d}</div></div>'
                  for t, d in cols)
    note = (f'<div style="background:rgba(23,34,47,0.05);border-radius:14px;padding:16px 24px;margin-top:24px;'
            f'text-align:center;color:{INK};font-weight:700;font-size:21px;">'
            f'Propreté, exactitude et arrivée pèsent double dans votre note.</div>')
    inner = stars + f'<div style="display:flex;gap:18px;align-items:stretch;">{row}</div>' + note
    return base("Astuce propriétaire", f'La recette des avis {acc("5 étoiles")}', inner,
        "ce conseil se poste tel quel : tes couleurs, ton logo, ta signature.")

# ---- P22 : CHECK-IN (chemin numerote fleche) ----
def p22_checkin():
    steps = [("J-1", "Le message qui dit tout : code, parking, wifi, horaires"),
             ("Jour J matin", "Code testé, logement à température, lumières prêtes"),
             ("Arrivée", "Entrée autonome fluide, ou accueil en personne"),
             ("H+1", "Petit message : « tout va bien ? » Les soucis se règlent à chaud")]
    rows = ""
    for i, (t, d) in enumerate(steps):
        rows += (f'<div style="display:flex;align-items:center;gap:20px;margin-top:{0 if i==0 else 14}px;">'
                 f'<div style="background:{ACCENT};color:#fff;font-weight:900;font-size:21px;border-radius:30px;'
                 f'padding:12px 22px;white-space:nowrap;flex-shrink:0;min-width:170px;text-align:center;">{t}</div>'
                 f'<div style="color:{INK};font-weight:600;font-size:23px;line-height:1.3;">{d}</div></div>')
        if i < 3:
            rows += f'<div style="color:{ACCENT};font-weight:900;font-size:26px;margin:6px 0 0 74px;">↓</div>'
    note = (f'<div style="background:rgba(23,34,47,0.05);border-radius:14px;padding:16px 24px;margin-top:26px;'
            f'text-align:center;color:{INK};font-weight:700;font-size:21px;">'
            f'L\'arrivée pèse double dans les avis : c\'est la première impression.</div>')
    return base("Astuce propriétaire", f'Un check-in sans accroc, la note {acc("suit")}', rows+note,
        "ce conseil se poste tel quel : tes couleurs, ton logo, ta signature.")

# ---- P23 : EQUIPEMENTS = FILTRES (grille de pills) ----
def p23_equipements():
    on = [("Lave-linge déclaré", "filtre familles et longs séjours"),
          ("Lit parapluie + chaise haute", "filtre voyage avec bébé"),
          ("Espace de travail dédié", "filtre télétravail"),
          ("Wifi mesuré, débit affiché", "rassure les nomades"),
          ("Tous les couchages déclarés", "mieux classé pour les familles")]
    pills = "".join(f'<div style="display:flex;gap:14px;align-items:center;background:{CARD};'
                    f'border:2px solid {GREENL};border-radius:40px;padding:14px 24px;margin-top:14px;">'
                    f'<div style="color:{GREENL};font-weight:900;font-size:26px;">✓</div>'
                    f'<div style="color:{INK};font-weight:700;font-size:22px;">{t} '
                    f'<span style="color:{MUTED};font-weight:500;font-size:19px;">· {d}</span></div></div>'
                    for t, d in on)
    off = (f'<div style="display:flex;gap:14px;align-items:center;background:rgba(185,74,68,0.07);'
           f'border:2px solid {REDL};border-radius:40px;padding:14px 24px;margin-top:20px;">'
           f'<div style="color:{REDL};font-weight:900;font-size:26px;">×</div>'
           f'<div style="color:{INK};font-weight:700;font-size:22px;">Cocher des cases « pour faire bien » '
           f'<span style="color:{MUTED};font-weight:500;font-size:19px;">· il faut les BONS équipements pour VOS voyageurs</span></div></div>')
    intro = (f'<div style="color:{MUTED};font-weight:600;font-size:22px;font-style:italic;margin-bottom:8px;">'
             f'Chaque équipement coché = un filtre de recherche où votre annonce apparaît.</div>')
    return base("Astuce propriétaire", f'Vos équipements sont des {acc("filtres")} de recherche', intro+pills+off,
        "ce conseil se poste tel quel : tes couleurs, ton logo, ta signature.", tsize=46)

# ---- P24 : 5 ERREURS (croix + bon reflexe) ----
def p24_erreurs():
    items = [("La photo principale montre un salon banal", "Montrez votre atout distinctif : vue, jacuzzi, terrasse"),
             ("Un prix unique toute l'année", "Chaque saison, chaque événement local a son tarif"),
             ("Le titre inventaire : wifi, parking, clim...", "Capacité + équipement star + localisation"),
             ("Décliner des demandes, annuler", "Chaque refus est un signal négatif pour l'algorithme"),
             ("L'annonce jamais mise à jour", "Une annonce vivante remonte, une annonce figée descend")]
    rows = "".join(f'<div style="background:{CARD};border:1.5px solid rgba(23,34,47,0.08);border-radius:14px;'
                   f'padding:17px 24px;margin-top:14px;">'
                   f'<div style="display:flex;gap:14px;align-items:flex-start;">'
                   f'<div style="color:{REDL};font-weight:900;font-size:26px;line-height:1.1;">×</div>'
                   f'<div style="color:{INK};font-weight:700;font-size:23px;line-height:1.25;">{e}</div></div>'
                   f'<div style="display:flex;gap:14px;align-items:flex-start;margin-top:6px;margin-left:40px;">'
                   f'<div style="color:{GREENL};font-weight:900;font-size:22px;">→</div>'
                   f'<div style="color:{GREENL};font-weight:600;font-size:20px;line-height:1.3;">{f}</div></div></div>'
                   for e, f in items)
    return base("Astuce propriétaire", f'5 erreurs qui {acc("plombent")} une annonce', rows,
        "ce conseil se poste tel quel : tes couleurs, ton logo, ta signature.")

# ---- P28 : AVANT / APRES ANNONCE (vertical, resultat) ----
def p28_avant_apres():
    av = (f'<div style="border:2px solid {REDL};border-radius:16px;padding:24px 28px;background:rgba(185,74,68,0.06);">'
          f'<div style="color:{REDL};font-weight:900;font-size:22px;text-transform:uppercase;">Avant</div>'
          f'<div style="color:{INK};font-weight:600;font-size:22px;line-height:1.45;margin-top:10px;">'
          f'12 photos sombres au téléphone · titre « Bel appartement centre-ville » · prix fixe · '
          f'<span style="color:{REDL};font-weight:800;">55% d\'occupation</span></div></div>')
    ap = (f'<div style="border:2px solid {GREENL};border-radius:16px;padding:24px 28px;background:rgba(47,125,87,0.06);margin-top:14px;">'
          f'<div style="color:{GREENL};font-weight:900;font-size:22px;text-transform:uppercase;">Après reprise en main</div>'
          f'<div style="color:{INK};font-weight:600;font-size:22px;line-height:1.45;margin-top:10px;">'
          f'Photos lumineuses refaites · titre qui fait cliquer · prix pilotés à la saison · '
          f'<span style="color:{GREENL};font-weight:800;">82% d\'occupation</span></div></div>')
    arrow = f'<div style="text-align:center;color:{ACCENT};font-weight:900;font-size:34px;margin:10px 0;">▼</div>'
    zone = (f'<div style="border:2.5px dashed {ANNOT};border-radius:16px;height:210px;margin-top:24px;'
            f'display:flex;align-items:center;justify-content:center;text-align:center;color:{ANNOT};'
            f'font-weight:700;font-size:22px;font-style:italic;line-height:1.4;">'
            f'Tes captures avant / après ici :<br>photos de l\'annonce, courbe de réservations...</div>')
    ex = f'<div class="ex" style="margin-top:14px;text-align:center;"><b>Exemple :</b> remplace par UN vrai bien que tu as repris (chiffres réels)</div>'
    return base("Preuve", f'Une annonce {acc("reprise en main")}, avant / après', av+arrow+ap+zone+ex,
        "tes vrais chiffres, tes vraies captures : c'est la preuve qui convainc le plus.", tsize=46)

# ---- P29 : VRAI OU FAUX ----
def p29_vrai_faux():
    def badge(v):
        c = GREENL if v else REDL
        return (f'<div style="background:{c};color:#fff;font-weight:900;font-size:20px;border-radius:10px;'
                f'padding:10px 18px;flex-shrink:0;letter-spacing:1px;">{"VRAI" if v else "FAUX"}</div>')
    items = [("Une annonce se classe surtout grâce à son prix", False, "C'est la conversion : les vues qui deviennent des réservations"),
             ("Répondre vite fait monter l'annonce", True, "Moins d'une heure : c'est un critère direct de l'algorithme"),
             ("Plus d'équipements cochés, mieux c'est, toujours", False, "Il faut les BONS équipements pour VOS voyageurs"),
             ("Les avis récents comptent plus que les anciens", True, "L'algorithme lit surtout les 2 derniers mois")]
    rows = "".join(f'<div style="background:{CARD};border:1.5px solid rgba(23,34,47,0.08);border-radius:14px;'
                   f'padding:19px 24px;margin-top:15px;display:flex;gap:18px;align-items:flex-start;">{badge(v)}'
                   f'<div><div style="color:{INK};font-weight:700;font-size:23px;line-height:1.25;">{q}</div>'
                   f'<div style="color:{MUTED};font-weight:500;font-size:19px;line-height:1.3;margin-top:6px;">{r}</div></div></div>'
                   for q, v, r in items)
    return base("Quiz", f'{acc("Vrai ou faux")} : la location courte durée', rows,
        "ce post se poste tel quel. En description : demande leur score en commentaire.")

# ---- P30 : QUESTION AUX PROPRIETAIRES (post conversation) ----
def p30_question():
    inner = (f'<div style="text-align:center;">'
             f'<div style="color:{ACCENT};font-weight:900;font-size:150px;line-height:0.9;">?</div>'
             f'<div style="color:{INK};font-weight:900;font-size:46px;line-height:1.15;text-transform:uppercase;'
             f'letter-spacing:-1px;margin-top:24px;">Qu\'est-ce qui vous empêche<br>de louer votre bien ?</div>'
             f'<div style="display:flex;gap:14px;justify-content:center;margin-top:34px;flex-wrap:wrap;">'
             + "".join(f'<div style="border:2px solid {ACCENT};color:{ACCENT};font-weight:800;font-size:21px;'
                       f'border-radius:40px;padding:14px 26px;">{t}</div>'
                       for t in ["Le temps", "La confiance", "Par où commencer ?"])
             + f'</div>'
             f'<div style="color:{MUTED};font-weight:600;font-size:23px;font-style:italic;margin-top:34px;">'
             f'Dites-le nous en commentaire : on répond à tout le monde.</div></div>')
    return base("On vous écoute", f'Parlons {acc("vrai")}, propriétaires', inner,
        "adapte la question à ta ville si tu veux (« ...votre bien à Annecy ? ») et poste.")

GROUPS = {
    "pack_demo": [visuel_01, visuel_02, visuel_03, visuel_04,
                  visuel_05, visuel_06, visuel_07, visuel_08,
                  visuel_09, visuel_10, visuel_11],
    "pack_variantes": [variante_mindmap, variante_funnel,
                       variante_avant_apres, variante_anatomie],
    # LE PACK FINAL : les 30 posts dans l'ordre du plan PACK_CONCIERGERIE_30_POSTS.md
    "pack_30": [
        visuel_04,            # 01 Pourquoi j'ai cree ma conciergerie (recit)
        p02_equipe,           # 02 Qui veille sur votre bien (portrait)
        p03_valeurs,          # 03 Nos valeurs (3 colonnes pictos)
        p04_journee,          # 04 Une journee type (timeline)
        visuel_02,            # 05 Nos services (cartes)
        p06_annonce,          # 06 Zoom annonce (checklist verte)
        p07_accueil,          # 07 Zoom accueil (2 colonnes)
        p08_menage,           # 08 Zoom menage (grille 2x2 pictos)
        visuel_11,            # 09 Zone d'intervention (pills + photo)
        visuel_01,            # 10 Pourquoi confier votre bien (4 cartes)
        p11_signes,           # 11 5 signes qu'il est temps de deleguer (checklist)
        p12_calcul,           # 12 Idee recue cout (calcul)
        p13_temps,            # 13 Temps recupere (addition)
        p14_distance,         # 14 Proprietaire a distance (objection/reponse)
        p15_etapes,           # 15 Les 4 etapes (escalier)
        p16_questions,        # 16 Les bonnes questions (Q/R a remplir)
        visuel_03,            # 17 Photos qui font reserver (liste)
        variante_anatomie,    # 18 Titre d'annonce (schema annote)
        variante_mindmap,     # 19 Algorithme (carte mentale)
        variante_avant_apres, # 20 Prix (match avant/apres)
        p21_avis,             # 21 Avis 5 etoiles (3 temps)
        p22_checkin,          # 22 Check-in (chemin numerote)
        p23_equipements,      # 23 Equipements = filtres (pills)
        p24_erreurs,          # 24 5 erreurs (croix + bon reflexe)
        variante_funnel,      # 25 3 chiffres a surveiller (entonnoir)
        visuel_09,            # 26 Temoignage proprietaire
        visuel_10,            # 27 Chiffres cles + slogan
        p28_avant_apres,      # 28 Annonce reprise en main (preuve)
        p29_vrai_faux,        # 29 Vrai ou faux (quiz)
        p30_question,         # 30 Question aux proprietaires (conversation)
    ],
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
