# List comprehension eem Python
# List comprehension é uma forma rápida de criar listas
# a partir de iteráveis

# print(list(range(10)))

import pprint


def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)


lista = []

for numero in range(10):
    lista.append(numero)
# print(lista)


lista = [
    numero * 2
    for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
# Gerar uma nova lista alterando algum dado, mas mantendo o tamanho
# Vem a esquerda do for
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
# print(*novos_produtos, sep='\n')

# p(novos_produtos)

# Filter vem a direita
lista = [
    n
    for n in range(10)
    if n < 5
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novos_produtos)
print(lista)
