import json

# pessoa = {
#     "nome": "Mauricio Ittner",
#     "sobrenome": "Queiroz",
#     "enderecos": [
#         {"rua": "R1", "numero": 32},
#         {"rua": "R2", "numero": 55}
#     ],
#     "altura": 1.8,
#     "numeros_preferidos": (2, 4, 6, 8, 10),
#     "dev": True,
#     "nada": None,
# }

# with open('aula125.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa,
#               arquivo,
#               ensure_ascii=False,  # Para imprimir acentos
#               indent=2,  # Para identar o codigo
#               )

with open('aula125.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    for chave, valor in pessoa.items():
        print(chave.upper(), '-', valor)
