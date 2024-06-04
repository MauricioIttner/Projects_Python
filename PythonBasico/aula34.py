"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    numero = int(input("Digite um numero: "))
    print(f"o dobro de {numero} é {numero * 2}")

    if numero <= 0:
        break
print("Acabou")
