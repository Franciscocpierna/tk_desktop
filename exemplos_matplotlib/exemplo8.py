

# 11. Boxplot
# Resume a distribuição mostrando mediana, quartis e outliers. Excelente para comparar
# grupos.
import matplotlib.pyplot as plt 
import numpy as np
 
# 1. Configura o gerador de números aleatórios com semente 42 para resultados reprodutíveis
rng = np.random.default_rng(42)

# 2. Gera os conjuntos de dados (100 amostras cada com médias e desvios diferentes)
g1 = rng.normal(70, 10, 100) # Média 70, desvio 10
g2 = rng.normal(75, 8, 100)  # Média 75, desvio 8
g3 = rng.normal(65, 12, 100) # Média 65, desvio 12

################# explicação a parte do gráfico como obteve os números do eixo y
# essa parte não aparece no programa 
#import numpy as np

# Dados da Turma A (o mesmo gerado anteriormente)
rng = np.random.default_rng(42)
g1 = rng.normal(70, 10, 100)

# Cálculo dos pontos que definem a posição no eixo Y
minimo = np.min(g1)
q1 = np.percentile(g1, 25) # 1º Quartil
mediana = np.median(g1)    # 2º Quartil
q3 = np.percentile(g1, 75) # 3º Quartil
maximo = np.max(g1)

print(f"Valores de referência para o eixo Y (Turma A):")
print(f"Mínimo: {minimo:.2f}")
print(f"Q1 (Base da caixa): {q1:.2f}")
print(f"Mediana (Linha interna): {mediana:.2f}")
print(f"Q3 (Topo da caixa): {q3:.2f}")
print(f"Máximo: {maximo:.2f}")

############################# explicação a parte do gráfico como obteve os números do eixo y

# 3. Cria o boxplot passando a lista de grupos
plt.boxplot([g1, g2, g3],
            labels=['Turma A','Turma B','Turma C'], # Define os nomes no eixo X
            patch_artist=True,                      # Permite colorir o interior da caixa
            boxprops=dict(facecolor='#93C5FD'))     # Define a cor de preenchimento das caixas

# 4. Adiciona rótulos aos eixos e título ao gráfico
plt.ylabel('Nota')              # Nome do eixo vertical
plt.title('Notas por Turma')    # Título do gráfico

# 5. Exibe o gráfico gerado
plt.show()