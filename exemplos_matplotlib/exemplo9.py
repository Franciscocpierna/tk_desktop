
import matplotlib.pyplot as plt
import numpy as np
'''
#12. Subplots — Múltiplos Gráficos
plt.subplots(linhas, colunas) #cria uma grade de gráficos em uma única figura.
fig, axes = plt.subplots(2, 2, figsize=(8, 5.5))
axes[0,0].plot(x, np.sin(x)); axes[0,0].set_title('Seno')
axes[0,1].plot(x, np.cos(x)); axes[0,1].set_title('Cosseno')
axes[1,0].bar(categorias[:4], vendas[:4]); axes[1,0].set_title('Vendas')
axes[1,1].hist(dados, bins=20); axes[1,1].set_title('Histograma')
fig.suptitle('Múltiplos Gráficos com subplots')
plt.tight_layout()
plt.show()
'''


# Preparação de dados de exemplo
x = np.linspace(0, 10, 100) # Dados para funções trigonométricas
categorias = ['A', 'B', 'C', 'D'] # Rótulos para gráfico de barras
vendas = [10, 25, 15, 30] # Valores para gráfico de barras
dados = np.random.randn(1000) # Dados para o histograma

# 1. Cria uma figura e uma grade de 2x2 subgráficos
# fig: é a janela/objeto principal | axes: é uma matriz (array) que contém cada subgráfico
fig, axes = plt.subplots(2, 2, figsize=(8, 5.5))

# 2. Plota no primeiro gráfico (linha 0, coluna 0)
axes[0,0].plot(x, np.sin(x))
axes[0,0].set_title('Seno')

# 3. Plota no segundo gráfico (linha 0, coluna 1)
axes[0,1].plot(x, np.cos(x))
axes[0,1].set_title('Cosseno')

# 4. Plota no terceiro gráfico (linha 1, coluna 0)
axes[1,0].bar(categorias, vendas)
axes[1,0].set_title('Vendas')

# 5. Plota no quarto gráfico (linha 1, coluna 1)
axes[1,1].hist(dados, bins=20)
axes[1,1].set_title('Histograma')

# 6. Adiciona um título geral para toda a figura
fig.suptitle('Múltiplos Gráficos com subplots')

# 7. Ajusta o espaçamento entre os gráficos para não haver sobreposição de rótulos
plt.tight_layout()

# 8. Exibe a janela final com todos os gráficos
plt.show()


''' 
Principais conceitos explicados:plt.subplots(2, 2): 
Cria uma grade de $2$ linhas e $2$ colunas. Isso retorna um objeto axes que 
funciona como uma matriz. Para acessar cada gráfico, você usa os índices [linha, coluna], 
começando sempre do zero.axes[i, j]: É a forma como você "chama" o gráfico específico onde 
deseja desenhar. Se você tiver apenas uma linha ou uma coluna, o axes será um array unidimensional
(ex: axes[0] e axes[1]).plt.tight_layout(): Esta função é essencial quando se trabalha com vários 
gráficos; ela ajusta automaticamente as margens e o espaçamento para garantir que títulos e nomes de 
eixos não fiquem sobrepostos.O uso de subplots é a maneira mais profissional e organizada de 
criar painéis de visualização (dashboards) estáticos com Matplotlib.Para aprofundar seu conhecimento, 
você gostaria de saber como compartilhar o mesmo eixo X ou Y entre esses gráficos, para que as escalas 
fiquem sincronizadas?

Para entender como os números do eixo Y são definidos no gráfico de subplots que acabamos de ver, 
precisamos distinguir entre o que o Matplotlib faz automaticamente e como ele calcula os limites.O 
Matplotlib, por padrão, utiliza um processo chamado "Auto-scaling" (ou escalonamento automático). 
Aqui está a lógica de como ele chega naqueles números que você vê no eixo vertical:1. O Cálculo Automático 
(Auto-scaling)Quando você chama um método como axes[0,0].plot(x, np.sin(x)), o Matplotlib executa estas 
etapas internas:Coleta de dados: Ele percorre todos os valores de $Y$ que você passou 
(no caso do seno, são os resultados de $\sin(x)$).Identificação de extremos: Ele encontra o valor mínimo 
e o valor máximo desses dados.Margens (Padding): Para que os pontos não fiquem "colados" na borda do gráfico, 
o Matplotlib aplica uma margem de segurança (geralmente de 5% a 10% do intervalo total) além dos valores 
mínimo e máximo encontrados.Cálculo dos Ticks (Marcadores): Ele executa um algoritmo chamado Locator que 
tenta encontrar números "redondos" ou visualmente limpos para colocar as marcações no eixo. É por isso que, 
muitas vezes, o eixo não começa exatamente no seu valor mínimo (ex: -1.0), mas sim um pouco abaixo ou acima 
para permitir que as linhas de grade fiquem espaçadas uniformemente.2. A estrutura de dados por trás dos 
eixosCada subgráfico (axes[0,0], axes[0,1], etc.) é um objeto independente que possui seus próprios limites 
de eixos. Você pode visualizar ou alterar esses limites manualmente usando estes comandos:Python# Para 
descobrir quais valores o Matplotlib escolheu para o eixo Y


min_y, max_y = axes[0,0].get_ylim()
print(f"O eixo Y vai de {min_y:.2f} até {max_y:.2f}")

# Para forçar o eixo a ter um intervalo específico (ex: de -2 a 2)
axes[0,0].set_ylim(-2, 2)
'''