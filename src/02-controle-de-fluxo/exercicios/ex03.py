""" Ex 03 """

CODIGO = input('Digite o código: ')
buffer = True

if len(CODIGO) == 7:
    if CODIGO[0] == 'B' and CODIGO[1] == 'R' and CODIGO[6] == 'X':
        for i in range (2, 6):
            if '0' <= CODIGO[i] <= '9':
                continue
            else:
                buffer = False
                break
    else:
        buffer = False
else:
    buffer = False

if buffer:
    print('O código é válido')
else:
    print('O código é inválido')
