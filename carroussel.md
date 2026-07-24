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

## 🔒 Règle de cloisonnement (IMPORTANTE)
Chaque conversation de travail reste **uniquement** sur ce que Martin y dit. On
ne pioche PAS d'infos d'autres conversations / projets, sauf s'il pose
explicitement la question. Ce fichier `carroussel.md` est la SEULE mémoire
partagée de référence.

## 🧠 Deux métiers distincts (ne pas confondre)
1. **Création de CONTENU** de carrousels (textes, structure, hiérarchie) → PARTIE A.
2. **Community manager** : descriptions Instagram/TikTok, hooks → PARTIE B.
3. **Mise en page** (design HTML/CSS → PNG via Playwright) → PARTIE C.
La création de contenu et la mise en page se font en général dans des
conversations séparées.

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
- **Photo de fond DEMANDÉE à chaque nouveau carrousel** : ne jamais réutiliser
  celle d'un précédent, ne jamais en inventer. Visible en filigrane (~45-50%).
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

## C7. Ce qu'il faut demander au début d'un carrousel de mise en page
1. Le logo officiel de la marque (PNG ; version blanche pour Le Sous Loueur).
2. La photo de fond du carrousel en cours.
(Guestlucky : + format du CTA slide 9.) Attendre que Martin ait tout envoyé avant
de commencer.

---

## 📝 Historique des sessions

### Session 1 — 24 juillet 2026
- Création du repo `CARROUSSEL-` et du fichier mémoire `carroussel.md`.
- Martin a fourni TOUT le contexte : les 3 marques (Le Sous Loueur, Guestlucky,
  Leapway), les règles de création de contenu (Le Sous Loueur + Guestlucky), les
  règles de community manager (descriptions/hooks/CTA des 3 marques), et les specs
  complètes de mise en page (Le Sous Loueur + Guestlucky, charte Leapway).
- Tout rangé dans ce fichier (PARTIES A / B / C).
- **Prochaine étape** : Martin envoie sa 1re source (transcription / thème) ou des
  slides à mettre en page. On applique directement les règles ci-dessus.

---

## 🛡️ Règles de sauvegarde
- Mettre à jour ce fichier à chaque grosse étape / nouvelle règle apprise.
- Commit + push fréquents sur `claude/salut-af8y9u`.
- « Sauvegarde » = mise à jour + commit + push immédiat, sans débat.
- Aucun secret / clé API dans le code (repo public).
