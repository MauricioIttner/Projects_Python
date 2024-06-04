"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é impar ou par. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# n = input("Digite um número inteiro: ")

# if n.isdigit():
#     n_int = int(n)
#     if n_int % 2 == 0:
#         print("Este numero é par")
#     else:
#         print("Este número é impar")
# else:
#     print("Esse não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom Dia 0-11, Boa Tarde 12-17 e Boa noite 28-23.
"""
# hora = int(input("Que horas são? "))

# if hora >= 0 and hora <= 11:
#     print("Bom dia")
# elif hora >= 12 and hora <= 17:
#     print("Boa Tarde")
# else:
#     print("Boa noite")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras "Seu nome é muito grande".
"""

nome = input("Qual seu nome? ")

if (len(nome)) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
