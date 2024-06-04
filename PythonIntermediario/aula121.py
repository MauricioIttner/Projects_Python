# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# import sys
# sys.setrecursionlimit(1004)


# def recursiva(i=0, f=10):

#     print(i, f)
#     # Caso Base
#     if i >= f:
#         return f

#     # Caso Recursivo
#     # contar até chegar ao final
#     i += 1
#     return recursiva(i, f)


# print(recursiva(0, 100))

def fatorial(n):
    if n <= 1:
        return n
    return n * fatorial(n - 1)


print(fatorial(5))
