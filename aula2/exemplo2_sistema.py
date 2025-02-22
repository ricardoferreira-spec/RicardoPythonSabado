"""
Criar novo arquivo
Desenvolver um sistema que recebe
valor A, Valor de b e Valor C
calcular Bhaskara
Delta = -b2 - 4*a*c
"""

import math

a = float(input("digite um número a: "))
b = float(input("digite um número b: "))
c = float(input("digite um número c: "))

Delta = float(b ** 2 - (4*a*c)) # -9 -(4*2*2) = -9 -(16) = -25

raiz_delta = math.sqrt(Delta)

x1 = (-b + raiz_delta)/(2*a) #-3 +5 / 4 = 
x2 = (-b - raiz_delta)/(2*a) # -3-5 / 4 = 

print("o Valor de Delta é:", Delta)
print("o Valor de X1 é:", x1)
print("o Valor de X2 é:", x2)
