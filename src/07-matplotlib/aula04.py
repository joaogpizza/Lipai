from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*(np.pi), 70)
y = np.cos(4*x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='#0f0f0f80', lw=0.5, marker='o',
         linestyle='dashdot')
plt.grid(True)
plt.title('Gráfico do Cosseno')
plt.xlabel('Eixo do Tempo')
plt.ylabel('Eixo da Amplitude')
plt.show()
