class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar_dinheiro(self, valor):
        self.saldo -= valor


#Programa
conta_Kaian = ContaCorrente("Kaian", '111.111.111.11')
conta_Kaian.consultar_saldo()

#Depositando 
conta_Kaian.depositar(10000)
conta_Kaian.consultar_saldo()

#Sacando 
conta_Kaian.sacar_dinheiro(1000)
conta_Kaian.consultar_saldo()

