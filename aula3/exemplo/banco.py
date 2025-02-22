class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        # mesma coisa que : self.saldo  = self.saldo + valor

    def sacar (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
        
    def get_saldo(self):
        return self.saldo
    
ContaRicardo = ContaBancaria(1000)  #inclui saldo no def __init__
ContaRicardo.sacar(700)             #executa o saque
ContaRicardo.depositar(1200)        #executa o deposito
print(ContaRicardo.get_saldo())     #imprime o saldo em tela
