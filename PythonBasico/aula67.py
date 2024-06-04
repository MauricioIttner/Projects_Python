import random

for _ in range(10):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    count_1 = 10

    resultado_1 = 0

    for numero in nove_digitos:
        resultado_1 += int(numero) * count_1
        count_1 -= 1

    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    count_2 = 11

    resultado_2 = 0

    for numero_2 in dez_digitos:
        resultado_2 += int(numero_2) * count_2
        count_2 -= 1

    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado)
