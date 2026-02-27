""" Exercicio 1 S6A2 """

import pandas as pd
import os

# Caminho absoluto baseado no local do ex01.py
caminho = os.path.join(os.path.dirname(__file__), "classification_results_trial_0001.csv")

df = pd.read_csv(caminho)

# Item 1:
benign_malign = df.groupby('real_class').count()['image_path']
benign = int(benign_malign.get('benign', 0))
malign = int(benign_malign.get('malign', 0))
print(f'1) Existe {benign} imagens "benign" e {malign} imagens "malign"')

# Item 2:
errou = df.query('real_class != predicted_class')
print('\n2) Imagens em que errou:')
for imagem in errou['image_path']:
    print(imagem)

# Item 3: (Nota: confiança foi tratada como superior a 0.75)
def confianca(linha):
    if linha['predicted_class'] == 'benign':
        return linha['prob_benign']
    else:
        return linha['prob_malign']
errou['confianca'] = errou.apply(confianca, axis=1)
errou_confiante = errou[errou['confianca'] > 0.75]
print('\n3) Errou de forma confiante:')
for imagem in errou_confiante['image_path']:
    print(imagem)

# Item 4:
positivo = 'malign'
negativo = 'benign'

TP = ((df['real_class'] ==positivo) & (df['predicted_class'] ==positivo)).sum()
TN = ((df['real_class'] == negativo) & (df['predicted_class'] == negativo)).sum()
FP = ((df['real_class'] == negativo) & (df['predicted_class'] ==positivo)).sum()
FN = ((df['real_class'] ==positivo) & (df['predicted_class'] == negativo)).sum()

print(f"\n4) TP: {TP}")
print(f"TN: {TN}")
print(f"FP: {FP}")
print(f"FN: {FN}")

# Item 5:
print(f'\n5) Acurácia: {(TP + TN)/(TP + TN + FP + FN)}')
print(f'Precisão: {TP/(TP+FP)}')
print(f'Recall: {TP/(TP+FN)}')
print(f'Especificidade: {TN/(TN+FP)}')

# Item 6:
menor_prob_benign = df.sort_values(by='prob_benign')
top_menor_prob_benign = (menor_prob_benign.query('real_class == "benign"')).head()
print('\n6) 5 benigns com menor prob_benign:')
for linha in top_menor_prob_benign.itertuples(index=False):
    print(f'{linha.image_path}: {linha.prob_benign:.4f}')

# Item 7:
maior_prob_benign = df.sort_values(by='prob_benign', ascending= False)
top_maior_prob_benign = (maior_prob_benign.query('real_class == "malign"')).head(5)
print('\n7) 5 maligns com maior prob_benign:')
for linha in top_maior_prob_benign.itertuples(index=False):
    print(f'{linha.image_path}: {linha.prob_benign:.4f}')
