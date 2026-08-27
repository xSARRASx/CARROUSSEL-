#!/usr/bin/env bash
# ============================================================================
# PREPARER L'ACCES YOUTUBE — a lancer AU DEBUT DE CHAQUE REVEIL DU ROBOT.
#
# Le conteneur repart de zero a chaque session : yt-dlp y est en version
# ancienne et sans moteur JavaScript. Or YouTube pose desormais un defi
# JavaScript, et yt-dlp le dit noir sur blanc :
#   « YouTube extraction without a JS runtime has been deprecated »
# Sans moteur, l'extraction tombe direct sur « Sign in to confirm you're not
# a bot », meme quand l'acces reseau est bon.
#
# Ce script installe la bonne version et branche le moteur, une fois pour
# toutes dans la session :
#     bash stories/engine/setup_youtube.sh
#
# Ensuite, yt-dlp lit tout seul sa configuration : plus besoin de repeter
# l'option sur chaque commande.
# ============================================================================
set -u

echo "1/3  yt-dlp a jour"
pip install --quiet -U "yt-dlp[default,curl-cffi]" 2>&1 | grep -vi warning | tail -1
echo "     version : $(yt-dlp --version)"

echo "2/3  moteur JavaScript"
# ⚠️ PIEGE : `node` dans le PATH est une VIEILLE version (20.x) que yt-dlp
# refuse -- il affiche « node-20.x (unsupported) » et continue sans moteur.
# Il faut lui donner le chemin d'un node recent. On prend le plus eleve.
NODE=""
for v in 24 23 22; do
    [ -x "/opt/node$v/bin/node" ] && { NODE="/opt/node$v/bin/node"; break; }
done
if [ -z "$NODE" ]; then
    C=$(command -v node || true)
    if [ -n "$C" ] && [ "$("$C" -e 'console.log(process.versions.node.split(".")[0])')" -ge 22 ]; then
        NODE="$C"
    fi
fi
if [ -z "$NODE" ]; then
    echo "     AUCUN node >= 22 trouve. yt-dlp fonctionnera sans moteur JS,"
    echo "     donc mal. Chercher un autre moteur (deno, bun, quickjs)."
else
    echo "     $NODE ($($NODE --version))"
    mkdir -p /root/.config/yt-dlp
    printf -- '--js-runtimes node:%s\n' "$NODE" > /root/.config/yt-dlp/config
    echo "     ecrit dans /root/.config/yt-dlp/config"
fi

echo "3/3  verification"
yt-dlp -v --skip-download --print "%(id)s" \
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 2>&1 \
    | grep -iE "JS runtimes|Challenge Providers" | head -2

cat <<'NOTE'

--- CE QUI NE MARCHE PAS, INUTILE DE REESSAYER -----------------------------
IMPERSONATION (curl_cffi, --impersonate) : INCOMPATIBLE avec ce conteneur.
Le trafic passe par un proxy qui re-termine le TLS. Quand curl_cffi imite la
signature reseau d'un navigateur, le proxy coupe la connexion :
    curl: (35) Recv failure: Connection reset by peer
Et de toute facon YouTube verrait la signature du proxy, pas la notre.
Teste et ecarte le 27/08/2026. Ne pas y repasser du temps.

ERREUR 429 « Too Many Requests » : c'est une limite posee sur l'ADRESSE du
serveur, pas un probleme d'outil. Aucune option n'en vient a bout. Elle se
leve d'elle-meme apres quelques heures ou quelques jours. Quand elle est la,
seul `--flat-playlist` (lister les videos) continue de repondre.
--> Dans ce cas : demander la transcription a Martin. C'est le canal le plus
    fiable, il l'a fourni trois fois de suite et ca marche tres bien.
NOTE
