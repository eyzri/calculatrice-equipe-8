# Module `static/`

## Raison d'être

Ce répertoire regroupe les ressources statiques servies telles quelles
par Flask (CSS, et éventuellement images ou JS externes plus tard).
Il isole le style de l'application pour garder les gabarits HTML légers
et maintenables.

## Fichiers principaux

- **`style.css`** — Apparence de la calculatrice : mise en page centrée, thème sombre, grille de boutons 4×N, états hover/active, distinction visuelle des opérateurs.

### Détail de `style.css`

- **`body`** : fond clair et centrage flexbox plein écran.
- **`.calculator`** : conteneur sombre avec largeur maximale et ombre.
- **`#display`** : afficheur en lecture seule, texte aligné à droite.
- **`.buttons` / `.btn`** : grille 4 colonnes et style des touches.
- **`.operator`** : couleur orange pour les opérateurs et le bouton `=`.

## Dépendances et hypothèses

- Flask sert ce dossier via la route `/static/...` (convention par défaut
  lorsque `static/` est à la racine, à côté de `app.py`).
- Le template `templates/index.html` référence la feuille avec
  `url_for('static', filename='style.css')` — le nom de fichier doit
  rester cohérent.
- Aucun préprocesseur CSS ni bundler : le fichier est du CSS pur, chargé
  directement par le navigateur.
- Les classes CSS (`.calculator`, `.btn`, `.operator`, `#display`) sont
  contractuelles avec le markup de `index.html` ; les renommer exige
  une mise à jour des deux côtés.
