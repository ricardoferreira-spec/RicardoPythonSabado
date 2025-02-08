""" Tabela - Operadores Relacionais
    ==	Igual a
    !=	Diferente
    >=	Maior ou igual
    >	Maior que
    <	Menor que
    <=	Maior ou igual
 """
#comparação
print(10==10)   #true     Igual a
print(10!=5)    #true     Diferente
print(10<5)     #false    menor que
print(10>5)     #true     maior que

""" Operadores Lógicos
    or	OU lógico
    and	E lógico
    not	Negação
Tabela verdade para operadores AND e OR
A           B           and
True        True	    True
True	    False	    False
False       True	    False
False	    False	    False

Tabela verdade para operador NOT

 A              not
True	        False
False	        True
 """
#logica
print ((10>5) and (2==2))   #True and True -> true
print((10<5) and (2==2))    #False and True -> false

print ((10<5) or (2==2))    #False and True -> true
print((10>5) or (2==3))     #True and false -> true

#diferente
print(not(10==10))  # not True -> False Inverte o resultado

""" Os operadores or e and devem ser sempre usados entre duas expressões relacionais como por exemplo:
(2 > 1) or (3 < 7)  : resultado VERDADEIRO
(3 < 2) and (2 == 2) : resultado FALSO

Já o operador not deve ser usado antes de uma expressão relacional, para inverter seu valor, como por exemplo:
not (2 > 1): resultado VERDADEIRO
not (1 < 0): resultado FALSO

not (5 !=0) and (1 < 2)  : resultado FALSO """