""" Exercicio 01 S3.A2 """

def carregar_dados_alunos(nome_arquivo):
    """ Retorna uma tupla de dicionários com dados de alunos. """
    resultado = ()

    with open(nome_arquivo, "r", encoding="utf8") as arq:
        linhas = arq.readlines()
        dicionarios = []
        for linha in linhas:
            linha.strip('\n')
            infos = linha.split(',')
            dicionario = {
                'prontuario': infos[0],
                'nome': infos[1],
                'email': infos[2]
            }
            dicionarios.append(dicionario)
    
    resultado = tuple(dicionarios)
    return resultado


tupla = carregar_dados_alunos("src/06-arquivos/exercicios/txtex01.txt")

for aluno in tupla:
    print(f'Prontuário: {aluno['prontuario']}\n' +
          f'Nome: {aluno['nome']}\n' +
          f'Email: {aluno['email']}\n' +
          '-----------------------------------\n')
