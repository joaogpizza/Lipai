""" Exercicio 06 S2.A4 """

def calcular_volume(informacoes):
    """ Calcula o volume por meio das informacoes fornecidas """
    return (informacoes['comprimento'] * informacoes['altura'] * informacoes['largura'] / 1000)

def potencia_termostato(informacoes):
    """ Calcula a potência do termostato por meio das informacoes fornecidas """
    volume = calcular_volume(informacoes)
    return volume * 0.05 * (informacoes['temperatura desejada'] - informacoes['temperatura ambiente'])

def faixa_filtragem(informacoes):
    """ Calcula a faixa mínima e máxima de filtragem recomendada """
    volume = calcular_volume(informacoes)
    return (2*volume, 3*volume)

breakpoint()
COMPRIMENTO = float(input('Digite o comprimento do aquário, em cm: '))
ALTURA = float(input('Digite a altura do aquário, em cm: '))
LARGURA = float(input('Digite a largura do aquário, em cm: '))
TEMP_DESEJADA = float(input('Digite a temperatura desejada'))
TEMP_AMBIENTE = float(input('Digite a temperatura ambiente: '))

INFOS = {
    'comprimento': COMPRIMENTO,
    'altura': ALTURA,
    'largura': LARGURA,
    'temperatura desejada': TEMP_DESEJADA,
    'temperatura ambiente': TEMP_AMBIENTE
}

VOLUME = calcular_volume(INFOS)
POTENCIA = potencia_termostato(INFOS)
FAIXA_FILTRAGEM = faixa_filtragem(INFOS)

print(f'Volume: {VOLUME} Litros\n' +
      f'Potência requirida do termostato: {POTENCIA}\n' +
      f'Filtragem mínima: {FAIXA_FILTRAGEM[0]}\n' +
      f'Filtragem máxima: {FAIXA_FILTRAGEM[1]}')
