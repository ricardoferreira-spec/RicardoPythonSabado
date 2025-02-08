# Números Pares em um Intervalo
""" 
solicite dois números inteiros aoa usuário
Representando o inicio e o fim de um intervalo
Mostre todos numeros pares nesse intervalo
(Incluindo limite inicial e final, se forem pares)
"""

print("Mostre os números pares do Intervalo")

n1 = int(input("digite um número inicial: "))
n2 = int(input("digite um número final: "))

# range (valor inicial, valor final e quanto diminui)
for y in range(n1,n2):
    if y % 2 == 0:    
        print("o Número é par:", y)
