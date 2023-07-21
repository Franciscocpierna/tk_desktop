from tkinter import *
from tkinter import messagebox
import rotinas
import sqlite3
from sqlite3 import Error
from time import sleep
from classes import montatela,centralizacao
   

#from modulos.classes import *

largura=0
altura=0
posx=0
posy=0
X=0
ler=""
opcao=0
flag=False
msg =""
 

def limpacamposfor():
  tela.codigo.delete(0,END)
  tela.nome.delete(0,END) 
  tela.endereco.delete(0,END) 
  tela.telefone.delete(0,END)
  tela.tipo.delete(0,END) 
  tela.cpf.delete(0,END)
  tela.cnpj.delete(0,END)
  tela.cep.delete(0,END)
  tela.e_mail.delete(0,END)
  return



def incluirfor():
   sqlres=""
   flag == True
   try:
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor (codigo varchar(5) NOT NULL, nome varchar(50) NOT NULL,
                                               endereco varchar(50) NOT NULL, telefone varchar(11),
                                               tipo varchar(1)NOT NULL,cpf varchar(11),cnpj varchar(14),cep varchar(8),
                                               e_mail varchar(17), 
                                               PRYMARY KEY (codigo) )''')
     cursor.close() 
   except Error as ex:
     messagebox.showinfo(title="",message=ex)
     #tela.informacao["text"] = "Informação:" + str(ex)
     # tela.informacao["text"] = "Informação:"
     print(ex)
   if len(tela.codigo.get())!=5:
        messagebox.showinfo(title="digite codigo",message="codigo tamanho 5")
        tela.codigo.focus()
        return    
   elif len(tela.nome.get())==0 or len(tela.nome.get())>50:
        msg = "Informação: digite o Nome esta vazio"
        messagebox.showinfo(title="digite nome",message="tamanho 50 máximo")
        tela.nome.focus()
        return
   elif len(tela.endereco.get())==0 or len(tela.endereco.get())>50: 
        messagebox.showinfo(title="digite endereço",message="tamanho 50 máximo")
        tela.endereco.setfocus()
        return
   elif len(tela.telefone.get())==0 or len(tela.telefone.get())>11:
        messagebox.showinfo(title="digite Telefone",message="tamanho 11 máximo")
        tela.telefone.setfocus()
        return    
   elif len(tela.tipo.get())!=1 or tela.tipo.get() not in ("F","J"):
        messagebox.showinfo(title="digite Tipo",message="tamanho 1 e (F)isica ou (J)")
        tela.tipo.setfocus()
        return        
   else:
      try:
       banco = sqlite3.connect('contaspagar.db')
       cursor = banco.cursor()
       sqlres=cursor.execute("SELECT * FROM fornecedor WHERE codigo = tela.codigo.get()")
       if sqlres != "":
          cursor.execute('''INSERT INTO fornecedor VALUES(tela.codigo.get(),tela.nome.get(),tela.endereco.get(),
                                                  tela.telefone.get(),tela.telefone.get(),tela.cpf.get(),tela.cnpj.get(),
                                                  tela.cep.get(), tela.e_mail.get())''')
          banco.commit()
          cursor.close()     
       else:
            msg= "Informação: Registro já existe não pode ser inserido" 
            sleep(5)
            limpacamposfor()
       
      except Error as ex:
       messagebox.showinfo(title="erro",message=ex)
       limpacamposfor()   
      return
   
def incluirfor_click():
    opcao=1
    opcao1=1
    global tela  
    manutencao = Toplevel() # janela de nível superior
    tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    botao=Button(manutencao, text='Salvar',command=incluirfor)
    botao.grid(row=9, column=0,padx=0,pady=50,sticky=W)
    
    #tela.informacao.configure(text="Informação: digite o Codigo com tamanho 5 ")
    #tela.informacao["text"] ="Informação:"

    tela.codigo.focus() 
    
    messagebox.showinfo(title="digite codigo",message="codigo tamanho 5")
          
    
    
    
           
     
def cosultafor_click():
     opcao=2
     opcao1=1
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
      
      banco.commit()
      cursor.execute("SELECT * FROM fornecedor")
      print(cursor.fetchall())
     
def alteracaofor_clik():
     opcao=3
     opcao1=1
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
     
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')

      banco.commit()
      cursor.execute("SELECT * FROM fornecedor")
      print(cursor.fetchall())
     
     
def excluirfor_click(): 
     opcao=4
     opcao1=1
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    # botao=Button(manutencao, text='contem', command = verconteudo)
    # botao.grid(row=20, column=1,sticky=N)
     if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
     
     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')

      banco.commit()
      cursor.execute("SELECT * FROM fornecedor")
      print(cursor.fetchall())
     

 

def incluicontas_click():
     opcao=1
     opcao1=2
     global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRYMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
     
     #
      banco.commit()
      cursor.execute("SELECT * FROM contas")
      print(cursor.fetchall())
def consultacontas_click():
     opcao1=2
     opcao=2
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()

      # CONSTRAINT fk_PesCarro FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa (ID_Pessoa)
     cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRYMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
     
     #
     banco.commit()
     cursor.execute("SELECT * FROM contas")
     print(cursor.fetchall())
def alteracaocontas_clik():
     opcao1=2
     opcao=3
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRYMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
    
     #
      banco.commit()
      cursor.execute("SELECT * FROM contas")
      print(cursor.fetchall())
def exclircontas_click():
   opcao1=2
   opcao=4
   global tela
   manutencao = Toplevel() # janela de nível superior
   tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
   if flag==True: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5) NOT NULL, pagamento varchar(10),
                                               compra varchar(10) NOT NULL, descricao varchar(50),
                                               desconto numeric(10,2),valpagar numeric(10,2),
                                               juros numeric(10,2),documento varchar(50),tparcela varchar(1),
                                               situacao varchar(1),
                                               cs varchar(1),
                                               PRYMARY KEY codigo+documento,FOREIGN KEY (codigo) REFERENCES fornecedor(codigo),FOREIGN KEY (tparcela) REFERENCES tipo(codigo))''')

     # cursor.execute('''INSERT INTO fornecedor VALUES('1','João','Rua tal nr 97',
     #                                            'F','504.543.417.20','teste','teste1')''')
    
     #
      banco.commit()
      cursor.execute("SELECT * FROM contas")
      print(cursor.fetchall())
def incluirtipo_click():
     opcao=1
     opcao1=3
     global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
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
     
def consultatipo_click():
     opcao1=3
     opcao=2
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
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
def alteracaotipo_clik():
     opcao1=3
     opcao=3
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
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
def excluirtipo_click(): 
     opcao1=3
     opcao=4
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     if flag==True: 
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
janela= Tk()
janela.title("Sistema de Contas a Pagar")
janela.configure(background='Gray')
janela.geometry('1500x1500')


#tela 2

janela1 = Toplevel() # janela de nível superior
janela1.title("Menu Manutenção - Relatórios")
#janela1.configure(height= 400)
#janela1.configure(width= 400) 
           
janela1.resizable(False, False) # tamanho fixo             
janela1.transient(janela) # de onde vem a janela
janela1.focus_force() #forçar foco
janela1.grab_set()    # impede que click na janela principal sem fechar janela atiual
#janela1.configure(background='red')
#janela1.overrideredirect(True)  

#adicionando menu

menujan = Menu(janela1)
filemenu= Menu(menujan, tearoff=0,)
filemenu.add_command(label = " Inclusão",command=incluirfor_click)
filemenu.add_command(label = " Consulta",command=cosultafor_click)
filemenu.add_command(label = " Alteração",command=alteracaofor_clik)
filemenu.add_command(label = " Excluir", command=excluirfor_click )
#filemenu.add_separator()
#filemenu.add_command(label='Sair', command=quit)

menujan.add_cascade(label = "Fornecedor", menu = filemenu)
cadmenu = Menu(menujan, tearoff=0)
cadmenu.add_command(label = " Inclusão",command=incluicontas_click)
cadmenu.add_command(label = " Consulta", command=consultacontas_click)
cadmenu.add_command(label = " Alteração",command=alteracaocontas_clik)
cadmenu.add_command(label = " Exclusão",command=exclircontas_click)
menujan.add_cascade(label = "Contas a pagar", menu = cadmenu)

cadtipo = Menu(menujan, tearoff=0)
cadtipo.add_command(label = " Inclusão",command=incluirtipo_click)
cadtipo.add_command(label = " Consulta", command=consultatipo_click)
cadtipo.add_command(label = " Alteração",command=alteracaotipo_clik)
cadtipo.add_command(label = " Exclusão",command=excluirtipo_click)
menujan.add_cascade(label = "Tipo de pagamento", menu = cadtipo)

editmenu = Menu(menujan, tearoff=0)
editmenu.add_command(label = "contas a pagar")
editmenu.add_command(label = "contas a pagar por fornecedor")
editmenu.add_command(label = "Contas a pagar por nome")
editmenu.add_command(label = "Contas a pagar por CNPJ Ou CPF")
menujan.add_cascade(label = "Relatórios", menu = editmenu)
menusair = Menu(menujan, tearoff=0)
menusair.add_command(label= "Sair click aqui", command=quit) 
menujan.add_cascade(label='para Sair',menu = menusair)
janela1.config(menu=menujan) #linha necessaria para aprecer o menu na janela de trabalho
largura= 500
altura = 400
centro=centralizacao(janela1,largura, altura, posx, posy)

janela1.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
largura=1200
altura=650
janela1.mainloop()
janela.mainloop()