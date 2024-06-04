"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Mauricio'
preco = 1000.9578456
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é %08x' %(1500, 1500))