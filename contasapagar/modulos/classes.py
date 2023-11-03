from tkinter import *

class variaveis():
     def __init__(self,indice,opcao,opcao1,manutencao):
       self.indice=indice
       self.opcao=opcao
       self.opcao1=opcao1
       self.manutencao=manutencao

     def getmanutencao(self):
         return self.manutencao
     def setmanutencao(self,manut):
         self.manutencao=manut
         return
     def getopcao(self):
         return self.opcao
     
     def setopcao(self,optar):
         self.opcao=optar
         return
     def getopcao1(self):
         return self.opcao1
     
     def setopcao1(self,optar):
         self.opcao1=optar
         return 

     def getvalor(self):
          return self.indice
     def setvalor(self,indice2):
          self.indice=indice2+1

class variaveis1(variaveis):
     def __init__(self,escolhido,escolhido1):
         self.escolhido=escolhido
         self.escolhido1=escolhido1
     def getescolhido(self):
         return self.escolhido       
     def setescolhido(self,escolha):
         self.escolhido = escolha
     def getescolhido1(self):
         return self.escolhido       
     def setescolhido1(self,escolha):
         self.escolhido1 = escolha           


class montatela():
      def __init__(self, manutencao1,janela1, opcao,posx,posy,largura, altura,opcao1):
         super().__init__() 
         self.opcao = opcao
         self.posx = posx
         self.posy = posy
         self.opcao1=opcao1
         self.largura = largura
         self.altura = altura
         
         #manutenção Inclusão
         
         #   
         if self.opcao==1 and self.opcao1 == 1: 
              manutencao1.title("Inclusão-Fornecedor - Esc para sair")
              Label(manutencao1, text= 'Fornecedor - Inclusão',font=('Arial', 20) ,fg="black").grid(row=0,column=2,padx=90,pady=30,sticky=W)
              #.grid(column=2,row=0,padx= 90, pady=30,sticky=W)
         elif self.opcao==1 and self.opcao1 == 2: 
             manutencao1.title("Inclusão-Contas- Esc para sair")
             Label(manutencao1, text= 'Contas - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)
         elif self.opcao==1 and self.opcao1 == 3: 
             manutencao1.title("Inclusão-Tipo- Esc para sair")
             Label(manutencao1, text= 'Tipo - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)
         elif self.opcao==1 and self.opcao1 == 4: 
             manutencao1.title("Inclusão-Produto- Esc para sair")
             Label(manutencao1, text= 'Produto - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)    
        

           #fim manutenção inclusão
           # 
           # 
          #manutenção Consulta
         elif self.opcao == 2 and self.opcao1 == 1: 
             manutencao1.title("Consulta-Fornecedor- Esc para sair")
             Label(manutencao1, text= 'Fornecedor - Consulta',font=('Arial', 20) ,fg="black").grid(column=2,row=0,padx= 90, pady=30,sticky=W)
         elif self.opcao == 2 and self.opcao1 == 2: 
             manutencao1.title("Consulta-Contas")
             Label(manutencao1, text= 'Contas - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)
         elif self.opcao == 2 and self.opcao1 == 3: 
             manutencao1.title("Consulta-Tipo")
             Label(manutencao1, text= 'Tipo - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)       
         elif self.opcao==2 and self.opcao1 == 4: 
             manutencao1.title("Consulta-Produto")
             Label(manutencao1, text= 'Produto - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)     

          # fim manutençao consulta

          # manutenção Alteração

         elif self.opcao == 3 and self.opcao1 == 1:
              manutencao1.title("Ateração-Fornecedor - Esc para sair")    
              Label(manutencao1, text= 'Fornecedor - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)
         elif self.opcao == 3 and self.opcao1 == 2:
              manutencao1.title("Ateração-Contas- Esc para sair")    
              Label(manutencao1, text= 'Contas - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)
         elif self.opcao == 3 and self.opcao1 == 3:
              manutencao1.title("Ateração-Tipo- Esc para sair")    
              Label(manutencao1, text= 'Tipo - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30) 
         elif self.opcao==3 and self.opcao1 == 4: 
             manutencao1.title("Alteração-Produto")
             Label(manutencao1, text= 'Produto - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)             
           
           #fim manutenção Alteração
           
           #manutenção Exclusão

         elif self.opcao == 4 and self.opcao1 == 1: 
              manutencao1.title("Exclusão-Fornecedor- Esc para sair")
              Label(manutencao1, text= 'Fornecedor - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)
         elif self.opcao == 4 and self.opcao1 == 2: 
              manutencao1.title("Exclusão-Contas- Esc para sair")
              Label(manutencao1, text= 'Contas - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)
         elif self.opcao == 4 and self.opcao1 == 3: 
              manutencao1.title("Exclusão-Tipo- Esc para sair")
              Label(manutencao1, text= 'Tipo - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)     
         elif self.opcao==4 and self.opcao1 == 4: 
             manutencao1.title("Exclusão-Produto")
             Label(manutencao1, text= 'Produto - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)  


             #fim manutenção exclusão
             # 
             #  
          #janela1.configure(height= 400)
          #janela1.configure(width= 400) 
                  
         manutencao1.resizable(False, False) # tamanho fixo             
         manutencao1.transient(janela1) # de onde vem a janela1
         manutencao1.focus_force() #forçar foco
         manutencao1.grab_set()    # impede que click na janela principal sem fechar
         centralizatela = centralizacao(manutencao1,self.largura,self.altura,self.posx,self.posy)

         if self.opcao1 == 1: 
               Label(manutencao1, text="Codigo:", font=('Arial', 15)).grid(row=1, column=0,sticky=W)
               self.codigo = Entry(manutencao1,width=7)
               self.codigo.grid(row=1, column=1, sticky=W)
               Label(manutencao1, text="Nome:",font=('Arial', 15)).grid(row=2, column=0,sticky=W)
               self.nome = Entry(manutencao1,width=50)
               self.nome.grid(row=2, column=1,sticky=W)
               Label(manutencao1, text="Endereço:",font=('Arial', 15)).grid(row=3, column=0,sticky=W)
               self.endereco= Entry(manutencao1,width=50)
               self.endereco.grid(row=3, column=1,sticky=W)
               Label(manutencao1, text="Telefone:",font=('Arial', 15)).grid(row=4, column=0,sticky=W)
               self.telefone= Entry(manutencao1,width=15)
               self.telefone.grid(row=4, column=1,sticky=W)
               Label(manutencao1, text="Tipo (F)isica (J)uridica:",font=('Arial', 15)).grid(row=5, column=0,sticky=W)
               self.tipo = Entry(manutencao1,width=3)
               self.tipo.grid(row=5, column=1,sticky=W)
               Label(manutencao1, text="Cpf:",font=('Arial', 15)).grid(row=6, column=0,sticky=W)
               self.cpf = Entry(manutencao1,width=16)
               self.cpf.grid(row=6, column=1,sticky=W)
               Label(manutencao1, text="Cnpj:",font=('Arial', 15)).grid(row=7, column=0,sticky=W)
               self.cnpj = Entry(manutencao1,width=17)
               self.cnpj.grid(row=7, column=1,sticky=W)
               Label(manutencao1, text="Cep:",font=('Arial', 15)).grid(row=8, column=0,sticky=W)
               self.cep = Entry(manutencao1,width=17)
               self.cep.grid(row=8, column=1,sticky=W)
               Label(manutencao1, text="E-mail:",font=('Arial', 15)).grid(row=9, column=0,sticky=W)
               self.e_mail = Entry(manutencao1,width=17)
               self.e_mail.grid(row=9, column=1,sticky=W)
                                            

               
        #NW , N , NE , W , E , SW , S e SE       
         if self.opcao1 == 2:
               Label(manutencao1, text="Fornecedor:", font=('Arial', 15)).grid(row=1, column=0,sticky=W)
               self.codigo = Entry(manutencao1,width=7)
               self.codigo.grid(row=1, column=1, sticky=W)
               Label(manutencao1, text="Nome:",font=('Arial', 15)).place(relx=0.3,rely=0.1)#grid(row=1, column=2,sticky=W)
               self.nome = Entry(manutencao1,width=50) #place(relx=0.5,rely=0.4)
               self.nome.place(relx=0.35,rely=0.11)#grid(row=1, column=3,sticky=E)
               Label(manutencao1, text="Número do documento:",font=('Arial', 15)).grid(row=2, column=0,sticky=W)
               self.documento = Entry(manutencao1,width=20)
               self.documento.grid(row=2, column=1,sticky=W)
               Label(manutencao1, text="Parcelado:",font=('Arial', 15)).grid(row=3, column=0,sticky=W)
               self.tparcela = Entry(manutencao1,width=3)
               self.tparcela.grid(row=3, column=1,sticky=W)
               Label(manutencao1, text="Data Compra:",font=('Arial', 15)).grid(row=4, column=0,sticky=W)
               self.compra= Entry(manutencao1,width=10)
               self.compra.grid(row=4,column=1,sticky=W)
               Label(manutencao1, text="Data Vencimento:",font=('Arial', 15)).grid(row=5, column=0,sticky=W)
               self.vencimento= Entry(manutencao1,width=10)
               self.vencimento.grid(row=5, column=1,sticky=W)
               Label(manutencao1, text="Descrição:",font=('Arial', 15)).grid(row=6, column=0,sticky=W)
               self.descricao= Entry(manutencao1,width=50)
               self.descricao.grid(row=6, column=1,sticky=W)
               Label(manutencao1, text="Data Pagamento:",font=('Arial', 15)).grid(row=7, column=0,sticky=W)
               self.pagamento= Entry(manutencao1,width=10)
               self.pagamento.grid(row=7, column=1,sticky=W)
               Label(manutencao1, text="Forma de Pagamento:",font=('Arial', 15)).grid(row=8, column=0,sticky=W)
               self.tipo= Entry(manutencao1,width=10)
               self.tipo.grid(row=8, column=1,sticky=W)
               Label(manutencao1, text="Descrição:",font=('Arial', 15)).place(relx=0.3,rely=0.415)
               self.desctipo = Entry(manutencao1,width=50)
               self.desctipo.place(relx=0.38,rely=0.422)
               Label(manutencao1, text="Desconto R$:",font=('Arial', 15)).grid(row=9, column=0,sticky=W)
               self.desconto= Entry(manutencao1,width=14)
               self.desconto.grid(row=9, column=1,sticky=W)
               Label(manutencao1, text="Juros R$:",font=('Arial', 15)).grid(row=10, column=0,sticky=W)
               self.juros = Entry(manutencao1,width=15)
               self.juros.grid(row=10, column=1,sticky=W)
               Label(manutencao1, text="Valor a Pagar R$:",font=('Arial', 15)).grid(row=11, column=0,sticky=W)
               self.valpagar = Entry(manutencao1,width=14)
               self.valpagar.grid(row=11, column=1,sticky=W)
               Label(manutencao1, text="(C)ompra ou (S)erviço:",font=('Arial', 15)).grid(row=12, column=0,sticky=W)
               self.cs = Entry(manutencao1,width=2)
               self.cs.grid(row=12, column=1,sticky=W)
               Label(manutencao1, text="Cod Produto:",font=('Arial', 15)).grid(row=13, column=0,sticky=W)
               self.produto = Entry(manutencao1,width=7)
               self.produto.grid(row=13, column=1,sticky=W)
               Label(manutencao1, text="Nome Produto:",font=('Arial', 15)).place(relx=0.25,rely=0.64)#grid(row=1, column=2,sticky=W)
               self.descproduto = Entry(manutencao1,width=50) #place(relx=0.5,rely=0.4)
               self.descproduto.place(relx=0.365,rely=0.65)#grid(row=1, column=3,sticky=E)

         if self.opcao1==3:
               Label(manutencao1, text="Codigo:", font=('Arial', 15)).grid(row=1, column=0,sticky=W)
               self.codigo = Entry(manutencao1,width=7)
               self.codigo.grid(row=1, column=1, sticky=W)
               Label(manutencao1, text="Nome:",font=('Arial', 15)).grid(row=2, column=0,sticky=W)
               self.nome = Entry(manutencao1,width=50)
               self.nome.grid(row=2, column=1,sticky=W) 
         if self.opcao1 == 4:
               Label(manutencao1, text="Codigo:", font=('Arial', 15)).grid(row=1, column=0,sticky=W)
               self.codigo = Entry(manutencao1,width=7)
               self.codigo.grid(row=1, column=1, sticky=W)
               Label(manutencao1, text="Nome:",font=('Arial', 15)).grid(row=2, column=0,sticky=W)
               self.nome = Entry(manutencao1,width=50)
               self.nome.grid(row=2, column=1,sticky=W)
         
         manutencao1.geometry("%dx%d+%d+%d" % (self.largura, self.altura, centralizatela.posx,centralizatela.posy-20))
     
             

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
      
          


      