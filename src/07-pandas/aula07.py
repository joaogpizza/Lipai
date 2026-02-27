import pandas as pd

# Parte 7

data_final = pd.read_csv('D:/LIPAI/src/07-pandas/GasPricesinBrazil_2004-2019_preprocessado_final.csv')

print(data_final.query('ANO != 2019'))

df = data_final.query('ANO != 2019')
print(df)

grupos = df.groupby('PRODUTO')
print(grupos['REGIÃO'].value_counts().to_frame())

gasolina_sp_2018 = df.query('PRODUTO == "GASOLINA COMUM" and ESTADO == "SAO PAULO" and ANO == 2018')
print(gasolina_sp_2018.head())

print(gasolina_sp_2018.shape)

print(gasolina_sp_2018.describe())

print(gasolina_sp_2018['PREÇO MÉDIO REVENDA'].describe().to_frame())

print(df.query('(PRODUTO == "GASOLINA COMUM" or PRODUTO == "ETANOL HIDRATADO") and ESTADO == "SAO PAULO" and ANO == 2018'))

lista_de_estados = ["GASOLINA COMUM", "ETANOL HIDRATADO"]
print(df.query('PRODUTO in @lista_de_estados and ESTADO == "SAO PAULO" and ANO == 2018'))

gasolina_etanol_sp_2018 = df.query('PRODUTO in ["GASOLINA COMUM", "ETANOL HIDRATADO"] and ESTADO == "SAO PAULO" and ANO == 2018')
print(gasolina_etanol_sp_2018)

# considerando os preços do etanol e da gasolina juntos, teremos essas estatística descritivas 
print(gasolina_etanol_sp_2018['PREÇO MÉDIO REVENDA'].describe().to_frame())

print(gasolina_etanol_sp_2018.groupby('PRODUTO')['PREÇO MÉDIO REVENDA'].describe())
