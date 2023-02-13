import os
palavra = 'perfume'
acertada = ''
contador = 0
while True:
    letra =  input('\nDigite uma letra: ')
    contador += 1 
    if len(letra) > 1:
        print('Digite apenas 1 letra!')
        continue
    if letra in palavra:
        acertada += letra
    palavra_formada = ''
    for c in palavra:
        if c in acertada:
            palavra_formada += c
        else:
            palavra_formada += '*'
    print(f'Palavra Formada : {palavra_formada}')
    if palavra_formada == palavra:
        os.system('cls')
        print('Congratulations!! You win bro!!')
        print(f'Ao final foram {contador} tentativas!')
        print(f'A palavra era {palavra}')
        break
    