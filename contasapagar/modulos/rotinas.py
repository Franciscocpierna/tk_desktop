from tkinter import *
import keyboard
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from tkinter import filedialog
import shutil
import os
import datetime
from time import sleep

def messagebox1(msg,manutencao):
    toplevel = Toplevel()
 
    toplevel.title("click em OK ou Tecla <enter> para Fechar")
    x_position = 300
    y_position = 200
    #toplevel.geometry(f"300x100+{x_position}+{y_position}")
    toplevel.geometry(f"550x100+{x_position}+{y_position}")
    toplevel.resizable(False, False) # tamanho fixo             
    toplevel.transient(manutencao) # de onde vem a janela
    toplevel.focus_force() #forçar foco
    toplevel.grab_set()    # impede que click na janela principal sem fechar janela atiual
    l1=Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="cvbnm,m")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
    l2["text"] = msg
    b1=Button(toplevel, text="OK", command=toplevel.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    keyboard.on_press_key("enter", lambda _: toplevel.destroy())




def salvar_bco():
    # 1. Solicita ao usuário que escolha o arquivo de banco de dados original
    arquivo_origem = filedialog.askopenfilename(
        title="Selecione o arquivo de banco de dados para copiar",
        filetypes=[("Banco de dados SQLite", "*.db")],
        initialdir="." # Começa a busca no diretório atual
    )

    # Se o usuário cancelar a seleção, encerra a função
    if not arquivo_origem:
        return
    # Pega a data atual no formato brasileiro (ex: 26-08-2026)
    data_atual = datetime.date.today().strftime("%d-%m-%Y")
    # 2. Solicita ao usuário onde ele deseja salvar a cópia
    caminho_destino = filedialog.asksaveasfilename(
        defaultextension=".db",
        filetypes=[("Banco de dados SQLite", "*.db")],
        title="Salvar cópia do banco de dados",
        initialfile = f"copia_{data_atual}_{os.path.basename(arquivo_origem)}"
    )

    # 3. Executa a cópia se o caminho de destino for definido
    if caminho_destino:
        try:
            shutil.copy2(arquivo_origem, caminho_destino)
            messagebox.showinfo("Sucesso", f"Backup realizado com sucesso em:\n{caminho_destino}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao realizar backup: {e}")



def criartabela2(janela3,sql):

   try:
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     
     cursor.execute(sql)
     cursor.close() 
     #cs compra ou serviço
   except Error as ex:
     messagebox1(str(ex)+ " linha 44 em rotinas",janela3)
     return 
   return 

def leiaInt1(msg):
  while True:
    try:
       n=int(input(msg))
    except (ValueError,TypeError):
       print('\n\033[31mErro: por favor, digite um número inteiro válido.\033[m')
    except (KeyboardInterrupt):
       print('\n\033[31mErro: por favor, digite um número inteiro válido.\033[m')
       return 0
    else:
       return n

def leiaFloat(msg):
  while True:
   try:
        n = str(input(msg))
        n = n.replace(',', '.')
        n = float(n)
   except (ValueError, TypeError):
          print('\033[0;31m erro: digite um numero real valido.\033[m')
          continue
   except (KeyboardInterrupt):
          print('\033[31mUsuário preferiu não digitar esse número:\033[m')
          return 0
   else:
          if (n // 1 == n):  # se a divisão por 1 igual n entao é inteiro se nao float
             n = int(n)
             return n

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
         valor = int(n)
         ok = True
        else:
          print ('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
             break
    return valor

def continua():
    while True:
        try:
            r=str(input('quer continuar:[S/N] ').upper()[0])
        except (KeyboardInterrupt):
            print('\n\033[31mErro: interrompeu execução\033[m')
            return 'N'
        except IndexError:
            print('\033[31mdigite opção valida S ou N: \033[m')
        else:
            if r not in "SN":
                 print('\033[31mdigite opção valida S ou N: \033[m')
            else:
                 return r

    

def lertabela(sql,codigomem,manutencao,mensagem,opcao=0):
   sqlres=""
   
   try:
       banco = sqlite3.connect('contaspagar.db')
       cursor = banco.cursor()
   except Error as ex:
       messagebox1("Erro na conexão com Banco de dados linha 115 em rotinas "+str(ex),manutencao)
       
       
       return sqlres 
   
   try:
       cursor.execute(sql)
       sqlres=cursor.fetchall()
       cursor.close() 
       if len(sqlres) == 0:
         if opcao!=1:
           messagebox1("esse "+mensagem+" não existe",manutencao)  
         return  sqlres
       else:
         return  sqlres   
        
   except Error as ex:
       messagebox1("Erro na leitura da tabela"+mensagem+"  linha 131 em rotinas "+str(ex),manutencao)
       
       
       return sqlres

def lertabela1(sql,codigomem,documentomem,tparcelamem,manutencao,mensagem,opcao=0):
   sqlres=""
   
   try:
       banco = sqlite3.connect('contaspagar.db')
       cursor = banco.cursor()
   except Error as ex:
       messagebox1("Erro na conexão com Banco de dados linha 115 em rotinas "+str(ex),manutencao)
       
       
       return sqlres 
   
   try:
       cursor.execute(sql)
       sqlres=cursor.fetchall()
       cursor.close() 
       if len(sqlres) == 0: 
          if opcao!=1:
            messagebox1("esse "+mensagem+" não existe",manutencao)  
          return  sqlres
       else:
          if opcao ==1:
              pass
           # messagebox1("esse "+mensagem+" já  existe não pode incluir ",manutencao)                  
       return sqlres 
   except Error as ex:
       messagebox1("Erro na leitura da tabela"+mensagem+"  linha 159 em rotinas "+str(ex),manutencao)
       
       
       return sqlres

def validar_data(P): #essa rotina pra incluir a / sem digitar usando # 4. Registra cada função separadamente
  # no motor do Tkinter
  # vcmd_data = root.register(validar_data)
  #  tk.Label(root, text="Data de Vencimento:", font=("Arial", 10)).pack(pady=(15, 0))
  # entry_data = tk.Entry(root, validate="key", validatecommand=(vcmd_data, '%P'), font=("Arial", 12))
  # entry_data.pack(pady=5)
  # entry_data.insert(0, "DD/MM/AAAA")
  if P == "":
    return True
  if len(P) > 10:
    return False

  # Extrai apenas os números digitados
  numeros = "".join(c for c in P if c.isdigit())

  # Reconstrói a string adicionando a barra após o índice 1 (2º número)
  # e após o índice 3 (4º número)
  novo_P = ""
  for i, c in enumerate(numeros):
    if i == 2 or i == 4:  # Equivalente a somar a barra após o índice 1 e após o 3
      novo_P += "/"
    novo_P += c

  # Atualiza a StringVar e o cursor se o texto formatado for diferente
  if len(novo_P) <= 10 and novo_P != P:
    data_var.set(novo_P)
    entry_data.icursor(len(novo_P))
    return False

  # Validação mantendo as posições das barras em 2 e 5 na string final
  for i, c in enumerate(P):
    if i == 2 or i == 5:
      if c != "/":
        return False
    else:
      if not c.isdigit():
        return False

  return True


  #explicação dessa parte do programa


  # # Atualiza a StringVar e o cursor se o texto formatado for diferente
  # if len(novo_P) <= 10 and novo_P != P:
  #   data_var.set(novo_P)
  #   entry_data.icursor(len(novo_P))
  #   return False
  #


#   Essa rotina é o "truque" necessário para fazer a barra aparecer automaticamente enquanto você digita no Entry do Tkinter. Sem essa parte, a função apenas validaria o que você digitou, mas não teria "poder" para alterar o texto que está dentro da caixinha.

#   Aqui está o passo a passo do que acontece:

# 1. O que é a StringVar e o Entry?
# data_var = tk.StringVar(): É uma variável especial do Tkinter que fica "conectada" ao campo de texto. Quando você muda o valor dessa variável, o campo de texto muda automaticamente.

# entry_data = tk.Entry(..., textvariable=data_var): O campo de texto está "ouvindo" a data_var.

# 2. O que a rotina faz?
# Quando você digita um número, o validatecommand dispara a função validar_data(P):

# novo_P = ...: A função pega o que você digitou, remove tudo que não é número e monta uma "versão corrigida" (ex: você digitou "12", a função monta "12/").

# if novo_P != P:: Ela compara o que você digitou (P) com a versão correta que ela montou (novo_P). Se forem diferentes (ex: você digitou "12" e o formato correto é "12/"), ela entra no if.

# data_var.set(novo_P): Aqui está a mágica! Ela força o campo a exibir a barra que ela criou. O campo de texto, que antes tinha apenas "12", agora passa a ter "12/".

# entry_data.icursor(len(novo_P)): Quando você altera o texto via código, o cursor do teclado às vezes pula para o início. Esse comando diz: "coloque o cursor no final do texto" para que você possa continuar digitando o próximo número normalmente.

# return False: Este é o ponto mais importante. Ao retornar False, você diz ao Tkinter: "Não aceite o caractere que o usuário acabou de digitar (aquela tecla que ele apertou), pois eu já corrigi o texto manualmente via data_var".

# Resumo em termos simples:
# Imagine que o validatecommand é um segurança na porta.

# Quando o segurança vê você tentando digitar apenas um número, ele diz: "Espera, falta a barra!".

# Em vez de apenas te bloquear (retornar False), ele mesmo pega uma caneta, coloca a barra para você (data_var.set), coloca o cursor no lugar certo (icursor) e depois te bloqueia (return False) apenas para evitar que o número que você digitou apareça duplicado ou fora de lugar.

# Por que isso é necessário?
# O validatecommand só consegue dizer "aceito" ou "rejeito" o que o usuário digitou. Ele não consegue mudar o texto por conta própria durante a validação. Por isso, usamos o data_var.set() para mudar o texto e return False para cancelar a digitação original, deixando apenas a nossa versão corrigida.