"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = "Mauricio"  # iteravel
# iterator = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iterator)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
