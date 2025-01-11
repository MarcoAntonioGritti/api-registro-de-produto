from ConexaoDataBase.database import conexao

def buscar_produtos():

    lista_produtos = []
    comando = "SELECT * FROM Produto"
    conexao.execute(comando)
    produtos = conexao.fetchall()

    for produto in produtos:
        lista_produtos.append({
            'id': produto[0],
            'nome': produto[1],
            'descricao': produto[2],
            'preco': produto[3],
            'quantidade': produto[4]
    })
    return lista_produtos


