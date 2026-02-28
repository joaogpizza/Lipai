import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**2
y2 = x**5

# subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,4))
plt.suptitle('Gráficos com subplots')
axes[0, 0].plot(x, y1)
axes[0, 0].set_title('Função do Quinto Grau $x^5$')
axes[0, 0].set_xlabel('Tempo')
axes[0, 0].set_ylabel('Amplitude')
axes[0, 0].grid = True

axes[0, 1].plot(x, y1)
axes[0, 1].set_title('Função do Quinto Grau $x^5$')
axes[0, 1].set_xlabel('Tempo')
axes[0, 1].set_ylabel('Amplitude')
axes[0, 1].grid = True

axes[1, 0].plot(x, y2)
axes[1, 0].set_title('Função do Quinto Grau $x^5$')
axes[1, 0].set_xlabel('Tempo')
axes[1, 0].set_ylabel('Amplitude')
axes[1, 0].grid = True

axes[1, 1].plot(x, y2)
axes[1, 1].set_title('Função do Quinto Grau $x^5$')
axes[1, 1].set_xlabel('Tempo')
axes[1, 1].set_ylabel('Amplitude')
axes[1, 1].grid = True

plt.show()
