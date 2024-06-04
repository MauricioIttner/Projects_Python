# reduce - faz a redução de um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# def funcao_do_reduce(acumulador, produto):
#     return round(acumulador + produto['preco'], 2)


total = reduce(
    lambda ac, p: round(ac + p['preco'], 2),
    produtos,
    0
)

print('O total é', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(round(total, 2))
