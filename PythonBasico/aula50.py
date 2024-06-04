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
lista.append("Mauricio")
nome = lista.pop()
lista.append(123)
del lista[-1]
lista.insert(0, 20)
print(lista)
lista.clear()
print(lista)
