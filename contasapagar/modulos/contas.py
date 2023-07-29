from tkinter import *
from tkinter import messagebox
import rotinas
import sqlite3
from sqlite3 import Error
from time import sleep
from classes import montatela,centralizacao
import keyboard
#from contasapagar import *

largura=0
altura=0
posx=0
posy=0
X=0
ler=""
opcao=0


def incluicontas_click(janela1):
     opcao=1
     opcao1=2
  #   global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     #if flag==True: 
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRIMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
     
     #
     banco.commit()
     cursor.execute("SELECT * FROM contas")
     print(cursor.fetchall())
def consultacontas_click(janela1):
     opcao1=2
     opcao=2
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     #if flag==True: 
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()

      # CONSTRAINT fk_PesCarro FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa (ID_Pessoa)
     cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRIMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
     
     #
     banco.commit()
     cursor.execute("SELECT * FROM contas")
     print(cursor.fetchall())
def alteracaocontas_clik(janela1):
     opcao1=2
     opcao=3
    # global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    # if flag==True: 
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRIMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
    
     #
     banco.commit()
     cursor.execute("SELECT * FROM contas")
     print(cursor.fetchall())
def excluircontas_click(janela1):
   opcao1=2
   opcao=4
  # global tela
   manutencao = Toplevel() # janela de nível superior
   tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
  # if flag==True: 
   banco = sqlite3.connect('contaspagar.db')
   cursor = banco.cursor()
   cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRIMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
    
     #
   banco.commit()
   cursor.execute("SELECT * FROM contas")
   print(cursor.fetchall())

def contas_menu(janela1):
 janela2 = Toplevel() # janela de nível superior
 janela2.title("Menu Manutenção - Relatórios")
#janela1.configure(height= 400)
#janela1.configure(width= 400) 
           
janela2.resizable(False, False) # tamanho fixo             
janela2.transient(janela1) # de onde vem a janela
janela2.focus_force() #forçar foco
janela2.grab_set()    # impede que click na janela principal sem fechar janela atiual
#janela1.configure(background='red')
#janela1.overrideredirect(True)  

#adicionando menu

menujan1 = Menu(janela2),
cadmenu = Menu(menujan2, tearoff=0)
cadmenu.add_command(label = " Inclusão",command=lambda: incluicontas_click(janela2))
cadmenu.add_command(label = " Consulta", command=lambda: consultacontas_click(janela2))
cadmenu.add_command(label = " Alteração",command=lambda: alteracaocontas_clik(janela2))
cadmenu.add_command(label = " Exclusão",command=lambda: excluircontas_click(janela2)
menujan.add_cascade(label = "Contas a pagar", menu = cadmenu)

consultamenu= Menu(menujan2, tearoff=0,)
consultamenu.add_command(label = " Inclusão",command= lambda: incluirfor_click(janela2))
consultamenu.add_command(label = " Consulta",command= lambda: cosultafor_click(janela2))
consultamenu.add_command(label = " Alteração",command=lambda: alteracaofor_clik(janela2))
consultamenu.add_command(label = " Excluir", command=lambda:  excluirfor_click(janela2))
menujan2.add_cascade(label = "Consutas diversas", menu = consultamenu)


editmenu = Menu(menujan1, tearoff=0)
editmenu.add_command(label = "contas a pagar")
editmenu.add_command(label = "contas a pagar por fornecedor")
editmenu.add_command(label = "Contas a pagar por nome")
editmenu.add_command(label = "Contas a pagar por CNPJ Ou CPF")
menujan1.add_cascade(label = "Relatórios", menu = editmenu)
menusair = Menu(menujan1, tearoff=0)
menusair.add_command(label= "Sair click aqui", command=quit) 
menujan1.add_cascade(label='para Sair',menu = menusair)
janela2.config(menu=menujan) #linha necessaria para aprecer o menu na janela de trabalho
largura= 550
altura = 450
centro=centralizacao(janela1,largura, altura, posx, posy)

janela2.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
janela2.mainloop()