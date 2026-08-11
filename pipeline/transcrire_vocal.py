#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSCRIRE UN MESSAGE VOCAL DE MARTIN (marche a suivre donnee par Martin, 11/08/2026)

    python3 transcrire_vocal.py vocal.ogg            (modele 'small', rapide)
    python3 transcrire_vocal.py vocal.ogg medium     (plus lent, plus fidele)

Le conteneur repart de zero a chaque session : installer d'abord Whisper.

    pip install --quiet faster-whisper

FORMATS LUS : .opus et .ogg (les vocaux WhatsApp), .m4a, .mp3, .wav, .mp4.
ffmpeg n'est PAS installe et ce n'est pas grave : le decodage passe par PyAV,
verifie le 11/08/2026 sur un vrai fichier .opus.

------------------------------------------------------------------------------
POURQUOI CE SCRIPT FAIT PLUS QUE LA COMMANDE D'ORIGINE

Martin : « Mets TOUJOURS vad_filter=True. Sans lui, Whisper invente du texte
sur les silences (genre "Sous-titres realises par la communaute d'Amara.org") ».
C'est juste, et le VAD reste actif ici. Mais il ne suffit PAS toujours : teste
le 11/08/2026 sur un son continu non-parle, Whisper a sorti exactement cette
phrase d'Amara MALGRE vad_filter=True. Le VAD coupe les SILENCES ; il ne
protege pas d'un bruit qu'il prend pour une voix.

Deux garde-fous sont donc ajoutes :

  1. no_speech_prob — le modele donne lui-meme sa probabilite que le passage ne
     soit PAS de la parole. Sur l'invention du test : 0,882. Autrement dit il
     "savait" et ecrivait quand meme. Au-dessus du seuil, on ecarte.
  2. une liste des phrases parasites connues de Whisper en francais (generique
     de sous-titrage, remerciements de fin de video...).

RIEN N'EST SUPPRIME EN SILENCE : tout passage ecarte est affiche dans un
encadre « PASSAGES ECARTES » pour que Martin puisse verifier.

Enfin, Whisper ecorche les noms propres (GuestLucky, Beds24, PriceLabs...).
Le script les retablit et DIT lesquels il a corriges.
"""
import re
import sys
import pathlib

# --------------------------------------------------------------------------
# Noms propres et termes metier que Whisper ecorche systematiquement.
# Cle = l'orthographe correcte ; valeurs = ce que Whisper ecrit a la place.
# La comparaison ignore la casse et les accents parasites.
# --------------------------------------------------------------------------
LEXIQUE = {
    "GuestLucky":      ["guest lucky", "guestlucky", "gest lucky", "guess lucky",
                        "guest lucki", "gueste lucky", "guest lakie", "guestlaki"],
    "Lucky Copilot":   ["lucky copilote", "lucky co-pilote", "lucky copilot",
                        "laki copilote", "lucky co pilote"],
    "Lucky Cover":     ["lucky cover", "laki cover", "lucky couvert"],
    "Lucky Clean":     ["lucky clean", "laki clean", "lucky cline"],
    "Beds24":          ["beds 24", "bed 24", "bed24", "beads 24", "bedse 24",
                        "bds 24"],
    "Channel Manager": ["channel manager", "chanel manager", "channel manageur",
                        "chanel manageur"],
    "PriceLabs":       ["price labs", "pricelabs", "price lab", "prislabs",
                        "price labse"],
    "Airbnb":          ["air bnb", "airbnb", "air b n b", "air b and b",
                        "airbeanbee", "air bene bee"],
    "Booking":         ["booking", "bouquine", "bookingue"],
    "Abritel":         ["abritel", "abri tel", "abritelle"],
    "loi Hoguet":      ["loi hoguet", "loi oguet", "loi ogay", "loi hoget",
                        "loi hogue", "loi oge"],
    "Catapush":        ["catapush", "cata push", "cata pouche", "catapouche"],
    "Igloohome":       ["igloohome", "igloo home", "iglou home", "iglouhome"],
    "Leapway":         ["leapway", "leap way", "lipway", "lip way"],
    "Factur-X":        ["factur x", "facture x", "facturx", "factur ix"],
    "Meetch":          ["meetch", "mitch", "meech", "mitche"],
    "PlanetHoster":    ["planet hoster", "planethoster", "planete hoster"],
    "Booking Engine":  ["booking engine", "bookingue engine", "booking enjin"],
    "Auto Action":     ["auto action", "autoaction", "auto-action"],
    "iClosed":         ["iclosed", "i closed", "aille closed"],
    "Instagram":       ["instagram", "insta gram"],
    "Gemini":          ["gemini", "geminie", "jemini", "gemeni"],
    "Stripe":          ["stripe", "straip", "stripes"],
    "Zoho":            ["zoho", "zolo", "zoo ho"],
    "Smoobu":          ["smoobu", "smoubou", "smou bou"],
    "Laravel":         ["laravel", "lara vel", "laravelle"],
    "Pierre":          ["pierre"],
    "Sebastien":       ["sebastien", "sebastian"],
}

# Phrases que Whisper invente en francais quand il n'y a pas de parole claire.
PARASITES = [
    "sous-titres réalisés par la communauté d'amara.org",
    "sous-titres réalisés par la communauté d'amara",
    "sous-titrage société radio-canada",
    "sous-titrage st' 501",
    "merci d'avoir regardé cette vidéo",
    "merci d'avoir regardé la vidéo",
    "abonnez-vous à la chaîne",
    "n'oubliez pas de vous abonner",
    "générique de fin",
    "à bientôt pour une nouvelle vidéo",
    "merci à tous et à bientôt",
]

# Au-dessus de ce seuil, le modele estime lui-meme que ce n'est pas de la
# parole. Volontairement haut (0,75) : on ecarte seulement les cas francs,
# pour ne jamais jeter une vraie phrase de Martin.
SEUIL_NON_PAROLE = 0.75


def est_parasite(texte):
    """La phrase fait-elle partie des inventions connues de Whisper ?"""
    t = texte.strip().lower().rstrip(".!? ")
    return any(p in t for p in PARASITES)


def corriger_noms(texte):
    """Retablit les noms propres. Renvoie (texte corrige, liste des corrections)."""
    corrections = []
    for correct, variantes in LEXIQUE.items():
        for var in sorted(variantes, key=len, reverse=True):
            motif = re.compile(r"\b" + re.escape(var).replace(r"\ ", r"\s+") + r"\b",
                               re.IGNORECASE)
            trouves = motif.findall(texte)
            if not trouves:
                continue
            # On ne signale que les vraies corrections : si Whisper avait deja
            # ecrit exactement le bon mot, inutile de le mentionner.
            reels = [t for t in trouves if t != correct]
            texte = motif.sub(correct, texte)
            if reels:
                corrections.append((reels[0], correct, len(reels)))
    return texte, corrections


def transcrire(chemin, taille="small"):
    from faster_whisper import WhisperModel

    fichier = pathlib.Path(chemin)
    if not fichier.exists():
        sys.exit(f"Fichier introuvable : {fichier}")

    modele = WhisperModel(taille, device="cpu", compute_type="int8")
    segments, info = modele.transcribe(
        str(fichier),
        language="fr",
        vad_filter=True,               # consigne de Martin : silences coupes
        condition_on_previous_text=False,  # evite les boucles de repetition
    )

    gardes, ecartes = [], []
    for s in segments:
        if est_parasite(s.text):
            ecartes.append((s.start, s.text.strip(), "phrase parasite connue"))
        elif s.no_speech_prob > SEUIL_NON_PAROLE:
            ecartes.append((s.start, s.text.strip(),
                            f"non-parole {s.no_speech_prob:.0%}"))
        else:
            gardes.append(s.text)

    texte = " ".join(t.strip() for t in gardes).strip()
    texte = re.sub(r"\s+", " ", texte)
    texte, corrections = corriger_noms(texte)

    print(f"\n--- TRANSCRIPTION ({fichier.name}, modele {taille}, "
          f"{info.duration:.0f}s d'audio) ---\n")
    print(texte if texte else "(aucune parole detectee)")

    if corrections:
        print("\n--- NOMS RETABLIS (a signaler a Martin) ---")
        for avant, apres, n in corrections:
            fois = f" ({n} fois)" if n > 1 else ""
            print(f"  « {avant} » -> « {apres} »{fois}")

    if ecartes:
        print("\n--- PASSAGES ECARTES (rien n'est supprime en silence) ---")
        for debut, txt, motif in ecartes:
            print(f"  [{debut:6.1f}s] {txt!r}  ({motif})")

    print()
    return texte


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage : python3 transcrire_vocal.py <fichier audio> [small|medium]")
    transcrire(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "small")
