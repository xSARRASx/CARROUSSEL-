#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compose les musiques de fond des publicites Lucky Conciergerie.

Elles sont synthetisees ici, de zero : aucune licence a verifier, aucun
risque de reclamation sur YouTube ou Meta.

Quatre ambiances, pour que chaque video ait la sienne :
  douce    piano feutre en mineur, intime          (video 1, le soir)
  posee    nappe lente et large, presque suspendue (video 2, la reflexion)
  claire   majeur lumineux, optimiste              (video 3, la reussite)
  allante  pulsation reguliere, on avance          (video 4, les 3 etapes)

Usage : python3 musique.py [duree] [ambiance]
"""
import sys, pathlib
import numpy as np

SR = 48000
ICI = pathlib.Path(__file__).resolve().parent

# (nom, notes aigues jouees en arpege, notes graves tenues)
AMBIANCES = {
    "douce": {
        "accords": [([220.00, 261.63, 329.63], [110.00, 164.81]),
                    ([174.61, 220.00, 261.63], [87.31, 130.81]),
                    ([196.00, 261.63, 329.63], [130.81, 196.00]),
                    ([196.00, 246.94, 293.66], [98.00, 146.83])],
        "mesure": 4.0, "piano": 0.30, "nappe": 0.32, "pulsation": 0.0,
    },
    "posee": {   # accords de septieme, tres lents : on laisse respirer
        "accords": [([174.61, 261.63, 329.63], [87.31, 130.81]),
                    ([196.00, 261.63, 349.23], [98.00, 146.83]),
                    ([146.83, 220.00, 293.66], [73.42, 110.00]),
                    ([233.08, 293.66, 349.23], [116.54, 174.61])],
        "mesure": 5.2, "piano": 0.22, "nappe": 0.40, "pulsation": 0.0,
    },
    "claire": {  # majeur, registre plus haut : lumineux et confiant
        "accords": [([261.63, 329.63, 392.00], [130.81, 196.00]),
                    ([196.00, 246.94, 392.00], [98.00, 146.83]),
                    ([220.00, 329.63, 440.00], [110.00, 164.81]),
                    ([174.61, 261.63, 349.23], [87.31, 130.81])],
        "mesure": 3.6, "piano": 0.32, "nappe": 0.26, "pulsation": 0.0,
    },
    "allante": {  # meme couleur, mais une pulsation qui pousse en avant
        "accords": [([261.63, 329.63, 392.00], [130.81, 196.00]),
                    ([233.08, 293.66, 349.23], [116.54, 174.61]),
                    ([220.00, 293.66, 349.23], [110.00, 164.81]),
                    ([196.00, 246.94, 329.63], [98.00, 146.83])],
        "mesure": 3.2, "piano": 0.26, "nappe": 0.24, "pulsation": 0.16,
    },
}


def note(freq, duree, force=1.0, chute_rapide=False):
    """Une note de piano : harmoniques + decroissance exponentielle."""
    n = int(duree * SR)
    t = np.arange(n) / SR
    son = np.zeros(n)
    for rang, poids in enumerate([1.0, 0.42, 0.22, 0.12, 0.06], start=1):
        f = freq * rang * (1 + 0.0004 * rang * rang)   # legere inharmonicite
        son += poids * np.sin(2 * np.pi * f * t)
    attaque = np.clip(t / 0.006, 0, 1)
    if chute_rapide:
        enveloppe = np.exp(-t * 7.0)
    else:
        enveloppe = np.exp(-t * 1.5) * 0.75 + np.exp(-t * 6.0) * 0.25
    return son * attaque * enveloppe * force


def nappe(freqs, duree, force=0.32):
    """Nappe de cordes : entree et sortie lentes, sans attaque marquee."""
    n = int(duree * SR)
    t = np.arange(n) / SR
    son = np.zeros(n)
    for f in freqs:
        for detune in (-0.15, 0.0, 0.15):
            son += np.sin(2 * np.pi * (f + detune) * t) / 3
        son += 0.18 * np.sin(2 * np.pi * f * 2 * t)
    enveloppe = np.minimum(np.clip(t / 1.2, 0, 1), np.clip((duree - t) / 1.2, 0, 1))
    vibrato = 1 + 0.004 * np.sin(2 * np.pi * 4.5 * t)
    return son * enveloppe * vibrato * force / max(len(freqs), 1)


def reverb(x, retards=((0.041, .28), (0.073, .21), (0.109, .15), (0.157, .10))):
    sortie = x.copy()
    for retard, gain in retards:
        d = int(retard * SR)
        sortie[d:] += x[:-d] * gain
    return sortie


def composer(duree_totale, ambiance="douce"):
    reglage = AMBIANCES[ambiance]
    accords = reglage["accords"]
    mesure = reglage["mesure"]
    n_total = int(duree_totale * SR)
    piste = np.zeros(n_total + SR)

    i, pos = 0, 0
    while pos < n_total:
        aigus, graves = accords[i % len(accords)]
        bloc = np.zeros(int(mesure * SR) + SR // 2)

        na = nappe(graves + aigus[:1], mesure, force=reglage["nappe"])
        bloc[:len(na)] += na

        for k, f in enumerate(aigus):                      # arpege
            depart = int((k * 0.55) * SR)
            no = note(f, mesure - k * 0.55 + 0.5, force=reglage["piano"] - k * 0.04)
            fin = min(depart + len(no), len(bloc))
            bloc[depart:fin] += no[:fin - depart]

        if i % 2 == 0:                                     # note aigue de respiration
            depart = int(mesure * 0.55 * SR)
            no = note(aigus[-1] * 2, 2.2, force=reglage["piano"] * 0.42)
            fin = min(depart + len(no), len(bloc))
            bloc[depart:fin] += no[:fin - depart]

        if reglage["pulsation"]:                           # basse reguliere
            pas = mesure / 4
            for battement in range(4):
                depart = int(battement * pas * SR)
                no = note(graves[0], pas * 0.9,
                          force=reglage["pulsation"], chute_rapide=True)
                fin = min(depart + len(no), len(bloc))
                bloc[depart:fin] += no[:fin - depart]

        fin = min(pos + len(bloc), len(piste))
        piste[pos:fin] += bloc[:fin - pos]
        pos += int(mesure * SR)
        i += 1

    piste = reverb(piste)[:n_total]
    fondu = int(min(1.5, duree_totale / 6) * SR)
    piste[:fondu] *= np.linspace(0, 1, fondu)
    piste[-fondu:] *= np.linspace(1, 0, fondu)

    crete = np.max(np.abs(piste)) or 1.0
    return (piste / crete * 0.62).astype("float32")


def ecrire_wav(signal, chemin):
    import wave
    entier = (np.clip(signal, -1, 1) * 32767).astype("<i2")
    stereo = np.repeat(entier[:, None], 2, axis=1).tobytes()
    with wave.open(str(chemin), "w") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(stereo)


if __name__ == "__main__":
    duree = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
    voulues = [sys.argv[2]] if len(sys.argv) > 2 else list(AMBIANCES)
    for nom in voulues:
        dest = ICI / f"musique_{nom}.wav"
        ecrire_wav(composer(duree, nom), dest)
        print(f"OK {dest.name} — {duree:.0f} s")
