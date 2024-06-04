# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


import json

CAMINHO_ARQUIVO = 'aula135.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Joao', 23)
p2 = Pessoa('Luiz', 36)
p3 = Pessoa('Lucas', 21)

bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print('ELE É O __main__')
    fazer_dump()
