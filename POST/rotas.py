from POST.comandos import adicionar_produto
from flask import Blueprint, jsonify, request

rotas_post = Blueprint("rotas_post", __name__)


@rotas_post.route("/produto", methods=["POST"])
def post_produto():
    dados = request.get_json()
    lista_resposta = []

    for item in dados:
        nome = item.get("nome")
        descricao = item.get("descricao")
        preco = item.get("preco")
        quantidade = item.get("quantidade")

        lista_resposta.append(
            {
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                " quantidade": quantidade,
            }
        )
        adicionar_produto(nome, descricao, preco, quantidade)

    return jsonify(lista_resposta), 201
