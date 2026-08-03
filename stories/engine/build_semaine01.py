#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construit les visuels de stories de la SEMAINE 01 (HTML 1080x1920).
Charte Le Sous Loueur (navy/orange/bleu, Montserrat), fonds generes par Gemini
(stories/assets/backgrounds/, voir gen_background.py).
Rendu ensuite via render_stories.py.

Seules les stories "texte sur fond" sont generees ici : les faces camera, captures
et screenshots restent a filmer/faire par Martin (voir le fichier semaine).
Les stickers Instagram (sondage, question, lien...) s'ajoutent DANS l'app au
moment de poster : les visuels laissent la place prevue.
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]           # stories/
REPO = ROOT.parents[0]                                        # CARROUSSEL-/
FONTS = REPO / "pipeline" / "assets" / "fonts"
BGS = ROOT / "assets" / "backgrounds"

NAVY   = "#0d1b2e"
ORANGE = "#E8561F"
BLUE   = "#2086C8"
WHITE  = "#ffffff"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font_face(weight):
    data = b64(FONTS / f"montserrat-latin-{weight}-normal.woff2", "font/woff2")
    return (f"@font-face{{font-family:'Montserrat';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")
FONT_FACES = "".join(font_face(w) for w in (400, 500, 600, 700, 800, 900))

# Zones libres pour l'interface Instagram et les stickers :
# haut ~240px (profil, croix) et bas ~360px (barre de reponse) sans texte.
COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
   -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
.story{{width:1080px;height:1920px;position:relative;overflow:hidden;color:{WHITE};background:{NAVY};}}
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:center;}}
.veil{{position:absolute;inset:0;background:
  linear-gradient(180deg, rgba(13,27,46,0.78) 0%, rgba(13,27,46,0.42) 42%, rgba(13,27,46,0.80) 100%);}}
.topbar{{position:absolute;top:0;left:0;right:0;height:6px;
  background:linear-gradient(90deg,{BLUE} 0%,#5fa0d0 50%,{ORANGE} 100%);z-index:5;}}
.pad{{position:absolute;inset:0;padding:250px 92px 370px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;}}
.pad.top{{justify-content:flex-start;padding-top:330px;}}
.kicker{{color:{ORANGE};font-weight:800;font-size:31px;letter-spacing:6px;
  text-transform:uppercase;margin-bottom:36px;text-shadow:0 2px 18px rgba(0,0,0,0.5);}}
.title{{font-weight:900;font-size:66px;line-height:1.12;letter-spacing:-1px;
  text-shadow:0 3px 26px rgba(0,0,0,0.55);}}
.sub{{color:rgba(255,255,255,0.94);font-weight:500;font-size:35px;line-height:1.42;
  margin-top:38px;text-shadow:0 2px 18px rgba(0,0,0,0.55);}}
.list{{display:flex;flex-direction:column;gap:26px;margin-top:44px;}}
.li{{font-weight:800;font-size:44px;line-height:1.15;text-shadow:0 2px 18px rgba(0,0,0,0.5);}}
.li .ar{{color:{ORANGE};font-weight:900;margin-right:16px;}}
.quote{{font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-0.5px;
  text-shadow:0 3px 26px rgba(0,0,0,0.55);}}
.quote .qm{{color:{ORANGE};font-weight:900;}}
.ctatop{{font-weight:800;font-size:47px;line-height:1.22;text-align:center;
  text-shadow:0 3px 24px rgba(0,0,0,0.55);}}
.card{{background:{WHITE};border-radius:26px;padding:46px 40px;margin:52px auto 0;
  width:100%;max-width:850px;text-align:center;box-shadow:0 18px 60px rgba(0,0,0,0.45);}}
.card .lbl{{color:{NAVY};font-weight:800;font-size:33px;letter-spacing:3px;}}
.card .kw{{color:{NAVY};font-weight:900;line-height:1.05;margin-top:10px;letter-spacing:2px;}}
.ctabottom{{color:{ORANGE};font-weight:600;font-style:italic;font-size:31px;line-height:1.4;
  text-align:center;margin-top:42px;text-shadow:0 2px 16px rgba(0,0,0,0.6);}}
"""

def acc(w):
    return f'<span style="color:{ORANGE};">{w}</span>'

def nb(text):
    """Typographie FR : espace insecable avant ? ! : ; et dans les guillemets."""
    if not text:
        return text
    for p in ("?", "!", ":", ";"):
        text = text.replace(f" {p}", f"&nbsp;{p}")
    return text.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")

def open_story(bg):
    img = b64(BGS / f"{bg}.jpg", "image/jpeg")
    return (f'<div class="story"><div class="bgimg" style="background-image:url({img});"></div>'
            f'<div class="veil"></div><div class="topbar"></div>')

def basic(bg, kicker, title, sub=None, items=None, top=False):
    body = open_story(bg) + f'<div class="pad{" top" if top else ""}">'
    if kicker: body += f'<div class="kicker">{nb(kicker)}</div>'
    body += f'<div class="title">{nb(title)}</div>'
    if items:
        body += '<div class="list">' + "".join(
            f'<div class="li"><span class="ar">→</span>{nb(i)}</div>' for i in items) + '</div>'
    if sub: body += f'<div class="sub">{nb(sub)}</div>'
    return body + '</div></div>'

def quote(bg, text, sub=None, top=False):
    body = open_story(bg) + f'<div class="pad{" top" if top else ""}">'
    body += f'<div class="quote"><span class="qm">«</span>&nbsp;{nb(text)}&nbsp;<span class="qm">»</span></div>'
    if sub: body += f'<div class="sub">{nb(sub)}</div>'
    return body + '</div></div>'

def cta(bg, toptext, keyword, bottom):
    size = 66 if len(keyword) >= 12 else (82 if len(keyword) >= 8 else 120)
    return (open_story(bg) + '<div class="pad">'
            f'<div class="ctatop">{nb(toptext)}</div>'
            f'<div class="card"><div class="lbl">RÉPONDS</div>'
            f'<div class="kw" style="font-size:{size}px;">{keyword}</div></div>'
            f'<div class="ctabottom">{nb(bottom)}</div>'
            '</div></div>')

SLUG = "semaine-01"
STORIES = {
    # ---- LUNDI : diagnostic + recyclage video du dimanche (parler d'argent)
    "lundi_02_sondage": basic("bg_navy", "Question du lundi",
        f'Et en ce moment, ta plus grosse {acc("galère")}, c\'est quoi ?',
        sub="Vote juste en dessous.", top=True),
    "lundi_03_questions": basic("bg_conversation", "On répond à tout le monde",
        f'Raconte ta {acc("situation")} en une phrase.', top=True),
    "lundi_05_reactions": basic("bg_mindset", "Parler d'argent",
        f'Quand tu dis {acc("combien tu gagnes")}, il n\'y a que 4 réactions possibles :',
        items=["La moquerie", "La jalousie", "L'attente", "Le calcul"],
        sub="Sébastien les a toutes vécues en 26 ans d'entrepreneuriat."),
    "lundi_06_citation": quote("bg_mindset",
        f'Les gens voient ton {acc("résultat")}. Ils ne voient jamais ton {acc("chemin")}.',
        sub="La 7e chose à ne jamais dire est la plus contre-intuitive. La vidéo complète est juste là :",
        top=True),
    # ---- MARDI : conseil terrain rendez-vous proprietaire
    "mardi_02_erreur": basic("bg_immobilier", "Rendez-vous propriétaire",
        f'L\'erreur : arriver et {acc("dérouler")}. Tes services, tes tarifs, ton fonctionnement.',
        sub="Le propriétaire, lui, se pose une seule question : son logement est-il entre de bonnes mains."),
    "mardi_03_conseil": basic("bg_immobilier", "Fais l'inverse",
        f'{acc("Écoute")} d\'abord. Vends {acc("après")}.',
        sub="Ses locataires actuels, ses galères, ce qui l'empêche de dormir.", top=True),
    "mardi_04_argumentaire": cta("bg_immobilier",
        "Les arguments qui font signer un propriétaire dès le premier rendez-vous.",
        "ARGUMENTAIRE", "On te l'envoie en message."),
    # ---- MERCREDI : parcours + question
    "mercredi_02_parcours": basic("bg_mindset", "Le chemin",
        f'À 40 ans : {acc("dépôt de bilan")}. Retombé à zéro.',
        sub="Aujourd'hui : 11 ans de conciergerie et de sous-location, plus de 3 000 élèves accompagnés."),
    "mercredi_03_question": basic("bg_conversation", "Et toi ?",
        f'Tu en es où de ton {acc("chemin")} ?', sub="Raconte, on lit tout.", top=True),
    # ---- JEUDI : CTA GO
    "jeudi_04_go": cta("bg_conversation",
        "Tu veux qu'on échange ensemble sur ton projet ?",
        "GO", "On fait le point ensemble, tout simplement."),
    # ---- VENDREDI : CTA SIMULATEUR
    "vendredi_03_simulateur": cta("bg_navy",
        "L'outil qu'on utilise avec nos élèves avant chaque signature.",
        "SIMULATEUR", "On te l'envoie en message."),
    # ---- SAMEDI : radar + rappel GO
    "samedi_01_radar": basic("bg_conversation", "Le point du samedi",
        f'Tu en es {acc("où")} dans ton projet aujourd\'hui ?',
        sub="Réponds en une phrase. On lit tout.", top=True),
    "samedi_03_go": cta("bg_navy", "Si tu veux avancer plus vite :",
        "GO", "On fait le point sur ton projet ensemble."),
    # ---- DIMANCHE : teaser + apres la video
    "dimanche_01_teaser": basic("bg_mindset", "Ce soir, 18h",
        f'Nouvelle {acc("vidéo")} sur la chaîne.', sub="Reste dans le coin.", top=True),
    "dimanche_03_avis": basic("bg_conversation", "Tu l'as vue ?",
        f'Dis-moi ce que tu en {acc("retiens")}.', sub="Réponds à cette story."),
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
    print(f"{len(STORIES)} stories HTML ecrites dans {out}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
