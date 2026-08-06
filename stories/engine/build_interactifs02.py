#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERACTIFS 02 — quiz et sondage tirés de la vidéo du 10 juillet 2026
(condamnation à 220 000 €, ID YiAaGhoimhA).

La story pose la question et laisse la moitié basse LIBRE : Martin y colle le
sticker sondage Instagram. La story suivante révèle la réponse.
Aucun CTA mot-clé sur ces formats (règle de Martin).

Style unique photo fait main, logo partout, fonds tous différents.
Rendu : python3 render_stories.py interactifs-02
"""
from photo_style import open_photo, underline, acc, nb, BLANC, BLEU, write_lot

STORIES = {}

def quiz_q(bg, num, total, kind, question, hint):
    return (open_photo(bg) + '<div class="pad" style="align-items:center;text-align:center;">'
            f'<div class="hand" style="font-size:52px;">quiz {num}/{total}</div>'
            f'<div class="serif" style="font-size:100px;line-height:1.05;margin-top:30px;">{nb(kind)}</div>'
            f'<div class="veil" style="margin-top:52px;max-width:870px;">'
            f'<div class="vt" style="font-size:31px;font-weight:700;">{nb(question)}</div></div>'
            f'<div class="hand" style="font-size:44px;margin-top:42px;opacity:0.95;">{nb(hint)}</div>'
            '</div></div>')

def quiz_r(bg, verdict, explication, chiffre=None):
    ch = (f'<div class="serif" style="font-size:120px;line-height:1;color:{BLEU};'
          f'margin-top:34px;">{chiffre}</div>') if chiffre else ''
    return (open_photo(bg) + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
            f'<div class="serif" style="font-size:150px;line-height:1;">{acc(verdict)}</div>' + ch +
            f'<div style="margin:44px auto;">{underline(220, BLANC, cls="inline")}</div>'
            f'<div class="veil" style="max-width:860px;">'
            f'<div class="vt" style="font-size:29px;">{nb(explication)}</div></div>'
            '</div></div>')

STORIES["quiz02_01"] = (
    open_photo("bg_bureau_matin") + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:190px;line-height:1;">QUIZ</div>'
    f'<div class="serif" style="font-size:52px;line-height:1.2;margin-top:36px;">'
    f'Tu connais tes {acc("obligations")}&nbsp;?</div>'
    f'<div style="margin:46px auto;">{underline(220, BLANC, cls="inline")}</div>'
    '<div class="hand" style="font-size:48px;line-height:1.3;">3 questions sur la condamnation<br>'
    'à 220 000 €. La réponse arrive après.</div>'
    '</div></div>')

STORIES["quiz02_02"] = quiz_q("bg_immeuble_dore", 1, 3, "Vrai ou faux ?",
    "Avoir la carte G aurait évité la condamnation de la conciergerie.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz02_03"] = quiz_r("bg_village", "Faux",
    "La carte G n'apparaît nulle part dans l'affaire. La conciergerie n'a pas été "
    "condamnée pour un défaut de statut, mais pour un défaut de vérification : elle "
    "n'avait pas contrôlé l'autorisation de changement d'usage.")

STORIES["quiz02_04"] = quiz_q("bg_terrasse", 2, 3, "Qui a payé ?",
    "Dans cette affaire, qui a été condamné à 220 000 € : le propriétaire, la conciergerie, ou les deux ?",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz02_05"] = quiz_r("bg_ville_doree", "Les deux",
    "220 000 € pour le propriétaire, et la même somme pour la conciergerie. C'est une "
    "première en France. Déléguer ne protège pas le propriétaire, et encaisser des "
    "prestations ne protège pas la conciergerie.", chiffre="× 2")

STORIES["quiz02_06"] = quiz_q("bg_lac", 3, 3, "Vrai ou faux ?",
    "Le numéro d'enregistrement suffit : avec lui, pas besoin d'autorisation de changement d'usage.",
    "vote avec le sondage, la réponse arrive")
STORIES["quiz02_07"] = quiz_r("bg_montagne", "Faux",
    "Ce sont deux étages différents, et ils se cumulent. Le numéro d'enregistrement ne "
    "protège pas du changement d'usage, et l'autorisation de changement d'usage ne "
    "dispense pas du numéro. La conciergerie doit vérifier les deux, pour chaque bien.")

STORIES["quiz02_08"] = (
    open_photo("bg_plage_aube") + '<div class="pad" style="justify-content:center;align-items:center;text-align:center;">'
    f'<div class="serif" style="font-size:86px;line-height:1.1;">3/3&nbsp;? {acc("Bravo.")}</div>'
    '<div class="veil" style="max-width:820px;margin-top:52px;">'
    '<div class="vt" style="font-size:29px;">Moins&nbsp;? Tout est détaillé dans la vidéo sur la '
    'chaîne : les faits, la checklist avant publication, et les lignes rouges à ne pas '
    'franchir.</div></div>'
    '</div></div>')

# --------------------------------------------------------------- sondages liés

def sondage(bg, kicker, title, note):
    return (open_photo(bg) + '<div class="pad">'
            f'<div class="hand" style="font-size:56px;margin-top:30px;">{nb(kicker)}</div>'
            f'<div class="serif" style="font-size:72px;line-height:1.16;margin-top:24px;">{nb(title)}</div>'
            + underline(430, BLANC, 84, 720) +
            f'<div class="hand" style="font-size:48px;position:absolute;right:130px;top:780px;">{nb(note)}</div>'
            '</div></div>')

CHANGEMENT_USAGE = acc("changement d'usage")
STORIES["sondage02_01"] = sondage("bg_ciel_rose", "dis-nous franchement",
    f"Tu vérifies l'autorisation de {CHANGEMENT_USAGE} avant de publier&nbsp;?",
    "vote juste en dessous")
STORIES["sondage02_02"] = sondage("bg_salon_cosy", "question du jour",
    f'Ton contrat conciergerie, il date de {acc("quand")}&nbsp;?',
    "vote juste en dessous")

SLUG = "interactifs-02"

def main():
    write_lot(SLUG, STORIES)

if __name__ == "__main__":
    main()
