from ..models.cliente import Cliente
from ..database.database import Bancofake

class clienteController:
    def __init__(self):
        #Conexao com o banco
        self.db = Bancofake()

    def criar_cliente(self, nome, email, idade):
        #Cria o objeto cliente e salva no banco
        novo_cliente = Cliente(nome, email, idade)
        #converter para dict(JSON)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }

        #salvar no banco
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_cliente(self):
        # retorna uma lista com todos os clientes cadastrados
        return self.db.listar_clientes()