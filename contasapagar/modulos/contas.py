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

def limpacamposcontas():
  tela.codigo.delete(0,END)
  tela.nome.delete(0,END)
  tela.compra.delete(0,END) 
  tela.vencimento.delete(0,END) 
  tela.descricao.delete(0,END)
  tela.tipo.delete(0,END) 
  tela.pagamento.delete(0,END)
  tela.valpagar.delete(0,END)
  tela.desconto.delete(0,END)
  tela.juros.delete(0,END)
  tela.documento.delete(0, END) 
  tela.tparcela.delete(0,END)
  tela.cs.delete(0,END)      
  return




# Relatórios

def abrirpdf2(arquivo1):
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



def imprimepdf2(arquivo1):
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


def pdfgerado2(sqlres,arquivo):
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
   elif  arquivo=="rel_nomep.pdf":
     cnv.drawString(250,830, "Relatório por parte do Nome")   
   elif  arquivo=="rel_cpfcnpj.pdf":        
    cnv.drawString(250,830, "Relatório por Cpf/Cnpj")   

   cnv.drawString(500,830, str(dia)+"/"+str(mes)+"/"+str(ano))
   eixo = 20
   y= 810
   z=1
   x=0

   for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
        x+=1
        y -= 20
        cnv.drawString(10,y,"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        y-= 20
        cnv.drawString(10,y, "codigo: "+ c+ " Nome: "+ n)
        y -= 20
        cnv.drawString(10,y, "Endereço: "+e)
        y -= 20               
        cnv.drawString(10,y, "Telefone: " + t+" Tipo:"+ti+ " Cpf: "+cp+" Cnpj: "+cn)               
        y -= 20
        cnv.drawString(10,y, "Cep: "+ce+" E_mail: "+ema)
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
          elif  arquivo=="rel_nomep.pdf":
            cnv.drawString(250,830, "Relatório por parte do Nome")   
          elif  arquivo=="rel_cpfcnpj.pdf":        
            cnv.drawString(250,830, "Relatório por Cpf/Cnpj")
          #    
          cnv.drawString(500,830, str(dia)+"/"+str(mes)+"/"+str(ano))
        z+=1  
            
   cnv.save()
   return
def gerapd3(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
          cursor.execute(f"SELECT *  FROM  contas ORDER BY cpf ASC")
        else:
          cursor.execute(f"SELECT *  FROM  contas ORDER BY cnpj ASC")

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            
        else:
           pdfgerado2(sqlres,"rel_cpfcnpj.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_cpfcnpj.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_cpfcnpj.pdf")
              cursor.close

      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),janela4)
        cursor.close()

def gerapdf2(event):
   escolhido=escolha.get()
   nomemem1= nomemem.get()
   #escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      nomemem1=nomemem1+"%"
      try:
        cursor.execute(f"SELECT *  FROM contas  WHERE nome LIKE '{nomemem1}'  ORDER BY nome ASC")
     
        sqlres=cursor.fetchall()
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            
        else:
           pdfgerado2(sqlres,"rel_nomep.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_nomep.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_nomep.pdf")
              cursor.close

      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),janela4)
        cursor.close()

def gerapd1(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
          cursor.execute(f"SELECT *  FROM  contas ORDER BY codigo ASC")
        else:
          cursor.execute(f"SELECT *  FROM  contas ORDER BY codigo DESC")

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return             
        else:
           pdfgerado2(sqlres,"rel_codigo.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_codigo.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_codigo.pdf")
              cursor.close
           return
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),janela4)
        cursor.close()
        return
def gerapdf(event):
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        
        cursor.execute(f"SELECT *  FROM  contas ORDER BY nome ASC")

        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return
        else:
           pdfgerado2(sqlres,"rel_nome.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_nome.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_nome.pdf")
              cursor.close
              return 
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),janela4)
        cursor.close()

   return
     
def moverpdf2(arquivo):
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

def rel_nome2(janela3):
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
   
   janela4.bind("<F3>", gerapdf)

   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #keyboard.on_press_key("f6", lambda _: moverpdf("rel_nome.pdf"))


def rel_cpfcnpj2(janela3):
   global janela4 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Cpf/Cnpj ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Cpf/Cnpj geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.25, rely=0.2)
   optado2= Radiobutton(janela4, text="CPF", value="A", variable=escolha1,font = ("Arial Bold", 9))
   optado2.place(relx=0.2,rely=0.3)
   optado3= Radiobutton(janela4, text= "CNPJ", value="D", variable=escolha1)
   optado3.place(relx=0.5,rely=0.3)
   escolhido1=escolha1.get()  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   escolhido=escolha.get()
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", gerapd3)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_nomep2(janela3):
   global janela4 
   global escolhido
   global escolha
   global nomemem

   escolha=StringVar(value="D")
   janela4 = Toplevel()
   janela4.title("Relatório por parte do Nome ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por por parte do Nome geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.2, rely=0.1)
   label1= Label(janela4, text="Entre com parte do Nome:",font=("Arial Bld",12))
   label1.place(relx=0.25, rely=0.25)
   nomemem = Entry(janela4,width=50)
   nomemem.place(relx=0.2,rely=0.3)
   nomemem.focus()  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   escolhido=escolha.get()
  # keyboard.on_press_key("f3", lambda _: gerapdf2())
   janela4.bind("<F3>", gerapdf2)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
  
   
def rel_codigo2(janela3):
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
   janela4.bind("<F3>", gerapd1)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")def rel_codigo(janela3):
   



def verificacodigo2():
   
   codigomem=tela.codigo.get()
   try:
       banco = sqlite3.connect('contaspagar.db')
       cursor = banco.cursor()
   except Error as ex:
       messagebox1("Erro na conexão com Banco de dados linha 45 "+str(ex),manutencao)
       limpacamposcontas()
       
       return 
   
   try:
       cursor.execute(f"SELECT * FROM contas WHERE codigo = '{codigomem}'")
       sqlres=cursor.fetchall()
       cursor.close() 
       if len(sqlres) == 0:  
          return sqlres
       else:
        
        messagebox1("Informação: Registro já existe não pode ser inserido linha 464",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return sqlres 
   except Error as ex:
       messagebox1("Erro na leitura da tabela contas linha 67 "+str(ex),manutencao)
       limpacamposcontas()
       
       return 

def consultacontas():
   
   sqlres=""
   tela.nome.delete(0,END) 
   tela.endereco.delete(0,END) 
   tela.telefone.delete(0,END)
   tela.tipo.delete(0,END) 
   tela.cpf.delete(0,END)
   tela.cnpj.delete(0,END)
   tela.cep.delete(0,END)
   tela.e_mail.delete(0,END)
   if len(tela.codigo.get())!=5:
        messagebox1("Tamanho do codigo sao 5 caracteres",manutencao)
        tela.codigo.delete(0,END)
        tela.codigo.focus()
        return sqlres 
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
       codigomem=tela.codigo.get()
       cursor.execute(f"SELECT * FROM contas WHERE codigo = '{codigomem}'")
       sqlres=cursor.fetchall()
       
       

       if len(sqlres) == 0:
            messagebox1("Registro não existe linha 501",manutencao)

            tela.codigo.delete(0,END)   
            tela.codigo.focus()
            cursor.close()  
            return sqlres
       else:
            tela.nome.insert(0, sqlres[0][1])
            tela.endereco.insert(0,sqlres[0][2])
            tela.telefone.insert(0, sqlres[0][3])
            tela.tipo.insert(0, sqlres[0][4]) 
            tela.cpf.insert(0, sqlres[0][5])
            tela.cnpj.insert(0, sqlres[0][6])
            tela.cep.insert(0, sqlres[0][7])
            tela.e_mail.insert(0, sqlres[0][8])
            cursor.close()  
            return sqlres 
      except Error as ex: 
         messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
         limpacamposcontas()
         cursor.close()
         return sqlres
         
   except Error as ex:
      messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 522 "+str(ex),manutencao)
      limpacamposcontas()
      cursor.close()  
      return sqlres   
                       
   
    
 
 

def tab_order2():
  tela.codigo.focus
  widgets = [tela.codigo,tela.documento,tela.tparcela,tela.compra,tela.vencimento,tela.descricao,tela.tipo,tela.pagamento,tela.valpagar,tela.desconto,tela.juros,tela.cs]
  for w in widgets:
     w.lift()

def vertipo(manutencao):
   sqleres=""
   if len(tela.tipo.get()) ==0 or len(tela.tipo.get()) > 2:
        messagebox1("Tipo tem que ser diferente de 0 tem que ter tamanho até 2",manutencao)
        tela.pagamento.focus()
        return
   if len(tela.pagamento.get())!=8:
        messagebox1("pagamento tem que ter tamanho 8",manutencao)
        tela.pagamento.focus()
        return
   tipomem=tela.tipo.get()
   mensagem= "Tipo"           
   sql=  f"SELECT nome FROM tipo WHERE codigo = '{tipomem}'"  
          
   sqlres=lertabela(sql,tipomem,manutencao,mensagem)
   if len(sqlres)==0:
       limpacamposcontas()
       tela.codigo.focus()
       return
   else:
      tela.nome.insert(0, sqlres[0][0])
   return


def verfornec(manutencao):
   sqleres=""
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tem que ter tamanho 5",manutencao)
        tela.codigo.focus()
        return
   codigomem=tela.codigo.get()         
   sql=  f"SELECT nome FROM fornecedor WHERE codigo = '{codigomem}'"  
   mensagem="fornecedor"       
   sqlres=lertabela(sql,codigomem,manutencao,mensagem)
   if len(sqlres)==0:
       limpacamposcontas()
       tela.codigo.focus()
       return
   else:
      tela.nome.insert(0, sqlres[0][0])
   return

def incluircontas():
      
   sqlres="" 
   
         
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        tela.codigo.focus()
        return
   else:
        sqlres =  verificacodigo2()
        if len(sqlres) != 0: 
          tela.codigo.focus
          return
   '''
                                               compra
                                               vencimento 
                                               descricao varchar(11),
                                               pagamento varchar(8),
                                               tipo integer,
                                               valpagar real(14),
                                               desconto real(14),
                                               juros    real(14),   
                                               documento varchar(20),
                                               tparcela integer,
                                               cs varchar(1),               

   '''

   if len(tela.compra.get())==0 or len(tela.compra.get())>8:
     
        messagebox1("Informação: digite o compra  esta vazio ou é maior que 8",manutencao)
        tela.compra.focus()
        return
   elif len(tela.vencimento.get())==0 or len(tela.vencimento.get())>8: 
        messagebox1("Informação: Endereço esta vazio ou é maior que 8",manutencao)
        tela.vencimento.focus()
        return
   elif len(tela.documento.get())==0 or len(tela.documento.get())>20:
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 20",manutencao)
        tela.documento.focus()
        return    
   elif len(tela.tparcela.get())==0 or len(tela.tparcela.get())>3:
        messagebox1("Informação: digite parcelado ou é maior que 3 digitos",manutencao)
        tela.tparcela.focus()
        return
   elif len(tela.cs.get()==0) or tela.cs.get() not in ("S","C") :
        messagebox1("Informação: digite o C para compras e S para Serviço tamanho 1",manutencao)
        tela.cep.focus()
        return            
   elif  len(tela.valpagar.get())==0 or  len(tela.valpagar.get()) > 14:
         messagebox1("Valor a pagar não pode ser zero e nem maior que 14",manutencao)
         tela.cpf.focus()
   
         
      
   try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()

        codigomem=tela.codigo.get()
        nomemem=tela.nome.get()
        enderecomem=tela.endereco.get()
        telefonemem=tela.telefone.get()
        tipomem=tela.tipo.get().upper()
        cpfmem=tela.cpf.get()
        cnpjmem=tela.cnpj.get()
        cepmem=tela.cep.get()
        e_mailmem = tela.e_mail.get()
        res = messagebox.askquestion('Confirma Inclusão', 'yes para sim - no para não')
        if res == 'yes':
          try:
           cursor.execute(f'''INSERT INTO contas VALUES('{codigomem}','{nomemem}','{enderecomem}',
                                                            '{telefonemem}','{tipomem}','{cpfmem}',
                                                                 '{cnpjmem}','{cepmem}','{e_mailmem}')''')
               

                                      
           banco.commit()
           cursor.close()
           messagebox1("registro Incluido com sucesso",manutencao)     
           limpacamposcontas()   
           tela.codigo.focus()
          except Error as ex:
            messagebox1("erro ao gravar tabela contas linha 252 "+ str(ex),manutencao)       
            limpacamposcontas()
        else:
           messagebox1("Registro não foi gravado",manutencao)

   except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 225 "+ str(ex),manutencao)
       limpacamposcontas()   
       tela.codigo.focus()
       return
   
def incluircontas_click(janela1):
    opcao=1
    opcao1=1
    
    global tela
    global manutencao  
    manutencao = Toplevel() # janela de nível superior
    tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    botao=Button(manutencao, text='Salvar',command=incluircontas)
    botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
    tab_order2()
    tela.codigo.focus()
    manutencao.bind("<F6>",verfornec(manutencao))
    manutencao.bind("<F7>", vertipo(manutencao))
    keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
             
    
    
    
           
     
def cosultacontas_click(janela1):
     opcao=2
     opcao1=1
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consultar',command=consultacontas)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     tela.codigo.focus()
     keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
      
def alteracaocontas():
    
    if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        tela.codigo.focus()
        return
    codigomem=tela.codigo.get() 
    nomemem=tela.nome.get()
    enderecomem=tela.endereco.get()
    telefonemem=tela.telefone.get()
    tipomem=tela.tipo.get().upper()
    cpfmem=tela.cpf.get()
    cnpjmem=tela.cnpj.get()
    cepmem=tela.cep.get()
    e_mailmem = tela.e_mail.get()
    sqlres= consultacontas()
    if len(sqlres)==0:
      limpacamposcontas()
      tela.codigo.focus()
      return
    if nomemem == "":
       nomemem = tela.nome.get()
    else:
       tela.nome.delete(0, END)
       tela.nome.insert(0, nomemem)

    if enderecomem == "":
       enderecomem = tela.endereco.get()
    else:
        tela.endereco.delete(0, END)
        tela.endereco.insert(0, enderecomem)

    if telefonemem=="":
        telefonemem = tela.telefone.get()
    else:
        tela.telefone.delete(0, END)
        tela.telefone.insert(0, telefonemem)    
    
    if tipomem =="":
        tipomem = tela.tipo.get()
    else:
        tela.tipo.delete(0, END)
        tela.tipo.insert(0, tipomem)


    if tipomem in ("F","f"):
       if cpfmem == "":
         cpfmem=tela.cpf.get()
       else:
         tela.cpf.delete(0, END)
         tela.cpf.insert(0,cpfmem)

    if tipomem in ("J","j"):  
       if cnpjmem=="":
         cnpjmem=tela.cnpj.get()
       else:
         tela.cnpj.delete(0, END)     
         tela.cnpj.insert(0,cnpjmem)    
    
    if cepmem=="":
        cepmem=tela.cep.get()
    else:
        tela.cep.delete(0, END)    
        tela.cep.insert(0, cepmem)

    if e_mailmem =="":
        e_mailmem = tela.e_mail.get()
    else:
        tela.e_mail.delete(0, END)
        tela.e_mail.insert(0, e_mailmem)   
                  
   
    if len(nomemem)==0 or len(nomemem) >50:
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 50",manutencao)
        tela.nome.focus()
        return
    elif len(enderecomem)==0 or len(enderecomem)>50: 
        messagebox1("Informação: Endereço esta vazio ou é maior que 50",manutencao)
        tela.endereco.focus()
        return
    elif len(telefonemem)==0 or len(telefonemem)>11:
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 11",manutencao)
        tela.telefone.focus()
        return    
    elif len(tipomem)!=1 or tipomem not in ("F","J", "f", "j"):
        messagebox1("Informação: tipo  tamanho 1 e pessoa (F)isica ou (J)urica",manutencao)
        tela.tipo.focus()
        return
    elif len(cepmem) != 8:
        messagebox1("Informação: digite o Cep tamanho 8",manutencao)
        tela.cep.focus()
        return
    elif  tipomem in ("F","f") and len(cpfmem) !=11:
         messagebox1("Cpf tem que ser tamanho 11 ",manutencao)
         tela.cpf.focus()
         
         if  len(cnpjmem) !=0:
              messagebox1("Você digitou Pessoa Fisica então não tem CNPJ ",manutencao)
              tela.cnpj.delete(0,END)
              return
         else:
              return

    elif tipomem in ("J","j") and len(cnpjmem) !=14:
               messagebox1("Cnpj tem que ser tamanho 14 ",manutencao)
               tela.cnpj.focus()
               if  len(cpfmem) !=0:
                 messagebox1("Você digitou Pessoa Juridica então não tem CPF ",manutencao)
                 tela.cpf.delete(0,END)
                 return
               else:
                 return      
    elif  tipomem in ("F","f") and len(cpfmem) == 11:
           if  len(cnpjmem) !=0:
               tela.cnpj.delete(0,END) 
    elif tela.tipo.get() in ("J","j") and len(tela.cnpj.get()) == 14:
           if  len(cpfmem) !=0:
               tela.cpf.delete(0,END)         
    
    res = messagebox.askquestion('Confirma Alteração', 'yes para sim - no para não')
    if res == 'yes':
    
      try:
          banco = sqlite3.connect('contaspagar.db')
          cursor = banco.cursor()
          
      except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 307 "+ str(ex),manutencao)
       limpacamposcontas()   
       tela.codigo.focus()
       return
          

      try:
           cursor.execute(f'''UPDATE contas SET codigo = '{codigomem}',
                                                    nome ='{nomemem}',
                                                    endereco ='{enderecomem}',
                                                    telefone ='{telefonemem}',
                                                    tipo = '{tipomem}',
                                                    cpf = '{cpfmem}',
                                                    cnpj = '{cnpjmem}',
                                                    cep = '{cepmem}',
                                                    e_mail ='{e_mailmem}'
                                                    WHERE codigo = '{codigomem}' ''')
               

                                      
           banco.commit()
           cursor.close()     
           messagebox1("registro Alterado com sucesso",manutencao)
           limpacamposcontas()   
           tela.codigo.focus()
      except Error as ex:
            messagebox("erro ao regravar tabela contas linha 333"+ str(ex),manutencao)       
            limpacamposcontas() 
            return
    else:
           messagebox1("Registro não foi Alterado",manutencao)
           return
    
def alteracaocontas_clik(janela1):
     opcao=3
     opcao1=1
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consutar',command=consultacontas)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Alterar',command=alteracaocontas)
     botao1.grid(row=10, column=1,padx=0,pady=50,sticky=W)
     tab_order2()
     tela.codigo.focus()
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
     
      
 
     
      
     
def exclusaocontas():
    codigomem=tela.codigo.get()
    sqlres= consultacontas()
    if len(sqlres)==0:
      limpacamposcontas()
      tela.codigo.focus()
      return
    
    res = messagebox.askquestion('Confirma Exclusão', 'yes para sim - no para não')
    if res == 'yes':
       try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        
        try:
           cursor.execute(f"DELETE  FROM contas WHERE codigo = '{codigomem}'")
           banco.commit()
           cursor.close()     
           messagebox1("Registro Excluido com sucesso",manutencao)
           limpacamposcontas()   
           tela.codigo.focus()
        except Error as ex:
            messagebox1("erro ao Excluir tabela contas linha 366"+ str(ex),manutencao)       
            limpacamposcontas() 
       except Error as ex:
           messagebox1("erro ao conectar com banco de dados linha 343 "+ str(ex),manutencao)
           limpacamposcontas()   
           tela.codigo.focus()
           return
    else:
           messagebox1("Registro não foi Excluido",manutencao)      
    return 
def excluircontas_click(janela1): 
     opcao=4
     opcao1=1
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consultar',command=consultacontas)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Excluir',command=exclusaocontas)
     botao1.grid(row=10, column=1,padx=0,pady=50,sticky=W)
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
# consultas

def consulta_nome2(janela3):
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Endereço', 'Telefone', 'Tipo', 'Cpf', 'Cnpj', 'Cep', 'E_mail' ), show= 'headings')
    
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
   tv.column('Endereço', minwidth=0, width=250)
   tv.column('Telefone', minwidth=9, width=100)
   tv.column('Tipo', minwidth=1, width=30)
   tv.column('Cpf', minwidth=0, width=100)
   tv.column('Cnpj', minwidth=0, width=150)
   tv.column('Cep', minwidth=0, width=100)
   tv.column('E_mail', minwidth=0, width=200)
   
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
   tv.heading('Endereço', text='ENDEREÇO')
   tv.heading('Telefone', text='TELEFONE')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Cpf', text='CPF')
   tv.heading('Cnpj', text='CNPJ')
   tv.heading('Cep', text='CEP')
   tv.heading('E_mail', text='E_MAIL')
  
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
        cursor.execute(f"SELECT *  FROM  contas ORDER BY nome")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 987 "+str(ex),janela4)
        cursor.close() 
        
 
def cosulta_cpf2(janela3):
   janela4 = Toplevel()
   janela4.title("Consultas por Cpf ESC para SAIR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Endereço', 'Telefone', 'Tipo', 'Cpf', 'Cnpj', 'Cep', 'E_mail' ), show= 'headings')
    
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
   tv.column('Endereço', minwidth=0, width=250)
   tv.column('Telefone', minwidth=9, width=100)
   tv.column('Tipo', minwidth=1, width=30)
   tv.column('Cpf', minwidth=0, width=100)
   tv.column('Cnpj', minwidth=0, width=150)
   tv.column('Cep', minwidth=0, width=100)
   tv.column('E_mail', minwidth=0, width=200)
   
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
   tv.heading('Endereço', text='ENDEREÇO')
   tv.heading('Telefone', text='TELEFONE')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Cpf', text='CPF')
   tv.heading('Cnpj', text='CNPJ')
   tv.heading('Cep', text='CEP')
   tv.heading('E_mail', text='E_MAIL')
  
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
        cursor.execute(f"SELECT *  FROM  contas ORDER BY cpf")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            return
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),janela4)
        cursor.close() 
        return

def cosulta_cnpj2(janela3):
   janela4 = Toplevel()
   janela4.title("Consultas por Cnpj ESC para SAIR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Endereço', 'Telefone', 'Tipo', 'Cpf', 'Cnpj', 'Cep', 'E_mail' ), show= 'headings')
    
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
   tv.column('Endereço', minwidth=0, width=250)
   tv.column('Telefone', minwidth=9, width=100)
   tv.column('Tipo', minwidth=1, width=30)
   tv.column('Cpf', minwidth=0, width=100)
   tv.column('Cnpj', minwidth=0, width=150)
   tv.column('Cep', minwidth=0, width=100)
   tv.column('E_mail', minwidth=0, width=200)
   
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
   tv.heading('Endereço', text='ENDEREÇO')
   tv.heading('Telefone', text='TELEFONE')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Cpf', text='CPF')
   tv.heading('Cnpj', text='CNPJ')
   tv.heading('Cep', text='CEP')
   tv.heading('E_mail', text='E_MAIL')
  
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
        cursor.execute(f"SELECT *  FROM  contas ORDER BY cnpj")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1123 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1127 "+str(ex),janela4)
        cursor.close() 
        

def consultacodigoopcao2(event):
   tv.delete(*tv.get_children())
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f"SELECT *  FROM  contas ORDER BY codigo ASC")
        else:
          cursor.execute(f"SELECT *  FROM  contas ORDER BY codigo DESC")

        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1156 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1160 "+str(ex),janela4)
        cursor.close() 
        

def consulta_codigo2(janela3):
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Endereço', 'Telefone', 'Tipo', 'Cpf', 'Cnpj', 'Cep', 'E_mail' ), show= 'headings')
    
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
   tv.column('Endereço', minwidth=0, width=250)
   tv.column('Telefone', minwidth=9, width=100)
   tv.column('Tipo', minwidth=1, width=30)
   tv.column('Cpf', minwidth=0, width=100)
   tv.column('Cnpj', minwidth=0, width=150)
   tv.column('Cep', minwidth=0, width=100)
   tv.column('E_mail', minwidth=0, width=200)
   
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
   tv.heading('Endereço', text='ENDEREÇO')
   tv.heading('Telefone', text='TELEFONE')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Cpf', text='CPF')
   tv.heading('Cnpj', text='CNPJ')
   tv.heading('Cep', text='CEP')
   tv.heading('E_mail', text='E_MAIL')
  
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
   janela4.bind("<F3>", consultacodigoopcao2)
   
def tecla_obtida2(event):
    tv.delete(*tv.get_children())
    nomemem1= nomemem.get()
    try: 
         banco = sqlite3.connect('contaspagar.db')
         cursor = banco.cursor()
         
         #cursor.execute(f"SELECT * FROM contas WHERE codigo = '{codigomem}'")
         #sqlres=cursor.fetchall()
         nomemem1=nomemem1+"%"
         try:
               cursor.execute(f"SELECT *  FROM contas  WHERE nome LIKE '{nomemem1}'  ORDER BY nome ASC")
               sqlres=cursor.fetchall()
               
          
               
               if len(sqlres) == 0:
                    messagebox1("Não tem dados a mostrar na consulta",janela4)
                    cursor.close()
                    return
               else:
                    for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
                         tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
                    
                    cursor.close()
                    return
         except Error as ex: 
               messagebox1("Erro ao tentar ler o registro linha 1315 "+str(ex),janela4)
               cursor.close()
               return
               
    except Error as ex:
          messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1251 "+str(ex),janela4)
          cursor.close()
          return 
     
     

def consulta_porcao2(janela3):
        
   global janela4 
   global tv 
   global nomemem 
   janela4 = Toplevel()
   janela4.title("Consultas por pedaços de Nomes - ESC  para SAIR  -  F3  PARA CONSULTAR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Endereço', 'Telefone', 'Tipo', 'Cpf', 'Cnpj', 'Cep', 'E_mail' ), show= 'headings')
   
   tv.column('Codigo', minwidth=5, width=50)
   tv.column('Nome', minwidth=0, width=250)
   tv.column('Endereço', minwidth=0, width=250)
   tv.column('Telefone', minwidth=9, width=100)
   tv.column('Tipo', minwidth=1, width=30)
   tv.column('Cpf', minwidth=0, width=100)
   tv.column('Cnpj', minwidth=0, width=150)
   tv.column('Cep', minwidth=0, width=100)
   tv.column('E_mail', minwidth=0, width=200)
   
   tv.heading('Codigo', text='Codigo' )
   tv.heading('Nome', text='NOME')
   tv.heading('Endereço', text='ENDEREÇO')
   tv.heading('Telefone', text='TELEFONE')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Cpf', text='CPF')
   tv.heading('Cnpj', text='CNPJ')
   tv.heading('Cep', text='CEP')
   tv.heading('E_mail', text='E_MAIL')
   tv.place(relx=0.01,rely=0.1,relwidth=0.97,relheight=0.75)
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)
   verscrlbar.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.75)
   verscrlbar1.place(relx=0.01,rely=0.85,relwidth=0.97,relheight=0.05)
   tv.config(yscrollcommand=verscrlbar.set)
   tv.config(xscrollcommand=verscrlbar1.set)
   Label(janela4, text="Entre com parte do nome:", font=('Arial', 15)).grid(row=1, column=3,sticky=W)   
   nomemem = Entry(janela4,width=50)
   nomemem.grid(row=1, column=4,sticky=W)
   nomemem.focus()
   print(nomemem.get())
   #keyboard.on_press_key("f3", lambda _: tecla_obtida())
   janela4.bind("<F3>", tecla_obtida2)   
     

# relatorios
  


def contas_menu(janela1):
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


 filemenu.add_command(label = " Inclusão",command= lambda: incluircontas_click(janela3))
 filemenu.add_command(label = " Consulta",command= lambda: cosultacontas_click(janela3))
 filemenu.add_command(label = " Alteração",command=lambda: alteracaocontas_clik(janela3))
 filemenu.add_command(label = " Excluir", command=lambda:  excluircontas_click(janela3))
 menujan2.add_cascade(label = "Manutenção", menu = filemenu)


 consultamenu= Menu(menujan2, tearoff=0,)
 consultamenu.add_command(label = " Consulta por nome",command= lambda: consulta_nome2(janela3))
 consultamenu.add_command(label = " Consulta por Cnpj",command= lambda: cosulta_cnpj2(janela3))
 consultamenu.add_command(label = " Consulta por Cpf",command= lambda: cosulta_cpf2(janela3))
 consultamenu.add_command(label = " Consulta por Codigo",command=lambda: consulta_codigo2(janela3))
 consultamenu.add_command(label = " consulta por pedaço do nome", command=lambda:  consulta_porcao2(janela3))
 menujan2.add_cascade(label = "Consutas diversas", menu = consultamenu)



 editmenu2 = Menu(menujan2, tearoff=0)
 editmenu2.add_command(label = "Nome", command= lambda: rel_nome2(janela3))
 editmenu2.add_command(label = "Cnpj/Cpf", command=lambda: rel_cpfcnpj2(janela3))
 editmenu2.add_command(label = "Pedaço do nome",command=lambda: rel_nomep2(janela3))
 editmenu2.add_command(label = "Codigo", command= lambda: rel_codigo2(janela3))
 menujan2.add_cascade(label = "Relatórios", menu = editmenu2)

 menusair = Menu(menujan2, tearoff=0)
 menusair.add_command(label= "Sair click aqui", command=janela3.destroy) 
 menujan2.add_cascade(label='para Sair',menu = menusair)

 janela3.config(menu=menujan2) #linha necessaria para aprecer o menu na janela de trabalho
 largura= 550
 altura = 450
 centro=centralizacao(janela3,largura, altura, posx, posy)
 sql='''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5)  NOT NULL, 
                                               compra varchar(8) NOT NULL, 
                                               vencimento varchar(8) not null,
                                               descricao varchar(11),
                                               pagamento varchar(8),
                                               tipo integer,
                                               valpagar real(14),
                                               desconto real(14),
                                               juros    real(14),   
                                               documento varchar(20),
                                               tparcela integer,
                                               cs varchar(1),               
                                               PRIMARY KEY (codigo,documento,tparcela),   
                                               FOREIGN KEY(codigo) REFERENCES  fornecedor(codigo),
                                               FOREIGN KEY(tipo) REFERENCES  tipo(codigo))'''

 criartabela2(janela3,sql) 
 janela3.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
 keyboard.on_press_key("f1", lambda _: janela3.destroy())
 #janela3.mainloop()

'''
                                               compra
                                               vencimento 
                                               descricao varchar(11),
                                               pagamento varchar(8),
                                               tipo integer,
                                               valpagar real(14),
                                               desconto real(14),
                                               juros    real(14),   
                                               documento varchar(20),
                                               tparcela integer,
                                               cs varchar(1),               

'''
