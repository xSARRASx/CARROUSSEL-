#!/usr/bin/env python3
"""
Transcription des messages vocaux de Martin.

Usage :
    python3 transcrire_vocal.py vocal.ogg
    python3 transcrire_vocal.py vocal.ogg medium

Formats lus directement (decodage par PyAV, ffmpeg n'est PAS necessaire) :
    .opus / .ogg (vocaux WhatsApp), .m4a, .mp3, .wav, .mp4

Modeles disponibles, du plus rapide au plus fidele :
    tiny, base, small (defaut), medium, large-v3

Prerequis, a refaire a chaque nouvelle session (le conteneur repart de zero) :
    pip install --quiet faster-whisper

Note importante : vad_filter est toujours actif. Sans lui, Whisper invente du
texte sur les silences ("Sous-titres realises par la communaute d'Amara.org").
"""

import os
import sys
import time

MODELES = ("tiny", "base", "small", "medium", "large-v2", "large-v3")


def transcrire(chemin, taille_modele="small", langue="fr"):
    """Retourne (texte, duree_audio_en_secondes)."""
    from faster_whisper import WhisperModel

    modele = WhisperModel(taille_modele, device="cpu", compute_type="int8")
    segments, info = modele.transcribe(chemin, language=langue, vad_filter=True)
    texte = " ".join(s.text.strip() for s in segments).strip()
    return texte, info.duration


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    chemin = sys.argv[1]
    taille_modele = sys.argv[2] if len(sys.argv) > 2 else "small"

    if not os.path.isfile(chemin):
        print(f"Fichier introuvable : {chemin}", file=sys.stderr)
        return 1

    if taille_modele not in MODELES:
        print(f"Modele inconnu : {taille_modele}", file=sys.stderr)
        print(f"Choix possibles : {', '.join(MODELES)}", file=sys.stderr)
        return 1

    debut = time.time()
    try:
        texte, duree = transcrire(chemin, taille_modele)
    except ImportError:
        print("faster-whisper n'est pas installe.", file=sys.stderr)
        print("Lance d'abord : pip install --quiet faster-whisper", file=sys.stderr)
        return 1

    ecoule = time.time() - debut

    if not texte:
        print("(aucune parole detectee dans ce fichier)")
    else:
        print(texte)

    print(
        f"\n--- {os.path.basename(chemin)} | audio {duree:.0f}s "
        f"| modele {taille_modele} | traite en {ecoule:.0f}s ---",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
