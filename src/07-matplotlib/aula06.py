from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2)

axe.text(2.6, 0.35, 'P(2,5; 0,4)')
axe.text(3, 0.42, 'Logarítmo $y = log_{10}x$',
         fontsize=10,
         bbox=dict(facecolor='red', alpha=0.5))
axe.annotate('P(2,5; 0,4)', xy=(2.5, 0.4),
             fontsize=14, xytext=(0.5, 0.5),
             arrowprops=dict(facecolor='red'),
             color='r')

axe.plot([0, 2.5], [0.4, 0.4],
         color='gray', linestyle='--', lw=0.8)
axe.plot([2.5, 2.5], [0.0, 0.4],
         color='gray', linestyle='--', lw=0.8)
axe.plot(2.5, 0.4, marker='o', color='gray')
axe.set_title('Gráfico Logarítmico')
axe.set_xlabel('Eixo X')
axe.set_ylabel('Eixo Y')
axe.set_xticks(np.arange(0, 5.5, 0.5))
plt.show()
