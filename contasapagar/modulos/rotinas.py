from tkinter import *
import keyboard
import sqlite3
from sqlite3 import Error

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






def criartabela2(janela3,sql):

   try:
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     
     cursor.execute(sql)
     cursor.close() 
     #cs compra ou serviço
   except Error as ex:
     messagebox1(str(ex)+ " linha 439",janela3)
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

    

def lertabela(sql,codigomem,manutencao,mensagem):
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
          messagebox1("esse "+mensagem+" não existe",manutencao)  
          return  sqlres
       else:
               
        return sqlres 
   except Error as ex:
       messagebox1("Erro na leitura da tabela"+mensagem+"  linha 131 em rotinas "+str(ex),manutencao)
       
       
       return sqlres

