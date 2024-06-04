"""
Retorno de valores de função (return)
"""


def soma(x, y):
    print(f'x={x} + y={y}')
    if x > 10:
        print(f'{x} é maior que 10')
        x = int(input('Digite outro valor: '))
        print(f'x={x} + y={y}')
        return x + y
    return x + y


soma1 = soma(4, 4)
soma2 = soma(11, 3)
print(soma1)
print(soma2)
