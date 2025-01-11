from PUT.comandos import atualizar_produto
from flask import Blueprint,jsonify,request

rotas_put = Blueprint('rotas_put',__name__)

@rotas_put.route('/produto/<int:id>',methods=['PUT'])
def put_produto(id):
    dados = request.get_json()
    lista_resposta = []

    nome = dados.get('nome')
    descricao = dados.get('descricao')
    preco = dados.get('preco')
    quantidade = dados.get('quantidade')

    lista_resposta.append({'nome': nome, 'descricao': descricao, 'preco': preco, 'quantidade': quantidade})
    atualizar_produto(id,nome, descricao, preco, quantidade)

    return jsonify(lista_resposta),200