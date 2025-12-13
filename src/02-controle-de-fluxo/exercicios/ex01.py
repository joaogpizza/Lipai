LIMITE_SUPERIOR = 10.0
LIMITE_INFERIOR = 0.0
NUMERO_NOTAS = 3

notas = []

for i in range(NUMERO_NOTAS):
    while(True):
        buffer = float(input(f'Digite a nota {i+1}: '))
        if LIMITE_INFERIOR <= buffer <= LIMITE_SUPERIOR:
            notas.append(buffer)
            break
        print(f'Nota invalida, tem de ser maior ou igual a {LIMITE_INFERIOR} e menor ou igual a {LIMITE_SUPERIOR}')
        continue    

media = 0.0
for i in range(NUMERO_NOTAS):
    media += notas[i]

media /= NUMERO_NOTAS
print(f'A média aritmética é: {media}')
