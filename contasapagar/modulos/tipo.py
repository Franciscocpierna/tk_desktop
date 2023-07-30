from tkinter import *
from tkinter import messagebox
import rotinas
import sqlite3
from sqlite3 import Error
from time import sleep
from classes import montatela,centralizacao
import keyboard
from contaspagar import *

largura=1200
altura=650
posx=0
posy=0
X=0
ler=""
opcao=0


def incluirtipo_click(janela1):
     opcao=1
     opcao1=3
   #  global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
   #  if flag==True: 
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor (codigo text, nome text,
                                               endereco text, telefone text,
                                               tipo text,cpf text,cnpj text  )''')
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')

     banco.commit()
     cursor.execute("SELECT * FROM fornecedor")
     print(cursor.fetchall())
     
def consultatipo_click(janela1):
     opcao1=3
     opcao=2
    # global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    # if flag==True: 
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor (codigo text, nome text,
                                               endereco text, telefone text,
                                               tipo text,cpf text,cnpj text  )''')
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')

     banco.commit()
     cursor.execute("SELECT * FROM fornecedor")
     print(cursor.fetchall())  
def alteracaotipo_clik(janela1):
     opcao1=3
     opcao=3
     #global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     #if flag==True: 
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor (codigo text, nome text,
                                               endereco text, telefone text,
                                               tipo text,cpf text,cnpj text  )''')
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')

     banco.commit()
     cursor.execute("SELECT * FROM fornecedor")
     print(cursor.fetchall())
def excluirtipo_click(janela1): 
     opcao1=3
     opcao=4
     #global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor (codigo text, nome text,
                                               endereco text, telefone text,
                                               tipo text,cpf text,cnpj text  )''')
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')

     banco.commit()
     cursor.execute("SELECT * FROM fornecedor")
     print(cursor.fetchall())

def tipo_menu(janela1):
   pass
#cadtipo = Menu(menujan, tearoff=0)
#cadtipo.add_command(label = " Inclusão",command=lambda: incluirtipo_click(janela1))
#cadtipo.add_command(label = " Consulta", command=lambda: consultatipo_click(janela1))
#cadtipo.add_command(label = " Alteração", command=lambda: alteracaotipo_clik(janela1))
#cadtipo.add_command(label = " Exclusão",command=lambda: excluirtipo_click(janela1))
#menujan.add_cascade(label = "Tipo de pagamento", menu = cadtipo)
#menusair = Menu(menujan, tearoff=0)
#menusair.add_command(label= "Sair click aqui", command=quit) 
#menujan.add_cascade(label='para Sair',menu = menusair)