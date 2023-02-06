alunos = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append(temp[:])
    temp.clear()
    resp = str(input('Continuamos? [S/N]: ')).strip().upper()[0]
    if resp not in 'S':
        break
print('-' * 30)
print('Nº', f'{"NOME":<15}', f'{"MÉDIA":<5}')
print('-' * 30)
for i, v in enumerate(alunos):
    print(f'{i}', end='  ')
    print(f'{v[0]:<15}', end='')
    media = (v[1] + v[2]) / 2
    print(f'{media:>5.2f}')
while True:
    resp2 = int(input(('Mostrar notas de qual aluno? (999 interrompe): ')))
    if resp2 == 999:
        break
    print(f'As notas de {alunos[resp2][0]} são {alunos[resp2][1], alunos[resp2][2]}')
