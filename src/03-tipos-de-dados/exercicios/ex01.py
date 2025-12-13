""" Exercício 01 S2.A3 """

QTD_NUMEROS = 3
numeros = []

for i in range(QTD_NUMEROS):
    numeros.append(int(input(f'Digite o número {i+1}: ')))

if len(numeros):
    maior = menor = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[i] < menor:
            menor = numeros[i]
        elif numeros[i] > maior:
            maior = numeros[i]

print(f'O maior elemento é: {maior}\n' + 
      f'O menor elemento é: {menor}')
