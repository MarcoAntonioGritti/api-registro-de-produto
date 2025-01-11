from ConexaoDataBase.database import conexao

def adicionar_produto(nome, descricao, preco, quantidade):
    comando = f"""INSERT INTO Produto(nome,descricao,preco,quantidade) VALUES ('{nome}','{descricao}',{preco},{quantidade})"""
    conexao.execute(comando)
    conexao.commit()
