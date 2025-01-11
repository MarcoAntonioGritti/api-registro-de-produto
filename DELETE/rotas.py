from DELETE.comados import excluir_produto
from flask import Blueprint,jsonify

rota_delete = Blueprint('rota_delete',__name__)

@rota_delete.route('/produto/<int:id>',methods=['DELETE'])
def delete_Produto(id):
    excluir_produto(id)
    return jsonify({"message": "Produto deletado com sucesso!"}),200