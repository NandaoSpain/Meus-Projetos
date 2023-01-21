print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
maior = 0
homem = 0
meninas = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'M':
        homem += 1
    if sexo in 'F':
        if idade < 20:
            meninas += 1
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resp not in 'Ss':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {meninas} mulheres cadastradas com menos de 20 anos')