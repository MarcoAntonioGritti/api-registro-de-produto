from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

connection_string = os.getenv('DB_CONNECTION_STRING')
dados_conexao = pyodbc.connect(connection_string)


conexao = dados_conexao.cursor()