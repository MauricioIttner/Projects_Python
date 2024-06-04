from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def get_agencia(self):
        return self.agencia

    def get_conta(self):
        return self.conta

    def get_saldo(self):
        return self.saldo

    @abstractmethod
    def sacar(self, value: float) -> float: ...

    def depositar(self, value: float):
        self.saldo += value
        print('')
        print('DEPOSITANDO...')
        self.detalhes(f'\n(DEPÓSITO FEITO NO VALOR DE R${value})')
        self.saldo

    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('----')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0.0,
                 limite: float = 0.0):
        Conta.__init__(self, agencia, conta, saldo)
        self.limite = limite

    def detalhe(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')

    def get_limite(self) -> float:
        return self.limite

    def sacar(self, value: float) -> float:
        valor_pos_saque = self.saldo - value
        limite_maximo = -self.limite
        limite_utilizado = self.limite + valor_pos_saque

        if valor_pos_saque >= limite_maximo:
            self.saldo -= value
            print('')
            print('SACANDO...')
            self.detalhe(f'\n(SAQUE APROVADO NO VALOR DE R${
                         value})\n (Limite restante: R${limite_utilizado})')
            print('----------')
            return self.saldo
        limite_restante = limite_utilizado
        limite_atual = limite_restante \
            if limite_restante >= 0 else self.limite \
            + self.saldo

        print('Não foi possível sacar o valor solicitado.')
        self.detalhes(f'\n(SAQUE NEGADO NO VALOR DE R${
                      value})\n(Limite restante: R${limite_atual})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {
            self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo=0.0):
        Conta.__init__(self, agencia, conta, saldo)

    def sacar(self, value):
        valor_pos_saque = self.saldo - value
        if valor_pos_saque >= 0:
            self.saldo -= value
            print('SACANDO...')
            self.detalhes(f'\n(SAQUE APROVADO NO VALOR DE R${value})')
            return self.saldo

        print('Não foi possível sacar o valor solicitado.')
        self.detalhes(f'\n(SAQUE NEGADO NO VALOR DE R${value})')
        return self.saldo


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.detalhes()
    cp1.sacar(1)
    cp1.depositar(2)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(231, 666, 0, 100)
    cc1.detalhes()
    cc1.sacar(1)
    cc1.depositar(2)
    cc1.sacar(50)
    cc1.sacar(5)
    cc1.sacar(40)
    cc1.sacar(7)
