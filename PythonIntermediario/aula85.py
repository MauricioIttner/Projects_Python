nota_A = float(input("Digite a nota A (de 0 a 10, com uma casa decimal): "))
nota_B = float(input("Digite a nota B (de 0 a 10, com uma casa decimal): "))

# Verifica se as notas estão no intervalo permitido
if 0 <= nota_A <= 10 and 0 <= nota_B <= 10:
    # Calcula a média ponderada
    media = (nota_A * 3.5 + nota_B * 7.5) / 11

    # Exibe a média
    print("A média do aluno é:", format(media, ".5f"))
else:
    print("Notas fora do intervalo permitido (0 a 10).")
