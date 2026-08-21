from tkinter import *
from tkinter import ttk

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

    # def getvalor(self):
    #      return self.indice
    #def setvalor(self,indice2):
    #self.indice=indice2+1

class variaveis1(variaveis):
     def __init__(self,escolhido,escolhido1):
         self.escolhido=escolhido
         self.escolhido1=escolhido1
     def getescolhido(self):
         return self.escolhido       
     def setescolhido(self,escolha):
         self.escolhido = escolha
     def getescolhido1(self):
         return self.escolhido1       
     def setescolhido1(self,escolha):
         self.escolhido1 = escolha           

class variaveis2(variaveis1):
     def __init__(self,escolha,escolha1):
         self.escolha=escolha
         self.escolha1=escolha1 
     def setescolha(self,escolha):
         self.escolha = escolha       
     def getescolha(self):
         return self.escolha
     def setescolha1(self,escolha1):
         self.escolha1 = escolha1       
     def getescolha1(self):
         return self.escolha1
      

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
         elif self.opcao==1 and self.opcao1 == 5:
              manutencao1.title("Inclusão-Cliente")
              Label(manutencao1, text= 'Cliente - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)
         elif self.opcao==1 and self.opcao1 == 6:
              manutencao1.title("Inclusão - Receber")
              Label(manutencao1, text= 'Receber - Inclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)     
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
         elif self.opcao==2 and self.opcao1 == 5: 
             manutencao1.title("Consulta-Cliente")
             Label(manutencao1, text= 'Cliente - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30) 
         elif self.opcao==2 and self.opcao1 == 6:
              manutencao1.title("Consulta - Receber")
              Label(manutencao1, text= 'Receber - Consulta',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)    
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
         elif self.opcao==3 and self.opcao1 == 5: 
             manutencao1.title("Alteração-Cliente")
             Label(manutencao1, text= 'Cliente - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)             
         elif self.opcao==3 and self.opcao1 == 6:
              manutencao1.title("Alteração - Receber")
              Label(manutencao1, text= 'Receber - Alteração',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)   
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
         elif self.opcao==4 and self.opcao1 == 5: 
             manutencao1.title("Exclusão-Cliente")
             Label(manutencao1, text= 'Cliente - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 90, pady=30)      

         elif self.opcao==4 and self.opcao1 == 6:
              manutencao1.title("Exclusão - Receber")
              Label(manutencao1, text= 'Receber - Exclusão',font=('Arial', 20) ,fg="black",).grid(column=2,row=0,padx= 15, pady=15)
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

         if self.opcao1 == 1 or opcao1==5: 
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
               self.codigo = Entry(manutencao1, width=7)
               self.codigo.grid(row=1, column=1, sticky=W,padx=(0,5))
               ########### tinha place mudou para frame
               # 2. Criamos um Frame para o grupo "Nome" e o colocamos na coluna 2 da tela principal
               frame_nome = Frame(manutencao1)
               frame_nome.grid(row=1, column=2, sticky=W)
               # 3. Dentro desse Frame, usamos o .grid() para colocar o Label "Nome" e o self.nome bem pertinho
               Label(frame_nome, text="Nome:", font=('Arial', 15)).grid(row=0, column=0, sticky=W, padx=(0, 5))
               self.nome = Entry(frame_nome, width=50)
               self.nome.grid(row=0, column=1, sticky=W) 
    
               ###########

           
               
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
               ###########
               # 2. Criamos um Frame para o grupo "frame_nomedesc" e o colocamos na coluna 2 da tela principal
               frame_nomedesc = Frame(manutencao1)
               frame_nomedesc.grid(row=8, column=2, sticky=W)
               # 3. Dentro desse Frame, usamos o .grid() para colocar o Label "Nome" e o self.nome bem pertinho
               Label(frame_nomedesc, text="Descrição:", font=('Arial', 15)).grid(row=0, column=0, sticky=W, padx=(0, 5))
               self.desctipo = Entry(frame_nomedesc, width=50)
               self.desctipo.grid(row=0, column=1, sticky=W) 
               ############

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
               ###########
               # 2. Criamos um Frame para o grupo "nomeprod" e o colocamos na coluna 2 da tela principal
               frame_nomeprod = Frame(manutencao1)
               frame_nomeprod.grid(row=13, column=2, sticky=W)
               # 3. Dentro desse Frame, usamos o .grid() para colocar o Label "Nome" e o self.nome bem pertinho
               Label(frame_nomeprod, text="Nome Produto:", font=('Arial', 15)).grid(row=0, column=0, sticky=W, padx=(0, 5))
               self.descproduto = Entry(frame_nomeprod, width=50)
               self.descproduto.grid(row=0, column=1, sticky=W) 
               ############
               Label(manutencao1, text="Data Inclusão",font=('Arial', 15)).grid(row=14, column=0,sticky=W)
               self.inclusao = Entry(manutencao1,width=10)
               self.inclusao.grid(row=14, column=1,sticky=W)     

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
         if self.opcao1==6: #contas a receber
               Label(manutencao1, text="Cliente:", font=('Arial', 15)).grid(row=1, column=0,sticky=W)
               self.codigo = Entry(manutencao1,width=7)
               self.codigo.grid(row=1, column=1, sticky=W)

                ########### tinha place mudou para frame
               # 2. Criamos um Frame para o grupo "frame_Nome1" e o colocamos na coluna 2 da tela principal
               frame_nome1 = Frame(manutencao1)
               frame_nome1.grid(row=1, column=2, sticky=W)
               # 3. Dentro desse Frame, usamos o .grid() para colocar o Label "Nome" e o self.nome bem pertinho
               Label(frame_nome1, text="Nome:", font=('Arial', 15)).grid(row=0, column=0, sticky=W, padx=(0, 5))
               self.nome = Entry(frame_nome1, width=50)
               self.nome.grid(row=0, column=1, sticky=W)
               ########### 
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
               Label(manutencao1, text="Valor a Pagar R$:",font=('Arial', 15)).grid(row=8, column=0,sticky=W)
               self.valpagar = Entry(manutencao1,width=14)
               self.valpagar.grid(row=8, column=1,sticky=W)

               Label(manutencao1, text="Data Inclusão",font=('Arial', 15)).grid(row=9, column=0,sticky=W)
               self.inclusao = Entry(manutencao1,width=10)
               self.inclusao.grid(row=9, column=1,sticky=W)          
         
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
      
# 1. Defina essa classe antes de criar a sua treeview (pode colocar logo no início do arquivo) no caso importei
# Cria uma classe nova que "herda" todas as funções da Treeview padrão do ttk.
class AcceleratedTreeview(ttk.Treeview):
    
    # Sobrescreve o método de rolagem horizontal (xview) da tabela.
    def xview(self, *args):
        
        # Verifica se o comando enviado é do tipo 'scroll' (gerado por setas ou pelas pontas da barra).
        if args and args[0] == 'scroll':
            try:
                # Define o fator multiplicador para deixar o movimento mais rápido (30x).
                multiplier = 30  
                
                # Modifica o argumento numérico da velocidade multiplicando ele por 30,
                # mantendo a estrutura original que o Tkinter espera receber.
                new_args = args[:1] + (str(multiplier * int(args[1])),) + args[2:]
                
                # Envia os argumentos modificados para a classe original fazer a rolagem rápida.
                return super().xview(*new_args)
                
            # Caso ocorra algum erro na conversão dos argumentos, apenas ignora.
            except (ValueError, IndexError):
                pass
                
        # Se não for um comando de 'scroll' (por exemplo, arrastar a barra com o mouse),
        # executa o comportamento padrão normal da tabela.
        return super().xview(*args)

from datetime import datetime
from tkinter import messagebox


class ValidaData:

  def __init__(self, entry_widget):
    """Recebe o widget Entry do Tkinter onde o usuário digita a data."""
    self.entry_widget = entry_widget

  def verificar_data_digitada(self):
    """Verifica se o texto no Entry é uma data válida no formato DD/MM/AAAA."""
    texto_data = self.entry_widget.get().strip()

    try:
      # Valida se é uma data real (ex: rejeita 31/02/2026)
      data_obj = datetime.strptime(texto_data, "%d/%m/%Y")
      messagebox.showinfo(
          "Sucesso", f"Data válida: {data_obj.strftime('%d/%m/%Y')}"
      )
      return True
    except ValueError:
      messagebox.showerror(
          "Erro", "A data digitada não é válida ou está incompleta!"
      )
      self.entry_widget.focus()
      return False

# como usar essa classe        

# # Importa a classe do arquivo validadata.py
#from classes import ValidaData  
#         # 1. Instancia a classe passando o entry
# validador = ValidaData(meu_entry)

# # 2. Chama o método de verificação e guarda o resultado em uma variável
# # (Lembre-se que ajustamos o método para retornar o objeto data_obj se for válido, ou None se falhar)
# resultado_data = validador.verificar_data_digitada()

# # 3. Agora sim, faça a verificação com if:
# if resultado_data:
#   print("A data é válida! Posso prosseguir com o salvamento.")
#   # Exemplo: formatar para salvar no banco (AAAA-MM-DD)
#   data_para_banco = resultado_data.strftime("%Y-%m-%d")
# else:
#   print("A data é inválida ou está vazia. O foco já voltou para o campo.")


