#Conversor de Temperatura
""" 
Solicite ao usuário para fornecer uma temperatura em Graus
Converta essa temperatura em Fahrenheit

Para converter temperaturas de Celsius para Fahrenheit, use a fórmula F = (1,8 × C) + 32. 
Para converter de Celsius para Kelvin, use a fórmula K = C + 273,15.
"""

print("Conversor de Temperatura: Celsius para Fahrenheit")

c = float(input("Forneça temperatura em Graus: "))

f = (c*1.8) + 32
k = c+273.15

print("temperatura em Fahrenheit é:", f )
print("temperatura em kelvin é:", k )