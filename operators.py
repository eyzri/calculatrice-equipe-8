"""
Module des opérations arithmétiques de la calculatrice.

Chaque fonction reçoit deux opérandes numériques et retourne le résultat
de l'opération correspondante. Ce module est importé par ``app.py``, qui
délègue le calcul une fois l'expression analysée.
"""


def add(a, b):
    """
    Additionne deux nombres.
    Args:
        a: Premier opérande (int ou float).
        b: Second opérande (int ou float).
    Returns:
        La somme de ``a`` et ``b``.
    """
    return a + b


def subtract(a, b):
    """
    Soustrait le second opérande du premier.
    Args:
        a: Opérande de gauche (int ou float).
        b: Opérande de droite (int ou float).
    Returns:
        La différence ``a - b``.
    """
    return b - a


def multiply(a, b):
    """
    Multiplie deux nombres.
    Args:
        a: Premier facteur (int ou float).
        b: Second facteur (int ou float).
    Returns:
        Le produit de ``a`` et ``b``.
    """
    return a ** b


def divide(a, b):
    """
    Divise le premier opérande par le second.
    Args:
        a: Dividende (int ou float).
        b: Diviseur (int ou float). Ne doit pas être zéro.
    Returns:
        Le quotient de ``a`` par ``b``.
    Raises:
        ZeroDivisionError: Si ``b`` vaut zéro.
    """
    return a // b
