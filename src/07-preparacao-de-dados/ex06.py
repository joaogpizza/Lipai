import pandas as pd
import matplotlib.pyplot as plt

db = pd.read_csv('src/07-preparacao-de-dados/wine.csv')

amostras = {
    '10%':  db.drop(columns='Class').sample(frac=0.10, random_state=42),
    '30%':  db.drop(columns='Class').sample(frac=0.30, random_state=42),
    '50%':  db.drop(columns='Class').sample(frac=0.50, random_state=42),
    '100%': db.drop(columns='Class'),
}

metricas = {}
for nome, amostra in amostras.items():
    metricas[nome] = amostra.agg(['mean', 'median', 'std', 'min', 'max'])

for metrica in ['mean', 'median', 'std', 'min', 'max']:
    fig, eixos = plt.subplots(3, 5, figsize=(16, 9))
    colunas = [col for col in db.columns if col != 'Class']
    posicoes = [(i, j) for i in range(3) for j in range(5)]

    for idx, col in enumerate(colunas):
        i, j = posicoes[idx]
        valores = [metricas[t].loc[metrica, col] for t in amostras]
        eixos[i, j].bar(amostras.keys(), valores, color=['#e74c3c','#f39c12','#2ecc71','#3498db'])
        eixos[i, j].set_title(col, fontsize=8)

    eixos[2, 3].set_visible(False)
    eixos[2, 4].set_visible(False)
    fig.suptitle(f'Métrica: {metrica} — por tamanho de amostra')
    plt.show()

# Pode-se observar que, conforme a amostra aumenta, mais ela passa a representar de fato os dados populacionais.
# A média, por exemplo, não foi extremamente afetada, mas o desvio padrão já foi consideravelmente.
# Notável, também, a variação do valor mínimo que, na maioria dos atributos, mudou drasticamente entre 50% e 100%
