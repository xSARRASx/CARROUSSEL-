# 📅 La trame de la semaine — stories @moresebastien

> Écrite le 6 août 2026, après l'échange vocal entre **Pierre** et **Martin**.
>
> ⚠️ Précision de Martin : quand Pierre dit « est-ce que tu aurais moyen de
> gérer aussi **les postés** », il parle du fait de **POSTER les stories**, pas
> des publications au feed. Sa demande : Martin reprend la publication, pour
> que Pierre n'ait plus rien à faire. Ses mots : *« mon but, c'est de plus m'en
> occuper »*.

---

## Qui fait quoi

| | Avant | Maintenant |
|---|---|---|
| Créer les stories | Claude | Claude |
| **Poster les stories** | **Pierre, tous les jours** | **Martin, une fois par semaine** |
| Les témoignages | Pierre, quand il y pense | Pierre, sur 2 créneaux fixes |

---

## Comment on poste sans y passer ses journées

Instagram permet de **programmer les stories à l'avance** depuis Meta Business
Suite (application ou ordinateur). C'est la clé pour tenir le rythme sans y
toucher tous les jours :

**Une seule session par semaine (30 à 45 min), le dimanche soir ou le lundi
matin** : on ouvre le pack de la semaine, on programme les stories jour par
jour, et c'est fini jusqu'à la semaine suivante.

⚠️ **Deux exceptions à poster à la main** : les stories **quiz** et
**sondages**. Le sticker de sondage Instagram ne peut pas être ajouté à une
story programmée, il faut le poser au moment de publier. Ces jours-là, ça
prend deux minutes sur le téléphone.

⚠️ **Ce que Claude ne peut PAS faire** : publier directement sur le compte
Instagram. Il n'a pas accès au compte, et l'API Instagram ne permet pas de
publier des stories avec stickers. Il livre donc les stories **prêtes,
numérotées dans l'ordre de publication** — il ne reste qu'à programmer.

---

## Le rythme, jour par jour

| Jour | Thème des stories | Nombre | CTA |
|---|---|---|---|
| **Lundi** | Aide gratuite tirée de la vidéo du dimanche | 4 à 6 | Aucun (on donne) |
| **Mardi** | Conseil terrain + le cadeau de la semaine | 3 à 4 | Mot-clé tournant |
| **Mercredi** | Coulisses + annonce de la vidéo de 18h · **🟨 témoignages Pierre** | 3 à 5 | **GO** |
| **Jeudi** | Aide gratuite tirée de la vidéo du mercredi | 4 à 6 | Aucun (on donne) |
| **Vendredi** | Le cadeau de la semaine | 3 à 4 | **SIMULATEUR** |
| **Samedi** | Quiz ou sondage (à poster à la main) | 3 à 5 | Aucun, on fait voter |
| **Dimanche** | Teaser + sortie de la vidéo à 18h · **🟨 témoignages Pierre** | 3 à 4 | **GO** |

**Total : 25 à 35 stories par semaine.** Jamais plus de 7 par jour. La première
story de la journée doit accrocher : c'est elle qui décide si les gens
regardent la suite.

**Deux jours sans aucun CTA** (lundi et jeudi) : ce sont les jours où on donne
sans rien demander. C'est ce qui rend les jours à CTA crédibles.

---

## Les deux créneaux de Pierre

Pierre garde **mercredi et dimanche** — les deux jours de sortie vidéo, donc
les jours où l'audience est la plus active. Il y poste :

1. **Son témoignage** (screenshot réel : message WhatsApp, annonce d'élève,
   résultat chiffré) ;
2. **Juste derrière, la story CTA** : « Réponds **GO** à cette story pour qu'on
   échange ensemble sur ton projet ».

### Son pack lui est PRÉPARÉ et ENVOYÉ
On ne se contente pas de lui dire que les gabarits existent : on lui envoie
son pack tout prêt. **10 modèles de témoignage + 3 stories « Réponds GO »**
dans `output/temoignages-pierre/jpg/`, avec son mode d'emploi
(`stories/pack-pierre.md`).

Dix modèles, parce qu'à deux par semaine, trois se répéteraient au bout de dix
jours. Là, il tourne plus d'un mois sans jamais reposter la même mise en page.

Chaque modèle a une **zone en pointillés** où il colle son screenshot réel
(sticker photo Instagram) : un message WhatsApp, une annonce d'élève, un
résultat chiffré, un premier contrat, un calendrier qui se remplit...

### La règle demandée
> *« Parfois tu mettais plusieurs témoignages d'une seule personne à la
> suite. »*

**Un seul témoignage par personne à la suite.** On alterne les profils : ça
donne l'image d'un flux continu d'élèves qui réussissent, pas d'un seul client
très bavard.

---

## Les mots-clés

| Mot-clé | Quand | Ce qui se passe en DM |
|---|---|---|
| **GO** | Mercredi et dimanche, derrière les témoignages | La closeuse qualifie puis propose l'appel |
| **SIMULATEUR** | Vendredi | Envoi du simulateur + questions de qualification |
| Mot-clé tournant | Mardi | Ressource de la semaine (banque partagée avec LinkedIn) |

⚠️ Un mot-clé n'est posté que si **sa ressource est réellement prête**.

---

## Le pack hebdomadaire livré par Claude

Chaque semaine, Claude livre un zip **rangé dans l'ordre de publication**, avec
des noms qui parlent tout seuls :

```
lundi-1.jpg, lundi-2.jpg, lundi-3.jpg...
mardi-1.jpg, mardi-2.jpg...
```

Plus un petit mémo qui dit, pour chaque jour : quelles stories, quel sticker
poser, quel CTA. Celui qui programme n'a plus à réfléchir, il suit la liste.

---

## Ce qui tourne déjà tout seul

Deux réveils automatiques produisent les stories sans que personne ait à le
demander (section « 🤖 ROBOT STORIES » de `stories.md`) :
- **lundi 8h** : stories tirées de la vidéo du dimanche ;
- **jeudi 8h** : stories tirées de la vidéo du mercredi, s'il y en a une.

Stock disponible au 6 août 2026 : **104 stories prêtes à poster** dans
`stories/output/` (banque-01 : 48, banque-02 : 17, interactifs-01 : 14,
interactifs-02 : 10, semaine-01 : 15). De quoi tenir environ **4 semaines**
même si aucune vidéo ne sortait.
