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
import datetime
import hashlib
import json
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
        "a1_clair": "#6d28d9",   # memes couleurs, un cran plus dense sur papier
        "a2_clair": "#d1258a",
        "red": "#ff5a5a", "green": "#5dd987",
        "logo": "guestlucky.png",            # glyphes blancs : fonds sombres
        "logo_clair": "guestlucky_sombre.png",  # glyphes navy : fonds clairs
        "papier": "#F4F1FA",                 # blanc casse legerement violace
        "encre": "#120a2e",
        "site": "guestlucky.com",
    },
    "lesousloueur": {
        "name": "Le Sous Loueur",
        "navy": "#0d1b2e", "deep": "#081320",
        "a1": "#E8561F",   # orange : accent principal
        "a2": "#2086C8",   # bleu : accent secondaire
        "a1_clair": "#D4471A",   # memes couleurs, un cran plus dense sur papier
        "a2_clair": "#17699F",
        "red": "#ff5a5a", "green": "#5dd987",
        "logo": "lesousloueur_white_temp.png",
        "logo_clair": "lesousloueur.png",    # version navy officielle
        "papier": "#F6F3EE",                 # blanc casse legerement chaud
        "encre": "#0d1b2e",
        "site": "WWW.LESOUSLOUEUR.FR",
    },
}

# --------------------------------------------------------------------------
# THEMES (Martin, 18/09/2026) : "toutes les couvertures se ressemblent".
# La cause etait structurelle : la feuille de style etait ecrite en dur pour un
# fond sombre. On peut desormais retourner entierement la charte. Le theme
# "clair" pose l'encre de la marque et ses accents sur un papier blanc casse.
# Les couleurs d'accent (orange/bleu, violet/rose) ne changent JAMAIS.
# --------------------------------------------------------------------------

THEMES = ("sombre", "clair")


def jetons_theme(marque, theme):
    """Les valeurs des jetons de la feuille de style pour une marque + un theme."""
    b = BRANDS[marque]
    if theme == "clair":
        encre = b["encre"]
        rgb = ",".join(str(int(encre.lstrip("#")[i:i + 2], 16)) for i in (0, 2, 4))
        return {
            "SURF": b["papier"], "SURF2": "#FFFFFF",
            "INK": encre, "INK_SOFT": "rgba(%s,0.74)" % rgb,
            "CARD": "rgba(%s,0.055)" % rgb, "BORDER": "rgba(%s,0.16)" % rgb,
            "DOT": "rgba(%s,0.22)" % rgb, "WIRE": "rgba(%s,0.22)" % rgb,
            "PANEL": encre, "PANEL_INK": "#FFFFFF",
            "A1": b["a1_clair"], "A2": b["a2_clair"],
            "VIG1": "rgba(255,255,255,0.30)", "VIG2": "rgba(255,255,255,0.45)",
            "logo": b["logo_clair"], "voile": b["papier"], "voile_defaut": 0.90,
        }
    return {
        "SURF": b["navy"], "SURF2": b["deep"],
        "INK": "#FFFFFF", "INK_SOFT": "rgba(255,255,255,0.86)",
        "CARD": "rgba(255,255,255,0.06)", "BORDER": "rgba(255,255,255,0.16)",
        "DOT": "rgba(255,255,255,0.30)", "WIRE": "rgba(255,255,255,0.26)",
        "PANEL": "#FFFFFF", "PANEL_INK": b["navy"],
        "A1": b["a1"], "A2": b["a2"],
        "VIG1": "rgba(0,0,0,0.40)", "VIG2": "rgba(0,0,0,0.30)",
        "logo": b["logo"], "voile": b["navy"], "voile_defaut": 0.84,
    }


# --------------------------------------------------------------------------
# Feuille de style V2 (tokens remplaces par la marque)
# --------------------------------------------------------------------------

CSS_TPL = """
*{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;
  background:{{SURF}};color:{{INK}};}

/* fond : degrade sobre, ou photo si fournie */
.bg{position:absolute;inset:0;background:
  radial-gradient(58% 44% at 26% 88%, {{A1}}2e 0%, rgba(0,0,0,0) 62%),
  radial-gradient(52% 40% at 84% 74%, {{A2}}24 0%, rgba(0,0,0,0) 64%),
  linear-gradient(180deg, {{SURF2}} 0%, {{SURF}} 100%);}
.bg::after{content:"";position:absolute;inset:0;background:
  radial-gradient(84% 80% at 50% 58%, rgba(0,0,0,0) 44%, {{VIG1}} 100%),
  linear-gradient(180deg, {{VIG2}} 0%, rgba(0,0,0,0) 30%);}
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
.lead{font-size:25px;font-weight:500;line-height:1.4;color:{{INK_SOFT}};
  margin-top:20px;max-width:830px;}
.grow{flex:1;}

/* bandeau de bas de slide */
.foot{display:flex;align-items:stretch;border-radius:12px;overflow:hidden;}
.foot .fl{background:{{A1}};color:#fff;font-weight:800;font-size:20px;
  padding:17px 21px;display:flex;align-items:center;flex-shrink:0;}
.foot .fv{background:{{PANEL}};color:{{PANEL_INK}};font-weight:700;font-size:20px;
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
  border:2px solid {{BORDER}};background:{{CARD}};}
.node .nl{font-size:29px;font-weight:800;color:{{A1}};line-height:1.12;}
.node .nt{font-size:22px;font-weight:500;line-height:1.34;margin-top:9px;
  color:{{INK_SOFT}};}
.core{position:absolute;left:314px;top:268px;width:300px;height:104px;
  border-radius:18px;display:flex;align-items:center;justify-content:center;
  text-align:center;padding:14px 18px;background:{{A1}};}
.core span{color:#fff;font-size:28px;font-weight:900;line-height:1.14;text-transform:uppercase;
  letter-spacing:-0.3px;}
.wires{position:absolute;inset:0;}

/* timeline verticale */
.tl{position:relative;padding-left:38px;display:flex;flex-direction:column;}
.tl::before{content:"";position:absolute;left:9px;top:10px;bottom:10px;width:3px;
  background:{{BORDER}};}
.tlrow{position:relative;min-height:128px;display:flex;
  flex-direction:column;justify-content:center;}

.tlrow::before{content:"";position:absolute;left:-38px;top:50%;margin-top:-11px;
  width:22px;height:22px;
  border-radius:5px;background:{{DOT}};}
.tlrow.hot::before{background:{{A1}};}
.tld{font-size:22px;font-weight:800;letter-spacing:2px;text-transform:uppercase;
  color:{{A2}};}
.tlrow.hot .tld{color:{{A1}};}
.tlt{font-size:31px;font-weight:800;margin-top:5px;line-height:1.2;}
.tls{font-size:23px;font-weight:500;margin-top:5px;line-height:1.34;
  color:{{INK_SOFT}};}

/* flux horizontal */
.flow{display:flex;align-items:stretch;gap:12px;min-height:450px;}
.step{flex:1;border-radius:16px;padding:28px 22px;display:flex;
  flex-direction:column;justify-content:center;
  border:2px solid {{BORDER}};background:{{CARD}};}
.step .sn{font-size:34px;font-weight:900;color:{{A1}};line-height:1;}
.step .sbar{width:34px;height:3px;background:{{A1}};margin:12px 0 14px;border-radius:2px;}
.step .st{font-size:28px;font-weight:800;line-height:1.16;}
.step .ss{font-size:22px;font-weight:500;line-height:1.32;margin-top:8px;
  color:{{INK_SOFT}};}
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
  padding-left:26px;position:relative;color:{{INK_SOFT}};}
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
  border:2px solid {{BORDER}};background:{{CARD}};}
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
  color:{{INK_SOFT}};}

/* etages empiles */
.layers{display:flex;flex-direction:column;gap:16px;align-items:center;}
.layer{border-radius:16px;padding:24px 28px;border-left:6px solid {{A1}};
  background:{{CARD}};width:100%;min-height:162px;
  display:flex;flex-direction:column;justify-content:center;}
.layer .ln{font-size:20px;font-weight:800;letter-spacing:3px;text-transform:uppercase;
  color:{{A2}};}
.layer .lt{font-size:31px;font-weight:800;margin-top:6px;line-height:1.16;}
.layer .ls{font-size:23px;font-weight:500;margin-top:6px;line-height:1.32;
  color:{{INK_SOFT}};}

/* tenaille : 2 menaces vers 1 bloc */
.pincer{display:flex;flex-direction:column;align-items:center;gap:0;}
.prow{display:flex;gap:16px;width:100%;}
.pbox{flex:1;border-radius:16px;padding:28px 26px;border:2px solid {{A2}};
  background:{{CARD}};display:flex;flex-direction:column;
  justify-content:center;min-height:212px;}
.pbox .pt{font-size:29px;font-weight:800;line-height:1.16;color:{{A2}};}
.pbox .ps{font-size:23px;font-weight:500;line-height:1.32;margin-top:7px;
  color:{{INK_SOFT}};}
.pv{color:{{A1}};font-size:42px;font-weight:900;margin:18px 0;line-height:1;
  flex:0 0 auto;}
.pcore{width:100%;border-radius:18px;padding:30px 28px;background:{{A1}};
  text-align:center;display:flex;flex-direction:column;
  justify-content:center;min-height:182px;}
.pcore .pct{color:#fff;font-size:34px;font-weight:900;line-height:1.16;text-transform:uppercase;}
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
  color:{{INK_SOFT}};}
.cov .cf{font-size:23px;font-weight:500;font-style:italic;margin-top:22px;
  color:{{INK_SOFT}};}

/* ---- COUVERTURES ALTERNATIVES (Martin, 02/09/2026) -----------------------
   Toutes les couvertures se ressemblaient sur le profil Instagram : meme
   silhouette, seuls les mots changeaient. On dispose maintenant de CINQ
   archetypes, a faire TOURNER. Voir la regle 16 dans carroussel.md.        */

/* A. le chiffre plein cadre */
.cvA{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;}
.cvA .eyb{font-size:23px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cvA .big{font-size:206px;font-weight:900;line-height:0.82;letter-spacing:-10px;
  color:{{A1}};margin-top:18px;}
.cvA .big small{font-size:94px;letter-spacing:-4px;}
.cvA .un{font-size:34px;font-weight:800;line-height:1.15;margin-top:26px;
  text-transform:uppercase;}
.cvA .sub{font-size:27px;font-weight:600;line-height:1.34;margin-top:20px;max-width:820px;
  color:{{INK_SOFT}};}

/* B. l'aplat de couleur */
.cvB{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;}
.cvB .haut{flex:1;}
.cvB .bloc{background:{{A1}};padding:56px 72px 64px;margin-bottom:118px;}
.cvB .bloc .q{font-size:60px;font-weight:900;line-height:1.06;letter-spacing:-2px;
  text-transform:uppercase;color:#fff;}
.cvB .bloc .r{font-size:26px;font-weight:600;line-height:1.34;margin-top:22px;
  color:rgba(255,255,255,0.95);}
.cvB .etq{color:{{INK}};position:absolute;top:96px;left:84px;font-size:23px;font-weight:800;
  letter-spacing:6px;text-transform:uppercase;color:#fff;}

/* C. la citation */
.cvC{position:absolute;inset:0;padding:110px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;}
.cvC .guil{font-size:196px;font-weight:900;line-height:0.5;color:{{A1}};opacity:0.55;}
.cvC .phr{font-size:52px;font-weight:800;line-height:1.14;letter-spacing:-1px;margin-top:14px;}
.cvC .phr em{font-style:normal;color:{{A1}};}
.cvC .qui{font-size:25px;font-weight:600;margin-top:34px;color:{{INK_SOFT}};}
.cvC .qui b{color:{{INK}};}

/* D. le duo avant / apres */
.cvD{position:absolute;inset:0;padding:96px 60px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;}
.cvD .eyb{font-size:23px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};text-align:center;}
.cvD .tt{font-size:50px;font-weight:900;line-height:1.06;text-transform:uppercase;
  text-align:center;margin-top:22px;letter-spacing:-1px;}
.cvD .cols{display:flex;gap:22px;margin-top:44px;}
.cvD .col{flex:1;background:{{CARD}};border-radius:22px;padding:30px 26px;
  border:1px solid {{BORDER}};}
.cvD .col.on{background:{{A1}};border-color:{{A1}};}
.cvD .col .k{font-size:21px;font-weight:800;letter-spacing:3px;text-transform:uppercase;
  color:{{A2}};}
.cvD .col.on .k{color:#fff;}
.cvD .col .v{font-size:62px;font-weight:900;line-height:0.98;margin-top:14px;color:{{A1}};}
.cvD .col.on .v{color:#fff;}
.cvD .col .d{font-size:23px;font-weight:600;line-height:1.3;margin-top:14px;
  color:{{INK_SOFT}};}

/* CTA */
.cta{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;align-items:center;text-align:center;}
.cta .qe{font-size:22px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cta .qt{font-size:46px;font-weight:900;line-height:1.1;margin-top:26px;max-width:860px;
  text-transform:uppercase;letter-spacing:-1px;}
.cta .qt em{font-style:normal;color:{{A1}};}
.cta .qs{font-size:25px;font-weight:500;line-height:1.38;margin-top:22px;max-width:780px;
  color:{{INK_SOFT}};}
.cta .box{background:{{PANEL}};border-radius:22px;padding:34px 30px;margin-top:34px;
  width:100%;max-width:840px;}
.cta .box .bk{font-size:28px;font-weight:800;letter-spacing:3px;color:{{PANEL_INK}};}
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

/* ---- SEPT COUVERTURES DE PLUS (Martin, 18/09/2026) ----------------------
   « elles se ressemblent toujours autant, il faudrait vraiment changer
   completement ». Douze archetypes au total, et deux themes : la meme
   semaine ne peut plus ressembler a la precedente.                        */

/* F. bandeau plein travers */
.cvF{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;
  justify-content:center;padding-bottom:70px;}
.cvF .eyb{position:absolute;top:96px;left:84px;font-size:23px;font-weight:800;
  letter-spacing:6px;text-transform:uppercase;color:{{A2}};}
.cvF .band{background:{{A1}};padding:52px 84px;}
.cvF .band .t{font-size:72px;font-weight:900;line-height:0.98;letter-spacing:-2.5px;
  text-transform:uppercase;color:#fff;}
.cvF .sub{padding:0 84px;margin-top:36px;font-size:27px;font-weight:600;
  line-height:1.36;max-width:880px;color:{{INK_SOFT}};}

/* G. sommaire numerote */
.cvG{position:absolute;inset:0;padding:100px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;}
.cvG .eyb{font-size:23px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cvG .t{font-size:54px;font-weight:900;line-height:1.02;letter-spacing:-1.8px;
  text-transform:uppercase;margin-top:18px;}
.cvG .lst{margin-top:40px;display:flex;flex-direction:column;}
.cvG .it{display:flex;align-items:center;gap:22px;padding:18px 0;
  border-bottom:2px solid {{BORDER}};}
.cvG .it .n{font-size:38px;font-weight:900;color:{{A1}};line-height:1;
  min-width:56px;letter-spacing:-2px;}
.cvG .it .x{font-size:27px;font-weight:700;line-height:1.2;}

/* H. un seul mot, plein cadre */
.cvH{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;}
.cvH .eyb{font-size:23px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cvH .mot{font-size:152px;font-weight:900;line-height:0.86;letter-spacing:-8px;
  text-transform:uppercase;color:{{A1}};margin-top:22px;overflow-wrap:anywhere;}
.cvH .rl{width:120px;height:6px;background:{{A2}};margin:34px 0;border-radius:3px;}
.cvH .sub{font-size:29px;font-weight:600;line-height:1.34;max-width:840px;
  color:{{INK_SOFT}};}

/* I. etiquette posee de travers */
.cvI{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;align-items:flex-start;}
.cvI .tag{transform:rotate(-2.4deg);background:{{PANEL}};color:{{PANEL_INK}};
  padding:42px 46px;border-radius:8px;max-width:880px;}
.cvI .tag .k{font-size:22px;font-weight:800;letter-spacing:5px;
  text-transform:uppercase;color:{{A1}};}
.cvI .tag .t{font-size:58px;font-weight:900;line-height:1.02;letter-spacing:-2px;
  text-transform:uppercase;margin-top:14px;}
.cvI .sub{margin-top:44px;font-size:26px;font-weight:600;line-height:1.36;
  max-width:840px;color:{{INK_SOFT}};}

/* J. deux moitiees empilees */
.cvJ{position:absolute;inset:0;padding-bottom:172px;z-index:2;display:flex;
  flex-direction:column;}
.cvJ .moitie{flex:1;padding:0 84px;display:flex;flex-direction:column;
  justify-content:center;}
.cvJ .moitie.pleine{background:{{A1}};}
.cvJ .k{font-size:22px;font-weight:800;letter-spacing:5px;text-transform:uppercase;
  color:{{A2}};}
.cvJ .moitie.pleine .k{color:rgba(255,255,255,0.88);}
.cvJ .t{font-size:54px;font-weight:900;line-height:1.02;letter-spacing:-2px;
  text-transform:uppercase;margin-top:12px;}
.cvJ .moitie.pleine .t{color:#fff;}
.cvJ .s{font-size:24px;font-weight:600;line-height:1.34;margin-top:14px;
  max-width:800px;color:{{INK_SOFT}};}
.cvJ .moitie.pleine .s{color:rgba(255,255,255,0.90);}

/* K. trois lignes barrees */
.cvK{position:absolute;inset:0;padding:96px 84px 176px;z-index:2;display:flex;
  flex-direction:column;justify-content:center;gap:30px;}
.cvK .eyb{font-size:23px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};margin-bottom:6px;}
.cvK .ln{border-left:9px solid {{A1}};padding-left:28px;}
.cvK .ln:last-child{border-left-color:{{A2}};}
.cvK .ln .t{font-size:52px;font-weight:900;line-height:1.02;letter-spacing:-1.8px;
  text-transform:uppercase;}
.cvK .ln .s{font-size:23px;font-weight:600;line-height:1.32;margin-top:9px;
  color:{{INK_SOFT}};}

/* L. cadre ouvert, la photo respire */
.cvL{position:absolute;left:46px;right:46px;top:46px;bottom:132px;
  border:3px solid {{A1}};z-index:2;display:flex;flex-direction:column;
  justify-content:flex-end;padding:0 46px 46px;}
.cvL .eyb{font-size:22px;font-weight:800;letter-spacing:6px;text-transform:uppercase;
  color:{{A2}};}
.cvL .t{font-size:58px;font-weight:900;line-height:1.02;letter-spacing:-2px;
  text-transform:uppercase;margin-top:16px;}
.cvL .t em{font-style:normal;color:{{A1}};}
.cvL .s{font-size:25px;font-weight:600;line-height:1.34;margin-top:18px;
  max-width:820px;color:{{INK_SOFT}};}
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

    def __init__(self, brand, theme="sombre"):
        if brand not in BRANDS:
            raise ValueError("Marque inconnue : " + brand)
        if theme not in THEMES:
            raise ValueError("Theme inconnu : %s (attendu %s)" % (theme, THEMES))
        self.key = brand
        self.b = BRANDS[brand]
        self.theme = theme
        self.t = jetons_theme(brand, theme)
        self.logo_b64 = b64(ASSETS / "logos" / self.t["logo"], "image/png")
        self.bg_photo_b64 = None
        self._build_css()

    # ---------- style ----------
    def _build_css(self):
        css = CSS_TPL
        for token, val in (("{{RED}}", self.b["red"]), ("{{GREEN}}", self.b["green"])):
            css = css.replace(token, val)
        for nom, val in self.t.items():
            if nom.isupper():
                css = css.replace("{{%s}}" % nom, val)
        assert "{{" not in css, "jeton de style non remplace"
        self.css = FONT_FACES + css
        if self.bg_photo_b64:
            self.css += self._photo_css()

    def set_bg_photo(self, filename, veil=None):
        """Pose une photo en fond (fichier dans assets/backgrounds/).
        veil : opacite du voile. Le voile prend la couleur du THEME : navy sur
        un theme sombre, papier sur un theme clair. Defaut 0.84 / 0.90."""
        self.bg_photo_b64 = b64(ASSETS / "backgrounds" / filename, "image/jpeg")
        self.veil = veil or self.t["voile_defaut"]
        self._build_css()

    def _photo_css(self):
        v = getattr(self, "veil", self.t["voile_defaut"])
        fond = self.t["voile"].lstrip("#")
        r, g, bl = int(fond[0:2], 16), int(fond[2:4], 16), int(fond[4:6], 16)
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

    def cover_chiffre(self, eyebrow, chiffre, unite, titre, subtitle):
        """COUVERTURE A : un chiffre enorme tire de la video, titre en dessous.
        A reserver aux sujets qui portent un vrai chiffre marquant."""
        u = '<small> %s</small>' % unite if unite else ""
        return (self._open() +
                '<div class="cvA"><div class="eyb">%s</div>'
                '<div class="big">%s%s</div><div class="un">%s</div>'
                '<div class="sub">%s</div></div>'
                % (eyebrow, chiffre, u, titre, subtitle) +
                self._logo(big=True, chevron=True))

    def cover_aplat(self, eyebrow, question, reponse):
        """COUVERTURE B : bandeau de couleur pleine en bas, question dessus.
        C'est la plus visible de loin dans une grille de vignettes sombres."""
        return (self._open() +
                '<div class="cvB"><div class="etq">%s</div><div class="haut"></div>'
                '<div class="bloc"><div class="q">%s</div>'
                '<div class="r">%s</div></div></div>' % (eyebrow, question, reponse) +
                self._logo(big=False, chevron=True))

    def cover_citation(self, phrase, auteur, role):
        """COUVERTURE C : une phrase forte de la video, entre guillemets.
        La phrase doit etre VRAIMENT dite dans la video, jamais inventee."""
        return (self._open() +
                '<div class="cvC"><div class="guil">&laquo;</div>'
                '<div class="phr">%s</div>'
                '<div class="qui">%s, <b>%s</b></div></div>' % (phrase, auteur, role) +
                self._logo(big=True, chevron=True))

    def cover_duo(self, eyebrow, titre, gauche, droite):
        """COUVERTURE D : deux etats opposes cote a cote.
        gauche et droite = (etiquette, valeur, phrase). La droite est mise en avant."""
        def col(t3, actif):
            k, v, d = t3
            return ('<div class="col%s"><div class="k">%s</div>'
                    '<div class="v">%s</div><div class="d">%s</div></div>'
                    % (" on" if actif else "", k, v, d))
        return (self._open() +
                '<div class="cvD"><div class="eyb">%s</div><div class="tt">%s</div>'
                '<div class="cols">%s%s</div></div>'
                % (eyebrow, titre, col(gauche, False), col(droite, True)) +
                self._logo(big=False, chevron=True))

    # ---- sept couvertures de plus (Martin, 18/09/2026) ------------------
    def cover_bandeau(self, eyebrow, titre, subtitle):
        """COUVERTURE F : un bandeau de couleur traverse la slide de part en
        part, titre dedans. Silhouette horizontale, tres reconnaissable."""
        return (self._open() +
                '<div class="cvF"><div class="eyb">%s</div>'
                '<div class="band"><div class="t">%s</div></div>'
                '<div class="sub">%s</div></div>' % (eyebrow, titre, subtitle) +
                self._logo(big=False, chevron=True))

    def cover_index(self, eyebrow, titre, points):
        """COUVERTURE G : le sommaire du carrousel, 3 a 5 points numerotes.
        points = liste de textes courts."""
        items = "".join('<div class="it"><div class="n">%d</div><div class="x">%s</div></div>'
                        % (i + 1, t) for i, t in enumerate(points))
        return (self._open() +
                '<div class="cvG"><div class="eyb">%s</div><div class="t">%s</div>'
                '<div class="lst">%s</div></div>' % (eyebrow, titre, items) +
                self._logo(big=False, chevron=True))

    def cover_mot(self, eyebrow, mot, subtitle):
        """COUVERTURE H : UN seul mot, en enorme. Affiche colle a l'affiche.
        Le mot doit etre court (12 caracteres au plus), sinon il deborde."""
        return (self._open() +
                '<div class="cvH"><div class="eyb">%s</div>'
                '<div class="mot">%s</div><div class="rl"></div>'
                '<div class="sub">%s</div></div>' % (eyebrow, mot, subtitle) +
                self._logo(big=True, chevron=True))

    def cover_etiquette(self, etiquette, titre, subtitle):
        """COUVERTURE I : une etiquette posee de travers, comme un dossier
        tamponne. Le seul archetype ou le titre est sur fond inverse."""
        return (self._open() +
                '<div class="cvI"><div class="tag"><div class="k">%s</div>'
                '<div class="t">%s</div></div>'
                '<div class="sub">%s</div></div>' % (etiquette, titre, subtitle) +
                self._logo(big=False, chevron=True))

    def cover_moities(self, haut, bas):
        """COUVERTURE J : deux moities empilees, la seconde en aplat de
        couleur. haut et bas = (etiquette, titre, phrase)."""
        def moitie(t3, pleine):
            k, t, s = t3
            return ('<div class="moitie%s"><div class="k">%s</div>'
                    '<div class="t">%s</div><div class="s">%s</div></div>'
                    % (" pleine" if pleine else "", k, t, s))
        return (self._open() +
                '<div class="cvJ">%s%s</div>' % (moitie(haut, False), moitie(bas, True)) +
                self._logo(big=False, chevron=True))

    def cover_trois(self, eyebrow, lignes):
        """COUVERTURE K : trois affirmations barrees d'un trait de couleur.
        lignes = liste de 3 tuples (titre, phrase)."""
        assert len(lignes) == 3, "cover_trois attend exactement 3 lignes"
        body = "".join('<div class="ln"><div class="t">%s</div><div class="s">%s</div></div>'
                       % (t, s) for t, s in lignes)
        return (self._open() +
                '<div class="cvK"><div class="eyb">%s</div>%s</div>' % (eyebrow, body) +
                self._logo(big=False, chevron=True))

    def cover_cadre(self, eyebrow, titre, subtitle):
        """COUVERTURE L : un filet encadre toute la slide, le texte est pousse
        en bas. C'est la couverture qui laisse le plus voir la photo."""
        return (self._open() +
                '<div class="cvL"><div class="eyb">%s</div>'
                '<div class="t">%s</div><div class="s">%s</div></div>'
                % (eyebrow, titre, subtitle) +
                self._logo(big=False, chevron=True))

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
            '<g fill="none" stroke="{{WIRE}}" stroke-width="3">'
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


# --------------------------------------------------------------------------
# ROTATION DES COUVERTURES (regle 16, Martin le 02/09/2026)
# --------------------------------------------------------------------------
# Le profil Instagram faisait moche : toutes les premieres pages avaient la
# meme silhouette. On dispose de CINQ archetypes ; ces deux fonctions
# garantissent qu'on ne reprend jamais le meme deux semaines de suite pour une
# marque, ni le meme sur les deux marques la meme semaine.

COUVERTURES = ("cover", "cover_chiffre", "cover_aplat", "cover_citation", "cover_duo",
               "cover_bandeau", "cover_index", "cover_mot", "cover_etiquette",
               "cover_moities", "cover_trois", "cover_cadre")
JOURNAL_COUVERTURES = ROOT / "output" / "couvertures.json"
JOURNAL_THEMES = ROOT / "output" / "themes.json"


def _journal(chemin):
    if chemin.is_file():
        try:
            return json.loads(chemin.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return {}


def _ecrire(chemin, j):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(j, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _historique(chemin, marque):
    """Les choix passes d'une marque, du plus ancien au plus recent.
    Accepte l'ancien format (une seule valeur texte) sans rien casser."""
    v = _journal(chemin).get(marque, [])
    return [v] if isinstance(v, str) else list(v)


def couvertures_possibles(marque, deja_prise=None):
    """Les archetypes autorises cette semaine pour cette marque, du plus au
    moins souhaitable. On ecarte les DEUX derniers de la marque et celui que
    l'autre marque vient de prendre. Choisis ensuite celui qui colle au SUJET :
    le chiffre demande un vrai chiffre marquant, la citation une phrase
    reellement prononcee, le sommaire un carrousel en points numerotes."""
    interdits = set(_historique(JOURNAL_COUVERTURES, marque)[-2:]) | {deja_prise}
    libres = [c for c in COUVERTURES if c not in interdits]
    return libres or [c for c in COUVERTURES if c != deja_prise]


def noter_couverture(marque, nom):
    """A appeler apres avoir ecrit le carrousel, pour que la semaine suivante
    sache quoi eviter."""
    assert nom in COUVERTURES, "archetype de couverture inconnu : %s" % nom
    j = _journal(JOURNAL_COUVERTURES)
    j[marque] = (_historique(JOURNAL_COUVERTURES, marque) + [nom])[-6:]
    _ecrire(JOURNAL_COUVERTURES, j)
    return nom


def themes_possibles(marque, deja_pris=None):
    """Le theme de la semaine : jamais le meme que la semaine derniere pour
    cette marque, et de preference pas celui que l'autre marque vient de
    prendre (une semaine tout sombre est moins vivante dans la grille)."""
    passe = _historique(JOURNAL_THEMES, marque)[-1:]
    libres = [t for t in THEMES if t not in set(passe) | {deja_pris}]
    return libres or [t for t in THEMES if t not in passe] or list(THEMES)


def noter_theme(marque, nom):
    assert nom in THEMES, "theme inconnu : %s" % nom
    j = _journal(JOURNAL_THEMES)
    j[marque] = (_historique(JOURNAL_THEMES, marque) + [nom])[-6:]
    _ecrire(JOURNAL_THEMES, j)
    return nom


def _melange(liste, marque, sel):
    """Melange stable : le tirage depend de la SEMAINE, donc il ne bouge pas
    pendant qu'on travaille, mais il change d'une semaine a l'autre. Sans cela
    on reprenait toujours le premier de la liste, c'est-a-dire le plus
    classique, et on retombait dans la monotonie qu'on essaie de corriger."""
    an, sem, _ = datetime.date.today().isocalendar()
    graine = "%d-%d-%s-%s" % (an, sem, marque, sel)
    ordre = sorted(liste, key=lambda x: hashlib.md5((graine + x).encode()).hexdigest())
    return ordre


def plan_semaine(marque, autre=None):
    """Propose (theme, couverture, scene de fond) pour la marque, en evitant
    tout ce qui a deja servi recemment et tout ce que l'autre marque prend la
    meme semaine. `autre` = le plan deja retenu pour l'autre marque.

    ⚠️ Ce n'est qu'une PROPOSITION : le sujet de la semaine prime toujours.
    Si la video n'a pas de chiffre marquant, ne prends pas cover_chiffre ;
    prends le suivant de la liste. Mais ne reviens JAMAIS a la couverture ni
    a la scene de la semaine precedente : c'est exactement ce que Martin a
    reproche deux fois (02/09 et 18/09).

    A appeler AVANT d'ecrire le carrousel ; noter_theme / noter_couverture /
    noter_scene enregistrent ensuite ce qui a reellement ete utilise."""
    from gemini_bg import scenes_possibles                 # import tardif : pas de cycle
    autre = autre or {}
    theme = themes_possibles(marque, autre.get("theme"))[0]
    couvertures = _melange(couvertures_possibles(marque, autre.get("couverture")), marque, "c")
    scenes = _melange(scenes_possibles(marque, theme, autre.get("scene")), marque, "s")
    return {"theme": theme, "couverture": couvertures[0], "scene": scenes[0],
            "couvertures_libres": couvertures, "scenes_libres": scenes}


def acc(word):
    """Met un mot en couleur d'accent principal (dans un titre)."""
    return "<em>%s</em>" % word
