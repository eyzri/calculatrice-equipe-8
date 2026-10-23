"""
Tests unitaires du module ``operators``.

Chaque fonction arithmétique est vérifiée isolément, sans passer par
l'analyse d'expression de ``app.py``, afin qu'un échec pointe
directement vers la fonction fautive.
"""

import pytest

from operators import add, subtract, multiply, divide


def test_add_entiers():
    """``add`` doit retourner la somme de deux entiers positifs."""
    assert add(2, 3) == 5


def test_add_negatif_et_decimal():
    """``add`` doit gérer les opérandes négatifs et décimaux."""
    assert add(-4, 1.5) == pytest.approx(-2.5)


def test_subtract_ordre_des_operandes():
    """
    ``subtract(a, b)`` doit calculer ``a - b`` et non ``b - a``.

    Les opérandes sont choisis différents pour que l'inversion soit visible.
    """
    assert subtract(10, 4) == 6


def test_subtract_resultat_negatif():
    """``subtract`` doit retourner un résultat négatif si ``b > a``."""
    assert subtract(3, 8) == -5


def test_multiply_entiers():
    """
    ``multiply`` doit retourner le produit et non une puissance.

    2 * 3 = 6 alors que 2 ** 3 = 8 : distingue les deux opérations.
    """
    assert multiply(2, 3) == 6


def test_multiply_par_zero():
    """Tout nombre multiplié par zéro doit donner zéro."""
    assert multiply(7, 0) == 0


def test_divide_resultat_entier():
    """``divide`` doit retourner le quotient exact quand la division tombe juste."""
    assert divide(8, 2) == 4


def test_divide_resultat_decimal():
    """
    ``divide`` doit effectuer une division réelle, pas une division entière.

    7 / 2 = 3.5 alors que 7 // 2 = 3 : la partie décimale ne doit pas être perdue.
    """
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_par_zero():
    """La division par zéro doit lever ``ZeroDivisionError`` (comportement documenté)."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
