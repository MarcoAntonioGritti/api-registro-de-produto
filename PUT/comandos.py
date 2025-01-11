from ConexaoDataBase.database import  conexao

def atualizar_produto(id, nome=None, descricao=None, preco=None, quantidade=None):
    partes = []
    valores = []

    if nome is not None:
        partes.append("nome = ?")
        valores.append(nome)
    if descricao is not None:
        partes.append("descricao = ?")
        valores.append(descricao)
    if preco is not None:
        partes.append("preco = ?")
        valores.append(preco)
    if quantidade is not None:
        partes.append("quantidade = ?")
        valores.append(quantidade)

    if partes:
        comando = f"""UPDATE Produto SET {', '.join(partes)} WHERE id = ?"""
        valores.append(id)
        conexao.execute(comando, tuple(valores))
