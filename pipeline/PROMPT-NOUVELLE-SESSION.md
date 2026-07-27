# Prompt de démarrage — nouvelle session Robot Carrousels

> À COLLER dans une NOUVELLE conversation Claude Code lancée sur :
> - Environnement : **CARROUSSEL AUTO** (réseau ouvert)
> - Dépôt : **CARROUSSEL-**
> - Branche : **claude/carrousel-instagram-robot-hk4743**
>
> Utile quand une variable d'environnement vient d'être ajoutée (elle n'est
> visible que dans les sessions démarrées APRÈS), ou pour reprendre le projet.

---

Salut Claude. Projet en cours, parle-moi en français, vocabulaire simple, par
micro-étapes (je débute en code). Je m'appelle Martin.

AVANT TOUTE ACTION : lis `carroussel.md` à la racine du dépôt CARROUSSEL- EN
ENTIER. C'est la mémoire complète du projet : les 3 marques, les chartes, le
design V2, les 10 règles non négociables et les pièges techniques déjà payés.
Commence par la section « À LIRE EN PREMIER » tout en haut. Lis aussi
`pipeline/engine/design_v2.py` et `pipeline/engine/gemini_bg.py`.

CONTEXTE : on a un robot qui, chaque lundi, fabrique tout seul DEUX carrousels
Instagram (Guestlucky + Le Sous Loueur) à partir de la vidéo YouTube du dimanche
de https://www.youtube.com/@moresebastien. Tout est automatique sauf la
programmation finale dans Metricool, que je fais à la main.

CE QUE JE VEUX MAINTENANT :

1. Vérifie que la variable `GEMINI_API_KEY` est bien visible dans cette session
   (sans l'afficher en clair). Si elle est absente, dis-le et arrête-toi là.

2. Fais UNE seule génération de test pour valider la chaîne (coût ~0,13 $) :
   `python3 pipeline/engine/gemini_bg.py --brand lesousloueur --theme "a court ruling on short-term rental compliance" --out test_gemini.jpg --go`
   Montre-moi l'image et dis-moi franchement si la qualité vaut celle de
   Nano Banana Pro sur le site Seedance. Une seule image, pas plus.

3. Si ça marche : commit + push sur `claude/carrousel-instagram-robot-hk4743`,
   note le résultat dans `carroussel.md` (section fonds automatiques).

4. Ensuite, RECRÉE le rendez-vous automatique du lundi DANS CETTE SESSION, avec
   l'outil `create_trigger` (serveur MCP Claude Code Remote) :
   - name : "Robot carrousels — package du lundi"
   - cron_expression : `0 6 * * 1` (6h UTC = 8h Paris en été)
   - mode par défaut (la Routine se déclenche dans CETTE conversation)
   - prompt : reprends mot pour mot le prompt hebdomadaire décrit dans
     `carroussel.md` (transcription → 2 carrousels design V2 → génération des
     2 fonds via gemini_bg → rendu et contrôles → 2 descriptions → livraison :
     les 10 slides de chaque marque affichées en `display:"render"` PUIS les
     ZIP en `display:"attach"`, plus une ligne indiquant quelle image de fond a
     été générée et utilisée → commit/push + mise à jour de la mémoire).
   - garde-fous : ne rien produire si la vidéo est la même que la semaine passée ;
     kill switch si j'écris STOP dans la conversation.

5. Dis-moi ensuite d'aller SUPPRIMER l'ancienne Routine dans l'autre
   conversation (elle s'appelle pareil, id `trig_01BJ9PpUqznmkYP7XwEfUyG3`),
   pour ne pas recevoir le package en double. Ou supprime-la toi-même si tu la
   vois dans `list_triggers`.

RÈGLES : repo PUBLIC, aucun secret dans le code (uniquement des variables
d'environnement). Commits réguliers. Mets à jour `carroussel.md` à chaque étape.
Si quelque chose bloque, dis-le franchement au lieu de contourner.
