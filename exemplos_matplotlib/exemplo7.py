
''' 
O que é um Histograma?
Diferente de um gráfico de dispersão (que mostra pares de valores), o histograma agrupa dados em "bins" 
(caixas ou intervalos). Ele mostra quantos valores caem dentro 
de cada intervalo. No seu exemplo, ele mostra como as alturas estão distribuídas em torno da média de 170 cm.
'''


import matplotlib.pyplot as plt
import numpy as np

# 1. Configura o gerador de números aleatórios para reprodutibilidade.
rng = np.random.default_rng(42)

# 2. Gera 1000 valores aleatórios seguindo uma distribuição normal:
# Média (loc) = 170, Desvio Padrão (scale) = 8, Quantidade = 1000.
dados = rng.normal(170, 8, 1000)
######
#explicação de onde veio os números do eixo yy 
# Ao executar esta linha, a variável 'contagens' guardará os valores de Y
contagens, bins, patches = plt.hist(dados, bins=30)

# Isso imprimirá quantos elementos caíram em cada uma das 30 barras
print(contagens)
#####


# 3. Cria o histograma:
# bins=30: Divide os dados em 30 faixas (colunas).
# color='#10B981' e edgecolor='white': Define cor e borda para facilitar a visualização.
plt.hist(dados, bins=30, color='#10B981', edgecolor='white')

# 4. Adiciona uma linha vertical (axvline) na posição da média dos dados.
# linestyle='--' faz a linha pontilhada; label exibe o valor da média no gráfico.
plt.axvline(dados.mean(), color='red', linestyle='--', label=f'Média={dados.mean():.1f}')

# 5. Adiciona rótulos aos eixos e um título.
plt.xlabel('Altura (cm)'); plt.ylabel('Frequência')
plt.title('Distribuição de Alturas')

# 6. Exibe a legenda (da média) e mostra o gráfico final.
plt.legend(); plt.show()