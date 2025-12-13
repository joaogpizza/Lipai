""" Ex 02 S2.A3 """

MESES = ('Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro')
while(True):
    MES = int(input('Digite o mês em formato numérico: '))
    if 0 < MES <= 12:
        print(MESES[MES-1])
        break
    else:
        print('Número não corresponde a um mês, tente novamente\n')
