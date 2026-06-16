import matplotlib.pyplot as plt
import numpy as np
# 1) Preparar os dados
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# 2) Criar o gráfico
plt.plot(x, y1, label='seno', linewidth=2)
plt.plot(x, y2, label='cosseno', linestyle='--')
# 3) Decorar
plt.title('Funções Trigonométricas')
plt.xlabel('x (radianos)')
plt.ylabel('f(x)')
plt.legend()
plt.show()


import matplotlib.pyplot as plt  # Importa o módulo de gráficos (pyplot) como 'plt'
import numpy as np  # Importa a biblioteca matemática/numérica como 'np'

# 1) Preparar os dados
# Cria 100 pontos no eixo X, espalhados uniformemente de 0 a 2*pi (aproximadamente 6.28)
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)  # Calcula o seno para cada um dos 100 pontos de X
y2 = np.cos(x)  # Calcula o cosseno para cada um dos 100 pontos de X

# 2) Criar o gráfico
# Plota a linha do seno, define o nome da legenda e deixa a linha mais grossa (linewidth=2)
plt.plot(x, y1, label="seno", linewidth=2)

# Plota a linha do cosseno, define o nome da legenda e deixa a linha tracejada (linestyle='--')
plt.plot(x, y2, label="cosseno", linestyle="--")

# 3) Decorar
plt.title("Funções Trigonométricas")  # Adiciona o título principal no topo
plt.xlabel("x (radianos)")  # Adiciona o texto descritivo no eixo X (horizontal)
plt.ylabel("f(x)")  # Adiciona o texto descritivo no eixo Y (vertical)

plt.legend()  # Mostra a caixinha de legenda com a identificação de cada linha

# 4) Exibir
plt.show()  # Abre a janela e exibe o gráfico final na tela