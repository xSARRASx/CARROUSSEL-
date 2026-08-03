#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 des visuels de stories : style "natif Instagram fait main", calibre sur les
stories historiques du compte @moresebastien (exemples de Pierre fournis par
Martin le 03/08/2026) :
  - fonds photo chauds (ciel dore, prairie, chemin, salon cosy) generes par Gemini
  - gros titres en serif blanche (Playfair Display, equivalent de la typo
    "serif" d'Instagram) avec mots-cles en bleu ciel
  - listes en noir gras (Montserrat) sur voile blanc translucide
  - fleches courbes et soulignements "dessines a la main" (SVG)
  - annotations manuscrites (Caveat)

5 stories temoins pour validation par Martin avant de generaliser a la semaine.
Rendu : python3 render_stories.py semaine-01-v2
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[0]
FONTS = REPO / "pipeline" / "assets" / "fonts"
BGS = ROOT / "assets" / "backgrounds"

BLEU   = "#4E9FE0"      # bleu ciel des dessins / accents (style des stories du compte)
BLEUF  = "#2F7EC4"      # bleu un peu plus soutenu pour les mots dans le texte noir
NOIR   = "#141414"
BLANC  = "#ffffff"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font_face(family, file, weight):
    data = b64(FONTS / file, "font/woff2")
    return (f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")

FONT_FACES = "".join([
    font_face("Montserrat", "montserrat-latin-500-normal.woff2", 500),
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
  background:#777;font-family:'Playfair',serif;}}
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:center;}}
.pad{{position:absolute;inset:0;padding:280px 84px 380px;z-index:2;display:flex;
  flex-direction:column;}}

.serif{{font-family:'Playfair',serif;font-weight:800;color:{BLANC};
  text-shadow:0 2px 22px rgba(0,0,0,0.45), 0 1px 4px rgba(0,0,0,0.35);}}
.serif .b{{color:{BLEU};}}
.t1{{font-size:82px;line-height:1.14;}}
.t2{{font-size:64px;line-height:1.18;}}

.veil{{background:rgba(255,255,255,0.68);border-radius:24px;padding:44px 42px;
  backdrop-filter:blur(7px);box-shadow:0 14px 44px rgba(0,0,0,0.18);}}
.veil .li{{font-family:'Montserrat',sans-serif;font-weight:700;font-size:31px;
  line-height:1.4;color:{NOIR};margin-bottom:22px;}}
.veil .li:last-child{{margin-bottom:0;}}
.veil .li .b{{color:{BLEUF};}}
.veil .li .tiret{{font-weight:800;margin-right:8px;}}

.hand{{font-family:'Caveat',cursive;font-weight:600;color:{BLANC};
  text-shadow:0 2px 14px rgba(0,0,0,0.5);}}

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

def underline(width=430, color=BLEU, x=0, y=0, cls="abs"):
    """Soulignement ondule dessine a la main."""
    w = width
    path = f"M 8 11 C {w*0.22:.0f} 3, {w*0.4:.0f} 15, {w*0.58:.0f} 9 S {w*0.85:.0f} 5, {w-8:.0f} 10"
    return (f'<svg class="{cls}" style="left:{x}px;top:{y}px;" width="{w}" height="20" '
            f'viewBox="0 0 {w} 20" fill="none"><path d="{path}" stroke="{color}" '
            f'stroke-width="8" stroke-linecap="round"/></svg>')

def arrow_down(x, y, w=240, h=330, color=BLEU, flip=False):
    """Fleche courbe dessinee a la main qui pointe vers le bas."""
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

# ---------------------------------------------------------------- les 5 stories

def story_sondage():
    return (open_story("bg_ciel_dore") + '<div class="pad">'
            f'<div class="serif t1" style="margin-top:40px;">Ta plus grosse {acc("galère")}<br>'
            'en ce moment&nbsp;?</div>'
            + underline(470, BLANC, x=88, y=610)
            + f'<div class="hand" style="font-size:52px;position:absolute;left:150px;top:700px;">'
            'conciergerie ou sous-location,</div>'
            f'<div class="hand" style="font-size:52px;position:absolute;left:150px;top:762px;">'
            'vote juste en dessous</div>'
            + arrow_down(560, 830, 240, 330, BLANC)
            + '</div></div>')

def story_reactions():
    lis = [
        (f'La {acc("moquerie")}', "si c'est moins que ce qu'ils imaginaient."),
        (f'La {acc("jalousie")}', "si c'est plus qu'eux."),
        (f'L\'{acc("attente")}', "tu gagnes bien, donc tu peux payer."),
        (f'Le {acc("calcul")}', "comment en récupérer un bout&nbsp;?"),
    ]
    lines = "".join(f'<div class="li"><span class="tiret">-</span>{h}&nbsp;: {t}</div>'
                    for h, t in lis)
    return (open_story("bg_salon_cosy") + '<div class="pad">'
            f'<div class="serif t2">Tu dis {acc("combien tu gagnes")}&nbsp;?<br>'
            '4 réactions, toujours&nbsp;:</div>'
            f'<div class="veil" style="margin-top:54px;">{lines}</div>'
            f'<div class="serif" style="font-size:46px;margin-top:56px;">'
            'Sébastien les a toutes vécues<br>en 26 ans d\'entrepreneuriat.</div>'
            + underline(390, BLEU, x=88, y=1345)
            + f'<div class="hand" style="font-size:48px;position:absolute;right:90px;top:1390px;">'
            'la parade en vidéo, lien plus haut</div>'
            + '</div></div>')

def story_argumentaire():
    return (open_story("bg_prairie") + '<div class="pad">'
            f'<div class="serif t2" style="margin-top:20px;">Ce qui fait {acc("signer")}<br>'
            f'{acc("un proprio")} au<br>1er rendez-vous.</div>'
            + arrow_down(700, 560, 220, 300, BLANC, flip=True)
            + f'<div class="serif" style="font-size:56px;position:absolute;left:88px;top:920px;">'
            'Réponds</div>'
            f'<div class="serif" style="font-size:88px;position:absolute;left:88px;top:990px;">'
            f'«&nbsp;{acc("ARGUMENTAIRE")}&nbsp;»</div>'
            + underline(640, BLANC, x=110, y=1120)
            + f'<div class="hand" style="font-size:54px;position:absolute;left:340px;top:1170px;">'
            'et on te l\'envoie en DM</div>'
            + '</div></div>')

def story_parcours():
    lis = [
        (f'{acc("40 ans")}', "dépôt de bilan, retour à zéro."),
        (f'{acc("11 ans")}', "de conciergerie et de sous-location."),
        (f'{acc("3 000 élèves")}', "accompagnés aujourd'hui."),
    ]
    lines = "".join(f'<div class="li"><span class="tiret">-</span>{h}&nbsp;: {t}</div>'
                    for h, t in lis)
    return (open_story("bg_chemin_aube") + '<div class="pad">'
            f'<div class="serif t1" style="margin-top:30px;">Ils voient le résultat.<br>'
            f'Jamais le {acc("chemin")}.</div>'
            f'<div class="veil" style="margin-top:64px;">{lines}</div>'
            + f'<div class="hand" style="font-size:56px;position:absolute;left:520px;top:1300px;">'
            'et toi, tu en es où&nbsp;?</div>'
            + underline(300, BLANC, x=560, y=1370)
            + '</div></div>')

def story_result_template():
    return (open_story("bg_ciel_dore") + '<div class="pad">'
            f'<div class="serif" style="font-size:76px;text-align:right;margin-top:10px;">'
            f'+&nbsp;1 pour {acc("[Prénom]")}</div>'
            + arrow_down(680, 480, 230, 300, BLANC)
            + '<div class="abs" style="left:120px;top:640px;width:520px;height:680px;'
            'border:5px dashed rgba(255,255,255,0.75);border-radius:26px;"></div>'
            f'<div class="hand" style="font-size:50px;position:absolute;left:180px;top:930px;'
            'color:rgba(255,255,255,0.95);">colle le screenshot<br>de l\'élève ici</div>'
            f'<div class="hand" style="font-size:62px;position:absolute;right:100px;top:1400px;">'
            'Bravo [Prénom]&nbsp;!</div>'
            + '</div></div>')

SLUG = "semaine-01-v2"
STORIES = {
    "v2_lundi_02_sondage": story_sondage(),
    "v2_lundi_05_reactions": story_reactions(),
    "v2_mardi_04_argumentaire": story_argumentaire(),
    "v2_mercredi_02_parcours": story_parcours(),
    "v2_jeudi_result_template": story_result_template(),
}

DASHES = "—–‒―⎯﹣－─"
def main():
    out = ROOT / "output" / SLUG / "html"
    out.mkdir(parents=True, exist_ok=True)
    td = 0
    for name, body in STORIES.items():
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body>{body}</body></html>'
        d = [c for c in html if c in DASHES]
        if d: print(f"  ALERTE tiret {name}: {set(d)}"); td += len(d)
        (out / f"{name}.html").write_text(html, encoding="utf-8")
    print(f"{len(STORIES)} stories V2 ecrites dans {out}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
