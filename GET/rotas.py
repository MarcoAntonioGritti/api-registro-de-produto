from GET.comandos import buscar_produtos
from flask import Blueprint,jsonify

rotas_get = Blueprint('rotas_get',__name__)

@rotas_get.route('/produto',methods=['GET'])
def get_Produto():
    produtos = buscar_produtos()
    return jsonify(produtos), 200