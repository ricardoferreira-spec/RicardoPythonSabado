"""
função def

print()
print()
print()
print("***************************************")

def carro_matheus():
    print("pegeout 206 turbo")
carro_matheus()
carro_matheus()
carro_matheus()

print("***************************************")

def escrever_carro(nome):       ### na função determina que terá 1 parametro
    print(nome)
escrever_carro("marea manual")  ### passa o parametro que esta pedindo = marea manual

print("***************************************")
def somar_numeros(num1, num2):  ### função esta pedindo 2 parametros
    return num1+num2            ### oque será realizado com os 2 parametros

resultado = somar_numeros(4,4)  ### informo os dois parametros 4,4

print("o resultado é:", resultado)

print("***************************************")
print()

### Desenvolvo a função, que espera receber 1 parametro = idade
def verificaidade(idade):
    if idade >= 18:                 
        return "Pode ver o filme"
    else:
        return "Não pode ver o filme"
    
### Interação com o usuário
print("digite sua idade:")
idade = int(input())

### Lógica onde acontece a mágica.
resultado = verificaidade(idade)
print(resultado)


"""
print("***************************************")
print()

def menu():
    print("Menu da calculadora")
    print("1 - Somar")
    print("2 - Subtrair")
    print("9 - Sair")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def verificaOpção(opcao):
    if opcao ==1:
        num1 = float(input("Dgite o número 1: "))
        num2 = float(input("Dgite o número 2: "))
        print (somar(num1, num2))
    elif opcao==2:
        num1 = float(input("Dgite o número 1: "))
        num2 = float(input("Dgite o número 2: "))
        print (subtrair(num1, num2))

def calculadora():
    while True:
        menu()
        opcao = int(input("escolha uma opção:"))
        verificaOpção(opcao)

calculadora()




print("***************************************")
print()
print()
print()