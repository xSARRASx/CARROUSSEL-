#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STYLE UNIQUE DES STORIES (decision de Martin, 03/08/2026, sur capture d'ecran
de la cover "Remplir ton Airbnb sans baisser tes prix") :

  TOUTES les stories, sans exception, sont dans le style "photo fait main" :
    - fond photo chaud plein ecran (stories/assets/backgrounds/)
    - titres en serif blanche (Playfair) avec mots-cles en bleu ciel
    - annotations manuscrites (Caveat) et fleches/soulignes dessines a la main
    - contenu dense sur voile blanc translucide (Montserrat, texte sombre,
      accents bleus)
    - LE LOGO SUR TOUTES LES STORIES (demande explicite de Martin), en haut
      au centre, blanc avec ombre portee douce.

  La famille "marque" (fond navy / orange de la charte) est ABANDONNEE pour
  les stories. La charte navy/orange reste celle des carrousels.

Ce module est LE socle commun : fonds, polices, logo, gabarits.
Les builds (banque, interactifs, semaine) ne font qu'assembler du contenu.
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[0]
FONTS = REPO / "pipeline" / "assets" / "fonts"
LOGO = REPO / "pipeline" / "assets" / "logos" / "lesousloueur_white_temp.png"
BGS = ROOT / "assets" / "backgrounds"
PHOTOS = ROOT / "assets" / "photos"          # photos de Sebastien (a venir)

# Palette du style photo
BLEU  = "#4E9FE0"    # bleu ciel (mots-cles dans les titres serif)
BLEUF = "#2F7EC4"    # bleu soutenu (accents sur voile blanc)
BLANC = "#ffffff"
INK   = "#22303f"    # texte principal sur voile
INKS  = "#4a5665"    # texte secondaire sur voile
RED   = "#D95043"    # corail doux (colonnes "jamais / fini")

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
    font_face("Playfair", "playfair-display-latin-700-normal.woff2", 700),
    font_face("Playfair", "playfair-display-latin-800-normal.woff2", 800),
    font_face("Caveat", "caveat-latin-600-normal.woff2", 600),
])

COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;
   text-rendering:geometricPrecision;}}
.story{{width:1080px;height:1920px;position:relative;overflow:hidden;color:{BLANC};
  background:#777;font-family:'Montserrat',sans-serif;}}
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:center;}}

/* LOGO : sur toutes les stories, sans exception (Martin, 03/08/2026) */
.plogo{{position:absolute;top:100px;left:0;right:0;display:flex;justify-content:center;
  z-index:8;}}
.plogo img{{height:56px;filter:drop-shadow(0 3px 14px rgba(0,0,0,0.45));opacity:0.97;}}

.pad{{position:absolute;inset:0;padding:270px 76px 380px;z-index:2;display:flex;
  flex-direction:column;}}
.pad2{{position:absolute;inset:0;padding:238px 70px 340px;z-index:2;display:flex;
  flex-direction:column;}}
.pfill{{flex:1;display:flex;flex-direction:column;justify-content:center;margin-top:34px;}}

.serif{{font-family:'Playfair',serif;font-weight:800;color:{BLANC};
  text-shadow:0 2px 22px rgba(0,0,0,0.45), 0 1px 4px rgba(0,0,0,0.35);}}
.serif .b{{color:{BLEU};}}
.t1{{font-size:84px;line-height:1.14;}}
.t2{{font-size:56px;line-height:1.18;}}
.t3{{font-size:46px;line-height:1.25;}}
.hand{{font-family:'Caveat',cursive;font-weight:600;color:{BLANC};
  text-shadow:0 2px 14px rgba(0,0,0,0.5);}}
.abs{{position:absolute;}}
.medaillon{{border-radius:50%;border:6px solid {BLANC};box-shadow:0 14px 44px rgba(0,0,0,0.4);
  background-size:cover;background-position:center;}}

/* TEXTE LIBRE : posé directement sur la photo, sans cadre.
   Martin, 10/08/2026 : « j'aime pas trop les gros blocs au centre ».
   Un paragraphe court n'a pas besoin d'un rectangle blanc : il se lit très
   bien en blanc sur la photo, avec une ombre portée. On garde le voile
   uniquement pour le contenu DENSE et structuré (listes, frises, tableaux),
   là où l'oeil a vraiment besoin d'un support. */
.libre{{font-weight:600;font-size:31px;line-height:1.52;color:{BLANC};
  text-shadow:0 2px 20px rgba(0,0,0,0.66), 0 1px 5px rgba(0,0,0,0.5);}}
.libre .b{{color:{BLEU};font-weight:800;}}
/* fondu sombre very doux, sans bord visible : garantit la lisibilite du
   texte libre meme sur une photo claire, sans jamais ressembler a un bloc. */
.scrim{{position:absolute;left:0;right:0;bottom:0;height:1250px;z-index:1;
  background:linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.12) 34%,
    rgba(0,0,0,0.40) 68%, rgba(0,0,0,0.55) 100%);}}
/* meme fondu, mais par le HAUT : pour les gabarits dont le texte est ancre en
   haut (les questions de quiz). Sans lui, une photo claire avalait le texte,
   puisque le fondu du bas ne monte pas jusque-la. */
.scrimhaut{{position:absolute;left:0;right:0;top:0;height:1120px;z-index:1;
  background:linear-gradient(to bottom, rgba(0,0,0,0.52) 0%, rgba(0,0,0,0.40) 38%,
    rgba(0,0,0,0.20) 72%, rgba(0,0,0,0) 100%);}}

/* voile blanc : le support du contenu dense */
.veil{{background:rgba(255,255,255,0.78);border-radius:26px;padding:40px 42px;
  backdrop-filter:blur(8px);box-shadow:0 14px 44px rgba(0,0,0,0.20);}}
.vt{{font-weight:600;font-size:27px;line-height:1.45;color:{INK};}}
.vt .b{{color:{BLEUF};font-weight:800;}}
.vnote{{display:flex;gap:14px;font-weight:600;font-size:25px;line-height:1.42;color:{INK};}}
.vnote .ar{{color:{BLEUF};font-weight:800;flex-shrink:0;}}
.vnote .b{{color:{BLEUF};font-weight:800;}}

/* etapes numerotees */
.pstep{{display:flex;gap:26px;align-items:flex-start;margin-bottom:30px;}}
.pstep:last-child{{margin-bottom:0;}}
.pstepn{{font-family:'Playfair',serif;font-weight:800;font-size:46px;line-height:1;
  color:{BLEUF};flex-shrink:0;width:54px;margin-top:2px;}}
.psteph{{font-weight:800;font-size:29px;line-height:1.25;color:{INK};}}
.psteph .b{{color:{BLEUF};}}
.pstept{{font-weight:500;font-size:26px;line-height:1.4;color:{INKS};margin-top:8px;}}
.pstept .b{{color:{BLEUF};font-weight:700;}}

/* timeline */
.ptlrow{{display:flex;gap:24px;}}
.ptlleft{{display:flex;flex-direction:column;align-items:center;width:30px;flex-shrink:0;}}
.ptldot{{width:22px;height:22px;border-radius:50%;background:{BLEUF};
  box-shadow:0 0 0 7px rgba(47,126,196,0.16);flex-shrink:0;margin-top:6px;}}
.ptlline{{width:4px;flex-grow:1;background:#c9d4de;margin-top:8px;}}
.ptlh{{font-weight:800;font-size:28px;line-height:1.22;color:{INK};}}
.ptlh .b{{color:{BLEUF};}}
.ptlt{{font-weight:500;font-size:25px;line-height:1.38;color:{INKS};
  margin-top:6px;padding-bottom:24px;}}

/* barres */
.pbarrow{{margin-bottom:26px;}}
.pbarrow:last-child{{margin-bottom:0;}}
.pbarlab{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px;}}
.pbarname{{font-weight:700;font-size:26px;color:{INK};}}
.pbarpct{{font-family:'Playfair',serif;font-weight:800;font-size:34px;color:{BLEUF};}}
.pbartrack{{height:36px;border-radius:18px;background:#e4e9ee;overflow:hidden;}}
.pbarfill{{height:100%;border-radius:18px;background:linear-gradient(90deg,#6FB4E6 0%,{BLEUF} 100%);}}

/* grand chiffre */
.pnum{{font-family:'Playfair',serif;font-weight:800;color:{BLEU};line-height:0.98;
  letter-spacing:-2px;text-shadow:0 3px 26px rgba(0,0,0,0.45);}}
.pnumlab{{font-family:'Playfair',serif;font-weight:800;font-size:40px;line-height:1.25;
  color:{BLANC};text-shadow:0 2px 22px rgba(0,0,0,0.45);margin-top:16px;}}

/* cartes duo / vs */
.pcard{{background:rgba(255,255,255,0.80);border-radius:22px;padding:32px 36px;
  backdrop-filter:blur(8px);box-shadow:0 14px 44px rgba(0,0,0,0.20);border-top:6px solid;}}
.pcard .h{{font-weight:800;font-size:26px;text-transform:uppercase;letter-spacing:1px;
  margin-bottom:18px;}}
.pcard .li{{display:flex;gap:14px;font-weight:600;font-size:26px;line-height:1.4;
  color:{INK};margin-bottom:13px;}}
.pcard .li:last-child{{margin-bottom:0;}}

/* carte CTA blanche */
.pctacard{{background:{BLANC};border-radius:28px;padding:50px 44px;text-align:center;
  box-shadow:0 22px 60px rgba(0,0,0,0.35);}}
.pctacard .lbl{{font-weight:800;font-size:30px;letter-spacing:5px;color:{INK};}}
.pctacard .kw{{font-family:'Playfair',serif;font-weight:800;line-height:1.05;
  color:#1d2a38;margin-top:14px;}}
"""

def acc(w):
    return f'<span class="b">{w}</span>'

def nb(text):
    """Typographie FR : espace insecable avant ? ! : ; et dans les guillemets."""
    if not text:
        return text
    for p in ("?", "!", ":", ";"):
        text = text.replace(f" {p}", f"&nbsp;{p}")
    return text.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")

def open_photo(bg):
    """Ouvre une story : fond photo + LOGO (toujours)."""
    img = b64(BGS / f"{bg}.jpg", "image/jpeg")
    return (f'<div class="story"><div class="bgimg" style="background-image:url({img});"></div>'
            f'<div class="plogo"><img src="{LOGO_B64}"/></div>')

def underline(width=430, color=BLEU, x=0, y=0, cls="abs"):
    w = width
    path = f"M 8 11 C {w*0.22:.0f} 3, {w*0.4:.0f} 15, {w*0.58:.0f} 9 S {w*0.85:.0f} 5, {w-8:.0f} 10"
    style = f'style="left:{x}px;top:{y}px;"' if cls == "abs" else 'style="display:block;margin:0 auto;"'
    return (f'<svg class="{cls}" {style} width="{w}" height="20" '
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

# =========================================================== gabarits pleine page

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
    """Une idee forte + son explication.

    L'explication est posee LIBREMENT sur la photo (plus de rectangle blanc au
    centre : demande de Martin le 10/08/2026). Un fondu sombre tres doux,
    sans bord visible, garantit la lisibilite.
    """
    k = (f'<div class="hand" style="font-size:54px;margin-bottom:26px;">{nb(kicker)}</div>'
         if kicker else '')
    b = (f'<div class="libre" style="margin-top:44px;">{nb(body)}</div>' if body else '')
    h = (f'<div class="hand" style="font-size:50px;position:absolute;right:100px;bottom:410px;">{nb(hand)}</div>'
         if hand else '')
    voile = '<div class="scrim"></div>' if body else ''
    return (open_photo(bg) + voile + '<div class="pad" style="justify-content:center;">'
            + k + f'<div class="serif t1">{nb(big)}</div>' + b + h
            + '</div></div>')

# ------------------------------------------------- formats interactifs partagés
# Ces trois gabarits etaient recopies dans chaque build_interactifs*.py. Les
# poser ici garantit qu'une correction de style profite a TOUTES les fournees
# suivantes, sans avoir a repasser sur chaque fichier.

def quiz_q(bg, num, total, kind, question, hint="vote avec le sondage, la réponse arrive"):
    """Une question de quiz. La moitie basse reste LIBRE pour le sticker.

    Fondu par le HAUT (le texte est ancre en haut) : sur un ciel pale, le
    fondu du bas ne remontait pas jusqu'au texte et la question devenait
    illisible. Corrige le 10/08/2026.
    """
    return (open_photo(bg) + '<div class="scrimhaut"></div>'
            + '<div class="pad" style="align-items:center;text-align:center;">'
            f'<div class="hand" style="font-size:52px;">quiz {num}/{total}</div>'
            f'<div class="serif" style="font-size:100px;line-height:1.05;margin-top:30px;">{nb(kind)}</div>'
            f'<div class="libre" style="margin-top:48px;max-width:880px;font-weight:700;">'
            f'{nb(question)}</div>'
            f'<div class="hand" style="font-size:44px;margin-top:44px;opacity:0.95;">{nb(hint)}</div>'
            '</div></div>')

def quiz_r(bg, verdict, explication, chiffre=None):
    """La reponse, revelee dans la story suivante."""
    ch = (f'<div class="serif" style="font-size:120px;line-height:1;color:{BLEU};'
          f'margin-top:34px;">{chiffre}</div>') if chiffre else ''
    return (open_photo(bg) + '<div class="scrim"></div>'
            + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
            f'<div class="serif" style="font-size:150px;line-height:1;">{acc(verdict)}</div>' + ch +
            f'<div style="margin:44px auto;">{underline(220, BLANC, cls="inline")}</div>'
            f'<div class="libre" style="max-width:870px;">{nb(explication)}</div>'
            '</div></div>')

def sondage(bg, kicker, title, note="vote juste en dessous"):
    """Un diagnostic. La moitie basse reste LIBRE pour le sticker."""
    return (open_photo(bg) + '<div class="pad">'
            f'<div class="hand" style="font-size:56px;margin-top:30px;">{nb(kicker)}</div>'
            f'<div class="serif" style="font-size:72px;line-height:1.16;margin-top:24px;">{nb(title)}</div>'
            + underline(430, BLANC, 84, 720) +
            f'<div class="hand" style="font-size:48px;position:absolute;right:130px;top:780px;">{nb(note)}</div>'
            '</div></div>')

def fin(bg, title, hand, keyword=None):
    kw = ''
    if keyword:
        kw = (f'<div class="serif" style="font-size:50px;margin-top:44px;">Réponds</div>'
              f'<div class="serif" style="font-size:84px;margin-top:8px;">'
              f'«&nbsp;{acc(keyword)}&nbsp;»</div>')
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            f'<div class="serif" style="font-size:58px;line-height:1.2;">{nb(title)}</div>' + kw
            + underline(560, BLANC, x=80, y=1150)
            + f'<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1190px;">{nb(hand)}</div>'
            + '</div></div>')

def p_head(kicker, title):
    k = (f'<div class="hand" style="font-size:50px;margin-bottom:20px;">{nb(kicker)}</div>'
         if kicker else '')
    return k + f'<div class="serif t2">{nb(title)}</div>'

def p_steps(bg, kicker, title, items):
    rows = ""
    for i, (label, texte) in enumerate(items, 1):
        t = f'<div class="pstept">{nb(texte)}</div>' if texte else ''
        rows += (f'<div class="pstep"><div class="pstepn">{i}</div>'
                 f'<div><div class="psteph">{nb(label)}</div>{t}</div></div>')
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + f'<div class="pfill"><div class="veil">{rows}</div></div></div></div>')

def p_timeline(bg, kicker, title, steps):
    tl = ""
    for i, (h, t, _hl) in enumerate(steps):
        last = i == len(steps) - 1
        line = '' if last else '<div class="ptlline"></div>'
        tl += (f'<div class="ptlrow"><div class="ptlleft"><div class="ptldot"></div>{line}</div>'
               f'<div><div class="ptlh">{nb(h)}</div>'
               f'<div class="ptlt"{" style=padding-bottom:0;" if last else ""}>{nb(t)}</div></div></div>')
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + f'<div class="pfill"><div class="veil">{tl}</div></div></div></div>')

def p_bars(bg, kicker, title, bars, note=None):
    maxv = max(v for _, v in bars)
    rows = ""
    for name, v in bars:
        rows += (f'<div class="pbarrow"><div class="pbarlab">'
                 f'<div class="pbarname">{nb(name)}</div>'
                 f'<div class="pbarpct">{v}&nbsp;%</div></div>'
                 f'<div class="pbartrack"><div class="pbarfill" style="width:{v/maxv*100:.0f}%;"></div></div></div>')
    n = (f'<div class="veil" style="margin-top:28px;"><div class="vnote"><span class="ar">→</span>'
         f'<span>{nb(note)}</span></div></div>') if note else ''
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + f'<div class="pfill"><div class="veil">{rows}</div>{n}</div></div></div>')

def p_bigstat(bg, kicker, title, number, numlab, points, numsize=190):
    pts = "".join(
        f'<div class="vnote" style="margin-bottom:{0 if i == len(points) - 1 else 20}px;">'
        f'<span class="ar">→</span><span>{nb(t)}</span></div>'
        for i, t in enumerate(points))
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + '<div class="pfill">'
            f'<div><div class="pnum" style="font-size:{numsize}px;">{number}</div>'
            f'<div class="pnumlab">{nb(numlab)}</div></div>'
            f'<div class="veil" style="margin-top:44px;">{pts}</div>'
            '</div></div></div>')

def p_duo(bg, kicker, title, bad_head, bad_items, good_head, good_items):
    def card(head, items, color, mark):
        lis = "".join(f'<div class="li"><span style="color:{color};font-weight:900;flex-shrink:0;">{mark}</span>'
                      f'<span>{nb(t)}</span></div>' for t in items)
        return (f'<div class="pcard" style="border-top-color:{color};">'
                f'<div class="h" style="color:{color};">{nb(head)}</div>{lis}</div>')
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + '<div class="pfill" style="gap:30px;">'
            + card(bad_head, bad_items, RED, "×")
            + card(good_head, good_items, BLEUF, "→")
            + '</div></div></div>')

def p_vs(bg, kicker, title, left_head, left_lines, right_head, right_lines, verdict):
    def card(head, lines, color):
        ls = "".join(f'<div style="font-weight:600;font-size:25px;line-height:1.42;'
                     f'color:{INK};margin-top:11px;">{nb(t)}</div>' for t in lines)
        return (f'<div class="pcard" style="flex:1;border-top-color:{color};padding:30px 30px;">'
                f'<div class="h" style="color:{color};font-size:25px;">{nb(head)}</div>{ls}</div>')
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + '<div class="pfill" style="gap:28px;">'
            '<div style="display:flex;gap:22px;align-items:stretch;">'
            + card(left_head, left_lines, RED)
            + card(right_head, right_lines, BLEUF)
            + '</div>'
            f'<div class="veil" style="padding:30px 36px;"><div class="vnote"><span class="ar">→</span>'
            f'<span>{nb(verdict)}</span></div></div>'
            '</div></div></div>')

def p_formula(bg, kicker, title, top, bottom, result, rule):
    return (open_photo(bg) + '<div class="pad2">' + p_head(kicker, title)
            + '<div class="pfill" style="gap:36px;">'
            '<div class="veil" style="text-align:center;padding:48px 40px;">'
            f'<div style="font-weight:800;font-size:32px;line-height:1.4;color:{INK};">{nb(top)}</div>'
            f'<div style="width:420px;height:5px;background:{BLEUF};border-radius:3px;margin:24px auto;"></div>'
            f'<div style="font-weight:800;font-size:32px;color:{INK};">{nb(bottom)}</div>'
            f'<div style="font-family:\'Playfair\',serif;font-weight:800;font-size:42px;color:{BLEUF};'
            f'margin-top:30px;">{nb(result)}</div>'
            '</div>'
            f'<div class="veil" style="padding:30px 36px;"><div class="vnote"><span class="ar">→</span>'
            f'<span>{nb(rule)}</span></div></div>'
            '</div></div></div>')

def p_cta(bg, kicker, title, keyword, sub, photo=None):
    size = 64 if len(keyword) >= 12 else (84 if len(keyword) >= 8 else 120)
    ph = photo_b64(photo)
    med = (f'<div class="medaillon" style="width:220px;height:220px;margin:0 auto 40px;'
           f'background-image:url({ph});"></div>') if ph else ''
    k = (f'<div class="hand" style="font-size:50px;margin-bottom:20px;">{nb(kicker)}</div>'
         if kicker else '')
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;">'
            + med + k + f'<div class="serif t2">{nb(title)}</div>'
            + f'<div class="pctacard" style="margin-top:60px;"><div class="lbl">RÉPONDS</div>'
            f'<div class="kw" style="font-size:{size}px;">{keyword}</div>'
            f'<div style="margin-top:22px;">{underline(150, BLEUF, cls="inline")}</div>'
            '</div>'
            f'<div class="hand" style="font-size:46px;text-align:center;margin-top:38px;">{nb(sub)}</div>'
            '</div></div>')

DASHES = "—–‒―⎯﹣－─"

def write_lot(slug, stories):
    """Ecrit un dict {nom: html_body} dans output/<slug>/html/."""
    out = ROOT / "output" / slug / "html"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.html"):
        old.unlink()
    td = 0
    for name, body in stories.items():
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{COMMON_CSS}</style></head><body>{body}</body></html>')
        d = [c for c in html if c in DASHES]
        if d:
            print(f"  ALERTE tiret {name}: {set(d)}")
            td += len(d)
    # deux passes : on n'ecrit qu'apres le controle tirets pour un log propre
    for name, body in stories.items():
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{COMMON_CSS}</style></head><body>{body}</body></html>')
        (out / f"{name}.html").write_text(html, encoding="utf-8")
    print(f"{len(stories)} stories ecrites dans {out}. Tirets longs: {td}")
