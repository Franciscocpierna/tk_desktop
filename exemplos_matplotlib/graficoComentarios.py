

'''



PAGAMENTO EM ATRASO 

SQL
SELECT 
    strftime('%m-%Y', data_vencimento) AS mes_ano, 
    COUNT(*) AS total_atrasados
FROM pagamentos
WHERE data_vencimento < DATE('now')          -- 1. Só o que já venceu (deixa os futuros de fora!)
  AND data_pagamento IS NULL                 -- 2. E que ainda não foi pago
GROUP BY mes_ano
ORDER BY mes_ano;

Python
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('seu_banco.db')
cursor = conn.cursor()

# Consulta SQL comparando com a data atual (DATE('now'))
query = """
   SQL
SELECT 
    strftime('%m-%Y', data_vencimento) AS mes_ano, 
    COUNT(*) AS total_atrasados
FROM pagamentos
WHERE data_vencimento < DATE('now')          -- 1. Só o que já venceu (deixa os futuros de fora!)
  AND data_pagamento IS NULL                 -- 2. E que ainda não foi pago
GROUP BY mes_ano
ORDER BY mes_ano;
"""

cursor.execute(query)
dados = cursor.fetchall()
conn.close()

# Separando os dados para o gráfico
meses = [row[0] for row in dados]
totais = [row[1] for row in dados]

# Criando o Gráfico de Colunas
plt.figure(figsize=(10, 5))
plt.bar(meses, totais, color='darkorange')
plt.xlabel('Mês/Ano')
plt.ylabel('Quantidade de Atrasados')
plt.title('Histórico de Pagamentos em Atraso (Comparado com a Data Atual)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

COM GRÁFICO DE LINHA

import sqlite3
import matplotlib.pyplot as plt

# 1. Conexão com o banco de dados
conn = sqlite3.connect('seu_banco.db')
cursor = conn.cursor()

# 2. Consulta SQL 
# Filtra o que já venceu (< DATE('now')) e o que ainda não foi pago (IS NULL), agrupando por mês/ano
query = """
    SELECT 
        strftime('%m-%Y', data_vencimento) AS mes_ano, 
        COUNT(*) AS total_atrasados
    FROM pagamentos
    WHERE data_vencimento < DATE('now')
      AND data_pagamento IS NULL
    GROUP BY mes_ano
    ORDER BY mes_ano;
"""

cursor.execute(query)
dados = cursor.fetchall()
conn.close()

# 3. Tratamento dos dados para o gráfico
meses = [row[0] for row in dados]
totais = [row[1] for row in dados]

# 4. Construção do Gráfico de Linha
plt.figure(figsize=(11, 6))

# plt.plot gera o gráfico de linha com marcadores nos pontos
plt.plot(meses, totais, color='crimson', marker='o', linewidth=2.5, markersize=6, label='Atrasados')

# Adicionando os valores exatos em cima de cada ponto da linha para facilitar a leitura
for i, txt in enumerate(totais):
    plt.annotate(str(txt), (meses[i], totais[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Estilização do gráfico
plt.xlabel('Mês/Ano de Vencimento', fontsize=11)
plt.ylabel('Quantidade de Pagamentos em Atraso', fontsize=11)
plt.title('Evolução Mensal de Pagamentos em Atraso (Baseado na Data Atual)', fontsize=13, pad=15)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Exibição
plt.show()  


INCLUSÃO NO MÊS

SELECT 
    strftime('%d', data_inclusao) AS dia, 
    COUNT(*) AS total
FROM produtos
WHERE strftime('%Y-%m', data_inclusao) = ?
GROUP BY dia
ORDER BY dia;


GRAFICO DE BARRA EM DETERMINADO MES

import sqlite3
import matplotlib.pyplot as plt

# Exemplo de valor que veio de um input do usuário ou tela de seleção
mes_escolhido = "2026-08"  # Formato: YYYY-MM

conn = sqlite3.connect('seu_banco.db')
cursor = conn.cursor()

# A query utiliza o parâmetro (?) para evitar injeção de SQL e aceitar qualquer mês
query = """
    SELECT 
        strftime('%d', data_vencimento) AS dia, 
        COUNT(*) AS total
    FROM produtos
    WHERE strftime('%Y-%m', data_vencimento) = ?
      -- AND data_vencimento < DATE('now') -- Sua regra de vencido, se aplicável
    GROUP BY dia
    ORDER BY dia;
"""

cursor.execute(query, (mes_escolhido,))
dados = cursor.fetchall()
conn.close()

# Separando os dados para o gráfico
dias = [row[0] for row in dados]
totais = [row[1] for row in dados]

# Criando o Gráfico
plt.figure(figsize=(10, 5))
plt.bar(dias, totais, color='crimson')
plt.xlabel('Dias do Mês')
plt.ylabel('Quantidade de Produtos Vencidos')
plt.title(f'Produtos Vencidos por Dia - Referência: {mes_escolhido}')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
'''



'''
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry("600x400")

# 1. Criamos um Frame qualquer (uma moldura/área na tela)
meu_painel = tk.Frame(root, bg="lightgray", bd=2, relief=tk.SUNKEN)
meu_painel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 2. Ao criar o canvas do gráfico, dizemos que o "master" (dono) é esse Frame
# (Aqui 'fig' é o seu gráfico do matplotlib já configurado)
canvas = FigureCanvasTkAgg(fig, master=meu_painel)
canvas.draw()

# 3. Posicionamos o gráfico dentro desse Frame usando o pack()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()
'''
# SELECT strftime('%m-%Y', data_inclusao) AS mes_ano, COUNT(*) AS total
# FROM sua_tabela
# GROUP BY mes_ano
# ORDER BY mes_ano;

# Ao fazer isso, o resultado que chega ao seu Python já está agrupado: uma lista com "01-2026", "02-2026", etc.,
#  e a contagem correspondente. 
# Aí é só passar para o Matplotlib. completo

  # Não esqueça de fechar a conexão
#    conn.close()

    #Essa é uma excelente pergunta técnica! A resposta curta é: o execute() serve para realizar ações, enquanto 
    # o read_sql_query() serve para trazer dados para análise.Aqui está a distinção prática:1. O que o execute() 
    # faz?Quando você usa cursor.execute(query), o Python apenas envia o comando para o banco de dados e deixa 
    # o cursor esperando. Para você obter os dados de fato, você ainda precisaria fazer mais dois passos 
    # manuais:cursor.execute(query) — Envia a ordem.dados = cursor.fetchall() — Busca os resultados para a 
    # memória.Transformação Manual: Você teria uma lista de tuplas (ex: [('01-2026', 10), ('02-2026', 15)]). 
    # O Matplotlib não "entende" nativamente uma lista de tuplas; você teria que separar manualmente essas tuplas 
    # em duas listas (uma de meses e uma de totais) para passar aos eixos do gráfico.2. O que o read_sql_query() faz?O 
    # pd.read_sql_query(query, conn) é um atalho de alto nível que faz todo o trabalho sujo para você em um 
    # único comando:Ele abre o cursor automaticamente.Ele executa a consulta.Ele busca os dados (fetchall).
    # Ele monta o DataFrame: Ele transforma as tuplas em uma tabela organizada (DataFrame) onde você acessa 
    # os dados pelos nomes das colunas (df['mes_ano']).Em resumo:ComandoO que faz?Ideal para...cursor.execute()
    # Envia o comando SQL.INSERT, UPDATE, DELETE ou quando você precisa de controle granular sobre cada linha 
    # lida (processamento linha a linha).pd.read_sql_query()Executa e converte em tabela.Análise de dados e 
    # visualização. É muito mais rápido para codificar e o resultado já está pronto para ser plotado.Se 
    # você estivesse apenas querendo deletar um registro ou inserir um nome, usaria execute(). Como o seu objetivo 
    # é gerar um gráfico, o Pandas já preparou a estrutura de dados (dataset) que o Matplotlib precisa para 
    # funcionar.Você prefere usar a abordagem mais direta do Pandas ou prefere o controle mais detalhado 
    # que o execute() oferece?

#     import sqlite3
#     import matplotlib.pyplot as plt

#     # 1. Conectar e preparar o cursor
#     conn = sqlite3.connect('seu_banco.db')
#     cursor = conn.cursor()

#     # 2. Executar a consulta
#     query = """
#     SELECT strftime('%m-%Y', data_inclusao) AS mes_ano, COUNT(*) AS total
#     FROM produtos
#     GROUP BY mes_ano
#     ORDER BY mes_ano;
#     """
#     cursor.execute(query)
#     resultados = cursor.fetchall() # Isso retorna uma lista de tuplas: [('01-2026', 10), ('02-2026', 15)]

#     # 3. "Desempacotar" os dados em duas listas separadas
#     # O Matplotlib precisa de listas individuais para X e Y
#     meses = [item[0] for item in resultados]
#     totais = [item[1] for item in resultados]

#     # 4. Plotar o gráfico
#     plt.figure(figsize=(10, 6))
#     plt.bar(meses, totais, color='teal')
#     plt.title('Total de inclusões por mês')
#     plt.xlabel('Meses')
#     plt.ylabel('Quantidade')
#     plt.show()

#     # 5. Fechar tudo
#     cursor.close()
#  #   conn.close()

    
# Caminho 2: Trazer os dados brutos e usar Pandas (Mais flexível)Se você preferir trazer todos os dados 
# para o Python e processar lá, a biblioteca Pandas é a ferramenta ideal. 
# Você carrega os dados em um DataFrame e usa o agrupamento do Pandas.  

# import pandas as pd
# import sqlite3
# import matplotlib.pyplot as plt

# 1. Conectar e carregar dados
# conn = sqlite3.connect('seu_banco.db')
# df = pd.read_sql_query("SELECT data_inclusao FROM produtos", conn)

# # 2. Converter para datetime e agrupar
# df['data_inclusao'] = pd.to_datetime(df['data_inclusao'])
# # essa linha explicação no final
# df_mensal = df.groupby(df['data_inclusao'].dt.to_period('M')).size()

# # 3. Plotar
# df_mensal.plot(kind='bar')
# plt.show()


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


#df_mensal = df.groupby(df['data_inclusao'].dt.to_period('M')).size()
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
#PARA UMA AREA DE CANVAS O GRAFICO


# Exemplo de janela principal do Tkinter
# root1 = tk.Tk()
# root1.title("Gráfico no Tkinter")
# root1.geometry("800x600")


'''python com django

from django.db.models.functions import TruncMonth
from django.db.models import Count

resultado = sua_tabela.objects.annotate(
    mes=TruncMonth('data_inclusao')
).values('mes').annotate(total=Count('id')).order_by('mes') 




PARA UMA AREA DE CANVAS O GRAFICO

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Exemplo de janela principal do Tkinter
root = tk.Tk()
root.title("Gráfico no Tkinter")
root.geometry("800x600")

def inserir_grafico_no_tkinter(frame_destino):
    # 1. Conectar ao banco e buscar os dados (sua query original)
    conn = sqlite3.connect('estoque.db')
    query = """
    SELECT strftime('%m-%Y', data_inclusao) AS mes_ano, COUNT(*) AS total
    FROM produtos
    GROUP BY mes_ano
    ORDER BY mes_ano;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # 2. Criar a figura do Matplotlib (Note que usamos 'fig, ax = plt.subplots' em vez de plt.figure)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(df['total'], labels=df['mes_ano'], autopct='%1.1f%%', startangle=90)
    ax.set_title('Registros Incluídos por Mês')
    fig.tight_layout()

    # 3. Converter a figura do Matplotlib para um widget compatível com o Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_destino)
    canvas.draw()
    
    # 4. Posicionar o gráfico na tela usando o pack() ou grid() do Tkinter
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Criando um Frame na tela para receber o gráfico
meu_painel = tk.Frame(root)
meu_painel.pack(fill=tk.BOTH, expand=True)

# Chamando a função passando o painel onde o gráfico vai aparecer
inserir_grafico_no_tkinter(meu_painel)

root.mainloop()

O que muda em relação ao código original:
fig, ax = plt.subplots(...): Em vez de usar funções globais soltas como plt.figure(), criamos explicitamente 
um objeto de figura (fig) e de eixos (ax).
Isso é obrigatório para manipular o gráfico dentro de bibliotecas de interface como o Tkinter.

FigureCanvasTkAgg(fig, master=frame): É o "tradutor" que pega o seu gráfico do Matplotlib e o 
transforma em um elemento gráfico que o Tkinter entende.

canvas.get_tk_widget().pack(...): Insere o gráfico na tela da sua aplicação Tkinter, 
substituindo o antigo plt.show() (que abria uma janela externa separada).

O que costuma ir dentro do pack():
Geralmente, para gráficos e painéis, usamos parâmetros como estes:
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

O significado de cada parâmetro comum:

side=tk.TOP: Define que o gráfico vai se posicionar a partir do topo do painel/janela.

fill=tk.BOTH: Faz com que o gráfico tente preencher todo o espaço disponível tanto na 
horizontal quanto na vertical.

expand=True: Permite que o gráfico cresça ou diminua de tamanho caso o usuário redimensione 
a janela do aplicativo.




PODE SER FEITO EM QUALUER AREA DO TK INTER

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry("600x400")

# 1. Criamos um Frame qualquer (uma moldura/área na tela)
meu_painel = tk.Frame(root, bg="lightgray", bd=2, relief=tk.SUNKEN)
meu_painel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 2. Ao criar o canvas do gráfico, dizemos que o "master" (dono) é esse Frame
# (Aqui 'fig' é o seu gráfico do matplotlib já configurado)
canvas = FigureCanvasTkAgg(fig, master=meu_painel)
canvas.draw()

# 3. Posicionamos o gráfico dentro desse Frame usando o pack()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()
'''

 # # Cria o Combobox
    # opcoes = ["Python", "JavaScript", "C++", "Java"]
    # combo = ttk.Combobox(minhaescolha, values=opcoes, state="readonly")
    # combo.pack(pady=20)
    # combo.set("Selecione uma linguagem") # Valor inicial opcional
    # # 2. Criar uma Label para orientar o usuário
    # rotulo = tk.Label(minhaescolha, text="tipo de gráfico:")
    # rotulo.pack(anchor="w", pady=5)


#if meu_check_var.get():


# O que muda em relação ao código original:
# fig, ax = plt.subplots(...): Em vez de usar funções globais soltas como plt.figure(), criamos explicitamente 
# um objeto de figura (fig) e de eixos (ax).
# Isso é obrigatório para manipular o gráfico dentro de bibliotecas de interface como o Tkinter.

# FigureCanvasTkAgg(fig, master=frame): É o "tradutor" que pega o seu gráfico do Matplotlib e o 
# transforma em um elemento gráfico que o Tkinter entende.

# canvas.get_tk_widget().pack(...): Insere o gráfico na tela da sua aplicação Tkinter, 
# substituindo o antigo plt.show() (que abria uma janela externa separada).

# O que costuma ir dentro do pack():
# Geralmente, para gráficos e painéis, usamos parâmetros como estes:
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# O significado de cada parâmetro comum:

# side=tk.TOP: Define que o gráfico vai se posicionar a partir do topo do painel/janela.

# fill=tk.BOTH: Faz com que o gráfico tente preencher todo o espaço disponível tanto na 
# horizontal quanto na vertical.

# expand=True: Permite que o gráfico cresça ou diminua de tamanho caso o usuário redimensione 
# a janela do aplicativo.




#PODE SER FEITO EM QUALUER AREA DO TK INTER
'''
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry("600x400")

# 1. Criamos um Frame qualquer (uma moldura/área na tela)
meu_painel = tk.Frame(root, bg="lightgray", bd=2, relief=tk.SUNKEN)
meu_painel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 2. Ao criar o canvas do gráfico, dizemos que o "master" (dono) é esse Frame
# (Aqui 'fig' é o seu gráfico do matplotlib já configurado)
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=meu_painel)
canvas.draw()

# 3. Posicionamos o gráfico dentro desse Frame usando o pack()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop() 


EXPLICA PASSO A PASSO EM UM GRÁFICO DE LINHA

# Adicionando os valores exatos em cima de cada ponto da linha para facilitar a leitura
for i, txt in enumerate(totais):
    plt.annotate(str(txt), (meses[i], totais[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

Passo a Passo de cada parte:
for i, txt in enumerate(totais):

totais é a lista com os números (ex: [5, 12, 8]).

enumerate() percorre essa lista pegando duas coisas ao mesmo tempo: o índice (i) que é a posição do número (0, 1, 2...) e o valor (txt) que é o número em si (5, 12, 8).

plt.annotate(...)

É a função do Matplotlib usada para colocar um texto em uma coordenada específica do gráfico.

str(txt)

Converte o número total (que é um número inteiro) em texto, pois a função de anotação precisa receber um texto para desenhar na tela.

(meses[i], totais[i])

Indica onde o texto deve ser colocado no gráfico. Ele pega o mês correspondente na horizontal (meses[i]) e a quantidade exata na vertical (totais[i]), posicionando o número exatamente em cima da bolinha da linha.

textcoords="offset points", xytext=(0, 10)

Controla o deslocamento do texto em relação ao ponto exato:

xytext=(0, 10): Significa que o número vai ficar deslocado 0 pixels para os lados e 10 pixels para cima. Isso garante que o texto não fique colado em cima da bolinha da linha, flutuando bonitinho logo acima dela.

ha='center'

Alinha o texto horizontalmente ao centro (Horizontal Alignment), garantindo que o número fique centralizado perfeitamente em cima da marcação.

fontsize=9

Define o tamanho da fonte do número como 9, mantendo a visualização limpa e sem poluir o gráfico.






'''