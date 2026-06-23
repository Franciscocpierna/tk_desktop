import matplotlib.pyplot as plt
import numpy as np

# 9. Gráfico de Dispersão (Scatter)
# Mostra a relação entre duas variáveis numéricas. Útil para identificar correlações e outliers.

# 1. Configuração do gerador de números aleatórios com uma semente fixa (42)
# para garantir que os resultados sejam sempre os mesmos a cada execução.
rng = np.random.default_rng(42)

# 2. Cria 50 valores aleatórios entre 1 e 10 (representando as horas de estudo).
horas = rng.uniform(1, 10, 50)

# 3. Calcula as notas baseando-se em uma fórmula linear (2 * horas) 
# adicionando um ruído aleatório para simular a variação do mundo real.
notas = 2*horas + rng.normal(0, 2, 50) 

# 4. Gera o gráfico de dispersão (scatter plot) com os eixos X e Y.
# c=notas define a cor dos pontos baseada no valor da nota.
# cmap='viridis' aplica um esquema de cores profissional.
# s=60 define o tamanho dos pontos; edgecolor='k' cria uma borda preta.
plt.scatter(horas, notas, c=notas, cmap='viridis', s=60, edgecolor='k')

# 5. Adiciona a barra lateral que indica a escala de cores das notas.
plt.colorbar(label='Nota')

# 6. Define os rótulos dos eixos e o título principal do gráfico.
plt.xlabel('Horas de Estudo'); plt.ylabel('Nota')
plt.title('Horas de Estudo x Nota')

# 7. Exibe a janela com o gráfico gerado.
plt.show()