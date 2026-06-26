# 14. Personalização e Estilo
# Você pode controlar cores, espessuras, anotações, grids e estilos globais.

import matplotlib.pyplot as plt # Importa o módulo de plotagem de gráficos
import numpy as np # Importa a biblioteca para cálculos matemáticos

# Gera 100 pontos espaçados uniformemente entre 0 e 10 para o eixo X
x = np.linspace(0, 10, 100)

# Cria uma nova figura para desenhar o gráfico
plt.figure()

# Plota a função de oscilação amortecida: seno multiplicado por uma exponencial decrescente
# 'color' define a cor (código hexadecimal) e 'linewidth' a espessura da linha
plt.plot(x, np.sin(x)*np.exp(-x/5), color='#EF4444', linewidth=3)

# Preenche a área abaixo da curva plotada
# 'alpha' define a opacidade (0 a 1) e 'color' a cor de preenchimento
plt.fill_between(x, np.sin(x)*np.exp(-x/5), alpha=0.3, color='#EF4444')

# Adiciona título ao gráfico com tamanho de fonte 14 e negrito
plt.title('Oscilação Amortecida', fontsize=14, fontweight='bold')

# Define os nomes dos rótulos para os eixos horizontal (Tempo) e vertical (Amplitude)
plt.xlabel('Tempo (s)'); plt.ylabel('Amplitude')

# Cria uma anotação com seta para destacar um ponto
# 'xy' é a coordenada do ponto apontado, 'xytext' é a posição do texto
# 'arrowprops' configura a aparência da seta
plt.annotate('Pico', xy=(1.5, 0.7), xytext=(3, 0.8), arrowprops=dict(arrowstyle='->'))

# Exibe o gráfico final na tela
plt.show()


'''
Uma oscilação amortecida ocorre quando um sistema que deveria oscilar indefinidamente (como um pêndulo ou 
uma massa em uma mola) perde energia gradualmente devido a forças dissipativas, como o atrito ou a resistência 
do ar.

Como resultado dessa perda de energia, a amplitude do movimento diminui com o tempo até que o sistema finalmente 
pare na sua posição de equilíbrio. É exatamente o comportamento que aquele gráfico que você estava analisando 
representa.

Por que isso acontece?
Em um sistema "ideal" (sem atrito), a energia mecânica seria conservada e o sistema oscilaria para sempre. 
Na vida real, quase todos os sistemas possuem forças que se opõem ao movimento. À medida que o sistema se move, 
parte da sua energia cinética é convertida em calor ou som, o que reduz a força que o impulsiona no próximo 
ciclo.

Os três tipos de amortecimento
Dependendo da intensidade da força de resistência (atrito), o sistema se comporta de maneiras diferentes ao retornar ao equilíbrio:

Subamortecimento: O sistema oscila várias vezes, mas a amplitude de cada oscilação diminui exponencialmente até parar. (É o caso do seu gráfico).

Amortecimento Crítico: O sistema retorna à posição de equilíbrio o mais rápido possível sem oscilar. É o ideal para sistemas que precisam parar rapidamente, como o ponteiro de alguns medidores analógicos ou o sistema de fechamento automático de algumas portas.

Superamortecimento: O sistema é tão "travado" pela resistência que ele retorna ao equilíbrio muito lentamente, sem nunca oscilar, levando mais tempo que no amortecimento crítico.

Exemplos no dia a dia
Amortecedores de carro: Eles são projetados para oferecer um amortecimento próximo ao crítico, garantindo que, após passar por um buraco, o carro não fique "quicando" infinitamente.

Baloiço (ou gangorra): Se você parar de dar impulso, a resistência do ar e o atrito no eixo farão com que o baloiço pare gradualmente.

Portas com molas: Aquelas portas que fecham sozinhas geralmente possuem um mecanismo de amortecimento para evitar que batam com força.

O conceito de "amplitude que decai com o tempo" é o que torna o seu gráfico de Oscilação Amortecida uma representação visual clara dessa perda de energia.

Ficou clara a diferença entre esses três comportamentos de amortecimento?

nesse exemplo é:

No seu exemplo, a função que você está usando é:
np.sin(x) * np.exp(-x/5)O "número" (ou parâmetro) que controla a intensidade da oscilação amortecida é o 5 
(que está no denominador da exponencial: -x/5).Em física, esse valor está relacionado ao fator de amortecimento 
($\gamma$). Ele determina o quão rápido a oscilação "morre".O que acontece quando você muda esse número?
Quanto menor for esse número, mais rápido o sistema perde energia (mais forte é o amortecimento). 
Quanto maior for esse número, mais tempo a oscilação dura.Se o número for pequeno (ex: -x/1): 
A amplitude cai muito rápido. A onda mal terá tempo de oscilar antes de voltar quase ao zero. 
Isso se aproxima do amortecimento crítico ou até superamortecimento (se o valor for muito baixo, ela deixa de 
oscilar completamente).Se o número for grande (ex: -x/20): A onda continuará oscilando por muito mais tempo. 
Ela demora mais para perder a amplitude, comportando-se como um sistema com muito pouco atrito (subamortecimento).
Por que o seu exemplo é "Subamortecido"?Como a sua função usa np.sin(x) (uma função oscilatória) multiplicada 
por np.exp(-x/5) (uma queda exponencial), ela gera uma onda que atravessa o eixo zero várias vezes enquanto 
diminui. Por definição, qualquer sistema que oscila em torno da posição de equilíbrio enquanto sua amplitude 
diminui é classificado como subamortecido.Se você quiser testar isso no seu código, tente alterar o 5 para 2 
(verá uma queda brusca) ou para 10 (verá uma oscilação muito mais longa). Você consegue ver a mudança 
visual na curva quando altera esse valor no seu editor


'''
