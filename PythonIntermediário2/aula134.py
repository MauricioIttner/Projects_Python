# __dict__ e vars para atributos de instância
import json


class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)

p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)
print(vars(p1))
print(p1.outra)

with open('aula134.json', 'w+', encoding='utf8') as arquivo:
    dados = json.dump(p1.__dict__, arquivo, indent=2, ensure_ascii=False)
