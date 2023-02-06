from ExerciciosPython.Ex045 import moeda

num = (int(input('Digite o Preço: R$')))
print(f'O dobro de {moeda.din(num)} é {moeda.din(moeda.dobro(num))}')
print(f'A metade de {moeda.din(num)} é {moeda.din(moeda.metade(num))}')
print(f'Aumentando 10%, temos {moeda.din(moeda.aumentar(num, 10))}')