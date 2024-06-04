# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING'
    )
    sobrenome: str = 'Not Sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)
    # Executado logo após a dataclass
    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.sprit()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    # lista = [Pessoa('Mauricio', 'Ittner'), Pessoa(
    #     'Luiz', 'Moura'), Pessoa('Joana', 'Silva')]
    # # se passar order=True no decorador ele ativa o sorted,
    # senao passar utiliza a key
    # ordenar = sorted(lista, reverse=False, key=lambda p: p.nome)
    p1 = Pessoa('Mauricio', 'Ittner')
    print(p1)
    # print(asdict(p1).keys())
    # print(asdict(p1).values())
    # print(asdict(p1).items())
    # print(astuple(p1)[0])
