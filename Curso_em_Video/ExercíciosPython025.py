galera = []
pessoas = {}
soma = mulheres = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Continuamos? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('* *' * 15)
print(f'  A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'  B) A média de idade é de {media:.2f} anos.')
print(f'  C) As mulheres cadastradas são: ', end=' ')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end='  ')
print(f'\n  D) As pessoas com idade acima da média de idades são: ', end=' ')
for p in galera:
    if p['Idade'] >= media:
        print(f'{p["Nome"]}', end=' ')
print('* *' * 15)
print()
