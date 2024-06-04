# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, telefone):
        self.telefone = telefone

    def __call__(self, nome):
        print(nome, 'está ligando', self.telefone)


call = CallMe('546577266')
call('Mauricio')
