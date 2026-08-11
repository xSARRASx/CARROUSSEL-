#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcrire_vocal.py -- Transcription des messages vocaux de Martin.

Martin envoie souvent des vocaux (WhatsApp .opus/.ogg, mais aussi m4a, mp3,
wav, mp4). Ce script les transcrit en francais.

Prerequis (a refaire A CHAQUE SESSION : le conteneur repart de zero) :
    pip install --quiet faster-whisper
Pas besoin de ffmpeg : le decodage passe par PyAV, embarque avec la librairie.

Usage :
    python3 pipeline/transcrire_vocal.py mon_vocal.ogg
    python3 pipeline/transcrire_vocal.py mon_vocal.ogg medium   # + fidele, + lent

Modeles : 'small' (defaut, rapide) ou 'medium' (audio difficile, jargon metier).

⚠️ vad_filter=True est OBLIGATOIRE : sans lui, Whisper invente du texte sur les
silences (typiquement "Sous-titres realises par la communaute d'Amara.org").

⚠️ Whisper ecorche les noms propres et le vocabulaire metier. Apres transcription,
TOUJOURS relire et corriger, puis signaler a Martin ce qui a ete retabli.
Corrections frequentes sur ce projet :
    Guest Lucky / Gessuki / Guestuki / Gasuki   -> GuestLucky
    loi Lumur / loi Leemur / Wemur / loi le meurt -> loi Le Meur
    Bet 24 / Beds vingt-quatre                  -> Beds24 (⚠️ mot BANNI en public)
    CH manager / chemin majeur / ch. manager    -> channel manager
    micro BC / micro-bic                        -> micro-BIC
    carte G, loi Hoguet, LMNP, DAC7, Declaloc, para-hotellerie
"""

import sys
import pathlib


def transcrire(chemin, modele="small", langue="fr"):
    """Transcrit un fichier audio et renvoie le texte brut."""
    from faster_whisper import WhisperModel

    fichier = pathlib.Path(chemin)
    if not fichier.exists():
        raise SystemExit("Fichier introuvable : " + str(fichier))

    m = WhisperModel(modele, device="cpu", compute_type="int8")
    segments, info = m.transcribe(str(fichier), language=langue, vad_filter=True)
    texte = " ".join(s.text.strip() for s in segments).strip()
    return texte, info


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit("Usage : python3 transcrire_vocal.py <fichier> [small|medium]")

    chemin = sys.argv[1]
    modele = sys.argv[2] if len(sys.argv) > 2 else "small"

    print("Transcription de", chemin, "avec le modele", modele, "...")
    texte, info = transcrire(chemin, modele)
    print("Duree audio :", round(getattr(info, "duration", 0), 1), "s")
    print("-" * 60)
    print(texte)
    print("-" * 60)
    print("Longueur :", len(texte), "caracteres")
    print("RAPPEL : relire et corriger les noms propres (GuestLucky, loi Le Meur,")
    print("channel manager, micro-BIC...) avant d'utiliser ce texte.")


if __name__ == "__main__":
    main()
