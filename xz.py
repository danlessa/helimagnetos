# Dependências 
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (18, 6)

# Criar uma matriz entre 0 e 2pi intervalados em pi/16
(l_min, l_max, d) = (0, 2 * np.pi, np.pi / 16)
Theta, Phi = np.meshgrid(np.arange(l_min, l_max, d), np.arange(l_min, l_max, d))

# Calcular os valores de K_b
U = np.cos(Theta) # K_b perpendicular ao eixo de simetria
V = np.sin(Theta) * np.sin(Phi) # K_b paralelo ao eixo de simetria

W = -np.sin(Phi) * np.sin(Theta)

## Fazer os gráficos
plt.title("Correntes ligadas na superfície lateral do cilindro (magnetização em paralelo ao plano do eixo de simetria)")
sc = plt.scatter(Phi, Theta, c=W, s=500, cmap="PiYG")
plt.quiver(Phi, Theta, U, V, label="$\\vec{K_b}$", scale=40)
#CS = plt.contour(Phi, Theta, np.sqrt(U ** 2 + V ** 2))
#plt.clabel(CS, inline=1, fontsize=10)
plt.colorbar(sc, label="$\\vec{J_b} \\cdot \\hat{n}$")
#plt.colorbar(CS, label="$||\\vec{K_b}||$")
plt.xlabel("$\\phi$")
plt.ylabel("$\\theta$")
xtick_loc = np.linspace(l_min, l_max, 9)
xtick_text = ["$%.3g\\pi$" % (d / np.pi) for d in xtick_loc]
plt.xticks(xtick_loc, xtick_text)
plt.yticks(xtick_loc, xtick_text)
plt.legend()
plt.show()
