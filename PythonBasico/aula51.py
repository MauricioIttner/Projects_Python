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


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
