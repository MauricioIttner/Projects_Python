"""
    Faça uma lista de compras com o list
    O usuário deve ter a possibilidade de
    inserir, apagar e listar valores da sua lista
    Não permita que o programa quebre com
    erros de indice inexistentes na lista.
"""
import os


lista = []

while True:
    opcao = input("Selecione uma opção: \n[i]nserir [a]pagar [l]istar:")

    if opcao == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.insert(0 + 1, valor)
        continue

    elif opcao == "a":
        apagar = int(input("Escolha o indice para apagar: "))
        try:
            lista.pop(apagar)
        except:
            print("Não foi possivel apagar este indice")

    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")

        for item in enumerate(lista):
            a, b = item
            print(a, b)

    else:
        print("Opção Invalida")
