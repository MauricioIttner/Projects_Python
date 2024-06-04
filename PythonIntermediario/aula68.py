"""
Introdução às funções (def) em Python
Funções são trechos de código usado para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmentros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
