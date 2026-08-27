# Relais de transcription — instruction à donner au Claude du Mac (une seule fois)

## À quoi ça sert
Le robot carrousels tourne sur un serveur derrière un proxy d'entreprise. Quelques
jours par mois, YouTube met cette adresse IP sous quota et refuse toute
transcription. Le Mac de Martin, lui, sort par une connexion normale : il n'est
jamais bloqué. Ce relais permet au Mac de débloquer le robot sans que Martin ait
quoi que ce soit à copier-coller.

## Ce que Martin a à faire
**Une seule chose, une seule fois** : coller le bloc ci-dessous dans les
instructions de son Claude du Mac (celui qui récupère déjà `livraison/` et
programme dans Metricool). Ensuite, plus rien, jamais.

---

## BLOC À COLLER DANS LE CLAUDE DU MAC

> **Relais de transcription YouTube (à faire à chaque fois que tu récupères le dépôt)**
>
> Après ton `git pull` habituel, regarde si le fichier
> `pipeline/output/transcripts/A_RECUPERER.json` existe.
>
> - **S'il n'existe pas** : rien à faire, continue ton travail normal.
> - **S'il existe** : le robot du cloud est bloqué par YouTube et te demande de
>   l'aider. Le fichier contient l'identifiant et le titre de la vidéo.
>
> Dans ce cas :
> 1. Récupère la transcription française de cette vidéo depuis le Mac :
>    ```
>    yt-dlp --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 \
>      -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<IDENTIFIANT>"
>    ```
>    Tu obtiens `<IDENTIFIANT>.fr-orig.json3`. Le texte s'obtient en concaténant
>    les `segs[].utf8` de chaque entrée de `events[]`, joints par un espace.
>    Enregistre ce texte dans un fichier, par exemple `/tmp/transcription.txt`.
> 2. Dépose-la dans le dépôt :
>    ```
>    python3 pipeline/engine/depot_transcript.py \
>      --video <IDENTIFIANT> --titre "<TITRE FRANÇAIS>" --fichier /tmp/transcription.txt
>    ```
>    Le script vérifie le format et efface la demande une fois honorée.
> 3. `git add -A`, commit, et push sur la branche
>    `claude/carrousel-instagram-robot-hk4743`.
>
> C'est tout. Au réveil suivant, le robot du cloud trouvera la transcription,
> ne rappellera pas YouTube, et produira les deux carrousels tout seul.
>
> Ne préviens pas Martin pour ça : c'est une opération de routine.

---

## Ce que ça change concrètement
| Situation | Avant | Maintenant |
|---|---|---|
| YouTube répond normalement | le robot travaille seul | inchangé, le robot travaille seul |
| IP sous quota | le robot était bloqué, Martin devait coller la transcription à la main | le Mac dépose la transcription, le robot repart seul |

## Pour vérifier que c'est en place
La prochaine fois que le robot sera bloqué, un fichier `A_RECUPERER.json`
apparaîtra dans `pipeline/output/transcripts/` sur GitHub. S'il disparaît tout
seul dans les heures qui suivent, remplacé par un fichier de transcription,
c'est que le relais fonctionne.
