#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur de carrousels Le Sous Loueur (charte navy/orange/bleu, PARTIE C1 de carroussel.md).
Meme structure que build_guestlucky.py, charte differente.
Rendu via render.py (identique).
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"
LOGO = ASSETS / "logos" / "lesousloueur_white_temp.png"   # TEMP : version blanche officielle a recevoir

# ---------- Couleurs Le Sous Loueur (exactes) ----------
NAVY   = "#0d1b2e"
ORANGE = "#E8561F"
BLUE   = "#2086C8"
WHITE  = "#ffffff"
RED    = "#ff5a5a"
GREEN  = "#5dd987"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()
LOGO_B64 = b64(LOGO, "image/png")

def font_face(weight):
    data = b64(FONTS / f"montserrat-latin-{weight}-normal.woff2", "font/woff2")
    return (f"@font-face{{font-family:'Montserrat';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")
FONT_FACES = "".join(font_face(w) for w in (400,500,600,700,800,900))

COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
   -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
.slide{{width:1080px;height:1350px;background:{NAVY};position:relative;overflow:hidden;color:{WHITE};}}
.bg{{position:absolute;inset:0;background:
  radial-gradient(115% 75% at 84% -5%, rgba(232,86,31,0.16) 0%, rgba(13,27,46,0) 55%),
  radial-gradient(100% 70% at -5% 105%, rgba(32,134,200,0.16) 0%, rgba(13,27,46,0) 52%),
  {NAVY};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:6px;
  background:linear-gradient(90deg,{BLUE} 0%,#5fa0d0 50%,{ORANGE} 100%);z-index:5;}}
.pad{{position:absolute;inset:0;padding:96px 84px 170px;z-index:2;display:flex;flex-direction:column;}}
.footer{{position:absolute;bottom:50px;left:0;right:0;display:flex;justify-content:center;align-items:center;z-index:6;}}
.footer img{{height:64px;}}
.chevron{{position:absolute;bottom:44px;right:55px;font-size:70px;font-weight:900;color:{ORANGE};line-height:1;z-index:6;}}

.head{{position:relative;min-height:150px;margin-bottom:10px;}}
.title{{color:{BLUE};font-weight:900;font-size:50px;line-height:1.02;letter-spacing:-1.5px;
  text-transform:uppercase;max-width:640px;}}
.num{{position:absolute;top:-26px;right:0;color:{ORANGE};font-weight:900;font-size:150px;
  line-height:0.85;letter-spacing:-6px;}}
.subpill{{display:inline-block;align-self:flex-start;background:{BLUE};color:{WHITE};
  font-weight:700;font-size:22px;padding:14px 26px;border-radius:10px;margin-bottom:38px;}}

.points{{display:flex;flex-direction:column;gap:30px;flex:1;}}
.pl{{color:{ORANGE};font-weight:800;font-size:33px;line-height:1.15;}}
.pl .ar{{color:{ORANGE};font-weight:900;margin-right:10px;}}
.pt{{color:{WHITE};font-weight:500;font-size:27px;line-height:1.35;margin-left:38px;margin-top:6px;opacity:0.93;}}

.info{{display:flex;align-items:stretch;border-radius:12px;overflow:hidden;margin-top:24px;}}
.info .il{{background:{BLUE};color:{WHITE};font-weight:800;font-size:21px;padding:18px 22px;
  display:flex;align-items:center;flex-shrink:0;}}
.info .iv{{background:{WHITE};color:{NAVY};font-weight:700;font-size:21px;padding:18px 24px;
  display:flex;align-items:center;flex-grow:1;line-height:1.3;}}
"""

def slide_open():
    return f'<div class="slide"><div class="bg"></div><div class="topbar"></div>'
def footer(chevron=True):
    ch = f'<div class="chevron">»</div>' if chevron else ''
    return f'<div class="footer"><img src="{LOGO_B64}"/></div>{ch}</div>'
def acc(w, color=ORANGE):
    return f'<span style="color:{color};">{w}</span>'

def cover(eyebrow, title_html, subtitle, bottom):
    return (slide_open() +
      f'<div class="pad" style="justify-content:center;align-items:center;text-align:center;padding:96px 90px 175px;">'
      f'<div style="color:{ORANGE};font-weight:800;font-size:26px;letter-spacing:6px;text-transform:uppercase;margin-bottom:34px;">{eyebrow}</div>'
      f'<div style="font-weight:900;font-size:68px;line-height:1.03;letter-spacing:-2px;text-transform:uppercase;">{title_html}</div>'
      f'<div style="color:{ORANGE};font-weight:800;font-size:28px;text-transform:uppercase;letter-spacing:0.5px;margin-top:34px;max-width:820px;line-height:1.3;">{subtitle}</div>'
      f'<div style="color:rgba(255,255,255,0.85);font-weight:500;font-style:italic;font-size:25px;margin-top:26px;">{bottom}</div>'
      f'</div>' +
      f'<div class="footer" style="bottom:52px;"><img src="{LOGO_B64}" style="height:78px;"/></div>'
      f'<div class="chevron" style="bottom:52px;font-size:78px;">»</div></div>')

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
    arrow = f'<div style="color:{ORANGE};font-weight:900;font-size:60px;align-self:center;padding:0 6px;">→</div>'
    return (slide_open() +
      f'<div class="pad">'
      f'<div class="head"><div class="title">{title_html}</div><div class="num">{num}</div></div>'
      f'<div class="subpill">{subtitle}</div>'
      f'<div class="points" style="flex-direction:row;gap:14px;align-items:stretch;">{av}{arrow}{ap}</div>'
      f'<div class="info"><div class="il">{info_label}</div><div class="iv">{info_value}</div></div>'
      f'</div>' + footer())

def cta(title_html, desc, keyword, value):
    return (slide_open() +
      f'<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
      f'<div style="background:{BLUE};border-radius:14px;padding:26px 34px;margin-bottom:34px;max-width:840px;">'
      f'<div style="font-weight:900;font-size:40px;line-height:1.1;text-transform:uppercase;">{title_html}</div></div>'
      f'<div style="color:rgba(255,255,255,0.9);font-weight:500;font-size:26px;line-height:1.4;margin-bottom:38px;max-width:760px;">{desc}</div>'
      f'<div style="background:{WHITE};border-radius:22px;padding:40px 36px;width:100%;max-width:840px;">'
      f'<div style="color:{NAVY};font-weight:800;font-size:32px;letter-spacing:2px;">COMMENTE</div>'
      f'<div style="color:{NAVY};font-weight:900;font-size:74px;letter-spacing:3px;line-height:1;margin-top:8px;">"{keyword}"</div>'
      f'</div>'
      f'<div style="color:{ORANGE};font-weight:600;font-style:italic;font-size:27px;line-height:1.4;margin-top:30px;max-width:760px;">{value}</div>'
      f'</div>' + footer())

def closing(message_html):
    ig = ('<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" '
          'stroke-linecap="round" stroke-linejoin="round">{p}</svg>')
    heart = ig.format(p='<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>')
    chat = ig.format(p='<path d="M21 11.5a8.4 8.4 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/>')
    send = ig.format(p='<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>')
    save = ig.format(p='<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>')
    return (slide_open() +
      f'<div class="pad" style="justify-content:center;align-items:center;text-align:center;padding-bottom:210px;">'
      f'<div style="color:{BLUE};font-weight:800;font-size:24px;letter-spacing:5px;text-transform:uppercase;margin-bottom:26px;">Rejoignez-nous sur</div>'
      f'<div style="font-weight:900;font-size:52px;letter-spacing:-0.5px;">WWW.LESOUSLOUEUR.FR</div>'
      f'<div style="width:80px;height:3px;background:{ORANGE};margin:34px 0;"></div>'
      f'<div style="color:#fff;font-weight:500;font-size:30px;line-height:1.4;max-width:800px;">{message_html}</div>'
      f'<div style="display:flex;gap:38px;align-items:center;margin-top:44px;background:{ORANGE};padding:22px 46px;border-radius:60px;">{heart}{chat}{send}{save}</div>'
      f'</div>' +
      f'<div class="footer" style="bottom:56px;"><img src="{LOGO_B64}" style="height:78px;"/></div></div>')

SLUG = "lsl_demo_relation_voyageurs"
SLIDES = [
  cover("Le Sous Loueur",
        f'Arrête de répondre à<br>tes voyageurs {acc("à 2h du matin")}',
        "La méthode pour automatiser ta relation voyageurs",
        "11 ans de terrain, plus de 3 000 élèves accompagnés."),

  content(1, "Le vrai<br>coût", "Ce que la gestion manuelle te prend vraiment",
    [("Ton temps","Tu passes tes soirées le téléphone à la main."),
     ("Ta tranquillité","Tu n'es jamais vraiment en week-end, ni en vacances."),
     ("Tes notes","Une réponse trop lente et le voyageur te sanctionne."),
     ("Ta croissance","Impossible de prendre plus de logements en gérant comme ça.")],
    "À retenir", "Gérer à la main, c'est un plafond de verre déguisé."),

  content(2, "Répondre<br>vite", "La rapidité, ton meilleur atout",
    [("Les cinq premières minutes","Un voyageur qui attend, c'est une note qui baisse."),
     ("Les questions récurrentes","La plupart des messages sont toujours les mêmes."),
     ("Des réponses prêtes","Un modèle pour chaque situation, sous la main."),
     ("Rester humain","Un message rapide mais qui sonne vrai, jamais robotique.")],
    "À retenir", "La vitesse de réponse pèse lourd dans ton classement."),

  content(3, "Les<br>modèles", "Tes messages types, une fois pour toutes",
    [("Le message de bienvenue","Envoyé dès que la réservation est confirmée."),
     ("Les instructions d'arrivée","Adresse, code, wifi, au bon moment."),
     ("Le rappel de départ","Les consignes de check-out, sans que tu y penses."),
     ("La demande d'avis","Le message qui fait grimper ta réputation.")],
    "À retenir", "Écris-les une fois, ils travaillent pour toi ensuite."),

  content(4, "L'auto<br>matisation", "Laisse les outils bosser à ta place",
    [("Les déclencheurs","Réservation, arrivée, départ : chaque étape part seule."),
     ("La caution","Demandée automatiquement, au bon moment du séjour."),
     ("Le multilingue","L'outil traduit pour toi, tu ne bloques plus jamais."),
     ("Le suivi","Tu vois d'un coup d'oeil ce qui est parti ou non.")],
    "À retenir", "Un bon outil transforme ta charge mentale en système."),

  content_ba(5, "Avant<br>après", "Ce que ça change dans ta vie",
    "Tu réponds toi-même, jour et nuit, la boule au ventre.",
    "Tes messages partent seuls, tu gardes le contrôle sans l'esclavage.",
    "À retenir", "Tu redeviens chef d'entreprise, plus jamais standardiste."),

  content(6, "L'effet<br>levier", "Pourquoi ça change vraiment ton activité",
    [("Plus de logements","Tu gères le double sans y passer plus d'heures."),
     ("Meilleures notes","La régularité fait grimper ta réputation."),
     ("Moins de stress","Ton téléphone arrête de commander ta vie."),
     ("Plus de marge","Le temps gagné, tu le remets sur la prospection.")],
    "À retenir", "Automatiser, c'est le premier vrai pas pour passer à l'échelle."),

  content(7, "Par où<br>commencer", "Trois actions dès cette semaine",
    [("Liste tes messages types","Repère les cinq que tu envoies le plus souvent."),
     ("Choisis ton outil","Une messagerie et des scénarios automatiques."),
     ("Mets en place trois automatismes","Bienvenue, arrivée, demande d'avis.")],
    "À retenir", "En un après-midi, ta relation voyageurs tourne déjà seule."),

  cta("Envie d'un système qui tourne sans toi ?",
      "Je te montre comment tout mettre en place, étape par étape.",
      "CONCIERGERIE",
      "et je t'offre l'accès à mon atelier gratuit de 2h."),

  closing("11 ans de terrain pour t'aider à vraiment vivre de la conciergerie."),
]

DASHES = "—–‒―⎯﹣－─"
def main():
    out = ROOT / "output" / SLUG
    html_dir = out / "html"; html_dir.mkdir(parents=True, exist_ok=True)
    td = 0
    for i, body in enumerate(SLIDES, 1):
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body>{body}</body></html>'
        d = [c for c in html if c in DASHES]
        if d: print(f"  ALERTE tiret slide {i}: {set(d)}"); td += len(d)
        (html_dir / f"slide_{i:02d}.html").write_text(html, encoding="utf-8")
    print(f"{len(SLIDES)} slides HTML ecrites. Tirets longs: {td}")

if __name__ == "__main__":
    main()
