# dir, hasattr, getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe metodo', metodo)
