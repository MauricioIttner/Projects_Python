"""
  Cuidados com dados mutáveis
 = - copiando o valor (imutáveis)
 = - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ["João", "Marco"]
lista_b = lista_a.copy()

lista_a[0] = "Outro valor"
print(lista_a)
print(lista_b)
