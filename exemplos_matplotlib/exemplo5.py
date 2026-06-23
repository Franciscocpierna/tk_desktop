
import matplotlib.pyplot as plt
import numpy as np
# 8. Gráfico de Pizza
# Mostra a proporção de cada parte em relação ao todo. Use para poucas categorias (até ~6).
# Define as categorias (nomes) que representarão cada fatia do gráfico.
labels = ['Aluguel','Comida','Transporte','Lazer','Outros']
# Define os valores numéricos correspondentes a cada categoria.
valores = [1200, 800, 400, 300, 250]

cores = ['#3B82F6','#10B981','#F59E0B','#EF4444','#8B5CF6']
# Cria o gráfico de pizza:
# valores: os dados numéricos.
# labels=labels: associa os nomes definidos anteriormente a cada fatia.
# autopct='%1.1f%%': formata a exibição da porcentagem (1 casa decimal + sinal de %).
# startangle=90: rotaciona o gráfico para que a primeira fatia comece no topo (90 graus).
# colors=[...]: define uma paleta de cores personalizada para cada fatia.
#plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, 
#        colors=['#3B82F6','#10B981','#F59E0B','#EF4444','#8B5CF6'])

plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, 
        colors=cores)


# Adiciona o título no topo do gráfico.
plt.title('Distribuição de Gastos Mensais')

# Renderiza e exibe o gráfico na janela.
plt.show()