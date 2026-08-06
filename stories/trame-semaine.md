# 📅 La trame de la semaine — @moresebastien

> Écrite le 6 août 2026, après l'échange vocal entre **Pierre** et **Martin**.
> Objectif de Pierre, dit mot pour mot : *« mon but, c'est de plus m'en
> occuper »*. Donc **Martin produit et poste tout**, et Pierre garde
> **deux créneaux par semaine** pour ses témoignages.

---

## Qui fait quoi

| | Martin (avec Claude) | Pierre |
|---|---|---|
| **Stories** | Tous les jours, toute la semaine | 2 créneaux témoignages |
| **Posts (feed)** | 3 carrousels par semaine | — |
| **Témoignages** | Fournit les gabarits vides | Colle les vrais screenshots |

---

## Le rythme, jour par jour

| Jour | Stories | Post feed | CTA |
|---|---|---|---|
| **Lundi** | Recyclage de la vidéo du dimanche + sondage diagnostic | 🟦 Carrousel | Sondage |
| **Mardi** | Conseil terrain + le cadeau de la semaine | — | Mot-clé tournant |
| **Mercredi** | Coulisses + annonce de la vidéo de 18h · **🟨 créneau témoignages Pierre** | 🟦 Carrousel | **GO** |
| **Jeudi** | Recyclage de la vidéo du mercredi (aide gratuite) | — | Lien vidéo |
| **Vendredi** | Le cadeau de la semaine | 🟦 Carrousel | **SIMULATEUR** |
| **Samedi** | « Tu en es où ? » + boîte à questions | — | Boîte à questions |
| **Dimanche** | Teaser + sortie de la vidéo à 18h · **🟨 créneau témoignages Pierre** | — | **GO** |

**Volume stories** : 3 à 5 par jour, jamais plus de 7. La première story de la
journée doit accrocher : c'est elle qui décide si les gens regardent la suite.

**Pourquoi mercredi et dimanche pour les témoignages** : ce sont les deux jours
de sortie vidéo (18h), donc les jours où l'audience est la plus active. Un
témoignage suivi d'un « réponds GO » y convertit mieux. Ces deux jours restent
modifiables si Pierre préfère d'autres créneaux.

---

## Les deux créneaux de Pierre

Ce que Pierre poste lui-même, sur ses 2 créneaux :

1. **Le témoignage** (son screenshot réel : message WhatsApp, annonce d'élève,
   résultat chiffré).
2. **Juste derrière, la story CTA** : « Réponds **GO** à cette story pour qu'on
   échange ensemble sur ton projet ».

### Les gabarits sont déjà prêts
Trois modèles avec une **zone en pointillés** où Pierre colle son screenshot
(sticker photo Instagram), déjà produits dans `output/interactifs-01/jpg/` :
- `temoin_01` — « + 1 pour [Prénom] »
- `temoin_02` — « La dernière annonce de nos élèves »
- `temoin_03` — « Ce qu'on a reçu de [Prénom] »

### La règle que Martin a demandée
> *« Parfois tu mettais plusieurs témoignages d'une seule personne à la
> suite. »*

**Un seul témoignage par personne à la suite.** On alterne les profils d'une
story à l'autre et d'une semaine à l'autre : ça donne l'image d'un flux
continu d'élèves qui réussissent, pas d'un seul client très bavard.

---

## Les mots-clés

| Mot-clé | Quand | Ce qui se passe en DM |
|---|---|---|
| **GO** | Mercredi et dimanche, derrière les témoignages | La closeuse qualifie puis propose l'appel |
| **SIMULATEUR** | Vendredi | Envoi du simulateur + questions de qualification |
| Mot-clé tournant | Mardi | Ressource de la semaine (banque partagée avec LinkedIn) |

⚠️ Un mot-clé n'est posté que si **sa ressource est réellement prête**.

---

## Les posts (feed) — la nouveauté

Pierre a demandé : *« est-ce que tu aurais moyen de gérer aussi les posts ? »*
Oui : le pipeline carrousels existe déjà dans ce repo
(`pipeline/engine/build_lesousloueur.py`, rendu via `pipeline/engine/render.py`).

**3 carrousels par semaine** : lundi, mercredi, vendredi. Même matière première
que les stories — les vidéos YouTube de Sébastien — mais découpée autrement :
la story donne envie, le carrousel démontre.

---

## Ce qui tourne déjà tout seul

Deux réveils automatiques produisent les stories sans que personne ait à le
demander (voir la section « 🤖 ROBOT STORIES » de `stories.md`) :
- **lundi 8h** : stories tirées de la vidéo du dimanche ;
- **jeudi 8h** : stories tirées de la vidéo du mercredi, s'il y en a une.

Le stock est déjà constitué : **104 stories prêtes à poster** dans
`stories/output/` au 6 août 2026 (banque-01 : 48, banque-02 : 17,
interactifs-01 : 14, interactifs-02 : 10, semaine-01 : 15). S'y ajoutent
21 planches du catalogue de thèmes et 5 stories V2, qui sont des archives de
recherche, pas du stock à poster.
