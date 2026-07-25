#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur du PACK ELEVES CONCIERGERIE : visuels Instagram "templates" que chaque
eleve (conciergerie deja lancee) personnalise avec SES couleurs, SON logo, SES
offres, puis poste tel quel. Objectif des posts : donner envie aux PROPRIETAIRES
de confier leur bien a la conciergerie.

Regles specifiques au pack :
- 1 visuel = 1 post (pas de carrousel) : 30 visuels = 30 posts.
- Style clair / editorial (fond creme), volontairement NEUTRE : chaque zone de
  marque est marquee "A personnaliser" (logo, couleur, ville, contact).
- Les contenus d'exemple sont prefixes "Exemple :" quand l'eleve doit les
  remplacer par ses propres infos.
- INTERDIT : le mot "gestion" (et derives), les emojis, les tirets longs.

Genere les 4 premiers visuels de demo dans output/pack_demo/html/slide_XX.html,
rendus ensuite par render.py ("python3 render.py pack_demo").
"""
import pathlib, re, base64

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS = ROOT / "assets" / "fonts"

# ---------- Palette du template (l'eleve remplace l'accent par SA couleur) ----------
CREAM  = "#F6F3EC"   # fond clair editorial
INK    = "#17222F"   # texte principal (encre)
ACCENT = "#C4633C"   # accent terracotta : zone "ta couleur de marque ici"
MUTED  = "#6E7683"   # texte secondaire
ANNOT  = "#8B8578"   # annotations "a personnaliser" (gris chaud, pointilles)
CARD   = "#FFFFFF"   # cartes / encadres

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font_face(weight):
    data = b64(FONTS / f"montserrat-latin-{weight}-normal.woff2", "font/woff2")
    return (f"@font-face{{font-family:'Montserrat';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")
FONT_FACES = "".join(font_face(w) for w in (400,500,600,700,800,900))

COMMON_CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Montserrat',sans-serif !important;
   -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
.slide{{width:1080px;height:1350px;background:{CREAM};position:relative;overflow:hidden;color:{INK};}}
.bg{{position:absolute;inset:0;background:
  radial-gradient(120% 70% at 90% -8%, rgba(196,99,60,0.09) 0%, rgba(246,243,236,0) 55%),
  radial-gradient(110% 70% at -10% 108%, rgba(23,34,47,0.06) 0%, rgba(246,243,236,0) 50%),
  {CREAM};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:8px;background:{ACCENT};z-index:5;}}
.pad{{position:absolute;inset:0;padding:64px 76px 150px;z-index:2;display:flex;flex-direction:column;}}

/* Bandeau haut : logo a remplacer + poignee du compte */
.brandrow{{display:flex;justify-content:space-between;align-items:center;margin-bottom:44px;}}
.logobox{{border:2.5px dashed {ANNOT};border-radius:12px;padding:16px 30px;color:{ANNOT};
  font-weight:700;font-size:21px;letter-spacing:2px;text-transform:uppercase;}}
.handle{{border:2.5px dashed {ANNOT};border-radius:40px;padding:12px 24px;color:{ANNOT};
  font-weight:600;font-size:20px;font-style:italic;}}

.eyebrow{{color:{ACCENT};font-weight:800;font-size:24px;letter-spacing:5px;text-transform:uppercase;margin-bottom:20px;}}
.title{{color:{INK};font-weight:900;font-size:58px;line-height:1.04;letter-spacing:-1.5px;text-transform:uppercase;}}
.title .acc{{color:{ACCENT};}}
.lede{{color:{MUTED};font-weight:500;font-size:26px;line-height:1.4;margin-top:22px;}}

.points{{display:flex;flex-direction:column;gap:24px;flex:1;justify-content:center;}}
.card{{background:{CARD};border-radius:16px;padding:26px 30px;box-shadow:none;border:1.5px solid rgba(23,34,47,0.08);}}
.card .cl{{color:{ACCENT};font-weight:800;font-size:29px;line-height:1.15;}}
.card .cl .n{{display:inline-block;min-width:44px;color:{INK};font-weight:900;}}
.card .ct{{color:{INK};font-weight:500;font-size:24px;line-height:1.35;margin-top:8px;opacity:0.9;}}
.card .ex{{color:{MUTED};font-weight:600;font-style:italic;font-size:21px;margin-top:8px;}}
.card .ex b{{color:{ANNOT};font-weight:800;font-style:normal;}}

/* Note "a personnaliser" : la consigne pour l'eleve, bien visible mais discrete */
.custom{{border:2.5px dashed {ANNOT};border-radius:14px;padding:18px 26px;margin-top:26px;
  color:{ANNOT};font-weight:600;font-size:21px;line-height:1.35;font-style:italic;}}
.custom b{{font-style:normal;font-weight:800;text-transform:uppercase;letter-spacing:1px;}}

/* Pied de page : contact a remplacer */
.footer{{position:absolute;bottom:44px;left:76px;right:76px;display:flex;justify-content:space-between;
  align-items:center;z-index:6;color:{ANNOT};font-weight:600;font-size:20px;font-style:italic;}}
.footer .pill{{border:2.5px dashed {ANNOT};border-radius:40px;padding:12px 26px;}}
"""

def page(body):
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head>'
            f'<body>{body}</body></html>')

def slide_open():
    return '<div class="slide"><div class="bg"></div><div class="topbar"></div>'

def brandrow():
    return ('<div class="brandrow"><div class="logobox">Ton logo ici</div>'
            '<div class="handle">@ta.conciergerie</div></div>')

def footer(left="Ta ville + ta zone", right="Ton site ou ton contact"):
    return (f'<div class="footer"><div class="pill">{left}</div>'
            f'<div class="pill">{right}</div></div></div>')

def acc(w):
    return f'<span class="acc">{w}</span>'

# =====================================================================
# VISUEL 1 : CONVERSION PROPRIETAIRE : pourquoi confier son bien
# =====================================================================
def visuel_01():
    cards = [
        ("1", "Vous récupérez votre temps",
         "Voyageurs, ménage, linge, imprévus : la conciergerie s'occupe de tout, du premier message au départ.", None),
        ("2", "Votre logement est entretenu",
         "Un passage professionnel après chaque séjour : votre bien reste impeccable, séjour après séjour.", None),
        ("3", "Vos revenus sont optimisés",
         "Prix ajustés selon la saison et la demande locale : votre bien travaille au bon tarif toute l'année.", None),
        ("4", "Des voyageurs vérifiés",
         "Profils contrôlés, règlement du logement, caution : votre bien est confié à de bonnes mains.", None),
    ]
    pts = ""
    for n, label, text, ex in cards:
        pts += (f'<div class="card"><div class="cl"><span class="n">{n}.</span>{label}</div>'
                f'<div class="ct">{text}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Propriétaires</div>'
        f'<div class="title">Pourquoi confier votre bien à une {acc("conciergerie")} ?</div>'
        f'<div class="points" style="margin-top:34px;">{pts}</div>'
        '<div class="custom"><b>À personnaliser :</b> remplace la couleur terracotta par TA couleur de marque, '
        'mets ton logo en haut et ta ville en bas. Le texte peut rester tel quel.</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUEL 2 : OFFRES / SERVICES (zones "Exemple :" a remplacer)
# =====================================================================
def visuel_02():
    cards = [
        ("Annonce", "Création et optimisation de votre annonce",
         "Photos mises en valeur, titre travaillé, description qui donne envie de réserver."),
        ("Sejours", "Accueil des voyageurs et départs",
         "Arrivées autonomes ou en personne, état du logement vérifié à chaque départ."),
        ("Entretien", "Ménage professionnel et linge hôtelier",
         "Logement remis à neuf entre chaque séjour, linge blanc qualité hôtel."),
        ("Revenus", "Prix ajustés toute l'année",
         "Tarifs adaptés à la saison, aux événements et à la demande de votre secteur."),
    ]
    pts = ""
    for tag, label, text in cards:
        pts += (f'<div class="card"><div class="cl">{label}</div>'
                f'<div class="ct">{text}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Nos services</div>'
        f'<div class="title">On s\'occupe de {acc("tout")}, vous profitez des revenus</div>'
        f'<div class="points" style="margin-top:34px;">{pts}</div>'
        '<div class="custom"><b>À personnaliser :</b> ces 4 services sont des <b>exemples</b> : '
        'remplace-les par TES prestations réelles (garde 4 blocs maximum pour rester lisible).</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUEL 3 : ASTUCE AIRBNB (conseil a valeur, publiable tel quel)
# =====================================================================
def visuel_03():
    cards = [
        ("1", "Ouvrez tout, lumière naturelle",
         "Rideaux ouverts, lumières allumées : shootez en fin de matinée, jamais au flash."),
        ("2", "Appareil à hauteur de hanche",
         "Pliez les genoux, tenez le téléphone droit à 1,20 m du sol : les pièces paraissent plus grandes."),
        ("3", "Shootez depuis un angle",
         "Placez-vous dans un coin de la pièce pour donner de la profondeur, pas face au mur."),
        ("4", "Zéro objet personnel",
         "Câbles, produits, chaussures : tout disparaît. Linge blanc tiré, serviettes pliées."),
        ("5", "La couverture, c'est la meilleure pièce",
         "Votre photo principale doit être la pièce la plus séduisante, pas la façade."),
    ]
    pts = ""
    for n, label, text in cards:
        pts += (f'<div class="card" style="padding:20px 28px;"><div class="cl" style="font-size:27px;">'
                f'<span class="n">{n}.</span>{label}</div>'
                f'<div class="ct" style="font-size:23px;">{text}</div></div>')
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Astuce propriétaire</div>'
        f'<div class="title">Des photos qui font {acc("réserver")} votre bien</div>'
        f'<div class="points" style="margin-top:26px;gap:16px;">{pts}</div>'
        '<div class="custom" style="margin-top:18px;padding:14px 24px;"><b>À personnaliser :</b> ce conseil se poste tel quel. '
        'Ajoute juste tes couleurs, ton logo et signe avec le nom de ta conciergerie.</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
# VISUEL 4 : NOTRE HISTOIRE (texte "Exemple :" a remplacer par la sienne)
# =====================================================================
def visuel_04():
    body = (slide_open() +
        '<div class="pad">' + brandrow() +
        '<div class="eyebrow">Notre histoire</div>'
        f'<div class="title">Pourquoi j\'ai créé ma {acc("conciergerie")}</div>'
        '<div class="points" style="margin-top:36px;justify-content:center;gap:30px;">'
        '<div class="card"><div class="ex" style="margin-top:0;"><b>Exemple :</b></div>'
        f'<div class="ct" style="font-size:26px;line-height:1.5;margin-top:12px;">'
        'Tout est parti d\'un constat simple : autour de moi, des propriétaires laissaient '
        'leur logement vide une partie de l\'année, faute de temps pour s\'en occuper.'
        '</div></div>'
        '<div class="card">'
        f'<div class="ct" style="font-size:26px;line-height:1.5;">'
        'J\'ai commencé avec un seul logement, celui d\'un proche. Annonce refaite, accueil '
        'soigné, ménage impeccable : les réservations ont suivi, et les avis 5 étoiles aussi.'
        '</div></div>'
        '<div class="card">'
        f'<div class="ct" style="font-size:26px;line-height:1.5;">'
        'Aujourd\'hui, j\'accompagne des propriétaires qui veulent que leur bien rapporte, '
        'sans y consacrer leurs soirées ni leurs week-ends.'
        '</div></div>'
        '</div>'
        '<div class="custom"><b>À personnaliser :</b> remplace ce récit par TON histoire : '
        'ton déclic, ta ville, ton premier logement, ce qui te rend fier aujourd\'hui.</div>'
        '</div>' + footer())
    return page(body)

# =====================================================================
BUILDERS = [visuel_01, visuel_02, visuel_03, visuel_04]

def check_no_forbidden(html, name):
    # mot "gestion" interdit (et derives), tirets longs interdits, emojis interdits
    text = re.sub(r'data:[^"\']+', '', html)
    for pat, label in [(r'(?i)gestion', 'mot "gestion"'),
                       (r'[‒–—―─﹣－]', 'tiret long'),
                       (r'[\U0001F000-\U0001FAFF☀-➿]', 'emoji')]:
        m = re.search(pat, text)
        assert not m, f"{name} : {label} detecte ({m.group(0)!r})"

def main():
    out = ROOT / "output" / "pack_demo" / "html"
    out.mkdir(parents=True, exist_ok=True)
    for i, build in enumerate(BUILDERS, 1):
        html = build()
        name = f"slide_{i:02d}.html"
        check_no_forbidden(html, name)
        (out / name).write_text(html, encoding="utf-8")
        print(f"OK {name}")
    print(f"HTML dans {out}")

if __name__ == "__main__":
    main()
