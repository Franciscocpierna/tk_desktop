# 13. Matplotlib + Pandas
# Pandas integra-se diretamente com matplotlib. Você pode passar colunas do DataFrame para
# as funções de plot
# 
# 
import matplotlib.pyplot as plt # Importa o módulo de plotagem
import pandas as pd # Importa a biblioteca para manipulação de dados

# Cria o DataFrame (tabela) com os dados de meses, receitas e custos
df = pd.DataFrame({
    'Mês': ['Jan','Fev','Mar','Abr','Mai','Jun'],
    'Receita': [12000, 15000, 9000, 18000, 21000, 17500],
    'Custo': [ 8000, 10000, 7500, 12000, 14000, 11000],
})

# Cria uma nova coluna 'Lucro' subtraindo os custos das receitas
df['Lucro'] = df['Receita'] - df['Custo']

# Plota a linha da Receita com marcadores circulares
plt.plot(df['Mês'], df['Receita'], marker='o', label='Receita')

# Plota a linha do Custo com marcadores quadrados
plt.plot(df['Mês'], df['Custo'], marker='s', label='Custo')

# Preenche a área entre as linhas de Custo e Receita com cor verde e transparência
plt.fill_between(df['Mês'], df['Custo'], df['Receita'], alpha=0.2, color='green')

# Adiciona legenda, nomeia o eixo Y e define o título do gráfico
plt.legend() 
plt.ylabel('R$')
plt.xlabel('Meses do ano')
plt.title('Receita vs Custo')

# Exibe o gráfico gerado na tela
plt.show()

'''
1. Importação de Bibliotecas
import matplotlib.pyplot as plt: Importa o módulo principal da biblioteca Matplotlib, que é responsável pela criação de visualizações
e gráficos. O as plt é um apelido padrão usado para facilitar a digitação.

import pandas as pd: Importa a biblioteca Pandas, essencial para manipulação e análise de dados (estruturados em tabelas).

2. Criação dos Dados
df = pd.DataFrame({ ... }): Cria um DataFrame (uma tabela) contendo três colunas: 'Mês', 'Receita' e 'Custo'. Cada lista representa 
os valores para cada mês.

3. Processamento dos Dados
df['Lucro'] = df['Receita'] - df['Custo']: Cria uma nova coluna chamada 'Lucro' calculando a diferença entre a 'Receita' e o 'Custo' 
para cada linha. Embora calculada, essa coluna não é plotada no seu gráfico atual.

4. Configuração e Plotagem do Gráfico
plt.plot(df['Mês'], df['Receita'], marker='o', label='Receita'): Desenha a linha da Receita. O argumento marker='o' adiciona 
círculos nos pontos de dados, e label define o nome que aparecerá na legenda.

plt.plot(df['Mês'], df['Custo'], marker='s', label='Custo'): Desenha a linha do Custo, utilizando quadrados (marker='s') para diferenciar
visualmente da Receita.

5. Estilização e Exibição
plt.fill_between(df['Mês'], df['Custo'], df['Receita'], alpha=0.2, color='green'): Esta função cria o sombreamento entre as duas linhas. 
Ela preenche a área entre a curva de 'Custo' e a curva de 'Receita'. O alpha=0.2 define uma transparência baixa, e a cor verde destaca 
a região que representa o lucro.

plt.legend(): Adiciona a legenda ao gráfico, utilizando os nomes definidos no parâmetro label anteriormente.

plt.ylabel('R$'): Adiciona o rótulo ao eixo Y, indicando que os valores representam Reais.

plt.title('Receita vs Custo'): Define o título do gráfico.

plt.show(): Comando final que renderiza e abre uma janela exibindo o gráfico gerado.

'''
