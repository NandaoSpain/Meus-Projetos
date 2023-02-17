from time import sleep
import os
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
acertos = 0
erros = 0 

print('Jogo do Milhão'.center(20))
for pergunta in perguntas:
    print()
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    print('Opção: ')
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) ', opcao)

       
    resp = input('Qual a Resposta? ')
    if resp == pergunta['Resposta']:
        print('Conferindo no nosso sistema...')
        sleep(2)
        print('Acertou!')
        print('Sorteando próxima pergunta...')
        sleep(2)
        acertos += 1
        os.system('cls')
    else:
        print('Conferindo no nosso sistema...')
        sleep(2)
        print('Errou!')
        print('Sorteando próxima pergunta...')
        sleep(2)
        erros += 1
        os.system('cls')

if acertos == 3:
    print('Você é Fera!! Acertou todas...')
    print()
elif acertos == 0:
    print('Vixi... Tem q treinar mais!!')
    print()
else:
    print(f'Você acertou {acertos} vezes e errou {erros} vezes.')
    print()