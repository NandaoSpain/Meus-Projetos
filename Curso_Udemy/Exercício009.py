def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


resultado = soma(10, 89, 95, 450, 985, 10, 69, 79, 56)
print(f'O resultado é {resultado}')