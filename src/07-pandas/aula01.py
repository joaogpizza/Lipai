import pandas as pd

# Parte 1

data = pd.read_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019.csv')
print(data)

print(data.head())

print(data.head(10))

print(data.info())

print(type(data))

print(data.shape)

print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')

personagens_df = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70.5, 15.2, 60.1],
    'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
})

print(personagens_df)

print(personagens_df.info())

print(personagens_df.columns)

print(type(personagens_df.columns))

print(list(personagens_df.columns))

personagens_df_renomeado = personagens_df.rename(columns={
    'nome': 'Nome Completo',  # renomeia a coluna de nome 'nome' para 'Nome Completo'
    'idade': 'Idade'
})

print(personagens_df_renomeado)

personagens_df.rename(columns={'nome': 'Nome Completo','idade': 'Idade'}, inplace=True)
print(personagens_df)

personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH_JEDI']
print(personagens_df)

# selecionando uma coluna inteira
print(data['ESTADO'])

# selecionando uma coluna inteira
# esta forma de acesso, só funciona para colunas com nomes sem espaços, acentos, etc (caracteres inválidos)
print(data.ESTADO)

print(type(data['ESTADO']))

print(data.iloc[1])

print(type(data.iloc[1]))

print(pd.Series([5.5, 6.0, 9.5]))

print(pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas dos Luke Skywalker'))

produto_view = data['PRODUTO']  # a series retornada refente à coluna, NÃO É UMA CÓPIA, mas sim, uma REFERÊNCIA/VIEW à coluna do dataframe
print(produto_view)

produto_copy_bkp = data['PRODUTO'].copy()  # retorna uma cópia da coluna 'PRODUTO'
print(produto_copy_bkp)

data['PRODUTO'] = 'Combustível'  # atribuindo o valor constante 'Combustível' para linha do dataframe na coluna 'PRODUTO'
print(data.head())
print(produto_view)
print(produto_copy_bkp)

nrows, ncols = data.shape
print(nrows, ncols)

novos_produtos = [f'Produto {i}' for i in range(nrows)]
print(len(novos_produtos))

# a quantidade de elementos da lista `novos_produtos` é igual ao número de linhas do dataframe
data['PRODUTO'] = novos_produtos
print(data)

print(produto_view)
print('\n')
print(produto_copy_bkp)

# voltando para os produtos originais
data['PRODUTO'] = produto_copy_bkp  # produto_copy_bkp é uma Series
print(data)

# criando uma coluna a partir de um valor constante/default
# todas as linhas terão o mesmo valor para esta nova coluna
data['coluna sem nocao'] = 'DEFAULT'
print(data)

data['coluna a partir de lista'] = range(data.shape[0])
print(data)

# não funciona pq a quantidade de elementos da lista (a serem atribuídos a nova coluna) é diferente
# da quantidade de linhas do dataframe
# data['nao funciona'] = [1, 2, 3]

data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0
print(data)

print(data.index)

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['XboxOne', 'Playstation4', 'Switch'])

print(pesquisa_de_satisfacao.head())
print(pesquisa_de_satisfacao.index)

# selecionando as linhas de índice de 0 a 5 (incluso)
print(data.iloc[:6])
print(data.iloc[10:16])

# selecionando as linhas/observações de índice 1, 5, 10, 15
print(data.iloc[[1, 5, 10, 15]])

# selecionando as linhas/observações de índices 5, 1, 15, 10
print(data.iloc[[5, 1, 15, 10]])

# retornar o valor da linha de índice 1, coluna 4 ('ESTADO')
print(data.iloc[1, 4])

# retorna a linha cujo o rótulo do índice é 'XboxOne'
print(pesquisa_de_satisfacao.loc['XboxOne'])

# NÃO FUNCIONA ===> iloc tentando acessar índices com rótulos
# print(pesquisa_de_satisfacao.iloc['XboxOne'])

# NÃO FUNCIONA ===> loc tentando acessar índices rotulados com números
# print(pesquisa_de_satisfacao.loc[0])

# retorna o valor da linha 'Playstation4', coluna 'ruim'
print(pesquisa_de_satisfacao.loc['Playstation4', 'ruim'])

# selecionando as linhas de índices rotulados 'XboxOne', 'Switch'
print(pesquisa_de_satisfacao.loc[['XboxOne', 'Switch']])

# retorna todas as linhas e apenas as colunas com rótulos 'bom' e 'pessimo'
print(pesquisa_de_satisfacao[['bom', 'pessimo']])

# retorna todas as linhas e apenas as colunas com rótulos 'bom' e 'pessimo'
print(pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']])

# selecionando múltiplas colunas: 'PRODUTO', 'ESTADO', 'REGIÃO'
print(data[['PRODUTO', 'ESTADO', 'REGIÃO']])

# deleta/remove in-place (ou seja, no próprio dataframe) a coluna de rótulo 'Unnamed: 0'
# del data['Unnamed: 0']
print(data)

del data['coluna sem nocao']
del data['coluna a partir de lista']
del data['PREÇO MÉDIO REVENDA (dólares)']

print(data.head())

data.to_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019.csv', index=False)

data = pd.read_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019.csv')
print(data.head())

# Mostra todos os estados cujos os preços dos combustíveis foram aferidos
# Mais tecnicamente, mostra os valores únicos presentes para o atributo/coluna 'ESTADO'.
print(data['ESTADO'].unique())

# faz uma comparação elemento a elemento da series, retornando uma Series de booleans
print(data['ESTADO'] == 'SAO PAULO')

# salvando essa Series de booleans em uma variável
selecao = data['ESTADO'] == 'SAO PAULO'
print(selecao)
print(type(selecao))

print(selecao.shape)
print(data.shape)

print(data[selecao])
print(data.loc[selecao])

print(data.query('ESTADO == "SAO PAULO"'))

postos_sp = data.query('ESTADO == "SAO PAULO"')
print(postos_sp)

print(type(postos_sp))
print(postos_sp.shape)
print(postos_sp)

print(postos_sp.reset_index())

print(postos_sp.reset_index(drop=True))

postos_sp.reset_index(drop=True, inplace=True)
print(postos_sp)

postos_sp = data.query('ESTADO == "SAO PAULO"').reset_index(drop=True)
print(postos_sp)

selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0)
print(selecao)

print(data[selecao])

# Não funciona
# data.query('ESTADO=="RIO DE JANEIRO" and PREÇO MÉDIO REVENDA > 2')

print(data.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"'))

selecao_1 = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[selecao_1]
print(postos_rj)

selecao_2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2
print(selecao_2)

postos_rj_preco_maior_que_2 = postos_rj[selecao_2]
print(postos_rj_preco_maior_que_2)


selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO')
selecao_2 = (data['PRODUTO'] == 'GASOLINA COMUM')
selecao_3 = (data['PREÇO MÉDIO REVENDA'] > 2)

selecao_final = selecao_1 & selecao_2 & selecao_3
print(selecao_final)

data_filtrado = data[selecao_final]
print(data_filtrado)

print(data_filtrado['ESTADO'].unique())
print(data_filtrado['PRODUTO'].unique())

selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO')
postos_sp_rj = data[selecao_1]

# apenas registros de postos dos estados de SP e RJ
print(postos_sp_rj)

selecao_2 = (postos_sp_rj['PRODUTO'] == 'GASOLINA COMUM')
postos_sp_rj_gasolina = postos_sp_rj[selecao_2]

# apenas registros de postos dos estados de SP e RJ cujo produto é GASOLINA COMUM
print(postos_sp_rj_gasolina)

selecao_3 = (postos_sp_rj_gasolina['PREÇO MÉDIO REVENDA'] > 2)

postos_sp_rj_gasolina_preco_maior_que_2 = postos_sp_rj_gasolina[selecao_3]
print(postos_sp_rj_gasolina_preco_maior_que_2)

selecao = (data['ANO'] == 2008) | (data['ANO'] == 2010) | (data['ANO'] == 2012)
print(data[selecao])

lista_de_anos = [2008, 2010, 2012]
selecao = data['ANO'].isin(lista_de_anos)  # retorna uma Series de booleanos
print(data[selecao])

print(data.query('ANO in @lista_de_anos'))

for index, row in data.head(10).iterrows():
    print(f'indice {index} ==> {row["ESTADO"]}')
