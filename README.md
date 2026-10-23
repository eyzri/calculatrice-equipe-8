# Calculatrice Flask — Équipe 8

**Cours :** LOG3000 

## Description du projet

Application web de calculatrice simple construite avec **Flask**.  
L'utilisateur compose une expression binaire (deux nombres et un opérateur
parmi `+`, `-`, `*`, `/`) via une interface graphique dans le navigateur.
Le serveur analyse l'expression, délègue le calcul au module
`operators`, puis affiche le résultat (ou un message d'erreur).

### Portée

**Inclus :**
- Opérations binaires `+`, `-`, `*`, `/`
- Interface web responsive basique
- Gestion d'erreurs d'expression
- Analyse d'une chaîne `nombre op nombre`

**Hors portée (pour l'instant) :**
- Expressions avec plusieurs opérateurs
- Priorité des opérateurs et parenthèses
- Authentification et base de données
- Historique des calculs

## Structure du projet

```
.
├── app.py                 # Serveur Flask, analyse d'expression, routes
├── operators.py           # Fonctions add / subtract / multiply / divide
├── templates/
│   ├── README.md          # Documentation du module templates
│   └── index.html         # Interface utilisateur (HTML + JS)
├── static/
│   ├── README.md          # Documentation du module static
│   └── style.css          # Styles de l'interface
└── README.md              # Ce fichier
```

Chaque sous-répertoire possède son propre `README.md` décrivant sa
raison d'être, ses fichiers et ses hypothèses. Consultez-les pour
naviguer rapidement dans le code.

- **`app.py`** — Point d'entrée : configure Flask, expose la route `/`, parse l'expression (`calculate`)
- **`operators.py`** — Opérations arithmétiques appelées après le parsing
- **`templates/`** — Gabarits Jinja2 rendus côté serveur
- **`static/`** — Ressources CSS (et autres assets statiques)

## Prérequis

- **Python** 3.8 ou plus récent
- **pip** (gestionnaire de paquets Python)
- **Git**
- Un navigateur web moderne (Chrome, Firefox, Safari, Edge, …)

## Installation (étape par étape)

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/eyzri/calculatrice-equipe-8.git
   cd calculatrice-equipe-8
   ```

2. **Créer et activer un environnement virtuel** (recommandé)

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate           # Windows
   ```

3. **Installer les dépendances**

   ```bash
   pip install flask
   ```

   Si un fichier `requirements.txt` est ajouté plus tard :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Lancer l'application

Depuis la racine du projet, avec l'environnement virtuel activé :

```bash
python3 app.py
```

Le serveur démarre en mode debug sur **http://127.0.0.1:5000**.

Ouvrez cette URL dans votre navigateur. Pour arrêter le serveur, faites
`Ctrl + C` dans le terminal.

### Utiliser la calculatrice

1. Cliquez sur les boutons numériques pour saisir le premier opérande.
2. Cliquez sur un opérateur (`+`, `-`, `*`, `/`).
3. Saisissez le second opérande.
4. Appuyez sur `=` pour envoyer l'expression au serveur et afficher le résultat.
5. Appuyez sur `C` pour effacer l'afficheur et recommencer.

**Exemples d'expressions valides :** `12+3`, `10-4`, `5*6`, `8/2`

**Cas d'erreur affichés à l'écran :** expression vide, format invalide,
plusieurs opérateurs, opérandes non numériques, etc.

> L'afficheur est en lecture seule : la saisie se fait uniquement via les boutons.

## Tests

Les tests automatisés utilisent **pytest** et se trouvent dans `tests/`
(voir [`tests/README.md`](tests/README.md) pour le détail de la couverture).

1. Installer les dépendances (Flask et pytest) :

   ```bash
   pip install -r requirements.txt
   ```

2. Exécuter toute la suite depuis la racine du projet :

   ```bash
   pytest
   ```

3. Afficher plus de détails en cas d'échec :

   ```bash
   pytest -v
   ```

Les tests couvrent :

- les fonctions de `operators.py` (résultats attendus, cas limites) ;
- la fonction `calculate` dans `app.py` (parsing, validation, erreurs) ;
- la route Flask `/` (requêtes GET/POST) et les libellés des boutons de l'interface.

## Flux de contribution

Ce projet suit un flux Git collaboratif classique. Tout le monde travaille
à partir de `main` via des branches de fonctionnalités et des pull requests.

### Branches

- **`main`** — Branche stable ; ne jamais y pousser directement du travail non revu
- **`feature/<nom>`** — Nouvelle fonctionnalité (ex. : `feature/historique`)
- **`fix/<nom>`** — Correction de bogue (ex. : `fix/division-entiere`)
- **`docs/<nom>`** — Documentation uniquement (ex. : `docs/readme`)
- **`test/<nom>`** — Ajout ou correction de tests

### Workflow recommandé

1. **Mettre à jour `main` localement**

   ```bash
   git checkout main
   git pull origin main
   ```

2. **Créer une branche** pour votre tâche

   ```bash
   git checkout -b feature/ma-tache
   ```

3. **Développer, committer** avec des messages clairs

   ```bash
   git add .
   git commit -m "Description concise du changement"
   ```

4. **Pousser la branche** et ouvrir une pull request

   ```bash
   git push -u origin feature/ma-tache
   ```

   Puis créer une PR vers `main` sur GitHub (titre clair, description
   du problème et de la solution, lien vers l'issue si applicable).

5. **Revue de code** : au moins un autre membre de l'équipe valide
   avant le merge.

6. **Merge** dans `main`, puis suppression de la branche de travail.

### Issues

- Ouvrir une **issue** pour chaque bogue, tâche ou amélioration.
- Utiliser des libellés si disponibles (`bug`, `documentation`, `enhancement`).
- Référencer l'issue dans les commits / la PR (`Fixes #12`, `Related to #5`).
- Assigner un responsable et préciser les critères d'acceptation quand c'est pertinent.

### Bonnes pratiques

- Une PR = un objectif clair .
- Ne pas committer de secrets (`.env`, mots de passe, clés API).
- Documenter le code (docstrings, commentaires utiles) en même temps
  que les changements fonctionnels.
- Faire passer les tests localement avant de demander une revue.

## Auteurs

Équipe 8 — LOG3000
