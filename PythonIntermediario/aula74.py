"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for num in args:
        total += num
    return total


soma_1 = soma(1, 2, 3, 4, 5)
print(soma_1)

soma_2 = soma(4, 6, 8)
print(soma_2)

numeros = 1, 2, 3, 4, 5, 6, 78, 98
soma_3 = soma(*numeros)
print(soma_3)

print(sum(numeros))
