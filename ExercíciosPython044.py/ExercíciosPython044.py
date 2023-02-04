from ExerciciosPython.Ex044 import moeda

num = (int(input('Digite o Preço: R$')))
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num, 10)}')