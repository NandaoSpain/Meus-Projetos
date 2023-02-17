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


print('Jogo do Milhão'.center(20))
for pergunta in perguntas:
    print()
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    print('Opção: ')
    print()
    ind = 1
    for opcao in pergunta['Opções']:
        print(f'{ind}) ', end='')
        print(opcao)
        ind += 1