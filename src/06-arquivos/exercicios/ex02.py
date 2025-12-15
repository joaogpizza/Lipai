""" Ex 02 S3.A2 """

def carregar_dados_projetos(nome_arquivo):
    """ Retorna uma tupla de dicionários com dados de projetos. """

    dicionarios = []
    
    with open(nome_arquivo, 'r', encoding='utf8') as arq:
        linhas = arq.readlines()
        for linha in linhas:
            linha.strip('\n')
            infos = linha.split(',')
            dicionario = {
                'codigo': int(infos[0]),
                'titulo': infos[1],
                'responsavel': infos[2]
            }
            dicionarios.append(dicionario)
    
    resultado = tuple(dicionarios)
    return resultado


tupla = carregar_dados_projetos("src/06-arquivos/exercicios/txtex02.txt")

for projeto in tupla:
    print(f'Código: {projeto['codigo']}\n' +
          f'Título: {projeto['titulo']}\n' +
          f'Responsável: {projeto['responsavel']}\n' +
          '-----------------------------------\n')
