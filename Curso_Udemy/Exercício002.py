#programa 1
num = input('Digite um número: ')
numero = int(num)
if numero % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')
#programa 2
hora = input('Que horas são? ')
horacerta = int(hora)
if horacerta <= 11:
    print('Bom dia ')
elif 12 <= horacerta <= 17:
    print('Boa Tarde')
else:
    print('Boa Noite')
#programa 3
nome = input('Qual seu nome? ')
tamanho_nome = len(nome)
if tamanho_nome < 5:
    print('Nominho curto')
elif 5 <= tamanho_nome <= 6:
    print('Normalzinho')
else: 
    print('Nomãozão')
