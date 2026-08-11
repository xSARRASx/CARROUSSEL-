# carroussel.md — Mémoire du projet Carrousels Instagram

> Fichier mémoire relu au début de chaque session. Il regroupe TOUT le contexte,
> les règles et les specs pour créer et mettre en page les carrousels Instagram
> des marques de Sébastien More.
> Pour reprendre : "lis le carroussel.md et continuons".
>
> Repo : `xSARRASx/CARROUSSEL-` — branche de dev : `claude/salut-af8y9u`

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

## 🎙️ TRANSCRIRE LES VOCAUX DE MARTIN (méthode validée, 24/07/2026)
Martin envoie souvent des messages vocaux. Whisper tourne EN LOCAL (pas d'API).

1. **À réinstaller à CHAQUE session** (le conteneur repart de zéro, ~40 s) :
   `pip install --quiet faster-whisper`
2. **Transcrire** (script prêt : `pipeline/transcrire_vocal.py`) :
   `python3 pipeline/transcrire_vocal.py vocal.ogg` (ou `... vocal.opus medium`)
   Équivalent direct :
   ```python
   from faster_whisper import WhisperModel
   m = WhisperModel('small', device='cpu', compute_type='int8')
   seg, _ = m.transcribe('LE_FICHIER.opus', language='fr', vad_filter=True)
   print(' '.join(s.text for s in seg))
   ```

Règles :
- Lit directement les vocaux WhatsApp (.opus/.ogg) + m4a, mp3, wav, mp4.
  **Pas besoin de ffmpeg** (non installé) : le décodage passe par PyAV.
- **`vad_filter=True` TOUJOURS.** Sans lui, Whisper invente du texte sur les
  silences (ex. « Sous-titres réalisés par la communauté d'Amara.org »).
- Audio difficile ou jargon → relancer avec **`medium`** au lieu de `small`
  (plus lent, bien plus fidèle).
- Whisper **écorche les noms propres et termes métier** (GuestLucky, Beds24,
  Metricool, Seedance, loi Hoguet, LuckyCover, Leapway, PriceLabs...). Toujours
  relire, corriger, et **signaler à Martin ce qui a été rétabli**.
- Vérifié le 24/07/2026 : le modèle se télécharge bien depuis HuggingFace même
  avec la politique réseau « Trusted » ; test à vide → aucune hallucination.

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

**GuestLucky :**
```
Commente "MOT" ↓ et [ce qu'ils reçoivent] 😉

[Contexte en 2-3 phrases]

[Valeur / fonctionnalité clé]

Commente "MOT" ↓ et [CTA final] 🔑
```

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

**GuestLucky :**
- OUTIL → lien tester gratuitement
- HOGUET → checklist conformité 12 points
- CAUTION → guide caution + checklist
- IA → 10 scénarios Auto Actions
- DEMO → démo gratuite 30 minutes
- AUDIT → audit gratuit annonce Airbnb

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
  - Le Sous Loueur (compte « Sebastien More ») : blogId = 3968518
  - Guestlucky (compte « guestlucky.off ») : blogId = 4001072
- **Seedance** : base URL https://api.seedance2.ai, auth Bearer, génération async
  (orienté vidéo ; vérifier l'endpoint AI Image pour les photos de fond).

## Workflow cible (précisé par Martin, 24/07/2026)
Cadence **hebdomadaire, 100% autonome** :
- Une vidéo sort **chaque dimanche** sur une chaîne YouTube (URL à fournir par Martin).
- **Chaque lundi** : le robot récupère tout seul la transcription → fabrique **DEUX**
  carrousels **adaptés** à partir de la même vidéo :
  - 1 pour **Guestlucky** (angle « ce qu'on vend », palette/logo/CTA Guestlucky),
  - 1 pour **Le Sous Loueur** (son angle, palette/logo/CTA Le Sous Loueur).
- Programmation **vendredi 18h** sur l'Instagram de Guestlucky ET celui de Le Sous
  Loueur, via **Metricool**.

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
- **Étape 1 (le cœur, se construit ici sans réseau)** : moteur de création
  (contenu → photo → 10 slides Playwright → JPEG Metricool-ready). Testé avec Martin.
- **Étape 2** : brique « récupérer la transcription YouTube » (dans l'env. à réseau ouvert).
- **Étape 3** : brique « publication Metricool » (d'abord brouillon programmé, pour vérifier).
- **Étape 4** : déclencheur hebdo (lundi) + filet de sécurité (contrôle qualité auto +
  journal des posts + kill switch) → tourne sans surveillance.

**Étape en cours : Étape 1 — construire le moteur de carrousels (démarre par Guestlucky).**
Prérequis immédiats : ZIP des logos + URL de la chaîne YouTube.

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

## 🛡️ Règles de sauvegarde
- Mettre à jour ce fichier à chaque grosse étape / nouvelle règle apprise.
- Commit + push fréquents sur `claude/salut-af8y9u`.
- « Sauvegarde » = mise à jour + commit + push immédiat, sans débat.
- Aucun secret / clé API dans le code (repo public).
