"""
Tests d'intégration de la route ``/`` et de l'interface HTML.

Utilise le client de test Flask (fixture ``client`` de ``conftest.py``)
pour simuler le navigateur, puis analyse le HTML rendu afin de vérifier
que chaque bouton affiche le caractère qu'il insère réellement.
"""

import re
from html.parser import HTMLParser

import pytest


class ButtonParser(HTMLParser):
    """
    Extrait les boutons de saisie de la calculatrice depuis le HTML rendu.

    Attributes:
        buttons: liste de tuples ``(valeur, libellé)`` où ``valeur`` est le
            caractère passé à ``appendToDisplay`` et ``libellé`` le texte
            visible sur le bouton.
    """

    def __init__(self):
        """Initialise le parseur et la liste de boutons trouvés."""
        super().__init__()
        self.buttons = []
        self._current_value = None
        self._current_label = ""

    def handle_starttag(self, tag, attrs):
        """
        Mémorise la valeur insérée par un bouton ``appendToDisplay('x')``.
        Args:
            tag: nom de la balise ouvrante.
            attrs: liste des attributs ``(nom, valeur)`` de la balise.
        """
        if tag != "button":
            return
        onclick = dict(attrs).get("onclick") or ""
        match = re.search(r"appendToDisplay\('(.)'\)", onclick)
        if match:
            self._current_value = match.group(1)
            self._current_label = ""

    def handle_data(self, data):
        """
        Accumule le texte visible du bouton en cours.
        Args:
            data: texte rencontré entre les balises.
        """
        if self._current_value is not None:
            self._current_label += data

    def handle_endtag(self, tag):
        """
        Enregistre le bouton en cours à la fermeture de ``</button>``.
        Args:
            tag: nom de la balise fermante.
        """
        if tag == "button" and self._current_value is not None:
            self.buttons.append((self._current_value, self._current_label.strip()))
            self._current_value = None


def _boutons_rendus(client):
    """
    Récupère les boutons de saisie de la page d'accueil.
    Args:
        client: client de test Flask.
    Returns:
        Un dictionnaire ``{valeur insérée: libellé affiché}``.
    """
    parser = ButtonParser()
    parser.feed(client.get("/").get_data(as_text=True))
    return dict(parser.buttons)


def test_get_index_affiche_la_calculatrice(client):
    """Un GET sur ``/`` doit répondre 200 avec l'interface et un afficheur vide."""
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'id="display"' in html
    assert 'value=""' in html


def test_post_expression_valide_affiche_le_resultat(client):
    """Un POST avec une expression valide doit afficher le résultat dans l'afficheur."""
    response = client.post("/", data={"display": "12+3"})
    assert response.status_code == 200
    assert 'value="15.0"' in response.get_data(as_text=True)


def test_post_expression_invalide_affiche_une_erreur(client):
    """Une expression invalide doit afficher un message d'erreur sans planter le serveur."""
    response = client.post("/", data={"display": "1+2+3"})
    assert response.status_code == 200
    assert "Error: only one operator is allowed" in response.get_data(as_text=True)


def test_post_division_par_zero_affiche_une_erreur(client):
    """La division par zéro doit être rapportée à l'utilisateur, pas causer une erreur 500."""
    response = client.post("/", data={"display": "5/0"})
    assert response.status_code == 200
    assert "Error:" in response.get_data(as_text=True)


def test_tous_les_boutons_sont_presents(client):
    """Les dix chiffres et les quatre opérateurs doivent avoir un bouton de saisie."""
    attendus = set("0123456789+-*/")
    assert set(_boutons_rendus(client)) == attendus


@pytest.mark.parametrize("valeur", list("0123456789+-*/"))
def test_libelle_du_bouton_correspond_a_sa_valeur(client, valeur):
    """
    Le texte affiché sur un bouton doit être le caractère qu'il insère.

    Un libellé différent (ex. « 02 » pour « 2 ») ou vide trompe
    l'utilisateur sur ce qu'il est en train de saisir.
    Args:
        client: client de test Flask.
        valeur: caractère inséré par le bouton testé.
    """
    assert _boutons_rendus(client).get(valeur) == valeur
