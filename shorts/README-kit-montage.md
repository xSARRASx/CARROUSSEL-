# Kit d'assets pour le montage des shorts

Petits visuels (icônes, badges, photos, captures) à intégrer dans le montage
des shorts de Sébastien. Les noms de fichiers sont ceux de **Kilian** : ils ne
changent jamais, c'est comme ça qu'il reconnaît le sujet automatiquement.

Tout est dans **`assets-montage/`**, en PNG.

---

## La règle qui compte : ne jamais laisser ça « faire IA »

Demande de Martin (03/08/2026) : *« je ne veux pas que ça fasse IA, je veux
vraiment naturel »*. Le premier lot a été audité image par image : **23 sur 29
ont été recalées**, presque toujours pour la même raison — **l'IA écrit du
texte, et elle l'écrit faux**.

Exemples réellement sortis du premier lot :

| Ce que l'IA a écrit | Ce que ça devrait être |
|---|---|
| ACCORD DU PROPRIÉT**ERE** | propriétaire |
| NUMÉRO D'**ENBEGRTEMENT** | enregistrement |
| Appartement **Lumiuxeux** | lumineux |
| Espace de **trovail** dédié | travail |
| Vous ne **paieer quaprèts** | payez qu'après |
| **JUNIE**, **FEBRUER**, LOW SEAS**E**N | juin, février |
| **Trouviez** votre location | trouvez |

D'où la répartition appliquée à tout le kit :

| Type d'asset | Comment il est fabriqué | Pourquoi |
|---|---|---|
| **Texte lisible** (badge, capture d'interface) | **HTML + navigateur** (`build_captures.py`) | Orthographe garantie, typographie nette. Zéro faute possible. |
| **Logo d'une vraie marque** | **Le vrai fichier de la marque** | L'IA invente le logotype. En attendant, un badge propre sert de remplacement. |
| **Icône, illustration, photo** | **IA (Gemini)** (`gen_assets_shorts.py`) | C'est là qu'elle est bonne — à condition de lui **interdire tout texte**. |

**Prompt-type pour une icône** : le sujet, puis toujours :
> Style icône flat vectoriel minimaliste, aplats de couleur unis, contours nets,
> composition centrée, fond blanc uni pur. Aucun texte, aucune lettre, aucun
> chiffre, aucun watermark. Formes simples et géométriquement correctes, aucun
> objet déformé.

**Prompt-type pour une photo** : le sujet, puis :
> Photographie professionnelle réaliste, lumière naturelle du jour, couleurs
> naturelles non saturées, mise au point nette. Aucun texte, aucun watermark.

---

## ⚠️ À remplacer par les vrais fichiers officiels

`logo-booking.png` et `logo-abritel.png` sont aujourd'hui des **badges
fabriqués en HTML** : nom de la plateforme écrit proprement, sans faute. Ce ne
sont **pas** les logotypes officiels — l'IA les déformait et inventait des
baselines fautives.

Pour un rendu impeccable, télécharger les vrais logos depuis l'espace presse /
marque de Booking.com et d'Abritel (Vrbo) et écraser les deux fichiers en
gardant exactement le même nom.

---

## Comment (re)fabriquer un asset

```bash
cd shorts

# 1. Icônes et photos (IA) — ne régénère que ce qui manque
python3 gen_assets_shorts.py
python3 gen_assets_shorts.py --force        # tout regénérer

# 2. Régénérer les assets recalés par un audit, prompts durcis
python3 regen_v2.py                          # tous
python3 regen_v2.py icone-mairie.png         # un seul

# 3. Badges et captures (HTML, texte garanti sans faute)
python3 build_captures.py
```

La clé Gemini vient de la variable d'environnement `GEMINI_API_KEY` — **jamais
dans le code**, le dépôt est public.

## Contrôle qualité (obligatoire avant livraison)

Chaque image doit être **regardée** avant d'être livrée. À traquer :
faute d'orthographe, lettres déformées, objet déformé (mains fusionnées,
billets fondus), fond pas vraiment blanc, style incohérent, logo inexact.

Le verdict du dernier audit est conservé dans `audit-v1.json`.
