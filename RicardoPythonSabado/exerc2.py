# Verificar se é impar ou par
""" 
Digite um número inteiro 
Verifique se o número é impar ou par escreva a mensagem correspondente
 """

#print("digite um número")
#n1 = int(input())
n1 = int(input("digite um número: "))

resto = n1%2

if resto == 0:
    print("Este número é par")
else:
    print("Este número é impar")

    # OU

if resto != 0:
    print("Este número é impar")
else:
    print("Este número é par")


