from ExerciciosPython.Ex046 import moeda

num = (int(input('Digite o Preço: R$')))
print(f'O dobro de {moeda.din(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.din(num)} é {moeda.metade(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num,  10, True)}')
print(f'Diminuindo 18%, temos {moeda.aumentar(num, 18, True)}')
