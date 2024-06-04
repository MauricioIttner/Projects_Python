frase = (
    "O Python é uma linguagem de programação "
    "multiparadigma. "
    "Python foi criado por Guido van Rossum"
)

i = 0
apareceu_x_vezes = 0
letra_que_mais_apareceu = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qts_vezes_ela_apareceu_ateAgora = frase.count(letra_atual)

    if apareceu_x_vezes < qts_vezes_ela_apareceu_ateAgora:
        apareceu_x_vezes = qts_vezes_ela_apareceu_ateAgora
        letra_que_mais_apareceu = letra_atual

    i += 1

print(
    "A letra que mais apareceu foi "
    f"'{letra_que_mais_apareceu}' e apareceu "
    f"{apareceu_x_vezes}x"
)
