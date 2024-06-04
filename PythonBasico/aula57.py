"""
 enumerate - enumera iteráveis (indices)
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

lista_enumerada = enumerate(lista)

# for nome in lista_enumerada:
#     print(nome)

for nome in lista_enumerada:
    a, b = nome
    print(a, b)

# for tupla_enum in enumerate(lista):
#     print("FOR da tupla")
#     for valor in tupla_enum:
#         print(f"\t{valor}")
