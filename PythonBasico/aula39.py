"""
   Iterando strings com while
"""

nome = "Mauricio Ittner"

tamanho_nome = len(nome)

indice = 0
novo_nome = ""
new_nome = ""
while indice < tamanho_nome:
    letra = nome[indice] + "*"
    letraa = nome[indice]
    novo_nome += letra
    new_nome += f"*{letraa}"

    indice += 1

print(15 * "-")
novo_nome += "*"
print(f"{novo_nome=}")
print(15 * "-")
print(f"{new_nome=}")
