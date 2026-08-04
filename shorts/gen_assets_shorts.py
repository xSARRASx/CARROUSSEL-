#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kit d'assets pour le MONTAGE DES SHORTS (demande de Martin, 03/08/2026).

Genere avec Gemini (gemini-2.5-flash-image) les petites icones / images que
Kilian integre dans le montage des shorts. Les prompts sont EXACTEMENT ceux
de la liste de Martin ("A taper dans la barre") ; les noms de fichiers sont
ceux de Kilian.

⚠️ Le tableau envoye par Martin etait coupe a droite : certains noms sont
completes logiquement (marques d'un commentaire "# nom complete").

Cle API : variable d'environnement GEMINI_API_KEY (jamais dans le code).
Usage :
  python3 gen_assets_shorts.py            # genere les manquants
  python3 gen_assets_shorts.py --force    # regenere tout
"""
import base64, io, json, os, pathlib, sys, time, urllib.request, urllib.error
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "assets-montage"
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# (nom de fichier Kilian, prompt Martin, aspect)
ASSETS = [
    # --- Administratif / legal
    ("icone-mairie.png", "Icône d'une mairie française avec drapeau bleu blanc rouge, style flat, fond blanc", "1:1"),
    ("icone-autorisation-proprietaire.png", "Document contrat signé avec stylo, accord du propriétaire, style icône, fond blanc", "1:1"),
    ("icone-numero-enregistrement.png", "Formulaire officiel avec numéro d'enregistrement et tampon mairie, style flat, fond blanc", "1:1"),
    ("icone-changement-usage.png", "Maison qui se transforme en local commercial, changement d'usage, style icône, fond blanc", "1:1"),
    # --- Argent
    ("icone-cashflow.png", "Liasse de billets euros avec flèche verte qui monte, cashflow, style flat, fond blanc", "1:1"),
    ("icone-rentabilite.png", "Symbole pourcentage avec flèche de rentabilité ROI, style icône, fond blanc", "1:1"),
    ("icone-calculatrice.png", "Calculatrice avec pièces euros, calcul de rentabilité, style flat, fond blanc", "1:1"),
    ("icone-loyer.png", "Enveloppe avec billets euros loyer, style icône, fond blanc", "1:1"),
    # --- Plateformes
    ("logo-booking.png", "Logo Booking.com officiel, fond blanc", "1:1"),
    ("logo-abritel.png", "Logo Abritel Vrbo officiel, fond blanc", "1:1"),
    ("capture-annonce-airbnb.png", "Capture d'écran d'une annonce Airbnb appartement, interface application, fond blanc", "9:16"),
    ("icone-etoiles-avis.png", "Cinq étoiles dorées avis client superhost, style icône, fond blanc", "1:1"),
    # --- Conciergerie
    ("icone-menage.png", "Produits de ménage spray et éponge, style icône flat, fond blanc", "1:1"),                    # nom complete
    ("icone-checkin.png", "Boîte à clés sécurisée avec clés, check-in autonome, style icône, fond blanc", "1:1"),       # nom complete
    ("icone-linge.png", "Pile de draps et serviettes propres pliés, style icône, fond blanc", "1:1"),                   # nom complete
    ("icone-serrure.png", "Serrure connectée à code digital sur une porte, style icône, fond blanc", "1:1"),            # nom complete
    # --- Prospection / negociation
    ("icone-proprietaire.png", "Deux mains qui se serrent, accord propriétaire, style icône flat, fond blanc", "1:1"),  # nom complete
    ("icone-agence.png", "Devanture d'une agence immobilière, style icône flat, fond blanc", "1:1"),                    # nom complete
    ("icone-contrat.png", "Stylo qui signe un contrat, style icône, fond blanc", "1:1"),                                # nom complete
    ("icone-telephone.png", "Téléphone avec appel de prospection, style icône flat, fond blanc", "1:1"),                # nom complete
    # --- Ameublement / deco
    ("icone-meuble.png", "Canapé et meubles modernes, style icône flat, fond blanc", "1:1"),
    ("icone-home-staging.png", "Avant après home staging d'un appartement, style illustration, fond blanc", "1:1"),     # nom complete
    ("icone-jacuzzi.png", "Jacuzzi spa extérieur, style icône flat, fond blanc", "1:1"),
    ("photo-appartement.png", "Photo d'un appartement meublé moderne et lumineux, décoration soignée", "9:16"),         # nom complete
    # --- Fiscalite
    ("icone-lmnp.png", "Badge avec texte LMNP loueur meublé non professionnel, style flat, fond blanc", "1:1"),
    ("icone-impots.png", "Feuille de déclaration d'impôts français, style icône, fond blanc", "1:1"),                   # nom complete
    ("icone-comptable.png", "Expert-comptable avec documents et calculatrice, style icône flat, fond blanc", "1:1"),    # nom complete
    # --- Marche
    ("icone-france-carte.png", "Carte de France simple bleue, style flat, fond blanc", "1:1"),                          # nom complete
    ("icone-saisonnalite.png", "Calendrier avec haute et basse saison touristique, style icône, fond blanc", "1:1"),    # nom complete
    # --- Mindset (noms entierement coupes dans le message de Martin -> deduits)
    ("icone-objectif.png", "Cible avec flèche en plein centre, objectif atteint, style icône flat, fond blanc", "1:1"), # nom deduit
    ("icone-experience.png", "Badge médaille avec texte 11 ans d'expérience, style flat, fond blanc", "1:1"),           # nom deduit

    # === VAGUE 2 (03/08, apres le retour de Martin "je veux pas que ca fasse IA") ===
    # Vraies photos d'interieur, nettes, pour la galerie de la capture Airbnb et
    # pour le montage. Prompt anti-IA : photographie immobiliere reelle, lumiere
    # naturelle, aucun texte (le texte est ce qui trahit l'IA).
    ("photo-salon.png", "Photographie immobilière professionnelle d'un salon d'appartement français lumineux, "
     "parquet en chevron, canapé gris clair, plantes vertes, grandes fenêtres, lumière naturelle du jour, "
     "photo réaliste prise à l'objectif grand angle, couleurs naturelles, aucun texte, aucun logo", "4:3"),
    ("photo-cuisine.png", "Photographie immobilière professionnelle d'une cuisine d'appartement moderne blanche, "
     "plan de travail en bois, crédence carrelage métro, lumière naturelle du jour, photo réaliste, "
     "couleurs naturelles, aucun texte, aucun logo", "4:3"),
    ("photo-chambre.png", "Photographie immobilière professionnelle d'une chambre d'appartement, lit double avec "
     "linge blanc impeccable, table de chevet en bois, lumière naturelle douce du matin, photo réaliste, "
     "couleurs naturelles, aucun texte, aucun logo", "4:3"),
    ("photo-salle-de-bain.png", "Photographie immobilière professionnelle d'une salle de bain moderne, carrelage "
     "clair, serviettes blanches pliées, grand miroir, lumière naturelle, photo réaliste, couleurs naturelles, "
     "aucun texte, aucun logo", "4:3"),
]

def call_gemini(body, key):
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)

def generate(name, prompt, aspect):
    key = os.environ.get("GEMINI_API_KEY")
    assert key, "GEMINI_API_KEY absente de l'environnement"
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"imageConfig": {"aspectRatio": aspect}},
    }
    data = None
    for attempt, wait in enumerate((0, 10, 30, 60), 1):
        if wait:
            print(f"  ...nouvel essai dans {wait}s ({name})")
            time.sleep(wait)
        try:
            data = call_gemini(body, key)
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:300]
            if e.code == 400 and body.get("generationConfig"):
                body.pop("generationConfig", None)
                data = call_gemini(body, key)
                break
            if e.code in (429, 500, 503) and attempt < 4:
                continue
            raise RuntimeError(f"Gemini HTTP {e.code}: {detail}")
    assert data, f"Gemini indisponible pour {name}"
    parts = data["candidates"][0]["content"]["parts"]
    b64 = next((p["inlineData"]["data"] for p in parts if "inlineData" in p), None)
    assert b64, f"pas d'image renvoyee pour {name}"
    im = Image.open(io.BytesIO(base64.b64decode(b64))).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)
    im.save(OUT / name, "PNG", optimize=True)
    print(f"{name}  {im.width}x{im.height}  ({(OUT / name).stat().st_size // 1024} Ko)")

def main():
    force = "--force" in sys.argv
    fails = []
    for name, prompt, aspect in ASSETS:
        if (OUT / name).exists() and not force:
            print(f"{name}  deja present, saute")
            continue
        try:
            generate(name, prompt, aspect)
        except Exception as e:
            print(f"ECHEC {name}: {e}")
            fails.append(name)
        time.sleep(3)      # douceur avec le quota par minute
    print(f"\nTermine. {len(ASSETS) - len(fails)}/{len(ASSETS)} ok" +
          (f" ; echecs : {', '.join(fails)}" if fails else ""))

if __name__ == "__main__":
    main()
