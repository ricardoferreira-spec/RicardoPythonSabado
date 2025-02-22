from ..models.produto import Produto
from ..database.database import Bancofake

class produtoController:
    def __init__(self):
        #Conexao com o banco
        self.db = Bancofake()

    def criar_produto(self, nome, preco):
        #Cria o objeto cliente e salva no banco
        novo_produto = Produto(nome, preco)
        #converter para dict(JSON)
        dict_produto = {
            "nome": novo_produto.nome,
            "preco": novo_produto.preco
        }

        #salvar no banco
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produto(self):
        # retorna uma lista com todos os clientes cadastrados
        return self.db.listar_produto()