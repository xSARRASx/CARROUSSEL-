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
    python3 livraison.py <slug> [--date AAAA-MM-JJ] [--sujet mot-cle] [--remplacer]
    python3 livraison.py --controle [--date AAAA-MM-JJ]

    python3 livraison.py lsl_conciergerie_220k
    python3 livraison.py v2_gl_conformite_lemeur --sujet conformite-lemeur-v2
    python3 livraison.py --controle          # verifie que la semaine est complete
"""
import argparse
import datetime
import filecmp
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIVRAISON = ROOT.parent / "livraison"

# Registre qui relie un identifiant de video aux dossiers livres.
# Il vit HORS de livraison/ pour ne pas polluer ce que lit le Mac.
# ⚠️ Ce fichier n'est qu'un ANNUAIRE : il ne prouve rien tout seul. Toute
# verification relit les fichiers reels sur le disque (voir video_livree()).
JOURNAL = ROOT / "output" / "traite.json"

# Jetons reconnus dans un slug -> nom de marque exact attendu par le Mac.
# On accepte les alias pour ne JAMAIS perdre un carrousel a cause d'un nom :
# lsl_x, v2_lsl_x, build_lsl_x, lesousloueur_x... donnent tous "lesousloueur".
MARQUES = {
    "lsl": "lesousloueur",
    "lesousloueur": "lesousloueur",
    "sousloueur": "lesousloueur",
    "gl": "guestlucky",
    "guestlucky": "guestlucky",
}

# Jetons techniques a ignorer quand ils precedent la marque (v2_lsl_..., build_gl_...)
JETONS_IGNORES = {"v1", "v2", "v3", "build", "deck", "carrousel", "carroussel"}

NB_SLIDES = 10
MARQUES_ATTENDUES = ("lesousloueur", "guestlucky")


def lundi_de_la_semaine(jour=None):
    """Renvoie le lundi de la semaine du jour donne (aujourd'hui par defaut)."""
    jour = jour or datetime.date.today()
    return jour - datetime.timedelta(days=jour.weekday())


def nettoie(texte):
    """Reduit un texte a des minuscules, chiffres et tirets."""
    texte = texte.lower()
    texte = re.sub(r"[^a-z0-9]+", "-", texte)
    return re.sub(r"-+", "-", texte).strip("-")


def devine_marque_et_sujet(slug):
    """Deduit la marque et le sujet du slug, quel que soit le prefixe.

    Accepte lsl_x, v2_lsl_x, build_gl_x, LSL-x, lesousloueur_x...
    On cherche le PREMIER jeton connu, le sujet est tout ce qui suit.
    """
    jetons = [j for j in re.split(r"[^a-zA-Z0-9]+", slug) if j]
    for i, jeton in enumerate(jetons):
        marque = MARQUES.get(jeton.lower())
        if marque:
            reste = jetons[i + 1:]
            sujet = nettoie("-".join(reste)) if reste else nettoie(slug)
            return marque, sujet

    connus = ", ".join(sorted(set(MARQUES)))
    raise SystemExit(
        f"ERREUR : impossible de deviner la marque du slug '{slug}'.\n"
        f"Le nom doit contenir un de ces jetons : {connus}.\n"
        f"Exemples valides : lsl_fiscalite, v2_gl_conformite, build_lsl_airbnb.\n"
        f"Sinon, force la marque en renommant le dossier de sortie."
    )


def _charger_journal():
    if not JOURNAL.is_file():
        return {"videos": {}}
    try:
        return json.loads(JOURNAL.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {"videos": {}}


def _noter_livraison(video_id, dossier, titre=None):
    """Note qu'un dossier a ete livre pour cette video. Simple annuaire."""
    if not video_id:
        return
    j = _charger_journal()
    fiche = j["videos"].setdefault(video_id, {"titre": titre or "", "dossiers": []})
    if titre:
        fiche["titre"] = titre
    if dossier not in fiche["dossiers"]:
        fiche["dossiers"].append(dossier)
        fiche["dossiers"].sort()
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    JOURNAL.write_text(json.dumps(j, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def dossier_valide(nom):
    """Vrai si le dossier livre existe VRAIMENT et est complet sur le disque."""
    d = LIVRAISON / nom
    if not d.is_dir():
        return False
    if not (d / "description.txt").is_file():
        return False
    return len(list(d.glob("[0-9][0-9].jpg"))) == NB_SLIDES


def video_livree(video_id):
    """La video a-t-elle REELLEMENT ete livree ? Renvoie (bool, message).

    C'est LE controle qui fait autorite. Il ne se contente pas de lire le
    registre : pour chaque dossier annonce, il verifie sur le disque qu'il
    existe, qu'il contient 10 images et une description.
    Une video n'est traitee que si les DEUX marques sont livrees et valides.

    ⚠️ Regle du projet : un controle verifie toujours le RESULTAT FINAL,
    jamais une etape intermediaire. L'existence d'une transcription ne prouve
    RIEN : le run a pu planter juste apres.
    """
    fiche = _charger_journal()["videos"].get(video_id)
    if not fiche:
        return False, "aucune livraison enregistree pour cette video"

    annonces = fiche.get("dossiers", [])
    if not annonces:
        return False, "fiche presente mais aucun dossier livre"

    manquants = [n for n in annonces if not dossier_valide(n)]
    if manquants:
        return False, "dossier(s) annonce(s) mais absent(s) ou incomplet(s) : " + ", ".join(manquants)

    marques = {n.split("-", 1)[0] for n in annonces}
    absentes = [m for m in MARQUES_ATTENDUES if m not in marques]
    if absentes:
        return False, "marque(s) jamais livree(s) : " + ", ".join(absentes)

    return True, "%d dossier(s) verifie(s) sur le disque : %s" % (len(annonces), ", ".join(annonces))


def _memes_dossiers(a, b):
    """Vrai si deux dossiers contiennent exactement les memes fichiers."""
    noms = sorted(f.name for f in a.iterdir())
    if noms != sorted(f.name for f in b.iterdir()):
        return False
    egaux, differents, erreurs = filecmp.cmpfiles(a, b, noms, shallow=False)
    return not differents and not erreurs


def livrer(slug, date=None, sujet=None, remplacer=False, video=None, titre=None):
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
    provisoire = LIVRAISON / f".tmp-{marque}-{date}-{sujet}"

    # Construction dans un dossier provisoire : si quelque chose casse en cours
    # de route, la livraison precedente reste intacte.
    if provisoire.exists():
        shutil.rmtree(provisoire)
    provisoire.mkdir(parents=True)
    for i, slide in enumerate(slides, start=1):
        shutil.copy2(slide, provisoire / f"{i:02d}.jpg")
    shutil.copy2(description, provisoire / "description.txt")

    if dest.exists():
        if _memes_dossiers(dest, provisoire):
            shutil.rmtree(provisoire)
            _noter_livraison(video, dest.name, titre)
            print(f"  deja livre a l'identique : livraison/{dest.name} (rien a faire)")
            return dest
        if not remplacer:
            shutil.rmtree(provisoire)
            raise SystemExit(
                f"ERREUR : livraison/{dest.name} existe deja avec un contenu DIFFERENT.\n"
                f"Livraison annulee pour ne rien ecraser par accident.\n"
                f"  - si c'est un autre carrousel : relance avec --sujet <autre-mot-cle>\n"
                f"  - si tu veux vraiment remplacer : relance avec --remplacer"
            )
        shutil.rmtree(dest)
        print(f"  (remplacement demande : ancienne version de {dest.name} supprimee)")

    provisoire.rename(dest)
    _noter_livraison(video, dest.name, titre)
    poids = sum(f.stat().st_size for f in dest.iterdir()) / 1024 / 1024
    print(f"  livre : livraison/{dest.name}  ({NB_SLIDES} images + description.txt, {poids:.1f} Mo)")
    return dest


def controle_semaine(date=None):
    """Verifie qu'une marque ET l'autre ont bien ete livrees pour la semaine.

    Renvoie True si tout va bien. Sinon affiche une alerte explicite et
    renvoie False (le robot du lundi doit alors PREVENIR Martin, pas pousser
    en silence).
    """
    date = date or lundi_de_la_semaine().isoformat()
    print(f"CONTROLE DE LA SEMAINE DU {date}")

    if not LIVRAISON.is_dir():
        print("  ALERTE : le dossier livraison/ n'existe pas du tout.")
        return False

    ok = True
    for marque in MARQUES_ATTENDUES:
        dossiers = sorted(LIVRAISON.glob(f"{marque}-{date}-*"))
        if not dossiers:
            print(f"  ALERTE : AUCUN carrousel '{marque}' livre pour le {date}.")
            ok = False
            continue
        if len(dossiers) > 1:
            noms = ", ".join(d.name for d in dossiers)
            print(f"  ATTENTION : {len(dossiers)} dossiers '{marque}' pour le {date} ({noms}).")
        for d in dossiers:
            images = sorted(d.glob("[0-9][0-9].jpg"))
            legende = (d / "description.txt").is_file()
            if len(images) != NB_SLIDES or not legende:
                print(
                    f"  ALERTE : {d.name} est INCOMPLET "
                    f"({len(images)}/{NB_SLIDES} images, description.txt "
                    f"{'presente' if legende else 'MANQUANTE'})."
                )
                ok = False
            else:
                print(f"  OK : {d.name} ({NB_SLIDES} images + description.txt)")

    if ok:
        print(f"  RESULTAT : semaine complete, les 2 marques sont livrees.")
    else:
        print(
            "  RESULTAT : SEMAINE INCOMPLETE.\n"
            "  NE PAS pousser en silence : previens Martin explicitement en lui\n"
            "  disant quelle marque manque et pourquoi."
        )
    return ok


def main():
    ap = argparse.ArgumentParser(description="Depose un carrousel fini dans livraison/.")
    ap.add_argument("slug", nargs="?", help="dossier dans pipeline/output/ (ex: lsl_conciergerie_220k)")
    ap.add_argument("--date", help="date du lundi, format AAAA-MM-JJ (defaut : lundi de cette semaine)")
    ap.add_argument("--sujet", help="mot-cle du sujet (defaut : deduit du slug)")
    ap.add_argument("--remplacer", action="store_true", help="autorise l'ecrasement d'une livraison differente")
    ap.add_argument("--controle", action="store_true", help="verifie que les 2 marques sont livrees pour la semaine")
    ap.add_argument("--video", help="identifiant YouTube de la video source (pour l'anti-doublon)")
    ap.add_argument("--titre", help="titre de la video, pour memoire dans le registre")
    args = ap.parse_args()

    if args.date:
        try:
            datetime.date.fromisoformat(args.date)
        except ValueError:
            raise SystemExit(f"ERREUR : date '{args.date}' invalide, format attendu AAAA-MM-JJ.")

    if args.controle:
        return 0 if controle_semaine(args.date) else 1

    if not args.slug:
        ap.error("indique un slug a livrer, ou utilise --controle.")

    livrer(args.slug, date=args.date, sujet=args.sujet, remplacer=args.remplacer,
           video=args.video, titre=args.titre)
    return 0


if __name__ == "__main__":
    sys.exit(main())
