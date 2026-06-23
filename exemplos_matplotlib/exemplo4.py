import matplotlib.pyplot as plt # Importa a biblioteca principal para plotagem.
import numpy as np             # Importa NumPy para manipular arrays, essencial para posicionar barras lado a lado.

categorias = ['Jan','Fev','Mar','Abr','Mai','Jun'] # Define os rótulos do eixo X (os meses).
prod_a = [120, 150, 90, 180, 210, 175]             # Valores do primeiro grupo de dados (Produto A).
prod_b = [100, 130, 110, 160, 190, 200]             # Valores do segundo grupo de dados (Produto B).

x = np.arange(len(categorias)) # Cria um array de números [0, 1, 2, 3, 4, 5] para servir como base das posições no eixo X.
w = 0.4                        # Define a largura (width) de cada barra.

# Desenha as barras do Produto A:
# x - w/2 desloca as barras para a esquerda para abrir espaço.
plt.bar(x - w/2, prod_a, w, label='Produto A', color='#3B82F6')

# Desenha as barras do Produto B:
# x + w/2 desloca as barras para a direita, colocando-as ao lado da primeira.
plt.bar(x + w/2, prod_b, w, label='Produto B', color='#F97316')

# Substitui os números do eixo X pelos nomes dos meses definidos em 'categorias'.
plt.xticks(x, categorias)

# plt.legend() cria a caixa explicativa (legenda) baseada nos labels definidos anteriormente.
# plt.title() adiciona o título do gráfico.
plt.legend(); plt.title('Comparação de Vendas')

# Exibe o gráfico final.
plt.show()
