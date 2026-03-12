""" Exercicio 03, 04 e 05 S7A2"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db = pd.read_csv('src/07-preparacao-de-dados/wine.csv')

# Exercicio 3
# Primeiro, tirar cédulas de forma randômica do db
df = db.copy()
rng = np.random.default_rng(42)
taxa_erro = 0.10

mascara = pd.DataFrame(False, index=df.index, columns=df.columns)
for col in df.columns:
    if col == 'Class':
        continue
    mascara_coluna = rng.random(len(df)) < taxa_erro
    mascara_coluna = mascara_coluna & ~df[col].isna()
    df.loc[mascara_coluna, col] = np.nan
    mascara[col] = mascara_coluna

# Segundamente, imputar os valores
imp_media = df.copy()
imp_mediana = df.copy()
imp_moda = df.copy()

for col in df.columns:
    if col == 'Class':
        continue
    col_orig = db[col]
    media = col_orig.mean()
    mediana = col_orig.median()
    imp_media[col].fillna(media, inplace=True)
    imp_mediana[col].fillna(mediana, inplace=True)
    moda = col_orig.mode().iloc[0] if not col_orig.mode().empty else col_orig.dropna().iloc[0]
    imp_moda[col].fillna(moda, inplace=True)

# Exercicio 4
# Histogramas da media
fig, eixos = plt.subplots(3, 5, figsize=(15, 9))
eixos[0,0].set_title('Alcohol')
eixos[0,0].hist(imp_media['Alcohol'], bins=10)
eixos[0,1].set_title('MalicAcid')
eixos[0,1].hist(imp_media['MalicAcid'], bins=10)
eixos[0,2].set_title('Ash')
eixos[0,2].hist(imp_media['Ash'], bins=10)
eixos[0,3].set_title('AlcalinityOfAsh')
eixos[0,3].hist(imp_media['AlcalinityOfAsh'], bins=10)
eixos[0,4].set_title('Magnesium')
eixos[0,4].hist(imp_media['Magnesium'], bins=10)
eixos[1,0].set_title('TotalPhenols')
eixos[1,0].hist(imp_media['TotalPhenols'], bins=10)
eixos[1,1].set_title('Flavanoids')
eixos[1,1].hist(imp_media['Flavanoids'], bins=10)
eixos[1,2].set_title('NonflavanoidPhenols')
eixos[1,2].hist(imp_media['NonflavanoidPhenols'], bins=10)
eixos[1,3].set_title('Proanthocyanins')
eixos[1,3].hist(imp_media['Proanthocyanins'], bins=10)
eixos[1,4].set_title('ColorIntensity')
eixos[1,4].hist(imp_media['ColorIntensity'], bins=10)
eixos[2,0].set_title('Hue')
eixos[2,0].hist(imp_media['Hue'], bins=10)
eixos[2,1].set_title('Od280/Od315OfDilutedWines')
eixos[2,1].hist(imp_media['Od280/Od315OfDilutedWines'], bins=10)
eixos[2,2].set_title('Proline')
eixos[2,2].hist(imp_media['Proline'], bins=10)
fig.suptitle('Impute por média')
fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

fig, eixos = plt.subplots(3, 5, figsize=(15, 9))
eixos[0,0].set_title('Alcohol')
eixos[0,0].hist(imp_mediana['Alcohol'], bins=10)
eixos[0,1].set_title('MalicAcid')
eixos[0,1].hist(imp_mediana['MalicAcid'], bins=10)
eixos[0,2].set_title('Ash')
eixos[0,2].hist(imp_mediana['Ash'], bins=10)
eixos[0,3].set_title('AlcalinityOfAsh')
eixos[0,3].hist(imp_mediana['AlcalinityOfAsh'], bins=10)
eixos[0,4].set_title('Magnesium')
eixos[0,4].hist(imp_mediana['Magnesium'], bins=10)
eixos[1,0].set_title('TotalPhenols')
eixos[1,0].hist(imp_mediana['TotalPhenols'], bins=10)
eixos[1,1].set_title('Flavanoids')
eixos[1,1].hist(imp_mediana['Flavanoids'], bins=10)
eixos[1,2].set_title('NonflavanoidPhenols')
eixos[1,2].hist(imp_mediana['NonflavanoidPhenols'], bins=10)
eixos[1,3].set_title('Proanthocyanins')
eixos[1,3].hist(imp_mediana['Proanthocyanins'], bins=10)
eixos[1,4].set_title('ColorIntensity')
eixos[1,4].hist(imp_mediana['ColorIntensity'], bins=10)
eixos[2,0].set_title('Hue')
eixos[2,0].hist(imp_mediana['Hue'], bins=10)
eixos[2,1].set_title('Od280/Od315OfDilutedWines')
eixos[2,1].hist(imp_mediana['Od280/Od315OfDilutedWines'], bins=10)
eixos[2,2].set_title('Proline')
eixos[2,2].hist(imp_mediana['Proline'], bins=10)
fig.suptitle('Impute por mediana')
fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

fig, eixos = plt.subplots(3, 5, figsize=(15, 9))
eixos[0,0].set_title('Alcohol')
eixos[0,0].hist(imp_moda['Alcohol'], bins=10)
eixos[0,1].set_title('MalicAcid')
eixos[0,1].hist(imp_moda['MalicAcid'], bins=10)
eixos[0,2].set_title('Ash')
eixos[0,2].hist(imp_moda['Ash'], bins=10)
eixos[0,3].set_title('AlcalinityOfAsh')
eixos[0,3].hist(imp_moda['AlcalinityOfAsh'], bins=10)
eixos[0,4].set_title('Magnesium')
eixos[0,4].hist(imp_moda['Magnesium'], bins=10)
eixos[1,0].set_title('TotalPhenols')
eixos[1,0].hist(imp_moda['TotalPhenols'], bins=10)
eixos[1,1].set_title('Flavanoids')
eixos[1,1].hist(imp_moda['Flavanoids'], bins=10)
eixos[1,2].set_title('NonflavanoidPhenols')
eixos[1,2].hist(imp_moda['NonflavanoidPhenols'], bins=10)
eixos[1,3].set_title('Proanthocyanins')
eixos[1,3].hist(imp_moda['Proanthocyanins'], bins=10)
eixos[1,4].set_title('ColorIntensity')
eixos[1,4].hist(imp_moda['ColorIntensity'], bins=10)
eixos[2,0].set_title('Hue')
eixos[2,0].hist(imp_moda['Hue'], bins=10)
eixos[2,1].set_title('Od280/Od315OfDilutedWines')
eixos[2,1].hist(imp_moda['Od280/Od315OfDilutedWines'], bins=10)
eixos[2,2].set_title('Proline')
eixos[2,2].hist(imp_moda['Proline'], bins=10)
fig.suptitle('Impute por moda')
plt.show()

# Exercicio 5
fig, eixos = plt.subplots(3, 5, figsize=(15, 9))

fig, eixos = plt.subplots(3, 5, figsize=(15, 9))

colunas = [
    ('Alcohol', 0, 0), ('MalicAcid', 0, 1), ('Ash', 0, 2),
    ('AlcalinityOfAsh', 0, 3), ('Magnesium', 0, 4),
    ('TotalPhenols', 1, 0), ('Flavanoids', 1, 1), ('NonflavanoidPhenols', 1, 2),
    ('Proanthocyanins', 1, 3), ('ColorIntensity', 1, 4),
    ('Hue', 2, 0), ('Od280/Od315OfDilutedWines', 2, 1), ('Proline', 2, 2),
]

for col, i, j in colunas:
    dados = [
        db[col].dropna().values,
        imp_media[col].dropna().values,
        imp_mediana[col].dropna().values,
        imp_moda[col].dropna().values,
    ]
    eixos[i, j].set_title(col)
    eixos[i, j].boxplot(dados)
    eixos[i, j].set_xticklabels(['Orig', 'Media', 'Mediana', 'Moda'])

eixos[2, 3].set_visible(False)
eixos[2, 4].set_visible(False)

fig.suptitle('Original vs Imputações')
plt.show()

# Os atributos com distribuição mais simétrica são: Hue, TotalPhenols, Alcohol e AlcalinityOfAsh.
# Sim, há outliers dentre os atributos Hue, Proanthocyanins, ColorIntensity, Magnesium, AlcalinityOfAsh,
# Ash e MalicAcid
