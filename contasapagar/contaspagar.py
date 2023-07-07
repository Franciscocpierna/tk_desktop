from tkinter import *
from modulos.classes import * #montatela
#from modulos.centralizatela import centralizacao


#import awesometkinter as atk
largura=0
altura=0
posx=0
posy=0
X=0
ler=""
opcao=0
tela=""
'''codigo="inicio"
nome=""
endereco=""
telefone=""
tipo=""
cpf=""
cnpj=""
'''
'''def tela1(manutencao):
    Label(manutencao, text="Codigo:").grid(row=1, column=0)
    codigo = Entry(manutencao,width=40).grid(row=1, column=1)
    Label(manutencao, text="Nome:").grid(row=2, column=0)
    nome = Entry(manutencao,width=40).grid(row=2, column=1)
    Label(manutencao, text="Endereço:").grid(row=3, column=0)
    endereco= Entry(manutencao,width=40).grid(row=3, column=1)
    Label(manutencao, text="Telefone:").grid(row=4, column=0)
    telefone= Entry(manutencao,width=40).grid(row=4, column=1)
    Label(manutencao, text="Tipo:").grid(row=5, column=0)
    tipo = Entry(manutencao,width=40).grid(row=5, column=1)
    Label(manutencao, text="Cpf:").grid(row=6, column=0)
    cpf = Entry(manutencao,width=40).grid(row=6, column=1)
    Label(manutencao, text="Cnpj:").grid(row=7, column=0)
    cnpj = Entry(manutencao,width=40).grid(row=7, column=1)
    ler=codigo.get()
    return '''     
def verconteudo():
     print (f'self.codigo.get = {tela.codigo.get()}') #{tela.codigo.get()}')
     
def incluir_click():
     opcao=1
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     print (f'tela.codigo.get = {tela.codigo.get()}')

     #tela1(manutencao) 
     
     botao=Button(manutencao, text='contem', command = verconteudo)
     botao.grid(row=20, column=1,sticky=N)
     
def cosulta_click():
     opcao=2
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     #tela1(manutencao) 
      
     print(f'a opcao consulta aqui é tela.opcao = {tela.opcao}')
def alteracao_clik():
     opcao=3
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     #tela1(manutencao) 
     print(f'a opcao alteraçao aqui é {opcao}')
def excluir_click(): 
     opcao=4
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     #tela1(manutencao) 
     print(f'a opcao Exclusao aqui é {opcao}')

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



'''import Tkinter
root = Tkinter.Tk()
root.configure(background='black') 
root.mainloop()
super().__init__()
      self['height'] =150
      self['width'] = 200
      self['bd'] = 2
      self['relief']= SOLID

      label_nome = Label(self,text=texto)
      text_nome = Entry(self)
      label_nome.grid(row=0,column=0)
      text_nome.grid(row=0, column=1)'''