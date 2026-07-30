#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_transcript.py -- Etape 2 du robot carrousels.

Role : trouver TOUT SEUL la derniere VRAIE video (pas un short) de la chaine
YouTube, recuperer sa transcription (le texte parle en francais), et la ranger
dans un fichier. C'est la matiere premiere des 2 carrousels.

Outil utilise : yt-dlp (robuste, passe depuis un serveur cloud, la ou la petite
librairie youtube-transcript-api se fait bloquer par YouTube).

Installation (une seule fois) :
    pip install yt-dlp

Usage (a la main, pour tester) :
    python3 pipeline/engine/fetch_transcript.py

Aucune cle API n'est necessaire pour cette etape.

On avance en 3 morceaux :
  - Morceau 1 : trouver la derniere VRAIE video (onglet "Videos", sans shorts)
  - Morceau 2 : recuperer la transcription francaise
  - Morceau 3 : ranger dans un fichier (texte + fiche d'infos)
"""

import json
import os
import re
import subprocess
import sys
import tempfile

# Chaine YouTube source (les videos du dimanche de Sebastien More).
CHANNEL_HANDLE = "moresebastien"
# L'onglet "/videos" ne contient QUE les vraies videos longues : pas les shorts,
# pas les lives. C'est exactement ce que Martin veut.
VIDEOS_TAB_URL = "https://www.youtube.com/@" + CHANNEL_HANDLE + "/videos"

# On prend les sous-titres francais : "fr-orig" = piste originale (ce que
# Sebastien dit vraiment), sinon "fr" en secours.
SUB_LANGS = "fr-orig,fr"

# Ou ranger les transcriptions (a la racine du repo, pas dans /tmp).
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
TRANSCRIPTS_DIR = os.path.join(REPO_ROOT, "pipeline", "output", "transcripts")


# --------------------------------------------------------------------------
# Petit utilitaire : lancer yt-dlp
# --------------------------------------------------------------------------

def _run_ytdlp(args):
    """Lance yt-dlp avec les arguments donnes. Renvoie la sortie texte.
    Explique clairement quoi faire si yt-dlp n'est pas installe."""
    try:
        result = subprocess.run(
            ["yt-dlp"] + args,
            capture_output=True, text=True, timeout=180,
        )
    except FileNotFoundError:
        raise RuntimeError(
            "yt-dlp n'est pas installe. Lance d'abord : pip install yt-dlp"
        )
    if result.returncode != 0:
        raise RuntimeError(
            "yt-dlp a echoue :\n" + (result.stderr or result.stdout)[-800:]
        )
    return result.stdout


# --------------------------------------------------------------------------
# MORCEAU 1 : trouver la derniere VRAIE video (sans shorts)
# --------------------------------------------------------------------------

def get_latest_video():
    """Renvoie la derniere vraie video de l'onglet "Videos" sous forme de
    dictionnaire : id, title, duration (secondes), url."""
    # --flat-playlist : liste seulement, sans telecharger.
    # --playlist-items 1 : uniquement la plus recente (la 1re de l'onglet).
    out = _run_ytdlp([
        "--flat-playlist",
        "--playlist-items", "1",
        "--print", "%(id)s\t%(title)s\t%(duration)s",
        VIDEOS_TAB_URL,
    ])
    line = out.strip().splitlines()[0]
    vid, title, duration = line.split("\t")
    return {
        "id": vid,
        "title": title,
        "duration": int(float(duration)) if duration not in ("", "NA") else None,
        "url": "https://www.youtube.com/watch?v=" + vid,
    }


# --------------------------------------------------------------------------
# MORCEAU 2 : recuperer la transcription francaise
# --------------------------------------------------------------------------

def get_transcript(video_id):
    """Telecharge les sous-titres francais de la video et renvoie un
    dictionnaire : text (transcription propre) + info (titre, date, duree...)."""
    with tempfile.TemporaryDirectory() as tmp:
        template = os.path.join(tmp, "sub")
        _run_ytdlp([
            "--skip-download",          # on ne veut pas la video, juste le texte
            "--write-auto-subs",        # sous-titres generes automatiquement
            "--write-subs",             # sous-titres manuels s'ils existent
            "--sub-langs", SUB_LANGS,
            "--sub-format", "json3",
            "--write-info-json",        # + une fiche d'infos (titre, date...)
            "-o", template,
            "https://www.youtube.com/watch?v=" + video_id,
        ])

        files = os.listdir(tmp)

        # On prefere fr-orig (piste originale francaise), sinon fr.
        sub_file = None
        for lang in ("fr-orig", "fr"):
            match = [f for f in files if f.endswith("." + lang + ".json3")]
            if match:
                sub_file = os.path.join(tmp, match[0])
                break
        if not sub_file:
            raise RuntimeError(
                "Pas de sous-titres francais trouves pour cette video."
            )

        text = _parse_json3(sub_file)

        # Fiche d'infos (facultative mais pratique).
        info = {}
        info_files = [f for f in files if f.endswith(".info.json")]
        if info_files:
            with open(os.path.join(tmp, info_files[0]), encoding="utf-8") as fh:
                raw = json.load(fh)
            info = {
                "title": raw.get("title", ""),
                "upload_date": raw.get("upload_date", ""),   # AAAAMMJJ
                "duration": raw.get("duration"),
                "url": raw.get("webpage_url", ""),
                "channel": raw.get("channel", ""),
            }

        return {"text": text, "info": info}


def _parse_json3(path):
    """Transforme un fichier de sous-titres json3 en texte propre.
    On recolle les segments proprement pour eviter les mots colles."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)

    lines = []
    for event in data.get("events", []):
        segs = event.get("segs") or []
        chunk = "".join(seg.get("utf8", "") for seg in segs)
        chunk = chunk.strip()
        if chunk:
            lines.append(chunk)

    # Chaque "ligne" de sous-titre est un morceau de phrase : on les separe par
    # un espace pour ne pas coller le dernier mot de l'une au 1er de la suivante.
    text = " ".join(lines)
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


# --------------------------------------------------------------------------
# MORCEAU 3 : ranger dans un fichier
# --------------------------------------------------------------------------

def save_transcript(video, transcript):
    """Ecrit la transcription + les infos dans pipeline/output/transcripts/.
    Renvoie le chemin du fichier texte cree."""
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

    info = transcript["info"]
    date = info.get("upload_date") or "date-inconnue"
    base = date + "_" + video["id"]
    txt_path = os.path.join(TRANSCRIPTS_DIR, base + ".txt")

    header = [
        "Titre : " + (info.get("title") or video["title"]),
        "Date de publication : " + date,
        "Duree (secondes) : " + str(info.get("duration") or video.get("duration") or "?"),
        "Lien : " + (info.get("url") or video["url"]),
        "Chaine : " + (info.get("channel") or CHANNEL_HANDLE),
        "-" * 60,
        "",
    ]
    with open(txt_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(header))
        fh.write(transcript["text"])
        fh.write("\n")

    return txt_path


# --------------------------------------------------------------------------
# Point d'entree : pour tester a la main
# --------------------------------------------------------------------------

def transcript_existant(video_id):
    """Renvoie le chemin du transcript deja range pour cette video, sinon None.

    Les fichiers sont nommes <date>_<identifiant>.txt : on cherche donc un nom
    qui se termine par _<identifiant>.txt.
    """
    if not os.path.isdir(TRANSCRIPTS_DIR):
        return None
    suffixe = "_" + video_id + ".txt"
    for nom in sorted(os.listdir(TRANSCRIPTS_DIR)):
        if nom.endswith(suffixe):
            return os.path.join(TRANSCRIPTS_DIR, nom)
    return None


def verifier():
    """Mode --verifier : dit si la derniere video est NOUVELLE, sans rien ecrire.

    A appeler AVANT la transcription. C'est le garde-fou anti-doublon : il ne
    telecharge rien et ne cree aucun fichier, donc il peut etre lance autant de
    fois qu'on veut sans fausser la comparaison.

    Code de sortie : 0 = nouvelle video (il faut la traiter),
                     1 = deja traitee (ne rien produire, ne rien depenser),
                     2 = PANNE (yt-dlp absent, reseau...) -- surtout ne pas
                         confondre avec "deja traitee" : la, on ne SAIT PAS.
    """
    try:
        video = get_latest_video()
    except Exception as err:
        print("PANNE pendant la verification :", err)
        print()
        print("VERDICT : impossible de savoir s'il y a une nouvelle video.")
        print("          NE PAS conclure 'deja traitee'. Corrige la panne")
        print("          (souvent : pip install yt-dlp) puis relance --verifier.")
        return 2

    deja = transcript_existant(video["id"])

    # LE controle qui fait autorite : les carrousels sont-ils REELLEMENT livres ?
    # On ne se fie PAS a l'existence de la transcription : un run peut planter
    # juste apres l'avoir ecrite, et la video serait alors declaree "traitee"
    # alors que Martin n'a rien recu. On verifie le RESULTAT FINAL.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from livraison import video_livree
    livree, detail = video_livree(video["id"])

    print("Derniere video de la chaine :")
    print("  - Titre       :", video["title"])
    print("  - Identifiant :", video["id"])
    print("  - Lien        :", video["url"])
    print("  - Transcript  :", os.path.basename(deja) if deja else "aucun")
    print("  - Livraison   :", detail)
    if livree:
        print()
        print("VERDICT : DEJA LIVREE. Rien a faire. Ne produis AUCUN carrousel")
        print("          et ne genere AUCUNE image. Previens Martin en une ligne.")
        return 1

    print()
    if deja:
        print("VERDICT : A REPRENDRE. La transcription existe mais les carrousels")
        print("          ne sont PAS livres : un run precedent s'est interrompu.")
        print("          Inutile de retelecharger la transcription : reprends")
        print("          directement a l'ecriture des 2 carrousels.")
    else:
        print("VERDICT : NOUVELLE video. Lance la transcription, puis les 2 carrousels.")
    return 0


def main():
    if "--verifier" in sys.argv[1:]:
        return verifier()

    print("Etape 2 -- transcription de la derniere VRAIE video YouTube")
    print("Chaine :", VIDEOS_TAB_URL)
    print()

    print("[1/3] Recherche de la derniere vraie video (sans shorts)...")
    video = get_latest_video()
    dur = video.get("duration")
    dur_txt = ("%dmin%02ds" % (dur // 60, dur % 60)) if dur else "?"
    print("      - Titre :", video["title"])
    print("      - Duree :", dur_txt)
    print("      - Lien  :", video["url"])
    print()

    print("[2/3] Telechargement de la transcription francaise...")
    transcript = get_transcript(video["id"])
    print("      - Longueur :", len(transcript["text"]), "caracteres")
    print("      - Debut    :", transcript["text"][:120], "...")
    print()

    print("[3/3] Rangement dans un fichier...")
    path = save_transcript(video, transcript)
    print("      - Fichier :", path)
    print()
    print("Termine. Ce fichier sert de matiere premiere aux 2 carrousels.")


if __name__ == "__main__":
    sys.exit(main())
