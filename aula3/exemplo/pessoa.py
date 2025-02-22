#definição da classe pessoa
class Pessoa:
    # Método Construtor: é chamado quando criamos um objeto
    def __init__(self, nome, idade, altura):
        #Atribuir a entidade
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Ola meu nome é {self.nome}, tenho {self.idade} anos e tenho {self.altura} metros de altura.')

    
p1 = Pessoa("Rafael", 34, "1.50")
p2 = Pessoa("Guilherme", 7, "1.35")
p3 = Pessoa("Alberto", 18, "1.95")

p1.apresentar()
p2.apresentar()
p3.apresentar()

