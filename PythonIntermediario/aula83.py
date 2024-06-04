# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Mauricio Ittner',
    'sobrenome': 'Queiroz',
}

print(p1.get('nome', input('Digite seu nome: ')))
# nome = p1.pop('nome')
# print(nome)

# item = p1.popitem()
# print(item)

# p1.update({
#     'idade': 19,
# })
# p1.update(nome='Mauricio', idade=19)
# tupla = ('nome', 'Mauricio'), ('idade', 19)
# lista = [('nome', 'Mauricio'), ('idade', 19)]
# p1.update(lista)
# print(p1)
