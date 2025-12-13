""" Ex 02 """

MEDIA_APROVACAO = 6.0
MEDIA_RECUPERACAO = 4.0

NOTAS_STRING = input('Digite as notas no formato n1, n2, n3, nm: \n')

NOTAS = NOTAS_STRING.split(',')

media = 0.0
for nota in NOTAS:
    media += float(nota)

media /= len(NOTAS)

if media >= MEDIA_APROVACAO:
    print('aprovado')
elif media >= MEDIA_RECUPERACAO:
    print('recuperação')
else:
    print('reprovado')
