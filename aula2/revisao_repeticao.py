
#for = repita enquanto isto for verdadeiro
""""

"""
# range (valor inicial, valor final e quanto diminui)
"""
print("*********** exemplo tabuada **************")

for i in range(1,11):
    print(" Tabuada do Número: ",i)
    for y in range(1,11):
        print(y," X ",i," = ",y*i)
        
print("*********** fim tabuada **************")


verificar se uma palavra é um palindromo: arara
caso seja, exiba "É palindromo"
caso não seja, exiba "Não é um palindromo"
A verificação deve ser case Sensitive

digite uma palavra: arara
é um palindromo

digite uma palavra: subi no onibus
é um palindromo

strip() retira os espaços
lower() trata sensitive case
replace(" ","") troca os espaços pra nada

"""
print()
palavra = input("digite uma palavra: ").lower().strip().replace(" ","")
if palavra == palavra[::-1]:
    print("é um palindromo")
else:
    print("Não é palindromo")


