class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular: str = titular
        self.saldo: float = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"valor depositado com sucesso!")
    
    def sacar(self, valor):
        if valor >= self.saldo:
            print(f"Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque realzado com sucesso!")

    def consultar(self):
        print(f"Seu saldo é de R${self.saldo:.2f}")

#============ AREA DE TESTE ============#

Cliente = ContaBancaria(titular="João", saldo=80.0)

Cliente.consultar()

Cliente.sacar(90)

Cliente.depositar(10)

Cliente.sacar(90)

Cliente.consultar()
