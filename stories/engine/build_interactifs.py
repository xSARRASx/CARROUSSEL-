#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FORMATS INTERACTIFS (voix de Martin, 04/08/2026 au soir) :
  - "pas toujours des trucs a repondre" -> CTA legers, pas de mot-cle partout
  - "des questionnaires, des questions-reponses" -> sequences QUIZ (la story
    pose la question, Martin ajoute le sticker sondage Instagram dans la zone
    libre ; la story suivante donne la reponse et l'explication)
  - "garder des trucs pour les temoignages, la derniere annonce de nos eleves,
    avec case vide pour mettre des photos" -> gabarits temoignage a zone
    pointillee (les SEULS avec placeholder, volontairement)
  - pas de logo ("simple, efficace")

Regle V5 respectee : 1 sequence = 1 seul theme visuel.
  Quiz          -> theme navy gros titres
  Sondages      -> theme ciel dore
  Temoignages   -> theme mer

Rendu : python3 render_stories.py interactifs-01
"""
import pathlib
from build_themes import (COMMON_CSS, photo_open, navy_open, underline, nb,
                          bleu, NAVY, ORANGE, BLUE, BLANC)

ROOT = pathlib.Path(__file__).resolve().parents[1]

STORIES = {}

# ============================================================================
# QUIZ — theme navy gros titres. La story pose la question et laisse la
# moitie basse LIBRE : Martin y colle le sticker sondage Instagram
# (vrai/faux ou QCM). La story suivante revele la reponse.
# Contenu tire des videos (algo 2026, caution).
# ============================================================================

def quiz_q(num, total, kind, question, hint):
    return (navy_open() + '<div class="pad" style="align-items:center;text-align:center;">'
            f'<div style="font-weight:800;font-size:30px;letter-spacing:8px;color:{ORANGE};'
            f'text-transform:uppercase;">quiz {num}/{total}</div>'
            f'<div style="font-weight:900;font-size:120px;line-height:1;letter-spacing:-3px;'
            f'text-transform:uppercase;margin-top:44px;">{kind}</div>'
            f'<div style="font-weight:700;font-size:44px;line-height:1.35;margin-top:56px;'
            f'max-width:860px;">{nb(question)}</div>'
            f'<div style="font-weight:500;font-style:italic;font-size:28px;'
            f'color:rgba(255,255,255,0.7);margin-top:46px;">{nb(hint)}</div>'
            '</div></div>')

def quiz_r(verdict, explication, chiffre=None):
    ch = (f'<div style="font-weight:900;font-size:150px;line-height:1;color:{ORANGE};'
          f'letter-spacing:-5px;margin-top:40px;">{chiffre}</div>') if chiffre else ''
    return (navy_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
            f'<div style="font-weight:900;font-size:170px;line-height:1;color:{ORANGE};'
            f'text-transform:uppercase;letter-spacing:-4px;">{verdict}</div>' + ch +
            f'<div style="width:120px;height:7px;background:{BLUE};border-radius:4px;margin:52px auto;"></div>'
            f'<div style="font-weight:600;font-size:36px;line-height:1.5;color:rgba(255,255,255,0.92);'
            f'max-width:840px;">{nb(explication)}</div>'
            '</div></div>')

STORIES["quiz_navy_01"] = (
    navy_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div style="font-weight:900;font-size:230px;line-height:1;letter-spacing:-6px;'
    f'text-transform:uppercase;">QUIZ</div>'
    f'<div style="font-weight:900;font-size:56px;line-height:1.2;text-transform:uppercase;'
    f'margin-top:40px;">T\'es à jour sur<br><span style="color:{ORANGE};">Airbnb 2026</span>&nbsp;?</div>'
    f'<div style="width:120px;height:7px;background:{ORANGE};border-radius:4px;margin:50px auto;"></div>'
    '<div style="font-weight:600;font-size:34px;line-height:1.5;color:rgba(255,255,255,0.85);">'
    '3 questions. Vote à chaque fois,<br>la réponse arrive juste après.</div>'
    '</div></div>')

STORIES["quiz_navy_02"] = quiz_q(1, 3, "Vrai ou faux ?",
    "Le badge Superhost booste ton classement en 2026.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz_navy_03"] = quiz_r("Faux",
    "Le Superhost est obsolète. Le nouveau Graal, c'est Guest Favorite : "
    "25 % du classement. Critères : note 4,9+ et au moins 5 avis en 2 ans.")

STORIES["quiz_navy_04"] = quiz_q(2, 3, "8, 15 ou 30 ?",
    "Combien pèse ta photo de couverture dans ton classement (en %) ?",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz_navy_05"] = quiz_r("8 %",
    "Et le séjour réel pèse 50 %. Réservations, avis, zéro problème : c'est ça "
    "que l'algorithme regarde en premier. La photo vient après.")

STORIES["quiz_navy_06"] = quiz_q(3, 3, "Vrai ou faux ?",
    "Ta conciergerie peut débiter elle-même la caution du voyageur.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz_navy_07"] = quiz_r("Faux",
    "Si la conciergerie déclenche le débit, c'est du maniement de fonds pour "
    "le compte de tiers : illégal au sens de la loi Hoguet. La caution part "
    "toujours du compte du propriétaire.")

STORIES["quiz_navy_08"] = (
    navy_open() + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div style="font-weight:900;font-size:96px;line-height:1.05;text-transform:uppercase;">'
    f'3/3&nbsp;? <span style="color:{ORANGE};">Respect.</span></div>'
    '<div style="font-weight:600;font-size:36px;line-height:1.5;color:rgba(255,255,255,0.9);'
    'max-width:820px;margin-top:52px;">Moins&nbsp;? Tout est expliqué en détail dans les '
    'vidéos de la chaîne. On en refait un bientôt.</div>'
    '</div></div>')

# ============================================================================
# SONDAGES DIAGNOSTIC — theme ciel dore. Zones libres pour les stickers
# Instagram (sondage / boite a questions). Aucun CTA mot-cle.
# ============================================================================

def sondage(kicker, title, note):
    return (photo_open("bg_ciel_dore") + '<div class="pad">'
            f'<div class="hand" style="font-size:56px;margin-top:30px;">{nb(kicker)}</div>'
            f'<div class="serif" style="font-size:76px;line-height:1.16;margin-top:24px;">{nb(title)}</div>'
            + underline(430, BLANC, 84, 700) +
            f'<div class="hand" style="font-size:48px;position:absolute;right:130px;top:760px;">{nb(note)}</div>'
            '</div></div>')

STORIES["sondage_ciel_01"] = sondage("dis-nous tout",
    f'Tu es plutôt {bleu("conciergerie")} ou {bleu("sous-location")}&nbsp;?',
    "vote juste en dessous")
STORIES["sondage_ciel_02"] = sondage("question du jour",
    f'Ta plus grosse {bleu("galère")} en ce moment&nbsp;?',
    "vote juste en dessous")
STORIES["sondage_ciel_03"] = sondage("on lit tout",
    f'Raconte ta {bleu("situation")} en une phrase.',
    "la boîte à questions est juste là")

# ============================================================================
# TEMOIGNAGES — theme mer. Les SEULS gabarits avec case vide (pointilles) :
# Martin colle l'annonce / le screenshot de l'eleve dans Instagram
# (sticker photo). Ne jamais inventer un temoignage.
# ============================================================================

def fleche_mer(x, y, w=200, h=240):
    path = f"M {w*0.85:.0f} 18 C {w*0.3:.0f} {h*0.25:.0f}, {w*0.1:.0f} {h*0.55:.0f}, {w*0.4:.0f} {h-26:.0f}"
    head = (f'<path d="M {w*0.4-32:.0f} {h-88:.0f} L {w*0.4:.0f} {h-22:.0f}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>'
            f'<path d="M {w*0.4+28:.0f} {h-82:.0f} L {w*0.4:.0f} {h-22:.0f}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>')
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" fill="none">'
            f'<path d="{path}" stroke="{BLANC}" stroke-width="11" stroke-linecap="round"/>{head}</svg>')

def case_vide(x, y, w, h, note):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            'border:5px dashed rgba(255,255,255,0.8);border-radius:26px;"></div>'
            f'<div class="hand" style="font-size:44px;position:absolute;left:{x+50}px;'
            f'top:{y+h//2-30}px;color:rgba(255,255,255,0.95);">{nb(note)}</div>')

STORIES["temoin_mer_01"] = (
    photo_open("bg_mer_calme") + '<div class="pad">'
    f'<div class="serif" style="font-size:80px;line-height:1.1;text-align:right;margin-top:20px;">'
    f'+&nbsp;1 pour {bleu("[Prénom]")}</div>'
    + fleche_mer(700, 460) + case_vide(110, 640, 540, 700, "colle l'annonce<br>de l'élève ici")
    + '<div class="hand" style="font-size:60px;position:absolute;right:100px;bottom:420px;">'
    'Bravo [Prénom]&nbsp;!</div>'
    '</div></div>')

STORIES["temoin_mer_02"] = (
    photo_open("bg_mer_calme") + '<div class="pad">'
    '<div class="hand" style="font-size:56px;margin-top:10px;">tombé ce matin</div>'
    f'<div class="serif" style="font-size:64px;line-height:1.15;margin-top:20px;">'
    f'La {bleu("dernière annonce")} de nos élèves.</div>'
    + case_vide(190, 620, 700, 760, "le screenshot ici")
    + '</div></div>')

STORIES["temoin_mer_03"] = (
    photo_open("bg_mer_calme") + '<div class="pad">'
    '<div class="hand" style="font-size:56px;margin-top:10px;">le message du jour</div>'
    f'<div class="serif" style="font-size:64px;line-height:1.15;margin-top:20px;">'
    f'Ce qu\'on a reçu de {bleu("[Prénom]")}.</div>'
    + case_vide(190, 600, 700, 720, "le message<br>WhatsApp ici")
    + '<div class="hand" style="font-size:54px;position:absolute;right:120px;bottom:410px;">'
    'fiers d\'eux</div>'
    '</div></div>')

SLUG = "interactifs-01"
DASHES = "—–‒―⎯﹣－─"

def main():
    out = ROOT / "output" / SLUG / "html"
    out.mkdir(parents=True, exist_ok=True)
    td = 0
    for name, body in STORIES.items():
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>{COMMON_CSS}</style></head><body>{body}</body></html>'
        d = [ch for ch in html if ch in DASHES]
        if d: print(f"  ALERTE tiret {name}: {set(d)}"); td += len(d)
        (out / f"{name}.html").write_text(html, encoding="utf-8")
    print(f"{len(STORIES)} stories ecrites dans {out}. Tirets longs: {td}")

if __name__ == "__main__":
    main()
