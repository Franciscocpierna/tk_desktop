# SELECT strftime('%m-%Y', data_inclusao) AS mes_ano, COUNT(*) AS total
# FROM sua_tabela
# GROUP BY mes_ano
# ORDER BY mes_ano;

# Ao fazer isso, o resultado que chega ao seu Python já está agrupado: uma lista com "01-2026", "02-2026", etc.,
#  e a contagem correspondente. 
# Aí é só passar para o Matplotlib.


# Caminho 2: Trazer os dados brutos e usar Pandas (Mais flexível)Se você preferir trazer todos os dados 
# para o Python e processar lá, a biblioteca Pandas é a ferramenta ideal. 
# Você carrega os dados em um DataFrame e usa o agrupamento do Pandas.  

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# 1. Conectar e carregar dados
conn = sqlite3.connect('seu_banco.db')
df = pd.read_sql_query("SELECT data_inclusao FROM sua_tabela", conn)

# 2. Converter para datetime e agrupar
df['data_inclusao'] = pd.to_datetime(df['data_inclusao'])
# essa linha explicação no final
df_mensal = df.groupby(df['data_inclusao'].dt.to_period('M')).size()

# 3. Plotar
df_mensal.plot(kind='bar')
plt.show()


# Qual escolher?
# Use o Caminho 1 (SQL) se o seu banco de dados for grande. Processar o agrupamento no banco de dados é muito 
# mais rápido do que trazer milhões de registros para a memória do Python.

# Use o Caminho 2 (Pandas) se você precisar de flexibilidade para manipular os dados, aplicar filtros 
# extras ou se já estiver habituado com a sintaxe do Pandas para análise de dados.

# Em resumo: o Matplotlib precisa de um dataset pronto (um eixo X com os meses e um eixo Y com as quantidades). 
# Cabe a você decidir se esse "preparo" acontece no motor do SQLite ou na memória do seu script Python.

# Múltiplos Gráficos - A forma mais VERSÁTIL - MATPLOTLIB Python

# Este vídeo é relevante porque demonstra, na prática, como preparar e organizar datasets no Python para
#  gerar diferentes tipos de visualizações com o Matplotlib.


df_mensal = df.groupby(df['data_inclusao'].dt.to_period('M')).size()
#Essa linha é o "coração" da transformação dos dados. Ela pega uma lista de datas individuais 
# e as agrupa em baldes mensais para contar quantos registros existem em cada um.Vamos dividir 
# o que acontece ali passo a passo:1. df['data_inclusao'].dtO sufixo .dt é um acessor. Ele permite 
# que você use propriedades específicas de objetos de data e hora (datetime) do Pandas. Sem ele, o 
# Pandas trataria a coluna apenas como texto ou números genéricos. Com o .dt, você ganha acesso a 
# ferramentas como .year, .month, .day, etc.2. .to_period('M')Esta é a parte que faz o "agrupamento 
# inteligente".Se você tem uma data como 2026-05-12 ou 2026-05-28, o .to_period('M') transforma tudo 
# isso em 2026-05.Ele descarta a precisão do dia e foca apenas no "período mensal". Isso é essencial 
# para que todas as datas que caem no mesmo mês sejam tratadas como uma categoria única.3. .groupby(...)
# Agora que o Pandas tem uma representação de "Mês/Ano" para cada linha, o groupby percorre todo o seu 
# DataFrame e coloca no mesmo "grupo" todas as linhas que compartilham o mesmo período 
# (ex: todas que viraram 2026-05 ficam juntas, todas que viraram 2026-06 ficam em outro grupo)
# .4. .size()Finalmente, o .size() conta quantas linhas existem dentro de cada um desses grupos que você 
# acabou de criar.Se você tinha 10 registros no mês de maio, o size() retorna o número 10 para o grupo 
# 2026-05.O resultado final (df_mensal) será uma Series onde:O índice são os períodos 
# (Ex: 2026-01, 2026-02).Os valores são as contagens (Ex: 5, 12).Exemplo visual da transformação:Imagine 
# que seu df original tem isto:data_inclusao2026-01-052026-01-202026-02-10to_period('M') 
# transforma para:| período || :--- || 2026-01 || 2026-01 || 2026-02 |groupby(...).size() 
# agrupa e conta:| Índice | Valor (Contagem) || :--- | :--- || 2026-01 | 2 || 2026-02 | 1 |
# É exatamente esse resultado final que você passa para o Matplotlib desenhar o seu gráfico.