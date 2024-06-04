class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


gol = Carro('Gol')
volkswagen = Fabricante('Volkswagen')
motor_1_6 = Motor('1.6')
gol.fabricante = volkswagen
gol.motor = motor_1_6
print(gol.fabricante.nome, gol.nome, gol.motor.nome)

palio = Carro('Palio')
fiat = Fabricante('Fiat')
motor_1_8 = Motor('1.8')
palio.fabricante = fiat
palio.motor = motor_1_8
print(palio.fabricante.nome, palio.nome,  palio.motor.nome)
