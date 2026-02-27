import pandas as pd

# Parte 2

data = pd.read_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019.csv')

print(data.info())

data_pre = data.copy()

data_pre['DATA INICIAL'] = pd.to_datetime(data_pre['DATA INICIAL'])
data_pre['DATA FINAL'] = pd.to_datetime(data_pre['DATA FINAL'])

print(data_pre.info())

# convertendo atributos/colunas para 'numeric'
for atributo in ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']:
    # converte a coluna (de valores string) para um tipo numérico
    # Em caso de erro na conversão (p. ex., uma string que não representa um número), um valor vazio (null / nan) será
    # atribuído no lugar
    data_pre[atributo] = pd.to_numeric(data_pre[atributo], errors='coerce')

print(data_pre.info())

mask = data_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()
print(data_pre[mask])
# Nos dados originais, quais eram os valores do PREÇO MÉDIO DISTRIBUIÇÃO dos registros que agora possuem valores NaN 
print(data[mask])

# Retorna uma cópia do data fram `data_pre` com todos os valores NaN de todas as colunas agora preenchidos com 0.
# Para alterar o próprio data frame, use o argumento `inplace=True`.
data_pre_fill = data_pre.fillna(0)
print(data_pre_fill)
print(data_pre_fill[mask])

# retorna uma cópia do data frame `data_pre` com todos os valores NaN das colunas:
# 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO' e 'PREÇO MÁXIMO DISTRIBUIÇÃO', respectivamente, com os valores: 10, 20, 30, 'vazio'.
data_pre_fill = data_pre.fillna(value={
    'PREÇO MÉDIO DISTRIBUIÇÃO': 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
})

print(data_pre_fill[mask])

# remove, no próprio dataframe, todas as linhas/registros com valores NaN (vazios) em quaisquer colunas/atributos.
data_pre.dropna(inplace=True)
print(data_pre.info())

data_pre.to_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019_preprocessado_final.csv', index=False)
