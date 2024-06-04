# Métodos em instâncias de classes Python
#  hard coded - é algo que foi escrito diretamente no codigo
# Classe - Molde (sem dados)
# Instancia da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
