# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel


# def multi(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total


# mult = multi(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
# print(mult)
# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar


def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par'
    return f'{x} é impar'


digito = int(input('Digite um número: '))

print(par_impar(digito))
