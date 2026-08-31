#!/usr/bin/env bash
# ============================================================================
# PREPARER L'ACCES YOUTUBE — a lancer AU DEBUT DE CHAQUE REVEIL DU ROBOT.
#
#     bash stories/engine/setup_youtube.sh
#
# Recette validee avec Martin (24 et 27/08/2026). Le conteneur repart de zero
# a chaque session : sans cette preparation, yt-dlp echoue sur
# « Sign in to confirm you're not a bot » MEME QUAND LE RESEAU VA BIEN.
#
# LA VRAIE CAUSE, dans neuf cas sur dix, est LOCALE : yt-dlp ne trouve aucun
# moteur JavaScript et ne le dit que dans un WARNING discret. Node existe dans
# le conteneur, mais celui du PATH est en 20.x -- yt-dlp le refuse en silence
# (« unsupported »). Il faut mettre /opt/node22 devant.
# ============================================================================
set -u
export PATH=/opt/node22/bin:$PATH

echo "1/4  node"
echo "     $(command -v node) -> $(node --version)"

echo "2/4  yt-dlp + fournisseur de jetons PO"
pip install --quiet -U yt-dlp bgutil-ytdlp-pot-provider 2>&1 | grep -vi warning | tail -1
echo "     yt-dlp $(yt-dlp --version)"
# ⚠️ curl_cffi est RETIRE volontairement : voir la note en bas.
pip uninstall -y curl_cffi >/dev/null 2>&1 && echo "     curl_cffi retire (il casse le telechargement ici)"

echo "3/4  serveur de jetons PO"
if [ ! -d /root/bgutil-ytdlp-pot-provider/server/build ]; then
    rm -rf /root/bgutil-ytdlp-pot-provider
    git clone --depth 1 https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git \
        /root/bgutil-ytdlp-pot-provider >/dev/null 2>&1
    ( cd /root/bgutil-ytdlp-pot-provider/server && npm install >/dev/null 2>&1 && npx tsc >/dev/null 2>&1 )
fi
[ -f /root/bgutil-ytdlp-pot-provider/server/build/main.js ] \
    && echo "     construit" || echo "     ECHEC de construction"
# ⚠️ LE CONSTRUIRE NE SUFFIT PAS, IL FAUT LE DEMARRER (trouve le 31/08/2026).
# Sans le serveur lance, yt-dlp echoue sur « Unable to fetch GVS PO Token:
# Missing required Visitor Data ». Une fois lance, ce message disparait.
if ! curl -sS --noproxy '*' --max-time 3 http://127.0.0.1:4416/ping >/dev/null 2>&1; then
    ( cd /root/bgutil-ytdlp-pot-provider/server && nohup node build/main.js >/tmp/bgutil.log 2>&1 & )
    sleep 6
fi
curl -sS --noproxy '*' --max-time 3 http://127.0.0.1:4416/ping >/dev/null 2>&1 \
    && echo "     serveur de jetons DEMARRE (port 4416)" \
    || echo "     serveur de jetons NON demarre -- voir /tmp/bgutil.log"

echo "4/4  configuration permanente"
mkdir -p /root/.config/yt-dlp
printf -- '--js-runtimes node:/opt/node22/bin/node\n' > /root/.config/yt-dlp/config
yt-dlp -v --skip-download --print "%(id)s" "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 2>&1 \
    | grep -i "JS runtimes" | head -1

cat <<'NOTE'

--- LA COMMANDE QUI PASSE -------------------------------------------------
yt-dlp --js-runtimes "node:/opt/node22/bin/node" \
  --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 \
  -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<ID>"

Elle produit <ID>.fr-orig.json3 : la VO francaise, a PRIVILEGIER sur <ID>.fr.
Parsing : concatener les segs[].utf8 de chaque events[], joindre par un espace.
Plus besoin de forcer player_client : avec le moteur JS, c'est inutile.

--- CE QUI NE SERT A RIEN, NE PAS Y PASSER DE TEMPS ------------------------
--impersonate / curl_cffi : le proxy sortant du conteneur re-termine le TLS,
la signature navigateur est reecrite avant d'atteindre YouTube. Pire, le
telechargement casse avec « curl: (35) Recv failure: Connection reset by
peer ». C'est pour ca que le script DESINSTALLE curl_cffi.

Empiler les player_client (ios, mweb, tv, web_safari...) : sans moteur JS
aucun ne passe, et avec le moteur ce n'est plus necessaire.

--- SI CA ECHOUE QUAND MEME -----------------------------------------------
TEST DE CONTROLE : relancer une video DEJA telechargee avec succes.
    - elle passe    -> le probleme vient de la video (pas de sous-titres ?)
    - elle echoue   -> c'est un vrai quota sur l'IP du serveur.
Dans ce cas : DEUX OU TROIS TENTATIVES MAXIMUM, puis attendre quelques heures.
Ne rien fabriquer, et demander la transcription a Martin -- canal le plus
fiable, il l'a fournie quatre fois en aout.

Pendant le blocage, ces deux-la repondent encore :
    yt-dlp --flat-playlist ...                      (lister les videos)
    curl "https://www.youtube.com/oembed?url=<URL>&format=json"
L'oEmbed donne le VRAI TITRE FRANCAIS, ce que le listing ne fait pas toujours.

--- LE CORRECTIF DEFINITIF ------------------------------------------------
Passer des cookies YouTube, via une VARIABLE D'ENVIRONNEMENT -- jamais dans le
repo, jamais dans le chat -- puis ajouter a la commande :
    --cookies /tmp/yt-cookies.txt
NOTE
