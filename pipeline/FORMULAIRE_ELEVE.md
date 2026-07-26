# Questionnaire élève — pack Instagram personnalisé (10 questions simples)

> L'élève répond à ces questions (Google Form, WhatsApp ou mail). On remplit un
> fichier profil (`profiles/prenom_nom.json`) avec ses réponses, on lance le
> moteur, et il reçoit SON pack déjà personnalisé : rien à modifier de son côté.
> 30 élèves = 30 packs différents (couleur, ville, histoire, services, textes).
>
> Commande : `python3 engine/build_pack_conciergerie.py profiles/eleve.json`
> puis `python3 engine/render.py <slug>`.

## Les 10 questions

1. **Le nom de ta conciergerie** (exactement comme tu veux qu'il s'affiche)
2. **Ton compte Instagram** (ex : @capocean.conciergerie)
3. **Ta ville et ta zone d'intervention** (ex : La Rochelle · Île de Ré)
4. **Ton site OU ton moyen de contact préféré** (site, téléphone, ou "message privé Instagram")
5. **Ta couleur de marque** (code hexadécimal si tu l'as, sinon envoie ton logo
   et on la récupère ; sinon dis juste "bleu marine", "vert forêt"...)
6. **Ton logo** en PNG fond transparent (optionnel : sinon ton nom stylisé fait le travail)
7. **Ton histoire en 3 phrases** : ton déclic, ton premier logement, où tu en es
   aujourd'hui (réponds naturellement, on met en forme)
8. **Tes 4 services principaux** (ex : annonce, accueil, ménage/linge, prix dynamiques,
   petit-déjeuner, spa... ce que TU proposes vraiment)
9. **Un chiffre dont tu es fier** (nombre de logements, note moyenne, avis 5 étoiles,
   années d'expérience...) : pour les posts preuve sociale
10. **Un avis d'un propriétaire ou d'un voyageur** (copié-collé, avec le prénom) :
    pour le post témoignage

## Ce que ça change sur les visuels (mode "perso" du moteur)
- Le bandeau pointillé « Ton logo ici » devient un bloc au NOM de la conciergerie
  dans SA couleur (ou son logo quand il est fourni).
- « @ta.conciergerie », « Ta ville + ta zone », « Ton site ou ton contact »
  sont remplacés par ses vraies infos.
- La couleur d'accent terracotta est remplacée partout par SA couleur.
- Les encadrés « À personnaliser » deviennent une signature :
  « Nom · Ville » en pied de visuel.
- Les textes variables (histoire, services, témoignage, chiffres) sont les siens :
  les étiquettes « Exemple : » disparaissent.
- Les posts conseils gardent le même fond d'expertise (c'est le but du pack) mais
  portent la marque de l'élève ; on peut varier les formulations de titres d'un
  élève à l'autre pour éviter les doublons entre comptes.

## Règles conservées quel que soit l'élève
- Le mot « gestion » reste interdit (le moteur refuse de générer s'il apparaît,
  y compris dans leurs réponses : on reformule alors avec eux).
- Zéro emoji sur les visuels, zéro tiret long, Montserrat partout.
