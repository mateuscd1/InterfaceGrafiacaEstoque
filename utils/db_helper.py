import mysql.connector
from db_config import db_config


def conectar():
    try:
         return mysql.connector.connect(**db_config)
    
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
    
def executar_query(query, valores=None):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute(query, valores or ())
            resultados = cursor.fetchall()
            conexao.commit()
            return resultados
        except mysql.connector.Error as err:
            print(f"Erro ao executar query: {err}")
        finally:
            cursor.close()
            conexao.close()

