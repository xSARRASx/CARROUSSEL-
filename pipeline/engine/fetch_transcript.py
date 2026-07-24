#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_transcript.py -- Etape 2 du robot carrousels.

Role : trouver TOUT SEUL la derniere video de la chaine YouTube, puis
recuperer sa transcription (le texte parle), et la ranger dans un fichier.

C'est la matiere premiere des 2 carrousels (Guestlucky + Le Sous Loueur).

Usage (a la main, pour tester) :
    python3 pipeline/engine/fetch_transcript.py

Aucune cle API n'est necessaire pour cette etape (flux public YouTube).
On avance en 3 morceaux :
  - Morceau 1 : trouver la derniere video           -> get_channel_id + get_latest_video
  - Morceau 2 : recuperer la transcription           -> (a venir)
  - Morceau 3 : ranger dans un fichier               -> (a venir)
"""

import re
import sys
import urllib.request

# Chaine YouTube source (la video du dimanche de Sebastien More).
CHANNEL_HANDLE = "moresebastien"
CHANNEL_URL = "https://www.youtube.com/@" + CHANNEL_HANDLE
RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

# On se fait passer pour un navigateur : YouTube renvoie une page vide sinon.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


def _http_get(url):
    """Petit telechargeur : renvoie le texte d'une page web."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


# --------------------------------------------------------------------------
# MORCEAU 1 : trouver la derniere video
# --------------------------------------------------------------------------

def get_channel_id(handle=CHANNEL_HANDLE):
    """A partir du @handle, retrouve l'identifiant technique de la chaine
    (ex: UCmimfmRMV0KYTjPeH2qw5wg). On en a besoin pour lire le flux RSS."""
    html = _http_get("https://www.youtube.com/@" + handle)
    match = re.search(r'"externalId":"(UC[0-9A-Za-z_-]+)"', html)
    if not match:
        match = re.search(r'/channel/(UC[0-9A-Za-z_-]+)', html)
    if not match:
        raise RuntimeError(
            "Impossible de trouver le channel_id de @" + handle +
            " (page YouTube changee ou acces bloque)."
        )
    return match.group(1)


def get_latest_video(channel_id):
    """Lit le flux public des dernieres videos de la chaine et renvoie la
    plus recente sous forme de dictionnaire (id, titre, date, url)."""
    xml = _http_get(RSS_URL.format(channel_id=channel_id))
    entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    if not entries:
        raise RuntimeError("Flux RSS vide : aucune video trouvee.")

    videos = []
    for entry in entries:
        vid = re.search(r"<yt:videoId>(.*?)</yt:videoId>", entry)
        title = re.search(r"<title>(.*?)</title>", entry)
        pub = re.search(r"<published>(.*?)</published>", entry)
        if not vid:
            continue
        videos.append({
            "id": vid.group(1),
            "title": _unescape(title.group(1)) if title else "",
            "published": pub.group(1) if pub else "",
            "url": "https://www.youtube.com/watch?v=" + vid.group(1),
        })

    # Le flux est deja trie du plus recent au plus ancien : on prend le 1er.
    return videos[0]


def _unescape(text):
    """Remet les caracteres speciaux du XML en clair (&amp; -> &, etc.)."""
    return (
        text.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
    )


# --------------------------------------------------------------------------
# Point d'entree : pour tester a la main
# --------------------------------------------------------------------------

def main():
    print("Etape 2 -- recuperation de la derniere video YouTube")
    print("Chaine :", CHANNEL_URL)
    print()

    print("[1/3] Recherche de l'identifiant de la chaine...")
    channel_id = get_channel_id()
    print("      channel_id =", channel_id)
    print()

    print("[2/3] Lecture du flux des dernieres videos...")
    video = get_latest_video(channel_id)
    print("      Derniere video trouvee :")
    print("      - Titre :", video["title"])
    print("      - Date  :", video["published"])
    print("      - Lien  :", video["url"])
    print()

    print("[3/3] Transcription : (Morceau 2, a venir)")


if __name__ == "__main__":
    sys.exit(main())
