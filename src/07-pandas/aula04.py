import pandas as pd

# Parte 4

df = pd.DataFrame({ 'A': [1, 2, 3, 4], 
                    'B': [10, 20, 30, 40],
                    'C': [100, 200, 300, 400]}, 
                     index=['Linha 1', 'Linha 2', 'Linha 3', 'Linha 4'])

print(df)

def nossa_soma(series):
    return series.sum()  # retorna a soma de todos os valores de uma series

# aplica a função soma para cada linha do dataframe
df['SOMA(A, B, C)'] = df.apply(nossa_soma, axis=1)
print(df)

# aplica a função soma para cada coluna do dataframe
df.loc['Linha 5'] = df.apply(nossa_soma, axis=0)
print(df)

df['MEDIA(A, B, C)'] = df[['A', 'B', 'C']].apply(lambda series: series.mean(), axis=1)
print(df)

# Aplica a lambda function abaixo para cada elemento da coluna
df['C * 2'] = df['C'].apply(lambda x: x * 2)
print(df)

df['A * 2'] = df['A'] * 2
print(df)

# retorna um novo dataframe com todos os elementos ao quadrado.
# poderíamos usar uma função ao invés de uma lambda function
print(df.map(lambda x: x ** 2))
print(df)

nomes = pd.Series(['João', 'Maria', 'Alice', 'Pedro'])
print(nomes)

# retorna uma nova Series com todos os nomes com letras maiuscúlas.
# poderíamos usar uma função ao invés de uma lambda function
print(nomes.map(lambda x: x.upper()))

# O Pandas já fornece uma série de métodos para manipulação de strings.
# Assim, poderíamos usar o código abaixo para obter o mesmo resultado.
print(nomes.str.upper())
