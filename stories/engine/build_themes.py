#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATALOGUE DE THEMES (04/08/2026) — regle de Martin : 1 sujet = 1 SEUL theme
visuel pour toute la sequence. Les couleurs LSL sont validees, la mise en page
"marque" V4 ne l'est pas -> nouvelles propositions.

7 themes, chacun demontre sur UN sujet avec 3 stories (cover + contenu + CTA).
Martin choisit ; ensuite la banque entiere est regeneree avec un theme par
sequence.

Rendu : python3 render_stories.py catalogue-themes
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[0]
FONTS = REPO / "pipeline" / "assets" / "fonts"
LOGO = REPO / "pipeline" / "assets" / "logos" / "lesousloueur_white_temp.png"
BGS = ROOT / "assets" / "backgrounds"

NAVY   = "#0d1b2e"
NUIT   = "#0a1322"
ORANGE = "#E8561F"
BLUE   = "#2086C8"
BLANC  = "#ffffff"
CREME  = "#F6F0E6"
ENCRE  = "#1c2a3e"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()
LOGO_B64 = b64(LOGO, "image/png")                                  # version blanche (fonds fonces)
LOGO_DARK_B64 = b64(LOGO.parent / "lesousloueur.png", "image/png")  # version navy (fonds clairs)

def logo_top(light_bg=False, height=50):
    """DESACTIVE le 04/08 au soir : Martin ne veut finalement PAS de logo
    ("simple, efficace"). Helper conserve au cas ou il rechange d'avis."""
    src = LOGO_DARK_B64 if light_bg else LOGO_B64
    return (f'<div class="abs" style="left:0;right:0;top:106px;display:flex;'
            f'justify-content:center;z-index:8;"><img src="{src}" style="height:{height}px;'
            f'opacity:0.95;"/></div>')

def font_face(family, file, weight):
    data = b64(FONTS / file, "font/woff2")
    return (f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")

FONT_FACES = "".join([
    font_face("Montserrat", "montserrat-latin-500-normal.woff2", 500),
    font_face("Montserrat", "montserrat-latin-600-normal.woff2", 600),
    font_face("Montserrat", "montserrat-latin-700-normal.woff2", 700),
    font_face("Montserrat", "montserrat-latin-800-normal.woff2", 800),
    font_face("Montserrat", "montserrat-latin-900-normal.woff2", 900),
    font_face("Playfair", "playfair-display-latin-700-normal.woff2", 700),
    font_face("Playfair", "playfair-display-latin-800-normal.woff2", 800),
    font_face("Caveat", "caveat-latin-600-normal.woff2", 600),
])

COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;
   text-rendering:geometricPrecision;}}
.story{{width:1080px;height:1920px;position:relative;overflow:hidden;
  font-family:'Montserrat',sans-serif;color:{BLANC};}}
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:center;}}
.pad{{position:absolute;inset:0;padding:270px 80px 380px;z-index:2;display:flex;
  flex-direction:column;}}
.abs{{position:absolute;}}
.serif{{font-family:'Playfair',serif;font-weight:800;
  text-shadow:0 2px 22px rgba(0,0,0,0.4);}}
.hand{{font-family:'Caveat',cursive;font-weight:600;
  text-shadow:0 2px 14px rgba(0,0,0,0.45);}}
.veil{{background:rgba(255,255,255,0.74);border-radius:26px;padding:42px 40px;
  backdrop-filter:blur(7px);box-shadow:0 14px 44px rgba(0,0,0,0.18);}}
"""

def nb(text):
    if not text:
        return text
    for p in ("?", "!", ":", ";"):
        text = text.replace(f" {p}", f"&nbsp;{p}")
    return text.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")

def photo_open(bg):
    img = b64(BGS / f"{bg}.jpg", "image/jpeg")
    return f'<div class="story"><div class="bgimg" style="background-image:url({img});"></div>'

def underline(width, color, x, y):
    w = width
    path = f"M 8 11 C {w*0.22:.0f} 3, {w*0.4:.0f} 15, {w*0.58:.0f} 9 S {w*0.85:.0f} 5, {w-8:.0f} 10"
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;" width="{w}" height="20" '
            f'viewBox="0 0 {w} 20" fill="none"><path d="{path}" stroke="{color}" '
            f'stroke-width="8" stroke-linecap="round"/></svg>')

STORIES = {}

# ============================================================================
# THEME 1 — MER (photo fait main, tout sur bg_mer_calme)
# Sujet : remplir son Airbnb sans baisser les prix
# ============================================================================
def bleu(w): return f'<span style="color:#4E9FE0;">{w}</span>'

STORIES["theme1_mer_01"] = (
    photo_open("bg_mer_calme") + '<div class="pad" style="justify-content:center;">'
    '<div class="hand" style="font-size:58px;margin-bottom:28px;">aide gratuite</div>'
    f'<div class="serif" style="font-size:84px;line-height:1.14;">Remplir ton Airbnb {bleu("sans baisser")} tes prix.</div>'
    '<div class="serif" style="font-size:46px;line-height:1.25;margin-top:44px;font-weight:700;">'
    'Airbnb ne classe pas par prix&nbsp;: il met en avant ce qui convertit.</div>'
    '<div class="hand" style="font-size:50px;position:absolute;right:120px;bottom:430px;">5 leviers, juste après</div>'
    '</div></div>')

STORIES["theme1_mer_02"] = (
    photo_open("bg_mer_calme") + '<div class="pad" style="justify-content:center;">'
    '<div class="hand" style="font-size:54px;margin-bottom:26px;">levier n°1</div>'
    f'<div class="serif" style="font-size:80px;line-height:1.14;">Affiche {bleu("95 € pour 2")}, pas 120 € pour tous.</div>'
    '<div class="veil" style="margin-top:48px;"><div style="font-weight:500;font-size:29px;line-height:1.45;color:#333;">'
    'La majorité des recherches se font en réglage par défaut, 1-2 voyageurs. '
    'Un T3 affiché <b style="color:#2F7EC4;">95 € pour 2 + 12 € par voyageur en plus</b> passe devant '
    'les concurrents à 120 €. Le couple paie 95 €, la famille de 4 paie 119 €.</div></div>'
    '</div></div>')

STORIES["theme1_mer_03"] = (
    photo_open("bg_mer_calme") + '<div class="pad" style="justify-content:center;">'
    '<div class="serif" style="font-size:58px;line-height:1.2;">Tu veux savoir ce que vaut TON annonce&nbsp;?</div>'
    '<div class="serif" style="font-size:50px;margin-top:44px;">Réponds</div>'
    f'<div class="serif" style="font-size:84px;margin-top:8px;">«&nbsp;{bleu("AUDIT")}&nbsp;»</div>'
    + underline(560, BLANC, 84, 1150) +
    '<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1190px;">'
    'et on t\'envoie l\'outil gratuit</div>'
    '</div></div>')

# ============================================================================
# THEME 2 — CIEL DORE (photo fait main, tout sur bg_ciel_dore)
# Sujet : recuperer les proprios decus
# ============================================================================
STORIES["theme2_ciel_01"] = (
    photo_open("bg_ciel_dore") + '<div class="pad" style="justify-content:center;">'
    '<div class="hand" style="font-size:58px;margin-bottom:28px;">la méthode du jour</div>'
    f'<div class="serif" style="font-size:84px;line-height:1.14;">Ton meilleur client&nbsp;? Le proprio {bleu("déçu")}.</div>'
    '<div class="serif" style="font-size:46px;line-height:1.25;margin-top:44px;font-weight:700;">'
    'Comment le trouver avant tout le monde, légalement.</div>'
    '<div class="hand" style="font-size:50px;position:absolute;right:150px;bottom:430px;">les 5 phases arrivent</div>'
    '</div></div>')

STORIES["theme2_ciel_02"] = (
    photo_open("bg_ciel_dore") + '<div class="pad">'
    f'<div class="serif" style="font-size:56px;line-height:1.2;margin-bottom:40px;">Les {bleu("5 phases")} avant la rupture&nbsp;:</div>'
    '<div class="veil"><div style="font-weight:600;font-size:29px;line-height:1.5;color:#222;">'
    '<div style="margin-bottom:20px;"><b style="color:#2F7EC4;">Mois 1-3</b> : la lune de miel. Il vient de déléguer, tout va bien.</div>'
    '<div style="margin-bottom:20px;"><b style="color:#2F7EC4;">Mois 4-8</b> : le doute. Communication lente, tarifs bas, avis moyens.</div>'
    '<div style="margin-bottom:20px;"><b style="color:#2F7EC4;">Mois 8-12</b> : la comparaison. Il regarde les autres conciergeries.</div>'
    '<div style="margin-bottom:20px;"><b style="color:#2F7EC4;">Mois 12-18</b> : la frustration. La rentabilité promise n\'est pas là.</div>'
    '<div><b style="color:#2F7EC4;">Puis la rupture</b> : recommandé, ou il part en fin de saison.</div>'
    '</div></div>'
    '<div class="hand" style="font-size:52px;margin-top:44px;text-align:right;">'
    'ta fenêtre de tir : mois 4 à 12</div>'
    '</div></div>')

STORIES["theme2_ciel_03"] = (
    photo_open("bg_ciel_dore") + '<div class="pad" style="justify-content:center;">'
    '<div class="serif" style="font-size:58px;line-height:1.2;">On regarde ta stratégie d\'acquisition ensemble&nbsp;?</div>'
    '<div class="serif" style="font-size:50px;margin-top:44px;">Réponds</div>'
    f'<div class="serif" style="font-size:110px;margin-top:8px;">«&nbsp;{bleu("GO")}&nbsp;»</div>'
    + underline(420, BLANC, 84, 1160) +
    '<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1200px;">'
    'on répond à tout le monde</div>'
    '</div></div>')

# ============================================================================
# THEME 3 — NAVY GROS TITRES (couleurs LSL, mise en page poster minimaliste :
# centre, enorme, formes rondes, logo discret en bas de zone)
# Sujet : l'algorithme Airbnb 2026
# ============================================================================
def navy_open():
    return ('<div class="story" style="background:'
            f'radial-gradient(120% 80% at 50% -10%, #16294a 0%, {NAVY} 55%);">'
            '<div class="abs" style="width:640px;height:640px;border-radius:50%;'
            f'background:radial-gradient(circle, rgba(232,86,31,0.25) 0%, rgba(232,86,31,0) 70%);'
            'right:-200px;top:180px;"></div>'
            '<div class="abs" style="width:520px;height:520px;border-radius:50%;'
            f'background:radial-gradient(circle, rgba(32,134,200,0.22) 0%, rgba(32,134,200,0) 70%);'
            'left:-160px;bottom:320px;"></div>')

STORIES["theme3_navy_01"] = (
    navy_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div style="font-weight:800;font-size:30px;letter-spacing:8px;color:{ORANGE};'
    'text-transform:uppercase;">info 2026</div>'
    '<div style="font-weight:900;font-size:96px;line-height:1.05;letter-spacing:-2px;'
    'text-transform:uppercase;margin-top:36px;">L\'algo Airbnb<br>a '
    f'<span style="color:{ORANGE};">changé</span>.</div>'
    f'<div style="width:140px;height:8px;background:{ORANGE};border-radius:4px;margin:52px auto;"></div>'
    '<div style="font-weight:600;font-size:36px;line-height:1.45;color:rgba(255,255,255,0.92);max-width:820px;">'
    'Il ne montre plus les «&nbsp;meilleurs&nbsp;» logements. Il montre le plus '
    f'<span style="color:{ORANGE};font-weight:800;">adapté</span> à chaque voyageur.</div>'
    '</div>' + '</div>')

STORIES["theme3_navy_02"] = (
    navy_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div style="font-weight:800;font-size:30px;letter-spacing:8px;color:rgba(255,255,255,0.75);'
    'text-transform:uppercase;">ce qui pèse vraiment</div>'
    f'<div style="font-weight:900;font-size:300px;line-height:0.95;color:{ORANGE};'
    'letter-spacing:-10px;margin-top:30px;">50<span style="font-size:150px;">%</span></div>'
    '<div style="font-weight:900;font-size:52px;text-transform:uppercase;margin-top:26px;">'
    'de ton classement =<br>le <span style="color:'f'{ORANGE};">séjour réel</span></div>'
    '<div style="font-weight:600;font-size:33px;line-height:1.5;color:rgba(255,255,255,0.85);'
    'max-width:800px;margin-top:44px;">Ta photo&nbsp;? 8&nbsp;%. Réservations, avis, zéro problème : '
    'c\'est ça que l\'algorithme regarde en premier.</div>'
    '</div>' + '</div>')

STORIES["theme3_navy_03"] = (
    navy_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div style="font-weight:900;font-size:64px;line-height:1.15;text-transform:uppercase;">'
    f'Le guide complet<br><span style="color:{ORANGE};">Airbnb 2026</span></div>'
    f'<div style="background:{BLANC};border-radius:32px;padding:56px 90px;margin-top:70px;'
    'box-shadow:0 24px 70px rgba(0,0,0,0.5);">'
    f'<div style="color:{NAVY};font-weight:800;font-size:34px;letter-spacing:4px;">RÉPONDS</div>'
    f'<div style="color:{NAVY};font-weight:900;font-size:110px;letter-spacing:2px;margin-top:10px;">ALGO</div>'
    f'<div style="width:150px;height:8px;background:{ORANGE};border-radius:4px;margin:26px auto 0;"></div></div>'
    f'<div style="color:{ORANGE};font-weight:600;font-style:italic;font-size:32px;margin-top:44px;">'
    'guide + checklist + plan 30 jours, en DM</div>'
    '</div>' + '</div>')

# ============================================================================
# THEME 4 — CARNET (fond papier creme, encre navy, surligneur orange,
# esprit notes manuscrites)  —  Sujet : le cout par nuitee / dire non
# ============================================================================
def carnet_open():
    return ('<div class="story" style="background:'
            f'linear-gradient(180deg, {CREME} 0%, #efe7d8 100%);color:{ENCRE};">'
            '<div class="abs" style="inset:0;background:repeating-linear-gradient('
            '0deg, rgba(28,42,62,0.045) 0px, rgba(28,42,62,0.045) 1px, transparent 1px, transparent 64px);"></div>'
            f'<div class="abs" style="left:110px;top:0;bottom:0;width:3px;background:rgba(232,86,31,0.35);"></div>'
)

def surligne(w):
    return (f'<span style="background:linear-gradient(180deg, transparent 55%, '
            f'rgba(232,86,31,0.35) 55%);">{w}</span>')

STORIES["theme4_carnet_01"] = (
    carnet_open() + '<div class="pad" style="padding-left:170px;justify-content:center;">'
    f'<div class="hand" style="font-size:58px;color:{ORANGE};text-shadow:none;">le carnet du sous loueur</div>'
    f'<div class="serif" style="font-size:80px;line-height:1.16;color:{ENCRE};text-shadow:none;margin-top:30px;">'
    f'La formule que {surligne("personne")} ne calcule.</div>'
    f'<div style="font-weight:600;font-size:36px;line-height:1.5;margin-top:44px;color:{ENCRE};">'
    'Ton coût par nuitée. Celui qui décide si un bien te fait gagner de l\'argent... ou t\'en fait perdre.</div>'
    f'<div class="hand" style="font-size:50px;color:{ENCRE};text-shadow:none;position:absolute;'
    'right:110px;bottom:420px;">je te montre, tourne pas la page</div>'
    '</div></div>')

STORIES["theme4_carnet_02"] = (
    carnet_open() + '<div class="pad" style="padding-left:170px;justify-content:center;">'
    f'<div class="serif" style="font-size:60px;line-height:1.2;color:{ENCRE};text-shadow:none;">'
    'Ton coût par nuitée&nbsp;:</div>'
    f'<div style="background:{BLANC};border:3px solid {ENCRE};border-radius:18px;'
    'padding:56px 44px;margin-top:52px;text-align:center;box-shadow:8px 10px 0 rgba(28,42,62,0.15);">'
    f'<div style="font-weight:800;font-size:36px;color:{ENCRE};">ménage + linge + consommables + ton temps</div>'
    f'<div style="width:440px;height:5px;background:{ORANGE};border-radius:3px;margin:28px auto;"></div>'
    f'<div style="font-weight:800;font-size:36px;color:{ENCRE};">nombre de nuitées</div></div>'
    f'<div style="font-weight:600;font-size:33px;line-height:1.5;margin-top:52px;color:{ENCRE};">'
    f'Si ta commission est {surligne("en dessous")}, tu refuses le bien.<br>'
    'Savoir dire non, c\'est la clé de la survie.</div>'
    '</div></div>')

STORIES["theme4_carnet_03"] = (
    carnet_open() + '<div class="pad" style="padding-left:170px;justify-content:center;">'
    f'<div class="serif" style="font-size:66px;line-height:1.2;color:{ENCRE};text-shadow:none;">'
    f'«&nbsp;Un propriétaire {surligne("bien informé")} ne part jamais.&nbsp;»</div>'
    f'<div class="hand" style="font-size:56px;color:{ENCRE};text-shadow:none;margin-top:60px;">Sébastien</div>'
    f'<div style="font-weight:600;font-size:32px;color:{ENCRE};margin-top:70px;">'
    f'La vidéo complète est sur la chaîne. Et si tu veux qu\'on en parle : réponds '
    f'<b style="color:{ORANGE};">GO</b>.</div>'
    '</div></div>')

# ============================================================================
# THEME 5 — ORANGE POSTER (fond orange plein, typo navy/blanc massive)
# Sujet : la caution
# ============================================================================
def orange_open():
    return (f'<div class="story" style="background:linear-gradient(165deg, #f0662e 0%, {ORANGE} 60%, #cf4514 100%);">'
)

STORIES["theme5_orange_01"] = (
    orange_open() + '<div class="pad" style="justify-content:center;">'
    f'<div style="font-weight:800;font-size:30px;letter-spacing:7px;color:{NAVY};'
    'text-transform:uppercase;">alerte conciergeries</div>'
    f'<div style="font-weight:900;font-size:104px;line-height:1.02;letter-spacing:-3px;'
    f'text-transform:uppercase;margin-top:34px;color:{BLANC};">La caution,<br>'
    f'<span style="color:{NAVY};">le piège</span> que 80&nbsp;% découvrent trop tard.</div>'
    f'<div style="font-weight:700;font-size:36px;margin-top:52px;color:{NAVY};">'
    'Caution, assurance, loi Hoguet : les bases, sans jargon.</div>'
    '</div></div>')

STORIES["theme5_orange_02"] = (
    orange_open() + '<div class="pad" style="justify-content:center;">'
    f'<div style="font-weight:900;font-size:72px;line-height:1.1;color:{BLANC};text-transform:uppercase;">'
    f'La question <span style="color:{NAVY};">légale</span> :</div>'
    f'<div style="background:{NAVY};border-radius:26px;padding:60px 48px;margin-top:54px;">'
    f'<div style="font-weight:900;font-size:64px;line-height:1.15;color:{BLANC};">Qui déclenche<br>le débit&nbsp;?</div>'
    f'<div style="font-weight:600;font-size:31px;line-height:1.5;color:rgba(255,255,255,0.9);margin-top:30px;">'
    'Si c\'est la conciergerie : maniement de fonds pour le compte de tiers. '
    f'<span style="color:#ffb695;font-weight:800;">Illégal</span> au sens de la loi Hoguet, '
    'même avec des sous-comptes.</div></div>'
    f'<div style="font-weight:700;font-size:33px;margin-top:48px;color:{NAVY};">'
    'La solution propre : la caution part du compte DU propriétaire. Jamais du tien.</div>'
    '</div></div>')

STORIES["theme5_orange_03"] = (
    orange_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div style="font-weight:900;font-size:78px;line-height:1.1;color:{BLANC};text-transform:uppercase;">'
    f'Et toi, tu gères<br>les cautions <span style="color:{NAVY};">comment&nbsp;?</span></div>'
    f'<div style="background:{BLANC};border-radius:999px;padding:34px 70px;margin-top:80px;">'
    f'<div style="font-weight:900;font-size:40px;color:{ORANGE};">réponds à cette story</div></div>'
    f'<div style="font-weight:700;font-size:31px;margin-top:40px;color:{NAVY};">'
    'raconte, on te dit si c\'est carré</div>'
    '</div></div>')

# ============================================================================
# THEME 6 — BLEU POSTER (fond bleu LSL plein, blanc + navy, chiffres geants)
# Sujet : trouver des clients
# ============================================================================
def bleu_open():
    return (f'<div class="story" style="background:linear-gradient(165deg, #2e97d8 0%, {BLUE} 55%, #16639a 100%);">'
)

STORIES["theme6_bleu_01"] = (
    bleu_open() + '<div class="pad" style="justify-content:center;">'
    f'<div style="font-weight:800;font-size:30px;letter-spacing:7px;color:{NAVY};'
    'text-transform:uppercase;">acquisition</div>'
    f'<div style="font-weight:900;font-size:100px;line-height:1.04;letter-spacing:-3px;'
    f'text-transform:uppercase;margin-top:34px;color:{BLANC};">Trouver des proprios&nbsp;: '
    f'<span style="color:{NAVY};">5 canaux</span>, classés.</div>'
    f'<div style="font-weight:700;font-size:36px;margin-top:52px;color:{NAVY};">'
    'Du moins au plus efficace. Le n°1 va te surprendre.</div>'
    '</div></div>')

STORIES["theme6_bleu_02"] = (
    bleu_open() + '<div class="pad" style="justify-content:center;">'
    + "".join(
        f'<div style="display:flex;align-items:center;gap:34px;margin-bottom:{mb}px;">'
        f'<div style="font-weight:900;font-size:{sz}px;color:{NAVY if i<5 else BLANC};line-height:1;">{i}</div>'
        f'<div><div style="font-weight:800;font-size:{tz}px;color:{BLANC};">{t}</div>'
        f'<div style="font-weight:500;font-size:26px;color:rgba(255,255,255,0.85);">{d}</div></div></div>'
        for i, t, d, sz, tz, mb in [
            (5, "La prospection ciblée", "Vise les proprios qui habitent loin de leur bien.", 64, 32, 40),
            (4, "Les apporteurs d'affaires", "Ménage, artisans, gardiens : un vrai deal.", 64, 32, 40),
            (3, "Les agents immobiliers", "Tes vendeurs contre ses investisseurs.", 64, 32, 40),
            (2, "La référence locale", "15 avis Google de PROPRIOS et tu écrases tout.", 64, 32, 40),
            (1, "L'audit chiffré", "« Tu perds 8 000 €/an. » Tu offres l'info, il signe.", 110, 40, 0),
        ])
    + '</div></div>')

STORIES["theme6_bleu_03"] = (
    bleu_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div style="font-weight:900;font-size:74px;line-height:1.1;color:{BLANC};text-transform:uppercase;">'
    f'On construit<br><span style="color:{NAVY};">ton plan</span> ensemble&nbsp;?</div>'
    f'<div style="background:{BLANC};border-radius:32px;padding:56px 100px;margin-top:74px;'
    'box-shadow:0 20px 60px rgba(0,0,0,0.25);">'
    f'<div style="color:{BLUE};font-weight:800;font-size:34px;letter-spacing:4px;">RÉPONDS</div>'
    f'<div style="color:{NAVY};font-weight:900;font-size:130px;letter-spacing:2px;margin-top:8px;">GO</div></div>'
    f'<div style="font-weight:700;font-size:31px;margin-top:44px;color:{NAVY};">'
    'gratuit, sans engagement, on fait juste le point</div>'
    '</div></div>')

# ============================================================================
# THEME 7 — NUIT FINE (noir bleuté, lignes fines, elegance, orange discret)
# Sujet : le plan de relance de zero
# ============================================================================
def nuit_open():
    return (f'<div class="story" style="background:{NUIT};">'
            '<div class="abs" style="inset:70px;border:2px solid rgba(255,255,255,0.14);'
            'border-radius:8px;"></div>')

STORIES["theme7_nuit_01"] = (
    nuit_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div style="font-weight:600;font-size:28px;letter-spacing:10px;color:{ORANGE};'
    'text-transform:uppercase;">le plan</div>'
    '<div class="serif" style="font-size:88px;line-height:1.15;color:#fff;margin-top:44px;">'
    'Si Sébastien repartait<br>de zéro.</div>'
    '<div style="width:70px;height:3px;background:rgba(255,255,255,0.35);margin:54px auto;"></div>'
    '<div style="font-weight:500;font-size:33px;line-height:1.55;color:rgba(255,255,255,0.85);max-width:760px;">'
    '12 mois. 3 phases. Des objectifs chiffrés.<br>Après 10 ans de terrain et près de 100 biens pilotés.</div>'
    '</div></div>')

STORIES["theme7_nuit_02"] = (
    nuit_open() + '<div class="pad" style="justify-content:center;padding-left:130px;padding-right:130px;">'
    + "".join(
        f'<div style="margin-bottom:{mb}px;">'
        f'<div style="font-weight:600;font-size:26px;letter-spacing:6px;color:{ORANGE};text-transform:uppercase;">{k}</div>'
        f'<div class="serif" style="font-size:46px;color:#fff;margin-top:14px;line-height:1.2;">{t}</div>'
        f'<div style="font-weight:500;font-size:28px;line-height:1.5;color:rgba(255,255,255,0.8);margin-top:12px;">{d}</div></div>'
        for k, t, d, mb in [
            ("semaines 1-4", "Les fondations", "Une zone de 15-20 minutes max. Premier client gratuit 2 mois contre témoignages. Des process dès le début.", 58),
            ("mois 2-6", "L'accélération", "Les outils pro au 5e bien : 50 h par mois gagnées. 2-3 agents de ménage. Pricing dynamique : +15 %.", 58),
            ("mois 6-12", "Le scale", "Coordinateur avant commercial. Montée en gamme : 20-25 % de commission sur les beaux biens.", 0),
        ])
    + '</div></div>')

STORIES["theme7_nuit_03"] = (
    nuit_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    '<div class="serif" style="font-size:64px;line-height:1.25;color:#fff;">Objectif à 12 mois&nbsp;:</div>'
    f'<div class="serif" style="font-size:96px;color:{ORANGE};margin-top:34px;">30 biens</div>'
    '<div class="serif" style="font-size:56px;color:#fff;margin-top:18px;">4 500 à 7 500 € / mois</div>'
    '<div style="width:70px;height:3px;background:rgba(255,255,255,0.35);margin:56px auto;"></div>'
    '<div style="font-weight:500;font-size:32px;line-height:1.5;color:rgba(255,255,255,0.85);">'
    f'Et pour TON plan à toi&nbsp;: réponds <span style="color:{ORANGE};font-weight:700;">GO</span>.</div>'
    '</div></div>')

SLUG = "catalogue-themes"
DASHES = "—–‒―⎯﹣－─"

def main():
    out = ROOT / "output" / SLUG / "html"
    out.mkdir(parents=True, exist_ok=True)
    td = 0
    for name, body in STORIES.items():
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body>{body}</body></html>'
        d = [ch for ch in html if ch in DASHES]
        if d: print(f"  ALERTE tiret {name}: {set(d)}"); td += len(d)
        (out / f"{name}.html").write_text(html, encoding="utf-8")
    print(f"{len(STORIES)} stories ecrites dans {out}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
