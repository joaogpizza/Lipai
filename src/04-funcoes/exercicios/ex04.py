""" Exercicio 04 S2.A4 """

def soma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

RESULTADO = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(RESULTADO)
