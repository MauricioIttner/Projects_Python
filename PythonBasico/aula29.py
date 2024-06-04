"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
"""
print(123)
print(456)
try:
    print(int('abc'))
except:
    print()"""
"""
numero = input('Vou dobrar o numero que você digitar: ')
if numero.isdigit():
    numero_p = int(numero)
    print(f'O dobro de {numero} é {numero_p * 2}')
else:
    print('Isso não é um numero')"""

numero = input("Vou dobrar o numero que você digitar: ")

try:
    numero_p = int(numero)
    print(f"O dobro de {numero} é {numero_p * 2}")

except:
    print("Isso não é um numero")
