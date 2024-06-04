# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Mauricio Ittner'
pessoa['sobrenome'] = 'Queiroz'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
