from tkinter import *


class montatela():
      def __init__(self, manutencao1,janela1, opcao,posx,posy):
         super().__init__() 
         self.opcao = opcao
         self.posx = posx
         self.posy = posy
         
              
         if self.opcao==1:
              manutencao1.title("Inclusão")
              Label(manutencao1, text= 'Manutenção - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 220, pady=30)
              
         elif self.opcao == 2:
             manutencao1.title("Consulta")
             Label(manutencao1, text= 'Manutenção - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 220, pady=30)
         elif self.opcao == 3:
              manutencao1.title("Ateração")    
              Label(manutencao1, text= 'Manutenção - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 220, pady=30) 
         else:
              manutencao1.title("Exclusão")
              Label(manutencao1, text= 'Manutenção - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 220, pady=30)
          #janela1.configure(height= 400)
          #janela1.configure(width= 400) 
                  
         manutencao1.resizable(False, False) # tamanho fixo             
         manutencao1.transient(janela1) # de onde vem a janela1
         manutencao1.focus_force() #forçar foco
         manutencao1.grab_set()    # impede que click na janela principal sem fechar 
         centralizatela = centralizacao(manutencao1,1200,650,self.posx,self.posy)
         manutencao1.geometry("%dx%d+%d+%d" % (1200, 650, centralizatela.posx, centralizatela.posy-20))
         #posx-200 ajuste de tela
         

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
    


      '''  for key, value in self.labelcria.items():
              # globals()['strg%s' % n] = 'Hello'
              globals()[value] = 'Hello'
              print(f'{value} é igual = {codigo}')
              #exec("%s = " % (value,""))
              self.codigo="helo"
        '''       
   #exec("%s = %d" % (name,100))