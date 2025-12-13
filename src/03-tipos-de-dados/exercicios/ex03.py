""" Ex 03 S2.A3 """

MESES = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

while(True):
    MES = int(input('Digite o mês em formato numérico: '))
    if 0 < MES <= 12:
        print(MESES[MES])
        break
    else:
        print('Número não corresponde a um mês, tente novamente\n')
