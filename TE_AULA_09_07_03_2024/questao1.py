# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# Gerar dados para a distribuição normal
mu = 0  # média
sigma = 1  # desvio padrão
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)  # valores para o eixo x
y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)  # densidade de probabilidade

# Plotar a distribuição normal
plt.plot(x, y)
plt.title('Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.grid(True)
plt.show()