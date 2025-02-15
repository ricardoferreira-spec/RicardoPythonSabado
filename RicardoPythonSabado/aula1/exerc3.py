# Calculadora de IMC
""" 
Solicite o peso em KG e Altura do usuário em metros
Calcule o IMC (indice de massa corporal)
peso / (altura * altura)
exibir o IMC

A classificação do IMC é a seguinte: 
Menor que 18,5: Magreza
Entre 18,5 e 24,9: Normal
Entre 25,0 e 29,9: Sobrepeso
Entre 30,0 e 39,9: Obesidade
Maior que 40,0: Obesidade Grave

 """


n1 = float(input("digite o seu peso: "))
n2 = float(input("digite sua altura: "))

IMC = n1/(n2*n2)

print("Seu IMC é:", IMC )

if IMC < 18.6:
    print("Seu IMC é considerado: Magreza")
elif IMC > 18.5 and IMC < 24.91:
    print("Seu IMC é considerado: Normal")    
elif IMC > 25 and IMC < 29.91:
    print("Seu IMC é considerado: Sobrepeso")
elif IMC > 30 and IMC < 39.91:
    print("Seu IMC é considerado: Obesidade")
else:
    print("Seu IMC é considerado: Obesidade Grave")