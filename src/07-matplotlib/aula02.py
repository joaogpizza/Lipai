import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*(np.pi), 500)
c = np.cos(x)
s = np.sin(x)

plt.figure('Gráficos cosenoidais', figsize=(8, 4))
plt.subplots_adjust(
    left=0.152,
    right=0.943,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.4
)

ax1 = plt.subplot(1, 2, 1)
plt.plot(x, c)
ax1.set_title('Gráfico do Cosseno')
ax1.set_xlabel('Eixo de Tempo')
ax1.set_ylabel('Eixo da Amplitude')
ax1.grid()

ax2 = plt.subplot(1, 2, 2)
plt.plot(x, s)
ax2.set_title('Gráfico do Seno')
ax2.set_xlabel('Eixo de Tempo')
ax2.set_ylabel('Eixo da Amplitude')
ax2.grid()

plt.show()
