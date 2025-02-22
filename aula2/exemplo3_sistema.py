# sistema de desconto de veículos
# Solicite o nome do veículo
# E o preço do veículo
# se o preço >80 - 60% de desconto
# se o preço >50 - 30% de desconto
# se o preço <30 - Não existe desconto

print("Bem vindo a loja de veículos")
nome_veiculo = input("Informe o nóme do veículo: ")
preco = float(input("Informe o Valor do veículo: "))

if preco > 80:
    print("*******************************************")
    print("Valor do carro comprado é ------------- R$ " , preco)
    print("Você recebeu um desconto de 60%  ------ R$ " , preco * 0.60)
    print("O valor a ser pago será:  --------------R$ " , preco - (preco * 0.60))
    print("*******************************************")
elif preco >= 50:
    print("*******************************************")
    print("Valor do carro comprado é ------------- R$ " , preco)
    print("Você recebeu um desconto de 30% ------- R$ " , preco * 0.30)
    print("O valor a ser pago será: ---------------R$ " , preco - (preco * 0.30))
    print("*******************************************")
else:
    print("*******************************************")
    print("Valor do carro comprado é ------------- R$ " , preco)
    print("Não terá desconto")
    print("O valor a ser pago será: ---------------R$ " , preco)
    print("*******************************************")
