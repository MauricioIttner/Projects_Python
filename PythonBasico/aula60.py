"""
split e join com list e str
split - divide uma string
join - une uma string
strip - corta espaços indesejados
"""
frase = "         Olha só que    ,    coisa interessante        "
lista_prim = frase.split(", ")

lista_fix = []

for i, frase in enumerate(lista_prim):
    lista_fix.append(lista_prim[i].strip())

# print(lista_prim)
# print(lista_fix)
frases_unidas = " ".join(lista_fix)
print(frases_unidas)
