# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a

# print(a, b)


# a, b = pessoa.values()
# print(a, b)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.60,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeado)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÂO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Mauricio', idade=23)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
