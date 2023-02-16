def multip(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multip(10, 89, 95, 450, 985, 10, 69, 79, 56)
print(f'O resultado é {resultado}')