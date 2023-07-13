from tkinter import *
from modulos.classes import * #montatela



#import awesometkinter as atk

largura=0
altura=0
posx=0
posy=0
X=0
ler=""
opcao=0


#def verconteudo():
#     print (f'self.codigo.get = {tela.codigo.get()}') #{tela.codigo.get()}')
     
def incluirfor_click():
     opcao=1
     opcao1=1
     global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     
     
def cosultafor_click():
     opcao=2
     opcao1=1
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
def alteracaofor_clik():
     opcao=3
     opcao1=1
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     
def excluirfor_click(): 
     opcao=4
     opcao1=1
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    # botao=Button(manutencao, text='contem', command = verconteudo)
    # botao.grid(row=20, column=1,sticky=N)
 

 

def incluicontas_click():
     opcao=1
     opcao1=2
     global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     
def consultacontas_click():
     opcao1=2
     opcao=2
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
 
def alteracaocontas_clik():
     opcao1=2
     opcao=3
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)

def exclusaocontas_click(): 
     opcao=4
     opcao1=2
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)

 
def incluirtipo_click():
     opcao=1
     opcao1=3
     global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)

     
def consultatipo_click():
     opcao1=3
     opcao=2
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)

def alteracaotipo_clik():
     opcao1=3
     opcao=3
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)

def excluirtipo_click(): 
     opcao1=3
     opcao=4
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)

janela= Tk()
janela.title("janela principal")
janela.configure(background='Gray')
janela.geometry('1500x1500')


#tela 2

janela1 = Toplevel() # janela de nível superior
janela1.title("janela de trabalho")
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
cadmenu.add_command(label = " Exclusão",command=exclusaocontas_click)
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
