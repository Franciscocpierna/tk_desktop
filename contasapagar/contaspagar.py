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


def verconteudo():
     print (f'self.codigo.get = {tela.codigo.get()}') #{tela.codigo.get()}')
     
def incluir_click():
     opcao=1
     global tela  
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     botao=Button(manutencao, text='contem', command = verconteudo)
     botao.grid(row=20, column=0,sticky=N)
     
def cosulta_click():
     opcao=2
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     botao=Button(manutencao, text='contem', command = verconteudo)
     botao.grid(row=20, column=0,sticky=E) 
def alteracao_clik():
     opcao=3
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     botao=Button(manutencao, text='contem', command = verconteudo)
     botao.grid(row=20, column=0,sticky=N)
def excluir_click(): 
     opcao=4
     global tela
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     botao=Button(manutencao, text='contem', command = verconteudo)
     botao.grid(row=20, column=1,sticky=N)
 
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
filemenu.add_command(label = "inclusão",command=incluir_click)
filemenu.add_command(label = "consulta",command=cosulta_click)
filemenu.add_command(label = "alteração",command=alteracao_clik)
filemenu.add_command(label = "excluir", command=excluir_click )
filemenu.add_separator()
filemenu.add_command(label='Sair', command=quit)

menujan.add_cascade(label = "Manutenção", menu = filemenu)
editmenu = Menu(menujan, tearoff=0)
editmenu.add_command(label = "contas a pagar")
editmenu.add_command(label = "contas a pagar por fornecedor")
editmenu.add_command(label = "Contas a pagar por nome")
editmenu.add_command(label = "Contas a pagar por CNPJ Ou CPF")
menujan.add_cascade(label = "Relatórios", menu = editmenu)
janela1.config(menu=menujan) #linha necessaria para aprecer o menu na janela de trabalho
largura= 400
altura = 400
centro=centralizacao(janela1,largura, altura, posx, posy)

janela1.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
janela1.mainloop()
janela.mainloop()
