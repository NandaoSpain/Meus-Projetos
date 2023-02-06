from time import sleep


def maior(* num):
    print('-_' * 20)
    cont = maiores = 0
    print(f'Analisando os valores passados...')
    for i, v in enumerate(num):
        print(v, end=' ')
        sleep(0.3)
    print(f'.  Foram passados {len(num)} valores.')
    for i, v in enumerate(num):
        if cont == 0:
            maiores = v
        else:
            if v > maiores:
                maiores = v
        cont += 1
    print(f'O maior valor é {maiores}')


maior(2, 4, 12, 7, 8)
maior(9, 18, 1)
maior(9, 8)
maior(5)
maior()
