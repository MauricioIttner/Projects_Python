# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a, b, c = lista
# print(a, c)
print(*lista)
print(*tupla)

for nome in lista:
    print(nome, end=' ')
