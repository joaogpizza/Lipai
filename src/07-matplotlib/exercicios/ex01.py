""" Ex 01 S6A3 """

import os
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

caminho = os.path.join(os.path.dirname(__file__), "classification_results_trial_0001.csv")

df = pd.read_csv(caminho)
# Item 1:
benign_malign = df.groupby('real_class').count()['image_path']
benign = int(benign_malign.get('benign', 0))
malign = int(benign_malign.get('malign', 0))
salto = 5
plt.bar(np.array([f'Benigno\n{benign}', f'Maligno\n{malign}']),
        np.array([benign, malign]),
        width=0.3)
plt.title('Contagem por real_class')
plt.ylabel('real_class')
plt.yticks(np.arange(0, 100+salto, salto))
plt.show()

# Item 2:
predicted_benign_malign = df.groupby('predicted_class').count()['image_path']
predicted_benign = int(predicted_benign_malign.get('benign', 0))
predicted_malign = int(predicted_benign_malign.get('malign', 0))
salto = 5
plt.bar(np.array([f'Benigno\n{predicted_benign}', f'Maligno\n{predicted_malign}']),
        np.array([predicted_benign, predicted_malign]),
        width=0.3)
plt.title('Contagem por predicted_class')
plt.ylabel('predicted_class')
plt.yticks(np.arange(0, 100+salto, salto))
plt.show()

# Item 3
probs_benign = np.asarray(df['prob_benign'])
qtd_intervalos = 10
salto = (probs_benign.max()-probs_benign.min()) / qtd_intervalos
plt.hist(probs_benign, bins=qtd_intervalos, edgecolor='black', lw=0.6, alpha=0.9)
plt.xlabel('prob_benign')
plt.xticks(np.arange(probs_benign.min(), probs_benign.max() + salto, salto))
plt.ylabel('contagem')
plt.title('Histograma de prob_benign')
plt.show()

# Item 4
probs_malign = np.asarray(df['prob_benign'])
qtd_intervalos = 20
salto = (probs_malign.max()-probs_malign.min()) / qtd_intervalos
plt.hist(probs_malign, bins=qtd_intervalos, edgecolor='black', lw=0.6, alpha=0.9)
plt.xlabel('prob_malign')
plt.xticks(np.arange(probs_malign.min(), probs_malign.max() + salto, salto))
plt.ylabel('contagem')
plt.title('Histograma de prob_malign')
plt.show()

# Item 5
x = np.asarray(df['prob_benign'])
y = np.asarray(df['prob_malign'])
real = np.asarray(df['real_class'])
pred = np.asarray(df['predicted_class'])
mask_ok = (real == pred)
mask_err = ~mask_ok
plt.scatter(x[mask_ok], y[mask_ok], s=30, alpha=0.7, label='acerto')
plt.scatter(x[mask_err], y[mask_err], s=30, alpha=0.8, marker='x', label='erro')
plt.xlabel('prob_benign')
plt.ylabel('prob_malign')
plt.title('Scatter plot: prob_benign vs prob_malign')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Item 6
# O mais comum é o falso negativo, com 9 ocorrências, enquanto
# o falso positivo tem apenas 3 ocorrências
# Código para criar o gráfico:
positivo = 'malign'
negativo = 'benign'
FP = ((df['real_class'] == negativo) & (df['predicted_class'] ==positivo)).sum()
FN = ((df['real_class'] ==positivo) & (df['predicted_class'] == negativo)).sum()
salto = 1
plt.bar(np.array([f'FP\n{FP}', f'FN\n{FN}']),
        np.array([FP, FN]))
plt.title('FP vs FN')
plt.ylabel('Quantidade')
plt.yticks(np.arange(0, 20+salto, salto))
plt.show()

# Item 7
# No contexto médico, ambos são preocupantes. Porém, no caso
# de um falso positivo, o paciente somente passará por um
# tratamento desnecessário, que pode ou não lhe prejudicar.
# Já no caso de um falso negativo, o paciente não saberá que
# algo de errado está ocorrendo com ele, permitindo uma possível
# evolução dos sintomas. Logo, deduzo que o falso negativo seja
# mais preocupante dentre os dois.
