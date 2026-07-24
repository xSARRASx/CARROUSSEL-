# Maxi prompt — Robot BLOG du lundi (à coller dans la discussion blog)

> ⚠️ À COLLER UNE SEULE FOIS dans la discussion Claude Code qui écrit déjà les
> articles de blog (celle qui connaît le processus habituel).
> Conditions : ce doit être une session Claude Code (avec terminal), sur un
> environnement dont l'« Accès réseau » est **Complet** (sinon YouTube est bloqué).

---

Salut Claude. Mission : AUTOMATISER ce qu'on fait déjà ensemble dans cette
conversation. Chaque semaine, une vidéo sort le dimanche sur la chaîne YouTube
https://www.youtube.com/@moresebastien. Je veux que TOUS LES LUNDIS à 8h (heure
de Paris), tu fasses TOUT SEUL, sans que je demande rien :

1. Récupérer la transcription de la DERNIÈRE vraie vidéo de la chaîne (les
   vidéos longues de l'onglet Vidéos, JAMAIS les shorts).
2. Écrire l'article de blog comme on fait d'habitude ici : mêmes règles, même
   format, même processus et même livraison que d'habitude dans cette
   conversation. Ne me pose aucune question, tranche toi-même.
3. Me livrer le résultat ici. Moi je passe dans la semaine le récupérer.

MISE EN PLACE : fais ça MAINTENANT, étape par étape, montre-moi chaque résultat.

A) Teste le réseau :
   curl -sS -m 15 -o /dev/null -w "%{http_code}\n" https://www.youtube.com
   Si le code n'est pas 200 : STOP. Dis-moi que l'environnement n'a pas le
   réseau ouvert. (Il faudra relancer cette discussion sur un environnement
   avec « Accès réseau = Complet ». Ne bricole pas de contournement.)

B) Installe la recette transcription (technique déjà validée sur un autre
   projet, recopie-la telle quelle) :
   - pip install yt-dlp
   - Dernière vraie vidéo (id + titre + durée), l'onglet /videos exclut les shorts :
     yt-dlp --flat-playlist --playlist-items 1 --print "%(id)s\t%(title)s\t%(duration)s" "https://www.youtube.com/@moresebastien/videos"
   - Sous-titres français de cette vidéo (fr-orig = piste originale, sinon fr) :
     yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "fr-orig,fr" --sub-format json3 -o "sub" "https://www.youtube.com/watch?v=<ID>"
   - Lire le fichier .json3 : pour chaque event, concaténer les segs[].utf8 ;
     joindre les events avec UN ESPACE (sinon les mots se collent) ; nettoyer
     les espaces multiples. Résultat = la transcription propre.
   - Range la transcription dans un fichier du projet (avec titre, date, lien),
     et garde une trace de l'ID de la vidéo traitée pour ne JAMAIS refaire deux
     fois la même.
   - TESTE la recette maintenant et montre-moi le titre + les 300 premiers
     caractères de la transcription.

C) Crée le déclencheur automatique : utilise l'outil create_trigger (serveur
   MCP « Claude Code Remote ») pour créer une Routine :
   - name : "Robot blog — article du lundi"
   - cron_expression : "0 6 * * 1"  (6h UTC = 8h Paris en été)
   - mode par défaut (la Routine se déclenche dans CETTE conversation)
   - prompt de la Routine : lui dire de faire les étapes 1 → 3 tout seul, avec
     ces garde-fous :
     * Si pas de nouvelle vidéo depuis la dernière fois (même ID que la trace) :
       laisser un petit message pour prévenir, et s'arrêter là.
     * Si Martin a écrit STOP dans la conversation depuis la dernière fois :
       ne rien produire et confirmer l'arrêt.
     * Livrer comme d'habitude, puis sauvegarder le travail (commit + push si
       cette discussion travaille dans un repo).
   Si l'outil create_trigger n'existe pas dans ta session : dis-le-moi
   clairement au lieu d'improviser autre chose.

D) Récap final : montre-moi ce qui est en place (nom de la Routine, prochaine
   exécution) et rappelle-moi le bouton STOP (écrire STOP dans la conversation).

RÈGLES NON NÉGOCIABLES : aucun secret / aucune clé dans le code si le repo est
public ; avance étape par étape en me montrant les résultats ; si quelque chose
bloque, dis-le franchement au lieu de contourner.
