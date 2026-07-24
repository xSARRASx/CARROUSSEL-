# Maxi prompt de démarrage — session « Robot Carrousels »

> À COLLER dans une NOUVELLE discussion Claude Code, lancée sur :
> - Environnement : **CARROUSSEL AUTO** (réseau ouvert / Accès réseau = Complet)
> - Dépôt : **CARROUSSEL-**
> - Branche : **claude/salut-af8y9u**
>
> ⚠️ AVANT de lancer la session : dans l'environnement CARROUSSEL AUTO, ajouter dans
> « Variables d'environnement » (privé, jamais dans le code) :
> `SEEDANCE_API_KEY=...` (la vraie clé Seedance) et, quand dispo,
> `METRICOOL_TOKEN=...` (le token Metricool).

---

Salut Claude. On reprend un projet en cours, avance en français, vocabulaire simple,
par micro-étapes (Martin débute en code).

AVANT TOUTE ACTION : lis le fichier `carroussel.md` à la racine du dépôt CARROUSSEL-
EN ENTIER. C'est la mémoire complète du projet (les 3 marques, les chartes, les règles
de contenu et de mise en page, ce qui est déjà fait, et le plan d'automatisation).
Lis aussi `pipeline/README.md`.

CONTEXTE COURT : je m'appelle Martin. On construit un ROBOT qui, tout seul CHAQUE
SEMAINE, crée ET publie des carrousels Instagram pour 2 marques, à partir d'une vidéo
YouTube qui sort le dimanche.

DÉJÀ FAIT (dans le repo) :
- La mémoire `carroussel.md`.
- Le MOTEUR de carrousels, testé et fonctionnel :
  - `pipeline/engine/build_guestlucky.py` (charte violet/rose)
  - `pipeline/engine/build_lesousloueur.py` (charte navy/orange/bleu)
  - `pipeline/engine/render.py` (HTML -> PNG 3240x4050 + JPEG 1080x1350 Metricool-ready,
    contrôle débordement + anti-tiret)
- Logos détourés + police Montserrat locale dans `pipeline/assets/`.
- Le fond des slides est TEMPORAIRE (fait main). Il devra être remplacé par une vraie
  photo générée par Seedance.

CET ENVIRONNEMENT a le réseau OUVERT. PREMIÈRE CHOSE À FAIRE : vérifie que tu atteins
bien l'extérieur (codes HTTP) :
- `curl -sS -m 15 -o /dev/null -w "%{http_code}\n" https://www.youtube.com`
- `curl -sS -m 15 -o /dev/null -w "%{http_code}\n" https://api.seedance2.ai`
- `curl -sS -m 15 -o /dev/null -w "%{http_code}\n" https://app.metricool.com`
Dis-moi les 3 codes. S'ils ne sont plus 403, le réseau est bon.

OBJECTIF (plan détaillé dans `carroussel.md` > « PROJET AUTOMATISATION ») :
- Étape 1 (FAITE) : moteur de création des slides.
- Étape 2 : brique « récupérer la transcription » de la DERNIÈRE vidéo de la chaîne
  YouTube https://www.youtube.com/@moresebastien.
- Étape 3 : brique « photo de fond Seedance » (base https://api.seedance2.ai, clé dans
  la variable d'environnement SEEDANCE_API_KEY, auth Bearer ; utiliser l'endpoint
  image ; générer une photo par marque et la poser en fond des slides à ~50 %).
- Étape 4 : brique « publication Metricool » (token dans METRICOOL_TOKEN ;
  userId = 3122469 ; blogId Le Sous Loueur = 3968518, Guestlucky = 4001072 ;
  programmer le carrousel pour VENDREDI 18h sur les 2 comptes Instagram).
- Étape 5 : déclencheur automatique TOUS LES LUNDIS + filet de sécurité (contrôle
  qualité auto + journal des publications + kill switch).

À partir de la MÊME vidéo, produire DEUX carrousels ADAPTÉS : un Guestlucky (angle
« ce qu'on vend »), un Le Sous Loueur (angle coaching). Jamais les mêmes slides.

RÈGLES NON NÉGOCIABLES :
- Repo PUBLIC : AUCUNE clé / AUCUN secret dans le code. Les secrets viennent UNIQUEMENT
  des variables d'environnement (SEEDANCE_API_KEY, METRICOOL_TOKEN).
- Commit + push réguliers sur `claude/salut-af8y9u`. Mets à jour `carroussel.md` à
  chaque étape (discipline mémoire, décrite dans le fichier).
- Publier en public est difficile à annuler : au début, programmer en BROUILLON /
  faire valider, avant de laisser publier tout seul.
- Avance UNE brique à la fois : code, teste, montre-moi le résultat, puis on continue.

COMMENCE PAR : lire `carroussel.md`, tester le réseau (3 curl ci-dessus), puis me
proposer ton plan pour l'Étape 2 (YouTube). NE code pas encore : dis-moi d'abord ton
plan, et on valide ensemble.
