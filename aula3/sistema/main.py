# main seá o aquivo principal

from app.controllers.clienteController import clienteController

def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")

def main():
    cntrlCliente = clienteController()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Cliente: ")
            email = input("Email do Cliente: ")
            idade = int(input("Idade do Cliente: "))
            #Salvar no banco de dados
            cntrlCliente.criar_cliente(nome, email, idade)

        elif opc == "2":
            # listar do banco de dados os clientes
            clientes = cntrlCliente.listar_cliente()
            # index -> Posiçao atual do clientes listado
            # __str__ -> cliente => cliente(nome="", email="", idade="")
            for index, cliente in enumerate(clientes, 1):
                print(f"{index}.{cliente}")

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
        
if __name__ == "__main__":
    main()
