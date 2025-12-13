""" Ex 04 """

CODIGO = input('Digite o identificador: ')
erros = []
buffer = False

if len(CODIGO) != 7:
    erros.append("O identificador tem mais de 7 digitos")

if len(CODIGO) >= 2:
    if not (CODIGO[0] == 'B' and CODIGO[1] == 'R'):
        erros.append("O identificador não inicia com a sequência BR")
else:
    erros.append("O identificador não inicia com a sequência BR")

if len(CODIGO) >= 4:
    for i in range(len(CODIGO) - 3):
        substring = CODIGO[i:i+4]
        buffer = '0001' <= substring <= '9999'
        for caractere in substring:
            buffer = buffer and ('0' <= caractere <= '9')
        if buffer:
            break
if not buffer:
    erros.append('O identificador não apresenta número inteiro entre 0001 e 9999')

if CODIGO[len(CODIGO)-1] != 'X':
    erros.append('O identificador não finaliza com o caractere X')

if erros:
    print('O identificador é invalido\nErros:')
    for erro in erros:
        print(erro)
else:
    print('O identificador é válido')
