# carroussel.md — Mémoire du projet Carrousels Instagram

> Fichier mémoire relu au début de chaque session. Il regroupe TOUT le contexte,
> les règles et les specs pour créer et mettre en page les carrousels Instagram
> des marques de Sébastien More.
> Pour reprendre : "lis le carroussel.md et continuons".
>
> Repo : `xSARRASx/CARROUSSEL-` — branche de dev ACTUELLE :
> `claude/carrousel-instagram-robot-hk4743` (l'ancienne `claude/salut-af8y9u` n'est plus utilisée)

---

# 🚦 À LIRE EN PREMIER — état du projet au 27/07/2026

**Le robot tourne déjà.** Chaîne complète, testée, en production :

| Brique | Fichier | État |
|---|---|---|
| Transcription YouTube (vraies vidéos, pas les shorts) | `pipeline/engine/fetch_transcript.py` | ✅ |
| Mise en page V2 par SCHÉMAS (le style actuel) | `pipeline/engine/design_v2.py` | ✅ |
| Rendu PNG/JPEG + contrôles | `pipeline/engine/render.py` | ✅ |
| Fonds photo automatiques (Nano Banana Pro / Google) | `pipeline/engine/gemini_bg.py` | ✅ testé en vrai le 27/07 (0,134 $/image) |
| Déclencheurs **lundi 8h + jeudi 8h** | `trig_01GTc5qL9sFLY2ZZ5tkcCTNh` (dimanche) et `trig_01RsQkR98YD4J7LvMNMKq79S` (mercredi) | ✅ (jeudi ajouté 29/07) |
| Anti-doublon `fetch_transcript.py --verifier` | codes 0 / 1 / 2 | ✅ corrigé 29/07 |
| Publication Metricool par API | — | ⛔ en pause (forfait Starter, API non incluse) |

**Exemples à copier pour un nouveau carrousel** (design V2, la référence) :
`pipeline/engine/v2_lsl_conciergerie_220k.py` et `v2_gl_conformite_lemeur.py`.
Les anciens `build_guestlucky.py` / `build_lesousloueur.py` sont l'ANCIEN style (V1),
gardés pour référence : ne plus les utiliser pour de nouveaux carrousels.

## ⚠️ LES 14 RÈGLES DE MARTIN (non négociables, apprises au fil des sessions)
1. **TOUJOURS afficher le rendu de chaque slide** (SendUserFile `display:"render"`,
   10 JPEG par marque) AVANT/EN PLUS des ZIP. Jamais les ZIP seuls.
2. **Design V2 uniquement** : chaque slide de contenu est un SCHÉMA (stats, timeline,
   flow, mindmap, compare, checklist, layers, pincer) + une phrase d'intro `lead=`.
   Jamais de simples listes de texte.
3. **Aucun grand vide** dans une slide, et aucun bloc démesuré : hauteurs maîtrisées.
4. **Montants avec espaces insécables** (`220&nbsp;000&nbsp;€`) : jamais un « € » seul
   en bout de ligne.
5. **Descriptions Instagram** : CTA en haut avec `↓` et `😉`, signature Le Sous Loueur,
   et **PAS d'emoji clé 🔑 à la fin** (Martin l'a fait retirer).
6. **Vraies vidéos** de l'onglet `/videos`, **jamais les shorts**.
7. **Deux carrousels ADAPTÉS** depuis la même vidéo : jamais les mêmes slides.
8. **Zéro emoji et zéro tiret long dans les slides**, acronymes expliqués,
   mots bannis Guestlucky (beds24, mandat de gestion, garantie financière),
   aucun dénigrement frontal de concurrent.
9. **Martin ne fait PLUS RIEN à la main** (mis à jour le 27/07/2026). Il ne télécharge
   plus, ne programme plus. Le **Claude du Mac** récupère `livraison/` sur GitHub et
   programme lui-même dans Metricool (vendredi 18h). **Le travail de ce robot s'arrête
   au push GitHub.** Dans le message du lundi : dire ce qui a été livré, et ne JAMAIS
   dire à Martin de télécharger ou de programmer.
10. **Honnêteté** : si une brique échoue (clé, quota, réseau), le dire clairement et
    livrer avec le fond de secours. Jamais improviser ni prétendre avoir vérifié.
14. **VIDÉO HORS THÈME : TOUJOURS PRODUIRE LE SOUS LOUEUR** (décision de Martin
    le 03/08/2026). La chaîne évolue vers le business, le développement personnel
    et l'investissement : Sébastien l'annonce lui-même en fin de vidéo. Quand la
    vidéo ne parle pas de location courte durée :
    - **Le Sous Loueur → on produit TOUJOURS.** La marque parle à des
      entrepreneurs : argent, mental, organisation, tout cela lui va.
    - **Guestlucky → on saute quand le sujet ne s'y prête vraiment pas.** Ne
      jamais forcer un angle produit artificiel sur un outil de gestion locative.
      ⚠️ Chercher d'abord un pont HONNÊTE : le 03/08, « ne dis pas combien tu
      gagnes » est devenu « le cloisonnement des accès » (interface propriétaire,
      application prestataires). Ne sauter que si aucun pont réel n'existe.
    - Dans ce cas, le contrôle dira « SEMAINE INCOMPLETE » : c'est normal et
      voulu. Le dire clairement à Martin en première ligne, sans s'excuser.
    ⛔ Ne JAMAIS inventer une fonctionnalité Guestlucky pour faire tenir un angle.
       La banque d'infos produit de la section A2 fait foi.

13. **AUCUN APPEL À COMMENTER CÔTÉ GUESTLUCKY** (règle posée par Martin le
    30/07/2026). Les légendes ET les slides Guestlucky ne doivent JAMAIS dire
    « Commente MOT et je t'envoie… », ni promettre quoi que ce soit qui
    obligerait Martin à répondre ou à envoyer un fichier à la main après la
    publication. **Les 4 seules actions autorisées pour Guestlucky** :
    s'abonner au compte, enregistrer le post, le partager, visiter le site
    (guestlucky.com). Côté slides, utiliser `d.cta_sans_commentaire(...)` au
    lieu de `d.cta(...)` : la brique `cta()` affiche le mot COMMENTE en dur.
    ⚠️ **Le Sous Loueur ne change PAS** : le « Commente LEMEUR ↓ » reste, c'est
    le système de Sébastien, et lui répond à ses commentaires.
    Raison : tout ce qui promet un envoi crée du travail manuel pour Martin,
    or le projet vise le zéro action manuelle après publication.
12. **UN CONTRÔLE VÉRIFIE TOUJOURS LE RÉSULTAT FINAL, JAMAIS UNE ÉTAPE
    INTERMÉDIAIRE** (règle posée par Martin le 30/07/2026, après trois pannes
    silencieuses de suite). Ne jamais déduire « c'est fait » de la présence d'un
    fichier de travail : un run peut s'interrompre juste après. Une vidéo n'est
    traitée que si **ses carrousels sont livrés dans `livraison/` et poussés**.
    Corollaire : un registre ou un journal ne prouve rien tout seul, il sert
    seulement d'annuaire — le contrôle relit toujours les fichiers réels.
11. **JAMAIS DE GÉNÉRATION POUR RIEN** (règle confirmée par Martin le 27/07/2026).
    Toute image payante (`gemini_bg`, ~0,134 $) doit servir un carrousel réellement
    livré. **Interdits** : les répétitions générales, les tests « pour voir », les
    régénérations parce qu'une image plaît moyennement, les essais en double.
    - Une seule génération de validation a été autorisée, le 27/07/2026 : c'est fait,
      la chaîne est prouvée, on ne la refait pas.
    - Pour tester du code sans dépenser : `--dry-run` (affiche le prompt, 0 $), ou
      réutiliser une image déjà générée dans `pipeline/assets/backgrounds/`.
    - **La validation d'un changement se fait sur la première VRAIE exécution du
      lundi**, jamais sur un tir d'essai payant.
    - Si tu penses vraiment qu'une génération de test est nécessaire : demander à
      Martin AVANT, en annonçant le coût. Ne jamais décider seul.

## 🚫 PIÈGES TECHNIQUES DÉJÀ PAYÉS (ne pas refaire)
- **NE JAMAIS installer `curl_cffi`** : casse yt-dlp derrière le proxy.
- **NE PAS faire `playwright install`** : Chromium est déjà là
  (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`). Seul `pip install playwright` est utile.
- **Piloter un navigateur est IMPOSSIBLE ici** (réseau bloqué pour Chromium, prouvé).
- **L'API Seedance ne génère pas d'images** (401) : uniquement de la vidéo.
- **Sonder une API en envoyant une requête valide coûte de l'argent** : toujours
  `--dry-run` ou un corps volontairement invalide pour tester.

---

## 👤 Qui

- **Sébastien More** (@moresebastien sur Instagram et YouTube) — expert location
  courte durée : 11 ans de terrain, 8 ans d'accompagnement, 3 000+ élèves.
- **Martin** gère les comptes Instagram et pilote la création des carrousels.
- Communication **en français**, casual, souvent avec des typos (à corriger
  implicitement). Martin délègue beaucoup de décisions créatives.

## 🏠 Les 3 marques (TOUJOURS demander pour laquelle on travaille si pas évident)

### 1. LE SOUS LOUEUR (@moresebastien)
- Marque personnelle : coaching / formation sous-location et conciergerie Airbnb.
- Cible : conciergeries Airbnb, propriétaires LMNP, para-hôteliers, sous-locataires.
- Site : `www.lesousloueur.fr`
- Signature récurrente : « Ça fait 11 ans que je vis de la conciergerie et de la
  sous-location. Depuis 8 ans j'accompagne ceux qui veulent en faire leur
  activité. Plus de 3 000 élèves nous ont fait confiance et on est là au
  quotidien pour leur donner les solutions dont ils ont besoin. »
- Ton : expert, pédagogique, terrain, ludique.

### 2. GUESTLUCKY (@guestlucky.off)
- SaaS français pour conciergeries Airbnb : PMS + channel manager tout-en-un.
- Site : `guestlucky.com`
- Pas de signature personnelle, ton produit / marque.
- Fondé par Sébastien More (actif depuis 2014). Support 100% humain sur WhatsApp.

### 3. LEAPWAY (@leapwayoff)
- Plateforme de réservation nouvelle génération (concurrent Airbnb/Booking).
- Co-fondée avec Nathan. Site : `leapwayapp.com`. Instagram : @leapwayoff.
- ⚠️ **PAS un channel manager, PAS un outil de sync multi-plateformes** (ne
  JAMAIS le qualifier ainsi).
- Outils intégrés : IA, automatisation, conciergerie, facturation, conformité FR.
- Commission : 0% le 1er mois, puis 10% dégressif, option Pro à 4,99€/mois/logement.
- En cours de finalisation, liste d'attente active. CTA principal : mot-clé LANCEMENT.

## 🔒 Règle de cloisonnement (IMPORTANTE)
Chaque conversation de travail reste **uniquement** sur ce que Martin y dit. On
ne pioche PAS d'infos d'autres conversations / projets, sauf s'il pose
explicitement la question. Ce fichier `carroussel.md` est la SEULE mémoire
partagée de référence.

## 🗺️ Carte des prompts (2 réseaux carrousels × 2 métiers + 2 rôles transverses)

| Marque | Création contenu | Mise en page |
|---|---|---|
| **Guestlucky** | prompt dédié (PARTIE A2) | prompt dédié (PARTIE C2) |
| **Le Sous Loueur** | prompt dédié (PARTIE A1) | prompt dédié (PARTIE C2 → C1) |

Plus 2 rôles transverses :
- **Community manager** (descriptions Instagram/TikTok, hooks, CTA — 3 marques) → PARTIE B.
- **Prompts visuels IA** (Seedance / Magnific / Ideogram / Midjourney — 3 marques) → PARTIE D.

## ⭐ MODE DE TRAVAIL PRINCIPAL — Claude fait TOUT de bout en bout (décision Martin, 24/07/2026)
Martin veut que je gère **toute la chaîne moi-même**, en une seule conversation :
1. **Création du CONTENU** des slides (PARTIE A)
2. **La description** Instagram / hooks / CTA (PARTIE B)
3. **La mise en page** design → PNG (PARTIE C)
4. **La photo de fond** que j'utilise dans le carrousel : je l'écris et je la crée
   moi-même (règles PARTIE D), je ne la demande PLUS à Martin.
→ Je ne demande à Martin que **la marque** (si pas évidente) et son **feu vert / ses
   retouches**. Le reste, je le fais.

## 🧠 Les 4 métiers (composantes de la chaîne — chacun a ses règles et parfois ses palettes)
1. **Création de CONTENU** de carrousels (textes, structure, hiérarchie) → PARTIE A.
2. **Community manager** : descriptions Instagram/TikTok, hooks → PARTIE B.
3. **Mise en page** carrousels (design HTML/CSS → PNG via Playwright) → PARTIE C.
4. **Prompts visuels + photo de fond** (génération IA : fonds, stories, pubs) → PARTIE D.

⚠️ Les palettes de la **mise en page** (PARTIE C, couleurs du design HTML) et des
**prompts visuels** (PARTIE D, couleurs des rendus IA photo) NE SONT PAS identiques :
ne pas les mélanger. Toujours se référer à la partie concernée.

---

# PARTIE A — CRÉATION DE CONTENU DES CARROUSELS

## A0. Règles communes de contenu
- **Source** : Martin colle une transcription YouTube / live / texte, OU demande
  un sujet libre (rester dans l'univers de la marque concernée). Travailler
  UNIQUEMENT à partir de ce qui est donné. Ne rien inventer ; poser les questions
  AVANT de générer si un détail manque.
- **10 slides max** (pas obligatoire d'aller jusqu'à 10 ; viser 10 si le sujet
  est riche).
- **Sauts de ligne clairs** entre chaque élément de chaque slide (pas de blocs
  collés). Bien aéré pour que tout loge sur une slide.
- Textes centraux **plus gros et lisibles** (lecture mobile).
- **AUCUN emoji dans les slides** (règle absolue).
- **AUCUN em-dash / en-dash** (— ou –) : remplacer par deux-points, virgules ou
  points.
- Pas de titres putaclik ni trop basiques : on veut sentir l'expertise.
- Pas de mots creux ni de formules bateau.
- **Acronymes expliqués entre parenthèses à leur 1re apparition** (OTA, CTA, IA,
  PMS, LCD…).
- **Loi Hoguet** : toujours écrite correctement (jamais « loi au gay » des
  transcriptions vocales). Corriger implicitement les fautes de reconnaissance.
- **Ne jamais dénigrer un concurrent frontalement** : on peut dire « tel outil ne
  fait pas ça », pas « tel outil c'est nul ».
- Ton par type de sujet : **alerte journalistique** (réforme/actu), **pédagogique
  et démonstratif** (produit/feature), **conseil actionnable** (stratégie/croissance).
- Style « fait main par un community manager », pas généré par une IA.
- Retenir tout au fil de la conversation.

## A1. Le Sous Loueur — structure de contenu

**Process** :
1. Martin envoie la source (ou demande un sujet libre).
2. Proposer **2 à 3 options de titre de couverture** (angles différents).
3. Martin choisit (ou laisse choisir).
4. Créer le carrousel complet (sauts de ligne + consignes visuelles).
5. Itérer.

**Slide 1 — Couverture**
- Titre principal fort et informatif (blanc, gros).
- Sous-titre (orange).
- Texte bas (blanc, plus petit).
- Logo bas : « Le Sous Loueur - Sébastien More ». Flèche orange à droite.

**Slides 2 à 8 — Contenu**
- Numéro orange en haut.
- Titre (bleu clair, gros).
- Encadré blanc (sous-titre).
- Texte hiérarchisé par couleur, ~4 points par slide :
  → (orange) Mot-clé / label
  (blanc) Explication courte
- Encadré bas « à retenir » : (bleu + blanc) au format « Label : | Message ».
- Logo bas + flèche orange à droite.
- **Variante « deux blocs »** (quand 2 mini-sujets dans une slide) :
  - ENCADRÉ GAUCHE (bleu) : NOM DU BLOC 1 → TEXTE DROITE : (orange) label / (blanc) explication
  - ENCADRÉ GAUCHE (bleu) : NOM DU BLOC 2 → TEXTE DROITE : (orange) label / (blanc) explication

**Slide 9 — CTA**
- Titre (encadré bleu, gros) : une question ou une ressource proposée.
- Texte centré (blanc) : ce que reçoit la personne.
- Texte bas (encadré blanc puis bleu, gros) : COMMENTE "MOT-CLÉ".
- Texte orange : et reçois le guide / l'outil complet gratuitement.
- Logo bas + flèche.

**Slide 10 — Clôture**
- Texte centré (bleu clair) : REJOIGNEZ-NOUS SUR WWW.LESOUSLOUEUR.FR
- Texte blanc centré (moyen) : phrase de clôture liée au sujet.
- Icônes bas : cœur, commentaire, partage, enregistrer (icônes Instagram).
- Logo bas : Le Sous Loueur - Sébastien More.

**Consigne visuelle** : à la fin de chaque slide 2 à 8, ajouter une CONSIGNE
VISUELLE précise pour la personne de la mise en page (type d'illustration,
schéma, timeline, checklist, icônes, blocs comparatifs, métaphore, mockup,
courbe…), assez claire pour qu'elle sache quoi créer sans reposer de question.

## A2. Guestlucky — structure de contenu

**Process** :
1. Martin envoie la source / le thème.
2. **Poser d'abord les questions de cadrage** (angle, CTA, ton, prix à mettre en
   avant…) — ne jamais générer avant.
3. Proposer **6 à 8 options de titre de couverture**, classées par angle.
4. Donner ses préférés + justification.
5. Martin choisit (ou dit de choisir).
6. Créer le carrousel complet (sauts de ligne + consignes visuelles).
7. Proposer **2-3 points d'ajustement** possibles à la fin.
8. Itérer.

**Slide 1 — Couverture** : titre principal fort + sous-titre (promesse) + logo
Guestlucky en pied. Pas de numéro.

**Slides 2 à 8 — Contenu** : numéro orange (01, 02…), titre, encadré sous-titre,
points → (orange) label / (texte standard) explication, encadré bas « À retenir »
(punchline), logo Guestlucky + flèche.

**Slide 9 — CTA** : titre percutant, soit un **mot-clé à commenter** (ex CAUTION,
IA, HOGUET) contre un guide/outil, soit une **redirection directe** vers
guestlucky.com / démo / audit. Selon ce que Martin précise.

**Slide 10 — Clôture** : site `www.guestlucky.com`, accroche courte (ex « Le PMS
pensé pour les conciergeries en 2026 »), logo Guestlucky centré, barre d'icônes
Instagram dans une pill orange arrondie.

**Consigne visuelle** à la fin de chaque slide : type de visuel, ambiance,
éléments centraux, usage des couleurs (accent orange sur les points forts).
Pour les couvertures : fond photo (à demander) opacité ~45-50% + overlay navy léger.

### Fonctionnalités & positionnement Guestlucky (banque d'infos produit)
PMS + channel manager tout-en-un :
- Channel Manager natif (Airbnb, Booking, Abritel, synchro temps réel)
- Messagerie IA voyageurs (24/7, multilingue, formée sur les annonces, OpenAI ou
  Google Gemini)
- Auto Actions (10 déclencheurs, 14 conditions, 9 actions empilables)
- Templates de messages avec variables auto-remplies
- Planning ménages + app mobile prestataires
- Interface propriétaire avec KPIs temps réel
- Livret d'accueil digital avec QR code
- Services additionnels à 0% commission (petit-déj, parking, linge)
- Caution intégrée via Stripe, compte par propriétaire (conforme loi Hoguet)
- LuckyCover : assurance intégrée (jusqu'à 50 000€, complémentaire à la caution)
- Facturation électronique conforme réforme 2026
- Conformité loi Hoguet native
- Multi-utilisateurs illimités, équipes illimitées
- PriceLabs intégré (pricing dynamique)
- Module Market Intelligence (audit d'annonces, étude de marché, rapport chiffré)
- Moteur de réservation directe (site direct 0% commission)
- Dashboard et KPIs

Tarifs :
- Gratuit jusqu'à 2 logements
- Premium : 5,99€ HT/mois/logement (ERP complet sans channel manager)
- Pro : 9,99€ HT/mois/logement (tout inclus)
- Personnalisé : sur devis à partir de 20 logements
- Sans engagement, résiliable en 1 clic

Positionnement clé :
- Tout-en-un, une plateforme, une facture
- Économise en moyenne 180€/mois vs stack éclaté
- 0% commission sur services et caution (vs 10-20% ailleurs)
- Pensé par un conciergeur (Sébastien More, depuis 2014)
- Support 100% humain sur WhatsApp
- Migration en < 48h depuis Smoobu, Superhote, Lodgify

---

# PARTIE B — COMMUNITY MANAGER (descriptions, hooks, CTA)

> Ici on rédige les DESCRIPTIONS Instagram/TikTok et les HOOKS. Contrairement aux
> slides, **les descriptions PEUVENT contenir des emojis** (voir formats).

## B0. Règles de style strictes (les 3 marques)

À NE JAMAIS FAIRE :
- « regarde ça », « écoute ça », « dans ce carrousel je te montre »
- « éprouvée », « prouvée » (trop IA)
- « 9 ans » → toujours **8 ans d'accompagnement**
- « webinaire » pour Le Sous Loueur → toujours **« atelier »**
- Hooks trop longs avec 3 phrases hachées
- Qualifier Leapway de channel manager

À TOUJOURS FAIRE :
- Authentique, simple, efficace, français correct. Sonne HUMAIN, pas IA.
- CTA entre guillemets avec flèche : `Commente "MOT" ↓`
- Emoji 😉 après le CTA, parfois 🔑
- Témoignages : commencer par le prénom
- Expliquer les acronymes entre parenthèses à la 1re utilisation
- Si « tu peux faire mieux » : reformuler plus simple, sans répéter
- Si « trop long » : couper drastiquement
- Si « pas français » : fluidifier, virer les points cassés
- Si « fais au mieux » / « choisis toi-même » : **trancher**, ne pas reposer la question

## B1. Formats de description par marque

**Le Sous Loueur :**
```
Commente "MOT" ↓ et [ce qu'ils reçoivent] 😉

[Contexte du post en 2-3 phrases, va droit au but]

[Insight / valeur]

Ça fait 11 ans que je vis de la conciergerie et de la sous-location. Depuis 8 ans j'accompagne ceux qui veulent en faire leur activité. Plus de 3 000 élèves nous ont fait confiance et on est là au quotidien pour leur donner les solutions dont ils ont besoin.

Commente "MOT" ↓ et je t'explique tout 🔑
```

**GuestLucky — FORMAT CHANGÉ LE 30/07/2026, voir la règle 13 :**
```
[Accroche qui pose le problème, 1 phrase]

[Contexte en 2-3 phrases]

[Valeur / fonctionnalité clé]

[CTA final SANS commentaire : enregistre ce post / partage-le /
 abonne-toi / rendez-vous sur guestlucky.com]
```
⛔ **INTERDIT pour Guestlucky** : « Commente MOT ↓ et je t'envoie… », ou toute
promesse qui obligerait Martin à répondre ou à envoyer quelque chose à la main.

**Leapway Instagram :**
```
Commente "LANCEMENT" ou envoie-moi un message en privé ↓ et je t'ajoute à la liste d'accès prioritaire 😉

[Contexte / problème]

[Solution Leapway]

Inscris-toi sur leapwayapp.com et suis @leapwayoff pour être prévenu du lancement.
```

**Leapway TikTok :**
```
Commente "LANCEMENT" ou envoie-moi un message en privé et je t'ajoute à la liste d'accès prioritaire 👇

[Contexte court]

Inscris-toi sur leapwayapp.com et abonne-toi à @leapwayoff sur Instagram, c'est là que tout se passe.

#leapway #locationcourteduree #airbnb #conciergerie #hote [+ hashtags pertinents] #leapwayoff #lancement
```
⚠️ TikTok Leapway : toujours inclure l'appel à s'abonner sur @leapwayoff Instagram.

## B2. Mots-clés CTA par marque

**Le Sous Loueur :**
- CONCIERGERIE → atelier gratuit 2h en DM
- SOUS-LOCATION → atelier gratuit 5h / guides
- CHECKLIST → plan d'action complet
- SIMULATEUR → fichier Excel calcul revenus / micro-BIC vs régime réel
- RADAR → méthode trouver propriétaires
- LEMEUR → guide conformité loi Le Meur
- FACTURATION → guide facturation électronique
- CHANNEL MANAGER → comparatif personnalisé
- ATELIER → lien inscription live gratuit
- BOOTCAMP → rejoindre la communauté

**GuestLucky — ⛔ CES MOTS-CLÉS NE SONT PLUS UTILISÉS (règle 13, 30/07/2026).**
Ils sont gardés pour mémoire seulement. Plus aucun « Commente MOT » côté Guestlucky :
OUTIL, HOGUET, CAUTION, IA, DEMO, AUDIT. Utiliser à la place les 4 actions
autorisées : s'abonner, enregistrer le post, le partager, visiter guestlucky.com.

**Leapway :**
- LANCEMENT → liste d'accès prioritaire
- COMPARO → tableau comparatif plateformes

## B3. Si Martin envoie une transcription de short
→ 5-8 hooks CAPS LOCK courts et intrigants
→ Description Instagram avec CTA EN HAUT
→ Donner le top 3 + la recommandation

## B4. Si Martin envoie des slides de carrousel
→ Demander la marque si pas évident
→ Faire la description Instagram
→ Pour Leapway : faire aussi la description TikTok avec hashtags

---

# PARTIE C — MISE EN PAGE (design HTML/CSS → PNG)

> Rôle EXCLUSIVEMENT mise en page. Martin envoie le contenu déjà rédigé slide par
> slide. On ne rédige jamais le contenu : on le met en page en HTML/CSS, on rend
> en image via Playwright Chromium, on livre les fichiers.

## C0. Format technique commun
- 10 slides par carrousel.
- Rendu HTML + CSS via **Playwright Chromium**.
- Viewport **1080×1350**, `device_scale_factor=3` → PNG **3240×4050** (portrait 4:5).
- Police **Montserrat** partout, sans exception : sélecteur universel `!important`,
  `@import ...&display=block`, `<link rel="preconnect">` + `<link rel="stylesheet">`,
  et `page.wait_for_function("document.fonts.check('900 80px Montserrat')")` avant capture.

## C0bis. Règles design absolues (toutes marques)
- **ZÉRO tiret long** (— – ‒ ― ⎯ ﹣ － ─, toutes variantes Unicode) : remplacer par
  deux-points, virgule ou point. Corriger sans demander + signaler lesquels.
  Ajouter un **check regex anti-tirets** dans le script (hors data:image base64).
- **ZÉRO emoji** dans les slides. Uniquement des SVG dessinés à la main (outline,
  stroke 2-3px, linecap/linejoin round). Unicode sobres monochromes (✓ × ▼ ↓ → ★)
  tolérés s'ils sont colorisés en CSS.
- **AUCUN glow / box-shadow lumineux**, aucune zone grise translucide vide, aucun
  petit rond numéroté. Style **éditorial magazine**, pas « IA générique ».
- Blocs de listes avec marges latérales (pas full-width brut).
- **Logo officiel EXTRAIT** (fond transparent via PIL/numpy), **jamais recréé en
  SVG**, jamais approximé. Toujours **centré en bas**.
- **Photo de fond : je l'écris et je la crée MOI-MÊME** (décision Martin, 24/07/2026).
  Je ne demande plus la photo à Martin : je rédige moi-même le prompt de fond
  (selon le sujet + la palette de la marque, règles PARTIE D) et je produis l'image.
  Ne jamais réutiliser la photo d'un carrousel précédent. Visible en filigrane (~45-50%).
- **Tailles textes centraux (lisibilité mobile), ne jamais descendre en dessous** :
  titre de point ~33px weight 800, description ~27px weight 500 (line-height 1.35),
  marge entre points 24-32px. Si ça ne rentre pas, réduire le titre de slide ou le
  visuel, jamais le corps.
- **Retouche** = corriger uniquement le point demandé, garder le reste identique.
  Ne jamais repartir de zéro.
- Honnêteté totale : signaler un contenu problématique avant de générer, vérifier
  les calculs. Si l'outil de visualisation d'images ne marche pas dans la session,
  le dire franchement et compenser par les contrôles automatiques (ne jamais
  prétendre avoir vérifié visuellement si ce n'est pas le cas).

## C1. Le Sous Loueur — charte + mise en page

**Couleurs (ne jamais dévier) :**
- Navy fond `#0d1b2e`
- Orange accent `#E8561F`
- Bleu clair `#2086C8` (titres, pills, info-pill gauche)
- Rouge soft `#ff5a5a` (erreurs, dangers, « avant » négatif)
- Vert soft `#5dd987` (validations, solutions, « après » positif)
- Blanc `#ffffff`
- Barre haut de slide : 6px, `linear-gradient(90deg, #2086C8 0%, #5fa0d0 50%, #E8561F 100%)`

**Logo :**
- Slides 2-9 : logo 64px centré (bottom:50px) + chevron orange « » absolute
  right:55px, 72px, weight 900.
- Slide 1 : logo 80px centré + chevron 80px.
- Slide 10 : logo 80px centré, SANS chevron.

**Photo de fond :** redim 900px large, JPEG q82, base64. `.bg-photo` opacity 0.50 ;
`.bg-overlay` `linear-gradient(135deg, rgba(13,27,46,.78), rgba(10,21,37,.85))`.
Si pas assez visible : opacité 0.55 + overlay 0.70.

**Slide 1 — Couverture (tout centré) :** titre blanc 60-76px weight 900 uppercase,
line-height 1.0, letter-spacing -2.2px (un mot-clé peut passer en orange) ;
sous-titre orange 27-28px weight 800 uppercase ; texte bas blanc italique 25px
weight 500 ; pas de trait orange en haut ; logo 80px + chevron.

**Slides 2 à 9 — Contenu :**
- Header flex space-between : titre top-left bleu `#2086C8` 48-54px weight 900
  uppercase (line-height 1.02, letter-spacing -1.5px, sauts de ligne manuels,
  lignes < ~20 caractères) ; chiffre éditorial top-right 140px weight 900 orange
  (line-height 0.85, letter-spacing -6px), **chiffres 1,2,3… SANS zéro devant**,
  pas de carré ni de rond.
- Sous-titre : pill bleue `#2086C8`, padding 14px 26px, radius 10px, 22px weight
  700, align-self flex-start.
- Corps (points) : `.pl` titre du point orange 33px weight 800 ; `.pt` description
  blanc 27px weight 500 line-height 1.35 ; gap 24-26px.
- Bas : info-pill = label bleu à gauche (flex-shrink:0) + valeur blanche fond blanc
  à droite (flex-grow:1), radius 12px, overflow hidden, 21px weight 700.
- Logo centré + chevron orange.

**Slide 9 (ou N-1) — CTA (si prévu dans le contenu, tout centré) :** pavé bleu
`#2086C8` titre 36px weight 900 uppercase ; description blanche 25px ; gros pavé
BLANC `COMMENTE "MOTCLÉ"` en navy 40px weight 900 ; ligne italique orange dessous.
(Certains carrousels n'ont pas de slide CTA : suivre exactement la structure envoyée.)

**Slide 10 — Finale :** « REJOIGNEZ-NOUS SUR » bleu `#2086C8` 32px ;
« WWW.LESOUSLOUEUR.FR » blanc 44px weight 900 ; message de clôture blanc 28px ;
barre d'icônes Instagram (cœur, commentaire, partage, enregistrer) dans une pill
orange arrondie (radius 70px, padding 22px 50px), SVG main stroke blanc 2.5px ;
logo 80px centré sans chevron.

**Police :** Montserrat forcée `!important`, numéros orange éditoriaux 140px.

## C2. Guestlucky — charte + mise en page

**Couleurs (exactes) :**
- Fond navy très foncé `#0a0e27`
- Violet principal `#7c3aed` (titres, chevron, accents)
- Violet foncé `#5b21b6` (dégradés)
- Rose magenta `#ec4899` (accent secondaire)
- Blanc `#ffffff`
- Rouge soft `#ff5a5a` (alertes, pièges)
- Vert soft `#5dd987` (solutions, bénéfices)
- Barre top : dégradé violet `#7c3aed` → rose `#ec4899`, 6px.
- **Code couleur narratif** : rouge = pain points/failles, violet = explications
  neutres, vert = solution Guestlucky/bénéfices, rose = « hi » secondaires.

**Logo :** PNG fond bleu marine RGB (24,39,70) → transparent (PIL, tolérance ~35),
jamais recréé en SVG. Centré en bas de chaque slide (64px, sauf slides 1 et 10 = 80px).

**Slide 1 — Couverture (centré) :** eyebrow « GUESTLUCKY · THÈME » rose magenta
uppercase letter-spacing 6px ; titre 60-64px weight 900 (accents violet + rouge/rose
sur mots-clés) ; sous-titre blanc translucide ; divider rose 80px×3px ; logo 80px ;
pas de numéro, pas de chevron.

**Slides 2 à 8 — Contenu :** titre top-left violet `#7c3aed` uppercase 38-42px
weight 800 ; chiffre éditorial top-right violet 140px weight 900 (1-7, sans zéro) ;
sous-titre en pill violette (padding 14px 28px, radius 10px, weight 700) ; points :
point-label violet 32-34px weight 800, point-text blanc 26-28px weight 400, marge
entre points 32px min, margin-left du point-text 36px ; info-pill bas (label violet
gauche / valeur blanche fond blanc droite) ; logo centré + chevron violet « »
(bottom:50px, right:55px, 72px weight 900).

**Badges spéciaux** (top:80px, left:80px, padding 6px 14px, radius 6px) :
- « Piège n° X » rouge soft (fond rgba(255,90,90,0.18), bordure 1.5px #ff5a5a)
- « Pilier X » / « Levier N° X » dégradé violet/rose ou violet
- « Conforme loi Hoguet » vert soft (fond rgba(93,217,135,0.18), bordure #5dd987)
- Badge date/deadline, DAC7… en rouge soft

**Slide 9 — CTA (2 formats) :**
- Format A (mot-clé à commenter) : eyebrow « ACTION · 1 MOT » rose ; titre « Envie
  de X ? » accent violet ; gros pavé blanc arrondi « COMMENTE » + mot-clé violet
  110-120px weight 900 letter-spacing 4-6px ; ligne valeur perçue ; flèche bas violette.
- Format B (démo/audit direct) : eyebrow « SOLUTION » / « PASSER À L'ACTION » rose ;
  titre percutant accent violet ; description highlight rose ; gros bouton dégradé
  violet→rose « RÉSERVE TA DÉMO » / « AUDIT GRATUIT » (padding 24px 44px, radius 60px,
  uppercase letter-spacing 2px) ; sous-texte « 30 min en visio · Sans engagement » ;
  pill blanche « guestlucky.com » en violet.

**Slide 10 — Finale :** eyebrow « REJOIGNEZ-NOUS SUR » rose ; « guestlucky.com »
64px weight 900 blanc ; séparateur violet 80px×3px ; message de fin blanc accent
violet ; barre icônes Instagram SVG main (stroke 2.2px) dans une pill dégradé
violet→rose (padding 22px 40px, gap 38px) ; logo 80px centré.

**Photo de fond :** recadrage 4:5 (PIL, crop centré, LANCZOS) ; overlay navy
`linear-gradient(135deg, rgba(10,14,39,0.80), rgba(10,14,39,0.86))` (renforcer à
0.82/0.88 si sujet grave/juridique) ; photo visible ~40-50%. Si pas de photo et
« lance » : fond navy uni gradient subtil sobre.

**CTA slide 9 à demander (2-3 questions max via l'outil de questions)** : photo de
fond (à envoyer ou navy uni ?), format A ou B, mots-clés/contenus sensibles.

### Workflow technique Guestlucky (référence)
1. Dossier de travail (ex `/home/claude/gl_cX`).
2. Copier logo + photo depuis les uploads.
3. Extraire le logo (fond navy → transparent, tolérance 35, crop auto marge 20px).
4. Recadrer la photo en 4:5 (LANCZOS).
5. Encoder logo + photo en base64 (fichiers `logo_b64.txt`, `bgN_b64.txt`).
6. `generate_cN.py` : COMMON_CSS (typo/couleurs), fonction `wrap()`, les 10 slides,
   check regex anti-tirets final.
7. `render_cN.py` (Playwright) : viewport 1080×1350, scale 3, wait Montserrat 900 80px,
   timeout 300ms, screenshot clip 1080×1350.
8. Vérifier 3-4 slides clés avant de zipper.
9. Copier les PNG en sortie avec préfixe explicite (ex `hoguet_slide_XX.png`).
10. ZIP `carrousel_guestlucky_SUJET.zip`.
11. Livrer via l'outil de partage : ZIP en premier + tous les PNG.

## C3. Leapway — charte visuelle (pour mémoire)
- Fond dark navy/black `#0a1410`, accent mint green `#8FF0B5`.
- Labels bracket `[ MOT ]` sur les eyebrows.
- Option B photo background = défaut.
- Slide 10 : Instagram @leapwayoff + leapwayapp.com.

## C4. Vérifications obligatoires avant livraison (Le Sous Loueur, applicable partout)
- **A) Débordements** : ouvrir chaque HTML dans Playwright, attendre
  `document.fonts.check('900 80px Montserrat')`, vérifier en JS que
  `scrollHeight <= clientHeight` et qu'aucun élément (.title, .pl, .pt, .info,
  .subpill, visuels…) ne dépasse la zone utile. Corriger avant de rendre.
- **B) Tirets longs** sur le HTML généré.
- **C) Contrôle pixel (numpy) sur les PNG** : logo présent en bas-centre ; chevron
  orange bas-droite (slides 1-9) ; chiffre éditorial orange haut-droite (slides de
  contenu).
- **D)** Si la visualisation d'images ne marche pas : le dire franchement, compenser
  par les contrôles auto, ne jamais prétendre avoir vérifié visuellement.

## C5. Livraison (Le Sous Loueur — contrainte Metricool)
Martin programme avec **Metricool** (auto-publish). Metricool refuse les images
> 1440px de large et plante sur certaines métadonnées. Livrer SYSTÉMATIQUEMENT
**deux dossiers + leurs ZIP** :
1. **DOSSIER JPG (celui utilisé)** : JPEG 1080×1350 exact, quality 88, optimize True,
   progressive=False (baseline), subsampling=2 (4:2:0), **AUCUN profil ICC, AUCUNE
   EXIF** (reconstruire l'image dans un nouvel objet PIL avant save), poids 60-250 Ko/slide.
2. **DOSSIER PNG HD** : PNG 3240×4050.
Présenter : ZIP JPG en premier, puis les 10 JPEG, puis le ZIP PNG HD.

## C6. Consignes visuelles → visuels sobres (banque de patterns réutilisables)
Comparatif avant/après (2 cards bordées rouge/vert ou bleu/orange + flèche orange
au milieu) ; timeline de rupture (date pivot orange centrée) ; entonnoir (blocs
100/84/68/52/38%, dernier orange plein) ; escalier de montants (opacité croissante) ;
formule mathématique (encadré orange, chiffre clé 52px) ; flux d'argent (3 blocs +
flèches + tampon incliné rotate(-6deg)) ; jauges (barres % horizontales) ; checklist
(coche verte / croix rouge / texte barré) ; blocs empilés bordure gauche 4px orange
+ picto carré arrondi ; schéma en tenaille (2 menaces → bloc central orange) ; stat
blocks (gros chiffre orange + libellé). Le visuel occupe 150-260px, sans écraser les
textes.

## C7. Ce qu'il faut demander au début (mode « Claude fait tout »)
- **La marque** (si pas évidente) et, pour Guestlucky, le format du CTA slide 9.
- Je ne demande PLUS la photo de fond (je la crée moi-même, PARTIE D).
- Seul élément que je ne peux pas inventer : **le logo officiel** de la marque (PNG).
  Si je ne l'ai pas encore reçu dans le projet, le demander une fois (version blanche
  pour Le Sous Loueur) ; ensuite le réutiliser.

---

# PARTIE D — ASSISTANT DE PROMPTS VISUELS (Seedance / Magnific / Ideogram / MJ)

> Rôle : créer des **prompts** pour générer des visuels IA (fonds photo réutilisables
> pour carrousels, stories, pubs Meta) pour les 3 marques. Martin = « Martin Moret »,
> prestation IA/tech/créa. Style direct et efficace, français, info importante en premier.
> ⚠️ **Règle d'or** : à chaque demande, DEMANDER pour quelle marque. Ne JAMAIS
> mélanger les univers ni les palettes entre marques dans un même prompt.

## D0. Règles générales sur les prompts
- **Seedance** : 5000 caractères max (viser 3500-4500). **Compter vraiment** les
  caractères avant de livrer, pas d'estimation.
- **Magnific / autres outils image** : ~10000 caractères, toujours détaillé.
- Structurer les prompts avec des sections séparées par des lignes `═══════` et des
  MAJUSCULES, **en anglais** (meilleurs résultats).
- Toujours inclure : palette exacte (codes hex), exclusions absolues, layout précis
  par zones (%), style, lighting, rendering, checklist finale.
- Story 9:16 : prévoir une **zone vide en bas (12-18%)** pour le sticker lien Instagram.
- « refais » / « variante » = concept VRAIMENT différent, pas une reformulation.
- Rendu qui ne plaît pas → demander ce qui cloche AVANT de re-proposer.

## D1. Règles logos (dans les prompts)
Toujours écrire : « DO NOT draw logos from memory, DO NOT recreate logos, USE ONLY
the exact logo files I provided ». Si le logo apparaît : « pixel perfect from reference ».

## D2. Règles orthographe (anti-fautes IA)
Les modèles écorchent le texte. Épeler lettre par lettre les mots critiques, ex :
« GuestLucky — G-u-e-s-t-L-u-c-k-y, only ONE 'Lu', NEVER 'GuestluLucky' ». Idem
WEBINAIRE (I après WEB, pas U), Découvrez (un seul r), maintenant (pas miiontent)…

## D3. Exclusions absolues (à ajouter à TOUS les prompts)
- NO visible light rays, NO halos, NO light beams, NO light shafts, NO « puits de lumière »
- NO exaggerated contrast, NO HDR over-processing, NO oversaturation
- NO artificial AI rendering look, NO plastic 3D cheap look
- NO emoji, NO × close button, NO screenshot artifact, NO browser frame, NO mouse cursor
- NO watermark, NO duplicate text, NO duplicate logo
- Photorealistic natural film grain, style Sony A7 / Hasselblad / iPhone 15 Pro selon le contexte

Pour les visuels intérieur / staging / conciergerie photo :
- Linge blanc hôtel-quality (jamais coloré), serviettes pliées spa ou roulées,
  bougies sur plateau / bord de bain, pas de chaussures ni objets perso, pas de
  plaid coloré sur les lits.

## D4. Palettes strictes par marque (prompts visuels IA — NE PAS confondre avec la mise en page)

**GUESTLUCKY** (SaaS channel manager + IA voyageurs ; conformité loi Hoguet 2026,
0% commission services, IA intégrée) :
- Fond bleu marine profond : `#0F1A35` / `#0A1228` / `#1A1330`
- Violet : `#7B4FE0` / `#8B3FD9` / `#9B6FFF`
- Magenta pink : `#C13FBE` / `#D6398E` / `#E84A8C`
- Blanc `#FFFFFF` ; Lavande claire (fond éditorial) `#F2EFFA`
- Ambiance : premium SaaS moderne, tech, éditorial (Stripe / Linear / Notion) ;
  du sombre premium au clair éditorial selon le sujet.
- Logo : maison violette + petit carré magenta au centre, « Guest » blanc + « lucky »
  violet. Jamais de mémoire, toujours pixel perfect depuis le fichier fourni.

**LE SOUS LOUEUR** (coaching/formation conciergerie & sous-location ; 11 ans terrain,
100+ logements pilotés, 3000+ élèves) :
- Bleu marine profond : `#0E1B2E` / `#142841` / `#182745`
- Orange vif : `#E8551F` / `#F25C2A` / `#FF5D00`
- Blanc `#FFFFFF` ; Cream/beige (fond éditorial) `#F5F5EE`
- Ambiance : premium éditorial hospitality magazine (Kinfolk / Monocle / Condé Nast
  Traveler) pour les flat-lay, OU dark sales funnel pour les slides bonus/promo.
- ⚠️ Ne JAMAIS utiliser le violet/magenta de Guestlucky sur un visuel Le Sous Loueur.
- Logo : maison blanche + barres orange + wordmark blanc + sous-titre « Sébastien More »
  blanc 70%. Typo exclusive : Montserrat.

**LEAPWAY** (plateforme de réservation FR en dev, channel manager natif intégré ;
plateforme unique, moins de commissions ; leapwayapp.com) :
- Fond vert nuit très foncé : `#0A1F1A` / `#0D2620` / `#0F2A22`
- Vert menthe lumineux : `#B8F5C4` / `#A8E8B5` / `#C8F5D4`
- Cream/blanc : `#F5F8F5`
- Ambiance : premium tech-hospitality (Linear / Vercel / Wired), nuit étoilée /
  constellations, réseaux connectés. Ne jamais utiliser les couleurs des autres marques.

## D5. Outils de génération (toujours suggérer le meilleur selon le visuel)
- **Seedance** (image + vidéo) : outil principal, limite 5000 caractères.
- **Magnific** (GPT 2, Nano Banana Pro, Nano Banana 2, Seedream 5.0) : Nano Banana Pro
  = paysages/flat-lay premium ; Nano Banana 2 = retouches ; Seedream = visuels avec
  texte ; GPT 2 = polyvalent. Limite ~10000 caractères.
- **Ideogram** : logos et texte précis dans le visuel.
- **Midjourney** : illustrations éditoriales.

## D6. Méthode de travail
- Carrousel envoyé (transcription de slides) → demander la marque, puis faire UN
  prompt de fond visuel réutilisable pour toutes les slides.
- Stories / pubs Meta → penser au sticker lien Instagram (zone vide en bas).
- Livrer l'info importante en premier, pas de long préambule.

---

# 🤖 PROJET — AUTOMATISATION COMPLÈTE (objectif de Martin, 24/07/2026)

**Objectif choisi par Martin : le TOUT-AUTOMATIQUE** — une chaîne qui crée ET
publie les carrousels seule, sans clic de sa part (option « tout auto sans moi »).
On y va, mais on le construit **brique par brique**, en testant chaque brique avant
de laisser tourner sans surveillance (un post fautif sur un compte public est dur à
rattraper). Même en tout-auto : filet de sécurité obligatoire (contrôle qualité auto
+ journal des publications + kill switch facile).

## Contrainte clé — où tourne la machine
Cet environnement (Claude Code sur le web) est un **bureau cloud à réseau bloqué** :
`api.seedance2.ai` et Metricool sont refusés par la politique réseau (403 CONNECT,
vérifié le 24/07/2026). → **L'automatisation doit tourner sur le Mac de Martin**
(Claude Code en local, sans ces restrictions). Ici, je PRÉPARE le code dans le repo ;
Martin le fait tourner sur son Mac.

## Seedance — ce qu'on sait
- API réelle : base URL `https://api.seedance2.ai` (docs `seedance2.ai/api-docs`).
- Auth : clé API en Bearer token (créée dans le dashboard, montrée une seule fois).
- Génération **asynchrone** (vidéo surtout) : créer une tâche → task ID → polling
  ou webhook → récupérer le rendu. Crédits réservés à la soumission, remboursés si échec.
- ⚠️ Surtout orienté VIDÉO ; pour des photos de fond, vérifier l'endpoint « AI Image ».
- ⚠️ Repo PUBLIC → la clé Seedance ne va JAMAIS dans le code : variable d'environnement
  / `.env` local non commité.

## Check-list des prérequis (à réunir avec Martin)
1. **Ouvrir la politique réseau** de l'environnement (autoriser youtube.com +
   api.seedance2.ai + metricool) — Option B choisie par Martin (24/07/2026).
2. Clé API Seedance + crédits (bouton "Create API Key" sur seedance2.ai/api-docs,
   affichée une seule fois). → à fournir comme SECRET, jamais dans le code.
3. Token API Metricool (Paramètres → section API) + forfait incluant l'API
   (souvent Advanced+). → SECRET.
4. Les pages de doc API Seedance + Metricool (Martin me les colle en capture).

## Repères comptes (fournis par Martin, 24/07/2026 — identifiants, PAS des secrets)
- **Chaîne YouTube (source du dimanche)** : https://www.youtube.com/@moresebastien
- **Metricool** : userId = 3122469
  - Le Sous Loueur (compte « Sebastien More », SANS accent, 3 réseaux) : blogId = 3968518
  - Guestlucky (compte « guestlucky.off ») : blogId = 4001072
  ⚠️ Voir plus bas « RÈGLES GRAVÉES — MARQUES METRICOOL » : une marque « Sébastien More »
  AVEC accent existe aussi et est INTERDITE partout.
- **Seedance** : base URL https://api.seedance2.ai, auth Bearer, génération async
  (orienté vidéo ; vérifier l'endpoint AI Image pour les photos de fond).

## 📦 LIVRAISON AUTOMATIQUE vers le Claude du Mac (27/07/2026) — EN PLACE
Martin ne télécharge plus les ZIP à la main. Chaque carrousel fini est poussé sur
GitHub dans `livraison/`, et le Claude de son Mac vient les chercher le vendredi.

### Pourquoi GitHub et rien d'autre (testé le 27/07)
- `git push` fonctionne (via le proxy local) et **atterrit sur le vrai GitHub** :
  vérifié en relisant le dépôt depuis l'internet public
  (`raw.githubusercontent.com` → HTTP 200 + contenu correct).
- ⛔ **Google Drive : piège.** Le connecteur existe en session interactive, mais une
  Routine créée via MCP **ne transporte aucun connecteur** : le lundi matin, Drive
  serait absent. Ça marcherait en test et casserait en production.
- ⛔ transfer.sh, 0x0.st : bloqués. catbox.moe, file.io : hébergeurs temporaires
  (liens expirables, pas de dossiers) → inadaptés à un rendez-vous hebdomadaire.
- ⛔ `api.metricool.com` : bloqué. `api.github.com` : 403 sur les endpoints repo.
- ✅ Avantage décisif de git : un push dépose les 20 images **d'un seul coup**.
  Le Mac ne peut jamais tomber sur un dossier à moitié rempli.

### Format EXACT (validé par Martin, le Mac s'aligne dessus)
```
livraison/
└── <marque>-<AAAA-MM-JJ>-<sujet>/
    ├── 01.jpg ... 10.jpg          (1080x1350, prêtes pour Metricool)
    └── description.txt            (légende Instagram)
```
- marque = **`lesousloueur`** ou **`guestlucky`** (jamais « guettelucky », jamais de majuscule)
- date = le **lundi** de la semaine → tri alphabétique = tri chronologique
- images renommées **`01.jpg` → `10.jpg`** (le préfixe `slide_` disparaît)
- ⛔ **les images de fond ne sont PAS livrées** (déjà incrustées, 2,9 Mo pièce)
- poids réel : **~1,2 Mo par carrousel**, soit ~2,5 Mo/semaine, ~130 Mo/an. OK pour GitHub.

### L'outil : `pipeline/engine/livraison.py`
`python3 livraison.py <slug> [--date AAAA-MM-JJ] [--sujet mot-cle] [--remplacer]`
`python3 livraison.py --controle [--date AAAA-MM-JJ]`

- **Marque déduite par recherche du jeton**, pas du seul préfixe : `lsl_x`,
  `v2_lsl_x`, `build_gl_x`, `LSL-x`, `lesousloueur_x` fonctionnent tous.
  Jetons reconnus : `lsl` / `lesousloueur` / `sousloueur` → lesousloueur ;
  `gl` / `guestlucky` → guestlucky.
- Date par défaut = lundi de la semaine en cours.
- **Refuse de livrer** s'il n'y a pas exactement 10 slides ou si `description.txt`
  manque → mieux vaut rien livrer qu'un carrousel incomplet.
- **Refuse d'écraser** une livraison au contenu DIFFÉRENT (il faut `--remplacer`
  ou un `--sujet` distinct). Re-livrer à l'identique dit « déjà livré, rien à faire ».
- Construction dans un dossier provisoire `.tmp-…` puis renommage : si ça casse en
  cours de copie, la livraison précédente reste intacte.
- **`--controle`** : vérifie que les DEUX marques sont livrées pour la semaine, avec
  10 images et une description chacune. Code de sortie 1 si incomplet.

### ⚠️ BUG TROUVÉ ET CORRIGÉ LE 27/07/2026 (2 carrousels perdus en silence)
La 1re version ne lisait que le **préfixe** du slug : tout nom commençant par `v2_`
était refusé. Résultat : `v2_lsl_conciergerie_220k` et `v2_gl_conformite_lemeur`
(les **démos design V2 validées**, donc les meilleures) n'avaient PAS été livrées,
sans que rien ne le signale. Le prompt du lundi n'imposait aucune règle de nommage,
alors qu'il demande de suivre le modèle des fichiers `v2_lsl_…py` : la panne était
donc probable dès la première exécution.
**Trois correctifs appliqués** :
1. détection du jeton de marque n'importe où dans le nom (plus seulement en préfixe) ;
2. règle de nommage écrite noir sur blanc dans le prompt du lundi (étape 3) ;
3. **étape 9 du robot = `--controle` obligatoire avant le push** : si une marque
   manque, interdiction de pousser en silence, il doit nommer la marque manquante
   en première ligne de son message à Martin.
Les 2 carrousels V2 ont été rattrapés sous les sujets `…-designv2`.
**Leçon générale : tout maillon silencieux doit avoir un contrôle qui alerte.**

### Adresses à donner au Claude du Mac
- dépôt : `https://github.com/xSARRASx/CARROUSSEL-`
- branche : `claude/carrousel-instagram-robot-hk4743`
- dossier : `livraison/`

## 🛑 RÈGLES GRAVÉES — MARQUES METRICOOL (Martin, 27/07/2026, vérifié à l'écran)
Orthographe EXACTE relevée par Martin dans sa liste de marques Metricool.
**Un piège volontaire existe : deux marques au nom presque identique.**

| Marque (orthographe exacte) | Réseaux | Usage | Autorisation |
|---|---|---|---|
| **`Sebastien More`** (SANS accent) | Instagram + TikTok + YouTube (**3 icônes**) | **SHORTS** | ✅ LA BONNE |
| `Sébastien More` (AVEC é accentué) | Instagram seul (**1 icône**) | — | ⛔ **INTERDITE** |
| `guestlucky.off` | Instagram seul | Carrousels Guestlucky (plus tard) | ⚠️ jamais pour les shorts |
| `Marque vide` (x2) | — | — | ⛔ **INTERDITES** |

### Procédure obligatoire avant toute action sur une marque
Vérifier **LES DEUX** critères, jamais un seul :
1. le nom est exactement **`Sebastien More`**, **sans accent** sur le e ;
2. la marque affiche bien **les 3 icônes de réseaux** (Instagram + TikTok + YouTube).
Si l'un des deux critères manque → **ne rien faire et demander à Martin**.
Le critère des 3 réseaux est le plus fiable : un accent se lit mal à l'écran,
trois icônes se comptent sans ambiguïté.

### ✅ TRANCHÉ par Martin le 27/07/2026 — plus aucune ambiguïté
Les **carrousels Le Sous Loueur** partent sur **`Sebastien More` SANS accent**, la
marque aux 3 réseaux — **la même que les shorts**. Publication sur **son Instagram**.
La marque accentuée `Sébastien More` est **interdite PARTOUT** : shorts, carrousels,
tout. Elle n'a aucun usage légitime dans ce projet.

Récapitulatif complet des destinations :
| Contenu | Marque Metricool | Réseau |
|---|---|---|
| Shorts | `Sebastien More` (sans accent, 3 réseaux) | Instagram + TikTok + YouTube |
| Carrousels **Le Sous Loueur** | `Sebastien More` (sans accent, 3 réseaux) | Instagram |
| Carrousels **Guestlucky** | `guestlucky.off` | Instagram |
| — | `Sébastien More` (accentuée) | ⛔ **JAMAIS, nulle part** |

### ❌ Ce que ce robot n'a JAMAIS fait, et ne peut pas faire
**Aucun calendrier Metricool n'a jamais été lu depuis cet environnement.**
`api.metricool.com` est **bloqué** par la politique réseau (revérifié le 27/07 :
aucune réponse). `app.metricool.com` répond 200 mais ce n'est que la page de
connexion, sans session : illisible. Si un calendrier a été consulté, c'est par le
**Claude du Mac**, pas ici. Ne jamais affirmer avoir vu un planning Metricool.

## Workflow cible (précisé par Martin, 24/07/2026)
Cadence **hebdomadaire, 100% autonome** :
- Une vidéo sort **chaque dimanche** sur une chaîne YouTube (URL à fournir par Martin).
- **Chaque lundi** : le robot récupère tout seul la transcription → fabrique **DEUX**
  carrousels **adaptés** à partir de la même vidéo :
  - 1 pour **Guestlucky** (angle « ce qu'on vend », palette/logo/CTA Guestlucky),
  - 1 pour **Le Sous Loueur** (son angle, palette/logo/CTA Le Sous Loueur).
- Programmation **vendredi 18h** sur l'Instagram de Guestlucky ET celui de Le Sous
  Loueur, via **Metricool** — faite par le **Claude du Mac** depuis le 27/07/2026,
  plus par Martin. Ce robot s'arrête au push GitHub.

## ✅ COMMENT OUVRIR LE RÉSEAU (trouvé le 24/07/2026)
Le réglage réseau n'est PAS modifiable dans une session en cours (l'env « Default »
est figé). Il se choisit à la **création d'un environnement** :
- Dans claude.ai/code → cliquer le nuage ☁️ de l'environnement → **« Nouvel
  environnement cloud »** (apparaît en créant une nouvelle conversation).
- Champ **« Accès réseau »** : 4 niveaux (doc code.claude.com) :
  - **Aucun / None** : pas d'accès internet.
  - **Trusted** : uniquement l'allowlist par défaut (npm, pypi, GitHub…). = l'actuel.
  - **Complet / Full** : **N'IMPORTE QUEL domaine** → YouTube + Seedance + Metricool OK.
  - **Custom** : allowlist perso (une ligne par domaine, wildcard `*.`).
- → Créer un env **« CARROUSSEL AUTO »** avec **Accès réseau = Complet**.
- Les **secrets** (clé Seedance, token Metricool) se mettent dans le champ
  **« Variables d'environnement »** de cet env (format `.env`, `KEY=valeur`) —
  JAMAIS dans le code. ⚠️ Visibles par qui peut éditer l'env (pas de coffre secret
  dédié), mais ça reste privé au compte de Martin. C'est le bon endroit.
- ⚠️ Le nouvel env n'ouvre le réseau que pour les **NOUVELLES sessions** lancées
  dessus (la session actuelle reste en Trusted). Le robot se construit dans une
  session neuve sur l'env « CARROUSSEL AUTO » + repo CARROUSSEL-. Tout le code est
  déjà dans le repo, donc une session neuve le retrouve.
- Setup script possible (installer Pillow/numpy/playwright) au démarrage de session.

## Décision d'architecture — OÙ tourne le robot (à trancher avec Martin)
- Ce bureau cloud actuel BLOQUE YouTube (403), Metricool (403) et Seedance (403).
  (googleapis.com répond 405 = joignable, mais youtube.com non.)
- **Option A — sur le Mac de Martin** : réseau ouvert, mais Mac doit être allumé le
  lundi + cron local. Mac éteint = pas de post.
- **Option B (RECOMMANDÉE pour du vrai « sans moi ») — environnement cloud toujours
  allumé avec politique réseau ouverte** (autoriser youtube.com + api.seedance2.ai +
  Metricool). Claude pose un déclencheur cron « tous les lundis » → tourne sans le Mac.
- Claude Code Remote dispose bien d'outils de planification (triggers/cron) : le
  « sans surveillance » est possible techniquement, à condition d'ouvrir le réseau.

## Plan par étapes
- **Étape 1 (FAITE)** : moteur de création (contenu → photo → 10 slides Playwright →
  JPEG Metricool-ready). Testé avec Martin.
- **Étape 2 (FAITE)** : brique « récupérer la transcription YouTube ».
  Script : `pipeline/engine/fetch_transcript.py`. Fonctionne dans l'env réseau ouvert.
- **Étape 3** : brique « photo de fond Seedance » (base https://api.seedance2.ai,
  clé SEEDANCE_API_KEY, Bearer, endpoint image).
- **Étape 4** : brique « publication Metricool » (d'abord brouillon programmé, pour vérifier).
- **Étape 5** : déclencheur hebdo (lundi) + filet de sécurité (contrôle qualité auto +
  journal des posts + kill switch) → tourne sans surveillance.

**Étape en cours : Étape 3 — photo de fond via Seedance (code prêt, test payant à valider).**

## Étape 3 — photo de fond Seedance (découvertes techniques, 24/07/2026)
⚠️ **L'API Seedance (avec la clé) ne fait QUE de la VIDEO**, pas de photo.
- generation_type acceptés : `text-to-video`, `image-to-video`, `reference-to-video`.
  Pas de `text-to-image`. Confirmé en testant l'API.
- Le "text-to-image" (Seedream, Nano Banana, Z-Image, GPT Image) existe seulement
  sur le **site web** seedance2.ai/ai-image (routes internes type
  `/api/video/<provider>/generate`, gated par session utilisateur), PAS via la clé API.
  Donc inutilisable par un robot automatique.
- **ASTUCE retenue** : l'API vidéo accepte l'option **`return_last_frame: true`** →
  elle renvoie une IMAGE (last_frame_url). On demande une mini-vidéo et on prend
  l'image : c'est notre photo de fond, 100% automatique avec la clé.
- **Endpoints** : créer = `POST /v1/videos/generations` (corps `{"input":{...}}`,
  Bearer) → renvoie `{taskId, credits}` ; suivre = `GET /v1/tasks/:id` (statut
  `generating`/`completed`/`failed`, `data.last_frame_url`, `data.results[0]`=mp4).
  Pas d'endpoint d'annulation (DELETE 405, cancel 404) ni de solde de crédits.
- **Coût mesuré** : génération standard 5s / 720p = **60 crédits**. (1080p/4k = plus.)
- ⚠️ **60 crédits dépensés par erreur** le 24/07 (un test a lancé une vraie tâche
  vidéo, prompt bidon). Leçon : NE JAMAIS envoyer un POST /v1/videos/generations
  valide en test ; pour sonder, corps volontairement invalide (400 sans coût).
- Script : `pipeline/engine/seedance_bg.py`. Modes `--dry-run` (0 crédit, prépare
  la commande) et `--go` (génère pour de vrai). Prompts de fond par marque (palettes
  PARTIE D strictes : Guestlucky navy/violet/magenta ; Le Sous Loueur navy/orange,
  jamais violet). Recadrage auto 4:5, sortie `pipeline/assets/backgrounds/<marque>_bg.jpg`.
- Outils requis : `pip install imageio imageio-ffmpeg` (secours extraction frame),
  Pillow. Pas de ffmpeg système dans l'env.
- ⚠️ Le CDN Seedance renvoie **403 sur le téléchargement** si on ne se présente pas
  comme un navigateur → `_download_bytes` envoie un User-Agent navigateur (comme YouTube).
- Option `--task-id <id>` : récupère l'image d'une tâche DÉJÀ générée sans repayer
  (utile si le download rate après une génération réussie).
- ✅ **Test payant fait (24/07/2026) : 2 fonds générés et validés visuellement** :
  - `pipeline/assets/backgrounds/guestlucky_bg.jpg` (navy + volutes violet/magenta, 720x900, 4:5)
  - `pipeline/assets/backgrounds/lesousloueur_bg.jpg` (navy + brume orange, sans violet, 720x900, 4:5)
  - Rendu premium éditorial, haut sombre dégagé pour le texte. Coût réel : 60 crédits/photo.
- **RESTE À FAIRE Étape 3** : brancher ces fonds dans build_guestlucky.py /
  build_lesousloueur.py (poser à ~50% opacité + overlay navy) au lieu du dégradé temporaire.

### ⚠️⚠️ PREUVE DÉFINITIVE (24/07/2026) : l'IMAGE Seedance est INACCESSIBLE au robot
Martin voulait ses vrais fonds "Nano Banana Pro" (flat-lay éditoriaux / visuels 3D,
faits sur le site Seedance en text-to-image). Investigation poussée :
- Le site utilise des routes internes `POST /api/image/{provider}/generate`
  (providers image : **fal**, kie, wavespeed). Modèles VALIDES sur fal :
  `nano-banana`, `nano-banana-pro`, `z-image`, `seedream-v4` (champ `modelId`).
- **MAIS ces routes exigent une SESSION connectée (cookies), PAS la clé API.**
  Testé : avec la clé Bearer, tout modèle image valide renvoie **401 Unauthorized**
  (`nano-banana-pro` → 401, `z-image` → 401, etc.). Un modèle inconnu renvoie 400
  "Unsupported model" (donc la validation modèle passe AVANT l'auth → preuve que
  l'auth par clé échoue). → **Le robot NE PEUT PAS générer d'image Seedance.**
- L'API "clé" de Seedance (`/v1/videos/generations`) = **VIDÉO uniquement**. Point.
- 🔑 **INSIGHT** : "Nano Banana Pro" est un **modèle de GOOGLE** (Gemini image).
  Seedance ne fait que le revendre. → Pour avoir EXACTEMENT ces fonds en automatique,
  appeler **Google directement** (Gemini API, `generativelanguage.googleapis.com`,
  joignable = 403 sans clé), avec un `GEMINI_API_KEY`. Même modèle, même qualité, clé-compatible.
- Décision en attente de Martin : (A) route Google Nano Banana Pro [recommandé,
  seule voie auto pour SA qualité] ; (B) réserve de fonds faits main sur le site Seedance
  + rotation par le robot. L'option "Seedance image par clé" est écartée (impossible, prouvé).

### PISTE RETENUE (24/07/2026) : fonds dessinés en HTML/CSS (gratuit, auto, 0 crédit)
Martin a proposé de faire les fonds en HTML. Excellent : le moteur rend déjà en
Playwright, donc on dessine des fonds premium en CSS et on les rend net (x3).
- Script : `pipeline/engine/bg_html.py` (Playwright + Chromium
  `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, viewport 1080x1350 x3).
  Styles : `mesh` (halos façon Stripe/Linear), `grid` (grille tech blueprint),
  `aurora` (bandes diagonales). Grain SVG feTurbulence + vignette. Palettes marque.
  `--all` génère les 6 (2 marques x 3 styles) dans assets/backgrounds/<marque>_html_<style>.jpg.
- Aussi `pipeline/engine/make_bg.py` : variante en PIL/numpy (halos + grain), au cas où.
- ⚠️ `pip install playwright` requis (le binaire Chromium est déjà présent, NE PAS
  faire `playwright install`). Rendu validé visuellement : très propre, haut sombre
  pour le texte, sur-marque. En attente : Martin choisit son style préféré.
- Prochaine étape : brancher le style choisi dans build_guestlucky.py / build_lesousloueur.py.

### ✅ ÉTAPE 3 TERMINÉE (24/07/2026) : fonds HTML branchés dans les slides
Décision Martin : un fond par marque, ses couleurs. Fonds dessinés en CSS directement
dans les build scripts (la div `.bg` de chaque slide), donc générés à chaque rendu,
0 crédit, 0 dépendance externe :
- **Guestlucky** : style "grid" (grille tech masquée) + halos violet #7c3aed / rose #ec4899
  sur navy, vignette (`.bg` + `.bg::before` grille + `.bg::after` vignette).
- **Le Sous Loueur** : style "mesh" (halos doux) orange #E8561F / bleu #2086C8 sur navy,
  vignette (`.bg` + `.bg::after`).
- Rendu des 2 démos validé visuellement : couvertures + slides de contenu, texte lisible,
  haut sombre, zéro débordement, zéro tiret. Gros gain vs l'ancien dégradé plat.
- Les fonds Seedance (guestlucky_bg.jpg, lesousloueur_bg.jpg) et les essais (make_bg/bg_html)
  restent dans assets/backgrounds/ comme références, mais NE sont plus utilisés (les slides
  dessinent leur fond en CSS). On peut ajuster couleurs/intensité à la demande.
- ⚠️ Dépendance rendu : `pip install playwright` (Chromium déjà présent, pas de playwright install).

**Étape suivante : Étape 4 — publication Metricool (token METRICOOL_TOKEN à fournir).**
⚠️ Metricool : forfait actuel de Martin = "Starter 5" → l'API n'est PAS incluse
(réservée Advanced/Custom). Décision d'upgrade en attente (Martin en parle avec le père).

## Démo de l'étape "écrire les carrousels" (24/07/2026) — le coeur du robot
À partir de la VRAIE dernière vidéo ("Airbnb tue le micro BIC", transcription Étape 2),
2 carrousels ADAPTÉS produits (même vidéo, 2 angles, jamais les mêmes slides) :
- `build_lsl_airbnb_microbic.py` (slug `lsl_airbnb_microbic`) : angle coaching / alerte
  réforme. Sujets : commission 15,5 % / coût réel 18,6 %, micro-BIC qui coule,
  calcul du prix ÷0,814, DAC7, micro vs réel + amortissement LMNP, décisions avant
  le 13 octobre. CTA : commenter **SIMULATEUR** (fichier micro vs réel).
- `build_gl_airbnb_direct.py` (slug `gl_airbnb_direct`) : angle produit Guestlucky.
  Sujets : hausse commission → dépendance risquée, réponse = réservation directe 0 %,
  channel manager natif, facturation électronique 2026 + loi Hoguet, tout-en-un.
  CTA : commenter **DIRECT** (⚠️ mot-clé NOUVEAU, pas dans la liste B2 : à valider
  avec Martin, sinon repli sur DEMO/OUTIL). Aucun concurrent nommé (mots bannis OK).
- Les 2 réutilisent les gabarits des moteurs (import, pas de duplication). Rendus :
  10 slides chacun, 0 débordement, 0 tiret, acronymes expliqués (BIC, TVA, DAC7, LMNP).
- C'est exactement l'étape que le robot fera seul chaque lundi (moi = le cerveau qui écrit).
- Descriptions Instagram écrites (PARTIE B) : `description.txt` dans chaque dossier de
  sortie. Règle apprise (Martin, 24/07) : **PAS d'emoji clé 🔑 à la fin des descriptions**
  (le 😉 après le CTA du haut reste). Package livré : 2 ZIP (10 JPG + description.txt).

## ⚙️ DÉCISION WORKFLOW (Martin, 24/07/2026) : mode SEMI-AUTO (Voie 2)
**« Claude prépare tout, Martin vient juste programmer. »**
⚠️ **DÉPASSÉ le 27/07/2026** : Martin ne programme plus non plus. Le Claude du Mac
s'en charge. Section gardée pour l'historique — voir « CHAÎNE 100% AUTOMATIQUE ».
- Pas d'API Metricool pour l'instant (forfait Starter 5, API réservée Advanced ;
  décision d'upgrade en discussion avec le père). L'Étape 4 (publication API) est en PAUSE.
- **Routine automatique du lundi** (trigger **`trig_01GTc5qL9sFLY2ZZ5tkcCTNh`**,
  cron `0 6 * * 1` UTC = lundi 8h Paris l'été, se déclenche dans CETTE session) :
  ⚠️ **27/07/2026 — Routine RECRÉÉE dans une nouvelle conversation.** L'ancienne
  (`trig_01BJ9PpUqznmkYP7XwEfUyG3`, session `session_01TEk97JnoYL2eRuncAvFmE8`) a été
  **supprimée avec delete_trigger** pour éviter que Martin reçoive le package en double.
  Une Routine est rattachée à UNE conversation : si on change de conversation, il faut
  recréer la Routine ET supprimer l'ancienne. Le prompt a été repris mot pour mot.
  Ne pas confondre avec `trig_018Re37nCRvKAFkHiXmcCbA3` = « Robot blog » de Sébastien
  (autre projet, autre repo) : **ne jamais y toucher**.
  ⚠️ Une Routine créée via MCP ne transporte pas de connecteurs (Gmail, Drive…).
  Sans importance ici : le robot n'utilise que Bash / Read / Write / SendUserFile.
  chaque lundi le robot fait TOUT seul : transcription dernière vidéo → 2 carrousels
  adaptés → 2 fonds générés par gemini_bg → rendu 20 slides + contrôles → 2 descriptions
  → slides affichées puis 2 ZIP envoyés à Martin (SendUserFile proactive) →
  **livraison.py sur les 2 carrousels (dépôt dans `livraison/`)** → commit/push
  (le push DOIT inclure `livraison/`) + mise à jour mémoire.
  ⚠️ Prompt mis à jour le 27/07/2026 : étape 8 = livraison GitHub, étape 9 = push,
  plus les règles gravées sur les marques Metricool.
  - Garde-fou anti-doublon : si pas de nouvelle vidéo (même id que dans
    output/transcripts/), prévenir et s'arrêter.
  - **Kill switch : Martin écrit STOP dans la conversation** (ou pause de la Routine
    dans l'interface claude.ai). Suppression : delete_trigger avec l'id ci-dessus.
- ⚠️ **OBSOLÈTE depuis le 27/07/2026** : Martin n'ouvre plus les ZIP et ne programme
  plus rien à la main. Voir « CHAÎNE 100% AUTOMATIQUE » ci-dessous.
- L'Étape 4 (publication Metricool par API depuis CET environnement) reste inutile :
  c'est le Claude du Mac qui programme, et `api.metricool.com` est de toute façon
  bloqué ici. Ne pas relancer ce chantier.

## 📅 DEUX VIDÉOS PAR SEMAINE (Martin, 29/07/2026) — DEUX RÉVEILS
Sébastien publie maintenant **2 vidéos/semaine** : dimanche + **mercredi 18h**.

| Réveil | Cron (UTC) | Heure Paris | Vidéo visée | Trigger |
|---|---|---|---|---|
| Lundi | `0 6 * * 1` | lundi 8h | celle du dimanche | `trig_01GTc5qL9sFLY2ZZ5tkcCTNh` |
| **Jeudi** | `0 6 * * 4` | jeudi 8h | celle du mercredi | `trig_01RsQkR98YD4J7LvMNMKq79S` |

Processus **strictement identique**. Le jeudi, il n'y a PAS toujours de vidéo :
dans ce cas le robot s'arrête sans rien produire ni dépenser, et le dit en une ligne.
Créneaux de publication (gérés par le Mac) : vendredi 18h et samedi 14h par marque.

### ✅ BLOCAGE YOUTUBE — RÉSOLU LE 10/08/2026 (solution trouvée par Martin)
**La parade : changer de PORTE D'ENTRÉE.** YouTube expose plusieurs clients
(site web, application Android, iPhone, télévision…). Quand l'un est fermé, un
autre reste souvent ouvert. On le choisit avec `player_client`.
```
yt-dlp --skip-download --write-auto-sub --sub-lang "fr.*" --sub-format json3 \
  --extractor-args "youtube:player_client=android" \
  -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=<ID>"
```
⚠️ **Deux détails indispensables, ne pas les perdre :**
1. `--sub-lang "fr.*"` (au SINGULIER, une expression). La liste explicite
   `--sub-langs "fr-orig,fr"` fait échouer la récupération sur plusieurs clients.
   **C'était la vraie cause du diagnostic raté du matin** : j'avais bien testé le
   client `android`, mais avec l'ancienne option de langue, et j'en ai conclu à
   tort qu'aucun client ne passait.
2. **La porte qui marche CHANGE avec le temps.** Aujourd'hui `android` ;
   demain ce sera peut-être `ios`. D'où la cascade automatique.

**Intégré dans `fetch_transcript.py`** : `get_transcript()` essaie les clients
dans l'ordre `android, ios, mweb, tv, web_safari, web` et s'arrête au premier qui
rapporte un fichier. ✅ Vérifié : la vidéo `URH12GYwAuc`, refusée le matin même,
a été récupérée automatiquement l'après-midi.

**Ce qui passe toujours, même bloqué** : `--flat-playlist` sur l'onglet /videos.
Donc `--verifier` fonctionne en toutes circonstances.

**Secours si un jour toutes les portes ferment** : le Claude du Mac récupère la
transcription (son adresse n'est pas bloquée) et la dépose dans
`pipeline/output/transcripts/` au format `<AAAAMMJJ>_<identifiant>.txt`.
`--verifier` répond alors « À REPRENDRE » et le robot repart tout seul.
✅ Circuit testé en vrai le 10/08 avec une transcription fournie par Martin.

### 🔴 ANCIEN CONSTAT DU 10/08 (conservé pour l'historique)
Le réveil du lundi 10/08 n'a pas pu récupérer la transcription : YouTube refuse
toute extraction de page vidéo depuis ce serveur avec « Sign in to confirm
you're not a bot ». Confirmé de façon indépendante par `youtube-transcript-api`
qui renvoie l'erreur explicite **`IpBlocked`**.

**Ce qui marche encore** : le LISTING de la chaîne (`--flat-playlist` sur
l'onglet /videos). Donc `--verifier` fonctionne : le robot voit qu'il y a une
nouvelle vidéo, il ne peut simplement pas la transcrire.

**Ce qui a été essayé sans succès** (ne pas refaire, c'est du temps perdu) :
- les 6 clients d'extraction : android, ios, tv, mweb, web_embedded, web_safari
- les moteurs JavaScript disponibles : `--js-runtimes node` et `--js-runtimes bun`
  (deno absent ; yt-dlp le réclame mais node et bun ne débloquent rien)
- mise à jour de yt-dlp : déjà en 2026.07.04, aucune version plus récente
- `youtube-transcript-api` : `IpBlocked`
- ⛔ NE JAMAIS installer curl_cffi pour tenter l'« impersonation » : règle du
  projet, ça casse yt-dlp derrière le proxy.

**Ce n'est pas un bug du code** : la même vidéo `URH12GYwAuc` se téléchargeait
sans problème le 06/08 et était refusée le 10/08. Le blocage vient de l'IP.

**Pistes de sortie, par ordre de préférence** :
1. **Le Claude du Mac récupère la transcription** : sa connexion n'est pas
   bloquée. Il pousserait le fichier dans `pipeline/output/transcripts/` au
   format `<AAAAMMJJ>_<identifiant>.txt`, et le robot repartirait de là
   (`--verifier` répondrait alors « À REPRENDRE »). C'est la solution durable.
2. Martin colle la transcription à la main dans la conversation.
3. Réessayer plus tard : le blocage a déjà été intermittent le 06/08.

### 🌍 PIÈGE DU TITRE TRADUIT (Martin, 29/07/2026) — RÈGLE GRAVÉE
**NE JAMAIS juger la langue ni le sujet d'une vidéo d'après son TITRE.**
YouTube renvoie les titres **traduits automatiquement selon la localisation du
serveur**. Depuis cet environnement (serveur à l'étranger), un titre français
arrive souvent en anglais. **Les vidéos sont TOUJOURS parlées en français.**

Cas réel du 29/07 : yt-dlp a renvoyé « Your HOA can block your Airbnb | Here's why ».
J'ai cru à une vidéo anglaise hors sujet et j'ai alerté Martin. **C'était faux** :
le vrai titre est « Ta copropriété peut te bloquer sur Airbnb | Voici pourquoi »,
vidéo française, en plein dans le thème.

**Ce qu'il faut faire à la place** : juger sur **la TRANSCRIPTION**, jamais sur le
titre. C'est sans risque, car `fetch_transcript.py` demande explicitement
`SUB_LANGS = "fr-orig,fr"` — la piste française d'origine, jamais une traduction.
La ligne « Titre : … » en tête du fichier transcript peut elle aussi être traduite :
**ne pas s'y fier non plus**, lire le corps du texte.

⛔ Ne JAMAIS bloquer ni questionner une vidéo à cause d'un titre en anglais.
✅ Ne s'arrêter pour demander que si le **corps de la transcription** n'est pas en
français, ou parle clairement d'autre chose que location courte durée / conciergerie.

### 🔴 ANTI-DOUBLON, 2e CORRECTION (30/07/2026) — il regardait la mauvaise chose
Le `--verifier` du 29/07 comparait l'identifiant de la vidéo aux fichiers de
`transcripts/`. Ça a lâché dès le premier vrai réveil : le jeudi 30/07, une erreur
529 de Google a interrompu le run **après** l'écriture de la transcription. Au
redémarrage, `--verifier` a répondu « DÉJÀ TRAITÉE » alors que **rien n'avait été
produit**. Sans l'intervention de Martin, le robot se serait tu pour toujours.

**Correction : le verdict se base désormais sur la LIVRAISON RÉELLE.**
- `livraison.py` gagne `video_livree(video_id)` : le contrôle qui fait autorité.
- Un registre `pipeline/output/traite.json` relie un identifiant de vidéo aux
  dossiers livrés. **Ce registre ne prouve rien tout seul** : pour chaque dossier
  annoncé, la fonction relit le disque et exige 10 images + `description.txt`,
  et exige que les DEUX marques soient présentes.
- `livraison.py <slug> --video <id> --titre "<titre>"` alimente le registre.
- Trois verdicts pour `--verifier` :
  - **DÉJÀ LIVRÉE** (code 1) : les carrousels existent et sont complets → stop.
  - **À REPRENDRE** (code 0) : transcription présente mais carrousels absents →
    reprendre à l'écriture, sans retélécharger la transcription.
  - **NOUVELLE** (code 0) : rien nulle part → run complet.
- ✅ 5 cas testés le 30/07 : livrée, transcript seul, une marque sur deux,
  registre qui annonce un dossier fantôme, dossier réel amputé d'une image.
  Les quatre derniers renvoient bien « à reprendre ».

### 🔴 BUG GRAVE TROUVÉ ET CORRIGÉ LE 29/07/2026 — l'anti-doublon ne marchait pas
`fetch_transcript.py` **écrit le transcript sans jamais vérifier s'il existe déjà**.
La consigne des robots était : « lance fetch_transcript.py puis compare l'identifiant
avec les fichiers de transcripts/ ». Or **après avoir lancé le script, l'identifiant
est TOUJOURS présent** — puisque le script vient de créer le fichier. Le robot aurait
donc conclu « déjà traitée » à CHAQUE fois, y compris pour une vraie nouvelle vidéo,
et n'aurait plus jamais rien produit. Le bug était invisible tant qu'il n'y avait
qu'une vidéo par semaine ; il devenait certain avec le réveil du jeudi.

**Correctif : nouveau mode `--verifier`** dans `fetch_transcript.py` :
```
python3 pipeline/engine/fetch_transcript.py --verifier
```
- ne télécharge rien, **n'écrit aucun fichier** → peut se relancer sans fausser le test
- cherche un fichier `*_<identifiant>.txt` dans `transcripts/`
- **code 0** = nouvelle vidéo à traiter
- **code 1** = déjà traitée → ne rien produire, ne rien dépenser
- **code 2** = PANNE (yt-dlp absent, réseau) → surtout NE PAS conclure « déjà traitée » :
  on ne SAIT PAS. Corriger et relancer.
⚠️ Les 3 codes sont distincts exprès : confondre une panne avec « rien à faire »
ferait taire le robot en silence pendant des semaines.
⚠️ Règle gravée dans les 2 prompts : **interdit de lancer `fetch_transcript.py`
sans `--verifier` tant qu'on n'a pas obtenu le code 0.**
✅ Testé en vrai le 29/07 : détection correcte, aucun fichier écrit, code panne validé.

## ✅ CHAÎNE 100% AUTOMATIQUE (Martin, 27/07/2026) — Martin ne fait PLUS RIEN
Le dernier maillon manuel a sauté. Répartition définitive du travail :

| Qui | Fait quoi | Quand |
|---|---|---|
| **Ce robot (cloud)** | vidéo → 2 carrousels design V2 → 2 fonds générés → rendu → 2 descriptions → dépôt dans `livraison/` → **push GitHub** | lundi 8h |
| **Claude du Mac** | `git pull` de `livraison/` → programme dans Metricool | vendredi 18h |
| **Martin** | **rien**. Il regarde les slides si ça lui chante. | — |

Programmation faite par le Mac : `lesousloueur-*` → marque **Sebastien More**
(sans accent, 3 réseaux) ; `guestlucky-*` → marque **guestlucky.off**.

### ⛔ Ce que ce robot ne doit PLUS écrire dans son message du lundi
- « les ZIP sont prêts à programmer », « pense à programmer vendredi 18h »,
  « télécharge les ZIP », « ouvre Metricool »… → **tout cela est FAUX désormais.**
- Le message du lundi dit simplement **ce qui a été livré** : les 2 noms de dossiers
  de `livraison/`, le résultat du contrôle, et quelle image de fond a servi.
- Le travail de ce robot **s'arrête au push GitHub**. Ce qui se passe après ne le
  regarde pas : c'est le Mac qui prend le relais.

## 📸 CIRCUIT PHOTOS DE FOND (Martin, 24/07/2026) : prompts Seedance faits main
Martin veut ses vrais fonds Nano Banana Pro (site Seedance) plutôt que les fonds CSS.
Circuit validé (intégré à la routine du lundi, trigger mis à jour) :
1. Chaque lundi, le robot écrit AUSSI **2 prompts Seedance** (un par marque, adaptés
   au sujet de la semaine, règles PARTIE D, cible 3500-4500 caractères comptés),
   sauvés en `seedance_prompt.txt` dans chaque dossier de sortie, envoyés avec les ZIP.
2. Martin (optionnel, quand il veut) : colle chaque prompt dans Seedance
   (AI Image → Nano Banana Pro → ratio 4:5 → 2K), renvoie les 2 photos ici.
3. Le robot : recadre 4:5, base64, fond des slides à ~45-50% + overlay navy (C1/C2),
   re-rend, renvoie les ZIP finaux.
4. Si Martin n'envoie rien : la version fonds CSS est déjà publiable (rien ne bloque).
Modèles de prompts : `pipeline/output/lsl_airbnb_microbic/seedance_prompt.txt`
(flat-lay éditorial navy/orange, zone haute vide) et
`pipeline/output/gl_airbnb_direct/seedance_prompt.txt` (still-life tech nuit
navy/violet/magenta, zone haute vide). Écrans toujours éteints, zéro texte lisible.

## Étape 2 — récupération transcription YouTube (FAITE, détails techniques)
- Script : `pipeline/engine/fetch_transcript.py` (aucune clé API requise).
- Outil retenu : **yt-dlp** (`pip install yt-dlp`). ⚠️ La petite lib
  `youtube-transcript-api` (plan A) se fait **bloquer par YouTube depuis un serveur
  cloud** (erreur RequestBlocked : IP data-center). yt-dlp (plan B) passe car il
  se présente comme un vrai navigateur. → toujours utiliser yt-dlp ici.
- **Vraies vidéos, PAS les shorts** (demande de Martin) : on lit l'onglet
  `/@moresebastien/videos` (exclut shorts + lives), `--playlist-items 1` = la plus récente.
- Transcription : sous-titres `fr-orig` (piste FR originale) sinon `fr`, format `json3`,
  parsé en texte propre (segments recollés avec espace pour éviter les mots collés).
- Sortie rangée dans `pipeline/output/transcripts/AAAAMMJJ_videoid.txt` (en-tête
  titre/date/durée/lien/chaîne + le texte). Ces .txt sont commités (contenu public).
- 1er test réussi (24/07/2026) : vidéo « Airbnb tue le micro BIC » (24min, 24329 car.).
  Sujets : commission Airbnb 15,5%/réel 18,6%, micro-BIC vs réel, DAC7, loi Le Meur,
  classement meublé de tourisme, réservation directe.
- ⚠️ La vidéo cite « Beds24 » = **mot banni côté Guestlucky** : à filtrer au moment
  de la création de contenu Guestlucky (jamais dans les slides publiées).

---

## 📝 Historique des sessions

### Session 1 — 24 juillet 2026
- Création du repo `CARROUSSEL-` et du fichier mémoire `carroussel.md`.
- Martin a fourni TOUT le contexte : les 3 marques (Le Sous Loueur, Guestlucky,
  Leapway), les règles de création de contenu (Le Sous Loueur + Guestlucky), les
  règles de community manager (descriptions/hooks/CTA des 3 marques), et les specs
  complètes de mise en page (Le Sous Loueur + Guestlucky, charte Leapway).
- Ajout de la PARTIE D : assistant de prompts visuels IA (Seedance / Magnific /
  Ideogram / Midjourney) avec les palettes strictes des 3 marques.
- Structure confirmée par Martin : 2 réseaux carrousels (Guestlucky, Le Sous Loueur)
  × 2 métiers (création de contenu + mise en page) = 4 prompts dédiés, + community
  manager + prompts visuels.
- Tout rangé dans ce fichier (PARTIES A / B / C / D + carte des prompts).
- **Logos reçus** (ZIP) : Guestlucky (détouré du fond navy → `pipeline/assets/logos/
  guestlucky.png`) et Le Sous Loueur version SOMBRE (`lesousloueur.png`). ⚠️ Il manque
  la **version BLANCHE de Le Sous Loueur** (pour les fonds navy). Guestlucky OK.
- **Moteur Guestlucky CONSTRUIT et FONCTIONNEL** : `pipeline/engine/build_guestlucky.py`
  (contenu + HTML des 10 slides, charte violet/rose C2) + `pipeline/engine/render.py`
  (Playwright → PNG 3240×4050 + JPEG 1080×1350 Metricool-ready, contrôle débordement +
  anti-tiret). Police Montserrat installée en local (`pipeline/assets/fonts/`, via npm
  @fontsource, car Google Fonts bloqué). Chromium lancé via `executable_path=
  /opt/pw-browsers/chromium-1194/chrome-linux/chrome` (mismatch de version, pas de
  `playwright install`).
- **1er carrousel de démo rendu** : `gl_demo_messagerie_ia` (Messagerie IA + Auto
  Actions), 10 slides, zéro débordement, zéro tiret, accents FR corrects. Fond
  TEMPORAIRE fait main (dégradé navy/violet) en attendant Seedance.
- **Prochaine étape** : retour de Martin sur la démo → ajustements ; brancher la vraie
  photo Seedance ; décliner le moteur pour Le Sous Loueur ; puis briques YouTube + Metricool.

---

### Session robot — lundi 27 juillet 2026 (1er run automatique RÉUSSI)
- Déclencheur du lundi 8h07 : premier réveil automatique, déroulé complet sans Martin.
- Vidéo du dimanche 26/07 détectée : « 220 000 € : le jugement qui fait trembler les
  concierges » (id YiAaGhoimhA, 27min50, transcription 30 008 car.). Sujets : conciergerie
  condamnée 220 000 € (autant que la propriétaire, 4 logements Paris 7e/8e, pas
  d'autorisation de changement d'usage, 410 000 € de recettes 2022-2024), loi Le Meur
  (intermédiaires sanctionnables jusqu'à 100 000 €), téléservice national/API meublés
  (mai 2026), 2 étages de sanctions (usage + enregistrement 12 500/50 000 ; loueur
  10 000/50 000, 120 jours/90 Paris), mythe de la carte G (défaut de vérification, pas
  de statut ; modèle prestation de services), 3 briques (contrat/doc, mode opératoire,
  outils/preuves), module conformité/gouvernance Guestlucky (fiche par bien, badges,
  rapport mensuel auto, accès propriétaire avancé, compteur de nuitées).
- 2 carrousels produits : `lsl_conciergerie_220k` (alerte/coaching, CTA LEMEUR) et
  `gl_conformite_lemeur` (produit module conformité, CTA DEMO). 20 slides, 0 débordement,
  0 tiret, montants en espaces insécables (leçon : le « € » seul en bout de ligne).
- 2 descriptions + 2 prompts Seedance (3984 et 4005 car.) + 2 ZIP livrés à Martin.
- ⚠️ Incident technique réglé : `curl_cffi` (installé pour un test jeudi) faisait planter
  les téléchargements yt-dlp derrière le proxy (Connection reset). → désinstallé.
  **Ne jamais installer curl_cffi dans cet environnement.**
- En attente : photos Seedance de Martin (optionnel) → re-rendu fonds ; sinon publiable tel quel.

### Session robot — lundi 17 août 2026 (run automatique, RÉUSSI malgré une panne Google)
- `--verifier` : verdict **NOUVELLE**. Vidéo `iVd1TQ-GUYs`, 20min48,
  « 8 astuces pour remplir votre Airbnb en basse saison (sans brader) ».
  Titre affiché par YouTube au moment de la récupération :
  « Remplir son Airbnb sans baisser les prix ? C'est possible ! » → **la langue a
  été vérifiée sur la transcription**, pas sur le titre (règle du 29/07).
- Transcription : 21 725 caractères. La porte `android` est passée au **3e tour**
  de la cascade — les deux premiers tours ont tout refusé. Les pauses servent.
- ⚠️ **Sujet volontairement recadré** : la vidéo du 03/08 traitait déjà « remplir
  sans baisser les prix » en général. Angle retenu ici : **la basse saison** et le
  **bail mobilité**. Toujours vérifier ce qui a déjà été livré avant de choisir
  l'angle, sinon on répète la semaine précédente.
- Contenu clé : les deux pièges du bradage (économique ET **algorithmique** —
  l'annonce apprend à la plateforme qu'elle est pas chère, remonter prend des
  mois) ; remises early bird et paliers 30/14/7 jours ; durée min 3 nuits ;
  nuits orphelines / bouche-trou ; calcul du mois plein (1 ménage au lieu de 6,
  scénario réel 40-50 % d'occupation, remise mensuelle 30-50 %) ; reconditionner
  l'annonce pour l'hiver (télétravailleurs, pas vacanciers) ; calendrier des
  événements que le revenue management ne voit pas à temps ; **bail mobilité
  (loi Elan 2018, 1 à 10 mois, non renouvelable) qui ne consomme PAS le quota de
  90/120 jours**.
- 2 carrousels livrés, 10 slides chacun, 0 débordement, 0 tiret long :
  `lesousloueur-2026-08-17-basse-saison-sans-brader` (CTA « HIVER ») et
  `guestlucky-2026-08-17-pilotage-basse-saison` (angle : la saison creuse, c'est là
  que les mandats se perdent — `cta_sans_commentaire()`, **règle 13 respectée**).
- Fonctions Guestlucky citées, aucune inventée : channel manager, remises last
  minute et bouche-trou (les deux nommées par Sébastien dans CETTE vidéo), plus
  rapports mensuels horodatés, documents par logement, historique des échanges,
  interface propriétaire (déjà établis).
- 🔴 **Panne Google d'une heure** sur `gemini-3-pro-image` → voir la section
  « PIÈGE HIGH DEMAND ». Résolu par une cascade de modèles désormais gravée dans
  `gemini_bg.py`. Le robot du jeudi n'aura plus à subir ça.
- Contrôles finaux verts : `livraison.py --controle` → « semaine complète, les 2
  marques sont livrées » ; `--verifier` → « DÉJÀ LIVRÉE, 2 dossiers vérifiés sur
  le disque ».

## 👁️ RÈGLE DE LIVRAISON (Martin, 27/07/2026) : TOUJOURS MONTRER LES SLIDES
Martin veut **voir le rendu de chaque slide**, pas seulement recevoir les ZIP.
À chaque livraison (hebdo automatique ou à la demande) :
1. Envoyer les **10 JPEG de chaque marque** via SendUserFile avec `display: "render"`
   (2 appels : un par marque, dans l'ordre slide_01 → slide_10, caption indiquant
   la marque + le CTA).
2. Puis (ou avant) les **ZIP** avec `display: "attach"`.
Ne jamais livrer uniquement les ZIP : les images d'abord, visibles dans la conversation.


## 🎙️ MESSAGES VOCAUX DE MARTIN (règle du 03/08/2026)
Martin envoie souvent des vocaux. On les transcrit nous-mêmes, en local.

**À refaire à CHAQUE session** (le conteneur repart de zéro, ~40 s) :
`pip install --quiet faster-whisper`

**Transcription** : `python3 pipeline/transcrire_vocal.py <fichier> [small|medium]`
ou en direct :
```
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8')
seg, _ = m.transcribe('vocal.opus', language='fr', vad_filter=True)
print(' '.join(s.text for s in seg))
```
- Lit .opus/.ogg (WhatsApp), m4a, mp3, wav, mp4. **ffmpeg inutile** (PyAV embarqué).
- **`vad_filter=True` OBLIGATOIRE** : sans lui Whisper invente du texte sur les
  silences (« Sous-titres réalisés par la communauté d'Amara.org »).
- Audio difficile ou jargon → relancer avec `'medium'` (plus lent, plus fidèle).
- ⚠️ **Whisper écorche les noms propres** : toujours relire, corriger, et
  SIGNALER à Martin ce qui a été rétabli. Corrections fréquentes :
  Gessuki/Guest Lucky → **GuestLucky** ; loi Lumur/Wemur → **loi Le Meur** ;
  CH manager/chemin majeur → **channel manager** ; micro BC → **micro-BIC** ;
  Bet 24 → **Beds24** (⚠️ mot banni en public) ; carte G, loi Hoguet, LMNP, DAC7.

## 🛡️ Règles de sauvegarde
- Mettre à jour ce fichier à chaque grosse étape / nouvelle règle apprise.
- Commit + push fréquents sur `claude/salut-af8y9u`.
- « Sauvegarde » = mise à jour + commit + push immédiat, sans débat.
- Aucun secret / clé API dans le code (repo public).

## 🎨 DESIGN V2 (Martin, 27/07/2026) : mise en page visuelle par SCHÉMAS
Martin a demandé de refaire totalement la mise en page : plus propre, avec des
**schémas et des cartes mentales** au lieu de listes de texte. Nouveau moteur :
`pipeline/engine/design_v2.py` (classe `Deck`), utilisé par les scripts `v2_*.py`.

**Briques visuelles disponibles** (une par slide de contenu) :
- `stats(...)` : blocs de gros chiffres (alterne accent 1 / accent 2)
- `timeline(...)` : chronologie verticale, l'étape clé marquée `hot=True`
- `flow(...)` : 3 étapes horizontales reliées par des flèches
- `mindmap(...)` : carte mentale, noyau central + 4 branches reliées (connecteurs SVG)
- `compare(...)` : 2 cartes rouge / vert (faux vs vrai, avant vs après)
- `checklist(...)` : lignes avec coche verte ou croix rouge
- `layers(...)` : étages empilés (piliers, briques, rôles)
- `pincer(...)` : tenaille, 2 contraintes qui convergent vers un bloc central
- plus `cover(...)`, `cta(...)`, `closing(...)`

**Choix de mise en page V2** :
- Titre BLANC + mot-clé en accent via `acc("mot")` (plus éditorial que le titre coloré).
- `eyebrow` (surtitre en accent 2) + gros chiffre éditorial en haut à droite.
- **Phrase d'intro obligatoire** (`lead=`) sous le titre : elle donne le contexte
  ET équilibre la composition (sans elle, gros vides).
- Hauteurs de blocs MAÎTRISÉES (`min-height` par brique) + visuel centré :
  ni grand vide, ni bloc démesuré. Leçon apprise en 3 itérations avec Martin.
- Carte mentale : noeuds du bas ancrés `bottom:0` (ils grandissent vers le haut,
  donc jamais de débordement sur le bandeau, quel que soit le nombre de lignes).
- Photo de fond via `deck.set_bg_photo(fichier, veil=0.82..0.88)` : monter le voile
  si la photo est claire (papiers blancs), baisser si elle est déjà sombre.

**Démos validées** : `v2_lsl_conciergerie_220k` et `v2_gl_conformite_lemeur`
(semaine du 27/07, 20 slides, 0 débordement, 0 tiret).
→ **Le robot du lundi utilise désormais design_v2.py** (ancien style conservé
dans build_guestlucky.py / build_lesousloueur.py pour référence).

## 🖼️ FONDS 100% AUTOMATIQUES via Google Nano Banana Pro (27/07/2026)
Objectif de Martin : ne plus JAMAIS générer les fonds à la main sur Seedance.

### Ce qui a été prouvé (ne pas re-tester)
- **Piloter un navigateur ici est impossible** : Playwright + Chromium se lancent,
  mais le réseau coupe le navigateur. Testé : Chromium via le proxy →
  ERR_CONNECTION_RESET (même sur un domaine autorisé) ; Chromium en direct →
  ERR_CERT_AUTHORITY_INVALID puis RESET. Seuls les domaines de l'allowlist
  (pypi.org…) répondent. curl/Python passent, Chromium non. Ce n'est pas un
  problème de code : c'est la politique réseau de l'environnement.
- **Seedance ne génère pas d'images par API** (401 sur /api/image/*/generate).
- → Voie retenue : **appeler Google directement**. "Nano Banana Pro" est un
  modèle Google que Seedance revend : même modèle, même qualité, clé-compatible.

### La brique : `pipeline/engine/gemini_bg.py`
- Modèle `gemini-3-pro-image`, format `4:5`, taille `2K`, sortie base64 → JPEG.
- Endpoint principal `POST /v1beta/interactions`, repli automatique sur
  `/v1beta/models/<model>:generateContent` (les deux formes sont gérées).
- Auth par en-tête `x-goog-api-key`, clé lue dans **GEMINI_API_KEY** (jamais en dur).
- `build_prompt(brand, theme)` écrit le prompt de la semaine (règles PARTIE D,
  palettes strictes par marque, zone haute vide, exclusions absolues).
- Modes : `--dry-run` (0 dépense, affiche le prompt) et `--go` (génère).
- **Coût officiel** : 0,134 $ par image 1K/2K, 0,24 $ en 4K, pas de palier gratuit.
  ≈ **1 $/mois** pour 8 fonds (2 carrousels/semaine). Facturation Google à activer.

### ⚠️ PIÈGE « HIGH DEMAND » SUR NANO BANANA PRO (constaté et corrigé le 17/08/2026)
**Ce qui s'est passé.** Au réveil du lundi 17/08, Google a refusé toute génération
pendant plus d'une heure : `500 / 503 — "gemini-3-pro-image is currently
experiencing high demand"`, sur les **deux** routes (`interactions` ET
`generateContent`). 12 relances espacées de 2 minutes : toutes refusées. La
variante `gemini-3-pro-image-preview` était saturée de la même façon.

**Ce qui a débloqué.** `gemini-3.1-flash-image` est passée **du premier coup**,
avec un rendu **conforme aux règles de la PARTIE D** (zone haute vide, objets en
bas, palette de la marque respectée). Vérifié à l'œil sur les deux fonds.

**La parade, désormais gravée dans le code.** `gemini_bg.py` contient une constante
`MODELS` et `generate_background()` parcourt la cascade dans cet ordre :
1. `gemini-3-pro-image` (Nano Banana Pro, choix par défaut, on ne dégrade jamais
   sans nécessité)
2. `gemini-3-pro-image-preview`
3. `gemini-3.1-flash-image` ← secours validé en conditions réelles
4. `gemini-2.5-flash-image`

Quand un modèle de secours est utilisé, le script l'affiche
(`modele de secours utilise : …`) : **le robot doit toujours dire quand il a
dégradé**, jamais le cacher.

**Deux points à retenir pour ne pas paniquer la prochaine fois :**
- Un appel refusé (500/503) n'est **PAS facturé**. Insister ne coûte rien. La
  règle 11 (« jamais de génération pour rien ») n'est donc pas violée par les
  relances : elle interdit de produire des images inutiles, pas de réessayer.
- Le plafond de temps d'une commande est de **10 minutes**. Pour attendre plus
  longtemps, lancer en arrière-plan et surveiller le journal.

**Défaut de rendu à surveiller sur les modèles flash.** Le 17/08, le premier fond
Guestlucky présentait une **couture horizontale nette** à ~29 % de la hauteur (une
bande plate en haut, puis la scène). Régénéré une fois → propre. Donc : **toujours
regarder le fond avant de construire le HTML**, la couture ne se voit pas dans les
logs. Une régénération pour remplacer un fond défectueux n'est pas une
« génération pour rien ».

### ⚠️ PIÈGE PLAYWRIGHT / CHROMIUM (corrigé le 27/07/2026)
`pip install playwright` installe la **dernière** version (1.61 → veut le build
`chromium-1228`), alors que l'environnement ne fournit que le build **1194**.
Résultat : `BrowserType.launch: Executable doesn't exist…` et Playwright réclame
`playwright install` — qui NE MARCHE PAS (téléchargement bloqué par le réseau).
**Correction appliquée dans `render.py`** : la fonction `find_chrome()` cherche le
binaire avec un glob `/opt/pw-browsers/chromium-*/chrome-linux/chrome` et prend le
build le plus récent, au lieu du chemin codé en dur. Si rien n'est trouvé, on laisse
Playwright se débrouiller. Le rendu survivra donc à une mise à jour de l'image.
✅ Revérifié : `python3 render.py lsl_conciergerie_220k` → 10 slides, 0 débordement.

### ✅ TEST PAYANT RÉUSSI (27/07/2026) : la chaîne fonds automatiques MARCHE
Première vraie génération lancée depuis une session avec `GEMINI_API_KEY` :
```
python3 pipeline/engine/gemini_bg.py --brand lesousloueur \
  --theme "a court ruling on short-term rental compliance" --out test_gemini.jpg --go
```
- Résultat : `pipeline/assets/backgrounds/test_gemini.jpg`, **1856×2304** (ratio 0,806,
  soit 4:5 à un cheveu près), JPEG RGB, 2,9 Mo. Coût réel : **0,134 $**.
- Endpoint qui a répondu : la chaîne `_payloads()` a abouti sans erreur (repli non nécessaire).
- **Qualité : équivalente à Nano Banana Pro sur Seedance, et pour cause : c'est le
  MÊME modèle** (`gemini-3-pro-image` = Nano Banana Pro, Seedance ne fait que le
  revendre). Flat-lay éditorial photo-réaliste, fond navy exact, orange limité à
  3 touches (stylo + trombones), zéro texte, zéro logo, zéro personne, objets dans
  le tiers bas, **haut de l'image sombre et dégagé** pour le titre blanc.
- ⚠️ **2 défauts mineurs constatés** (à corriger dans le prompt si ça se reproduit) :
  1. une **traînée de lumière** en haut à gauche, alors que COMMON_RULES interdit les
     « light shafts » : renforcer l'exclusion (ex. « NO haze, NO light streak,
     NO lens flare, NO fog in the upper zone »).
  2. la **pile de papiers est coupée au bord droit** malgré la consigne de marges :
     insister (« ALL objects fully inside the frame, nothing touching the edges »).
  Ni l'un ni l'autre ne gêne : sous le voile navy 0,82-0,88 du design V2, ça disparaît.
- ⚠️ Le ratio n'est pas 4:5 pile (0,8056) : `set_bg_photo` / le recadrage 4:5 reste
  nécessaire avant de poser la photo en fond.
- **Conclusion : plus besoin de passer par le site Seedance à la main. Étape « fonds »
  100 % automatique et validée.**

### Nouveau circuit hebdomadaire (plus aucune action de Martin sur les fonds)
Le robot du lundi : transcription → 2 carrousels → **écrit lui-même les 2 prompts
d'image et génère les 2 fonds via gemini_bg** → pose les fonds (design_v2
`set_bg_photo`) → rendu → descriptions → livraison (slides affichées + ZIP).
Martin ne fait plus rien du tout : le Claude du Mac programme (27/07/2026).
⚠️ Toujours indiquer en une ligne quelle image a été générée et utilisée.
⚠️ Si la génération échoue (quota, clé, refus) : s'arrêter proprement, le dire,
et livrer avec le fond CSS de secours plutôt que d'improviser.
