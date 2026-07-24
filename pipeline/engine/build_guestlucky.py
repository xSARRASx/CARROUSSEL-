#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur de carrousels Guestlucky (charte violet/rose, PARTIE C2 de carroussel.md).
Genere 10 slides HTML puis les rend en PNG HD + JPEG Metricool-ready via Playwright.

Usage : python3 build_guestlucky.py
Sortie : pipeline/output/<slug>/  (html/, PNG 3240x4050, JPEG 1080x1350)
"""
import base64, os, re, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]          # pipeline/
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"
LOGO = ASSETS / "logos" / "guestlucky.png"

# ---------- Couleurs Guestlucky (exactes) ----------
NAVY   = "#0a0e27"
VIOLET = "#7c3aed"
VIOLET_D = "#5b21b6"
ROSE   = "#ec4899"
WHITE  = "#ffffff"
RED    = "#ff5a5a"
GREEN  = "#5dd987"

# ---------- Assets en base64 ----------
def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

LOGO_B64 = b64(LOGO, "image/png")

def font_face(weight):
    data = b64(FONTS / f"montserrat-latin-{weight}-normal.woff2", "font/woff2")
    return (f"@font-face{{font-family:'Montserrat';font-style:normal;"
            f"font-weight:{weight};font-display:block;src:url({data}) format('woff2');}}")

FONT_FACES = "".join(font_face(w) for w in (400,500,600,700,800,900))

# ---------- CSS commun ----------
COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
   -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
.slide{{width:1080px;height:1350px;background:{NAVY};position:relative;overflow:hidden;color:{WHITE};}}
.bg{{position:absolute;inset:0;background:
  radial-gradient(115% 75% at 82% -5%, rgba(124,58,237,0.20) 0%, rgba(10,14,39,0) 55%),
  radial-gradient(100% 70% at -5% 105%, rgba(236,72,153,0.13) 0%, rgba(10,14,39,0) 52%),
  {NAVY};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:6px;
  background:linear-gradient(90deg,{VIOLET} 0%,{ROSE} 100%);z-index:5;}}
.pad{{position:absolute;inset:0;padding:96px 84px 170px;z-index:2;display:flex;flex-direction:column;}}
.footer{{position:absolute;bottom:50px;left:0;right:0;display:flex;justify-content:center;align-items:center;z-index:6;}}
.footer img{{height:64px;}}
.chevron{{position:absolute;bottom:46px;right:55px;font-size:72px;font-weight:900;color:{VIOLET};line-height:1;z-index:6;}}

/* header slides contenu */
.head{{position:relative;min-height:150px;margin-bottom:10px;}}
.title{{color:{VIOLET};font-weight:800;font-size:42px;line-height:1.02;letter-spacing:-1px;
  text-transform:uppercase;max-width:660px;}}
.num{{position:absolute;top:-24px;right:0;color:{VIOLET};font-weight:900;font-size:150px;
  line-height:0.85;letter-spacing:-6px;opacity:0.95;}}
.subpill{{display:inline-block;align-self:flex-start;background:{VIOLET};color:{WHITE};
  font-weight:700;font-size:22px;padding:14px 28px;border-radius:10px;margin-bottom:38px;}}

.points{{display:flex;flex-direction:column;gap:30px;flex:1;}}
.pl{{color:{VIOLET};font-weight:800;font-size:33px;line-height:1.15;}}
.pl .ar{{color:{ROSE};font-weight:900;margin-right:10px;}}
.pt{{color:{WHITE};font-weight:400;font-size:27px;line-height:1.35;margin-left:38px;margin-top:6px;opacity:0.92;}}

.info{{display:flex;align-items:stretch;border-radius:12px;overflow:hidden;margin-top:24px;}}
.info .il{{background:{VIOLET};color:{WHITE};font-weight:800;font-size:21px;padding:18px 22px;
  display:flex;align-items:center;flex-shrink:0;}}
.info .iv{{background:{WHITE};color:{NAVY};font-weight:700;font-size:21px;padding:18px 24px;
  display:flex;align-items:center;flex-grow:1;line-height:1.3;}}
"""

# ---------- Gabarits ----------
def slide_open():
    return f'<div class="slide"><div class="bg"></div><div class="topbar"></div>'

def footer(chevron=True):
    ch = f'<div class="chevron">»</div>' if chevron else ''
    return f'<div class="footer"><img src="{LOGO_B64}"/></div>{ch}</div>'

def cover(eyebrow, title_html, subtitle):
    return (slide_open() +
      f'<div class="pad" style="justify-content:center;align-items:center;text-align:center;padding:96px 90px 170px;">'
      f'<div style="color:{ROSE};font-weight:800;font-size:26px;letter-spacing:6px;text-transform:uppercase;margin-bottom:34px;">{eyebrow}</div>'
      f'<div style="font-weight:900;font-size:70px;line-height:1.04;letter-spacing:-2px;text-transform:uppercase;">{title_html}</div>'
      f'<div style="width:80px;height:3px;background:{ROSE};margin:40px 0;"></div>'
      f'<div style="color:rgba(255,255,255,0.82);font-weight:500;font-size:30px;line-height:1.4;max-width:820px;">{subtitle}</div>'
      f'</div>' +
      f'<div class="footer" style="bottom:56px;"><img src="{LOGO_B64}" style="height:80px;"/></div></div>')

def content(num, title_html, subtitle, points, info_label, info_value):
    pts = ""
    for label, text in points:
        pts += f'<div><div class="pl"><span class="ar">→</span>{label}</div><div class="pt">{text}</div></div>'
    return (slide_open() +
      f'<div class="pad">'
      f'<div class="head"><div class="title">{title_html}</div><div class="num">{num}</div></div>'
      f'<div class="subpill">{subtitle}</div>'
      f'<div class="points">{pts}</div>'
      f'<div class="info"><div class="il">{info_label}</div><div class="iv">{info_value}</div></div>'
      f'</div>' + footer())

def content_ba(num, title_html, subtitle, avant, apres, info_label, info_value):
    card = ('<div style="flex:1;border-radius:16px;padding:34px 30px;border:2px solid {bd};background:{bg};">'
            '<div style="color:{bd};font-weight:900;font-size:26px;text-transform:uppercase;letter-spacing:1px;margin-bottom:18px;">{h}</div>'
            '<div style="color:#fff;font-weight:500;font-size:27px;line-height:1.4;opacity:0.95;">{t}</div></div>')
    av = card.format(bd=RED, bg="rgba(255,90,90,0.10)", h="Avant", t=avant)
    ap = card.format(bd=GREEN, bg="rgba(93,217,135,0.10)", h="Après", t=apres)
    arrow = f'<div style="color:{VIOLET};font-weight:900;font-size:60px;align-self:center;padding:0 6px;">→</div>'
    return (slide_open() +
      f'<div class="pad">'
      f'<div class="head"><div class="title">{title_html}</div><div class="num">{num}</div></div>'
      f'<div class="subpill">{subtitle}</div>'
      f'<div class="points" style="flex-direction:row;gap:14px;align-items:stretch;">{av}{arrow}{ap}</div>'
      f'<div class="info"><div class="il">{info_label}</div><div class="iv">{info_value}</div></div>'
      f'</div>' + footer())

def cta(eyebrow, title_html, keyword, value):
    return (slide_open() +
      f'<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
      f'<div style="color:{ROSE};font-weight:800;font-size:24px;letter-spacing:6px;text-transform:uppercase;margin-bottom:30px;">{eyebrow}</div>'
      f'<div style="font-weight:900;font-size:52px;line-height:1.08;margin-bottom:46px;max-width:840px;">{title_html}</div>'
      f'<div style="background:{WHITE};border-radius:22px;padding:44px 40px;width:100%;max-width:820px;">'
      f'<div style="color:{NAVY};font-weight:800;font-size:34px;letter-spacing:2px;">COMMENTE</div>'
      f'<div style="color:{VIOLET};font-weight:900;font-size:118px;letter-spacing:6px;line-height:1;margin-top:8px;">{keyword}</div>'
      f'</div>'
      f'<div style="color:rgba(255,255,255,0.85);font-weight:500;font-size:27px;line-height:1.4;margin-top:34px;max-width:760px;">{value}</div>'
      f'<div style="color:{VIOLET};font-weight:900;font-size:54px;margin-top:18px;">↓</div>'
      f'</div>' + footer())

def closing(message_html):
    ig = ('<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" '
          'stroke-linecap="round" stroke-linejoin="round">{p}</svg>')
    heart = ig.format(p='<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>')
    chat = ig.format(p='<path d="M21 11.5a8.4 8.4 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/>')
    send = ig.format(p='<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>')
    save = ig.format(p='<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>')
    icons = ("".join([heart,chat,send,save]))
    return (slide_open() +
      f'<div class="pad" style="justify-content:center;align-items:center;text-align:center;padding-bottom:210px;">'
      f'<div style="color:{ROSE};font-weight:800;font-size:24px;letter-spacing:5px;text-transform:uppercase;margin-bottom:26px;">Rejoignez-nous sur</div>'
      f'<div style="font-weight:900;font-size:64px;letter-spacing:-1px;">guestlucky.com</div>'
      f'<div style="width:80px;height:3px;background:{VIOLET};margin:34px 0;"></div>'
      f'<div style="color:#fff;font-weight:500;font-size:31px;line-height:1.4;max-width:780px;">{message_html}</div>'
      f'<div style="display:flex;gap:38px;align-items:center;margin-top:44px;'
      f'background:linear-gradient(90deg,{VIOLET},{ROSE});padding:22px 44px;border-radius:60px;">{icons}</div>'
      f'</div>' +
      f'<div class="footer" style="bottom:56px;"><img src="{LOGO_B64}" style="height:80px;"/></div></div>')

def acc(word, color=VIOLET):
    return f'<span style="color:{color};">{word}</span>'

# ---------- CONTENU DU CARROUSEL (demo Guestlucky) ----------
SLUG = "gl_demo_messagerie_ia"

SLIDES = [
  cover("Guestlucky · Messagerie IA",
        f'Réponds à tes voyageurs {acc("24h/24",VIOLET)}<br>sans y passer {acc("tes nuits",ROSE)}',
        "L'intelligence artificielle qui gère la majorité de tes messages pendant que tu dors, formée sur tes propres annonces."),

  content(1, "Le vrai<br>problème", "Ce qui te bouffe le plus de temps",
    [("Les mêmes questions","Wifi, heure d'arrivée, parking : tu réponds trente fois la même chose."),
     ("Les messages la nuit","Un voyageur écrit à 2h du matin et il veut une réponse tout de suite."),
     ("Le multilingue","Un Italien, un Allemand et un Espagnol le même jour."),
     ("La charge mentale","Ton téléphone sonne en continu, même quand tu es en vacances.")],
    "À retenir", "Répondre vite améliore tes notes, mais ça finit par t'épuiser."),

  content(2, "L'IA<br>messagerie", "Une messagerie qui répond à ta place",
    [("Formée sur tes annonces","Elle connaît ton logement, tes règles et tes équipements."),
     ("Disponible 24h/24","Elle ne dort jamais et répond en quelques secondes."),
     ("Multilingue","Elle répond dans la langue du voyageur, automatiquement."),
     ("OpenAI ou Google Gemini","Tu choisis le moteur d'intelligence artificielle (IA).")],
    "À retenir", "Le voyageur a sa réponse tout de suite, et toi tu dors tranquille."),

  content(3, "Les Auto<br>Actions", "Des scénarios qui se déclenchent seuls",
    [("Dix déclencheurs","Nouvelle réservation, arrivée proche, message reçu, et plus encore."),
     ("Quatorze conditions","Tu cibles un logement, un canal de vente ou un type de séjour."),
     ("Neuf actions empilables","Envoyer un message, poser une étiquette, demander la caution."),
     ("Zéro oubli","Chaque étape part au bon moment, sans que tu y penses.")],
    "À retenir", "Tu construis le scénario une fois, il tourne ensuite pour toujours."),

  content(4, "Les<br>templates", "Tes messages types, prêts à l'emploi",
    [("Variables auto-remplies","Le prénom, la date d'arrivée et le code d'accès s'insèrent seuls."),
     ("Toujours personnalisé","Chaque voyageur reçoit un message qui lui parle vraiment."),
     ("Gain de temps","Fini le copier-coller, tout est déjà prêt à partir."),
     ("Cohérence","Le même niveau de qualité sur tous tes logements.")],
    "À retenir", "Un message qui a l'air écrit à la main, envoyé en un seul clic."),

  content_ba(5, "Avant<br>après", "Ce que ça change concrètement",
    "Tu réponds toi-même, jour et nuit, dans plusieurs langues, sans répit.",
    "L'IA gère la majorité des messages, tu gardes ceux qui comptent vraiment.",
    "À retenir", "Tu passes de standardiste à chef d'orchestre de ta conciergerie."),

  content(6, "Pourquoi<br>ça compte", "L'impact réel sur ton activité",
    [("Meilleures notes","Répondre vite fait grimper ta note voyageurs sur les plateformes."),
     ("Plus de logements","Tu gères davantage d'annonces sans avoir à embaucher."),
     ("Moins de stress","Ton téléphone arrête de dicter le rythme de ta vie."),
     ("Plus de réservations","Une bonne note, c'est plus de visibilité, donc plus de séjours.")],
    "À retenir", "Automatiser la messagerie, c'est grandir sans t'épuiser."),

  content(7, "Par où<br>commencer", "Trois réglages pour démarrer aujourd'hui",
    [("Active la messagerie IA","Choisis le moteur et laisse-la apprendre tes annonces."),
     ("Crée trois Auto Actions","Le message de bienvenue, les instructions d'arrivée, la demande d'avis."),
     ("Prépare tes templates","Les réponses aux questions que l'on te pose le plus souvent.")],
    "À retenir", "En un après-midi, ta messagerie tourne déjà toute seule."),

  cta("Action · 1 mot", f'Envie {acc("d’automatiser",VIOLET)}<br>ta messagerie ?', "IA",
      "Commente le mot IA et je t'envoie dix scénarios Auto Actions prêts à copier."),

  closing(f'L\'outil tout-en-un qui répond à tes voyageurs {acc("pendant que tu vis ta vie",VIOLET)}.'),
]

# ---------- Anti tiret long ----------
DASHES = "—–‒―⎯﹣－─"
def check_dashes(html, idx):
    found = [c for c in html if c in DASHES]
    if found:
        print(f"  ALERTE tiret long slide {idx}: {set(found)}")
    return found

# ---------- Ecriture HTML ----------
def main():
    out = ROOT / "output" / SLUG
    html_dir = out / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    total_dash = 0
    for i, body in enumerate(SLIDES, 1):
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{COMMON_CSS}</style></head><body>{body}</body></html>')
        total_dash += len(check_dashes(html, i))
        (html_dir / f"slide_{i:02d}.html").write_text(html, encoding="utf-8")
    print(f"{len(SLIDES)} slides HTML ecrites dans {html_dir}")
    print("Tirets longs trouves :", total_dash)

if __name__ == "__main__":
    main()
