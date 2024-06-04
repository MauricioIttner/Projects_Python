# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6 7
# M A U R I C I O
#-8-7-6-5-4-3-2-1

'''nome = 'Mauricio'
print(nome[0])

print('cio' in nome)
print('x' not in nome)'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')