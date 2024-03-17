from datetime import datetime
import pytz
import time


class ContaCorrente:


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Voce não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
         print('Seu limite de Cheque Especial é de R$ {:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Historico de Transações')
        print('Valor', 'Saldo', 'Data e Hora')
        for transacao in self.transacoes:
            print(transacao)


#Programa
conta_Kaian = ContaCorrente("Kaian", '111.111.111.11', 1234, 34567)
conta_Kaian.consultar_saldo()

#Depositando 
conta_Kaian.depositar(10000)
conta_Kaian.consultar_saldo()

time.sleep(3)

#Sacando 
conta_Kaian.sacar_dinheiro(1000)
conta_Kaian.consultar_saldo()
print('Saldo Final')
conta_Kaian.consultar_saldo()
conta_Kaian.consultar_limite_chequeespecial()

print('=' * 25)
conta_Kaian.consultar_historico_transacoes()
