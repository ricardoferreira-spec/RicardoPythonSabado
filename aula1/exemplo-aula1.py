# sistema que valida idade
print("qual a idade do aluno?")
idade = int(input())

if idade >=18:
    print("a pessoa pode sair")
else:
    print("presa para sempre")

""" Idade
Categoria
0-1     Recém Nascido
2-12    Criança
13-18   Adolescente
19-60   Adulto
60-80   Idoso
>80     Longevo

a = input("Digite a idade da pessoa: ")
idade = int (a)

if idade <=1:
    print ("Recém nascido")
else:
    if idade < 13: 
        print ("Criança")
    else:
        if idade < 18:
            print ("Adolescente")
        else:
            if idade < 60:
                print ("Adulto")
            else:
                if idade < 80:
                    print ("Idoso")
                else:
                    print ("Longevo")

print ("Acabou.")

ou 
a = input("Digite a idade da pessoa: ")
idade = int (a)

if idade <=1:
    print ("Recém nascido")
elif idade < 13:  
        print ("Criança")
elif idade < 18:
    print ("Adolescente")
elif idade < 60:
    print ("Adulto")
elif idade < 80:
    print ("Idoso")
else:
    print ("Longevo")

print ("Acabou.")


Ainhamento de IFs
Quando é preciso refinar uma condição, tomando uma decisão depois que outra já foi tomada, usa-se o aninhamento de IFs.
No exemplo a seguir, caso a nota de um aluno seja menor do que 7, ainda é preciso testar se ele tem uma nota maior ou igual a 4 para que possa realizar a prova G2.

a = input("Digite sua nota: ")
nota = float (a)

if nota >=7.0:
    print ("Você está aprovado por média.")
    if nota>9.0:  # IF ANINHADO
        print ("Parabéns!")  # se nota > 9
    print ("Boas Ferias!")  #  se nota >=7
else:
    if nota>=4: # IF ANINHADO
        print ("Você pode fazer G2.");
        print ("Venha na próxima semana")
    else:
        print ("Você está reprovado!")
        print ("Você não pode fazer G2.")
       
print ("Acabou.")

 """