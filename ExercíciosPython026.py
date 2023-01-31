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
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('* *' * 13)
print(f'{"cod":<6}', f'{"nome":<15}', f'{"gols":<8}', f'{"total":>6}')
print('-' * 40)
for k, v in enumerate(princ):
    print(f'{k:<7}', end='')
    print(f'{v["Nome"]:<17}', end='')
    print(f'{"v":<8}', end='')
    print(f'{v["Total"]:^6}')
print('-' * 40)
while True:
    busca = int(input('\nMostrar dados de qual jogador? [999 para parar]: '))
    print('-' * 40)
    if busca == 999:
        break
    print(f'Levantamento do jogador {princ[busca]["Nome"]}:')
    for i, p in enumerate(princ[busca]["Gols"]):
        print(f' => Na Partida {i} ele fez {p} gols')
