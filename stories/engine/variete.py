#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONTROLE DE VARIETE — a lancer AVANT chaque livraison.

    python3 stories/engine/variete.py banque-13 interactifs-13

Demande de Martin, le 10/09/2026 : « je vois que les stories que tu fais sont
parfois les mêmes, je veux des choses différentes ». Une promesse de faire
attention ne tient pas trois semaines : il fallait une mesure.

CE QUE CE CONTROLE REGARDE, et pourquoi :

1. LES FONDS DEJA VUS RECEMMENT. Sur les 10 premiers lots de quiz, le meme
   fond (bg_plage_aube) revenait 13 fois. Martin poste ces quiz TOUS LES
   SAMEDIS : il voyait donc la meme photo chaque semaine.

2. LES FORMULES RECOPIEES. 40 couvertures sur 40 finissaient par « ... juste
   après », et les 10 lots de quiz ouvraient et fermaient avec exactement le
   meme texte. Les listes tournantes de photo_style.py (ACCROCHES,
   QUIZ_OUVERTURES, QUIZ_CLOTURES) sont la pour ca, encore faut-il s'en servir.

3. LA FORME DES SEQUENCES. Les 40 sequences commencaient par `cover` et 33
   finissaient par `fin`. Ce n'est pas interdit -- une couverture qui promet
   et une cloture qui conclut, c'est la regle de la maison -- mais une
   sequence entiere batie sur la MEME suite de gabarits qu'une precedente
   donne deux fournees jumelles.

4. LES GABARITS OUBLIES. focus, cover, p_steps et fin representaient 73 % de
   tout. p_bars, p_formula, p_vs et p_timeline dormaient. Une fournee qui
   n'utilise que les quatre habituels est signalee.

Sortie 1 si quelque chose cloche, comme `livraison.py --controle`.
"""
import collections
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
GABARITS = ("cover", "focus", "fin", "p_steps", "p_timeline", "p_bars",
            "p_bigstat", "p_duo", "p_vs", "p_formula", "p_cta",
            "quiz_q", "quiz_r", "sondage")
HABITUELS = {"cover", "focus", "fin", "p_steps"}

# Un fond revu dans les DERNIERES fournees fatigue l'oeil. Trois lots, c'est
# une semaine et demie de publication.
PROFONDEUR = 3


def builds():
    """Les fichiers de construction, du plus ancien au plus recent."""
    def rang(p):
        m = re.search(r"(\d+)", p.stem)
        return (p.stem.split("0")[0], int(m.group(1)) if m else 0)
    return sorted(ICI.glob("build_*.py"), key=rang)


def fonds_de(fichier):
    return re.findall(r'bg_[a-z_]+', fichier.read_text(encoding="utf-8"))


def sequences_de(fichier):
    """{nom de sequence: [gabarits dans l'ordre]} pour un build de banque."""
    txt = fichier.read_text(encoding="utf-8")
    out = {}
    for nom, corps in re.findall(r'^"(\w+)": \[$(.*?)^\],$', txt, re.S | re.M):
        gab = [g for g in re.findall(r'^    (\w+)\(', corps, re.M) if g in GABARITS]
        if gab:
            out[nom] = gab
    return out


def controler(lots):
    alertes, remarques = [], []
    tous = builds()

    for lot in lots:
        # « banque-13 » -> build_banque13.py
        stem = "build_" + lot.replace("-", "")
        f = ICI / f"{stem}.py"
        if not f.is_file():
            alertes.append(f"{lot} : {f.name} introuvable")
            continue

        precedents = [p for p in tous if p != f
                      and p.stem.split("0")[0] == stem.split("0")[0]][-PROFONDEUR:]

        # 1. fonds deja vus dans les fournees precedentes
        mes_fonds = fonds_de(f)
        vus = collections.Counter()
        for p in precedents:
            vus.update(set(fonds_de(p)))
        repetes = sorted({b for b in set(mes_fonds) if vus[b] >= PROFONDEUR})
        if repetes:
            alertes.append(
                f"{lot} : fond(s) présent(s) dans les {PROFONDEUR} fournées "
                f"précédentes -> {', '.join(repetes)}")

        # ... et deux fois le meme fond DANS le lot
        doubles = sorted({b for b, n in collections.Counter(mes_fonds).items() if n > 1})
        if doubles:
            remarques.append(f"{lot} : fond utilisé plus d'une fois -> {', '.join(doubles)}")

        txt = f.read_text(encoding="utf-8")

        # 2. formules recopiees
        n_juste_apres = len(re.findall(r'juste après"', txt))
        n_cover = len(re.findall(r'^    cover\(', txt, re.M))
        if n_cover and n_juste_apres >= n_cover:
            alertes.append(
                f"{lot} : les {n_cover} couvertures finissent toutes par "
                f"« juste après ». Utilise photo_style.accroche().")
        for phrase, quoi in (("3 questions. Vote à chaque fois", "l'ouverture du quiz"),
                             ("Tout est détaillé dans la vidéo sur la chaîne", "la clôture du quiz")):
            if phrase in txt:
                alertes.append(
                    f"{lot} : {quoi} reprend le texte par défaut, identique aux "
                    f"lots précédents. Utilise photo_style.quiz_ouverture() / "
                    f"quiz_cloture().")

        # 3 et 4 : la forme des sequences (banques seulement)
        seqs = sequences_de(f)
        if seqs:
            deja = {}
            for p in precedents:
                for nom, gab in sequences_de(p).items():
                    deja.setdefault(tuple(gab), f"{p.stem}/{nom}")
            for nom, gab in seqs.items():
                jumelle = deja.get(tuple(gab))
                if jumelle:
                    alertes.append(
                        f"{lot}/{nom} : même suite de gabarits que {jumelle} "
                        f"({' > '.join(gab)})")
            employes = {g for gab in seqs.values() for g in gab}
            if not (employes - HABITUELS):
                alertes.append(
                    f"{lot} : que des gabarits habituels ({', '.join(sorted(employes))}). "
                    f"Il en existe d'autres : p_bars, p_formula, p_vs, p_timeline, p_bigstat.")
            else:
                remarques.append(f"{lot} : gabarits employés -> {', '.join(sorted(employes))}")

    for r in remarques:
        print(f"    {r}", flush=True)
    if alertes:
        print("\nTROP DE REPETITION — Martin l'a demandé, on ne livre pas comme ça :", flush=True)
        for a in alertes:
            print(f"  - {a}", flush=True)
        return 1
    print(f"\nVariété OK : {len(lots)} lot(s), rien de recopié.", flush=True)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(controler(sys.argv[1:]))
