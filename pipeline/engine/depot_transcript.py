#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
depot_transcript.py -- Deposer une transcription recuperee AILLEURS.

POURQUOI CE SCRIPT EXISTE
-------------------------
Ce serveur sort par un proxy d'entreprise. YouTube le prend regulierement pour
un robot ("Sign in to confirm you're not a bot"), et la parade habituelle
(curl_cffi / --impersonate) est IMPOSSIBLE ici : le proxy re-termine le TLS,
donc l'empreinte de navigateur forgee par curl_cffi se fait couper net
("Connection reset by peer"). Teste et verifie le 27/08/2026.

La solution qui marche : recuperer la transcription depuis une connexion NON
bloquee (le Mac de Martin, en residentiel), puis la deposer ici. Ce script
garantit le bon format, pour que le reste de la chaine reparte sans rien savoir
de la maniere dont le texte est arrive.

USAGE (depuis le Mac, ou d'ici avec un texte colle)
---------------------------------------------------
    python3 pipeline/engine/depot_transcript.py \\
        --video h0GZh51rtCk \\
        --titre "Comment faire baisser sa taxe fonciere ?" \\
        --fichier /tmp/transcription.txt

    # ou en lisant l'entree standard :
    pbpaste | python3 pipeline/engine/depot_transcript.py --video <id> --titre "..."

Le fichier produit va dans pipeline/output/transcripts/ au format attendu, et la
demande de relais (A_RECUPERER.json) est effacee si elle concernait cette video.
"""

import argparse
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
TRANSCRIPTS = ROOT / "pipeline" / "output" / "transcripts"
DEMANDE = TRANSCRIPTS / "A_RECUPERER.json"

MINIMUM = 2000          # en dessous, ce n'est pas une transcription de 20 minutes


def nettoyer(brut):
    """Retire les horodatages colles depuis l'interface YouTube et recolle le
    texte en paragraphes lisibles."""
    lignes = []
    for ligne in brut.splitlines():
        ligne = ligne.strip()
        if not ligne:
            continue
        # "0:07", "12:34", "1:02:03" seuls sur leur ligne
        if re.fullmatch(r"\d{1,2}:\d{2}(:\d{2})?", ligne):
            continue
        # Titres de chapitres ajoutes par l'interface YouTube
        if re.match(r"^Chapter\s+\d+\s*:", ligne, re.I):
            continue
        # Horodatage colle au texte, en francais OU en anglais :
        #   "0:077 secondes...", "12 minutes et 3 secondes...", "0:000 secondsMenage..."
        ligne = re.sub(
            r"^\d{1,2}:\d{2}(:\d{2})?\d*\s*"
            r"(secondes?|seconds?|minutes?(\s*(et|,)\s*\d+\s*(secondes?|seconds?))?)?\s*",
            "", ligne).strip()
        if ligne:
            lignes.append(ligne)
    return " ".join(lignes)


def main():
    ap = argparse.ArgumentParser(description="Deposer une transcription recuperee ailleurs.")
    ap.add_argument("--video", required=True, help="identifiant YouTube (ex: h0GZh51rtCk)")
    ap.add_argument("--titre", required=True, help="titre francais de la video")
    ap.add_argument("--fichier", help="fichier texte a deposer (defaut : entree standard)")
    ap.add_argument("--duree", type=int, default=None, help="duree en secondes, optionnel")
    ap.add_argument("--date", default=None, help="date de publication AAAAMMJJ, optionnel")
    ap.add_argument("--source", default="relais (connexion non bloquee)",
                    help="d'ou vient cette transcription, pour la memoire du fichier")
    args = ap.parse_args()

    brut = (pathlib.Path(args.fichier).read_text(encoding="utf-8")
            if args.fichier else sys.stdin.read())
    texte = nettoyer(brut)

    if len(texte) < MINIMUM:
        raise SystemExit(
            "ERREUR : seulement %d caracteres apres nettoyage.\n"
            "Une vraie transcription de video fait des dizaines de milliers de\n"
            "caracteres. Refuse de deposer un texte tronque : le robot ecrirait\n"
            "des carrousels sur une video qu'il n'a pas vraiment lue." % len(texte))

    jour = datetime.date.today().strftime("%Y%m%d")
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    cible = TRANSCRIPTS / ("%s_%s.txt" % (jour, args.video))

    entete = [
        "Titre : " + args.titre,
        "Date de publication : " + (args.date or "inconnue"),
        "Duree (secondes) : " + (str(args.duree) if args.duree else "inconnue"),
        "Lien : https://www.youtube.com/watch?v=" + args.video,
        "Chaine : moresebastien",
        "Source : " + args.source,
        "-" * 60,
    ]
    cible.write_text("\n".join(entete) + "\n" + texte + "\n", encoding="utf-8")

    print("Transcription deposee :")
    print("  - fichier    :", cible)
    print("  - longueur   :", len(texte), "caracteres")
    print("  - debut      :", texte[:110], "...")

    # La demande de relais est honoree : on la retire pour ne pas la refaire.
    if DEMANDE.exists():
        try:
            demande = json.loads(DEMANDE.read_text(encoding="utf-8"))
        except ValueError:
            demande = {}
        if demande.get("video_id") == args.video:
            DEMANDE.unlink()
            print("  - demande de relais honoree et retiree")

    print()
    print("Le robot repartira de ce fichier sans rien redemander a YouTube.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
