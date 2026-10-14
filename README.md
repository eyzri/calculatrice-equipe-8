# Calculatrice Flask

**Cours :** LOG3000, Polytechnique Montréal
**Équipe :** 8

## Objectif

Application web de calculatrice simple construite avec Flask. L'utilisateur entre une opération avec deux nombres et un opérateur (`+`, `-`, `*`, `/`) dans l'interface, et le serveur calcule et affiche le résultat.

Ce dépôt sert à structurer le projet : gestion de versions, documentation du code, tests et correction de bogues.

## Structure du projet

```
.
├── app.py           # Serveur Flask et analyse de l'expression
├── operators.py     # Fonctions des opérations mathématiques
├── templates/
│   └── index.html   # Interface utilisateur
└── static/
    └── style.css    # Style de l'interface
```

## Prérequis

- Python 3.8 ou plus récent
- pip
- Git

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/eyzri/calculatrice-equipe-8.git
   cd calculatrice-equipe-8
   ```

2. (Optionnel) Créer et activer un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate           # Windows
   ```

3. Installer Flask :

   ```bash
   pip install flask
   ```

## Lancer l'application

```bash
python3 app.py
```

Ouvrir ensuite http://127.0.0.1:5000 dans un navigateur.

Pour arrêter le serveur, faire `Ctrl + C` dans le terminal.
