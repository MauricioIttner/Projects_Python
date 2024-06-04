primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor and primeiro_valor > 0:
    print(f'Primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}')
elif segundo_valor > primeiro_valor and segundo_valor > 0:
    print(f'Segundo valor: {segundo_valor} é maior que o primeiro valor: {primeiro_valor}')
else:
    print('Os valores são iguais ou negativos')