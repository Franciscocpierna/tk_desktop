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
  tela.desctipo.delete(0,END)
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
  messagebox1("Erro ao tentar Abrir linha 61 "+str(ex),janela4)
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
    messagebox1("Erro ao tentar imprimir linha 81 "+str(ex),janela4)
    return


def pdfgerado2(sqlres,arquivo):
   data = datetime.date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
  
   try: 
    cnv = canvas.Canvas(rf"C:\python_projetos\3.11.2\tk_desktop\arquivo\{arquivo}", pagesize=A4)
   except Error as ex:
    messagebox1(str(ex)+ " linha 94",janela4)
    return
   cnv.setFont('Helvetica', 9)  
   #cnv.drawString(10,830, "teste") # canto superior A4
   if arquivo=="rel_nome.pdf":
    cnv.drawString(250,830, "Relatório por Nomes") # centro do pdf linha superior
   elif  arquivo=="rel_codigo.pdf":
    cnv.drawString(250,830, "Relatório por Código")   
   elif  arquivo=="rel_nomep.pdf":
     cnv.drawString(250,830, "Relatório por parte do Nome ou Código")   
   elif  arquivo=="rel_verncimento.pdf":        
    cnv.drawString(250,830, "Relatório por Vencimento")   
   elif arquivo == "rel_compras.pdf":
    cnv.drawString(250,830, "Relatório por Compras")  
   elif arquivo == "rel_pagamento.pdf":
    cnv.drawString(250,830, "Relatório por Pagamento")           
   elif arquivo == "rel_atraso.pdf":
    cnv.drawString(250,830, "Relatório por Atraso")

   cnv.drawString(500,830, str(dia)+"/"+str(mes)+"/"+str(ano))
   eixo = 20
   y= 810
   z=1
   x=0

   for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
        x+=1
        y -= 20
        cnv.drawString(10,y,"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        y-= 20
        cnv.drawString(10,y, "codigo: "+ c+ " Nome: "+ n)
        y -= 20
        cnv.drawString(10,y, "Compra: "+co+"Vencimento: " + ve+" Descrição:"+de) 
        y -= 20               
        cnv.drawString(10,y,  " Pagamento: "+pg+" Tipo: "+tp+ " Descrição Tipo:"+str(dt)+ " Valor a Pagar:"+str(vp))        
        y -= 20
        cnv.drawString(10,y, " Desconto:"+str(des)+" Juros: "+ju+" Documento:"+doc+" Parcelas:"+par+" Serviço ou compra (C)ompra e (S)serviço:"+cs1)
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
            cnv.drawString(250,830, "Relatório por parte do Nome ou Código")   
          elif  arquivo=="rel_verncimento.pdf":        
            cnv.drawString(250,830, "Relatório por Vencimento")   
          elif arquivo == "rel_compras.pdf":
            cnv.drawString(250,830, "Relatório por Compras")  
          elif arquivo == "rel_pagamento.pdf":
            cnv.drawString(250,830, "Relatório por Pagamento")           
          elif arquivo == "rel_atraso.pdf":
            cnv.drawString(250,830, "Relatório por Atraso")

          #    
          cnv.drawString(500,830, str(dia)+"/"+str(mes)+"/"+str(ano))  
        z+=1  
            
   cnv.save()
   return

def gerapdv(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.vencimento ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.vencimento DESC''')

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            
        else:
           pdfgerado2(sqlres,"rel_vencimento.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_vencimento.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_vencimento.pdf")
              cursor.close

      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 196 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 200 "+str(ex),janela4)
        cursor.close()


def gerapdp(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento DESC''')

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            
        else:
           pdfgerado2(sqlres,"rel_pagemento.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_pagamento.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_pagamento.pdf")
              cursor.close

      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 240 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 244 "+str(ex),janela4)
        cursor.close()

def gerapdat(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento DESC''')

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return             
        else:
           pdfgerado2(sqlres,"rel_atraso.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_atraso.pdf")
              cursor.close()              
           else:        
              abrirpdf2("rel_atraso.pdf")
              cursor.close
           return
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 283 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 287 "+str(ex),janela4)
        cursor.close()
        return

def gerapdf2(event):
   escolhido=escolha.get()
   nomemem1= nomemem.get()
   
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      #nomemem1=nomemem1+"%"
      #nome ou codigo
      try:
        if  escolhido1== "N":
          nomemem1= nomemem.get()
          nomemem1=nomemem1+"%"
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND b.nome LIKE '{nomemem1}' ORDER BY b.nome ASC''')
            
        else:
           codigomem=nomemem.get()
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.codigo = '{codigomem}' ORDER BY a.codigo ASC''')

       # cursor.execute(f"SELECT *  FROM contas  WHERE b.nome LIKE '{nomemem1}'  ORDER BY nome ASC")
     
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
           messagebox1("Erro ao tentar ler o registro linha 332 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 336 "+str(ex),janela4)
        cursor.close()

def gerapd1(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento DESC''')

      
        
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
           messagebox1("Erro ao tentar ler o registro linha 375 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 379 "+str(ex),janela4)
        cursor.close()
        return
def geracompras(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.compras ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.compras DESC''')

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return             
        else:
           pdfgerado2(sqlres,"rel_compras.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_compras")
              cursor.close()              
           else:        
              abrirpdf2("rel_compras.pdf")
              cursor.close
           return
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 418 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 422 "+str(ex),janela4)
        cursor.close()
        return

def gerapdf(event):
   escolhido=escolha.get()
   escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY b.nome ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY b.nome DESC''')

      
        
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
           messagebox1("Erro ao tentar ler o registro linha 462 "+str(ex),janela4)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 466 "+str(ex),janela4)
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
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Nome ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Nome geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.25, rely=0.2)
   optado2= Radiobutton(janela4, text="Crescente", value="A", variable=escolha1,font = ("Arial Bold", 9))
   optado2.place(relx=0.2,rely=0.3)
   optado3= Radiobutton(janela4, text= "Decrescente", value="D", variable=escolha1)
   optado3.place(relx=0.5,rely=0.3)
   escolhido1=escolha1.get()  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   escolhido=escolha.get()
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   #keyboard.on_press_key("f3", lambda _: gerapdf())
   
   janela4.bind("<F3>", gerapdf)

   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #keyboard.on_press_key("f6", lambda _: moverpdf("rel_nome.pdf"))

def rel_vencimento(janela3):
   global janela4 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Vencimento ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Vencimento geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.25, rely=0.2)
   optado2= Radiobutton(janela4, text="Crescente", value="A", variable=escolha1,font = ("Arial Bold", 9))
   optado2.place(relx=0.2,rely=0.3)
   optado3= Radiobutton(janela4, text= "Decrescente", value="D", variable=escolha1)
   optado3.place(relx=0.5,rely=0.3)
   escolhido1=escolha1.get()  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   escolhido=escolha.get()
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", gerapdv)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")



def rel_atraso(janela3):
   global janela4 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Pagamento ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Atraso de Pagamento geração em PDF ",font = ("Arial Bold", 12))
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
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", gerapdat)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_compras(janela3):
   global janela4 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Pagamento ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Compras geração em PDF ",font = ("Arial Bold", 12))
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
   janela4.bind("<F3>", geracompras)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_pagamento(janela3):
   global janela4 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Pagamento ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Pagamento geração em PDF ",font = ("Arial Bold", 12))
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
   janela4.bind("<F3>", gerapdp)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_nomep2(janela3):
   global janela4 
   global escolhido
   global escolha
   global nomemem
   global escolha1
   global escolhido1

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
   optado3= Radiobutton(janela4, text="Nome", value="N", variable=escolha1)
   optado3.grid(relx=0.8,rely=0.4)
   optado4= Radiobutton(janela4, text= "Código", value="C", variable=escolha1)
   optado4.grid(relx=1.0,rely=0.4)
   escolhido1=escolha1.get()

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
       messagebox1("Erro na conexão com Banco de dados linha 752 "+str(ex),manutencao)
       limpacamposcontas()
       
       return 
   
   try:
       #cursor.execute(f"SELECT * FROM contas WHERE codigo = '{codigomem}'")
       cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento ASC''')
       sqlres=cursor.fetchall()
       cursor.close() 
       if len(sqlres) == 0:  
          return sqlres
       else:
        
        messagebox1("Informação: Registro já existe não pode ser inserido linha 768",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return sqlres 
   except Error as ex:
       messagebox1("Erro na leitura da tabela contas linha 773 "+str(ex),manutencao)
       limpacamposcontas()
       
       return 

def consultacontas():
   
   sqlres=""
   tela.nome.delete(0,END)
   tela.compra.delete(0,END) 
   tela.vencimento.delete(0,END) 
   tela.descricao.delete(0,END)
   tela.tipo.delete(0,END) 
   tela.desctipo.delete(0,END)
   tela.desctipo.delete(0,END)
   tela.pagamento.delete(0,END)
   tela.valpagar.delete(0,END)
   tela.desconto.delete(0,END)
   tela.juros.delete(0,END)
   tela.documento.delete(0, END) 
   tela.tparcela.delete(0,END)
   tela.cs.delete(0,END)      

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
       #cursor.execute(f"SELECT * FROM contas WHERE codigo = '{codigomem}'")
       cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento ASC''')
       sqlres=cursor.fetchall()
       
       

       if len(sqlres) == 0:
            messagebox1("Registro não existe linha 815",manutencao)

            tela.codigo.delete(0,END)   
            tela.codigo.focus()
            cursor.close()  
            return sqlres
       else:
            codigomem=tela.codigo.get()
            cursor.execute(f"SELECT mome FROM fornecedor WHERE codigo = '{codigomem}'")
            sql1 = cursor.fetchall()
            tela.nome.insert(0, sql1[0][0])
            tela.compra.insert(0, sqlres[0][1])
            tela.vencimento.insert(0,sqlres[0][2])
            tela.descricao.insert(0, sqlres[0][3])
            tela.pagamento.insert(0, sqlres[0][4]) 
            tela.tipo.insert(0, sqlres[0][5])
            tipomem=sqlres[0][5]
            if tipomem!="":
              cursor.execute(f"SELECT nome FROM tipo WHERE codigo = '{tipomem}'")
              sql2=cursor.fetchall()
              tela.desctipo.insert(0, sql2[0][0])
            tela.valpagar.insert(0, sqlres[0][6])
            tela.desconto.insert(0, sqlres[0][7])
            tela.juros.insert(0, sqlres[0][8])
            tela.documento.insert(0, sqlres[0][9])
            tela.tparcela.insert(0, sqlres[0][10])
            tela.cs.insert(0, sqlres[0][11])
            
            cursor.close()  
            return sqlres 
      except Error as ex: 
         messagebox1("Erro ao tentar ler o registro linha 846 "+str(ex),manutencao)
         limpacamposcontas()
         cursor.close()
         return sqlres
         
   except Error as ex:
      messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 852 "+str(ex),manutencao)
      limpacamposcontas()
      cursor.close()  
      return sqlres   
                       
   
    
 
 

def tab_order2():
  tela.codigo.focus
  widgets = [tela.codigo,tela.documento,tela.tparcela,tela.compra,tela.vencimento,tela.descricao,tela.tipo,tela.pagamento,tela.valpagar,tela.desconto,tela.juros,tela.cs]
  for w in widgets:
     w.lift()

def vertipo(manutencao):
   if  len(tela.tipo.get())!=2:
      return
   sqleres=""
   if len(tela.tipo.get())  !=2:
        messagebox1("Tipo tem que ser diferente de 0 tem que ter tamanho  2",manutencao)
        tela.pagamento.focus()
        return
   if len(tela.pagamento.get())!=8:
        messagebox1("pagamento tem que ter tamanho 8",manutencao)
        tela.pagamento.focus()
        return
   tipomem=tela.tipo.get()
   mensagem= "Tipo"           
   sql=  f"SELECT nome FROM tipo WHERE contas.tipo = '{tipomem}'"  
          
   sqlres=lertabela(sql,tipomem,manutencao,mensagem)
   if len(sqlres)==0:
       limpacamposcontas()
       tela.codigo.focus()
       return
   else:
      tela.desctipo.insert(0, sqlres[0][0])
   return


def verfornec():
   if len(tela.codigo.get())!=5:
      return

   sqleres=""
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tem que ter tamanho 5",manutencao)
        tela.codigo.focus()
        return
   codigomem=tela.codigo.get()         
   sql=  f"SELECT nome FROM fornecedor WHERE contas.codigo = '{codigomem}'"  
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
   

   if len(tela.compra.get())==0:
        messagebox1("Informação: digite a compra  esta vazio ",manutencao)
        tela.compra.focus()
        return
   elif len(tela.vencimento.get())==0: 
        messagebox1("Informação: Data de Vencimento esta vazio",manutencao)
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
   #elif  len(tela.valpagar.get())==0 or  len(tela.valpagar.get()) > 14:
   #      messagebox1("Valor a pagar não pode ser zero e nem maior que 14",manutencao)
   #      tela.cpf.focus()
   
         
      
   try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        codigomem=tela.codigo.get()
        compramem=tela.compra.get()
        vencimentomem=tela.vencimento.get()
        descricaomem=tela.descricao.get()
        pagamentomem=tela.pagamento.get()
        tipomem=tela.tipo.get()
        valpagarmem=tela.valpagar.get()
        descontomem = tela.desconto.get()
        jurosmem = tela.juros.get()
        documentomem=tela.documento.get()
        tparcelamem=tela.tparcela.get()
        csmem=tela.cs.get()
        

        res = messagebox.askquestion('Confirma Inclusão', 'yes para sim - no para não')
        if res == 'yes':
          try:
           cursor.execute(f'''INSERT INTO contas VALUES('{codigomem}','{compramem}','{vencimentomem}',
                                                            '{descricaomem}','{pagamentomem}','{tipomem}',
                                                                 '{valpagarmem}','{descontomem}','{jurosmem}',
                                                                 '{documentomem}','{tparcelamem}','{csmem}')''')
               
                     
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
       messagebox1("erro ao conectar com banco de dados linha 995 "+ str(ex),manutencao)
       limpacamposcontas()   
       tela.codigo.focus()
       return
def dadosdatac():
 if len(tela.compra.get()) ==2:
      memdata=tela.compra.get()
      
      if memdata.isnumeric():
         memdata=memdata+"/"
         tela.compras.insert(0,memdata)
      else:
         messagebox1("digite números é data",manutencao)   
 elif len(tela.compra.get())==5:
         memdata1=tela.compra.get()
         memdata=tela.compra.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           tela.compra.insert(0,memdata1)
         else:
           messagebox1("digite números é data",manutencao)   
 elif len(tela.compra.get())==10:
         memdata1=memdata
         memdata=tela.compra.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           tela.compra.insert(0,memdata1)
         else:
           messagebox1("digite números é data",manutencao) 
           tela.compra.focus()   
         
          
         
def dadosdatav():
   if len(tela.vencimento.get()) ==2:
      memdata=tela.vencimento.get()
      
      if memdata.isnumeric():
         memdata=memdata+"/"
         tela.vencimento.insert(0,memdata)
      else:
         messagebox1("digite números é data",manutencao)   
   elif len(tela.vencimento.get())==5:
         memdata1=tela.vencimento.get()
         memdata=tela.vencimento.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           tela.vencimento.insert(0,memdata1)
         else:
           messagebox1("digite números é data",manutencao)   
   elif len(tela.vencimento.get())==10:
         memdata1=memdata
         memdata=tela.vencimento.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           tela.vencimento.insert(0,memdata1)
         else:
           messagebox1("digite números é data",manutencao) 
           tela.vencimento.focus()    
              
def dadosdatap():
   if len(tela.pagamento.get()) ==2:
      memdata=tela.pagamento.get()
      
      if memdata.isnumeric():
         memdata=memdata+"/"
         tela.pagamento.insert(0,memdata)
      else:
         messagebox1("digite números é data",manutencao)   
   elif len(tela.pagamento.get())==5:
         memdata1=tela.pagamento.get()
         memdata=tela.pagamento.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           tela.pagamento.insert(0,memdata1)
         else:
           messagebox1("digite números é data",manutencao)   
   elif len(tela.pagamento.get())==10:
         memdata1=memdata
         memdata=tela.pagamento.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           tela.pagamento.insert(0,memdata1)
         else:
           messagebox1("digite números é data",manutencao) 
           tela.compra.focus()   



def verificadatac():
     
    data2=tela.compra.get().split('/')

    dia = int(data2[0])
    mes = int(data2[1] )
    ano = int(data2[2])

    valida = False
    
    # Meses com 31 dias
    if( mes==1 or mes==3 or mes==5 or mes==7 or \
        mes==8 or mes==10 or mes==12):
        if(dia<=31):
            valida = True
    # Meses com 30 dias
    elif( mes==4 or mes==6 or mes==9 or mes==11):
        if(dia<=30):
            valida = True
    elif mes==2:
        # Testa se é bissexto
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
            if(dia<=29):
                valida = True
        elif(dia<=28):
                valida = True

    if(valida) == False:
        messagebox1("Data Inválida digite novamente",manutencao)
        tela.compra.focus()

def verificadatav():
     
    data2=tela.vencimento.split('/')

    dia = int(data2[0])
    mes = int(data2[1] )
    ano = int(data2[2])

    valida = False
    
    # Meses com 31 dias
    if( mes==1 or mes==3 or mes==5 or mes==7 or \
        mes==8 or mes==10 or mes==12):
        if(dia<=31):
            valida = True
    # Meses com 30 dias
    elif( mes==4 or mes==6 or mes==9 or mes==11):
        if(dia<=30):
            valida = True
    elif mes==2:
        # Testa se é bissexto
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
            if(dia<=29):
                valida = True
        elif(dia<=28):
                valida = True

    if(valida) == False:
        messagebox1("Data Inválida digite novamente",manutencao)
        tela.vencimento.focus()
def verificadatap():
   if tela.pagamento.get() != 0:  
    data2=tela.pagamento.split('/')

    dia = int(data2[0])
    mes = int(data2[1] )
    ano = int(data2[2])

    valida = False
    
    # Meses com 31 dias
    if( mes==1 or mes==3 or mes==5 or mes==7 or \
        mes==8 or mes==10 or mes==12):
        if(dia<=31):
            valida = True
    # Meses com 30 dias
    elif( mes==4 or mes==6 or mes==9 or mes==11):
        if(dia<=30):
            valida = True
    elif mes==2:
        # Testa se é bissexto
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
            if(dia<=29):
                valida = True
        elif(dia<=28):
                valida = True

    if(valida) == False:
        messagebox1("Data Inválida digite novamente",manutencao)
        tela.pagamento.focus()

def dadosvalor():
   if len(tela.valpagar.get())==0:
      return
   if tela.valpagar.get() in ",0123456789":
     return
   else:
      messagebox1("valor inválido digite novamente",manutencao)
      tela.valpagar.insert(0,END)
      return        
def valorout():
   valpag=tela.valapagar.get()
   if len(valpag)> 0:
     if valpag.find(',')==0 or len(valpag)>12:
        messagebox1("digite virgula tem que ter 2 casas decimais ou tem mais de 12 digitos",manutencao)
        tela.valpagar.insert(0,END)
        tela.valpagar.focus()
     else:   
      if len(valpag[valpag.find(',')+1:]) > 2:
        messagebox1("digite novamente tem que ter 2 casas decimais",manutencao)
        tela.valpagar.insert(0,END)
        tela.valpagar.focus()
      else:
        if len(valpag) == 7:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6]
        if len(valpag) == 8:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]          
        if len(valpag) == 9:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]
        if len(valpag) == 10:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+"."+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]
        if len(valpag) == 11:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+"."+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]
        if len(valpag) == 12:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+"."+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]+valpag[11]
     tela.valpagar.insert(0, valpag1)      
     return
def dadosdesconto():
   if len(tela.desconto.get())==0:
      return
   if tela.desconto.get() in ",0123456789":
     return
   else:
      messagebox1("valor inválido digite novamente",manutencao)
      tela.desconto.insert(0,END)
      return        
def descontoout():
   valpag=tela.desconto.get()
   if len(valpag)> 0:
     if valpag.find(',')==0 or len(valpag)>12:
        messagebox1("digite virgula tem que ter 2 casas decimais ou tem mais de 12 digitos",manutencao)
        tela.desconto.insert(0,END)
        tela.desconto.focus()
     else:   
      if len(valpag[valpag.find(',')+1:]) > 2:
        messagebox1("digite novamente tem que ter 2 casas decimais",manutencao)
        tela.desconto.insert(0,END)
        tela.desconto.focus()
      else:
        if len(valpag) == 7:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6]
        if len(valpag) == 8:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]          
        if len(valpag) == 9:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]
        if len(valpag) == 10:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+"."+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]
        if len(valpag) == 11:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+"."+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]
        if len(valpag) == 12:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+"."+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]+valpag[11]
     tela.desconto.insert(0, valpag1)      
     return
def dadosjuros():
   if len(tela.juros.get())==0:
      return
   if tela.juros.get() in ",0123456789":
     return
   else:
      messagebox1("valor inválido digite novamente",manutencao)
      tela.juros.insert(0,END)
      return        
def jurosout():
   valpag=tela.juros.get()
   if len(valpag)> 0:
     if valpag.find(',')==0 or len(valpag)>12:
        messagebox1("digite virgula tem que ter 2 casas decimais ou tem mais de 12 digitos",manutencao)
        tela.juros.insert(0,END)
        tela.juros.focus()
        return
     else:   
      if len(valpag[valpag.find(',')+1:]) > 2:
        messagebox1("digite novamente tem que ter 2 casas decimais",manutencao)
        tela.juros.insert(0,END)
        tela.juros.focus()
      else:
        if len(valpag) == 7:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6]
        if len(valpag) == 8:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]          
        if len(valpag) == 9:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]
        if len(valpag) == 10:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+"."+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]
        if len(valpag) == 11:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+"."+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]
        if len(valpag) == 12:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+"."+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]+valpag[11]
     tela.juros.insert(0, valpag1)      
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
    tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
    tela.compra.bind("<KeyRelease>", dadosdatac)
    tela.vencimento.bind("<KeyRelease>", dadosdatav)
    tela.pagamento.bind("<KeyRelease>", dadosdatap)
    #
    tela.valpagar.bind("<KeyRelease>", dadosvalor)
    tela.valpagar.bind("<FocusOut>",valorout)
    #
    #
    tela.desconto.bind("<KeyRelease>", dadosdesconto)
    tela.desconto.bind("<FocusOut>",descontoout)
    #
    #
    tela.juros.bind("<KeyRelease>", dadosjuros)
    tela.juros.bind("<FocusOut>",jurosout)
    #

    tela.compra.bind("<FocusOut>",verificadatac)
    tela.vencimento.bind("<FocusOut>",verificadatav)
    tela.pagamento.bind("<FocusOut>",verificadatap) 
    tela.tipo.bind("<KeyRelease>", vertipo)  # rastreia as entradas
    #manutencao.bind("<F6>",verfornec(manutencao))
    #manutencao.bind("<F7>", vertipo(manutencao))

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
     #tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
     #tela.tipo.bind("<KeyRelease>", vertipo)  # rastreia as entradas
     #manutencao.bind("<F6>",verfornec(manutencao))
     #manutencao.bind("<F7>", vertipo(manutencao))   
     keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
      
def alteracaocontas():
    
    if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        tela.codigo.focus()
        return
    codigomem=tela.codigo.get() 
    compramem=tela.compra.get()
    vencimentomem=tela.vencimento.get()
    descricaomem=tela.descricao.get()
    pagamentomem=tela.pagamento.get()
    tipomem=tela.tipo.get()
    valpagarmem=tela.valpagar.get()
    descontomem = tela.desconto.get()
    jurosmem = tela.juros.get()
    documentomem=tela.documento.get()
    tparcelamem=tela.tparcela.get()
    csmem=tela.cs.get()
    sqlres= consultacontas()
    if len(sqlres)==0:
      limpacamposcontas()
      tela.codigo.focus()
      return
    if documentomem=="":
      documentomem=tela.documento.get()
    else:
       tela.documento.delete(0, END)
       tela.documento.insert(0, documentomem)
    
    if tparcelamem=="":
       tparcelamem = tela.tparcela.get()
    else:
       tela.tparcela.delete(0, END)
       tela.tparcela.insert(0, tparcelamem)      
    
    if compramem == "":
       compramem = tela.compra.get()
    else:
       tela.compra.delete(0, END)
       tela.compra.insert(0, compramem)

    if vencimentomem == "":
       vencimentomem = tela.vencimento.get()
    else:
        tela.vencimento.delete(0, END)
        tela.vencimento.insert(0, vencimentomem)

    if descricaomem=="":
        descricaomem = tela.descricao.get()
    else:
        tela.descricao.delete(0, END)
        tela.descricao.insert(0, descricaomem)    
    
    if tipomem =="":
        tipomem = tela.tipo.get()
    else:
        tela.tipo.delete(0, END)
        tela.tipo.insert(0, tipomem)

 
    if pagamentomem=="":
        pagamentomem=tela.pagamento.get()
    else:
        tela.pagamento.delete(0, END)    
        tela.pagamento.insert(0, pagamentomem)

    if valpagarmem =="":
        valpagarmem = tela.valpagar.get()
    else:
        tela.valpagar.delete(0, END)
        tela.valpagar.insert(0, valpagarmem)   

    if descontomem =="":
        descontomem = tela.desconto.get()
    else:
        tela.desconto.delete(0, END)
        tela.desconto.insert(0, descontomem)
    if jurosmem =="":
        jurosmem = tela.juros.get()
    else:
        tela.juros.delete(0, END)
        tela.juros.insert(0, jurosmem)
    if csmem =="":
        csmem = tela.cs.get()
    else:
        tela.cs.delete(0, END)
        tela.cs.insert(0, csmem)                         
   
    if len(compramem)==0:
        messagebox1("Informação: digite data da compra",manutencao)
        tela.compra.focus()
        return
    elif len(documentomem)==0 or len(documentomem)>20: 
        messagebox1("Informação: documento esta vazio ou é maior que 20",manutencao)
        tela.documento.focus()
        return
    elif len(tparcelamem)==0 or len(tparcelamem)>3:
        messagebox1("Informação: digite a parcela esta vazio ou é maior que 3",manutencao)
        tela.telefone.focus()
        return    
    elif len(vencimentomem)=="":
        messagebox1("Informação: vencimento é data  ",manutencao)
        tela.vencimento.focus()
        return
    elif len(descricaomem) =="" or len(descricaomem)> 50:
        messagebox1("Informação: descrição tamanho até 50",manutencao)
        tela.cep.focus()
        return
    elif  valpagarmem == "" and len(valpagarmem) > 14:
         messagebox1("Valor a pagar tem que ser tamanho até 14 ",manutencao)
         tela.valpagar.focus()
         return
    elif csmem=="" or csmem> 1:
       messagebox1(" (C) compra e (S) serviço tamanho 1 ",manutencao)
       tela.cs.focus()
       return
    elif pagamentomem!="":
        if tipomem !=2:
           messagebox1("Tipo é a Forma de Pagamento e tem tamanho 2 ",manutencao)
           tela.tipo.focus()
           return      
    res = messagebox.askquestion('Confirma Alteração', 'yes para sim - no para não')
    if res == 'yes':
    
      try:
          banco = sqlite3.connect('contaspagar.db')
          cursor = banco.cursor()
          
      except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 1478 "+ str(ex),manutencao)
       limpacamposcontas()   
       tela.codigo.focus()
       return
          

      try:
          

           cursor.execute(f'''UPDATE contas SET codigo = '{codigomem}',
                                                    compra ='{compramem}',
                                                    vencimento ='{vencimentomem}',
                                                    descricao ='{descricaomem}',
                                                    pagamento = '{pagamentomem}',
                                                    tipo = '{tipomem}',
                                                    valpagar = '{valpagarmem}',
                                                    desconto = '{descontomem}',
                                                    juros ='{jurosmem}',
                                                    documento='{documentomem}',
                                                    tparcela='{tparcelamem}',
                                                    cs='{csmem}'
                                                    WHERE codigo = '{codigomem}' ''')
               

                                      
           banco.commit()
           cursor.close()     
           messagebox1("registro Alterado com sucesso",manutencao)
           limpacamposcontas()   
           tela.codigo.focus()
      except Error as ex:
            messagebox("erro ao regravar tabela contas linha 1509"+ str(ex),manutencao)       
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
     tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
     tela.tipo.bind("<KeyRelease>", vertipo)  # rastreia as entradas
     tela.compra.bind("<KeyRelease>", dadosdatac)
     tela.vencimento.bind("<KeyRelease>", dadosdatav)
     tela.pagamento.bind("<KeyRelease>", dadosdatap)

     tela.compra.bind("<FocusOut>",verificadatac)
     tela.vencimento.bind("<FocusOut>",verificadatav)
     tela.pagamento.bind("<FocusOut>",verificadatap)
     #manutencao.bind("<F6>",verfornec(manutencao))
     #manutencao.bind("<F7>", vertipo(manutencao))
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
           cursor.execute(f"DELETE  FROM contas WHERE contas.codigo = '{codigomem}'")
           banco.commit()
           cursor.close()     
           messagebox1("Registro Excluido com sucesso",manutencao)
           limpacamposcontas()   
           tela.codigo.focus()
        except Error as ex:
            messagebox1("erro ao Excluir tabela contas linha 1569"+ str(ex),manutencao)       
            limpacamposcontas() 
       except Error as ex:
           messagebox1("erro ao conectar com banco de dados linha 1572 "+ str(ex),manutencao)
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

def consultacompraopcao():
   tv.delete(*tv.get_children())
   data = datetime.date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   data3= data.strftime("%Y-%m-%d")
   data3=datetime.strptime(data,"%d/%m/%Y")
   data3=str(data3)
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.compra ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.compra DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1505 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1632 "+str(ex),janela4)
        cursor.close() 


def consulta_compra(janela3):
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Compra', 'vencimento','Descrição', 'Pagamento', 'Tipo', 'Descrição do tipo', 'Valor a Pagar', 'Desconto','juros','Documento','Parcela','Compra ou serviço' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('Compra', minwidth=0, width=250)
   tv.column('Vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=30)
   tv.column('Pagamento', minwidth=0, width=100)
   tv.column('Tipo', minwidth=0, width=150)
   tv.column('Descrição do tipo')
   tv.column('Valpagar', minwidth=0, width=100)
   tv.column('Desconto', minwidth=0, width=200)
   tv.column('Juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   
   tv.heading('Codigo', text='CÓDIGO' )
   tv.heading('Nome', text='NOME')
   tv.heading('Compra', text='COMPRA')
   tv.heading('Vencimento', text='VENCIMENTO')
   tv.heading('Descrição', text='DESCRIÇÃO')
   tv.heading('Pagamento', text='PAGAMENTO')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Descrição do Tipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('Valor a Pagar', text='VALOR A PAGAR')
   tv.heading('Desconto', text='DESCONTO')
   tv.heading('Juros', text='JUROS')
   tv.heading('Documento', text='DOCUMENTO')
   tv.heading('Parcela', text='PARCELADO')
   tv.heading('Compra ou Serviço', text='COMPRA OU SEVIÇO') 
 
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
   janela4.bind("<F3>", consultacompraopcao)
        
def consultapagopcao2():
   tv.delete(*tv.get_children())
   data = datetime.date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   data3= data.strftime("%Y-%m-%d")
   data3=datetime.strptime(data,"%d/%m/%Y")
   data3=str(data3)
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.pagamento ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.pagamento DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1613 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1740 "+str(ex),janela4)
        cursor.close() 

def consulta_pagamento(janela3):
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Compra', 'vencimento','Descrição', 'Pagamento', 'Tipo', 'Descrição do tipo', 'Valor a Pagar', 'Desconto','juros','Documento','Parcela','Compra ou serviço' ), show= 'headings')

    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('Compra', minwidth=0, width=250)
   tv.column('Vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=30)
   tv.column('Pagamento', minwidth=0, width=100)
   tv.column('Tipo', minwidth=0, width=150)
   tv.column('Descrição do tipo')
   tv.column('Valpagar', minwidth=0, width=100)
   tv.column('Desconto', minwidth=0, width=200)
   tv.column('Juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   
   tv.heading('Codigo', text='CÓDIGO' )
   tv.heading('Nome', text='NOME')
   tv.heading('Compra', text='COMPRA')
   tv.heading('Vencimento', text='VENCIMENTO')
   tv.heading('Descrição', text='DESCRIÇÃO')
   tv.heading('Pagamento', text='PAGAMENTO')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Descrição do Tipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('Valor a Pagar', text='VALOR A PAGAR')
   tv.heading('Desconto', text='DESCONTO')
   tv.heading('Juros', text='JUROS')
   tv.heading('Documento', text='DOCUMENTO')
   tv.heading('Parcela', text='PARCELADO')
   tv.heading('Compra ou Serviço', text='COMPRA OU SEVIÇO') 
 
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
   janela4.bind("<F3>", consultapagopcao2)


def consultavencopcao2():
   tv.delete(*tv.get_children())
   data = datetime.date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   data3= data.strftime("%Y-%m-%d")
   data3=datetime.strptime(data,"%d/%m/%Y")
   data3=str(data3)
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.vencimento ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo  ORDER BY a.vencimento DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1723 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1850 "+str(ex),janela4)
        cursor.close() 

def consulta_vencimento(janela3):
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Compra', 'vencimento','Descrição', 'Pagamento', 'Tipo', 'Descrição do tipo', 'Valor a Pagar', 'Desconto','juros','Documento','Parcela','Compra ou serviço' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('Compra', minwidth=0, width=250)
   tv.column('Vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=30)
   tv.column('Pagamento', minwidth=0, width=100)
   tv.column('Tipo', minwidth=0, width=150)
   tv.column('Descrição do tipo')
   tv.column('Valpagar', minwidth=0, width=100)
   tv.column('Desconto', minwidth=0, width=200)
   tv.column('Juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   
   tv.heading('Codigo', text='CÓDIGO' )
   tv.heading('Nome', text='NOME')
   tv.heading('Compra', text='COMPRA')
   tv.heading('Vencimento', text='VENCIMENTO')
   tv.heading('Descrição', text='DESCRIÇÃO')
   tv.heading('Pagamento', text='PAGAMENTO')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Descrição do Tipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('Valor a Pagar', text='VALOR A PAGAR')
   tv.heading('Desconto', text='DESCONTO')
   tv.heading('Juros', text='JUROS')
   tv.heading('Documento', text='DOCUMENTO')
   tv.heading('Parcela', text='PARCELADO')
   tv.heading('Compra ou Serviço', text='COMPRA OU SEVIÇO') 
 
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
   janela4.bind("<F3>", consultavencopcao2)     

def consultacodigoopcao2(event):
   tv.delete(*tv.get_children())
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo ORDER BY a.codigo ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo ORDER BY a.codigo DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1947 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1951 "+str(ex),janela4)
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Compra', 'vencimento','Descrição', 'Pagamento', 'Tipo', 'Descrição do tipo', 'Valor a Pagar', 'Desconto','juros','Documento','Parcela','Compra ou serviço' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('Compra', minwidth=0, width=250)
   tv.column('Vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=30)
   tv.column('Pagamento', minwidth=0, width=100)
   tv.column('Tipo', minwidth=0, width=150)
   tv.column('Descrição do tipo')
   tv.column('Valpagar', minwidth=0, width=100)
   tv.column('Desconto', minwidth=0, width=200)
   tv.column('Juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   
   tv.heading('Codigo', text='CÓDIGO' )
   tv.heading('Nome', text='NOME')
   tv.heading('Compra', text='COMPRA')
   tv.heading('Vencimento', text='VENCIMENTO')
   tv.heading('Descrição', text='DESCRIÇÃO')
   tv.heading('Pagamento', text='PAGAMENTO')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Descrição do Tipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('Valor a Pagar', text='VALOR A PAGAR')
   tv.heading('Desconto', text='DESCONTO')
   tv.heading('Juros', text='JUROS')
   tv.heading('Documento', text='DOCUMENTO')
   tv.heading('Parcela', text='PARCELADO')
   tv.heading('Compra ou Serviço', text='COMPRA OU SEVIÇO') 
 
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
   

                     
                        
   
def consutaporcao2():
    tv.delete(*tv.get_children())
    escolhido=escolha.get()   
    escolhido1=escolha1.get()
    try: 
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        try:
         if escolhido == "A" and escolhido1== "N":
            nomemem1= nomemem.get()
            nomemem1=nomemem1+"%"
            cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                       a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                       FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND b.nome LIKE '{nomemem1}' ORDER BY b.nome ASC''')
      
         elif escolhido == "D" and escolhido1=="N":
            nomemem1= nomemem.get()
            nomemem1=nomemem1+"%"
            cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                       a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                       FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND b.nome LIKE '{nomemem1}' ORDER BY b.nome DESC''')
         elif escolhido == "A" and escolhido1=="C":
            codigomem=nomemem.get()
            cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                       a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                       FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.codigo = '{codigomem}' ORDER BY a.codigo ASC''')
            
         else:
            codigomem=nomemem.get()
            cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                       a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                       FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.codigo = '{codigomem}' ORDER BY a.codigo DESC''')

       
                       
         sqlres=cursor.fetchall()
               
          
               
         if len(sqlres) == 0:
                    messagebox1("Não tem dados a mostrar na consulta",janela4)
                    cursor.close()
                    return
         else:
                    for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
                      tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1)) 
 
                    
                    cursor.close()
                    return
        except Error as ex: 
               messagebox1("Erro ao tentar ler o registro linha 2075 "+str(ex),janela4)
               cursor.close()
               return
               
    except Error as ex:
          messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 2080 "+str(ex),janela4)
          cursor.close()
          return 
    
def consulta_porcao2(janela3):
   global janela4 
   global tv 
   global escolhido
   global escolhido1
   global escolha
   global escolha1
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Compra', 'vencimento','Descrição', 'Pagamento', 'Tipo', 'Descrição do tipo', 'Valor a Pagar', 'Desconto','juros','Documento','Parcela','Compra ou serviço' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('Compra', minwidth=0, width=250)
   tv.column('Vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=30)
   tv.column('Pagamento', minwidth=0, width=100)
   tv.column('Tipo', minwidth=0, width=150)
   tv.column('Descrição do tipo')
   tv.column('Valpagar', minwidth=0, width=100)
   tv.column('Desconto', minwidth=0, width=200)
   tv.column('Juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   
   tv.heading('Codigo', text='CÓDIGO' )
   tv.heading('Nome', text='NOME')
   tv.heading('Compra', text='COMPRA')
   tv.heading('Vencimento', text='VENCIMENTO')
   tv.heading('Descrição', text='DESCRIÇÃO')
   tv.heading('Pagamento', text='PAGAMENTO')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Descrição do Tipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('Valor a Pagar', text='VALOR A PAGAR')
   tv.heading('Desconto', text='DESCONTO')
   tv.heading('Juros', text='JUROS')
   tv.heading('Documento', text='DOCUMENTO')
   tv.heading('Parcela', text='PARCELADO')
   tv.heading('Compra ou Serviço', text='COMPRA OU SEVIÇO') 
 
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.yview)

   tv.configure(yscroll=verscrlbar)
  # tv.configure(xscroll=verscrlbar1.set)
   tv.configure(xscroll=verscrlbar1)
   tv.place(relx=0.01,rely=0.1,relwidth=0.97,relheight=0.75)
   verscrlbar.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.75)
   verscrlbar1.place(relx=0.01,rely=0.85,relwidth=0.95,relheight=0.05)
   Label(janela4, text="Entre com parte do nome  ou código:", font=('Arial', 15)).grid(row=1, column=3,sticky=W)   
   nomemem = Entry(janela4,width=50)
   nomemem.grid(row=1, column=4,sticky=W)
   nomemem.focus()
   escolha=StringVar(value="A")
   escolha1=StringVar(value= "N")
   optado= Radiobutton(janela4, text="Ascendente", value="A", variable=escolha)
   optado.grid(row=1, column=3)
   optado1= Radiobutton(janela4, text= "Descendente", value="D", variable=escolha)
   optado1.grid(row=1, column=4)
   escolhido=escolha.get()
   optado3= Radiobutton(janela4, text="Nome", value="N", variable=escolha1)
   optado3.grid(row=1, column=4)
   optado4= Radiobutton(janela4, text= "Código", value="C", variable=escolha1)
   optado4.grid(row=1, column=5)
   escolhido1=escolha1.get()
  # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   janela4.bind("<F3>", consutaporcao2)

def consultaatrasoopcao2():
   tv.delete(*tv.get_children())
   data = datetime.date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   data3= data.strftime("%Y-%m-%d")
   data3=datetime.strptime(data,"%d/%m/%Y")
   data3=str(data3)
   escolhido=escolha.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.vencimento ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.vencimento DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1) in sqlres:
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 2199 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 2203 "+str(ex),janela4)
        cursor.close() 


def consulta_ematraso(janela3):
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
   tv=ttk.Treeview(janela4,columns=('Codigo', 'Nome', 'Compra', 'vencimento','Descrição', 'Pagamento', 'Tipo', 'Descrição do tipo', 'Valor a Pagar', 'Desconto','juros','Documento','Parcela','Compra ou serviço' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('Compra', minwidth=0, width=250)
   tv.column('Vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=30)
   tv.column('Pagamento', minwidth=0, width=100)
   tv.column('Tipo', minwidth=0, width=150)
   tv.column('Descrição do tipo')
   tv.column('Valpagar', minwidth=0, width=100)
   tv.column('Desconto', minwidth=0, width=200)
   tv.column('Juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   
   tv.heading('Codigo', text='CÓDIGO' )
   tv.heading('Nome', text='NOME')
   tv.heading('Compra', text='COMPRA')
   tv.heading('Vencimento', text='VENCIMENTO')
   tv.heading('Descrição', text='DESCRIÇÃO')
   tv.heading('Pagamento', text='PAGAMENTO')
   tv.heading('Tipo', text='TIPO')
   tv.heading('Descrição do Tipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('Valor a Pagar', text='VALOR A PAGAR')
   tv.heading('Desconto', text='DESCONTO')
   tv.heading('Juros', text='JUROS')
   tv.heading('Documento', text='DOCUMENTO')
   tv.heading('Parcela', text='PARCELADO')
   tv.heading('Compra ou Serviço', text='COMPRA OU SEVIÇO') 
 
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
   janela4.bind("<F3>", consultaatrasoopcao2)


  
  


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
 consultamenu.add_command(label = " Consulta por Compra",command= lambda: consulta_compra(janela3))
 consultamenu.add_command(label = " Consulta por pagamento",command= lambda: consulta_pagamento(janela3))
 consultamenu.add_command(label = " Consulta em atraso",command= lambda: consulta_ematraso(janela3))
 consultamenu.add_command(label = " Consulta por vencimento",command= lambda: consulta_vencimento(janela3))
 consultamenu.add_command(label = " Consulta por Codigo",command=lambda: consulta_codigo2(janela3))
 consultamenu.add_command(label = " consulta por pedaço do nome ou codigo", command=lambda:  consulta_porcao2(janela3))
 menujan2.add_cascade(label = "Consutas diversas", menu = consultamenu)



 editmenu2 = Menu(menujan2, tearoff=0)
 editmenu2.add_command(label = "Nome", command= lambda: rel_nome2(janela3))
 editmenu2.add_command(label = "Compras", command=lambda: rel_compras(janela3))
 editmenu2.add_command(label = "Pagamento", command=lambda: rel_pagamento(janela3))
 editmenu2.add_command(label = "Vencimento", command= lambda: rel_vencimento(janela3))
 editmenu2.add_command(label = "Em atraso", command= lambda: rel_atraso(janela3))
 editmenu2.add_command(label = "Pedaço do nome",command=lambda: rel_nomep2(janela3))
 editmenu2.add_command(label = "Codigo Fornecedor", command= lambda: rel_codigo2(janela3))
 menujan2.add_cascade(label = "Relatórios", menu = editmenu2)

 menusair = Menu(menujan2, tearoff=0)
 menusair.add_command(label= "Sair click aqui", command=janela3.destroy) 
 menujan2.add_cascade(label='para Sair',menu = menusair)

 janela3.config(menu=menujan2) #linha necessaria para aprecer o menu na janela de trabalho
 largura= 550
 altura = 450
 centro=centralizacao(janela3,largura, altura, posx, posy)
 sql='''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5)  NOT NULL, 
                                               compra TEXT NOT NULL, 
                                               vencimento TEXT NOT NULL,
                                               descricao varchar(50),
                                               pagamento TEXT,
                                               tipo integer,
                                               valpagar TEXT NOT NULL,
                                               desconto TEXT,
                                               juros    TEXT,   
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
