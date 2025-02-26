from flask import Flask, request, jsonify
from sympy import symbols, Eq, solve, sympify, SympifyError
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir solicitações do frontend

def validar_entrada(entrada):
    """Valida se a entrada é uma equação matemática válida."""
    # Verifica se a entrada contém exatamente um sinal de igual
    if entrada.count('=') != 1:
        return False

    # Verifica se a entrada contém apenas caracteres válidos
    padrao_valido = re.compile(r'^[0-9xX+\-*/=. ()]+$')
    return bool(padrao_valido.match(entrada))

def resolver_equacao(entrada):
    """Resolve uma equação do primeiro grau usando SymPy."""
    x = symbols('x')
    try:
        # Valida a entrada
        if not validar_entrada(entrada):
            return "Erro: A entrada deve ser uma única equação matemática válida (ex: 2x + 3 = 7)."

        # Divide a equação em lado esquerdo e direito
        lado_esquerdo, lado_direito = entrada.split('=')
        lado_esquerdo = lado_esquerdo.strip()
        lado_direito = lado_direito.strip()

        # Converte os lados da equação em expressões SymPy
        expr_esquerda = sympify(lado_esquerdo)
        expr_direita = sympify(lado_direito)

        # Resolve a equação
        solucao = solve(Eq(expr_esquerda, expr_direita), x)
        if not solucao:
            return "Erro: A equação não tem solução ou não é do primeiro grau."
        return f"A solução é x = {solucao[0]}"
    except SympifyError:
        return "Erro: A equação contém caracteres ou formatos inválidos."
    except Exception as e:
        return f"Erro ao resolver a equação: {str(e)}"

@app.route('/resolver', methods=['POST'])
def resolver():
    """Recebe um problema do usuário e retorna a solução."""
    try:
        data = request.get_json()  # Obtém os dados JSON da solicitação
        entrada = data.get("entrada")

        if not entrada:
            return jsonify({"erro": "Nenhum problema foi fornecido."}), 400

        # Resolve a equação com SymPy
        solucao = resolver_equacao(entrada)

        return jsonify({
            "solucao": solucao
        })
    except Exception as e:
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)