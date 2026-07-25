# PACK ÉLÈVES CONCIERGERIE — 30 visuels Instagram à personnaliser

> Pack "prêt à poster" pour les élèves : des conciergeries DÉJÀ LANCÉES dont
> l'objectif est de convaincre des PROPRIÉTAIRES de leur confier leur bien.
> 1 visuel = 1 post. 30 visuels = 3 mois de contenu (1 post tous les 3 jours).
>
> Règles du pack :
> - Le mot « gestion » est INTERDIT (et ses dérivés). On dit : s'occuper de,
>   prendre en charge, piloter, accompagner, confier.
> - Zéro emoji sur les visuels, zéro tiret long, Montserrat partout.
> - Style clair / éditorial (fond crème), volontairement neutre : chaque élève
>   remplace la couleur d'accent, le logo, la ville, le contact.
> - Zones en pointillés = à remplacer par l'élève. Textes préfixés « Exemple : »
>   = contenu d'exemple à adapter. Les posts conseils se postent tels quels.
> - Conseils Airbnb : à nourrir avec les vidéos YouTube de Sébastien qui parlent
>   du BUSINESS Airbnb (algorithme, annonces, photos, prix, avis), PAS des vidéos
>   sur « se lancer en conciergerie » (celles-là s'adressent aux élèves, pas aux
>   propriétaires).

## Moteur
- `engine/build_pack_conciergerie.py` : génère les HTML (dossier `output/pack_demo`).
- `engine/render.py pack_demo` : rend PNG HD + JPEG 1080x1350 prêts Instagram.
- Check automatique intégré : mot « gestion », tirets longs, emojis → build refusé.

## Les 30 posts (6 catégories)

### A. Identité et histoire (4 posts)
1. Pourquoi j'ai créé ma conciergerie (récit « Exemple : » à remplacer) — **FAIT (démo visuel 4)**
2. Qui s'occupe de votre bien : présentation de l'équipe / du fondateur
3. Nos valeurs : ce qu'on promet à chaque propriétaire
4. Les coulisses : une journée type entre deux séjours

### B. Offres et services (5 posts)
5. Nos services de A à Z (blocs « Exemple : » à remplacer) — **FAIT (démo visuel 2)**
6. Zoom service : votre annonce créée et optimisée
7. Zoom service : accueil des voyageurs et départs soignés
8. Zoom service : ménage professionnel et linge hôtelier
9. Là où on intervient : votre ville et ses alentours (carte / liste de zones)

### C. Conversion propriétaires (7 posts)
10. Pourquoi confier votre bien à une conciergerie — **FAIT (démo visuel 1)**
11. 5 signes qu'il est temps de déléguer votre location
12. « Ça coûte cher » : l'idée reçue passée au calcul (commission vs revenus optimisés)
13. Ce que vous récupérez : votre temps, chiffré heure par heure
14. Propriétaire à distance : louer sereinement sans être sur place
15. Comment ça se passe : les 4 étapes pour nous confier votre bien
16. Les questions à poser avant de confier son bien (et nos réponses)

### D. Conseils et astuces Airbnb, valeur pure (9 posts, source : vidéos YouTube business Airbnb)
> Matière détaillée post par post : `sources/youtube/BANQUE_CONSEILS.md`
> (extraite des 7 transcriptions de `sources/youtube/`, promos et contenus
> « conciergerie » filtrés).
17. Des photos qui font réserver votre bien — **FAIT (démo visuel 3)**
18. Le titre d'annonce qui arrête le scroll (formule + exemples)
19. Comment l'algorithme Airbnb classe votre annonce (et comment remonter)
20. Prix : pourquoi un tarif fixe toute l'année vous fait perdre de l'argent
21. La recette des avis 5 étoiles (avant, pendant, après le séjour)
22. Check-in sans friction : la première impression qui fait la note
23. Les équipements qui font vraiment la différence dans les recherches
24. Les 5 erreurs qui plombent une annonce (et comment les corriger)
25. Taux de réponse, annulations, note globale : les 3 chiffres à surveiller

### E. Preuve sociale (3 posts)
26. Témoignage propriétaire (gabarit citation, « Exemple : » à remplacer)
27. Nos chiffres : logements accompagnés, note moyenne, taux d'occupation (« Exemple : »)
28. Avant / après : une annonce reprise en main (photos, titre, résultats)

### F. Engagement (2 posts)
29. Vrai ou faux : 4 idées reçues sur la location courte durée
30. Question aux propriétaires : qu'est-ce qui vous empêche de louer ? (post conversation)

## État
- [x] Moteur + 4 visuels de démo (posts 1, 5, 10, 17) rendus et validés (zéro débordement).
- [x] Chaîne YouTube @moresebastien récupérée : 7 transcriptions business Airbnb
      + banque de conseils reliée aux posts 17-25 (`sources/youtube/`).
- [ ] Retour de Martin sur le style (fond clair, zones pointillées, accent terracotta).
- [ ] Produire les 26 visuels restants après validation.
- [ ] Option à discuter : livrer aussi une version Canva pour que les élèves modifient
      facilement (les JPEG ne sont pas éditables par eux).
