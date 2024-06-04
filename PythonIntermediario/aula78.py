# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam
#  o número recebido como parâmetro.

def numero(x):
    def mult(multi):
        return f'{x*multi}'
    return mult


while True:

    num = int(input('Digite um numero: '))
    multip = int(input(f'Esse numero {num} vezes quanto? '))

    if num != '':
        numero0 = numero(num)
        multiplicad = multip

    print(numero0(multiplicad))


# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar


# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))
