nome = input("Seu nome: ")
sobrenome = input("Seu sobrenome: ")
idade = int(input("Sua idade: "))
ano_nascimento = int(input("Seu ano de nascimento: "))
maior_de_idade = idade >= 18
altura_metros = float(input("Sua altura: "))

print(f'{nome} {sobrenome}, tem {idade} anos, nasceu em {ano_nascimento} e tem {altura_metros}')
print(f'É de maior ? {maior_de_idade}')