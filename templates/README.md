# Module `templates/`

## Raison d'être

Ce répertoire contient les gabarits HTML rendus par Flask via Jinja2.
Il sépare la présentation (markup et interactions côté navigateur) de la
logique serveur située dans `app.py`.

## Fichiers principaux

- **`index.html`** — Interface unique de la calculatrice : formulaire POST, grille de boutons, champ d'affichage et scripts JavaScript pour construire l'expression avant envoi.

### Détail de `index.html`

- **Formulaire** : envoie le contenu du champ `display` à la route `/`
  (méthode POST). Après calcul, Flask réinjecte le résultat via
  `{{ result }}`.
- **Boutons numériques / opérateurs** : appellent `appendToDisplay(value)`
  pour concaténer le caractère choisi à l'afficheur (sans recharger la page).
- **Bouton `=`** : type `submit` — déclenche l'envoi du formulaire au serveur.
- **Bouton `C`** : appelle `clearDisplay()` pour vider l'afficheur.
- **Styles** : liés via `url_for('static', filename='style.css')`.

## Dépendances et hypothèses

- Flask doit pouvoir trouver ce dossier (emplacement par défaut :
  `templates/` à la racine du projet, à côté de `app.py`).
- La variable de template `result` est toujours fournie par la vue
  `index()` dans `app.py` (chaîne vide en GET, résultat ou message
  d'erreur en POST).
- Le JavaScript suppose la présence d'un élément `#display` dans le DOM.
- Aucune dépendance npm : le JS est inline et autonome.
