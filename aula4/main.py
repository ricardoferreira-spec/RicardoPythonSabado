# main seá o aquivo principal
from src.controller import produto_controller

def exibir_menu():
    print("\nMAREA TOCA TUDO LTDA!")
    print("\n==== MENU ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar Produto unico")
    print("0 - Sair")

def listar_produtos():
    print ("\n ==== Lista de Produtos ==== ")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco {produto['preco']}")
    else
        print("Não existe produtos cadastrados")

def cadastrar_produto():
    print("\n ---- Cadastrar Produtos ----")
    nome = input("Digite o nome: ")
    preco = input("digite o preco: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com novo ID {novo_id}.")