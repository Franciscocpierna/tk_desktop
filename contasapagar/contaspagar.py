from tkinter import *
from modulos.classes import * #montatela
#from modulos.centralizatela import centralizacao


#import awesometkinter as atk
largura=0
altura=0
posx=0
posy=0
X=0
opcao=0

'''def montatela(opcao):
   manutencao = Toplevel() # janela de nível superior
   if opcao==1:
      manutencao.title("Inclusão")
      Label(manutencao, text= 'Manutenção - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30)
      
   elif opcao == 2:
      manutencao.title("Consulta")
      Label(manutencao, text= 'Manutenção - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30)
   elif opcao == 3:
      manutencao.title("Ateração")    
      Label(manutencao, text= 'Manutenção - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30) 
   else:
       manutencao.title("Exclusão")
       Label(manutencao, text= 'Manutenção - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30)
   #janela1.configure(height= 400)
   #janela1.configure(width= 400) 
           
   manutencao.resizable(False, False) # tamanho fixo             
   manutencao.transient(janela1) # de onde vem a janela1
   manutencao.focus_force() #forçar foco
   manutencao.grab_set()    # impede que click na janela principal sem fechar janela atual
   #janela1.configure(background='red')
   #janela1.overrideredirect(True)  
   centralizacao(manutencao,1200,650)
   manutencao.geometry("%dx%d+%d+%d" % (1200, 650, posx-400, posy-150))#posx-200 ajuste de tela
   # itens da tetla
   Label(manutencao, text='Usuario:').grid(row=0, sticky=W)
   Label(manutencao, text='Senha:').grid(row=1, sticky=W)
   text_usuario= Entry(manutencao).grid(row=0, column=1)
   text_senha = Entry(manutencao).grid(row=1,column=1)
   login = Button(janela, text='login').grid(row=2, column=1,sticky=E)
   print(f'a opcao inclusao aqui é {opcao}')


   return manutencao
'''

def incluir_click():
     opcao=1
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     '''Label(manutencao, text='Usuario:').grid(row=0, sticky=W)
     Label(manutencao, text='Senha:').grid(row=1, sticky=W)
     text_usuario= Entry(manutencao).grid(row=0, column=1)
     text_senha = Entry(manutencao).grid(row=1,column=1)
     login = Button(janela, text='login').grid(row=2, column=1,sticky=E)
     '''
def cosulta_click():
     opcao=2
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     print(f'a opcao consulta aqui é tela.opcao = {tela.opcao}')
def alteracao_clik():
     opcao=3
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
     print(f'a opcao alteraçao aqui é {opcao}')
def excluir_click(): 
     opcao=4
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy)
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


#centraliza(janela1,400,400)
largura= 400
altura = 400
#RESOLUÇÃO DO NOSSO SISTEMA
largura_screen = janela1.winfo_screenwidth()
altura_screen = janela1.winfo_screenheight()
# print(largura_screen, altura_screen)
posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2
print(f'a janela1 posy = {posy} e a posx = {posx}') 
janela1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
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