# Exercício - sistema de perguntas e repostas

def exibir_pergunta(pergunta, opcoes):
    print(pergunta)
    for i, opcao in enumerate(opcoes, start=1):
        print(f'{chr(96 + i)}) {opcao}')
    escolha = input('Escolha uma opção: (a, b, c, d): ').lower()
    return escolha


def verificar_resposta(escolha, resposta_certa):
    return escolha == resposta_certa.lower()


def jogar():

    perguntas = [
        'Quanto é 2+2?',
        'Quanto é 5*5?',
        'Quanto é 10/2?'
    ]

    opcoes = [
        ['1', '3', '4', '5'],
        ['25', '55', '10', '51'],
        ['4', '5', '2', '1']
    ]

    respostas_certas = ['c', 'a', 'b']

    pontuacao = 0

    for i in range(len(perguntas)):
        pergunta_atual = perguntas[i]
        opcoes_atual = opcoes[i]
        resposta_certa_atual = respostas_certas[i]

        escolha = exibir_pergunta(pergunta_atual, opcoes_atual)

        if verificar_resposta(escolha, resposta_certa_atual):
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f'Resposta Incorreta. A resposta certa era {
                  resposta_certa_atual.upper()}.\n')

    print(f"Sua pontuação final: {pontuacao}/{len(perguntas)}")


if __name__ == "__main__":
    jogar()
