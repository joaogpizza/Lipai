""" Exercício 03 S3.A2"""

def linha_para_dict(linha, chaves):
    """ Recebe uma linha e uma lista de chaves e retorna um dicionário. """
    
    dicionario = {}
    
    linha.strip('\n')
    infos = linha.split(',')
    if len(infos) != len(chaves):
        print('ERRO: menos informações do que necessário')
        return dicionario
    for i in range(len(infos)):
        dicionario[chaves[i]] = infos[i]
    return dicionario

print(linha_para_dict('SP000001,Maria da Silva,maria@email.com', ['prontuario','nome','email']))
print(linha_para_dict('banana,3', ['item', 'quantidade']))
