# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como tuplas
# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Carta = namedtuple(
#     'Carta', ['valor', 'naipe']
#     # defaults=[]
# )
as_espada = Carta('A', '♠')

#
#
#
#
#
#
#
#
#
#
#
#
#
print('--------DICT-----')
print(as_espada._asdict())
print('--------TUPLE-----')
print(as_espada)
print('--------INDICE 0 TUPLE-------')
print(as_espada[0])
print('--------INDICE VALOR TUPLE-----')
print(as_espada.valor)
print('--------INDICE 1 TUPLE-------')
print(as_espada[1])
print('--------INDICE NAIPE TUPLE------')
print(as_espada.naipe)
print('--------')

print()
print('--------NAME FIELDS TUPLE------')
print(as_espada._fields)
print('--------FIELDS DEFAULT------')
print(as_espada._field_defaults)
print()

print('---------FOR TUPLE------')
for valor in as_espada:
    print(valor)
