#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REGENERATION V3 : les 5 icones encore recalees par l'audit v2.

Le defaut qui reste est TOUJOURS le meme : des qu'il y a des MAINS ou des
PERSONNAGES, l'IA fusionne les doigts, laisse des zones non remplies ou des
taches parasites. Deux parades appliquees ici :
  1. quand le sujet n'a pas besoin de mains, on les supprime du prompt ;
  2. quand elles sont indispensables (poignee de main), on impose des aplats
     de deux couleurs franches, sans degrade ni ombre, doigts separes.
"""
import importlib.util, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("g", ROOT / "gen_assets_shorts.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

NET = (" Style icône flat vectoriel minimaliste, aplats de couleur unis et franches, "
       "contours nets, aucun dégradé, aucune ombre, aucune tache ni pixel parasite, "
       "aucune zone non remplie, fond blanc uni pur. Aucun texte, aucune lettre, "
       "aucun chiffre, aucun symbole monétaire, aucun watermark. Formes simples, "
       "fermées et géométriquement correctes.")

REGEN = {
    # mains supprimees : le sujet se lit tres bien sans
    "icone-autorisation-proprietaire.png":
        "Une feuille de contrat rectangulaire vue de face avec quelques lignes grises "
        "abstraites, un stylo bleu posé en diagonale dessus, et un petit tampon rond "
        "bleu lisse dans le coin en bas à droite. Aucune main, aucun personnage." + NET,
    "icone-loyer.png":
        "Une enveloppe blanche ouverte vue de face, d'où dépassent trois billets "
        "rectangulaires vert clair parfaitement unis et totalement vierges, sans aucune "
        "inscription ni symbole dessus. Aucune main, aucun personnage." + NET,
    "icone-jacuzzi.png":
        "Un jacuzzi extérieur rond vu de trois quarts, cuve en bois clair, eau bleue avec "
        "quelques bulles rondes blanches, deux petites marches en bois devant. Le jacuzzi "
        "est VIDE : aucune personne, aucun personnage, aucune silhouette." + NET,
    # mains indispensables : on impose deux aplats francs
    "icone-proprietaire.png":
        "Deux mains stylisées qui se serrent, vues de profil, dessinées en deux aplats de "
        "couleur franche nettement séparés par un contour blanc : la main de gauche "
        "entièrement bleue, la main de droite entièrement orange. Cinq doigts distincts et "
        "bien séparés sur chaque main. Aucune autre couleur." + NET,
    "icone-comptable.png":
        "Buste d'une personne stylisée vue de face, coupée à la taille, derrière un bureau "
        "vu de face ; sur le bureau une calculatrice vierge et une pile de documents. "
        "Silhouette simple entièrement remplie de couleur, visage sans détail, aucune jambe "
        "visible, aucun doigt détaillé." + NET,
}

def main():
    cibles = [a for a in sys.argv[1:] if not a.startswith("-")]
    todo = {k: v for k, v in REGEN.items() if not cibles or k in cibles}
    fails = []
    for name, prompt in todo.items():
        try:
            g.generate(name, prompt, "1:1")
        except Exception as e:
            print(f"ECHEC {name}: {e}", flush=True)
            fails.append(name)
        time.sleep(3)
    print(f"\nTermine. {len(todo)-len(fails)}/{len(todo)} regeneres" +
          (f" ; echecs : {', '.join(fails)}" if fails else ""), flush=True)

if __name__ == "__main__":
    main()
