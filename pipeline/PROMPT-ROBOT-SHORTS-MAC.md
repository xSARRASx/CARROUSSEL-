# Maxi prompt — Robot SHORTS du lundi (à coller dans le Claude Code du TERMINAL DU MAC)

> ⚠️ À COLLER UNE SEULE FOIS dans la session Claude Code du terminal de ton Mac,
> celle qui fait DÉJÀ le montage des shorts (elle connaît tes règles de montage
> et le dossier où ranger les shorts).
> Condition : le Mac doit être ALLUMÉ (ou en veille, branché) le lundi à 8h.
> S'il dort, le montage part à son réveil. S'il est éteint, ça saute la semaine.

---

Salut Claude. Mission : AUTOMATISER ce qu'on fait déjà ensemble ici. Chaque
dimanche, une vidéo sort sur la chaîne YouTube
https://www.youtube.com/@moresebastien. Je veux que TOUS LES LUNDIS à 8h
(heure locale du Mac), le montage des shorts se fasse TOUT SEUL, sans moi :

1. Télécharger la DERNIÈRE vraie vidéo de la chaîne (l'onglet /videos, jamais
   les shorts existants) en bonne qualité (1080p).
2. Faire le montage des shorts EXACTEMENT comme on fait d'habitude ici :
   mêmes règles, mêmes formats, même nombre de shorts, mêmes sous-titres, etc.
3. Ranger les shorts dans le dossier habituel sur cet ordinateur.
4. Me laisser un petit résumé écrit (fichier journal) de ce qui a été produit.

MISE EN PLACE : fais ça MAINTENANT, étape par étape, montre-moi chaque résultat.

A) Vérifie les outils :
   - yt-dlp installé ? (sinon : brew install yt-dlp  ou  pip3 install yt-dlp)
   - Teste : yt-dlp --flat-playlist --playlist-items 1 --print "%(id)s | %(title)s" "https://www.youtube.com/@moresebastien/videos"
   - Puis teste un vrai téléchargement rapide (360p) pour confirmer que ça passe :
     yt-dlp -f 18 -o /tmp/test_robot.mp4 "https://www.youtube.com/watch?v=<ID>"
     (supprime le fichier après le test)

B) Écris le PROMPT HEBDOMADAIRE dans un fichier du projet (ex :
   robot-shorts-prompt.txt) : il doit te dire de faire les étapes 1 → 4
   tout seul, avec ces garde-fous :
   - Garder la trace de l'ID de la dernière vidéo traitée (petit fichier) :
     si c'est la même que la semaine passée, ne rien refaire et juste le noter
     dans le journal.
   - Si un fichier nommé STOP existe à la racine du projet : ne rien faire.
     (C'est mon bouton d'arrêt : je crée ce fichier = robot en pause.)
   - Écrire un résumé dans un fichier journal (ex : robot-shorts-journal.txt) :
     date, vidéo traitée, shorts produits, problèmes éventuels.

C) Crée le RÉVEIL AUTOMATIQUE du Mac (launchd) :
   - Crée un petit script shell (ex : robot-shorts.sh) qui va dans le dossier
     du projet et lance :  claude -p "$(cat robot-shorts-prompt.txt)"
     avec les permissions nécessaires pour travailler sans poser de questions
     (explique-moi ce que tu actives et pourquoi).
   - Crée le fichier ~/Library/LaunchAgents/com.martin.robot-shorts.plist
     avec StartCalendarInterval : Weekday 1 (lundi), Hour 8, Minute 0,
     qui lance ce script, avec un fichier de log pour la sortie.
   - Charge-le : launchctl load ~/Library/LaunchAgents/com.martin.robot-shorts.plist
   - Vérifie qu'il est bien chargé : launchctl list | grep robot-shorts

D) TESTE une fois en vrai, tout de suite : lance le script à la main
   (./robot-shorts.sh ou launchctl start com.martin.robot-shorts) et vérifie
   que tout se déroule de bout en bout (téléchargement → montage → dossier →
   journal). Montre-moi le journal à la fin.

E) Récap final : rappelle-moi
   - l'heure du rendez-vous (lundi 8h, heure du Mac),
   - la condition (Mac allumé ou en veille branché),
   - le bouton STOP (créer un fichier STOP à la racine du projet),
   - où je trouve les shorts et le journal chaque semaine.

RÈGLES : avance étape par étape en me montrant les résultats ; si un outil
manque ou si quelque chose bloque, dis-le franchement au lieu de contourner ;
ne touche à rien d'autre sur l'ordinateur que le dossier du projet et le
fichier launchd ci-dessus.
