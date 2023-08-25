from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from rotinas import *
import sqlite3
from sqlite3 import Error
from time import sleep
from classes import montatela,centralizacao
import keyboard
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import win32print
import win32api
import os
import datetime 
import shutil


largura=1200
altura=650

posx=0
posy=0
X=0
ler=""
opcao=0

# Relatórios

def abrirpdf1(arquivo1):
 try:
  caminho = r"C:\python_projetos\3.11.2\tk_desktop\arquivo"
  #lista_arquivos = os.listdir(caminho)

  #print(lista_arquivos[0])
 # https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
 
  win32api.ShellExecute(0, "open", arquivo1,None, caminho, 0) 
  
 except Error as ex:
  messagebox1("Erro ao tentar Abrir linha 41 "+str(ex),janela4)
  return

 return

def imprimepdf1(arquivo1):
  try: 
   lista_impressoras = win32print.EnumPrinters(2)
   impressora = lista_impressoras[2]
   win32print.SetDefaultPrinter(impressora[2])
   # mandar imprimir todos os arquivos de uma pasta
   caminho = r"C:\python_projetos\3.11.2\tk_desktop\arquivo"
   #lista_arquivos = os.listdir(caminho)
   # https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
   #if arquivo in lista_arquivos:
   win32api.ShellExecute(0, "print", arquivo1, None, caminho, 0)       
   return
  except  Error as ex:
    messagebox1("Erro ao tentar imprimir linha 58 "+str(ex),janela4)
    return


def pdfgerado1(sqlres,arquivo):
   data = datetime.date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
  
   try: 
    cnv = canvas.Canvas(rf"C:\python_projetos\3.11.2\tk_desktop\arquivo\{arquivo}", pagesize=A4)
   except Error as ex:
    messagebox1(str(ex)+ " linha 62",janela4)
    return
   cnv.setFont('Helvetica', 9)  
   #cnv.drawString(10,830, "teste") # canto superior A4
   if arquivo=="rel_nome.pdf":
    cnv.drawString(250,830, "Relatório por Nomes") # centro do pdf linha superior
   elif  arquivo=="rel_codigo.pdf":
    cnv.drawString(250,830, "Relatório por Código")   
   

   cnv.drawString(500,830, str(dia)+"/"+str(mes)+"/"+str(ano))
   eixo = 20
   y= 810
   z=1
   x=0

   for (c,n) in sqlres:
        x+=1
        y -= 20
        cnv.drawString(10,y,"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        y-= 20
        cnv.drawString(10,y, "codigo: "+ str(c)+ " Nome: "+ n)
        
        if z == 8: 
         if x  < len(sqlres): 
          z = 0 
          y=810
          cnv.showPage()
          cnv.setFont('Helvetica', 9)
          #
          if arquivo=="rel_nome.pdf":
            cnv.drawString(250,830, "Relatório por Nomes") # centro do pdf linha superior
          elif  arquivo=="rel_codigo.pdf":
            cnv.drawString(250,830, "Relatório por Código")   
        
        
          #    
          cnv.drawString(500,830, str(dia)+"/"+str(mes)+"/"+str(ano))
        z+=1  
            
   cnv.save()
   return

def gerapf1(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
          cursor.execute(f"SELECT *  FROM  tipo ORDER BY codigo ASC")
        else:
          cursor.execute(f"SELECT *  FROM  tipo ORDER BY codigo DESC")

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return             
        else:
           pdfgerado1(sqlres,"rel_codigo.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf1("rel_codigo.pdf")
              cursor.close()              
           else:        
              abrirpdf1("rel_codigo.pdf")
              cursor.close
           return
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 147 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 151 "+str(ex),janela4)
        cursor.close()
        return

def gerapf(event):
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        
        cursor.execute(f"SELECT *  FROM  tipo ORDER BY nome ASC")

        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return
        else:
           pdfgerado1(sqlres,"rel_nome.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf1("rel_nome.pdf")
              cursor.close()              
           else:        
              abrirpdf1("rel_nome.pdf")
              cursor.close
              return 
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 182 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 186 "+str(ex),janela4)
        cursor.close()

   return
     
def copiapdf(arquivo):
  #quebra o codigo se arquivo estiver aberto
  try:
   caminho = r"C:\python_projetos\3.11.2\tk_desktop\arquivo"
   lista_arquivos = os.listdir(caminho) 
   if arquivo in lista_arquivos:    
      shutil.copy(rf"C:\python_projetos\3.11.2\tk_desktop\arquivo\{arquivo}", rf"C:\python_projetos\3.11.2\tk_desktop\pastausuario\{arquivo}"),
      messagebox1('Arquivo copiado com sucesso',janela4)
   else: 
      messagebox1(f'Arquivo {arquivo} não existe na Pasta gere Arquivo',janela4)    
      return   
  except Error as ex:
    messagebox1('Erro ao copiar arquivo'+str(ex),janela4)
    return
  return   

def rel_nome1(janela3):
   global janela4 
   global escolhido
   global escolha
   escolha=StringVar(value="D")
   janela4 = Toplevel()
   janela4.title("Relatório por Nomes ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem fechar essa
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Nomes geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.25, rely=0.2)  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   #label1=Label(janela4,text="Copiar Arquivo Pdf gerado para para pastausuario tecle - F6" )
   #label1.place(relx=0.2,rely=0.6)
   escolhido=escolha.get()
   #keyboard.on_press_key("f3", lambda _: gerapdf())
   
   janela4.bind("<F3>", gerapf)

   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #keyboard.on_press_key("f6", lambda _: moverpdf("rel_nome.pdf"))



  
   
def rel_codigo1(janela3):
   global janela4 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
   janela4 = Toplevel()
   janela4.title("Relatório por Codigo ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Código geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.25, rely=0.2)
   optado2= Radiobutton(janela4, text="Ascendente", value="A", variable=escolha1,font = ("Arial Bold", 9))
   optado2.place(relx=0.2,rely=0.3)
   optado3= Radiobutton(janela4, text= "Descendente", value="D", variable=escolha1)
   optado3.place(relx=0.5,rely=0.3)
   escolhido1=escolha1.get()  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   escolhido=escolha.get()
   
   #keyboard.on_press_key("f3", lambda _: gerapdf1())
   janela4.bind("<F3>", gerapf1)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")def rel_codigo(janela3):
   

def criartabela1(janela3):

   try:
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     
     cursor.execute('''CREATE TABLE IF NOT EXISTS tipo (codigo INTEGER PRIMARY KEY  NOT NULL, 
                                                        nome varchar(50) NOT NULL)''')
     cursor.close() 
   except Error as ex:
     messagebox1(str(ex)+ " linha 287",janela3)
     return 
   return 


def verificacodigo1():
   
   codigomem=tela.codigo.get()
   try:
       banco = sqlite3.connect('contaspagar.db')
       cursor = banco.cursor()
   except Error as ex:
       messagebox1("Erro na conexão com Banco de dados linha 299 "+str(ex),manutencao)
       limpacampostipo()
       
       return 
   
   try:
       cursor.execute(f"SELECT * FROM tipo WHERE codigo = '{codigomem}'")
       sqlres=cursor.fetchall()
       cursor.close() 
       if len(sqlres) == 0:  
         
        return sqlres
       else:
        
        messagebox1("Informação: Registro já existe não pode ser inserido linha 313",manutencao)
        limpacampostipo()
        tela.codigo.focus()
        return sqlres 
   except Error as ex:
       messagebox1("Erro na leitura da tabela Fornecedor linha 318 "+str(ex),manutencao)
       limpacampostipo()
       
       return 

def consultatipo():
   if len(tela.codigo) != 2:
        messagebox1("Codigo tem que ser tamnho 2", manutencao)
        return
   sqlres=""   
   tela.nome.delete(0,END) 
   
    
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
       codigomem=tela.codigo.get()
       cursor.execute(f"SELECT * FROM tipo WHERE codigo = '{codigomem}'")
       sqlres=cursor.fetchall()
       
       

       if len(sqlres) == 0:
            messagebox1("Registro não existe linha 342",manutencao)

            tela.codigo.delete(0,END)   
            tela.codigo.focus()
            cursor.close()  
            return sqlres
       else:
            tela.nome.insert(0, sqlres[0][1])
            cursor.close()  
            return sqlres
      except Error as ex: 
         messagebox1("Erro ao tentar ler o registro linha 353 "+str(ex),manutencao)
         limpacampostipo()
         cursor.close()  
         return sqlres
              
   except Error as ex:
      messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 359 "+str(ex),manutencao)
      limpacampostipo()
      cursor.close()  
      return sqlres                    
   
    
 
 

def tab_order():
  tela.codigo.focus
  widgets = [tela.codigo,tela.nome]
  for w in widgets:
     w.lift()

def limpacampostipo():
  tela.codigo.delete(0,END)
  tela.nome.delete(0,END) 
  return



def incluirtipo():
      
   sqlres="" 
   if len(tela.codigo) != 2:
        messagebox1("Codigo tem que ser tamnho 2", manutencao)
        return
   
   
   sqlres =  verificacodigo1()
   if len(sqlres) !=0:
      tela.codigo.focus
      return          
   
   if len(tela.nome.get())==0 or len(tela.nome.get())>50:
     
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 50",manutencao)
        tela.nome.focus()
        return
            
  
     
   try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        codigomem=tela.codigo.get()
        nomemem=tela.nome.get()
        
        res = messagebox.askquestion('Confirma Inclusão', 'yes para sim - no para não')
        if res == 'yes':
          try:
           cursor.execute(f'''INSERT INTO tipo VALUES('{codigomem}','{nomemem}')''')
               

                                      
           banco.commit()
           cursor.close()
           messagebox1("registro Incluido com sucesso",manutencao)     
           limpacampostipo()   
           tela.codigo.focus()
          except Error as ex:
            messagebox1("erro ao gravar tabela Fornecedor linha 252 "+ str(ex),manutencao)       
            limpacampostipo()
        else:
           messagebox1("Registro não foi gravado",manutencao)

   except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 427 "+ str(ex),manutencao)
       limpacampostipo()   
       tela.codigo.focus()
       return
   
def incluirtipo_click(janela1):
    opcao=1
    opcao1=3
    
    global tela
    global manutencao  
    manutencao = Toplevel() # janela de nível superior
    tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    botao=Button(manutencao, text='Salvar',command=incluirtipo)
    botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
    tab_order()
    tela.codigo.focus()
    keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
             
    
    
    
           
     
def cosultatipo_click(janela1):
     opcao=2
     opcao1=3
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consultar',command=consultatipo)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     tela.codigo.focus()
     keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
      
def alteracaotipo():
    if len(tela.codigo) != 2:
        messagebox1("Codigo tem que ser tamnho 2", manutencao)
        return
    codigomem=tela.codigo.get() 
    nomemem=tela.nome.get()
    
    sqlres= consultatipo()
    if len(sqlres)==0:
      limpacampostipo()
      tela.codigo.focus()
      return
    if nomemem == "":
       nomemem = tela.nome.get()
    else:
       tela.nome.delete(0, END)
       tela.nome.insert(0, nomemem)

       
    if len(nomemem)==0 or len(nomemem) >50:
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 50",manutencao)
        tela.nome.focus()
        return
        
    res = messagebox.askquestion('Confirma Alteração', 'yes para sim - no para não')
    if res == 'yes':
    
      try:
          banco = sqlite3.connect('contaspagar.db')
          cursor = banco.cursor()
          
      except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 307 "+ str(ex),manutencao)
       limpacampostipo()   
       tela.codigo.focus()
       return
          

      try:
           cursor.execute(f'''UPDATE fornecedor SET codigo = '{codigomem}',
                                                    nome ='{nomemem}',
                                                    WHERE codigo = '{codigomem}' ''')
               

                                      
           banco.commit()
           cursor.close()     
           messagebox1("registro Alterado com sucesso",manutencao)
           limpacampostipo()   
           tela.codigo.focus()
      except Error as ex:
            messagebox("erro ao regravar tabela Fornecedor linha 514"+ str(ex),manutencao)       
            limpacampostipo() 
            return
    else:
           messagebox1("Registro não foi Alterado",manutencao)
           return
    
def alteracaotipo_clik(janela1):
     opcao=3
     opcao1=3
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consutar',command=consultatipo)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Alterar',command=alteracaotipo)
     botao1.grid(row=10, column=1,padx=0,pady=50,sticky=W)
     tab_order()
     tela.codigo.focus()
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
     
      
 
     
      
     
def exclusaotipo():
    if len(tela.codigo) != 2:
        messagebox1("Codigo tem que ser tamnho 2", manutencao)
        return
    codigomem=tela.codigo.get()
    sqlres= consultatipo()
    if len(sqlres)==0:
      limpacampostipo()
      tela.codigo.focus()
      return
    
    res = messagebox.askquestion('Confirma Alteração', 'yes para sim - no para não')
    if res == 'yes':
       try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        
        try:
           cursor.execute(f"DELETE  FROM fornecedor WHERE codigo = '{codigomem}'")
           banco.commit()
           cursor.close()     
           messagebox1("Registro Excluido com sucesso",manutencao)
           limpacampostipo()   
           tela.codigo.focus()
        except Error as ex:
            messagebox1("erro ao Excluir tabela Tipo linha 566"+ str(ex),manutencao)       
            limpacampostipo() 
       except Error as ex:
           messagebox1("erro ao conectar com banco de dados linha 569 "+ str(ex),manutencao)
           limpacampostipo()   
           tela.codigo.focus()
           return
    else:
           messagebox1("Registro não foi Excluido",manutencao)      
    return 
def excluirtipo_click(janela1): 
     opcao=4
     opcao1=3
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consultar',command=consultatipo)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Excluir',command=exclusaotipo)
     botao1.grid(row=10, column=1,padx=0,pady=50,sticky=W)
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
# consultas

def consulta_nome1(janela3):
   janela4 = Toplevel()
   janela4.title("Consultas por Nomes ESC para SAIR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome'), show= 'headings')
    
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
   
   
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
   
  
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.yview)

   tv.configure(yscroll=verscrlbar)
  # tv.configure(xscroll=verscrlbar1.set)
   tv.configure(xscroll=verscrlbar1)
   tv.place(relx=0.01,rely=0.1,relwidth=0.97,relheight=0.75)
   verscrlbar.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.75)
   verscrlbar1.place(relx=0.01,rely=0.85,relwidth=0.95,relheight=0.05)
   
   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        cursor.execute(f"SELECT *  FROM  tipo ORDER BY nome")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n) in sqlres:
               tv.insert("","end",value=(c,n)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 640 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 664 "+str(ex),janela4)
        cursor.close() 
        
 
        


def consultacodigoopcao1(event):
   tv.delete(*tv.get_children())
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f"SELECT *  FROM  tipo ORDER BY codigo ASC")
        else:
          cursor.execute(f"SELECT *  FROM  tipo ORDER BY codigo DESC")

        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n) in sqlres:
               tv.insert("","end",value=(c,n)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 676 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 680 "+str(ex),manutencao)
        cursor.close() 
        

def consulta_codigo1(janela3):
   global janela4 
   global tv 
   global escolhido
   global escolha
   janela4 = Toplevel()
   janela4.title("Consultas por Codigo ESC para SAIR -  F3 - PARA COSULTAR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome'), show= 'headings')
    
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
      
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
     
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.yview)

   tv.configure(yscroll=verscrlbar)
  # tv.configure(xscroll=verscrlbar1.set)
   tv.configure(xscroll=verscrlbar1)
   tv.place(relx=0.01,rely=0.1,relwidth=0.97,relheight=0.75)
   verscrlbar.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.75)
   verscrlbar1.place(relx=0.01,rely=0.85,relwidth=0.95,relheight=0.05)
   escolha=StringVar(value="A")
   optado= Radiobutton(janela4, text="Ascendente", value="A", variable=escolha)
   optado.grid(row=1, column=3)
   optado1= Radiobutton(janela4, text= "Descendente", value="D", variable=escolha)
   optado1.grid(row=1, column=4)
   escolhido=escolha.get()
  # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   janela4.bind("<F3>", consultacodigoopcao1)
   
     
     

     

# relatorios
  

def tipo_menu(janela1):
 pass
 janela3 = Toplevel() # janela de nível superior
 janela3.title("Menu Manutenção - Consultas Relatorios  F1 - PARA SAIR")
#janela1.configure(height= 400)
#janela1.configure(width= 400) 
           
 janela3.resizable(False, False) # tamanho fixo             
 janela3.transient(janela1) # de onde vem a janela
 janela3.focus_force() #forçar foco
 janela3.grab_set()    # impede que click na janela principal sem fechar janela atiual
#janela1.configure(background='red')
#janela1.overrideredirect(True)  

#adicionando menu

 menujan2 = Menu(janela3)
 filemenu= Menu(menujan2, tearoff=0,)


 filemenu.add_command(label = " Inclusão",command= lambda: incluirtipo_click(janela3))
 filemenu.add_command(label = " Consulta",command= lambda: cosultatipo_click(janela3))
 filemenu.add_command(label = " Alteração",command=lambda: alteracaotipo_clik(janela3))
 filemenu.add_command(label = " Excluir", command=lambda:  excluirtipo_click(janela3))
 menujan2.add_cascade(label = "Manutenção", menu = filemenu)


 consultamenu= Menu(menujan2, tearoff=0,)
 consultamenu.add_command(label = " Consulta por nome",command= lambda: consulta_nome1(janela3))
 consultamenu.add_command(label = " Consulta por Codigo",command=lambda: consulta_codigo1(janela3))

 menujan2.add_cascade(label = "Consutas diversas", menu = consultamenu)



 editmenu2 = Menu(menujan2, tearoff=0)
 editmenu2.add_command(label = "Nome", command= lambda: rel_nome1(janela3))
 editmenu2.add_command(label = "Codigo", command= lambda: rel_codigo1(janela3))
 menujan2.add_cascade(label = "Relatórios", menu = editmenu2)

 menusair = Menu(menujan2, tearoff=0)
 menusair.add_command(label= "Sair click aqui", command=janela3.destroy) 
 menujan2.add_cascade(label='para Sair',menu = menusair)

 janela3.config(menu=menujan2) #linha necessaria para aprecer o menu na janela de trabalho
 largura= 550
 altura = 450
 centro=centralizacao(janela3,largura, altura, posx, posy)
 criartabela1(janela3)
 janela3.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
 keyboard.on_press_key("f1", lambda _: janela3.destroy())
 #janela3.mainloop()

