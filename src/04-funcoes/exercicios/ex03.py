""" Exercicio 03 S2.A4 """

def soma(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

breakpoint()
RESULTADO = soma((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(RESULTADO)
