# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. ELe é usado para 
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome = 'Mauricio'
idade = 17
maior_de_idade = idade >= 18
if(maior_de_idade  == False):
    print(f"{nome} você não é de maior")
else:
    print(f"{nome} você é de maior")