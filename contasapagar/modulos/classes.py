from tkinter import *
from modulos import *

class montatela():
      def __init__(self, manutencao,janela1, opcao,posx,posy):
         super().__init__() 
         self.posx=0
         self.posy=0
         
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
         centralizatela = centralizacao(manutencao,1200,650)
         manutencao.geometry("%dx%d+%d+%d" % (1200, 650, posx-400, posy-150))#posx-200 ajuste de tela
         # itens da tetla
         '''Label(manutencao, text='Usuario:').grid(row=0, sticky=W)
          Label(manutencao, text='Senha:').grid(row=1, sticky=W)
          text_usuario= Entry(manutencao).grid(row=0, column=1)
          text_senha = Entry(manutencao).grid(row=1,column=1)
          login = Button(janela, text='login').grid(row=2, column=1,sticky=E)
          print(f'a opcao inclusao aqui é {opcao}')
         '''
   
  class  centralizacao(janinclusao,largura1, altura1):
   #RESOLUÇÃO DO NOSSO SISTEMA
   largura_screen = janinclusao.winfo_screenwidth()
   altura_screen = janinclusao.winfo_screenheight()
   # print(largura_screen, altura_screen)
   posx=largura_screen/2 - largura1/2
   posy= altura_screen/2 - altura1/2 
   #janela1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
   print(f'a posy = {posy} e a posx = {posx}')
    