import mysql.connector
from config import Config

class ProdutoModel:
    def __init__(self):
        # iniciando a configuração do banco de dados mysql
        self.config = Config()

        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )

        # faz o cursor trazer o resultado em dicionário
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_products(self):
        """ Retorna a lista de todos os produtos"""
        query = "SELECT id, nome, preco FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_product(self, nome, preco):
        """ Inserir um produto na tabela produtos"""
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        self.cursor.execute(query, (nome, preco))
        self.connection.commit() #confirma a transição
        return self.cursor.lastrowid
    
    def get_product_by_id(self, product_id):
        """ Busca o produto pelo ID"""
        query = "SELECT id, nome, preco FROM produto WHERE id = %s"
        self.cursor.execute(query, product_id)
        return self.cursor.fetchone()
    
    def delete_product_by_id(self, product_id):
        """ Deletar um produto pelo ID"""
        query = "DELETE FROM produto WHERE id = %s"
        self.cursor.execute(query, product_id)
        self.connection.commit() #confirma a deleção
        return self.cursor.rowcount
    
    def update_product_by_id(self, product_id, nome, preco):
        """" Atualizar um produto pelo ID"""
        query = "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s"
        self.cursor.execute(query, nome, preco, product_id)
        self.connection.commit() #confirma alteração
        return self.cursor.rowcount
    
    def close_coneection(self):
        self.cursor.close()
        self.connection.close()

