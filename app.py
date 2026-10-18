"""
Point d'entrée de l'application web Calculatrice Flask.

Ce module configure le serveur Flask, analyse les expressions saisies
par l'utilisateur et délègue le calcul aux fonctions de ``operators``.
Lancer avec ``python3 app.py`` pour démarrer le serveur en mode debug
sur http://127.0.0.1:5000.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Association symbole d'opérateur a fonction de calcul correspondante
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """
    Analyse une expression binaire simple et calcule le résultat.

    L'expression attendue est de la forme ``<nombre><opérateur><nombre>``,
    par exemple ``12+3`` ou ``10 / 2``. Les espaces sont ignoré.
    Un seul opérateur parmi ``+``, ``-``, ``*``, ``/`` est autorisé.
    Args:
        expr: chaîne représentant l'expression à évaluer.
    Returns:
        Le résultat numérique de l'opération (int ou float selon les
        opérandes et l'opérateur utilisés).
    Raises:
        ValueError: Si l'expression est vide, mal formée, contient plus
            d'un opérateur, ou si les opérandes ne sont pas numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Normalise pour simplifier le parcours caractère par caractère
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            # Un seul opérateur binaire est supporté par expression
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # L'opérateur doit être strictement entre les deux opérandes
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos + 1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale : affiche la calculatrice et traite les soumissions.
    GET: rend le template sans résultat.
    POST, lit le champ ``display`` du formulaire, appelle ``calculate``
    et renvoie le résultat (ou un message d'erreur) au template.
    Returns:
        Réponse HTML rendue à partir de ``templates/index.html``.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Afficher l'erreur à l'utilisateur plutôt que de planter le serveur
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    # Mode debug utile en développement ; à désactiver en production
    app.run(debug=True)
