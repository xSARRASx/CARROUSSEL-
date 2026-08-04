#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CAPTURES D'INTERFACE POUR LE MONTAGE DES SHORTS — fabriquees en HTML.

POURQUOI (regle de Martin, 03/08/2026) : "je ne veux pas que ca fasse IA,
je veux vraiment naturel". Or l'IA image est INCAPABLE d'ecrire du texte
d'interface sans fautes : la capture Airbnb generee par Gemini sortait
"Appartement Lumiuxeux", "Espace de trovail dedie", "Vous ne paieer
quaprets la confirmation", des dates "10 /Uin - 20 /24"... Ca se voit en
une seconde et ca ruine le montage.

LA SOLUTION : tout ce qui contient du TEXTE LISIBLE est ecrit en HTML/CSS
puis photographie par un vrai navigateur (Playwright), exactement comme les
stories. Resultat : typographie nette, zero faute, espaces insecables
francais, rendu credible d'une vraie capture d'ecran.

REGLE GENERALE POUR LES ASSETS :
  - texte lisible dans l'image   -> HTML (ce fichier)
  - logo d'une vraie marque      -> le VRAI fichier officiel de la marque
  - illustration / icone / photo -> Gemini (gen_assets_shorts.py)

Usage : python3 build_captures.py        (HTML + PNG d'un coup)
"""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
FONTS = REPO / "pipeline" / "assets" / "fonts"
PHOTOS = ROOT / "assets-montage"
BGS = REPO / "stories" / "assets" / "backgrounds"
OUT_HTML = ROOT / "captures" / "html"
OUT_PNG = ROOT / "assets-montage"        # les PNG finaux rejoignent le kit

ROUGE_AIRBNB = "#FF385C"
INK = "#222222"
GRIS = "#717171"
BORD = "#DDDDDD"

def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

def font_face(family, file, weight):
    data = b64(FONTS / file, "font/woff2")
    return (f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data}) format('woff2');}}")

FONT_FACES = "".join([
    font_face("Mont", "montserrat-latin-400-normal.woff2", 400),
    font_face("Mont", "montserrat-latin-500-normal.woff2", 500),
    font_face("Mont", "montserrat-latin-600-normal.woff2", 600),
    font_face("Mont", "montserrat-latin-700-normal.woff2", 700),
    font_face("Mont", "montserrat-latin-800-normal.woff2", 800),
])

def nb(t):
    """Typographie FR : espace insecable avant ? ! : ; et dans les guillemets."""
    for p in ("?", "!", ":", ";"):
        t = t.replace(f" {p}", f" {p}")
    return t.replace("« ", "« ").replace(" »", " »")

def photo(name, folder=None):
    """Renvoie une image du kit (ou un fond de stories) en base64."""
    src = (folder or PHOTOS) / name
    if not src.exists():
        return None
    return b64(src, "image/png" if src.suffix == ".png" else "image/jpeg")

# Le "Belo" d'Airbnb, redessine proprement en SVG (forme nette, pas de bavure IA).
BELO = ('<svg viewBox="0 0 32 32" width="52" height="52" fill="none">'
        '<path d="M16 3.2c-1.9 0-3.2 1.2-4.4 3.5-1 1.9-2.4 4.9-4 8.5-1.1 2.5-1.8 4.2-2.1 5.2'
        '-.3 1-.5 1.9-.5 2.7 0 3.2 2.4 5.7 5.6 5.7 2.2 0 4.1-1.1 5.4-2.8 1.3 1.7 3.2 2.8 5.4 2.8'
        ' 3.2 0 5.6-2.5 5.6-5.7 0-.8-.2-1.7-.5-2.7-.3-1-1-2.7-2.1-5.2-1.6-3.6-3-6.6-4-8.5'
        'C19.2 4.4 17.9 3.2 16 3.2Zm0 2.6c.8 0 1.5.6 2.3 2.2.9 1.8 2.3 4.7 3.9 8.3 1 2.4 1.7 4 2 4.9'
        '.2.7.3 1.3.3 1.8 0 1.8-1.3 3.1-3 3.1-1.6 0-3-1-4-2.5 1.6-2.1 2.6-4 2.6-5.6 0-2.5-1.8-4.3-4.1-4.3'
        's-4.1 1.8-4.1 4.3c0 1.6 1 3.5 2.6 5.6-1 1.5-2.4 2.5-4 2.5-1.7 0-3-1.3-3-3.1 0-.5.1-1.1.3-1.8'
        '.3-.9 1-2.5 2-4.9 1.6-3.6 3-6.5 3.9-8.3.8-1.6 1.5-2.2 2.3-2.2Zm0 12.3c1 0 1.6.7 1.6 1.9'
        ' 0 1-.6 2.3-1.6 3.8-1-1.5-1.6-2.8-1.6-3.8 0-1.2.6-1.9 1.6-1.9Z" fill="' + ROUGE_AIRBNB + '"/>'
        '</svg>')

def etoiles(n=5, taille=30, couleur="#FFB400"):
    une = (f'<svg viewBox="0 0 24 24" width="{taille}" height="{taille}" fill="{couleur}">'
           '<path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z"/></svg>')
    return f'<span style="display:inline-flex;gap:3px;vertical-align:-5px;">{une * n}</span>'

CSS = f"""
{FONT_FACES}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;
   text-rendering:geometricPrecision;font-family:'Mont',sans-serif;}}
.shot{{width:1080px;height:1920px;position:relative;overflow:hidden;background:#fff;color:{INK};}}
.bar{{height:96px;display:flex;align-items:center;justify-content:space-between;
  padding:0 44px;border-bottom:1px solid {BORD};}}
.bar .logo{{display:flex;align-items:center;gap:10px;}}
.bar .wordmark{{font-weight:800;font-size:38px;color:{ROUGE_AIRBNB};letter-spacing:-1px;}}
.ico{{width:44px;height:44px;stroke:{INK};stroke-width:2;fill:none;}}
.gal{{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:8px;
  height:660px;padding:24px 24px 0;}}
.gal .c{{background-size:cover;background-position:center;background-color:#eee;}}
.gal .c1{{grid-row:1 / span 2;border-radius:20px 0 0 20px;}}
.gal .c3{{border-radius:0 20px 0 0;}}
.gal .c5{{border-radius:0 0 20px 0;}}
.body{{padding:38px 44px 0;}}
.h1{{font-weight:700;font-size:52px;line-height:1.22;letter-spacing:-0.5px;}}
.loc{{font-size:33px;color:{GRIS};margin-top:14px;}}
.meta{{display:flex;align-items:center;gap:14px;margin-top:26px;font-size:31px;font-weight:600;}}
.meta .g{{color:{GRIS};font-weight:400;}}
.sep{{height:1px;background:{BORD};margin:34px 0;}}
.prix{{display:flex;align-items:baseline;gap:12px;}}
.prix .n{{font-weight:800;font-size:56px;}}
.prix .u{{font-size:33px;color:{GRIS};}}
.equip{{display:flex;flex-direction:column;gap:26px;margin-top:30px;}}
.equip .l{{display:flex;align-items:center;gap:22px;font-size:32px;}}
.equip svg{{flex-shrink:0;}}
.avis .tete{{display:flex;align-items:center;gap:20px;}}
.avis .pastille{{width:64px;height:64px;border-radius:50%;background:#EFEFEF;color:{INK};
  font-weight:700;font-size:30px;display:flex;align-items:center;justify-content:center;}}
.avis .nom{{font-weight:700;font-size:31px;}}
.avis .date{{font-size:27px;color:{GRIS};margin-top:4px;}}
.avis .txt{{font-size:31px;line-height:1.5;margin-top:20px;color:#3a3a3a;}}
.cta{{position:absolute;left:44px;right:44px;bottom:56px;height:112px;border-radius:18px;
  background:{ROUGE_AIRBNB};color:#fff;font-weight:700;font-size:38px;
  display:flex;align-items:center;justify-content:center;}}
.badge{{display:inline-block;background:#fff;border:1px solid {BORD};border-radius:999px;
  padding:12px 26px;font-weight:700;font-size:28px;box-shadow:0 2px 8px rgba(0,0,0,0.06);}}
.shot-carre{{width:1024px;height:1024px;display:flex;align-items:center;justify-content:center;}}
.badgebox{{display:flex;flex-direction:column;align-items:center;gap:18px;}}
.badgebox .bnom{{font-weight:800;font-size:104px;letter-spacing:-2px;line-height:1.05;
  text-align:center;}}
.badgebox .bsous{{font-weight:500;font-size:36px;color:{GRIS};text-align:center;
  max-width:820px;}}
"""

def svg_line(d, size=40):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
            f'stroke="{INK}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{d}</svg>')

WIFI = svg_line('<path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5.5 5.5 0 0 1 7 0"/>'
                '<circle cx="12" cy="19.5" r="1.1" fill="' + INK + '" stroke="none"/>'
                '<path d="M1.5 9a15 15 0 0 1 21 0"/>')
BUREAU = svg_line('<rect x="3" y="5" width="18" height="11" rx="1.5"/><path d="M8 20h8M12 16v4"/>')
MACHINE = svg_line('<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="12" cy="13" r="4"/>'
                   '<circle cx="8" cy="6.5" r="0.6" fill="' + INK + '" stroke="none"/>')
CLIM = svg_line('<rect x="3" y="5" width="18" height="7" rx="2"/><path d="M7 15v2M12 15v3M17 15v2"/>')

def capture_airbnb():
    """Capture d'annonce Airbnb : tout le texte est ecrit, donc parfait.

    La galerie utilise les VRAIES photos d'interieur du kit (nettes) ; si
    elles ne sont pas encore generees, on retombe sur les fonds de stories.
    """
    prefs = ["photo-salon.png", "photo-cuisine.png", "photo-chambre.png",
             "photo-salle-de-bain.png", "photo-appartement.png"]
    cells = [photo(n) for n in prefs]
    secours = [photo("bg_salon_cosy.jpg", BGS), photo("bg_terrasse.jpg", BGS),
               photo("bg_bureau_matin.jpg", BGS), photo("bg_immeuble_dore.jpg", BGS),
               photo("bg_lac.jpg", BGS)]
    cells = [c or secours[i] for i, c in enumerate(cells)]
    gal = "".join(
        f'<div class="c c{i}" style="{f"background-image:url({src});" if src else ""}"></div>'
        for i, src in enumerate(cells[:5], 1))
    equipements = [(WIFI, "Wifi rapide, 200 Mb/s"), (BUREAU, "Espace de travail dédié"),
                   (MACHINE, "Lave-linge"), (CLIM, "Climatisation")]
    eq = "".join(f'<div class="l">{ico}<span>{nb(t)}</span></div>' for ico, t in equipements)
    return f"""<div class="shot">
  <div class="bar">
    <div class="logo">{BELO}<span class="wordmark">airbnb</span></div>
    <span class="badge">Coup&nbsp;de&nbsp;cœur voyageurs</span>
  </div>
  <div class="gal">{gal}</div>
  <div class="body">
    <div class="h1">{nb("Appartement lumineux et moderne, hypercentre")}</div>
    <div class="loc">Bordeaux, France</div>
    <div class="meta">{etoiles()}<span>4,92</span>
      <span class="g">· 358 commentaires · Superhôte</span></div>
    <div class="sep"></div>
    <div class="prix"><span class="n">120&nbsp;€</span><span class="u">par nuit</span></div>
    <div class="equip">{eq}</div>
    <div class="sep"></div>
    <div class="avis">
      <div class="tete"><div class="pastille">C</div>
        <div><div class="nom">Camille</div><div class="date">Juillet 2026</div></div></div>
      <div class="txt">{nb("« Appartement impeccable, très bien situé et arrivée "
                           "autonome parfaite. On reviendra sans hésiter. »")}</div>
    </div>
  </div>
  <div class="cta">Réserver</div>
</div>"""

def badge_plateforme(nom, couleur, taille=104):
    """Carton NOM DE PLATEFORME, en remplacement d'un faux logo genere par IA.

    ⚠️ Ce n'est PAS le logotype officiel de la marque, et il ne cherche pas a
    en avoir l'air : juste le nom ecrit proprement dans la couleur de la
    marque. L'audit v2 a recale la version precedente parce qu'elle ajoutait
    un pictogramme maison et une baseline inventes, IDENTIQUES pour deux
    marques differentes : ca fabriquait un faux logo.
    Pour le vrai logotype : telecharger le fichier de l'espace presse.
    """
    return f"""<div class="shot shot-carre">
  <div class="badgebox">
    <div class="bnom" style="color:{couleur};font-size:{taille}px;">{nom}</div>
  </div>
</div>"""

MEDAILLE = ('<svg viewBox="0 0 24 24" width="96" height="96" fill="none" stroke="#C9A227" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<circle cx="12" cy="14.5" r="6.2" fill="#FBF3DA"/>'
            '<path d="M8.6 8.6 6 2.5h5l2 4.2M15.4 8.6 18 2.5h-5"/>'
            '<circle cx="12" cy="14.5" r="3.1"/></svg>')

def badge_texte(pictogramme, gros, sous_titre, couleur, taille_gros=112):
    """Badge a texte fabrique en HTML : orthographe garantie, rendu net.

    C'est le remplacant de tous les visuels ou l'IA devait ecrire des mots
    (elle les ecrit faux : "PROPRIETERE", "Trouviez", "FEBRUER"...).
    """
    return f"""<div class="shot shot-carre">
  <div class="badgebox">
    {pictogramme}
    <div class="bnom" style="color:{couleur};font-size:{taille_gros}px;">{nb(gros)}</div>
    <div class="bsous">{nb(sous_titre)}</div>
  </div>
</div>"""

SHOTS = {
    "capture-annonce-airbnb": capture_airbnb(),
    "logo-abritel": badge_plateforme("Abritel", "#1E4C9A", 130),
    "logo-booking": badge_plateforme("Booking.com", "#003580", 104),
    "icone-lmnp": badge_texte("", "LMNP", "Loueur meublé non professionnel", "#1E4C9A", 150),
    "icone-experience": badge_texte(MEDAILLE, "11 ans", "d'expérience sur le terrain", "#0d1b2e", 128),
}

# Les captures carrees (badges) sont rendues en 1024x1024 comme les icones.
TAILLES = {n: (1024, 1024) for n in
           ("logo-abritel", "logo-booking", "icone-lmnp", "icone-experience")}

def main():
    OUT_HTML.mkdir(parents=True, exist_ok=True)
    OUT_PNG.mkdir(parents=True, exist_ok=True)
    for name, body in SHOTS.items():
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{CSS}</style></head><body>{body}</body></html>')
        (OUT_HTML / f"{name}.html").write_text(html, encoding="utf-8")
    print(f"{len(SHOTS)} captures HTML ecrites dans {OUT_HTML}")

    if "--html-only" in sys.argv:
        return
    from playwright.sync_api import sync_playwright
    from PIL import Image
    CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        for name in SHOTS:
            w, h = TAILLES.get(name, (1080, 1920))
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            pg.goto((OUT_HTML / f"{name}.html").as_uri())
            pg.wait_for_function("document.fonts.ready.then(()=>true)")
            pg.wait_for_timeout(300)
            tmp = OUT_PNG / f"{name}.raw.png"
            pg.screenshot(path=str(tmp), clip={"x": 0, "y": 0, "width": w, "height": h})
            im = Image.open(tmp).convert("RGB").resize((w, h), Image.LANCZOS)
            im.save(OUT_PNG / f"{name}.png", "PNG", optimize=True)
            tmp.unlink()
            pg.close()
            print(f"{name}.png  {w}x{h}")
        b.close()

if __name__ == "__main__":
    main()
