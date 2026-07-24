# pipeline/ — Moteur de génération de carrousels

Structure du projet d'automatisation (voir la section « PROJET AUTOMATISATION »
de `../carroussel.md`).

## Arborescence
- `assets/logos/` : logos officiels des marques (fichiers PNG fournis par Martin).
  - `guestlucky.png` (à recevoir) — logo fond bleu marine, à extraire en transparent.
  - `lesousloueur.png` (à recevoir) — logo fond clair.
- `assets/backgrounds/` : photos de fond (temporaires faites main ici ; plus tard
  générées par Seedance sur le Mac de Martin).
- `engine/` : le code du moteur (génération HTML des 10 slides + rendu PNG/JPEG
  via Playwright). À construire.
- `output/` : sorties (PNG HD + JPEG Metricool-ready).

## Étapes (rappel)
1. Chaîne de création : contenu → photo → 10 slides → JPEG. **En cours.**
2. Publication Metricool (brouillon programmé).
3. Déclencheur automatique + filet de sécurité.

## À faire avant le 1er rendu réel
- Recevoir les fichiers logos (ZIP) → les placer dans `assets/logos/`.
- Choisir un 1er sujet Guestlucky (ou Claude en propose un).
