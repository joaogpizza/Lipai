import pandas as pd

# Parte 5

data_final = pd.read_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019_preprocessado_final.csv')

# agrupa as linhas da tablea de acordo com suas respectivas regiões
grupos = data_final.groupby('REGIÃO')
print(grupos)

# retorna os grupos obtidos pelo groupby
print(grupos.groups)

# retorna os índices das linhas/observações de cada grupo
print(grupos.indices)

# retorna um dataframe apenas com as observações do grupo 'CENTRO OESTE'
print(grupos.get_group('CENTRO OESTE'))

# descreva para nós algumas estatística descritivas para as observações de cada grupo
print(grupos.describe())

# print(grupos.mean()) (não funciona +, função mean antigamente ignorava colunas não numéricas)

print(grupos.min())

print(data_final.groupby('REGIÃO').min())

# Agrupa os registros do dataframe primeiramente por suas regiões.
# Então, agrupa os registros de cada região (grupo) de acordo com seus produtos.
grupos = data_final.groupby(['REGIÃO', 'PRODUTO'])
print(grupos)

print(grupos.groups)

# print(grupos.mean())

print(grupos['PREÇO MÉDIO REVENDA'].mean())

print(grupos['PREÇO MÉDIO REVENDA'].describe())

df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [None, None, None]],
                  columns=['A', 'B', 'C'])
print(df)

print(df.agg([sum, min]))  # ignora o nan

grupos = data_final.groupby('REGIÃO')
print(grupos)

# Computa o menor e maior valor do 'PREÇO MÉDIO REVENDA' para cada região (grupo)
print(grupos['PREÇO MÉDIO REVENDA'].agg([min, max]))
