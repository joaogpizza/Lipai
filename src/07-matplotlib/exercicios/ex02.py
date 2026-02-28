""" Ex02 S6A3 """

import os
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

caminho = os.path.join(os.path.dirname(__file__), "metrics.csv")

df = pd.read_csv(caminho)

total = df.count()['train_loss']
epochs = np.arange(1, total + 1)
precisao_train = np.asarray(df['train_acc'])
precisao_val = np.asarray(df['val_acc'])
perda_train = np.asarray(df['train_loss'])
perda_val = np.asarray(df['val_loss'])

fig, eixos = plt.subplots(nrows=1, ncols=2, figsize=(12,4))
plt.suptitle('Gráficos de treinamento')

eixos[0].plot(epochs, precisao_train, label='train')
eixos[0].plot(epochs, precisao_val, label='valid')
eixos[0].set_title('model accuracy')
eixos[0].set_xlabel('epoch')
eixos[0].set_ylabel('accuracy')
eixos[0].legend()

eixos[1].plot(epochs, perda_train, label='train')
eixos[1].plot(epochs, perda_val, label='valid')
eixos[1].set_title('model loss')
eixos[1].set_xlabel('epoch')
eixos[1].set_ylabel('loss')
eixos[1].legend()

plt.show()
