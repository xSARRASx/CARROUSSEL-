#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transcrit un message vocal (WhatsApp .opus/.ogg, m4a, mp3, wav, mp4) en francais.

Usage :
  python3 transcrire_vocal.py <fichier_audio> [small|medium]

- Prerequis (a refaire a chaque session, le conteneur repart de zero) :
    pip install --quiet faster-whisper
- 'small' (defaut) : rapide, tres bon pour un vocal normal.
- 'medium' : plus lent, a utiliser si l'audio est difficile ou plein de jargon.
- vad_filter=True TOUJOURS : sans lui, Whisper invente du texte sur les
  silences (ex : "Sous-titres realises par la communaute d'Amara.org").
- Pas besoin de ffmpeg : le decodage passe par PyAV (installe avec faster-whisper).
- ATTENTION : Whisper ecorche les noms propres et termes techniques
  (GuestLucky, Beds24, loi Hoguet...). Relire et corriger, en signalant
  ce qui a ete retabli.
"""
import sys

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    audio = sys.argv[1]
    taille = sys.argv[2] if len(sys.argv) > 2 else "small"
    from faster_whisper import WhisperModel
    model = WhisperModel(taille, device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio, language="fr", vad_filter=True)
    print(f"[duree {info.duration:.0f}s, modele {taille}]")
    textes = []
    for s in segments:
        print(f"({s.start:>4.0f}s) {s.text.strip()}")
        textes.append(s.text.strip())
    print("\n----- TEXTE BRUT -----")
    print(" ".join(textes))

if __name__ == "__main__":
    main()
