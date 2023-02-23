def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


dobro = multiplicar(2)
quituplo = multiplicar(5)


print(dobro(5))
print(quituplo(1985))


def nome(nombre):
    def upper(nombre):
        return nombre.upper()
    return upper

@nome
def imprimir(nome):
    return f'Seu nome é {nome}'

print(imprimir('Fernando'))