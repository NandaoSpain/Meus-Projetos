def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
quintuplicar = criar_multiplicador(5)
print(duplicar(10))
print(quintuplicar(10598))