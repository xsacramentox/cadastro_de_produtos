
from database.mysql import get_connection, close_resource

class ProdutosModel:

    def carregar_produtos(self):
        conexao = get_connection()
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM produto ")
            return cursor.fetchall()
        finally:
            close_resource(conexao)

    def carregar_produto(self, id):
        conexao = get_connection()
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM produto WHERE id = " + id)
            return cursor.fetchone()
        finally:
            close_resource(conexao)

    def incluir_produto(self, produto):
        conexao = get_connection()
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produto (descricao, codigo_de_barras, preco, data_alteracao) VALUES (%s, %s, %s, now())", (produto['descricao'], produto['codigo_de_barras'], produto['preco'],))
            conexao.commit()        
        finally:
            close_resource(conexao)

    def editar_produto(self, produto):
        conexao = get_connection()
        try:
            cursor = conexao.cursor()
            cursor.execute("UPDATE produto SET descricao = %s, codigo_de_barras = %s, preco = %s, data_alteracao = now() WHERE id = %s", (produto['descricao'], produto['codigo_de_barras'], produto['preco'], produto['id'],))
            conexao.commit()
        finally:
            close_resource(conexao)

    def excluir_produto(self, produto):
        conexao = get_connection()
        try:
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM produto WHERE id = %s", (produto['id'],))
            conexao.commit()
        finally:
            close_resource(conexao)
            