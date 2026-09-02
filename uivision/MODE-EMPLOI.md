# Captures d'écran avec UI.Vision — mode d'emploi

42 captures, entièrement automatisées. Compter ~5 minutes d'exécution.

## Avant de lancer : activer le mode disque dur

**Sans cette étape, rien ne marche** : le CSV ne sera pas lu et les images resteront
bloquées dans la mémoire de l'extension au lieu d'atterrir sur votre disque.

1. Installer l'extension **UI.Vision RPA** (Chrome ou Firefox)
2. Installer le module **FileAccess XModule** → https://ui.vision/rpa/x
3. Dans UI.Vision, onglet **XModule** → cocher **Hard Drive Storage**, choisir un dossier

UI.Vision crée alors cette arborescence :

```
UIVision/
├── datasources/    ← y déposer captures.csv
├── macros/         ← y déposer les deux .json
└── screenshots/    ← les 42 PNG arriveront ici
```

## Installation

| Fichier | Destination |
|---|---|
| `captures.csv` | `UIVision/datasources/` |
| `Captures-Entrepreneur-Augmente.json` | `UIVision/macros/` |
| `Captures-Viewport.json` | `UIVision/macros/` |

Les macros peuvent aussi s'importer par le bouton **Import** de l'extension.

## Lancement

1. Ouvrir la macro **Captures-Entrepreneur-Augmente**
2. **Ne pas cliquer sur Play.** Utiliser la flèche à côté de Play → **Loop**
3. Régler **From: 1** et **To: 42**
4. Lancer

Chaque boucle lit une ligne du CSV : `${!COL1}` = l'URL, `${!COL2}` = le nom du fichier.

> ⚠️ Le bouton **Play** seul ne traiterait que la première ligne. C'est l'erreur
> classique avec `csvRead` — la boucle est obligatoire.

## Les deux macros

**`Captures-Entrepreneur-Augmente`** (par défaut) — `captureEntirePageScreenshot` :
capture la page entière, du haut jusqu'en bas.

**`Captures-Viewport`** — `capturescreenshot` : capture seulement la partie visible
(la « fenêtre »). À utiliser si les pages pleines sont trop hautes pour être lisibles
en édition. Pour un livre, c'est souvent le meilleur choix : une page d'accueil complète
fait parfois 5000 px de haut et devient illisible une fois réduite à 15 cm.

## Ce que fait la macro à chaque page

1. `open` l'URL
2. `pause 4000` — laisse charger polices et images
3. Défilement jusqu'en bas — déclenche le chargement différé (lazy-load)
4. Remontée en haut, `pause 1500` — stabilise l'affichage
5. Capture sous le nom prévu

Ces temporisations évitent le défaut le plus courant : une capture prise avant la fin
du chargement, avec des zones vides à la place des images.

## Réglages utiles

**Fenêtre du navigateur** : mettez-la en 1440 px de large avant de lancer. La capture
reprend la taille réelle de la fenêtre — c'est ce qui garantit 42 images homogènes.

**Bandeaux cookies** : ils apparaîtront sur certaines captures. Deux options — les accepter
une première fois manuellement sur chaque site (le cookie est mémorisé), ou les retirer
ensuite dans un éditeur d'images.

**Si une page échoue** : notez son numéro de ligne, puis relancez en Loop From/To sur
cette seule ligne.

**Pages nécessitant un compte** (`claude.ai/new`, `chatgpt.com`, `gemini.google.com`) :
connectez-vous d'abord dans le navigateur, la session sera réutilisée. Sinon vous
capturerez l'écran de connexion — ce qui peut d'ailleurs suffire pour illustrer un livre.

## Ensuite

Déposez les 42 PNG dans un dossier du dépôt et signalez-le moi : je les intègre dans
les deux .docx, avec recadrage, légendes bilingues et placement au chapitre prévu.
Les noms de fichiers encodent déjà le chapitre (`ch14-supabase-01.png`), le placement
sera donc automatique.
