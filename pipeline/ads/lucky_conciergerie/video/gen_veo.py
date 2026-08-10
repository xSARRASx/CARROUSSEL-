#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les plans video Lucky Conciergerie avec Veo (API Gemini).

Usage : python3 gen_veo.py <fichier_plans.json> [--modele fast|lite|hq]

Le fichier de plans est une liste :
  [{"id": "v1_plan1", "prompt": "...", "duree": 8}, ...]

Chaque plan est genere une seule fois : Veo est facture a la seconde,
on ne relance donc jamais un plan deja produit (fichier .mp4 present).
"""
import os, sys, json, time, pathlib, urllib.request, urllib.error

KEY = os.environ["GEMINI_API_KEY"]
BASE = "https://generativelanguage.googleapis.com/v1beta"
ICI = pathlib.Path(__file__).resolve().parent
CLIPS = ICI / "clips"
CLIPS.mkdir(parents=True, exist_ok=True)

MODELES = {
    "hq":   "veo-3.1-generate-preview",
    "fast": "veo-3.1-fast-generate-preview",
    "lite": "veo-3.1-lite-generate-preview",
}

NEG = ("text, letters, captions, subtitles, watermark, logo, distorted hands, "
       "extra fingers, deformed faces, morphing objects")


class Quota(Exception):
    """Quota Veo atteint : il faut patienter, pas abandonner."""


def appel(url, body=None, methode=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=methode,
        headers={"x-goog-api-key": KEY, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:300]
        if e.code == 429:
            raise Quota(detail)
        raise SystemExit(f"HTTP {e.code} sur {url.split('?')[0]}\n{detail}")


def lancer(plan, modele):
    body = {
        "instances": [{"prompt": plan["prompt"]}],
        "parameters": {
            "aspectRatio": plan.get("ratio", "9:16"),
            "durationSeconds": plan.get("duree", 8),
            "negativePrompt": NEG,
        },
    }
    op = appel(f"{BASE}/models/{modele}:predictLongRunning", body)
    return op["name"]


def attendre(nom_op, etiquette, timeout=900):
    debut = time.time()
    while time.time() - debut < timeout:
        op = appel(f"{BASE}/{nom_op}")
        if op.get("done"):
            if "error" in op:
                print(f"  ECHEC {etiquette} : {op['error'].get('message','')[:200]}")
                return None
            return op
        time.sleep(12)
    print(f"  TIMEOUT {etiquette}")
    return None


def extraire_uri(op):
    rep = op.get("response", {})
    for cle in ("generatedVideos", "videos"):
        for v in rep.get(cle, []) or []:
            uri = (v.get("video") or {}).get("uri") or v.get("uri")
            if uri:
                return uri
    gen = rep.get("generateVideoResponse", {})
    for v in gen.get("generatedSamples", []) or []:
        uri = (v.get("video") or {}).get("uri")
        if uri:
            return uri
    return None


def telecharger(uri, dest):
    sep = "&" if "?" in uri else "?"
    req = urllib.request.Request(uri + f"{sep}key={KEY}")
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest.stat().st_size


def main():
    fichier = sys.argv[1] if len(sys.argv) > 1 else str(ICI / "plans.json")
    modele_cle = "fast"
    if "--modele" in sys.argv:
        modele_cle = sys.argv[sys.argv.index("--modele") + 1]
    modele = MODELES[modele_cle]

    plans = json.loads(pathlib.Path(fichier).read_text(encoding="utf-8"))
    a_faire = [p for p in plans if not (CLIPS / f"{p['id']}.mp4").exists()]
    secondes = sum(p.get("duree", 8) for p in a_faire)
    print(f"Modele : {modele}")
    print(f"{len(a_faire)} plan(s) a generer, {secondes} secondes de video au total.")
    if not a_faire:
        return

    # un plan a la fois : le quota Veo n'accepte que tres peu de generations
    # simultanees, et une rafale se solde par des 429 en serie
    for p in a_faire:
        dest = CLIPS / f"{p['id']}.mp4"
        for essai in range(4):
            try:
                nom = lancer(p, modele)
            except Quota:
                attente = 60 * (essai + 1)
                print(f"  quota atteint sur {p['id']}, nouvelle tentative dans {attente}s")
                time.sleep(attente)
                continue

            op = attendre(nom, p["id"])
            if not op:                       # erreur interne Veo : on retente
                time.sleep(20)
                continue
            uri = extraire_uri(op)
            if not uri:
                print(f"  PAS DE VIDEO pour {p['id']}")
                break
            taille = telecharger(uri, dest)
            print(f"  OK {dest.name} ({taille // 1024} Ko)", flush=True)
            break
        else:
            print(f"  ABANDON {p['id']} apres 4 tentatives", flush=True)
        time.sleep(6)                        # on laisse respirer le quota

    faits = len(list(CLIPS.glob("v*_p*.mp4")))
    print(f"TERMINE — {faits} clip(s) disponibles")


if __name__ == "__main__":
    main()
