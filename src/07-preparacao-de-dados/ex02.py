""" Exercicio 02 S7A2 """

import matplotlib.pyplot as plt
import pandas as pd

db = pd.read_csv('src/07-preparacao-de-dados/wine.csv')

fig, eixos = plt.subplots(3, 5)

eixos[0,0].set_title('Alcohol')
eixos[0,0].hist(db['Alcohol'], bins=10)

eixos[0,1].set_title('MalicAcid')
eixos[0,1].hist(db['MalicAcid'], bins=10)

eixos[0,2].set_title('Ash')
eixos[0,2].hist(db['Ash'], bins=10)

eixos[0,3].set_title('AlcalinityOfAsh')
eixos[0,3].hist(db['AlcalinityOfAsh'], bins=10)

eixos[0,4].set_title('Magnesium')
eixos[0,4].hist(db['Magnesium'], bins=10)

eixos[1,0].set_title('TotalPhenols')
eixos[1,0].hist(db['TotalPhenols'], bins=10)

eixos[1,1].set_title('Flavanoids')
eixos[1,1].hist(db['Flavanoids'], bins=10)

eixos[1,2].set_title('NonflavanoidPhenols')
eixos[1,2].hist(db['NonflavanoidPhenols'], bins=10)

eixos[1,3].set_title('Proanthocyanins')
eixos[1,3].hist(db['Proanthocyanins'], bins=10)

eixos[1,4].set_title('ColorIntensity')
eixos[1,4].hist(db['ColorIntensity'], bins=10)

eixos[2,0].set_title('Hue')
eixos[2,0].hist(db['Hue'], bins=10)

eixos[2,1].set_title('Od280/Od315OfDilutedWines')
eixos[2,1].hist(db['Od280/Od315OfDilutedWines'], bins=10)

eixos[2,2].set_title('Proline')
eixos[2,2].hist(db['Proline'], bins=10)

plt.show()
