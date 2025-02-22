# main seá o aquivo principal
# controllers
# database
# models

def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")

def main():

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Cliente: ")
            email = input("Email do Cliente: ")
            idade = int(input("Idade do Cliente: "))
            #Salvar no banco de dados
        elif opc == "2":
            # listar do banco de dados os clientes
            print("listar")
        elif opc == "3":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do Produto: "))
        elif opc == "4":
            # listar do banco de dados os produtos
            print("listar")
        elif opc == "0":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção Inválida. Tente novamente.")
        