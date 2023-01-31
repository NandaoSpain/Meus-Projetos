princ = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    somagols = 0
    ngols = 0
    for c in range(1, partidas + 1):
        ngols = int(input(f'Quantos gols {jogador["Nome"]} marcou na {c}ª partida?'))
        somagols += ngols
        gols.append(ngols)
    jogador['Gols'] = gols[:]
    jogador['Total'] = somagols
    princ.append(jogador.copy())
    while True:
        resp = str(input('Continuamos? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        print('ERROR! Digite apenas S ou N')
    if resp == 'N':
        break
print('* *' * 17)
print(f'{"cod":<6}', f'{"nome":<20}', f'{"gols":<12}', f'{"total":>8}')
print('-' * 50)
for k, v in enumerate(princ):
    print(f'{k:<6}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('\nMostrar dados de qual jogador? [999 para parar]: '))
    print('-' * 50)
    if busca == 999:
        break
    print(f'Levantamento do jogador {princ[busca]["Nome"]}:')
    for i, p in enumerate(princ[busca]["Gols"]):
        print(f' => Na Partida {i} ele fez {p} gols')
