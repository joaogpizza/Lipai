import pandas as pd

# Parte 3

data_final = pd.read_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019_preprocessado_final.csv')
print(data_final)

print(data_final.describe())

print(data_final['PREÇO MÉDIO REVENDA'].describe())

print(data_final.describe()['PREÇO MÉDIO REVENDA'])

stats = data_final.describe()
print(stats)

print(stats[['PREÇO MÉDIO REVENDA', 'PREÇO MÁXIMO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO']])

# ALTERNATIVA MAIS EFICIENTE
# apenas computa as estatísticas descritivas para 3 atributos
print(data_final[['PREÇO MÉDIO REVENDA', 'PREÇO MÁXIMO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO']].describe())

print(stats.loc[['min', 'max', 'mean']])

print(stats.loc[['min', 'max', 'mean'], 'PREÇO MÉDIO REVENDA'])

print(stats.loc[['min', 'max', 'mean'], ['PREÇO MÉDIO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO']])

print(data_final['PREÇO MÍNIMO REVENDA'].min())

mean = data_final['PREÇO MÍNIMO REVENDA'].mean()
std = data_final['PREÇO MÍNIMO REVENDA'].std()

print(f'A média dos preços mínimos de revenda é {mean:.2f} +- {std:.2f}')

print(sorted(data_final['ESTADO'].unique()))

print(data_final['ESTADO'].value_counts())  # retorna em ordem decrescente, a quantidade de registros/linhas para cada estado

print(data_final['ESTADO'].value_counts().to_frame())  # converte uma Series para um DataFrame

data_final.to_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019_preprocessado_final.csv', index= False)
