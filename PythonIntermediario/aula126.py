# Problema dos parâmetros mutáveis em funções Python

def add_client(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


client1 = add_client('Mauricio')
add_client('Ana', client1)
print(client1)

client2 = add_client('Helena')
add_client('Julia', client2)
print(client2)

client3 = add_client('Luiz')
add_client('Lucas', client3)
print(client3)

lista = client1 + client2 + client3

client4 = lista
print(sorted(client4))
