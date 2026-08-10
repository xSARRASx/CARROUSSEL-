#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transcrit un message vocal (WhatsApp, dictaphone...) en texte francais.

Usage : python3 transcrire_vocal.py mon_vocal.ogg [modele]
        modele = tiny | base | small (defaut) | medium | large-v3

Formats lus : ogg/opus (WhatsApp), m4a, mp3, wav, mp4... (decodage PyAV,
pas besoin de ffmpeg en ligne de commande).

Prerequis (le conteneur repart a zero a chaque session) :
    pip install --quiet faster-whisper
"""
import sys, pathlib

def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    chemin = sys.argv[1]
    modele = sys.argv[2] if len(sys.argv) > 2 else "small"

    from faster_whisper import WhisperModel
    fichier = pathlib.Path(chemin)
    if not fichier.exists():
        raise SystemExit(f"fichier introuvable : {fichier}")

    print(f"Modele '{modele}', transcription de {fichier.name}...", file=sys.stderr)
    m = WhisperModel(modele, device="cpu", compute_type="int8")
    segments, info = m.transcribe(
        str(fichier),
        language="fr",
        beam_size=5,
        vad_filter=True,          # coupe les silences : moins d'hallucinations
        vad_parameters={"min_silence_duration_ms": 500},
    )

    morceaux = []
    for s in segments:
        mn, sec = divmod(int(s.start), 60)
        morceaux.append(s.text.strip())
        print(f"[{mn}:{sec:02d}] {s.text.strip()}", file=sys.stderr)

    print(f"\n--- duree {info.duration:.0f}s ---", file=sys.stderr)
    print(" ".join(morceaux))   # le texte complet part sur la sortie standard


if __name__ == "__main__":
    main()
