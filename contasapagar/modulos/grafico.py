
import sqlite3
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib


#matplotlib.use('Agg')





  


# def inserir_grafico_no_tkinter(frame_destino):
def inserir_grafico_no_tkinter(frame_destino, combo_tipo, combo_incvenc, meu_check_var,conn,nome_tabela_escolhida):    
    # 1. Conectar ao banco e buscar os dados (sua query original)
  #  conn = sqlite3.connect('contaspagar.db')
    escolha1=combo_incvenc.get()
    if escolha1 == "Inclusao":  
        query = """
        SELECT strftime('%m-%Y', inclusao) AS mes_ano, COUNT(*) AS total
        FROM {nome_tabela_escolhida}
        GROUP BY mes_ano
        ORDER BY mes_ano;
        """
    else:
        query = """
        SELECT strftime('%m-%Y', vencimento) AS mes_ano, COUNT(*) AS total
        FROM {nome_tabela_escolhida}
        WHERE  vencimento < DATE('now') 
        GROUP BY mes_ano
        ORDER BY mes_ano;
        """    
    # # 1. Limpa qualquer widget anterior (o gráfico velho) de dentro do painel
    for widget in frame_destino.winfo_children():
        widget.destroy()
    
    plt.close('all')
    df = pd.read_sql_query(query, conn)
   # conn.close()
    escolha = combo_tipo.get()
    
    
    if escolha == "Pizza": 
      # 2. Criar a figura do Matplotlib (Note que usamos 'fig, ax = plt.subplots' em vez de plt.figure)
      fig, ax = plt.subplots(figsize=(8, 5))
      ax.pie(df['total'], labels=df['mes_ano'], autopct='%1.1f%%', startangle=90)
      if escolha1 == 'Inclusao':
        titulo = "Registros Incluídos por Mês"
      else:
         titulo = "Registros Vencidos por Mês"
      ax.set_title(titulo)
      fig.tight_layout()
    elif escolha == "Barra":
      
      fig, ax = plt.subplots(figsize=(8, 5))

      # O eixo X (mes_ano) vem primeiro, depois o eixo Y (total)
      ax.bar(df['mes_ano'], df['total'])

      if escolha1 == 'Inclusao':
        titulo = "Registros Incluídos por Mês"
      else:
         titulo = "Registros Vencidos por Mês"
      ax.set_title(titulo)
      ax.set_xlabel('Mês/Ano')
      ax.set_ylabel('Total')

      # Rotaciona os rótulos do eixo X para não embolarem
      #plt.xticks(rotation=45)
      plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

      fig.tight_layout()
    else:
      # 2. Criar a figura do Matplotlib (Note que usamos 'fig, ax = plt.subplots' em vez de plt.figure)
      fig, ax = plt.subplots(figsize=(8, 5))
      # Mudou de plt.pie para plt.plot
      # Usando o ax em vez de plt
      # Usamos marker='o' para marcar cada ponto no mês, linestyle='-' para a linha e linewidth para grossura
      ax.plot(df['mes_ano'], df['total'], marker='o', linestyle='-', color='b', linewidth=2)
      if escolha1 == 'Inclusao':
        titulo = "Registros Incluídos por Mês"
      else:
        titulo = "Registros Vencidos por Mês"
      ax.set_title(titulo)
      ax.set_xlabel('Mês/Ano')
      ax.set_ylabel('Quantidade')
      ax.tick_params(axis='x', rotation=45)  # Equivalente ao plt.xticks(rotation=45)
      ax.grid(True, linestyle='--', alpha=0.6)
      fig.tight_layout()
    #   # Usamos marker='o' para marcar cada ponto no mês, linestyle='-' para a linha e linewidth para grossura
    #   plt.plot(df['mes_ano'], df['total'], marker='o', linestyle='-', color='b', linewidth=2)
    #   # plt.bar(df['mes_ano'], df['total'], color='skyblue') 
    #   # 4. Ajustes visuais
    #   plt.title('Registros Incluídos por Mês')
    #   plt.xlabel('Mês/Ano')
    #   plt.ylabel('Quantidade')
    #   plt.xticks(rotation=45) # Gira o texto do eixo X para não sobrepor
    #   plt.grid(True, linestyle='--', alpha=0.6) # Adiciona uma grade de fundo sutil (ótimo para gráficos de linha)
    #   plt.tight_layout()      # Ajusta o layout para não cortar as legendas
     # 3. Salvar em PDF DEPOIS que o gráfico foi gerado
    if meu_check_var.get():
        fig.savefig('grafico_estoque.pdf', format='pdf', bbox_inches='tight')

   # # 5. Salvar em PDF (substitui o plt.show())
    # if meu_check_var.get():
    #   plt.savefig('grafico_estoque.pdf', format='pdf', bbox_inches='tight')     
    
    # 3. Converter a figura do Matplotlib para um widget compatível com o Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_destino)
    canvas.draw()
    
    # 4. Posicionar o gráfico na tela usando o pack() ou grid() do Tkinter
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# def inserir_grafico_no_tkinter(frame_destino):
def inserir_grafico_no_tkinter1(frame_destino, combo_tipo, meu_check_var,conn,mes_escolhido,nome_tabela_escolhida):    
    # 1. Conectar ao banco e buscar os dados (sua query original)
    # conn = sqlite3.connect('contaspagar.db')
    escolha = combo_tipo.get()
    if escolha == "Inclusao":  
        query = """
          SELECT 
          strftime('%d', inclusao) AS dia, 
          COUNT(*) AS total
          FROM {nome_tabela_escolhida}
          WHERE strftime('%Y-%m', inclusao) = ?
          GROUP BY dia
          ORDER BY dia;
          """
    else:
        query = """
             SELECT 
                 strftime('%d', data_vencimento) AS dia, 
                 COUNT(*) AS total
              FROM {nome_tabela_escolhida}
              WHERE strftime('%Y-%m', data_vencimento) = ?
              GROUP BY dia
              ORDER BY dia;
             """
    #AND vencimento < DATE('now') PARA VENCIDOS NO MES SÓ COLOCAR ANTES DO GROUP BY dia       
    cursor = conn.cursor()     
    cursor.execute(query, (mes_escolhido,))
    dados = cursor.fetchall()
    # Separando os dados para o gráfico
    dias = [row[0] for row in dados]
    totais = [row[1] for row in dados]

        # # 1. Limpa qualquer widget anterior (o gráfico velho) de dentro do painel
    for widget in frame_destino.winfo_children():
        widget.destroy()
    
    plt.close('all')
    # df = pd.read_sql_query(query, conn)
    # conn.close()
    fig, ax = plt.subplots(figsize=(8, 5))      
    plt.bar(dias, totais, color='crimson')
    plt.xlabel('Dias do Mês')
    if escolha == "Inclusao":
        # é possível trocar ax por plt
        # ax.set_ylabel('Quantidade de Produtos Inclusos')
        # ax.set_title(f'Produtos Inclusos por Dia - Referência: {mes_escolhido}')
        plt.ylabel("Quantidade de Produtos Inclusos")
        plt.title(f"Produtos Inclusos por Dia - Referência: {mes_escolhido}")
         
    else:
        # é possível trocar ax por plt
        # ax.set_ylabel('Quantidade de Produtos Vencidos')
        # ax.set_title(f'Produtos Vencidos por Dia - Referência: {mes_escolhido}')
        plt.ylabel("Quantidade de Produtos Vencidos")
        plt.title(f"Produtos Vencidos por Dia - Referência: {mes_escolhido}")
      
      # O eixo X (mes_ano) vem primeiro, depois o eixo Y (total)
      
      # Rotaciona os rótulos do eixo X para não embolarem
      #plt.xticks(rotation=45)
      
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    fig.tight_layout()  
      
    # 3. Salvar em PDF DEPOIS que o gráfico foi gerado
    if meu_check_var.get():
        fig.savefig('grafico_estoque.pdf', format='pdf', bbox_inches='tight')

   # # 5. Salvar em PDF (substitui o plt.show())
    # if meu_check_var.get():
    #   plt.savefig('grafico_estoque.pdf', format='pdf', bbox_inches='tight')     
    
    # 3. Converter a figura do Matplotlib para um widget compatível com o Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_destino)
    canvas.draw()
    
    # 4. Posicionar o gráfico na tela usando o pack() ou grid() do Tkinter
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def pegar_selecao(event):
    # event.widget é o Combobox, e o .get() extrai o texto selecionado dele
    valor_escolhido = event.widget.get() 
    
    print(f"Você escolheu: {valor_escolhido}")
    
def desativar_x():
    pass

def fechar_programa1(janela,conn):
    conn.close()      # Fecha a conexão com o banco
    janela.destroy()   # Destrói a janela de vez e limpa da memória

# 1. Criar um Frame (ou usar sua estrutura existente)
def grafico_tela():
    matplotlib.use('Agg')
    root1 = tk.Toplevel()
    root1.title("Gráfico de Inclusões por Mês")
    root1.geometry("800x600")
    root1.grab_set()
    # Faz a janela abrir maximizada no Windows
    root1.state('zoomed')
    # 1. Conectar ao seu banco de dados
    conn = sqlite3.connect('contaspagar.db')
    #root1.protocol("WM_DELETE_WINDOW", fechar_programa1)
    # Configura o fechamento da janela usando lambda para passar a root1 correta
    #root1.protocol("WM_DELETE_WINDOW", lambda: fechar_programa1(root1))
    # 2. Atrela essa função vazia ao protocolo do "X"
    root1.protocol("WM_DELETE_WINDOW", desativar_x)
    # 3. Cria o seu próprio botão ou menu "Sair" que realmente fecha a janela
    
    minhaescolha = tk.Frame(root1)
    minhaescolha.pack(padx=20, pady=20)
    
      

    # Variável de controle
    meu_check_var = tk.BooleanVar(value=False)

    # Criando o Checkbutton e ligando à variável
    chk = ttk.Checkbutton(minhaescolha, text="Grava em Pdf", variable=meu_check_var)
    chk.pack(side=tk.LEFT,padx=40)
    
   
    # 3. Criar o Combobox
    # Definimos as opções disponíveis usando o parâmetro 'values'
    opcoes = ["Barra", "Pizza", "Linha"]
    combo_tipo = ttk.Combobox(minhaescolha, values=opcoes, state="readonly") # "readonly" impede que o usuário digite texto livre
    combo_tipo.pack(side=tk.LEFT,padx=40)
    # Opcional: Selecionar um item padrão inicial (ex: o primeiro da lista)
    combo_tipo.current(0)


    #vencimento/inclusao
    #####################

    opcoes1 = ["Inclusao", "Vencidos"]
    combo_incvenc = ttk.Combobox(minhaescolha, values=opcoes1, state="readonly") # "readonly" impede que o usuário digite texto livre
    combo_incvenc.pack(side=tk.LEFT,padx=40)
    # Opcional: Selecionar um item padrão inicial (ex: o primeiro da lista)
    combo_incvenc.current(0)
     
    
    # 4. Função para pegar o valor que o usuário escolheu
    #escolha = combo_tipo.get()
    # Associa o evento de mudança ao combobox
    combo_incvenc.bind("<<ComboboxSelected>>",pegar_selecao)

    ####################

    btn_sair = ttk.Button(minhaescolha, text="Sair / Fechar", command= lambda: fechar_programa1(root1,conn))
    btn_sair.pack(side=tk.LEFT, padx=40) # padx adiciona um espaço horizontal entre eles 
    
    # 4. Função para pegar o valor que o usuário escolheu
    #escolha = combo_tipo.get()
    # Associa o evento de mudança ao combobox
    combo_tipo.bind("<<ComboboxSelected>>",pegar_selecao)

   

    # Criando um Frame na tela para receber o gráfico
    meu_painel = tk.Frame(root1)
    meu_painel.pack(fill=tk.BOTH, expand=True)

    # Chamando a função passando o painel onde o gráfico vai aparecer

    # COMO ASSOCIAR A TECLA F3:
    # Usamos lambda para passar o 'frame_destino' para a sua função,
    # já que o bind vai injetar o argumento 'event' automaticamente.
    # ---------------------------------------------------------
    root1.bind("<F3>", lambda event: inserir_grafico_no_tkinter(meu_painel, combo_tipo,combo_incvenc, meu_check_var,conn))
    # 3. Força o foco do sistema operacional para esta janela imediatamente
    root1.focus_force()
    
    root1.title("Atalho F3 para Gráfico")
# 2. Define uma função chamada 'validar_input' que recebe o argumento 'P'    
def validar_input(P):
    # P é o valor que o Entry *terá* se a ação for permitida
    # Permite apenas números e o hífen, com no máximo 7 caracteres
    # 3. Comentário explicando que 'P' representa o valor que o campo 'Entry' passará a ter caso a digitação seja permitida
    # 4. Verifica se o comprimento (quantidade de caracteres) do texto em 'P' é menor ou igual a 7
    if len(P) <= 7:
        # 5. Verifica se todos os caracteres da string 'P' são dígitos numéricos OU se o caractere é um hífen ('-')
        if all(c.isdigit() or c == '-' for c in P):
            # 6. Se a verificação anterior for verdadeira, retorna True, permitindo que o caractere seja digitado
            return True
    # 7. Se a quantidade passar de 7 ou houver algum caractere inválido, retorna False, bloqueando a digitação        
    return False

def grafico_tela_mes():
    matplotlib.use('Agg')
    root1 = tk.Toplevel()
    root1.title("Gráfico em determinado Mês")
    root1.geometry("800x600")
    root1.grab_set()
    # Faz a janela abrir maximizada no Windows
    root1.state('zoomed')
    # 1. Conectar ao seu banco de dados
    conn = sqlite3.connect('contaspagar.db')
    #root1.protocol("WM_DELETE_WINDOW", fechar_programa1)
    # Configura o fechamento da janela usando lambda para passar a root1 correta
    #root1.protocol("WM_DELETE_WINDOW", lambda: fechar_programa1(root1))
    # 2. Atrela essa função vazia ao protocolo do "X"
    root1.protocol("WM_DELETE_WINDOW", desativar_x)
    # 3. Cria o seu próprio botão ou menu "Sair" que realmente fecha a janela
    
    minhaescolha = tk.Frame(root1)
    minhaescolha.pack(padx=20, pady=20)
    
      

    # Variável de controle
    meu_check_var = tk.BooleanVar(value=False)

    # Criando o Checkbutton e ligando à variável
    chk = ttk.Checkbutton(minhaescolha, text="Grava em Pdf", variable=meu_check_var)
    chk.pack(side=tk.LEFT,padx=40)
    #tk.label
    # 8. Registra a função Python 'validar_input' no interpretador do Tkinter para que ele possa usá-la como regra
    vcmd = root1.register(validar_input)
    tk.Label(minhaescolha, text="Digite o Mês").pack(side=tk.LEFT,padx=10)
    #mes_escolhido = tk.Entry(minhaescolha).pack(side=tk.LEFT,padx=40)
    # Cria o Entry já aplicando a regra

    # 9. Cria o campo de texto (Entry), configurando-o para validar a cada tecla pressionada ('validate="key"') 
    # e passando a regra registrada junto com o argumento '%P' (que envia o futuro texto para a função)
    mes_escolhido = tk.Entry(minhaescolha, validate="key", validatecommand=(vcmd, '%P'))
    mes_escolhido.pack(side=tk.LEFT,padx=10)
    mes_escolhido.insert(0, "AAAA-MM")
    # 3. Criar o Combobox
    # Definimos as opções disponíveis usando o parâmetro 'values'
    
    opcoes = ["Inclusao", "Vencimento"]
    combo_tipo = ttk.Combobox(minhaescolha, values=opcoes, state="readonly") # "readonly" impede que o usuário digite texto livre
    combo_tipo.pack(side=tk.LEFT,pady=40)
    # Opcional: Selecionar um item padrão inicial (ex: o primeiro da lista)
    combo_tipo.current(0)
    btn_sair = ttk.Button(minhaescolha, text="Sair / Fechar", command= lambda: fechar_programa1(root1,conn))
    btn_sair.pack(side=tk.LEFT, padx=40) # padx adiciona um espaço horizontal entre eles 
    
    # 4. Função para pegar o valor que o usuário escolheu
    #escolha = combo_tipo.get()
    # Associa o evento de mudança ao combobox
    combo_tipo.bind("<<ComboboxSelected>>",pegar_selecao)

    # Criando um Frame na tela para receber o gráfico
    meu_painel = tk.Frame(root1)
    meu_painel.pack(fill=tk.BOTH, expand=True)

    # Chamando a função passando o painel onde o gráfico vai aparecer

    # COMO ASSOCIAR A TECLA F3:
    # Usamos lambda para passar o 'frame_destino' para a sua função,
    # já que o bind vai injetar o argumento 'event' automaticamente.
    # ---------------------------------------------------------
    #tirei m_escolhido.get()
    root1.bind("<F3>", lambda event: inserir_grafico_no_tkinter1(meu_painel, combo_tipo, meu_check_var,conn,mes_escolhido.get()))
    # 3. Força o foco do sistema operacional para esta janela imediatamente
    root1.focus_force()
    
    root1.title("Atalho F3 para Gráfico")