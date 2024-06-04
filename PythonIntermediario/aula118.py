# map - para mapear dados

from functools import partial
from types import GeneratorType


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_valor(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_10_porCento = partial(
    aumentar_valor,
    porcentagem=1.1
)


def mudar_preco(produto):
    return {**produto, 'preco': aumentar_10_porCento(produto['preco'])}


# novos_produtos = [
#     mudar_preco(p)
#     for p in produtos
# ]


novos_produtos = map(
    mudar_preco,
    produtos
)

print_iter(novos_produtos)

print(list(map(
    lambda x: x * 3
    [1, 2, 3, 4]
))
)
