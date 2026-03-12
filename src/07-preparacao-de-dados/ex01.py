""" Exercicio 01 S7A2 """

import pandas as pd
from pandas.api.types import is_numeric_dtype

db = pd.read_csv('src/07-preparacao-de-dados/wine.csv')

for col in db.columns:
    if col == 'Class':
        continue
    if is_numeric_dtype(db[col]):
        print('%s:' % (col))
        print('\t Média = %.2f' % db[col].mean())
        print('\t Mediana = %.2f' % db[col].median())
        print('\t Desvio padrão = %.2f' % db[col].std())
        print('\t Variância = %.2f' % db[col].var())
        print('\t Mínimo = %.2f' % db[col].min())
        print('\t Máximo = %.2f' % db[col].max())
