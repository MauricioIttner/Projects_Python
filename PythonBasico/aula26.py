"""
Interpolação básica de strings
s - string
d e i - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal _ + ou - 
Ex.: 0>100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'.{variavel:->10}.')
print(f'.{variavel:-<10}.')
print(f'.{variavel:-^10}.')
print(f'{1000.568487897489798:0=+10.2f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
