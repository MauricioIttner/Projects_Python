"""
 Listas em Python
 Tpo list - Mutável
 Suporta vários valores de qualquer tipo
 Conhecemos reutilizáveis - índices e fatiamento
 Métodos úteis: 
    append - Adiciona um item no final
    insert - Adiciona um item no indice escolhido
    pop    - Remove do final ou do indice escolhido
    del    - apaga um indice
    clear  - Limpa a lista
    extend - Estene a lista
    +      - Concatena listas

 Create Read Update     Delete
 Criar  Ler  Alterar  Apagar  = list[i] (CRUD)
"""


lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])

lista.append(50)
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, "Removido:", ultimo_valor)
