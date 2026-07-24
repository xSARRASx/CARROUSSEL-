#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carrousel Le Sous Loueur (angle coaching / alerte reforme) genere a partir de la
vraie video YouTube "Airbnb tue le micro BIC" (transcription Etape 2).

Reutilise les gabarits du moteur build_lesousloueur.py (aucune duplication de
l'engine). Ecrit les 10 slides HTML dans output/<SLUG>/html, a rendre via render.py.

Usage : python3 build_lsl_airbnb_microbic.py && python3 render.py lsl_airbnb_microbic
"""
import pathlib
from build_lesousloueur import (
    cover, content, content_ba, cta, closing, acc, COMMON_CSS, ROOT, DASHES,
)

SLUG = "lsl_airbnb_microbic"

SLIDES = [
  cover("Le Sous Loueur",
        f'La commission Airbnb<br>passe à {acc("15,5 %")}',
        "Pourquoi ça tue le micro-BIC le 13 octobre 2026",
        "11 ans de terrain pour décrypter la réforme avec toi."),

  content(1, "Ce qui<br>change", "La fin du système partagé",
    [("Commission unique","Avant : 3 % pour toi, 14 à 16 % pour le voyageur. Dès le 13 octobre, une seule commission de 15,5 %, à ta charge."),
     ("Comme sur Booking","Le voyageur ne paie plus les frais à part : tout passe dans ton prix."),
     ("Le vrai taux","Airbnb est en Irlande et ajoute 20 % de TVA (taxe sur la valeur ajoutée). Le coût réel monte à 18,6 %."),
     ("Déjà en cours","Te connecter à un channel manager, l'outil qui synchronise tes annonces, te bascule automatiquement dans ce système.")],
    "À retenir", "15,5 % affiché, mais 18,6 % réellement supporté."),

  content(2, "Le micro<br>BIC coule", "Tu paies l'impôt sur l'argent d'Airbnb",
    [("Recettes brutes","En micro-BIC (Bénéfices Industriels et Commerciaux), tu déclares tout ce que paie le voyageur, commission comprise."),
     ("Charge non déduite","Cette commission, tu ne peux pas la retirer. Tu es imposé sur de l'argent qu'Airbnb garde."),
     ("L'abattement fond","Ton abattement de 30 % ne vaut plus vraiment que 14 %. Classé en meublé, le 50 % tombe à 39 %."),
     ("La double peine","Le voyageur paie plus cher, et toi tu ne gagnes pas un euro de plus.")],
    "À retenir", "Le micro-BIC devient une machine à payer trop d'impôt."),

  content(3, "Le piège<br>du prix", "Augmenter de 15,5 %, c'est déjà perdre",
    [("La marge descendante","On calcule toujours la commission sur le nouveau prix, jamais sur l'ancien."),
     ("Le bon calcul","Pour toucher la même chose, divise ton prix cible par 0,814."),
     ("Pas 18,6 mais 23 %","C'est la vraie hausse à appliquer pour ne rien perdre sur ta marge."),
     ("Avant le 13 octobre","Recalcule tes tarifs maintenant, pas trois mois trop tard.")],
    "Repère", "Prix juste égale prix voulu divisé par 0,814."),

  content(4, "Le fisc<br>voit tout", "Ta déclaration se remplit toute seule",
    [("La DAC7","Cette directive européenne oblige Airbnb, Booking et Abritel à transmettre tes revenus bruts au fisc."),
     ("Déclaration pré-remplie","Tes montants arrivent déjà dans ta déclaration, avec ton identité."),
     ("L'écart se voit","Déclarer ton net laissait 3 % d'écart. Aujourd'hui c'est 19 %, donc un contrôle quasi assuré."),
     ("Fini les approximations","Tu déclares le brut, point. Le formulaire ne prévoit rien d'autre.")],
    "À retenir", "Ce que tu ne déclares pas, le fisc le connaît déjà."),

  content_ba(5, "Micro<br>ou réel", "Le régime réel change la donne",
    "Micro-BIC : tu paies l'impôt sur le brut, commission incluse, sans rien déduire.",
    "Régime réel : tu déduis tout et tu amortis le bien. Souvent zéro impôt pendant des années.",
    "Exemple", "30 000 € de recettes : environ 2 000 € d'impôt économisés chaque année."),

  content(6, "La force<br>du réel", "Amortir, l'arme du loueur meublé",
    [("Tout se déduit","Commissions, TVA, taxe foncière, assurance, intérêts, comptable, ménage."),
     ("L'amortissement","En LMNP (Loueur Meublé Non Professionnel), tu déduis l'usure du bien chaque année."),
     ("Souvent zéro impôt","En moyenne, tu neutralises ton résultat pendant environ huit ans."),
     ("L'objection revente","Les amortissements repris à la vente restent un impôt différé, à taux réduit, pas un piège.")],
    "À retenir", "Le réel n'est pas plus compliqué, il est plus intelligent."),

  content(7, "Tes choix<br>avant octobre", "Quatre décisions à prendre maintenant",
    [("Simule d'abord","Compare micro et réel sur tes propres chiffres avant toute décision."),
     ("Fais classer ton meublé","Tu passes l'abattement de 30 à 50 % et le plafond à 77 700 €."),
     ("Recalcule tes prix","Divise par 0,814 et applique avant le 13 octobre 2026."),
     ("Sors de la dépendance","Développe la réservation directe pour ne plus tout miser sur Airbnb.")],
    "À retenir", "Une décision non préparée, c'est le réel subi au lieu de choisi."),

  cta("Micro ou réel : combien tu perds vraiment ?",
      "Rentre tes chiffres et vois ton impôt dans les deux régimes, en clair.",
      "SIMULATEUR",
      "et je t'envoie mon simulateur pour trancher en connaissance de cause."),

  closing("11 ans de terrain pour t'aider à préparer la réforme au lieu de la subir."),
]


def main():
    html_dir = ROOT / "output" / SLUG / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    td = 0
    for i, body in enumerate(SLIDES, 1):
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{COMMON_CSS}</style></head><body>{body}</body></html>')
        d = [c for c in html if c in DASHES]
        if d:
            print(f"  ALERTE tiret slide {i}: {set(d)}"); td += len(d)
        (html_dir / f"slide_{i:02d}.html").write_text(html, encoding="utf-8")
    print(f"{len(SLIDES)} slides HTML ecrites dans {html_dir}. Tirets longs: {td}")


if __name__ == "__main__":
    main()
