#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
design_v2.py -- Mise en page V2 des carrousels (demande Martin, 27/07/2026).

Objectif : moins de murs de texte, plus de VISUEL. Chaque slide de contenu est
batie autour d'un schema : carte mentale, timeline, flux, comparatif, blocs de
chiffres, checklist, etages, tenaille.

Regles respectees (carroussel.md) :
- Montserrat partout, 1080x1350, logo officiel centre en bas, chevron accent.
- AUCUN emoji, AUCUN tiret long, aucun glow / box-shadow lumineux.
- Pas de petit rond numerote (on utilise des carres arrondis et des chiffres nus).
- Palettes strictes par marque, jamais melangees.

Usage :
    from design_v2 import Deck
    deck = Deck("lesousloueur")                       # ou "guestlucky"
    deck.set_bg_photo("mon_fond.jpg")                 # optionnel
    slides = [deck.cover(...), deck.mindmap(...), ...]
    deck.write("mon_slug", slides)
"""

import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"

DASHES = "—–‒―⎯﹣－─"


def b64(path, mime):
    return "data:%s;base64,%s" % (
        mime, base64.b64encode(pathlib.Path(path).read_bytes()).decode())


def _font_faces():
    out = []
    for w in (400, 500, 600, 700, 800, 900):
        data = b64(FONTS / ("montserrat-latin-%d-normal.woff2" % w), "font/woff2")
        out.append(
            "@font-face{font-family:'Montserrat';font-style:normal;font-weight:%d;"
            "font-display:block;src:url(%s) format('woff2');}" % (w, data))
    return "".join(out)


FONT_FACES = _font_faces()

BRANDS = {
    "guestlucky": {
        "name": "Guestlucky",
        "navy": "#0a0e27", "deep": "#05060f",
        "a1": "#7c3aed",   # violet : accent principal
        "a2": "#ec4899",   # rose : accent secondaire
        "red": "#ff5a5a", "green": "#5dd987",
        "logo": "guestlucky.png",
        "site": "guestlucky.com",
    },
    "lesousloueur": {
        "name": "Le Sous Loueur",
        "navy": "#0d1b2e", "deep": "#081320",
        "a1": "#E8561F",   # orange : accent principal
        "a2": "#2086C8",   # bleu : accent secondaire
        "red": "#ff5a5a", "green": "#5dd987",
        "logo": "lesousloueur_white_temp.png",
        "site": "WWW.LESOUSLOUEUR.FR",
    },
}

# --------------------------------------------------------------------------
# Feuille de style V2 (tokens remplaces par la marque)
# --------------------------------------------------------------------------

CSS_TPL = """
*{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;
  background:{{NAVY}};color:#fff;}

/* fond : degrade sobre, ou photo si fournie */
.bg{position:absolute;inset:0;background:
  radial-gradient(58% 44% at 26% 88%, {{A1}}2e 0%, rgba(0,0,0,0) 62%),
  radial-gradient(52% 40% at 84% 74%, {{A2}}24 0%, rgba(0,0,0,0) 64%),
  linear-gradient(180deg, {{DEEP}} 0%, {{NAVY}} 100%);}
.bg::after{content:"";position:absolute;inset:0;background:
  radial-gradient(84% 80% at 50% 58%, rgba(0,0,0,0) 44%, rgba(0,0,0,0.40) 100%),
  linear-gradient(180deg, rgba(0,0,0,0.30) 0%, rgba(0,0,0,0) 30%);}
.topbar{position:absolute;top:0;left:0;right:0;height:5px;z-index:6;
  background:linear-gradient(90deg,{{A2}} 0%,{{A1}} 100%);}

.pad{position:absolute;inset:0;padding:84px 76px 166px;z-index:2;
  display:flex;flex-direction:column;}

/* en-tete de slide de contenu */
.eyebrow{font-size:21px;font-weight:800;letter-spacing:5px;text-transform:uppercase;
  color:{{A2}};}
.h1{font-size:48px;font-weight:900;line-height:1.02;letter-spacing:-1.4px;
  text-transform:uppercase;margin-top:16px;max-width:780px;}
.h1 em{font-style:normal;color:{{A1}};}
.num{position:absolute;top:78px;right:76px;font-size:118px;font-weight:900;
  line-height:0.78;letter-spacing:-7px;color:{{A1}};}
.rule{width:66px;height:4px;background:{{A1}};margin-top:24px;border-radius:2px;}
.lead{font-size:25px;font-weight:500;line-height:1.4;color:rgba(255,255,255,0.86);
  margin-top:20px;max-width:830px;}
.grow{flex:1;}

/* bandeau de bas de slide */
.foot{display:flex;align-items:stretch;border-radius:12px;overflow:hidden;}
.foot .fl{background:{{A1}};color:#fff;font-weight:800;font-size:20px;
  padding:17px 21px;display:flex;align-items:center;flex-shrink:0;}
.foot .fv{background:#fff;color:{{NAVY}};font-weight:700;font-size:20px;
  padding:17px 23px;display:flex;align-items:center;flex-grow:1;line-height:1.3;}

.logo{position:absolute;bottom:48px;left:0;right:0;display:flex;
  justify-content:center;align-items:center;z-index:6;}
.logo img{height:62px;}
.chev{position:absolute;bottom:44px;right:54px;font-size:68px;font-weight:900;
  line-height:1;color:{{A1}};z-index:6;}

/* ---------- briques visuelles ----------
   .viz occupe TOUT l'espace restant entre l'en-tete et le bandeau du bas :
   les schemas remplissent la slide, aucun grand vide. */
.viz{flex:1;display:flex;flex-direction:column;justify-content:center;
  margin:26px 0 22px;}
.viz.mid{justify-content:center;}

/* carte mentale */
.map{position:relative;width:928px;height:640px;}
.node{position:absolute;border-radius:18px;padding:22px 22px;min-height:150px;
  display:flex;flex-direction:column;justify-content:center;
  border:2px solid rgba(255,255,255,0.18);background:rgba(255,255,255,0.06);}
.node .nl{font-size:29px;font-weight:800;color:{{A1}};line-height:1.12;}
.node .nt{font-size:22px;font-weight:500;line-height:1.34;margin-top:9px;
  color:rgba(255,255,255,0.88);}
.core{position:absolute;left:314px;top:268px;width:300px;height:104px;
  border-radius:18px;display:flex;align-items:center;justify-content:center;
  text-align:center;padding:14px 18px;background:{{A1}};}
.core span{font-size:28px;font-weight:900;line-height:1.14;text-transform:uppercase;
  letter-spacing:-0.3px;}
.wires{position:absolute;inset:0;}

/* timeline verticale */
.tl{position:relative;padding-left:38px;display:flex;flex-direction:column;}
.tl::before{content:"";position:absolute;left:9px;top:10px;bottom:10px;width:3px;
  background:rgba(255,255,255,0.18);}
.tlrow{position:relative;min-height:128px;display:flex;
  flex-direction:column;justify-content:center;}

.tlrow::before{content:"";position:absolute;left:-38px;top:50%;margin-top:-11px;
  width:22px;height:22px;
  border-radius:5px;background:rgba(255,255,255,0.30);}
.tlrow.hot::before{background:{{A1}};}
.tld{font-size:22px;font-weight:800;letter-spacing:2px;text-transform:uppercase;
  color:{{A2}};}
.tlrow.hot .tld{color:{{A1}};}
.tlt{font-size:31px;font-weight:800;margin-top:5px;line-height:1.2;}
.tls{font-size:23px;font-weight:500;margin-top:5px;line-height:1.34;
  color:rgba(255,255,255,0.84);}

/* flux horizontal */
.flow{display:flex;align-items:stretch;gap:12px;min-height:450px;}
.step{flex:1;border-radius:16px;padding:28px 22px;display:flex;
  flex-direction:column;justify-content:center;
  border:2px solid rgba(255,255,255,0.16);background:rgba(255,255,255,0.05);}
.step .sn{font-size:34px;font-weight:900;color:{{A1}};line-height:1;}
.step .sbar{width:34px;height:3px;background:{{A1}};margin:12px 0 14px;border-radius:2px;}
.step .st{font-size:28px;font-weight:800;line-height:1.16;}
.step .ss{font-size:22px;font-weight:500;line-height:1.32;margin-top:8px;
  color:rgba(255,255,255,0.84);}
.arw{align-self:center;color:{{A1}};font-size:40px;font-weight:900;line-height:1;}

/* comparatif 2 cartes */
.cmp{display:flex;gap:14px;align-items:stretch;min-height:520px;}
.card{flex:1;border-radius:18px;padding:28px 26px;display:flex;
  flex-direction:column;}
.card .ch{font-size:26px;font-weight:900;text-transform:uppercase;letter-spacing:1px;
  margin-bottom:14px;}
.card .cb{font-size:25px;font-weight:500;line-height:1.38;}
.card ul{list-style:none;margin-top:12px;flex:1;display:flex;
  flex-direction:column;justify-content:center;gap:8px;}
.card li{font-size:25px;font-weight:500;line-height:1.3;margin-top:10px;
  padding-left:26px;position:relative;color:rgba(255,255,255,0.9);}
.card li::before{content:"";position:absolute;left:0;top:9px;width:12px;height:12px;
  border-radius:3px;}
.bad{border:2px solid {{RED}};background:rgba(255,90,90,0.10);}
.bad .ch{color:{{RED}};}
.bad li::before{background:{{RED}};}
.good{border:2px solid {{GREEN}};background:rgba(93,217,135,0.10);}
.good .ch{color:{{GREEN}};}
.good li::before{background:{{GREEN}};}
.cmparw{align-self:center;color:{{A1}};font-size:46px;font-weight:900;}

/* blocs de chiffres */
.stats{display:flex;flex-direction:column;gap:16px;}
.stat{display:flex;align-items:center;gap:24px;border-radius:16px;
  padding:22px 26px;min-height:120px;
  border:2px solid rgba(255,255,255,0.14);background:rgba(255,255,255,0.05);}
.stat .sv{font-size:56px;font-weight:900;color:{{A1}};line-height:1;flex-shrink:0;
  letter-spacing:-2px;}
.stat .sl{font-size:25px;font-weight:600;line-height:1.28;}
.stat.alt .sv{color:{{A2}};}

/* checklist */
.check{display:flex;flex-direction:column;gap:18px;}
.crow{display:flex;align-items:center;gap:20px;min-height:112px;}
.mk{flex-shrink:0;width:46px;height:46px;border-radius:12px;display:flex;
  align-items:center;justify-content:center;}
.mk.no{background:rgba(255,90,90,0.16);border:2px solid {{RED}};}
.mk.ok{background:rgba(93,217,135,0.16);border:2px solid {{GREEN}};}
.ctxt .cl{font-size:30px;font-weight:800;line-height:1.16;}
.ctxt .cs{font-size:23px;font-weight:500;line-height:1.32;margin-top:5px;
  color:rgba(255,255,255,0.84);}

/* etages empiles */
.layers{display:flex;flex-direction:column;gap:16px;align-items:center;}
.layer{border-radius:16px;padding:24px 28px;border-left:6px solid {{A1}};
  background:rgba(255,255,255,0.06);width:100%;min-height:162px;
  display:flex;flex-direction:column;justify-content:center;}
.layer .ln{font-size:20px;font-weight:800;letter-spacing:3px;text-transform:uppercase;
  color:{{A2}};}
.layer .lt{font-size:31px;font-weight:800;margin-top:6px;line-height:1.16;}
.layer .ls{font-size:23px;font-weight:500;margin-top:6px;line-height:1.32;
  color:rgba(255,255,255,0.84);}

/* tenaille : 2 menaces vers 1 bloc */
.pincer{display:flex;flex-direction:column;align-items:center;gap:0;}
.prow{display:flex;gap:16px;width:100%;}
.pbox{flex:1;border-radius:16px;padding:28px 26px;border:2px solid {{A2}};
  background:rgba(255,255,255,0.05);display:flex;flex-direction:column;
  justify-content:center;min-height:212px;}
.pbox .pt{font-size:29px;font-weight:800;line-height:1.16;color:{{A2}};}
.pbox .ps{font-size:23px;font-weight:500;line-height:1.32;margin-top:7px;
  color:rgba(255,255,255,0.86);}
.pv{color:{{A1}};font-size:42px;font-weight:900;margin:18px 0;line-height:1;
  flex:0 0 auto;}
.pcore{width:100%;border-radius:18px;padding:30px 28px;background:{{A1}};
  text-align:center;display:flex;flex-direction:column;
  justify-content:center;min-height:182px;}
.pcore .pct{font-size:34px;font-weight:900;line-height:1.16;text-transform:uppercase;}
.pcore .pcs{font-size:24px;font-weight:600;line-height:1.32;margin-top:8px;
  color:rgba(255,255,255,0.92);}

/* couverture */
.cov{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.cov .ce{font-size:24px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cov .ct{font-size:66px;font-weight:900;line-height:1.03;letter-spacing:-2px;
  text-transform:uppercase;margin-top:30px;}
.cov .ct em{font-style:normal;color:{{A1}};}
.cov .cr{width:78px;height:4px;background:{{A1}};margin:34px 0;border-radius:2px;}
.cov .cs{font-size:28px;font-weight:600;line-height:1.36;max-width:840px;
  color:rgba(255,255,255,0.90);}
.cov .cf{font-size:23px;font-weight:500;font-style:italic;margin-top:22px;
  color:rgba(255,255,255,0.80);}

/* CTA */
.cta{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.cta .qe{font-size:22px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cta .qt{font-size:46px;font-weight:900;line-height:1.1;margin-top:26px;max-width:860px;
  text-transform:uppercase;letter-spacing:-1px;}
.cta .qt em{font-style:normal;color:{{A1}};}
.cta .qs{font-size:25px;font-weight:500;line-height:1.38;margin-top:22px;max-width:780px;
  color:rgba(255,255,255,0.88);}
.cta .box{background:#fff;border-radius:22px;padding:34px 30px;margin-top:34px;
  width:100%;max-width:840px;}
.cta .box .bk{font-size:28px;font-weight:800;letter-spacing:3px;color:{{NAVY}};}
.cta .box .bw{font-size:80px;font-weight:900;letter-spacing:2px;line-height:1.02;
  margin-top:8px;color:{{A1}};}
.cta .qv{font-size:24px;font-weight:600;font-style:italic;line-height:1.36;
  margin-top:26px;max-width:800px;color:{{A1}};}

/* cloture */
.end{position:absolute;inset:0;padding:96px 84px 186px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.end .ee{font-size:22px;font-weight:800;letter-spacing:5px;text-transform:uppercase;
  color:{{A2}};}
.end .es{font-size:52px;font-weight:900;letter-spacing:-1px;margin-top:20px;}
.end .er{width:78px;height:4px;background:{{A1}};margin:30px 0;border-radius:2px;}
.end .em{font-size:29px;font-weight:500;line-height:1.38;max-width:800px;}
.end .em em{font-style:normal;color:{{A1}};font-weight:700;}
.icons{display:flex;gap:36px;align-items:center;margin-top:40px;padding:20px 42px;
  border-radius:60px;background:linear-gradient(90deg,{{A1}},{{A2}});}
"""


def _icons_svg():
    tpl = ('<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#fff" '
           'stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">%s</svg>')
    heart = tpl % ('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0'
                   '-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>')
    chat = tpl % ('<path d="M21 11.5a8.4 8.4 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21'
                  'l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/>')
    send = tpl % ('<line x1="22" y1="2" x2="11" y2="13"/>'
                  '<polygon points="22 2 15 22 11 13 2 9 22 2"/>')
    save = tpl % '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>'
    return heart + chat + send + save


CHECK_SVG = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="%s" '
             'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">'
             '<polyline points="20 6 9 17 4 12"/></svg>')
CROSS_SVG = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="%s" '
             'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">'
             '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>'
             '</svg>')


class Deck:
    """Un carrousel : une marque, une charte, des slides construites par methodes."""

    def __init__(self, brand):
        if brand not in BRANDS:
            raise ValueError("Marque inconnue : " + brand)
        self.key = brand
        self.b = BRANDS[brand]
        self.logo_b64 = b64(ASSETS / "logos" / self.b["logo"], "image/png")
        self.bg_photo_b64 = None
        self._build_css()

    # ---------- style ----------
    def _build_css(self):
        css = CSS_TPL
        for token, val in (("{{NAVY}}", self.b["navy"]), ("{{DEEP}}", self.b["deep"]),
                           ("{{A1}}", self.b["a1"]), ("{{A2}}", self.b["a2"]),
                           ("{{RED}}", self.b["red"]), ("{{GREEN}}", self.b["green"])):
            css = css.replace(token, val)
        self.css = FONT_FACES + css
        if self.bg_photo_b64:
            self.css += self._photo_css()

    def set_bg_photo(self, filename, veil=None):
        """Pose une photo en fond (fichier dans assets/backgrounds/).
        veil : opacite du voile navy (defaut 0.84 ; monter si la photo est claire)."""
        self.bg_photo_b64 = b64(ASSETS / "backgrounds" / filename, "image/jpeg")
        self.veil = veil or 0.84
        self._build_css()

    def _photo_css(self):
        v = getattr(self, "veil", 0.84)
        navy = self.b["navy"].lstrip("#")
        r, g, bl = int(navy[0:2], 16), int(navy[2:4], 16), int(navy[4:6], 16)
        rgb = "%d,%d,%d" % (r, g, bl)
        return (
            ".bg{background-image:url(" + self.bg_photo_b64 + ") !important;"
            "background-size:cover !important;background-position:center bottom !important;}"
            ".bg::after{background:"
            "linear-gradient(135deg, rgba(" + rgb + "," + str(v) + "), "
            "rgba(" + rgb + "," + str(min(v + 0.05, 0.95)) + ")),"
            "linear-gradient(180deg, rgba(" + rgb + ",0.55) 0%, rgba(" + rgb + ",0.10) 40%)"
            " !important;}"
        )

    # ---------- briques communes ----------
    def _open(self):
        return '<div class="slide"><div class="bg"></div><div class="topbar"></div>'

    def _logo(self, big=False, chevron=True):
        h = ' style="height:78px;"' if big else ""
        bottom = ' style="bottom:52px;"' if big else ""
        ch = '<div class="chev">»</div>' if chevron else ""
        return ('<div class="logo"' + bottom + '><img src="' + self.logo_b64 + '"' + h +
                '/></div>' + ch + '</div>')

    def _head(self, num, title, subtitle=None, lead=None):
        n = '<div class="num">%d</div>' % num if num else ""
        eye = '<div class="eyebrow">%s</div>' % subtitle if subtitle else ""
        ld = '<div class="lead">%s</div>' % lead if lead else ""
        return (eye + '<div class="h1">%s</div><div class="rule"></div>' % title + ld + n)

    def _foot(self, label, value):
        if not label:
            return ""
        return ('<div class="foot"><div class="fl">%s</div><div class="fv">%s</div></div>'
                % (label, value))

    def _wrap(self, num, title, eyebrow, viz, foot_label, foot_value, lead=None):
        """Assemble une slide de contenu : en-tete, visuel centre, bandeau, logo.
        Les deux .grow encadrent le visuel pour le centrer dans l'espace restant."""
        return (self._open() + '<div class="pad">' +
                self._head(num, title, eyebrow, lead) + viz +
                self._foot(foot_label, foot_value) + '</div>' + self._logo())

    # ---------- slides ----------
    def cover(self, eyebrow, title, subtitle, footnote=None):
        fn = '<div class="cf">%s</div>' % footnote if footnote else ""
        return (self._open() +
                '<div class="cov"><div class="ce">%s</div>'
                '<div class="ct">%s</div><div class="cr"></div>'
                '<div class="cs">%s</div>%s</div>' % (eyebrow, title, subtitle, fn) +
                self._logo(big=True, chevron=True))

    def mindmap(self, num, title, eyebrow, core, branches, foot_label=None, foot_value="", lead=None):
        """Carte mentale : un noyau central + 4 branches (haut/bas x gauche/droite)."""
        assert len(branches) == 4, "la carte mentale attend exactement 4 branches"
        pos = [("left:0;top:18px;width:300px;", 0), ("left:628px;top:18px;width:300px;", 1),
               ("left:0;bottom:0;width:300px;", 2), ("left:628px;bottom:0;width:300px;", 3)]
        nodes = ""
        for style, i in pos:
            label, text = branches[i]
            nodes += ('<div class="node" style="%s"><div class="nl">%s</div>'
                      '<div class="nt">%s</div></div>' % (style, label, text))
        wires = (
            '<svg class="wires" width="928" height="640" viewBox="0 0 928 640">'
            '<g fill="none" stroke="rgba(255,255,255,0.26)" stroke-width="3">'
            '<path d="M314 320 H282 Q270 320 270 308 V97 Q270 85 282 85 H300"/>'
            '<path d="M614 320 H646 Q658 320 658 308 V97 Q658 85 646 85 H628"/>'
            '<path d="M314 320 H282 Q270 320 270 332 V538 Q270 550 282 550 H300"/>'
            '<path d="M614 320 H646 Q658 320 658 332 V538 Q658 550 646 550 H628"/>'
            '</g></svg>')
        viz = ('<div class="viz mid"><div class="map">%s%s'
               '<div class="core"><span>%s</span></div></div></div>'
               % (wires, nodes, core))
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def timeline(self, num, title, eyebrow, rows, foot_label=None, foot_value="", lead=None):
        """rows : liste de (date, titre, texte, hot_bool)."""
        body = ""
        for date, t, s, hot in rows:
            body += ('<div class="tlrow%s"><div class="tld">%s</div>'
                     '<div class="tlt">%s</div><div class="tls">%s</div></div>'
                     % (" hot" if hot else "", date, t, s))
        viz = '<div class="viz"><div class="tl">%s</div></div>' % body
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def flow(self, num, title, eyebrow, steps, foot_label=None, foot_value="", lead=None):
        """steps : liste de (titre, texte) ; 3 max pour rester lisible."""
        parts = []
        for i, (t, s) in enumerate(steps, 1):
            parts.append('<div class="step"><div class="sn">%d</div>'
                         '<div class="sbar"></div><div class="st">%s</div>'
                         '<div class="ss">%s</div></div>' % (i, t, s))
        viz = ('<div class="viz"><div class="flow">' +
               '<div class="arw">→</div>'.join(parts) + '</div></div>')
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def compare(self, num, title, eyebrow, left, right, foot_label=None, foot_value="", lead=None):
        """left / right : dict(head=..., items=[...])."""
        def card(cls, d):
            lis = "".join('<li>%s</li>' % x for x in d["items"])
            return ('<div class="card %s"><div class="ch">%s</div><ul>%s</ul></div>'
                    % (cls, d["head"], lis))
        viz = ('<div class="viz"><div class="cmp">%s<div class="cmparw">→</div>%s</div></div>'
               % (card("bad", left), card("good", right)))
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def stats(self, num, title, eyebrow, items, foot_label=None, foot_value="", lead=None):
        """items : liste de (valeur, libelle) ; alterne les 2 accents."""
        body = ""
        for i, (v, l) in enumerate(items):
            body += ('<div class="stat%s"><div class="sv">%s</div>'
                     '<div class="sl">%s</div></div>' % (" alt" if i % 2 else "", v, l))
        viz = '<div class="viz"><div class="stats">%s</div></div>' % body
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def checklist(self, num, title, eyebrow, rows, foot_label=None, foot_value="", lead=None):
        """rows : liste de (ok_bool, titre, texte)."""
        body = ""
        for ok, t, s in rows:
            icon = (CHECK_SVG % self.b["green"]) if ok else (CROSS_SVG % self.b["red"])
            body += ('<div class="crow"><div class="mk %s">%s</div>'
                     '<div class="ctxt"><div class="cl">%s</div>'
                     '<div class="cs">%s</div></div></div>'
                     % ("ok" if ok else "no", icon, t, s))
        viz = '<div class="viz"><div class="check">%s</div></div>' % body
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def layers(self, num, title, eyebrow, rows, foot_label=None, foot_value="", lead=None):
        """rows : liste de (numero/label, titre, texte)."""
        body = ""
        for n, t, s in rows:
            body += ('<div class="layer"><div class="ln">%s</div>'
                     '<div class="lt">%s</div><div class="ls">%s</div></div>' % (n, t, s))
        viz = '<div class="viz"><div class="layers">%s</div></div>' % body
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def pincer(self, num, title, eyebrow, top_left, top_right, core,
               foot_label=None, foot_value="", lead=None):
        """Schema en tenaille : 2 contraintes qui convergent vers un bloc central."""
        def box(d):
            return ('<div class="pbox"><div class="pt">%s</div>'
                    '<div class="ps">%s</div></div>' % (d[0], d[1]))
        viz = ('<div class="viz"><div class="pincer">'
               '<div class="prow">%s%s</div><div class="pv">↓</div>'
               '<div class="pcore"><div class="pct">%s</div>'
               '<div class="pcs">%s</div></div></div></div>'
               % (box(top_left), box(top_right), core[0], core[1]))
        return self._wrap(num, title, eyebrow, viz, foot_label, foot_value, lead)

    def cta(self, eyebrow, title, keyword, value, subtitle=None):
        sub = '<div class="qs">%s</div>' % subtitle if subtitle else ""
        return (self._open() +
                '<div class="cta"><div class="qe">%s</div><div class="qt">%s</div>%s'
                '<div class="box"><div class="bk">COMMENTE</div>'
                '<div class="bw">%s</div></div>'
                '<div class="qv">%s</div></div>' % (eyebrow, title, sub, keyword, value) +
                self._logo())

    def cta_sans_commentaire(self, eyebrow, title, action, value, subtitle=None):
        """Appel a l'action qui ne demande AUCUN commentaire (Guestlucky).

        Regle Martin du 30/07/2026 : les legendes et les slides Guestlucky ne
        doivent jamais promettre un envoi en reponse a un commentaire, sinon
        Martin doit repondre a la main apres publication. Actions autorisees :
        s'abonner, enregistrer le post, le partager, visiter le site.

        `action` est le petit label du cadre (ex. "RENDEZ-VOUS SUR"), et le gros
        mot affiche est l'adresse du site de la marque.
        """
        sub = '<div class="qs">%s</div>' % subtitle if subtitle else ""
        return (self._open() +
                '<div class="cta"><div class="qe">%s</div><div class="qt">%s</div>%s'
                '<div class="box"><div class="bk">%s</div>'
                '<div class="bw">%s</div></div>'
                '<div class="qv">%s</div></div>'
                % (eyebrow, title, sub, action, self.b["site"], value) +
                self._logo())

    def closing(self, message, eyebrow="Rejoignez-nous sur"):
        return (self._open() +
                '<div class="end"><div class="ee">%s</div>'
                '<div class="es">%s</div><div class="er"></div>'
                '<div class="em">%s</div><div class="icons">%s</div></div>'
                % (eyebrow, self.b["site"], message, _icons_svg()) +
                self._logo(big=True, chevron=False))

    # ---------- ecriture ----------
    def write(self, slug, slides):
        out = ROOT / "output" / slug / "html"
        out.mkdir(parents=True, exist_ok=True)
        bad = 0
        for i, body in enumerate(slides, 1):
            html = ('<!doctype html><html><head><meta charset="utf-8">'
                    '<style>' + self.css + '</style></head><body>' + body +
                    '</body></html>')
            found = [c for c in html if c in DASHES]
            if found:
                print("  ALERTE tiret long slide %d : %s" % (i, set(found)))
                bad += len(found)
            (out / ("slide_%02d.html" % i)).write_text(html, encoding="utf-8")
        print("%d slides HTML ecrites dans %s. Tirets longs : %d" % (len(slides), out, bad))
        return out


def acc(word):
    """Met un mot en couleur d'accent principal (dans un titre)."""
    return "<em>%s</em>" % word
