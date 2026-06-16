import matplotlib.pyplot as plt
'''
# 1) Interface pyplot (rápida)
plt.plot([1,2,3],[4,5,6])
plt.title('Exemplo')
plt.show()
# 2) Interface orientada a objetos (recomendada)
fig, ax = plt.subplots()
ax.plot([1,2,3],[4,5,6])
ax.set_title('Exemplo')
plt.show()
'''


# ==============================================================================
# 1) INTERFACE PYPLOT (Abordagem Funcional / Rápida)
# ==============================================================================
# Essa interface gerencia automaticamente a criação de figuras e eixos por baixo
# dos panos. É excelente para scripts rápidos, testes e análises exploratórias.

# Plota os pontos (1,4), (2,5) e (3,6) conectando-os com uma linha reta.
# O primeiro argumento é a lista do eixo X, o segundo é a lista do eixo Y.
plt.plot([1, 2, 3], [4, 5, 6])

# Define o título do gráfico atual que está sendo manipulado.
plt.title('Exemplo - Interface Pyplot')

# Renderiza e exibe a janela com o gráfico na tela.
plt.show()


# ==============================================================================
# 2) INTERFACE ORIENTADA A OBJETOS (Abordagem Recomendada)
# ==============================================================================
# Essa interface é mais explícita e robusta. Ela separa a "janela/página" (fig)
# da "área do gráfico" (ax). É a ideal para projetos reais, gráficos complexos
# com múltiplos subplots ou quando você precisa de controle total sobre o layout.

# plt.subplots() cria e retorna dois objetos ao mesmo tempo:
# - 'fig' (Figure): A janela/container principal que guarda tudo.
# - 'ax' (Axes): A área interna onde o gráfico de fato é desenhado (eixos X e Y).
fig, ax = plt.subplots()

# Dizemos explicitamente para a área 'ax' desenhar a linha com as coordenadas X e Y.
ax.plot([1, 2, 3], [4, 5, 6])

# Na interface OO, a maioria das funções de configuração ganha o prefixo "set_".
# Aqui definimos o título especificamente para este objeto 'ax'.
ax.set_title('Exemplo - Interface Orientada a Objetos')

# Renderiza e exibe a janela na tela.
plt.show()


'''
O comando plt.plot([1, 2, 3], [4, 5, 6]) é a forma mais básica de desenhar um gráfico de linha no Matplotlib.Para entender o 
que ele faz, pense nele como um jogo de ligar os pontos em um plano cartesiano (com eixos $X$ e $Y$).Como o Matplotlib interpreta 
os dadosO segredo está em entender que o comando recebe duas listas de coordenadas: [lista_X], [lista_Y].Primeira lista [1, 2, 3]: 
Representa as posições no eixo horizontal (X).Segunda lista [4, 5, 6]: Representa as posições no eixo vertical (Y).O Matplotlib cruza 
os elementos dessas listas na ordem em que aparecem para criar pontos (X, Y):Pega o primeiro de cada lista: (1, 4)
Pega o segundo de cada lista: (2, 5)Pega o terceiro de cada lista: (3, 6)Depois de mapear esses três pontos no gráfico, ele desenha uma 
linha reta conectando-os. Como a proporção de crescimento 
aqui é constante, o resultado final será uma linha diagonal perfeita subindo da esquerda para a direita.




'''


import matplotlib.pyplot as plt

# ==============================================================================
# 1) Interface Pyplot
# ==============================================================================
plt.plot([1,2,3],[4,5,6])
plt.title('Exemplo - Interface Pyplot')

# Força o eixo X a exibir APENAS os números 1, 2 e 3
plt.xticks([1, 2, 3])
# Força o eixo Y a exibir APENAS os números 4, 5 e 6
plt.yticks([4, 5, 6])

plt.show()

# ==============================================================================
# 2) Interface Orientada a Objetos (Recomendada)
# ==============================================================================
fig, ax = plt.subplots()
ax.plot([1,2,3],[4,5,6])
ax.set_title('Exemplo - Interface Orientada a Objetos')

# Na interface OO, usamos set_xticks e set_yticks
ax.set_xticks([1, 2, 3])
ax.set_yticks([4, 5, 6])

plt.show()