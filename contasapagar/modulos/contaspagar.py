from tkinter import *
from tkinter import messagebox
#import rotinas
#import sqlite3
#from sqlite3 import Error
#from time import sleep
#from classes import montatela,centralizacao
#import keyboard
from fornecedor import *
from contas import *
from tipo import *



largura=0
altura=0
posx=0
posy=0
X=0
ler=""
opcao=0

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
filemenu.add_command(label = " Fornecedor",command= lambda: fornecedor_menu(janela1))
filemenu.add_command(label = " Contas",command= lambda: contas_menu(janela1))
filemenu.add_command(label = " Tipo",command=lambda: tipo_menu(janela1))
menujan.add_cascade(label='Manutenção Geral',menu = filemenu)

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
