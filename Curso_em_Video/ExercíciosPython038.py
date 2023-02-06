def preços(msg):
    n = msg
    print(f'A metade de R${n} é R${n/2} ')
    print(f'O dobro de R${n} é R${n*2}')
    print(f'Aumentando 10%, temos {(n/100) * 110} ')


preços(int(input('Digite o Preço: R$')))