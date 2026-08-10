#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compose la musique de fond des publicites Lucky Conciergerie.

Elle est synthetisee ici, de zero : aucune licence a verifier, aucun risque
de reclamation sur YouTube ou Meta.

Piano feutre + nappe de cordes, progression lente en La mineur, volume bas
pour rester derriere les sous-titres.

Usage : python3 musique.py [duree_en_secondes]
"""
import sys, pathlib, math
import numpy as np

SR = 48000
ICI = pathlib.Path(__file__).resolve().parent


def note(freq, duree, force=1.0):
    """Une note de piano : harmoniques + decroissance exponentielle."""
    n = int(duree * SR)
    t = np.arange(n) / SR
    son = np.zeros(n)
    # le timbre du piano tient a ses harmoniques, de moins en moins fortes
    for rang, poids in enumerate([1.0, 0.42, 0.22, 0.12, 0.06], start=1):
        # legere inharmonicite : les cordes reelles ne sont jamais parfaites
        f = freq * rang * (1 + 0.0004 * rang * rang)
        son += poids * np.sin(2 * np.pi * f * t)
    attaque = np.clip(t / 0.006, 0, 1)              # 6 ms de montee
    chute = np.exp(-t * 1.5) * 0.75 + np.exp(-t * 6.0) * 0.25
    return son * attaque * chute * force


def nappe(freqs, duree, force=0.32):
    """Nappe de cordes : entree et sortie lentes, sans attaque marquee."""
    n = int(duree * SR)
    t = np.arange(n) / SR
    son = np.zeros(n)
    for f in freqs:
        for detune in (-0.15, 0.0, 0.15):           # 3 voix legerement desaccordees
            son += np.sin(2 * np.pi * (f + detune) * t) / 3
        son += 0.18 * np.sin(2 * np.pi * f * 2 * t)
    enveloppe = np.minimum(np.clip(t / 1.2, 0, 1),
                           np.clip((duree - t) / 1.2, 0, 1))
    vibrato = 1 + 0.004 * np.sin(2 * np.pi * 4.5 * t)
    return son * enveloppe * vibrato * force / max(len(freqs), 1)


def reverb(x, retards=((0.041, .28), (0.073, .21), (0.109, .15), (0.157, .10))):
    """Reverberation simple : quelques reflets decroissants."""
    sortie = x.copy()
    for retard, gain in retards:
        d = int(retard * SR)
        sortie[d:] += x[:-d] * gain
    return sortie


def composer(duree_totale):
    # La mineur : Am - F - C - G, une progression douce et rassurante
    accords = [
        ("Am", [220.00, 261.63, 329.63], [110.00, 164.81]),
        ("F",  [174.61, 220.00, 261.63], [87.31, 130.81]),
        ("C",  [196.00, 261.63, 329.63], [130.81, 196.00]),
        ("G",  [196.00, 246.94, 293.66], [98.00, 146.83]),
    ]
    par_accord = 4.0
    n_total = int(duree_totale * SR)
    piste = np.zeros(n_total + SR)

    i = 0
    pos = 0
    while pos < n_total:
        nom, aigus, graves = accords[i % len(accords)]
        n = int(par_accord * SR)

        # nappe tenue sous l'accord
        bloc = np.zeros(n + SR // 2)
        na = nappe(graves + aigus[:1], par_accord)
        bloc[:len(na)] += na

        # arpege : les notes s'egrenent au lieu de tomber ensemble
        for k, f in enumerate(aigus):
            depart = int((0.0 + k * 0.55) * SR)
            no = note(f, par_accord - k * 0.55 + 0.5, force=0.30 - k * 0.04)
            fin = min(depart + len(no), len(bloc))
            bloc[depart:fin] += no[:fin - depart]

        # une note aigue posee sur le 3e temps, pour respirer
        if i % 2 == 0:
            depart = int(2.2 * SR)
            no = note(aigus[-1] * 2, 2.2, force=0.13)
            fin = min(depart + len(no), len(bloc))
            bloc[depart:fin] += no[:fin - depart]

        fin = min(pos + len(bloc), len(piste))
        piste[pos:fin] += bloc[:fin - pos]
        pos += n
        i += 1

    piste = reverb(piste)[:n_total]

    # fondu d'entree et de sortie
    fondu = int(1.5 * SR)
    piste[:fondu] *= np.linspace(0, 1, fondu)
    piste[-fondu:] *= np.linspace(1, 0, fondu)

    crete = np.max(np.abs(piste)) or 1.0
    return (piste / crete * 0.62).astype("float32")


def ecrire_wav(signal, chemin):
    import wave
    entier = np.clip(signal, -1, 1)
    entier = (entier * 32767).astype("<i2")
    stereo = np.repeat(entier[:, None], 2, axis=1).tobytes()
    with wave.open(str(chemin), "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(stereo)


if __name__ == "__main__":
    duree = float(sys.argv[1]) if len(sys.argv) > 1 else 40.0
    dest = ICI / "musique_fond.wav"
    ecrire_wav(composer(duree), dest)
    print(f"OK {dest.name} — {duree:.0f} s, {dest.stat().st_size // 1024} Ko")
