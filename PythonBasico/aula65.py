"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex: 746.824.890-70
    10  9   8   7   6   5   4   3   2
     7  4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0=301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
"""

cpf_enviado = input('Digite o cpf: ')
nove_digitos = cpf_enviado[:9]
count_1 = 10

resultado_1 = 0

for numero in nove_digitos:
    resultado_1 += int(numero) * count_1
    count_1 -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(f'O primeiro digito do CPF é {digito_1}')

print('-' * 25)

dez_digitos = nove_digitos + str(digito_1)
count_2 = 11

resultado_2 = 0

for numero_2 in dez_digitos:
    resultado_2 += int(numero_2) * count_2
    count_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'O primeiro digito do CPF é {digito_2}')

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado)

if cpf_enviado == cpf_gerado:
    print('CPF é válido')
else:
    print('CPF inválido, call 911 now')
