#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANQUE DE SEQUENCES V4 : stories "aide gratuite" auto-suffisantes, construites
a partir des transcriptions des videos YouTube de Sebastien (@moresebastien).

Retours de Martin (04/08/2026) : "il faut vraiment DE TOUT" :
  - des SCHEMAS qui remplissent (presque) toute la story
  - des stories dans le THEME Le Sous Loueur (couleurs de la charte)
  - garder aussi les styles photo "fait main" qu'il aime
  - bientot : integrer des PHOTOS de Sebastien (en fond ou en medaillon) ->
    deposer les fichiers dans stories/assets/photos/ (ex. sebastien_01.jpg),
    le parametre photo= des gabarits cover() et b_cta() les integre en
    medaillon rond ; tant que le fichier n'existe pas, le gabarit s'affiche
    sans medaillon (aucune casse).

Deux familles de gabarits, MIXEES dans chaque sequence :
  FAMILLE MARQUE (fond navy charte LSL, Montserrat, schemas pleine hauteur) :
    b_steps / b_timeline / b_bars / b_bigstat / b_duo / b_vs / b_formula / b_cta
  FAMILLE PHOTO (fonds chauds Gemini, serif, fait main) :
    cover / focus / fin

Chaque story reste complete et prete a poster (rien a rajouter).
Contenu 100 % tire des transcriptions (rien d'invente).
Rendu : python3 render_stories.py banque-01
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[0]
FONTS = REPO / "pipeline" / "assets" / "fonts"
LOGO = REPO / "pipeline" / "assets" / "logos" / "lesousloueur_white_temp.png"
BGS = ROOT / "assets" / "backgrounds"
PHOTOS = ROOT / "assets" / "photos"          # photos de Sebastien (a venir)

# Charte Le Sous Loueur (identique aux carrousels, PARTIE C1)
NAVY   = "#0d1b2e"
ORANGE = "#E8561F"
BLUE   = "#2086C8"
BLANC  = "#ffffff"
RED    = "#ff5a5a"
GREEN  = "#5dd987"
# Accents famille photo
BLEU   = "#4E9FE0"
BLEUF  = "#2F7EC4"
NOIR   = "#161616"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()
LOGO_B64 = b64(LOGO, "image/png")

def photo_b64(name):
    """Photo de Sebastien si presente, sinon None (les gabarits s'adaptent)."""
    if not name:
        return None
    p = PHOTOS / name
    return b64(p, "image/jpeg") if p.exists() else None

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
.story{{width:1080px;height:1920px;position:relative;overflow:hidden;color:{BLANC};
  background:{NAVY};font-family:'Montserrat',sans-serif;}}

/* ------------------------- FAMILLE PHOTO (fait main) ------------------------ */
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:center;}}
.pad{{position:absolute;inset:0;padding:270px 76px 380px;z-index:2;display:flex;
  flex-direction:column;}}
.serif{{font-family:'Playfair',serif;font-weight:800;color:{BLANC};
  text-shadow:0 2px 22px rgba(0,0,0,0.45), 0 1px 4px rgba(0,0,0,0.35);}}
.serif .b{{color:{BLEU};}}
.t1{{font-size:84px;line-height:1.14;}}
.t2{{font-size:58px;line-height:1.2;}}
.t3{{font-size:46px;line-height:1.25;}}
.hand{{font-family:'Caveat',cursive;font-weight:600;color:{BLANC};
  text-shadow:0 2px 14px rgba(0,0,0,0.5);}}
.veil{{background:rgba(255,255,255,0.74);border-radius:26px;padding:42px 40px;
  backdrop-filter:blur(7px);box-shadow:0 14px 44px rgba(0,0,0,0.18);}}
.stept{{font-family:'Montserrat',sans-serif;font-weight:500;font-size:29px;
  line-height:1.45;color:#333;}}
.stept .b{{color:{BLEUF};font-weight:700;}}
.abs{{position:absolute;}}
.medaillon{{border-radius:50%;border:6px solid {BLANC};box-shadow:0 14px 44px rgba(0,0,0,0.4);
  background-size:cover;background-position:center;}}

/* ------------------------- FAMILLE MARQUE (charte LSL) ---------------------- */
.bbg{{position:absolute;inset:0;background:
  radial-gradient(115% 75% at 84% -5%, rgba(232,86,31,0.18) 0%, rgba(13,27,46,0) 55%),
  radial-gradient(100% 70% at -5% 105%, rgba(32,134,200,0.18) 0%, rgba(13,27,46,0) 52%),
  {NAVY};}}
.btopbar{{position:absolute;top:0;left:0;right:0;height:10px;
  background:linear-gradient(90deg,{BLUE} 0%,#5fa0d0 50%,{ORANGE} 100%);z-index:5;}}
.blogo{{position:absolute;top:104px;left:0;right:0;display:flex;justify-content:center;z-index:6;}}
.blogo img{{height:54px;opacity:0.95;}}
.bpad{{position:absolute;inset:0;padding:236px 74px 372px;z-index:2;display:flex;
  flex-direction:column;}}
.bkick{{color:{ORANGE};font-weight:800;font-size:27px;letter-spacing:5px;
  text-transform:uppercase;margin-bottom:22px;}}
.btitle{{font-weight:900;font-size:56px;line-height:1.12;letter-spacing:-1px;
  text-transform:uppercase;}}
.btitle .o{{color:{ORANGE};}}
.btitle .c{{color:{BLUE};}}
.bfill{{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;
  margin-top:14px;}}

.bstep{{display:flex;gap:28px;align-items:flex-start;}}
.bstepn{{flex-shrink:0;width:64px;height:64px;border-radius:16px;background:{ORANGE};
  color:{BLANC};font-weight:900;font-size:33px;display:flex;align-items:center;
  justify-content:center;margin-top:2px;}}
.bsteph{{font-weight:800;font-size:34px;line-height:1.2;color:{BLANC};}}
.bsteph .o{{color:{ORANGE};}}
.bstept{{font-weight:500;font-size:27px;line-height:1.4;color:rgba(255,255,255,0.88);
  margin-top:8px;}}
.bstept .o{{color:{ORANGE};font-weight:700;}}

.btl{{display:flex;flex-direction:column;flex:1;margin-top:10px;}}
.btlrow{{display:flex;gap:30px;flex:1;}}
.btlleft{{display:flex;flex-direction:column;align-items:center;width:40px;flex-shrink:0;}}
.btldot{{width:30px;height:30px;border-radius:50%;background:{ORANGE};
  box-shadow:0 0 0 8px rgba(232,86,31,0.20);flex-shrink:0;margin-top:6px;}}
.btldot.blue{{background:{BLUE};box-shadow:0 0 0 8px rgba(32,134,200,0.20);}}
.btlline{{width:5px;flex-grow:1;background:rgba(255,255,255,0.18);margin-top:8px;}}
.btlh{{font-weight:800;font-size:33px;line-height:1.2;}}
.btlh .o{{color:{ORANGE};}}
.btlt{{font-weight:500;font-size:26px;line-height:1.38;color:rgba(255,255,255,0.85);
  margin-top:6px;padding-bottom:26px;}}

.bbarrow{{margin-bottom:8px;}}
.bbarlab{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px;}}
.bbarname{{font-weight:700;font-size:29px;color:{BLANC};}}
.bbarpct{{font-weight:900;font-size:38px;color:{ORANGE};}}
.bbartrack{{height:44px;border-radius:22px;background:rgba(255,255,255,0.10);overflow:hidden;}}
.bbarfill{{height:100%;border-radius:22px;background:linear-gradient(90deg,{BLUE} 0%,{ORANGE} 100%);}}

.bnum{{font-weight:900;color:{ORANGE};line-height:0.95;letter-spacing:-4px;}}
.bnumlab{{font-weight:800;font-size:40px;line-height:1.25;margin-top:18px;}}
.bpoint{{display:flex;gap:18px;align-items:flex-start;font-weight:500;font-size:28px;
  line-height:1.4;color:rgba(255,255,255,0.9);}}
.bpoint .ar{{color:{ORANGE};font-weight:900;flex-shrink:0;}}

.bcard{{border-radius:20px;padding:36px 38px;border:2.5px solid;}}
.bcard .h{{font-weight:900;font-size:30px;text-transform:uppercase;letter-spacing:1px;
  margin-bottom:20px;}}
.bcard .li{{font-weight:600;font-size:27px;line-height:1.4;color:rgba(255,255,255,0.92);
  margin-bottom:14px;display:flex;gap:14px;}}
.bcard .li:last-child{{margin-bottom:0;}}

.bctacard{{background:{BLANC};border-radius:28px;padding:52px 44px;text-align:center;
  box-shadow:0 24px 70px rgba(0,0,0,0.5);}}
.bctacard .lbl{{color:{NAVY};font-weight:800;font-size:34px;letter-spacing:4px;}}
.bctacard .kw{{color:{NAVY};font-weight:900;line-height:1.05;margin-top:12px;letter-spacing:2px;}}
.bctacard .und{{width:150px;height:8px;background:{ORANGE};border-radius:4px;margin:26px auto 0;}}
"""

def acc(w):      return f'<span class="b">{w}</span>'      # bleu (photo)
def o(w):        return f'<span class="o">{w}</span>'      # orange (marque)

def nb(text):
    if not text:
        return text
    for p in ("?", "!", ":", ";"):
        text = text.replace(f" {p}", f"&nbsp;{p}")
    return text.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")

# ------------------------------------------------------- FAMILLE PHOTO

def open_photo(bg):
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

def cover(bg, hand_top, title, sub=None, hand_bottom="la suite juste après", photo=None):
    h = (f'<div class="hand" style="font-size:58px;margin-bottom:28px;">{nb(hand_top)}</div>'
         if hand_top else '')
    s = (f'<div class="serif t3" style="margin-top:44px;font-weight:700;">{nb(sub)}</div>'
         if sub else '')
    ph = photo_b64(photo)
    med = (f'<div class="medaillon abs" style="width:300px;height:300px;right:84px;top:290px;'
           f'background-image:url({ph});"></div>') if ph else ''
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            + h + f'<div class="serif t1">{nb(title)}</div>' + s + med
            + f'<div class="hand" style="font-size:50px;position:absolute;right:230px;bottom:430px;">'
            f'{nb(hand_bottom)}</div>'
            + arrow_down(940, 1330, 120, 170, BLANC)
            + '</div></div>')

def focus(bg, kicker, big, body=None, hand=None):
    k = (f'<div class="hand" style="font-size:54px;margin-bottom:26px;">{nb(kicker)}</div>'
         if kicker else '')
    b = ''
    if body:
        b = (f'<div class="veil" style="margin-top:48px;">'
             f'<div class="stept">{nb(body)}</div></div>')
    h = (f'<div class="hand" style="font-size:50px;position:absolute;right:100px;bottom:410px;">{nb(hand)}</div>'
         if hand else '')
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            + k + f'<div class="serif t1">{nb(big)}</div>' + b + h
            + '</div></div>')

def fin(bg, title, hand, keyword=None):
    kw = ''
    if keyword:
        kw = (f'<div class="serif" style="font-size:50px;margin-top:44px;">Réponds</div>'
              f'<div class="serif" style="font-size:84px;margin-top:8px;">'
              f'«&nbsp;{acc(keyword)}&nbsp;»</div>')
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            f'<div class="serif t2">{nb(title)}</div>' + kw
            + underline(560, BLANC, x=80, y=1150)
            + f'<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1190px;">{nb(hand)}</div>'
            + '</div></div>')

# ------------------------------------------------------- FAMILLE MARQUE

def open_brand():
    return ('<div class="story"><div class="bbg"></div><div class="btopbar"></div>'
            f'<div class="blogo"><img src="{LOGO_B64}"/></div>')

def b_head(kicker, title):
    k = f'<div class="bkick">{nb(kicker)}</div>' if kicker else ''
    return k + f'<div class="btitle">{nb(title)}</div>'

def b_steps(kicker, title, items):
    rows = ""
    for i, (label, texte) in enumerate(items, 1):
        t = f'<div class="bstept">{nb(texte)}</div>' if texte else ''
        rows += (f'<div class="bstep"><div class="bstepn">{i}</div>'
                 f'<div><div class="bsteph">{nb(label)}</div>{t}</div></div>')
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + f'<div class="bfill">{rows}</div></div></div>')

def b_timeline(kicker, title, steps):
    tl = '<div class="btl">'
    for i, (h, t, blue) in enumerate(steps):
        last = i == len(steps) - 1
        line = '' if last else '<div class="btlline"></div>'
        tl += (f'<div class="btlrow"><div class="btlleft">'
               f'<div class="btldot{" blue" if blue else ""}"></div>{line}</div>'
               f'<div><div class="btlh">{nb(h)}</div>'
               f'<div class="btlt">{nb(t)}</div></div></div>')
    tl += '</div>'
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + tl + '</div></div>')

def b_bars(kicker, title, bars, note=None):
    maxv = max(v for _, v in bars)
    rows = ""
    for name, v in bars:
        rows += (f'<div class="bbarrow"><div class="bbarlab">'
                 f'<div class="bbarname">{nb(name)}</div>'
                 f'<div class="bbarpct">{v}&nbsp;%</div></div>'
                 f'<div class="bbartrack"><div class="bbarfill" style="width:{v/maxv*100:.0f}%;"></div></div></div>')
    n = (f'<div class="bpoint" style="margin-top:6px;"><span class="ar">→</span>'
         f'<span>{nb(note)}</span></div>') if note else ''
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + f'<div class="bfill">{rows}{n}</div></div></div>')

def b_bigstat(kicker, title, number, numlab, points, numsize=190):
    pts = "".join(f'<div class="bpoint"><span class="ar">→</span><span>{nb(t)}</span></div>'
                  for t in points)
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + '<div class="bfill">'
            f'<div><div class="bnum" style="font-size:{numsize}px;">{number}</div>'
            f'<div class="bnumlab">{nb(numlab)}</div></div>'
            f'<div style="display:flex;flex-direction:column;gap:26px;">{pts}</div>'
            '</div></div></div>')

def b_duo(kicker, title, bad_head, bad_items, good_head, good_items):
    def card(head, items, color, bg, mark):
        lis = "".join(f'<div class="li"><span style="color:{color};font-weight:900;">{mark}</span>'
                      f'<span>{nb(t)}</span></div>' for t in items)
        return (f'<div class="bcard" style="border-color:{color};background:{bg};">'
                f'<div class="h" style="color:{color};">{nb(head)}</div>{lis}</div>')
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + '<div class="bfill" style="gap:30px;justify-content:center;">'
            + card(bad_head, bad_items, RED, "rgba(255,90,90,0.08)", "×")
            + card(good_head, good_items, GREEN, "rgba(93,217,135,0.08)", "→")
            + '</div></div></div>')

def b_vs(kicker, title, left_head, left_lines, right_head, right_lines, verdict):
    def card(head, lines, color, bg):
        ls = "".join(f'<div style="font-weight:600;font-size:27px;line-height:1.45;'
                     f'color:rgba(255,255,255,0.92);margin-top:12px;">{nb(t)}</div>' for t in lines)
        return (f'<div class="bcard" style="flex:1;border-color:{color};background:{bg};">'
                f'<div class="h" style="color:{color};">{nb(head)}</div>{ls}</div>')
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + '<div class="bfill" style="gap:30px;justify-content:center;">'
            '<div style="display:flex;gap:24px;align-items:stretch;">'
            + card(left_head, left_lines, RED, "rgba(255,90,90,0.08)")
            + card(right_head, right_lines, GREEN, "rgba(93,217,135,0.08)")
            + '</div>'
            f'<div class="bpoint" style="font-size:30px;"><span class="ar">→</span>'
            f'<span>{nb(verdict)}</span></div>'
            '</div></div></div>')

def b_formula(kicker, title, top, bottom, result, rule):
    return (open_brand() + '<div class="bpad">' + b_head(kicker, title)
            + '<div class="bfill" style="justify-content:center;gap:44px;">'
            '<div style="background:rgba(255,255,255,0.07);border:2.5px solid rgba(255,255,255,0.18);'
            'border-radius:22px;padding:52px 40px;text-align:center;">'
            f'<div style="font-weight:800;font-size:35px;line-height:1.4;">{nb(top)}</div>'
            f'<div style="width:420px;height:5px;background:{ORANGE};border-radius:3px;margin:26px auto;"></div>'
            f'<div style="font-weight:800;font-size:35px;">{nb(bottom)}</div>'
            f'<div style="font-weight:900;font-size:44px;color:{ORANGE};margin-top:34px;">{nb(result)}</div>'
            '</div>'
            f'<div class="bpoint" style="font-size:31px;"><span class="ar">→</span>'
            f'<span>{nb(rule)}</span></div>'
            '</div></div></div>')

def b_cta(kicker, title, keyword, sub, photo=None):
    size = 68 if len(keyword) >= 12 else (88 if len(keyword) >= 8 else 130)
    ph = photo_b64(photo)
    med = (f'<div class="medaillon" style="width:220px;height:220px;margin:0 auto 40px;'
           f'background-image:url({ph});"></div>') if ph else ''
    return (open_brand() + '<div class="bpad" style="justify-content:center;">'
            + med + b_head(kicker, title)
            + f'<div class="bctacard" style="margin-top:64px;"><div class="lbl">RÉPONDS</div>'
            f'<div class="kw" style="font-size:{size}px;">{keyword}</div>'
            '<div class="und"></div></div>'
            f'<div style="color:{ORANGE};font-weight:600;font-style:italic;font-size:31px;'
            f'text-align:center;margin-top:40px;">{nb(sub)}</div>'
            '</div></div>')

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
    b_vs("levier 1", f'Le {o("tarif par voyageur")}',
         "Ce que tout le monde fait", ["120 € la nuit,", "pour tout le monde,", "quel que soit le nombre de voyageurs."],
         "Ce que font les pros", ["95 € pour 2 voyageurs", "+ 12 € par voyageur en plus.", "Couple : 95 €. Famille de 4 : 119 €."],
         "La majorité des recherches se font en réglage par défaut (1-2 voyageurs) : "
         "tu t'affiches à 95 € et tu passes devant les annonces à 120 €."),
    b_bigstat("levier 2, ignoré par 90 % des hôtes", f'Le tarif {o("non remboursable")}',
              "-10&nbsp;%", "affiché dans les résultats de recherche.",
              ["Ton annonce paraît moins chère, donc mieux classée.",
               "La remise ne s'applique qu'à ceux qui acceptent le non remboursable.",
               "Ceux-là n'auraient jamais annulé : tu offres 10 % à des résas en béton."]),
    b_steps("levier 3", f'Les équipements sont des {o("filtres")}',
            [("Coche TOUT ce que tu as", "Non coché = invisible pour celui qui filtre. Sèche-cheveux, fer, détecteur de fumée : pense aux oubliés."),
             ("Le combo famille", "Lit parapluie + chaise haute : tu ressors dans les filtres famille plusieurs fois."),
             ("Le canal télétravail", "Un vrai espace de travail, et le débit wifi mesuré écrit dans l'annonce.")]),
    b_steps("leviers 4 et 5", f'Ta {o("vitrine")} : photo, titre, avis',
            [("La couverture, jamais le salon", "Montre le distinctif : la vue, le jacuzzi, la terrasse. En miniature, un salon ressemble à tous les salons."),
             ("Le titre en 50 caractères", "Capacité + atout star + lieu : « 6 personnes, jacuzzi, 5 min de la plage »."),
             ("Les avis à mots-clés", "L'algorithme lit le texte des avis. Invite tes voyageurs à citer le jacuzzi, le check-in... pendant 6 mois.")]),
    b_cta("on te dit ce que vaut ton annonce", "Tu veux ton audit ?",
          "AUDIT", "On t'envoie l'outil d'audit gratuit en DM."),
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
    b_bars("du moins au plus efficace", f'Les 5 canaux, {o("classés")}',
           [("5. Prospection ciblée", 20),
            ("4. Apporteurs d'affaires", 40),
            ("3. Agents immobiliers", 60),
            ("2. Référence locale (Google)", 80),
            ("1. L'audit chiffré", 100)],
           note="Les % = efficacité relative d'après le classement de la vidéo. "
                "Le n°1 est détaillé juste après."),
    focus("bg_ville_doree", "le canal n°1",
          f'Fais un {acc("audit")}, pas un pitch.',
          body="Repère une annonce qui sous-performe : mauvaises notes, trous en "
               "juillet, prix qui ne bougent jamais. Chiffre son manque à gagner avec "
               "un outil de data : « tu perds peut-être 8 000 € par an ». Tu offres "
               "l'info, tu ne vends rien : le proprio voit le chiffre tout seul."),
    b_duo("côté légal", f'Les {o("pièges")} à éviter',
          "Jamais", ["Prospecter via la messagerie Airbnb : bannissement possible",
                     "Le pitch commercial direct : valeur perçue zéro"],
          "À la place", ["Retrouve le proprio ailleurs : son site, sa fiche Google, Le Bon Coin",
                         "Offre l'audit et laisse les chiffres parler"]),
    b_bigstat("l'astuce que personne ne fait", f'Les avis Google de {o("proprios")}',
              "15", "avis de propriétaires satisfaits, et tu écrases la concurrence locale.",
              ["Celui qui tape « conciergerie + ta ville » est un prospect chaud.",
               "Demande les avis à tes PROPRIOS, pas à tes voyageurs.",
               "Bonus : une page par quartier, même par rue. Sur « conciergerie + ta rue », il n'y a personne."],
              numsize=210),
    b_cta("acquisition", "On regarde ton plan ensemble ?",
          "GO", "Réponds GO et on fait le point sur ta stratégie."),
],

# ============================================================================
# SEQUENCE C — Recuperer les proprios decus (video t_sxyIULJEQ)
# ============================================================================
"C_proprios_decus": [
    cover("bg_ville_doree", "aide gratuite du jour",
          f'Ton meilleur client&nbsp;? Le proprio {acc("déçu")} d\'une autre conciergerie.',
          sub="Comment le trouver avant tout le monde, légalement.",
          hand_bottom="la méthode juste après"),
    b_timeline("psychologie du proprio", f'Les {o("5 phases")} avant la rupture',
               [("Mois 1 à 3 : la lune de miel", "Il vient de déléguer, il est soulagé, tout va bien.", False),
                ("Mois 4 à 8 : le doute", "Communication lente, tarifs qui semblent bas, avis moyens.", False),
                ("Mois 8 à 12 : la comparaison", "Il regarde les autres et parle aux voisins proprios.", False),
                ("Mois 12 à 18 : la frustration", "Il fait ses comptes : la rentabilité promise n'est pas là.", False),
                ("La rupture", "Lettre recommandée, ou il part à la fin de saison.", True)]),
    b_bigstat("le vrai secret, c'est le timing", f'La {o("fenêtre de tir")}',
              "4 → 12", "c'est entre le mois 4 et le mois 12 que tout se joue.",
              ["En phase de doute, il tape déjà ses questions sur Google.",
               "Si ton contenu répond à ses douleurs, tu deviens sa référence.",
               "Une fois la rupture décidée, c'est la guerre du moins cher."],
              numsize=170),
    b_steps("lead magnets", f'3 {o("aimants")} à proprios déçus',
            [("L'audit gratuit en 48 h", "Il t'envoie son annonce, tu réponds sous 48 h. Bonus : tu vois le bien et la gestion AVANT de t'engager."),
             ("Le calculateur de revenus", "Il entre son adresse et découvre ce que son bien devrait vraiment rapporter."),
             ("La checklist des 10 questions", "« Les 10 questions à poser à votre conciergerie. » Tu éduques, tu ne vends pas.")]),
    b_duo("la ligne est claire", f'Côté {o("légal")}',
          "Jamais", ["Dénigrer un concurrent par son nom",
                     "Démarcher les clients d'un concurrent au téléphone",
                     "Récupérer des emails sur les annonces (RGPD)"],
          "Toujours", ["Éduquer avec du contenu qui répond aux douleurs",
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
    b_steps("d'abord, ce qui tue", f'Les {o("3 erreurs")} fatales',
            [("Le mode bricolage", "Contrat trouvé sur internet, annonces sur TON compte Airbnb. À 10 logements, tout est à refaire."),
             ("Vendre de la « gestion »", "« Gérer », « mandat » : ces mots te font tomber sous la loi Hoguet. Dis pilotage, coordination, prestation."),
             ("Empiler les contrats", "À 8-10 contrats sans système, tu es devenu le salarié de ta propre boîte.")]),
    b_timeline("la roadmap", f'Les {o("4 piliers")} de 0 à 30',
               [("Contrats 1 à 5 : les fondations", "Contrat conforme, UNE ville et 30 km max, des prix jamais bradés.", False),
                ("5 à 12 : le système", "Channel manager, messages automatiques, onboarding standardisé, ménage sous-traité.", False),
                ("10 à 20 : les leviers", "Parrainage structuré, proprios déçus, référencement local. Premier city manager.", False),
                ("20 à 30 : l'industrialisation", "Tu pilotes aux chiffres : occupation, prix moyen, satisfaction proprio.", True)]),
    b_bigstat("la règle qui change tout", f'{o("2026")} : tout au nom du proprio',
              "100&nbsp;%", "des comptes au nom du propriétaire : Airbnb, Booking, revenue management.",
              ["C'est le proprio qui pilote et qui valide les prix.",
               "En 2025, des conciergeries ont été condamnées pour avoir géré sans validation.",
               "Les juges vérifient l'opérationnel, pas juste le contrat."],
              numsize=170),
    focus("bg_prairie", "le canal que personne ne structure",
          f'Le bouche à oreille, ça se {acc("fabrique")}.',
          body="Offre 1 mois de prestation au proprio qui t'amène un nouveau client. "
               "Même mécanique avec les agents immobiliers et les experts-comptables "
               "LMNP. C'est un canal d'acquisition, pas de la chance."),
    b_cta("la méthode complète est en vidéo", "Et pour TON plan ?",
          "GO", "Réponds GO, on en parle. La vidéo t'attend sur la chaîne."),
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
    b_bars("ce qui pèse vraiment", f'Ton classement, {o("décomposé")}',
           [("Haut : photo, titre, prix", 20),
            ("Milieu : clics, favoris", 30),
            ("Bas : séjour réel, avis", 50)],
           note="90 % des loueurs optimisent dans le mauvais sens : le séjour "
                "d'abord, la photo ensuite."),
    b_bars("les 7 facteurs mesurés", f'Les nouveaux {o("poids")} 2026',
           [("Guest Favorite", 25),
            ("Avis récents (le texte)", 20),
            ("Temps de réponse", 10),
            ("Taux de conversion", 10),
            ("Photos", 8),
            ("Instant Book", 7),
            ("Prix vs marché", 5)],
           note="Le Superhost est obsolète : Guest Favorite = 4,9+ et 5 avis en 2 ans."),
    b_duo("mise à jour", f'Ce qui ne {o("marche plus")}',
          "Oublie", ["Le boost nouvelle annonce : quasi nul désormais",
                     "Tes bons avis de 2023 : seuls les 30-60 derniers jours comptent",
                     "Le Superhost et la course aux 5 étoiles"],
          "À la place", ["Instant Book activé : 15 à 25 % de boost",
                         "Une photo qui tranche : couleurs vives, photo saisonnière",
                         "Viser TES voyageurs, pas tous les voyageurs"]),
    b_bigstat("le levier le plus rapide", f'La {o("photo de couverture")}',
              "+35&nbsp;%", "de revenus possibles en changeant UNE photo.",
              ["80 % des voyageurs décident en 2-3 secondes.",
               "Couleurs vives quand tout le monde est en gris pastel.",
               "Photo de Noël dès fin novembre : une annonce qui vit, l'algorithme le voit."],
              numsize=190),
    b_cta("le plan 30 jours est en vidéo", "Tu veux le guide complet ?",
          "ALGO", "Réponds ALGO et on t'envoie le pack Airbnb 2026 en DM."),
],

# ============================================================================
# SEQUENCE F — Le piege de la caution (video 4Dlw1_c593k)
# ============================================================================
"F_caution": [
    cover("bg_salon_cosy", "l'erreur qui coûte cher",
          f'La {acc("caution")} : le piège que 80 % découvrent trop tard.',
          sub="Caution, assurance, loi Hoguet : ce qu'il faut savoir AVANT l'incident.",
          hand_bottom="explication simple juste après"),
    b_vs("la base que tout le monde confond", f'Caution {o("vs")} assurance',
         "La caution", ["Tu récupères l'argent DU voyageur.", "Montant limité à la caution fixée.", "Le litige, c'est toi qui le gères."],
         "L'assurance", ["Un tiers paie à ta place.", "Montant limité par la garantie.", "L'assureur gère sinistre ET litige."],
         "Elles ne se remplacent pas : la vraie protection, c'est les deux couches empilées."),
    focus("bg_salon_cosy", "conciergeries : le test en une question",
          f'Qui {acc("déclenche")} le débit&nbsp;?',
          body="Si c'est la conciergerie, c'est du maniement de fonds pour le compte "
               "de tiers : illégal au sens de la loi Hoguet, même avec des "
               "sous-comptes. La solution propre : la caution part du compte de "
               "paiement DU propriétaire, jamais du tien."),
    b_steps("les règles qui sauvent", f'4 réflexes {o("caution")}',
            [("Chèque, virement, espèces : terminé", "On ne demande plus jamais ça à un voyageur."),
             ("L'empreinte expire en 7 jours", "Un dégât découvert tard, et il n'y a plus rien à débiter."),
             ("Débiter ne règle rien", "Le voyageur peut contester. Un sinistre documenté, photos à l'appui, change tout."),
             ("AirCover ne couvre qu'Airbnb", "Sur Booking et les résas en direct, sans solution dédiée, tu n'es couvert par rien.")]),
    b_bigstat("la stratégie des pros", f'Le {o("double filet")}',
              "50 000 €", "couverts par une assurance dédiée, pour environ 100 € par an.",
              ["La caution dissuade et couvre les petits dégâts.",
               "L'assurance prend le relais sur les gros sinistres.",
               "Et quand le débit de la caution échoue : ça arrive vraiment."],
              numsize=150),
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
    b_steps("auto-diagnostic", f'Les {o("5 erreurs")} fatales',
            [("Pas de positionnement", "« Je fais de la conciergerie » = généraliste choisi sur le prix. Le spécialiste fixe ses tarifs."),
             ("Tout à la main", "Tableurs, messages copiés-collés, prix fixes. Les pros automatisent et gèrent 3 fois plus."),
             ("Le client, c'est le voyageur ?", "Non : le vrai client, c'est le proprio. C'est lui qui donne les clés, et qui peut les reprendre."),
             ("Ignorer ses chiffres", "Certains paient plus de ménage qu'ils n'encaissent, et le découvrent au bilan."),
             ("Tout faire tout seul", "Mois 1-3 : facile. Mois 7-9 : plus de vie. Mois 10-12 : j'arrête.")]),
    b_bigstat("le mythe du volume", f'50 biens à 15 %&nbsp;? Tu bosses {o("gratuitement")}',
              "10 = 50", "10 logements bien choisis rapportent autant que 50 subis.",
              ["Ménage mal maîtrisé, occupation à 30-40 %, prix bradés : il ne reste rien.",
               "Le volume, c'est une vanité. La marge, c'est la survie.",
               "Et en prime : beaucoup moins de stress."],
              numsize=150),
    b_formula("la formule que personne ne calcule", f'Ton {o("coût par nuitée")}',
              "ménage + linge + consommables + ton temps",
              "nombre de nuitées",
              "= ton coût par nuitée",
              "Si ta commission est en dessous, tu refuses le bien. Savoir dire "
              "non, c'est la clé de la survie."),
    b_steps("rétention proprios", f'Le {o("reporting")} qui les retient',
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
    b_timeline("la roadmap 12 mois", f'Les {o("3 phases")}',
               [("Semaines 1-4 : les fondations", "Une zone de 15-20 min max. Premier client gratuit 2 mois (ménage payé) contre témoignages. Process documentés dès le début.", False),
                ("Mois 2-6 : l'accélération", "Outils pro au 5e bien (50 h/mois gagnées à 10 biens). 2-3 agents de ménage + 1 artisan. Pricing dynamique : +15 %.", False),
                ("Mois 6-12 : le scale", "Coordinateur AVANT commercial. Montée en gamme : 20-25 % de commission sur les beaux biens.", True)]),
    b_bigstat("l'acquisition sans site web", f'Ta fiche {o("Google")}',
              "43&nbsp;%", "des proprios choisissent leur conciergerie via un avis Google.",
              ["Au début : une fiche Google + LinkedIn suffisent, pas de site.",
               "L'audit gratuit sous 48 h à la place du démarchage : conversion triplée.",
               "3 offres au lieu d'un tarif unique : panier presque doublé."],
              numsize=190),
    b_bigstat("la sélection des biens", f'À 30 € la nuit, tu gagnes {o("6 €")}',
              "400-500 €", "de gain par mois et par bien, c'est la cible.",
              ["10 biens dans la cible = 5 000 € par mois.",
               "Une maison à 3 000 € de CA demande le même travail qu'un appart à 700 €.",
               "Moins de volume, plus de valeur."],
              numsize=150),
    b_duo("l'expérience parle", f'Ce qu\'il ne {o("referait plus")}',
          "Fini", ["Accepter tous les biens, même les galères",
                   "Casser les prix à 12-15 % de commission",
                   "Le local et le site web dès le départ"],
          "À la place", ["Refuser un bien (et parfois un proprio) non rentable",
                         "Démarrer à 18-20 %, à la hauteur du travail",
                         "Chez soi 1 an, charges fixes minimales"]),
    b_cta("objectif 12 mois : 30 biens, 4 500-7 500 €/mois", "Et TON plan à toi ?",
          "GO", "Réponds GO et on le construit ensemble."),
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
            d = [ch for ch in html if ch in DASHES]
            if d: print(f"  ALERTE tiret {name}: {set(d)}"); td += len(d)
            (out / f"{name}.html").write_text(html, encoding="utf-8")
            n += 1
    print(f"{n} stories ecrites dans {out}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
