import matplotlib.pyplot as plt
import numpy as np

'''Gráfico de Barras
Compara valores entre categorias discretas. Use plt.bar (vertical) ou plt.barh
(horizontal). '''
categorias = ['Jan','Fev','Mar','Abr','Mai','Jun']
vendas = [120, 150, 90, 180, 210, 175]
bars = plt.bar(categorias, vendas, color='#3B82F6', edgecolor='#1E40AF')
# Adicionar valor em cima de cada barra
for b, v in zip(bars, vendas):
    plt.text(b.get_x()+b.get_width()/2, v+3, str(v),
ha='center', fontsize=9)
plt.title('Vendas por Mês')
plt.ylabel('Unidades')
plt.show()

import matplotlib.pyplot as plt # Importa o módulo pyplot da biblioteca Matplotlib, que é usado para criar gráficos.
import numpy as np             # Importa a biblioteca NumPy (comum em ciência de dados), embora não seja usada neste exemplo específico.

# Define as categorias (eixo X) como uma lista de meses.
categorias = ['Jan','Fev','Mar','Abr','Mai','Jun']
# Define os valores correspondentes às vendas (eixo Y) para cada mês.
vendas = [120, 150, 90, 180, 210, 175]
cores = ['red', 'green', 'blue', 'red', 'green', 'blue']
# Cria o gráfico de barras verticais: usa 'categorias' para o eixo X, 'vendas' para a altura, define a cor de preenchimento e a cor da borda.
#bars = plt.bar(categorias, vendas, color='#3B82F6', edgecolor='#1E40AF')
bars = plt.bar(categorias, vendas, color=cores, edgecolor='#1E40AF')
# Inicia um loop para percorrer cada objeto 'barra' e seu respectivo valor 'v' (vendas).
for b, v, c in zip(bars, vendas,cores):
    # plt.text posiciona o valor numérico acima de cada barra:
    # b.get_x()+b.get_width()/2 centraliza horizontalmente na barra.
    # v+3 coloca o texto um pouco acima do topo da barra (margem).
    # str(v) converte o valor numérico em texto.
    # ha='center' garante alinhamento centralizado e fontsize define o tamanho da fonte.
    #plt.text(b.get_x()+b.get_width()/2, v+3, str(v), ha='center', fontsize=9)
    plt.text(b.get_x() + b.get_width()/2, v + 3, str(v),ha='center', fontsize=9, color=c, fontweight='bold') 
# Define o título principal do gráfico.
plt.title('Vendas por Mês')
# Define o rótulo do eixo Y (vertical).
plt.ylabel('Unidades')
# Exibe a janela com o gráfico pronto na tela.
plt.show()

'''categorias = ['Jan', 'Fev', 'Mar']
vendas = [120, 150, 90]
cores = ['red', 'green', 'blue']

# O zip pareia o 1º de cada, depois o 2º de cada, e assim por diante
for cat, val, col in zip(categorias, vendas, cores):
    print(f"Mês: {cat} | Vendas: {val} | Cor da barra: {col}") '''