"""
Configuration partagée par tous les tests pytest.

Ajoute la racine du projet au ``sys.path`` pour que les tests puissent
importer ``app`` et ``operators`` peu importe le répertoire depuis lequel
``pytest`` est lancé, et fournit le client de test Flask.
"""

import os
import sys

import pytest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import app as flask_app  # noqa: E402  (import après ajustement du path)


@pytest.fixture
def client():
    """
    Fournit un client de test Flask pour simuler des requêtes HTTP.
    Returns:
        Un ``FlaskClient`` lié à l'application en mode ``TESTING``,
        ce qui propage les exceptions au lieu de renvoyer une page 500.
    """
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as test_client:
        yield test_client
