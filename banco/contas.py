import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg=''):
        print(f' o seu saldo é {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor})')

        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO: {valor})')