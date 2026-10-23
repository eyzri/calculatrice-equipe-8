# Module `tests/`

## Raison d'être

Ce répertoire contient la suite de tests automatisés de la calculatrice.
Elle sert à détecter les bogues de la logique de calcul et de l'interface,
et à vérifier qu'un correctif règle bien le problème sans en créer d'autres.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `conftest.py` | Configuration partagée : ajoute la racine du projet au `sys.path` et fournit la fixture `client` (client de test Flask). |
| `test_operators.py` | Tests unitaires de `add`, `subtract`, `multiply` et `divide` (`operators.py`), appelées directement. |
| `test_calculate.py` | Tests de `calculate` (`app.py`) : expressions valides, espaces, décimaux, opérandes négatifs et toutes les erreurs de validation. |
| `test_routes.py` | Tests d'intégration de la route `/` (GET et POST) et vérification que chaque bouton de `templates/index.html` affiche le caractère qu'il insère. |
| `__init__.py` | Marque le répertoire comme paquet Python. |

## Exécuter les tests

Depuis la racine du projet, avec l'environnement virtuel activé :

```bash
pip install -r requirements.txt             # installe flask et pytest
python -m pytest                            # lance toute la suite
python -m pytest -v                         # affiche chaque test individuellement
python -m pytest tests/test_operators.py    # lance un seul fichier
python -m pytest -k divide                  # lance les tests dont le nom contient "divide"
```

## Couverture

| Zone | Ce qui est vérifié |
|---|---|
| Opérations | Résultat de chaque opération, ordre des opérandes (`a - b`), multiplication et non puissance, division réelle et non entière, division par zéro. |
| Analyse d'expression | Les 4 opérateurs, espaces ignorés, nombres décimaux et négatifs, expression vide, plusieurs opérateurs, opérateur mal placé ou absent, opérande non numérique. |
| Route `/` | GET (page rendue, afficheur vide), POST valide (résultat affiché), POST invalide et division par zéro (message `Error:` sans erreur 500). |
| Interface | Présence d'un bouton par chiffre et par opérateur, et libellé de chaque bouton identique à la valeur insérée. |

Hors couverture : le JavaScript côté client (`appendToDisplay`, `clearDisplay`)
et le rendu CSS, qui nécessiteraient un navigateur (ex. Selenium/Playwright).

## Hypothèses

- Les tests sont lancés depuis la racine du projet ou depuis `tests/`
  (`conftest.py` gère le chemin d'import dans les deux cas).
- Les résultats décimaux sont comparés avec `pytest.approx` pour éviter
  les faux échecs dus à l'arrondi des flottants.
- Un test en échec signale un bogue dans le code de l'application, pas
  dans le test : chaque échec correspond à une issue GitHub.
