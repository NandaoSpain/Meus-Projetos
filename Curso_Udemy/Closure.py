def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


dobro = multiplicar(2)
quituplo = multiplicar(5)


print(dobro(5))
print(quituplo(1985))