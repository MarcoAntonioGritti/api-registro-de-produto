from ConexaoDataBase.database import conexao

def excluir_produto(id):
    comando = f"""DELETE FROM Produto WHERE id = ?"""
    conexao.execute(comando, (id,))
    conexao.commit()
