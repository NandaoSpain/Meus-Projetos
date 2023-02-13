import os
from time import sleep
compras = []
while True:
    try:
        print('Selecione uma opção:')
        opção = input('[i]nserir  [a]pagar  [l]istar [s]air: ').strip().lower()[0]
        if opção in 'l':
            if len(compras) >= 1:
                os.system('cls')
                for i, v in enumerate(compras):
                    print(i, v)
            else:
                print('Lista vazia, nada para exibir')
        elif opção in 'a':
            if len(compras) > 0:
                try:
                    apagar = input('Qual item deseja apagar?')
                    indice_apagar = int(apagar)
                    del compras[indice_apagar]
                    print(f'Item {indice_apagar} apagado com sucesso!')
                    sleep(2)
                    os.system('cls')
                except (TypeError, ValueError):
                    print('Por favor digite somente números!')
                    continue
            else:
                print('Lista vazia, nada para apagar!')
        elif opção in 'i':
            os.system('cls')
            compras.append(input('Digite um item para inserir: '))
            print('Item inserido com sucesso!')
        elif opção in 's':
            
            break
    except IndexError:
        print('Por favor digite uma opção válida!')
        continue
