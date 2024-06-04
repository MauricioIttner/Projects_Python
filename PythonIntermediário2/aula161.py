# Classes decoradoras = (Decorator classes)
class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador


@Multiplicar
def soma(x, y):
    return x+y


somar = soma(2, 5)
print(somar)
