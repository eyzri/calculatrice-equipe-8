"""
Tests de la fonction ``calculate`` de ``app.py``.

Vérifie l'analyse d'une expression ``<nombre><opérateur><nombre>`` de bout
en bout : découpage, conversion des opérandes, appel du bon opérateur et
messages d'erreur pour les entrées invalides.
"""

import pytest

from app import calculate


@pytest.mark.parametrize(
    "expression, attendu",
    [
        ("12+3", 15),
        ("10-4", 6),
        ("5*6", 30),
        ("8/2", 4),
        ("7/2", 3.5),
    ],
)
def test_calculate_operations_valides(expression, attendu):
    """
    Chaque opérateur doit produire le résultat mathématique attendu.
    Args:
        expression: expression saisie par l'utilisateur.
        attendu: résultat correct de l'expression.
    """
    assert calculate(expression) == pytest.approx(attendu)


def test_calculate_ignore_les_espaces():
    """Les espaces autour des opérandes et de l'opérateur doivent être ignorés."""
    assert calculate(" 10 + 2 ") == 12


def test_calculate_nombres_decimaux():
    """Les opérandes décimaux doivent être acceptés."""
    assert calculate("1.5+2.25") == pytest.approx(3.75)


@pytest.mark.parametrize("expression", ["", None])
def test_calculate_expression_vide(expression):
    """Une expression vide ou absente doit lever ``ValueError``."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate(expression)


def test_calculate_plusieurs_operateurs():
    """Seul un opérateur binaire est supporté : ``1+2+3`` doit être refusé."""
    with pytest.raises(ValueError, match="only one operator"):
        calculate("1+2+3")


@pytest.mark.parametrize("expression", ["+5", "5+", "42"])
def test_calculate_format_invalide(expression):
    """
    Un opérateur en début/fin d'expression ou absent doit être refusé.
    Args:
        expression: expression sans deux opérandes autour de l'opérateur.
    """
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate(expression)


def test_calculate_operande_non_numerique():
    """Un opérande qui n'est pas un nombre doit lever ``ValueError``."""
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a+2")


def test_calculate_division_par_zero():
    """La division par zéro doit remonter ``ZeroDivisionError`` jusqu'à l'appelant."""
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")


@pytest.mark.parametrize(
    "expression, attendu",
    [
        ("-5+3", -2),
        ("5*-3", -15),
    ],
)
def test_calculate_operandes_negatifs(expression, attendu):
    """
    Un opérande négatif doit être accepté.

    Le ``-`` est actuellement toujours interprété comme l'opérateur de
    soustraction, ce qui empêche de saisir un nombre négatif. C'est aussi
    le cas quand on enchaîne un calcul sur un résultat négatif affiché.
    Args:
        expression: expression contenant un opérande négatif.
        attendu: résultat correct de l'expression.
    """
    assert calculate(expression) == pytest.approx(attendu)
