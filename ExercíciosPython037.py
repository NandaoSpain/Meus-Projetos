from time import sleep
c = ('\033[m',        #0 - sem cores
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;42m', #2 - verde
     '\033[0;30;43m', #3 - amarelo
     '\033[0;30;44m', #4 - azul
     '\033[0;30;45m', #5 - roxo
     '\033[7;30m'     #6 - branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('Sistema de ajuda PyHelp', 1)
    print(c[3], end='')
    comando = str(input('Funcão ou Biblioteca >>> '))
    print(c[0], end='')
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!', 2)
