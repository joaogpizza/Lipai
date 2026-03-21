""" Exercicio S8A1 """

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score

# Primeira parte: Carregando o dataset e dividindo entre teste e treino

CAMINHO_CSV = os.path.join(os.path.dirname(__file__), "mental_health_risk_dataset.csv")

db = pd.read_csv(CAMINHO_CSV)

divisao = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for index_treino, index_teste in divisao.split(db, db['employment_status']):
    con_treino = db.loc[index_treino]
    con_teste = db.loc[index_teste]

db = con_treino.drop("mental_health_risk", axis=1)
label = con_treino["mental_health_risk"].copy()

# Segunda parte: Pré-processamento do dataset

db_num = db.select_dtypes(include=[np.number])
db_cat = db.select_dtypes(include=['string'])

pipeline_num = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('std_scaler', StandardScaler())
])

atr_num = list(db_num)
atr_cat = list(db_cat)

pipeline_completa = ColumnTransformer([
    ("num", pipeline_num, atr_num),
    ("cat", OneHotEncoder(), atr_cat)
])
db_preparado = pipeline_completa.fit_transform(db)

# Terceira parte: Comparação entre os modelos

def mostrar_scores(scores):
    print("Scores:", scores)
    print("Media:", scores.mean())
    print("Desvio Padrao:", scores.std())

reg_linear = LinearRegression()
reg_linear.fit(db_preparado, label)

reg_arvore = DecisionTreeRegressor(random_state=42)
reg_arvore.fit(db_preparado, label)

reg_floresta = RandomForestRegressor(random_state=42)
reg_floresta.fit(db_preparado, label)

scores = cross_val_score(reg_linear, db_preparado, label, scoring="neg_mean_squared_error", cv=10)
rmse_scores_linear = np.sqrt(-scores)

scores = cross_val_score(reg_arvore, db_preparado, label, scoring="neg_mean_squared_error", cv=10)
rmse_scores_arvore = np.sqrt(-scores)

scores = cross_val_score(reg_floresta, db_preparado, label, scoring="neg_mean_squared_error", cv=10)
rmse_scores_floresta = np.sqrt(-scores)

print('Regressao Linear:')
mostrar_scores(rmse_scores_linear)
print('\nRegressao por arvore de decisao:')
mostrar_scores(rmse_scores_arvore)
print('\nRegressao por Random Forest:')
mostrar_scores(rmse_scores_floresta)

modelo_medias_desvio = {
    'linear': (rmse_scores_linear.mean(), rmse_scores_linear.std()),
    'arvore': (rmse_scores_arvore.mean(), rmse_scores_arvore.std()),
    'floresta': (rmse_scores_floresta.mean(), rmse_scores_floresta.std())
}

menor_media = min(modelo_medias_desvio, key=lambda k: modelo_medias_desvio[k][0])
menor_desvio = min(modelo_medias_desvio, key=lambda k: modelo_medias_desvio[k][1])
melhor = min(modelo_medias_desvio, key=lambda k: modelo_medias_desvio[k][0] + 2*modelo_medias_desvio[k][1])

print('\nMenor media de scores: ',menor_media,' (',modelo_medias_desvio[menor_media][0],')', sep='')
print('\nMenor desvio padrao de scores: ',menor_desvio,' (',modelo_medias_desvio[menor_desvio][1],')', sep='')
print('\nMelhor Overall (média baixa e estável):',melhor)
