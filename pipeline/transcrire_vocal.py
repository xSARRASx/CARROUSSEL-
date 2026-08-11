#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transcription des messages vocaux de Martin (Whisper local, sans réseau).

Prerequis (le conteneur repart de zero a chaque session, donc a refaire) :
    pip install --quiet faster-whisper

Usage :
    python3 transcrire_vocal.py vocal.ogg           # modele 'small' (rapide)
    python3 transcrire_vocal.py vocal.opus medium   # plus lent, plus fidele

Formats lus directement : .opus / .ogg (vocaux WhatsApp), m4a, mp3, wav, mp4.
Pas besoin de ffmpeg : le decodage passe par PyAV (embarque avec faster-whisper).

IMPORTANT :
- vad_filter=True TOUJOURS. Sans lui, Whisper invente du texte sur les silences
  (typiquement "Sous-titres realises par la communaute d'Amara.org").
- Whisper ecorche les noms propres et le jargon metier (GuestLucky, Beds24,
  Metricool, Seedance, loi Hoguet, LuckyCover, Leapway, PriceLabs...).
  => Toujours relire la transcription, corriger ces termes, et SIGNALER a Martin
     ce qui a ete retabli.
"""
import sys
import pathlib

# Termes metier souvent deformes par Whisper (aide a la relecture, pas une
# correction automatique : on signale a Martin ce qu'on retablit).
TERMES_A_VERIFIER = [
    "GuestLucky", "Guestlucky", "Lucky Copilot", "LuckyCover", "Leapway",
    "Le Sous Loueur", "Sebastien More", "Metricool", "Seedance", "PriceLabs",
    "loi Hoguet", "loi Le Meur", "Beds24", "Channel Manager", "Airbnb",
    "Booking", "Abritel", "Auto Actions", "micro-BIC", "conciergerie",
]


def transcrire(chemin: str, taille_modele: str = "small") -> str:
    from faster_whisper import WhisperModel

    fichier = pathlib.Path(chemin)
    if not fichier.exists():
        raise SystemExit(f"Fichier introuvable : {fichier}")

    modele = WhisperModel(taille_modele, device="cpu", compute_type="int8")
    segments, info = modele.transcribe(
        str(fichier),
        language="fr",
        vad_filter=True,          # NE JAMAIS retirer : evite le texte invente
    )
    texte = " ".join(s.text for s in segments).strip()
    duree = getattr(info, "duration", None)
    if duree:
        print(f"[duree audio : {duree:.0f}s | modele : {taille_modele}]\n",
              file=sys.stderr)
    return texte


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    chemin = sys.argv[1]
    taille = sys.argv[2] if len(sys.argv) > 2 else "small"
    print(transcrire(chemin, taille))


if __name__ == "__main__":
    main()
