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
            + f'<div class="hand" style="font-size:50px;position:absolute;right:110px;bottom:420px;">'
            f'{nb(hand_bottom)}</div>'
            + arrow_down(880, 1330, 130, 170, BLANC)
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
        kw = (f'<div class="serif" style="font-size:84px;margin-top:34px;">'
              f'«&nbsp;{acc(keyword)}&nbsp;»</div>')
    return (open_story(bg) + '<div class="pad" style="justify-content:center;">'
            f'<div class="serif t2">{nb(title)}</div>' + kw
            + underline(560, BLANC, x=80, y=1150)
            + f'<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1190px;">{nb(hand)}</div>'
            + '</div></div>')

# ------------------------------------------------------- les sequences (contenu)
# REMPLI a partir des extractions de transcriptions (agents du 03/08/2026).

SEQUENCES = {}   # rempli plus bas par un Edit une fois les extractions recues

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
