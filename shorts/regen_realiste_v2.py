#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CORRECTION du kit realiste : regenere les photos recalees par l'audit, en
reutilisant DIRECTEMENT le prompt corrige que l'audit a redige pour chacune
(shorts/audit-realiste.json).

Les trois pieges identifies sur les photos :
  1. les CLAVIERS (serrure a code, calculatrice) : l'IA invente les chiffres
     (4-8-9 au lieu de 7-8-9, deux touches 0, chiffres manquants). Parade :
     "touches vues en biais, aucun chiffre lisible" ou cadrage qui les exclut.
  2. le rendu 3D qui revient (bois trop lisse, bulles figees, tissu sans
     grain). Parade : exiger les IMPERFECTIONS (grain, micro-rayures, noeuds
     du bois, plis, poussiere, reflets irreguliers).
  3. l'ANATOMIE des mains en gros plan. Parade : cadrer plus large et exiger
     "cinq doigts, ongles visibles, doigts bien separes".
"""
import importlib.util, json, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("g", ROOT / "gen_assets_shorts.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

audit = json.loads((ROOT / "audit-realiste.json").read_text(encoding="utf-8"))
todo = {r["file"]: r["prompt_corrige"] for r in audit
        if r["verdict"] == "refaire" and r.get("prompt_corrige")}

cibles = [a for a in sys.argv[1:] if not a.startswith("-")]
if cibles:
    todo = {k: v for k, v in todo.items() if k in cibles}

fails = []
for name, prompt in todo.items():
    try:
        g.generate(name, prompt, "1:1")
    except Exception as e:
        print(f"ECHEC {name}: {e}", flush=True)
        fails.append(name)
    time.sleep(3)
print(f"\nTermine. {len(todo) - len(fails)}/{len(todo)} regeneres" +
      (f" ; echecs : {', '.join(fails)}" if fails else ""), flush=True)
