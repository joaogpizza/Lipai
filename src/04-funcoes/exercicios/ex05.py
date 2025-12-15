""" Exercicio 05 S2.A4 """

def calcular_imc(individuo):
    """Retorna o IMC de um indivíduo com base na sua altura e peso."""
    return individuo['peso'] / (individuo['altura'] ** 2)

def obter_classificacao(imc):
    """Retorna a classificação com base no IMC."""
    if imc < 18.5:
        return 'Baixo peso'
    elif imc < 25.0:
        return 'Peso normal'
    elif imc < 30.0:
        return 'Excesso de peso'
    elif imc < 35.0:
        return 'Obesidade de Classe 1'
    elif imc < 40:
        return 'Obesidade de Classe 2'
    return 'Obesidade de Classe 3'

def situacao_individuo(imc):
    """Retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no IMC"""
    if imc < 18.5:
        return 'ganhar peso'
    elif imc < 25.0:
        return 'normal'
    return 'perder peso'

breakpoint()
PESO = float(input('Digite seu peso (kg): '))
ALTURA = float(input('Digite sua altura (m): '))

INDIVIDUO = {
    'peso': PESO,
    'altura': ALTURA
}

IMC = calcular_imc(INDIVIDUO)
CLASSIFICACAO = obter_classificacao(IMC)
SITUACAO = situacao_individuo(IMC)

print(f'IMC = {IMC}\n' +
      f'Classificação = {CLASSIFICACAO}\n' +
      f'Situação = {SITUACAO}')
