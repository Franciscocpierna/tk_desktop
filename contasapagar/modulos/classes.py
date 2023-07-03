from tkinter import *


class montatela():
      def __init__(self, manutencao1,janela1, opcao,posx,posy,labelcria):
         super().__init__() 
         self.labelcria=labelcria
         self.opcao = opcao
         self.posx = posx
         self.posy = posy
         
         if self.opcao==1:
              manutencao1.title("Inclusão")
              Label(manutencao1, text= 'Manutenção - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30)
              
         elif self.opcao == 2:
             manutencao1.title("Consulta")
             Label(manutencao1, text= 'Manutenção - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30)
         elif self.opcao == 3:
              manutencao1.title("Ateração")    
              Label(manutencao1, text= 'Manutenção - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30) 
         else:
              manutencao1.title("Exclusão")
              Label(manutencao1, text= 'Manutenção - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 410, pady=30)
          #janela1.configure(height= 400)
          #janela1.configure(width= 400) 
                  
         manutencao1.resizable(False, False) # tamanho fixo             
         manutencao1.transient(janela1) # de onde vem a janela1
         manutencao1.focus_force() #forçar foco
         manutencao1.grab_set()    # impede que click na janela principal sem fechar janela atual
         #janela1.configure(background='red')
         #janela1.overrideredirect(True)  
         centralizatela = centralizacao(manutencao1,1200,650,self.posx,self.posy)
         manutencao1.geometry("%dx%d+%d+%d" % (1200, 650, centralizatela.posx, centralizatela.posy-20))
         #posx-200 ajuste de tela
         for key, value in labelcria.items():
             Label(manutencao1, text=value+":").grid(row=(key+1), column=0)
            # text_usuario + str(key)= Entry(manutencao1).grid(row=(key+1), column=1)
             Entry(manutencao1).grid(row=(key+1), column=1)


         # itens da tetla
         '''Label(manutencao, text='Usuario:').grid(row=0, sticky=W)
          Label(manutencao, text='Senha:').grid(row=1, sticky=W)
          text_usuario= Entry(manutencao).grid(row=0, column=1)
          text_senha = Entry(manutencao).grid(row=1,column=1)
          login = Button(janela, text='login').grid(row=2, column=1,sticky=E)
          print(f'a opcao inclusao aqui é {opcao}')
         '''
class  centralizacao():
   def __init__(self,manutencao,largura1, altura1,posx,posy):
      #super().__init__() 
      self.largura1=largura1
      self.altura1=altura1
      self.posx = posx
      self.posy = posy
      #RESOLUÇÃO DO NOSSO SISTEMA
      largura_screen = manutencao.winfo_screenwidth()
      altura_screen = manutencao.winfo_screenheight()
       # print(largura_screen, altura_screen)
      self.posx=largura_screen/2 - self.largura1/2
      self.posy= altura_screen/2 - self.altura1/2 
      #janela1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
      print(f'a posy = {posy} e a posx = {posx}')
    