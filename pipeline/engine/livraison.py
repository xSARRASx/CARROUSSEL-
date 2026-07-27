#!/usr/bin/env python3
"""
livraison.py — depose un carrousel fini dans livraison/ pour le Claude du Mac.

Format de depot (valide par Martin le 27/07/2026) :

    livraison/
    └── <marque>-<AAAA-MM-JJ>-<sujet>/
        ├── 01.jpg ... 10.jpg
        └── description.txt

Regles :
  - la marque s'ecrit exactement "lesousloueur" ou "guestlucky" (jamais
    "guettelucky", jamais de majuscule) ;
  - les images sont renommees 01.jpg a 10.jpg, sans prefixe "slide_" ;
  - les images de fond ne sont PAS copiees (deja incrustees dans les slides,
    et 2,9 Mo piece : inutile d'alourdir le depot) ;
  - la date est celle du LUNDI de la semaine de livraison, pour que le tri
    alphabetique soit aussi un tri chronologique.

Usage :
    python3 livraison.py <slug> [--date AAAA-MM-JJ] [--sujet mot-cle]

    python3 livraison.py lsl_conciergerie_220k
    python3 livraison.py gl_conformite_lemeur --sujet conformite
"""
import argparse
import datetime
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIVRAISON = ROOT.parent / "livraison"

# prefixe de slug -> nom de marque exact attendu par le Mac
MARQUES = {
    "lsl": "lesousloueur",
    "gl": "guestlucky",
}

NB_SLIDES = 10


def lundi_de_la_semaine(jour=None):
    """Renvoie le lundi de la semaine du jour donne (aujourd'hui par defaut)."""
    jour = jour or datetime.date.today()
    return jour - datetime.timedelta(days=jour.weekday())


def nettoie(texte):
    """Reduit un texte a des minuscules, chiffres et tirets."""
    texte = texte.lower().replace("_", "-")
    texte = re.sub(r"[^a-z0-9-]+", "-", texte)
    return re.sub(r"-+", "-", texte).strip("-")


def devine_marque_et_sujet(slug):
    """Deduit la marque et le sujet du slug (ex: lsl_conciergerie_220k)."""
    prefixe, _, reste = slug.partition("_")
    marque = MARQUES.get(prefixe)
    if not marque:
        raise SystemExit(
            f"ERREUR : slug '{slug}' — prefixe '{prefixe}' inconnu.\n"
            f"Prefixes acceptes : {', '.join(sorted(MARQUES))}."
        )
    return marque, nettoie(reste or slug)


def livrer(slug, date=None, sujet=None):
    """Copie un carrousel fini dans livraison/. Renvoie le dossier cree."""
    src = ROOT / "output" / slug
    jpg_dir = src / "jpg"
    description = src / "description.txt"

    if not jpg_dir.is_dir():
        raise SystemExit(f"ERREUR : pas de dossier jpg dans {src}. Lance render.py d'abord.")
    if not description.is_file():
        raise SystemExit(f"ERREUR : description.txt manquant dans {src}. La legende est obligatoire.")

    slides = sorted(jpg_dir.glob("slide_*.jpg"))
    if len(slides) != NB_SLIDES:
        raise SystemExit(
            f"ERREUR : {len(slides)} slide(s) trouvee(s) dans {jpg_dir}, il en faut {NB_SLIDES}.\n"
            f"Livraison annulee : mieux vaut rien livrer qu'un carrousel incomplet."
        )

    marque, sujet_auto = devine_marque_et_sujet(slug)
    sujet = nettoie(sujet) if sujet else sujet_auto
    date = date or lundi_de_la_semaine().isoformat()

    dest = LIVRAISON / f"{marque}-{date}-{sujet}"
    if dest.exists():
        shutil.rmtree(dest)          # re-livraison propre, jamais de melange
    dest.mkdir(parents=True)

    for i, slide in enumerate(slides, start=1):
        shutil.copy2(slide, dest / f"{i:02d}.jpg")
    shutil.copy2(description, dest / "description.txt")

    poids = sum(f.stat().st_size for f in dest.iterdir()) / 1024 / 1024
    print(f"  livre : livraison/{dest.name}  ({NB_SLIDES} images + description.txt, {poids:.1f} Mo)")
    return dest


def main():
    ap = argparse.ArgumentParser(description="Depose un carrousel fini dans livraison/.")
    ap.add_argument("slug", help="nom du dossier dans pipeline/output/ (ex: lsl_conciergerie_220k)")
    ap.add_argument("--date", help="date du lundi, format AAAA-MM-JJ (defaut : lundi de cette semaine)")
    ap.add_argument("--sujet", help="mot-cle du sujet (defaut : deduit du slug)")
    args = ap.parse_args()

    if args.date:
        try:
            datetime.date.fromisoformat(args.date)
        except ValueError:
            raise SystemExit(f"ERREUR : date '{args.date}' invalide, format attendu AAAA-MM-JJ.")

    livrer(args.slug, date=args.date, sujet=args.sujet)


if __name__ == "__main__":
    sys.exit(main())
