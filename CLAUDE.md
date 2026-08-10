## 🎙️ VOCAUX — transcrire les messages vocaux de Martin avec Whisper

> Demandé par Martin le 10/08/2026 — **à connaître dans TOUTES les conversations.**

Martin envoie souvent des vocaux. On sait maintenant les transcrire nous-mêmes.

**⚠️ Ce n'est PAS préinstallé** : le conteneur repart de zéro à chaque session,
il faut relancer l'installation (environ 40 secondes) :

```bash
pip install --quiet faster-whisper
```

**Transcrire** (script prêt à l'emploi : `pipeline/transcrire_vocal.py` du repo CARROUSSEL-) :

```bash
python3 transcrire_vocal.py vocal.ogg          # modele small (defaut, suffisant)
python3 transcrire_vocal.py vocal.ogg medium   # si l'audio est difficile
```

Ou directement, sans le script :

```bash
python3 -c "
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8')
seg, _ = m.transcribe('vocal.ogg', language='fr', vad_filter=True)
print(' '.join(s.text for s in seg))"
```

- **Formats lus** : ogg/opus (**le format des vocaux WhatsApp**), m4a, mp3, wav, mp4.
  Le décodage passe par PyAV : `ffmpeg` en ligne de commande n'est PAS installé,
  et ce n'est pas grave.
- **Toujours mettre `vad_filter=True`** : sans lui, Whisper invente du texte sur
  les silences (typiquement « Sous-titres réalisés par la communauté d'Amara.org »).
  Vérifié le 10/08/2026 : avec le filtre, le parasite disparaît.
- **Comment Martin envoie le vocal** : un fichier collé dans le chat n'arrive pas
  toujours comme vrai fichier côté Claude. La méthode sûre reste le **ZIP**
  (même règle que pour les images, cf. session 22 GuestLucky).

---

## 🎨 Visuels publicitaires Lucky Conciergerie

Tout est dans `pipeline/ads/lucky_conciergerie/` :

```
html/            une maquette par visuel + base.css (le design system)
assets/          fonds photo (generes via Gemini), logos, police Manrope
output/png       rendus haute definition (x2)
output/jpg       fichiers prets pour les regies pub (dimensions exactes)
render_ads.py    HTML -> PNG -> JPG, avec controle de debordement
```

**Regenerer les visuels** :
```bash
cd pipeline/ads/lucky_conciergerie
python3 render_ads.py              # tout
python3 render_ads.py D_performance # un seul concept
```
(prerequis : `pip install --quiet pillow playwright`)

**Formats** : story 1080x1920 · carre 1080x1080 · paysage 1200x628.

**Charte** (reprise du site luckyconciergerie.fr) : navy `#011640`,
or `#B08A3E`, creme `#F4ECDF`, police **Manrope**.

**12 angles** : A reseau · B mise en relation gratuite · C comparatif ·
D performance (+36 %) · E fondateur · F taux d'occupation · G zero souci ·
H espace proprietaire · I question directe · J proximite · K 3 etapes ·
L multi-diffusion.

⚠️ **Pieges verifies le 10/08/2026** :
- Le subset latin de Manrope ne contient NI la fleche → NI ✓ NI ✕ : ces
  caracteres s'afficheraient en carres vides. Toutes les icones sont donc
  en **SVG inline**. Ne jamais les remettre en texte.
- Les chiffres publicitaires (+36 %, +40 %, 82 %, 118 EUR) sont des
  **valeurs a confirmer par Martin** : une allegation chiffree doit pouvoir
  etre justifiee.
- Pas de photo generee par IA representant une personne reelle
  (Sebastien More) : le concept E utilise un medaillon avec ses initiales,
  a remplacer par sa vraie photo.
