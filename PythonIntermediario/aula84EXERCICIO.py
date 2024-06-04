# Exercício - sistema de perguntas e repostas
respostas = ['c', 'a', 'b']
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    # Inicia em falso, porque ainda nao acertou
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    # Verifica se a pessoa digitou um digito
    if escolha.isdigit():
        escolha_int = int(escolha)

    # Se for um digito ele converte para inteiro e cai no segundo if
    if escolha_int is not None:
        # Verifica se a pessoa digitou um indice que está dentro das opçoes
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            # Verifica se a opção escolhida é igual a resposta certa
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()

    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
