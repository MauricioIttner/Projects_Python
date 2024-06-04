""" CALCULADORA COM WHILE"""

import math
import calculadora_m as c

while True:
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))
    operador = input("Digite o operador (+ - / * r): ")

    operador_permitido = "+-/*r"

    if operador not in operador_permitido:
        print("Operador Inválido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    conta = c.calculator(operador, num_1, num_2)
    print(conta)

    sair = input("Quer sair ? [s]im: ").lower().startswith("s")

    if sair is True:
        break
