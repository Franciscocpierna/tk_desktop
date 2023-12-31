from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from rotinas import *
import sqlite3
from sqlite3 import Error
from time import sleep
#from classes import montatela,centralizacao,variaveis
from classes import *
import keyboard
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import win32print
import win32api
import os
from datetime import date,datetime
import shutil


largura=1200
altura=650

posx=0
posy=0
X=0
ler=""
#opcao=0
variaveis=variaveis(0,0,0,"")
variaveis1 = variaveis1(0,0)
     
     

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
  tela.cs.delete(0, END)  
  tela.produto.delete(0,END)    
  tela.descproduto.delete(0,END)
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
   data = date.today() 
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
   elif  arquivo=="rel_vencimento.pdf":        
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

   for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
        co=recupdata(co)
        ve=recupdata(ve)
        pg=recupdata(pg)
        vp=recuperaval(vp)
        des=recuperaval(des)
        ju=recuperaval(ju)
        x+=1
        y -= 20
        cnv.drawString(10,y,"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        y-= 20
        cnv.drawString(10,y, "codigo: "+ c+ " Nome: "+ n)
        y -= 20
        cnv.drawString(10,y, "Compra: "+co+" Vencimento: " + ve+" Descrição:"+de) 
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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()
   #escolhido1=escolha1.get()
   escolhido1 = variaveis1.setescolhido1(escolha1.get())
   escolhido1=variaveis1.getescolhido1()
   if dataini.get() !="":
       if datafim.get()=="":
         messagebox1("Data final precisa ser digitada",janela4)
         dataini.delete(0,END)
         return
   if datafim.get() !="":
       if dataini.get()=="":
         messagebox1("Data inicial precisa ser digitada",janela4)
         datafim.delete(0,END)
         return
             
   memini=dataini.get()
   memfim=datafim.get()
      
   memini = memini[6:]+"-"+memini[3:5]+"-"+memini[0:2]
   memfim= memfim[6:]+"-"+memfim[3:5]+"-"+memfim[0:2]   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.vencimento ASC''')
   
        elif escolhido1=="D" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.vencimento DESC''')
        elif escolhido1 == "A" and dataini.get()!="":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento ASC''')  
        
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento DESC''')  

      
        
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
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
 

   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()
   #escolhido1=escolha1.get()
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   escolhido1=variaveis1.getescolhido1()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.pagamento ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.pagamento DESC''')

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            
        else:
           pdfgerado2(sqlres,"rel_pagamento.pdf") #gerar PDF
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
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
#   data1="21/09/2023"
#   data5=  datetime.strptime(data1,"%d/%m/%Y").date()
   if dataini.get() !="":
       if datafim.get()=="":
         messagebox1("Data final precisa ser digitada",janela4)
         dataini.delete(0,END)
         return
   if datafim.get() !="":
       if dataini.get()=="":
         messagebox1("Data inicial precisa ser digitada",janela4)
         datafim.delete(0,END)
         return

   memini=dataini.get()
   memfim=datafim.get()
      
   memini = memini[6:]+"-"+memini[3:5]+"-"+memini[0:2]
   memfim= memfim[6:]+"-"+memfim[3:5]+"-"+memfim[0:2]

   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()
   #escolhido1=escolha1.get()   
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   escolhido1=variaveis1.getescolhido1()
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) < '{data}' ORDER BY a.vencimento ASC''')
   
        elif escolhido1=="D" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) < '{data}' ORDER BY a.vencimento DESC''')
          
        elif escolhido1 == "A" and dataini.get()!="":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento=''  AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento ASC''')  
        
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento DESC''')  

      
        
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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()
   nomemem1= nomemem.get()
   
   #escolhido1=escolha1.get()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      #nomemem1=nomemem1+"%"
      #nome ou codigo
      try:
         nomemem1= nomemem.get()
         nomemem1="%"+nomemem1+"%"
         cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND b.nome LIKE '{nomemem1}' ORDER BY b.nome ASC''')
            
     

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
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   

   #escolhido=escolha.get()
   #escolhido1=escolha1.get()  
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   escolhido=variaveis1.getescolhido() 
   escolhido1=variaveis1.getescolhido1()
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.codigo ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.codigo DESC''')

      
        
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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()
   #escolhido1=escolha1.get()   
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   escolhido1=variaveis1.getescolhido1()
   data = date.today()
    
   ano = data.year
   mes = data.month
   dia = data.day
   

   

   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.compra ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.compra DESC''')

      
        
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta", janela4)
            cursor.close()
            return             
        else:
           pdfgerado2(sqlres,"rel_compras.pdf") #gerar PDF
           if escolhido == "A":
              imprimepdf2("rel_compras.pdf")
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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()
   #escolhido1=escolha1.get()
   escolhido1=variaveis1.setescolhido1(escolha1.get())   
   escolhido1=variaveis1.getescolhido1()
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
  

   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido1 == "A":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY b.nome ASC''')
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY b.nome DESC''')

      
        
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
   #global escolhido
   #global escolhido1
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
   #escolhido1=escolha1.get()
   escolhido1=variaveis1.setescolhido1(escolha1.get())  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   #keyboard.on_press_key("f3", lambda _: gerapdf())
   
   janela4.bind("<F3>", gerapdf)

   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #keyboard.on_press_key("f6", lambda _: moverpdf("rel_nome.pdf"))

def rel_vencimento(janela3):
   global janela4 
   #global escolhido
   #global escolhido1
   global escolha
   global escolha1
   global dataini 
   global datafim

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
   #escolhido1=escolha1.get()
   escolhido1=variaveis1.setescolhido1(escolha1.get())  
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   Label(janela4, text="Data Inicial:", font=('Arial', 9)).place(relx=0.2,rely=0.5)   
   dataini = Entry(janela4,width=15)
   dataini.place(relx=0.32,rely=0.5)
   Label(janela4, text="Data Final:", font=('Arial', 9)).place(relx=0.51,rely=0.5)   
   datafim = Entry(janela4,width=15)
   datafim.place(relx=0.62,rely=0.5)
   dataini.bind("<KeyRelease>", dadosdataini)
   datafim.bind("<KeyRelease>", dadosdatafim)
   dataini.bind("<FocusIn>",vercampos1)
   datafim.bind("<FocusIn>",vercampos1)

   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", gerapdv)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")



def rel_atraso(janela3):
   global janela4 
   #global escolhido
   #global escolhido1
   global escolha
   global escolha1
   global dataini 
   global datafim

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
   #escolhido1=escolha1.get()  
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   Label(janela4, text="Data Inicial:", font=('Arial', 9)).place(relx=0.2,rely=0.5)   
   dataini = Entry(janela4,width=15)
   dataini.place(relx=0.32,rely=0.5)
   Label(janela4, text="Data Final:", font=('Arial', 9)).place(relx=0.51,rely=0.5)   
   datafim = Entry(janela4,width=15)
   datafim.place(relx=0.62,rely=0.5)
   dataini.bind("<KeyRelease>", dadosdataini)
   datafim.bind("<KeyRelease>", dadosdatafim)
   dataini.bind("<FocusIn>",vercampos1)
   datafim.bind("<FocusIn>",vercampos1)

   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", gerapdat)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_compras(janela3):
   global janela4 
   #global escolhido
   #global escolhido1
   global escolha
   global escolha1
   escolha=StringVar(value="D")
   escolha1=StringVar(value="A")
  
   janela4 = Toplevel()
   janela4.title("Relatório por Compra ESC para SAIR  F3 - Gerar relatório")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,600, 500, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   label = Label(janela4,text="Relatório por Compras geração em PDF ",font = ("Arial Bold", 12))
   label.place(relx=0.25, rely=0.2)
   optado2= Radiobutton(janela4, text="Ascendente", value="A", variable=escolha1,font = ("Arial Bold", 9))
   optado2.place(relx=0.2,rely=0.3)
   optado3= Radiobutton(janela4, text= "Descendente", value="D", variable=escolha1)
   optado3.place(relx=0.5,rely=0.3)
   #escolhido1=escolha1.get()  
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", geracompras)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_pagamento(janela3):
   global janela4 
   #global escolhido
   #global escolhido1
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
   optado2= Radiobutton(janela4, text="Ascendente", value="A", variable=escolha1,font = ("Arial Bold", 9))
   optado2.place(relx=0.2,rely=0.3)
   optado3= Radiobutton(janela4, text= "Desacendente", value="D", variable=escolha1)
   optado3.place(relx=0.5,rely=0.3)
   #escolhido1=escolha1.get()  
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: gerapdf3())
   janela4.bind("<F3>", gerapdp)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")

def rel_nomep2(janela3):
   global janela4 
   #global escolhido
   global nomemem
   global escolha
   #global escolhido1

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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  

  # keyboard.on_press_key("f3", lambda _: gerapdf2())
   janela4.bind("<F3>", gerapdf2)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
  
   
def rel_codigo2(janela3):
   global janela4 
   #global escolhido
   #global escolhido1
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
   #escolhido1=escolha1.get()  
   escolhido1=variaveis1.setescolhido1(escolha1.get())
   optado= Radiobutton(janela4, text="Imprimir Gerar PDF", value="A", variable=escolha,font = ("Arial Bold", 9))
   optado.place(relx=0.2,rely=0.4)
   optado1= Radiobutton(janela4, text= "Não Imprimir e Gerar e Abrir PDF", value="D", variable=escolha)
   optado1.place(relx=0.5,rely=0.4)
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   
   #keyboard.on_press_key("f3", lambda _: gerapdf1())
   janela4.bind("<F3>", gerapd1)
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   #shutil.move("caminhoa/arquivo.txt", "caminhob/arquivo.txt")def rel_codigo(janela3):
   




                  
   
    
 
 

def tab_order2():
  tela.codigo.focus
  widgets = [tela.codigo,tela.documento,tela.tparcela,tela.compra,tela.vencimento,tela.descricao,tela.pagamento,tela.tipo,tela.desconto,tela.juros,tela.valpagar,tela.cs,tela.produto]
  for w in widgets:
     w.lift()

def vertipo(event):
   if len(tela.tipo.get())==0 or len(tela.tipo.get())<2:
      return    
   manutencao=variaveis.getmanutencao()
   if len(tela.pagamento.get())!=0:
        if len(tela.pagamento.get())!=10: 
          messagebox1("Informação: Data de pagamento tamanho 10",manutencao)
          tela.pagamento.focus()
          return        
        else:
         if len(tela.tipo.get()) !=2 or tela.tipo.get()=="00":
           messagebox1("Tipo é a Forma que Pagou e tamanho 2 diferente 00 ",manutencao)
           tela.tipo.focus()
           return 
   else:
         if tela.tipo.get()!="00":
            messagebox1("sem Data de pagamento tamanho  tipo igual 00",manutencao)
  
   
   if not tela.tipo.get().isnumeric():
     messagebox1("é necessário preencher nr tipo com numeros e tamanho  2 ",manutencao)
     tela.tipo.delete(0,END)
     tela.tipo.focus()
     return
  
   if len(tela.tipo.get()) > 2:
      messagebox1("é necessário preencher numeros e  tamanho  2 ",manutencao)
      tela.tipo.delete(0,END)
      tela.tipo.focus()
      return

      sqleres=""
   tipomem=tela.tipo.get()
   mensagem= "Tipo"  
   
            
   sql=  f"SELECT nome FROM tipo WHERE codigo = '{tipomem}'"  
   sqlres=lertabela(sql,tipomem,manutencao,mensagem)
   if len(sqlres)==0:
       messagebox.showinfo("","tipo não existe")
       tela.tipo.delete(0,END)
       tela.tipo.focus()
       return
   else:
      tela.desctipo.delete(0,END)
      tela.desctipo.insert(0, sqlres[0][0])
   return


def verfornec(event):
   if len(tela.codigo.get())==1:
       tela.codigo.insert(1, "F")

   if len(tela.codigo.get())!=5:
      return

   sqleres=""
   manutencao=variaveis.getmanutencao()
   opcao=variaveis.getopcao() 
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tem que ter tamanho 5",manutencao)
      
        tela.codigo.focus()
        return
   #
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
   tela.cs.delete(0, END)
   tela.produto.delete(0,END)
   tela.descproduto.delete(0,END)
   #
   codigomem=tela.codigo.get()         
   sql=  f"SELECT nome FROM fornecedor WHERE codigo = '{codigomem}'"  
   mensagem="fornecedor"       
   
   
   sqlres=lertabela(sql,codigomem,manutencao,mensagem,opcao)
   if len(sqlres)==0:
         messagebox1("codigo não existe em fornecedor",manutencao)
         limpacamposcontas()
         tela.codigo.focus()
         return
   tela.nome.insert(0, sqlres[0][0])
   tela.documento.focus()
   return

def verproduto(event):

   if len(tela.produto.get())==0:
      tela.produto.insert(0, "P")

   if len(tela.produto.get())!=5:
      return

   sqleres=""
   manutencao=variaveis.getmanutencao()
   opcao=variaveis.getopcao() 
   if len(tela.produto.get())!=5:
        messagebox1("produto tem que ter tamanho 5",manutencao)
      
        tela.produto.focus()
        return
   #
   
      #
   produtomem=tela.produto.get()         
   sql=  f"SELECT nome FROM produto WHERE codigo = '{produtomem}'"  
   mensagem="Produto"       
   
   
   sqlres=lertabela(sql,produtomem,manutencao,mensagem,opcao)
   if len(sqlres)==0:
         messagebox.showinfo("","produto não existe em Produto")
         #limpacamposcontas()
         tela.produto.delete(0,END)
         tela.descproduto.delete(0,END)
         tela.produto.focus()
         tela.produto.insert(0, "P")
         return
   if tela.descproduto.get()=="": 
      tela.descproduto.insert(0, sqlres[0][0])
   if tela.descricao.get()=="":
     tela.descricao.insert(0, sqlres[0][0])
   tela.codigo.focus()
   return

def verchave(event):
  sqlres=""
  
     
     
  if len(tela.tparcela.get()) == 0:
      return
  if len(tela.tparcela.get()) < 3 and tela.tparcela.get().isnumeric():
     return
  manutencao=variaveis.getmanutencao()
  opcao=variaveis.getopcao() 
  if not tela.tparcela.get().isnumeric():
     messagebox1("é necessário preencher nr parcela com numeros e tamanho  3 ",manutencao)
     tela.tparcela.delete(0,END)
     tela.tparcela.focus()
     return
  
  if len(tela.tparcela.get()) != 3:
      messagebox1("é necessário preencher nr parcela  tamanho  3 ",manutencao)
      tela.tparcela.delete(0,END)
      tela.tparcela.focus()
      return
  
  if len(tela.codigo.get()) !=5:
    messagebox1("tamanho do campo codigo fornecedor  é 5 ",manutencao)
    tela.tparcela.delete(0,END)
    tela.codigo.delete(0,END)
    tela.documento.delete(0,END)
    tela.codigo.focus()
    return  
  
  if len(tela.documento.get())==0 or len(tela.documento.get())>20:
    messagebox1("Informação: digite o Nome esta vazio ou é maior que 20",manutencao)
    tela.tparcela.delete(0,END)
    tela.codigo.delete(0,END)
    tela.documento.delete(0,END)
    tela.codigo.focus()
    return           
  

     
     

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
  tela.cs.delete(0, END)      
  tela.produto.delete(0,END)
  tela.descproduto.delete(0,END)

  codigomem=tela.codigo.get().upper()
  documentomem=tela.documento.get()
  tparcelamem=tela.tparcela.get()
  

  sql=f'''SELECT a.codigo,b.nome,a.documento,a.tparcela,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.codigo = '{codigomem}' AND a.documento = '{documentomem}' AND a.tparcela = '{tparcelamem}' '''
        
  mensagem="Contas"        
  sqlres=lertabela1(sql,codigomem,documentomem,tparcelamem,manutencao,mensagem,opcao)
  if len(sqlres)!=0:
   if opcao ==1:
     messagebox1("Registro já existe não pode ser incluido ",manutencao)
     limpacamposcontas()
     tela.codigo.focus()
     return
   else:
     
     tela.compra.insert(0, recupdata(sqlres[0][4]))
     tela.vencimento.insert(0,recupdata(sqlres[0][5]))
     tela.descricao.insert(0, sqlres[0][6]) 
     tela.pagamento.insert(0, recupdata(sqlres[0][7])) 
     tela.tipo.insert(0, sqlres[0][8])
     tela.desctipo.insert(0, sqlres[0][9])
     tela.valpagar.insert(0, recuperaval(sqlres[0][10]))
     tela.desconto.insert(0, recuperaval(sqlres[0][11]))
     tela.juros.insert(0, recuperaval(sqlres[0][12]))
     tela.cs.insert(0, sqlres[0][13])
     tela.produto.insert(0, sqlres[0][14])
     tela.descproduto.insert(0, sqlres[0][15])
     return
  else:
    if opcao==1:
       if tela.tparcela.get()> "001":
        tparcelamem="001"
        sql=f'''SELECT a.codigo,b.nome,a.documento,a.tparcela,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.codigo = '{codigomem}' AND a.documento = '{documentomem}' AND a.tparcela = '{tparcelamem}' '''
        sqlres=lertabela1(sql,codigomem,documentomem,tparcelamem,manutencao,mensagem,opcao)
        if len(sqlres)!=0:
         tela.compra.insert(0, recupdata(sqlres[0][4]))
         tela.descricao.insert(0, sqlres[0][6])
         tela.cs.insert(0, sqlres[0][13])
         tela.produto.insert(0, sqlres[0][14])
         tela.descproduto.insert(0, sqlres[0][15])
         tela.vencimento.focus()  
         return                   
        else:
          messagebox1("não existe a parcela 001 trocando parcela",manutencao)
          tela.tparcela.delete(0,END)
          tela.tparcela.insert(0, "001")
          tela.compra.focus()
          return   
       else:  
        tela.compra.focus()
       return 
    else:
       limpacamposcontas()
       tela.codigo.focus()
       return

def valores(valor):
   while True:
    if valor.find('.')==-1:
     break
    else:
     valor = valor.replace('.','')
   valor=valor.replace(',','.')  
   return valor

def dataa(datav):
   memdata = datav[6:]+"-"+datav[3:5]+"-"+datav[0:2]
   return memdata


def incluircontas():
   manutencao=variaveis.getmanutencao()   
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return
   if len(tela.documento.get()) ==0:
        messagebox1(" digite documento  ",manutencao)
        limpacamposcontas()
        tela.documento.focus()
        return
   if len(tela.tparcela.get()) != 3:
        messagebox1("parcela tamanho 3 digite ",manutencao)
        limpacamposcontas() 
        tela.tparcela.focus()
        return     
   if len(tela.compra.get())!=10:
      messagebox1("Informação: digite a compra  esta vazio ",manutencao)
      tela.compra.focus()
      return
   if len(tela.vencimento.get())!=10: 
        messagebox1("Informação: Data de Vencimento esta vazio",manutencao)
        tela.vencimento.focus()
        return
       
   if  len(tela.valpagar.get()) == 0  or len(tela.valpagar.get()) > 12:
         messagebox1("Valor a pagar tem que ser tamanho até 12 ",manutencao)
         tela.valpagar.focus()
         return
   if len(tela.pagamento.get())!=0:
        if len(tela.pagamento.get())!=10: 
          messagebox1("Informação: Data de pagamento tamanho 10",manutencao)
          tela.pagamento.focus()
          return        
        else:
         if len(tela.tipo.get()) !=2 or tela.tipo.get()=="00":
           messagebox1("Tipo é a Forma de Pagamento e tem tamanho 2 ",manutencao)
           tela.tipo.focus()
           return 
   if tela.tipo.get()=="":
       tela.tipo.insert(0, "00")
       tela.desctipo.insert(0, "NÃO PREVISTO")  
       

   if len(tela.documento.get())==0 or len(tela.documento.get())>20:
        messagebox1("Informação: digite o DOCUMENTO esta vazio ou é maior que 20",manutencao)
        tela.documento.focus()
        return
   if  not tela.tparcela.get().isnumeric() and tela.tparcela.get()!=3:          
        messagebox1("preencher nr parcela com numeros e tamanho  3 ",manutencao)
        tela.tparcela.delete(0,END)
        tela.tparcela.focus()
        return    
   if "S" not in tela.cs.get().upper(): 
         if "C" not in tela.cs.get().upper():
           messagebox1(" (C) compra e (S) serviço tamanho 1 ",manutencao)
           tela.cs.delete(0, END)
           tela.cs.focus()
           return            
   if len(tela.descricao.get())==0 or len(tela.descricao.get())>50: 
         messagebox1("Falta decrição da compra ou maior 50",manutencao)
         tela.descricao.focus()
         return
   if len(tela.produto.get())==0 or len(tela.produto.get())>5: 
         messagebox1("Falta código do produto",manutencao)
         tela.produto.focus()    
         return 
          
      
   try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        codigomem=tela.codigo.get()
        documentomem=tela.documento.get()
        tparcelamem = tela.tparcela.get()
        compramem=dataa(tela.compra.get())
        vencimentomem= dataa(tela.vencimento.get())
        descricaomem=tela.descricao.get()
        if tela.pagamento.get()!="":
          pagamentomem=dataa(tela.pagamento.get()) 
        else:    
          pagamentomem=tela.pagamento.get()
        tipomem=tela.tipo.get()
        valpagarmem= valores(tela.valpagar.get())
        descontomem = valores(tela.desconto.get())
        jurosmem = valores(tela.juros.get())
        csmem=tela.cs.get().upper()
        produtomem=tela.produto.get()
        if len(tela.pagamento.get())!=0:
         if vencimentomem > pagamentomem:
             tela.vencimento.delete(0, END)
             tela.vencimento.insert(0, tela.pagamento.get())
             vencimentomem=pagamentomem
     

        res = messagebox.askquestion('Confirma Inclusão', 'yes para sim - no para não')
        if res == 'yes':
          try:
       
            banco = sqlite3.connect('contaspagar.db')
            cursor = banco.cursor()
            cursor.execute(f'''INSERT INTO contas VALUES('{codigomem}','{compramem}','{vencimentomem}',
                                                            '{descricaomem}','{pagamentomem}','{tipomem}',
                                                                 '{valpagarmem}','{descontomem}','{jurosmem}',
                                                                 '{documentomem}','{tparcelamem}','{csmem}
                                                                 ','{produtomem}')''')
               
                     
            banco.commit()
            cursor.close()
            messagebox1("registro Incluido com sucesso",manutencao)     
            limpacamposcontas()   
            tela.codigo.focus()
          except Error as ex:
            messagebox1("erro ao gravar tabela contas linha 1062 "+ str(ex),manutencao)       
            limpacamposcontas()
        else:
           messagebox1("Registro não foi gravado",manutencao)

   except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 995 "+ str(ex),manutencao)
       limpacamposcontas()   
       tela.codigo.focus()
       return


def verificadatac(memdata1):

    data2=memdata1.split('/')

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
        manutencao=variaveis.getmanutencao()
        messagebox1("Data Inválida digite novamente",manutencao)
        return valida 
    return valida


def dadosdatac(event):
 indice=len(tela.compra.get())
 if indice==0:
   return
 indice=indice-1
 manutencao=variaveis.getmanutencao()
 
 memdata=tela.compra.get()
 
 if str(indice) in ("0","1","3","4","6","7","8","9"):
    if memdata[indice].isnumeric():
       if indice ==1 or indice ==4:
          memdata=memdata+"/"
          tela.compra.delete(0,END)
          tela.compra.insert(0,memdata)
          return
       elif indice == 9:
           valida=verificadatac(memdata)
           if valida==False:
             tela.compra.delete(0,END) 
             tela.compra.focus()
             return
           else:
             return 
       else:         
           return
    else:
      messagebox1("data tem que ser numerica nessa posição",manutencao) 
      tela.compra.delete(0,END)
      tela.compra.focus()
      return
 
 elif indice==2 or indice==5:
     if memdata[indice] not in ("/"):
         messagebox1("digite barra automatica nesta posição é data",manutencao)
         tela.compra.delete(0,END)
         tela.compra.focus()
         return   
     else:
        return 
   
 if len(tela.compra.get())==0:
      tela.compra.focus()
      return 
 if len(tela.compra.get()) ==1:
    digitado=tela.compra.get()
    if digitado in ("0","1","2","3","4","5","6","7","8","9"):
       return
    else: 
       messagebox1("digite números é data",manutencao)
       tela.compra.delete(0,END)
       tela.compra.focus()   
       return
 if len(tela.compra.get()) ==2:
      memdata=tela.compra.get()
      if memdata.isnumeric():
         memdata=memdata+"/"
         tela.compra.delete(0,END)
         tela.compra.insert(0,memdata)
      else:
         messagebox1("digite números é data",manutencao)
         tela.compra.delete(0,END)
         tela.compra.focus()
         return   
 elif len(tela.compra.get())==5:
         memdata1=tela.compra.get()
         memdata=tela.compra.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           tela.compra.delete(0,END)
           tela.compra.insert(0,memdata1)
           return
         else:
           messagebox1("digite números é data",manutencao)
           tela.compra.delete(0,END)
           tela.compra.focus()   
           return
 elif len(tela.compra.get())==10:
         memdata=tela.compra.get()
         memdata1=memdata
         memdata=tela.compra.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           tela.compra.delete(0,END)
           tela.compra.insert(0,memdata1)
           valida=verificadatac(memdata1)
           if valida==False:
             tela.compra.delete(0,END) 
             tela.compra.focus()   
           return
         else:
           messagebox1("digite números é data",manutencao) 
           tela.compra.delete(0,END)
           tela.compra.focus()   
           return
                    
         
def dadosdatav(event):
 indice=len(tela.vencimento.get())
 if indice==0:
   return
 indice=indice-1
 manutencao=variaveis.getmanutencao() 
 
 memdata=tela.vencimento.get()
 
 if str(indice) in ("0","1","3","4","6","7","8","9"):
    if memdata[indice].isnumeric():
       if indice ==1 or indice ==4:
          memdata=memdata+"/"
          tela.vencimento.delete(0,END)
          tela.vencimento.insert(0,memdata)
          return
       elif indice == 9:
           valida=verificadatac(memdata)
           if valida==False:
             tela.vencimento.delete(0,END) 
             tela.vencimento.focus()
             return
           else:
             return 
       else:         
           return
    else:
      messagebox1("data tem que ser numerica nessa posição",manutencao) 
      tela.vencimento.delete(0,END)
      tela.vencimento.focus()
      return
 
 elif indice==2 or indice==5:
     if memdata[indice] not in ("/"):
         messagebox1("digite barra automatica nesta posição é data",manutencao)
         tela.vencimento.delete(0,END)
         tela.vencimento.focus()
         return   
     else:
        return 
   
 if len(tela.vencimento.get())==0:
      tela.vencimento.focus()
      return 
 if len(tela.vencimento.get()) ==1:
    digitado=tela.vencimento.get()
    if digitado in ("0","1","2","3","4","5","6","7","8","9"):
       return
    else: 
       messagebox1("digite números é data",manutencao)
       tela.vencimento.delete(0,END)
       tela.vencimento.focus()   
       return
 if len(tela.vencimento.get()) ==2:
      memdata=tela.vencimento.get()
      if memdata.isnumeric():
         memdata=memdata+"/"
         tela.vencimento.delete(0,END)
         tela.vencimento.insert(0,memdata)
      else:
         messagebox1("digite números é data",manutencao)
         tela.vencimento.delete(0,END)
         tela.vencimento.focus()
         return   
 elif len(tela.vencimento.get())==5:
         memdata1=tela.vencimento.get()
         memdata=tela.vencimento.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           tela.vencimento.delete(0,END)
           tela.vencimento.insert(0,memdata1)
           return
         else:
           messagebox1("digite números é data",manutencao)
           tela.vencimento.delete(0,END)
           tela.vencimento.focus()   
           return
 elif len(tela.vencimento.get())==10:
         memdata=tela.vencimento.get()
         memdata1=memdata
         memdata=tela.vencimento.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           tela.vencimento.delete(0,END)
           tela.vencimento.insert(0,memdata1)
           valida=verificadatac(memdata1)
           if valida==False:
             tela.vencimento.delete(0,END) 
             tela.vencimento.focus()   
           return
         else:
           messagebox1("digite números é data",manutencao) 
           tela.vencimento.delete(0,END)
           tela.vencimento.focus()   
           return
                    

              
def dadosdatap(event):
 indice=len(tela.pagamento.get())
 if indice==0:
   return
 indice=indice-1

 
 manutencao=variaveis.getmanutencao()
 memdata=tela.pagamento.get()
 
 if str(indice) in ("0","1","3","4","6","7","8","9"):
    if memdata[indice].isnumeric():
       if indice ==1 or indice ==4:
          memdata=memdata+"/"
          tela.pagamento.delete(0,END)
          tela.pagamento.insert(0,memdata)
          return
       elif indice == 9:
           valida=verificadatac(memdata)
           if valida==False:
             tela.pagamento.delete(0,END) 
             tela.pagamento.focus()
             return
           else:
             return 
       else:         
           return
    else:
      messagebox1("data tem que ser numerica nessa posição",manutencao) 
      tela.pagamento.delete(0,END)
      tela.pagamento.focus()
      return
 
 elif indice==2 or indice==5:
     if memdata[indice] not in ("/"):
         messagebox1("digite barra automatica nesta posição é data",manutencao)
         tela.pagamento.delete(0,END)
         tela.pagamento.focus()
         return   
     else:
        return 
   
 if len(tela.pagamento.get())==0:
      tela.pagamento.focus()
      return 
 if len(tela.pagamento.get()) ==1:
    digitado=tela.pagamento.get()
    if digitado in ("0","1","2","3","4","5","6","7","8","9"):
       return
    else: 
       messagebox1("digite números é data",manutencao)
       tela.pagamento.delete(0,END)
       tela.pagamento.focus()   
       return
 if len(tela.pagamento.get()) ==2:
      memdata=tela.pagamento.get()
      if memdata.isnumeric():
         memdata=memdata+"/"
         tela.pagamento.delete(0,END)
         tela.pagamento.insert(0,memdata)
      else:
         messagebox1("digite números é data",manutencao)
         tela.pagamento.delete(0,END)
         tela.pagamento.focus()
         return   
 elif len(tela.pagamento.get())==5:
         memdata1=tela.pagamento.get()
         memdata=tela.pagamento.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           tela.pagamento.delete(0,END)
           tela.pagamento.insert(0,memdata1)
           return
         else:
           messagebox1("digite números é data",manutencao)
           tela.pagamento.delete(0,END)
           tela.pagamento.focus()   
           return
 elif len(tela.pagamento.get())==10:
         memdata=tela.pagamento.get()
         memdata1=memdata
         memdata=tela.pagamento.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           tela.pagamento.delete(0,END)
           tela.pagamento.insert(0,memdata1)
           valida=verificadatac(memdata1)
           if valida==False:
             tela.pagamento.delete(0,END) 
             tela.pagamento.focus()   
           return
         else:
           messagebox1("digite números é data",manutencao) 
           tela.pagamento.delete(0,END)
           tela.pagamento.focus()   
           return
                    





def dadosvalor(event):

   if len(tela.valpagar.get())==0:
      return
   manutencao=variaveis.getmanutencao()
   valpag=tela.valpagar.get()
   if "," in valpag:
     if len(valpag[valpag.find(','):])==1:
       return
     if not valpag[valpag.find(',')+1:].isnumeric():
        messagebox1("valor inválido digite novamente",manutencao)
        tela.valpagar.delete(0,END)
        tela.valpagar.focus()
        return
     if len(valpag[valpag.find(',')+1:]) == 2:
          valpag=tela.valpagar.get()
          valpag1=valorout(valpag)
          tela.valpagar.delete(0,END)
          tela.valpagar.insert(0, valpag1)
     elif len(valpag[valpag.find(',')+1:]) > 2 or len(valpag)>12:
          messagebox1("digite virgula tem que ter 2 casas decimais ou tem mais de 12 digitos",manutencao)
          tela.valpagar.delete(0,END)  
          tela.valpagar.focus()
     return
   else:
      if not valpag.isnumeric():
        messagebox1("valor inválido digite novamente",manutencao)
        tela.valpagar.delete(0,END)
        tela.valpagar.focus()
      return     

def recupdata(data):
   if len(data)==0:
      return data
   data=  data[8:]+"/"+data[5:7]+"/"+data[0:4]
   return data
                   
def recuperaval(valpag):
   valpag=str(valpag)
   valpag1=valpag
   if len(valpag[valpag.find('.')+1:]) == 1:
         valpag=valpag+"0"
   valpag = valpag.replace('.',',')      
   if len(valpag) == 4:
       valpag1=valpag[0]+valpag[1]+valpag[2]+valpag[3]
   elif len(valpag)== 5:
       valpag1=valpag[0]+valpag[1]+valpag[2]+valpag[3]+valpag[4]
   elif len(valpag)==6:
       valpag1=valpag[0]+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]
   elif len(valpag) == 7:
        valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6]
   elif len(valpag) == 8:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]          
   elif len(valpag) == 9:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]
   elif len(valpag) == 10:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+"."+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]
   elif len(valpag) == 11:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+"."+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]
   elif len(valpag) == 12:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+"."+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]+valpag[11]
         
   return valpag1

def valorout(valpag):
   
   if len(valpag) == 4:
       valpag1=valpag[0]+valpag[1]+valpag[2]+valpag[3]
   elif len(valpag)== 5:
       valpag1=valpag[0]+valpag[1]+valpag[2]+valpag[3]+valpag[4]
   elif len(valpag)==6:
       valpag1=valpag[0]+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]
   elif len(valpag) == 7:
        valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6]
   elif len(valpag) == 8:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]          
   elif len(valpag) == 9:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]
   elif len(valpag) == 10:
           valpag1=valpag[0]+"."+valpag[1]+valpag[2]+valpag[3]+"."+valpag[4]+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]
   elif len(valpag) == 11:
           valpag1=valpag[0]+valpag[1]+"."+valpag[2]+valpag[3]+valpag[4]+"."+valpag[5]+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]
   elif len(valpag) == 12:
           valpag1=valpag[0]+valpag[1]+valpag[2]+"."+valpag[3]+valpag[4]+valpag[5]+"."+valpag[6] + valpag[7]+valpag[8]+valpag[9]+valpag[10]+valpag[11]
         
   return valpag1 

def dadosdesconto(event):
   if len(tela.desconto.get())==0:
      return
   manutencao=variaveis.getmanutencao()
   valpag=tela.desconto.get()
   if "," in valpag:
       if len(valpag[valpag.find(','):])==1:
        return

       if not valpag[valpag.find(',')+1:].isnumeric():
        messagebox1("valor inválido digite novamente",manutencao)
        tela.desconto.delete(0,END)
        tela.desconto.focus()
        return
       if len(valpag[valpag.find(',')+1:]) == 2:
          valpag=tela.desconto.get()
          valpag1=valorout(valpag)
          tela.desconto.delete(0,END)
          tela.desconto.insert(0, valpag1)
       elif len(valpag[valpag.find(',')+1:]) > 2 or len(valpag)>12:
          messagebox1("digite virgula tem que ter 2 casas decimais ou tem mais de 12 digitos",manutencao)
          tela.desconto.delete(0,END)  
          tela.desconto.focus()
       return
 
   else:
      if not valpag.isnumeric():
        messagebox1("valor inválido digite novamente",manutencao)
        tela.desconto.delete(0,END)
        return        

def dadosjuros(event):
   if len(tela.juros.get())==0:
      return
   valpag=tela.juros.get()
   manutencao=variaveis.getmanutencao()
   if "," in valpag:
       if len(valpag[valpag.find(','):])==1:
        return

       if not valpag[valpag.find(',')+1:].isnumeric():
        messagebox1("valor inválido digite novamente",manutencao)
        tela.juros.delete(0,END)
        tela.juros.focus()
        return
       if len(valpag[valpag.find(',')+1:]) == 2:
          valpag=tela.juros.get()
          valpag1=valorout(valpag)
          tela.juros.delete(0,END)
          tela.juros.insert(0, valpag1)
       elif len(valpag[valpag.find(',')+1:]) > 2 or len(valpag)>12:
          messagebox1("digite virgula tem que ter 2 casas decimais ou tem mais de 12 digitos",manutencao)
          tela.juros.deletet(0,END)  
          tela.juros.focus()
       return
 
   else:
      if not valpag.isnumeric():
         messagebox1("valor inválido digite novamente",manutencao)
         tela.juros.delete(0,END)
         return        
    

def vercampos(event):
   manutencao=variaveis.getmanutencao()
   if len(tela.codigo.get())!=5:
        messagebox1("campo chave incompleto digite",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return
   if len(tela.documento.get()) ==0:
        messagebox1("campo chave incompleto digite",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return
   if len(tela.tparcela.get()) < 3:
        messagebox1("campo chave incompleto digite",manutencao)
        limpacamposcontas() 
        tela.codigo.focus()
        return
   if len(tela.pagamento.get()) ==10: 
       if len(tela.tipo.get())==0 or len(tela.tipo.get())==1:
        tela.tipo.focus()
        return  
   if len(tela.compra.get())>10:
       messagebox1("campo data tamanho 10 digite novamente",manutencao)
       tela.compra.delete(0,END)
       tela.compra.focus()
   if len(tela.vencimento.get())>10:
       messagebox1("campo data tamanho 10 digite novamente",manutencao)
       tela.vencimento.delete(0,END)
       tela.vencimento.focus()
   if len(tela.pagamento.get())>10:
       messagebox1("campo data tamanho 10 digite novamente",manutencao)
       tela.pagamento.delete(0,END)
       tela.pagamento.focus()
   if len(tela.produto.get())> 5:
       messagebox1("campo produto tamanho 5 digite novamente",manutencao)
       tela.produto.delete(0,END)
       tela.produto.focus() 
  

def incluircontas_click(janela1):
    global tela
    #global manutencao
    global codigomem
    global documentomem
    global tparcelamem
    global flag 
    
    #global opcao
    opcao=variaveis.setopcao(1) 
    opcao1=variaveis.setopcao1(2) 
    opcao=variaveis.getopcao() 
    opcao1=variaveis.getopcao1() 
    #opcao=1
    #opcao1=2 
    codigomem=""
    documentomem=""
    tparcelamem =""
    #manutencao = Toplevel() # janela de nível superior
    manutencao=variaveis.setmanutencao(Toplevel())
    manutencao=variaveis.getmanutencao()
    tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    botao=Button(manutencao, text='Salvar',command=incluircontas)
    botao.grid(row=14, column=0,padx=0,pady=50,sticky=W)
    tab_order2()
    tela.codigo.focus()
    tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
    tela.tparcela.bind("<KeyRelease>", verchave)
    #tela.tparcela.bind("<KeyRelease>", verproduto)
    tela.compra.bind("<KeyRelease>", dadosdatac)
    tela.vencimento.bind("<KeyRelease>", dadosdatav)
    tela.pagamento.bind("<KeyRelease>", dadosdatap)
    tela.valpagar.bind("<KeyRelease>", dadosvalor)
    tela.desconto.bind("<KeyRelease>", dadosdesconto)
    tela.juros.bind("<KeyRelease>", dadosjuros)
    tela.tipo.bind("<KeyRelease>", vertipo)  # rastreia as entradas
    tela.compra.bind("<FocusIn>",vercampos)
    tela.vencimento.bind("<FocusIn>",vercampos)
    tela.valpagar.bind("<FocusIn>",vercampos)
    tela.descricao.bind("<FocusIn>",vercampos)
    tela.pagamento.bind("<FocusIn>",vercampos)
    tela.tipo.bind("<FocusIn>",vercampos)
    tela.desctipo.bind("<FocusIn>",vercampos)
    tela.desconto.bind("<FocusIn>",vercampos)
    tela.juros.bind("<FocusIn>",vercampos)
    tela.cs.bind("<FocusIn>",vercampos)
    tela.produto.bind("<KeyRelease>", verproduto)
    tela.produto.bind("<FocusIn>",vercampos)
    keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
             
    
    
    
           
     
def cosultacontas_click(janela1):
     #global opcao
     global tela
     #global manutencao
     global codigomem
     global documentomem
     global tparcelamem 
     opcao=variaveis.setopcao(2) 
     opcao1=variaveis.setopcao1(2) 
     opcao=variaveis.getopcao() 
     opcao1=variaveis.getopcao1() 
     #opcao=2
     #opcao1=2
     codigomem=""
     documentomem=""
     tparcelamem =""
     #manutencao = Toplevel() # janela de nível superior
     manutencao=variaveis.setmanutencao(Toplevel())
     manutencao=variaveis.getmanutencao()
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     tela.codigo.focus()
     tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
     tela.tparcela.bind("<KeyRelease>", verchave)
     tela.compra.bind("<FocusIn>",vercampos)
     tela.vencimento.bind("<FocusIn>",vercampos)
     tela.valpagar.bind("<FocusIn>",vercampos)
     tela.descricao.bind("<FocusIn>",vercampos)
     tela.pagamento.bind("<FocusIn>",vercampos)
     tela.tipo.bind("<FocusIn>",vercampos)
     tela.desctipo.bind("<FocusIn>",vercampos)
     tela.desconto.bind("<FocusIn>",vercampos)
     tela.juros.bind("<FocusIn>",vercampos)
     tela.cs.bind("<FocusIn>",vercampos) 
     keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
      
def alteracaocontas():
    manutencao=variaveis.getmanutencao()
    if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return
    if len(tela.documento.get()) ==0:
        messagebox1(" digite documento  ",manutencao)
        limpacamposcontas()
        tela.documento.focus()
        return
    if len(tela.tparcela.get()) < 3:
        messagebox1("parcela tamanho 3 digite ",manutencao)
        limpacamposcontas() 
        tela.tparcela.focus()
        return
    

    if len(tela.compra.get())!=10:
      messagebox1("Informação: digite a compra  esta vazio ",manutencao)
      tela.compra.focus()
      return
    if len(tela.vencimento.get())!=10: 
        messagebox1("Informação: Data de Vencimento esta vazio",manutencao)
        tela.vencimento.focus()
        return
    
    if len(tela.pagamento.get())!=0:
        if len(tela.pagamento.get())!=10: 
          messagebox1("Informação: Data de pagamento tamanho 10",manutencao)
          tela.pagamento.focus()
          return        
        else:
         if len(tela.tipo.get()) !=2 or tela.tipo=="00":
           messagebox1("Tipo é a Forma de Pagamento e tem tamanho 2 ",manutencao)
           tela.tipo.focus()
           return 
    
    
    if len(tela.descricao.get()) ==0 or len(tela.descricao.get())> 50:
        messagebox1("Informação: descrição tamanho até 50",manutencao)
        tela.descricao.focus()
        return
    if  len(tela.valpagar.get()) == 0  or len(tela.valpagar.get()) > 12:
         messagebox1("Valor a pagar tem que ser tamanho até 12 ",manutencao)
         tela.valpagar.focus()
         return
    if "S" not in tela.cs.get().upper(): 
         if "C" not in tela.cs.get().upper():
           messagebox1(" (C) compra e (S) serviço tamanho 1 ",manutencao)
           tela.cs.delete(0, END)
           tela.cs.focus()
           return
    if len(tela.pagamento.get())!=0:
        if len(tela.tipo.get()) !=2:
           messagebox1("Tipo é a Forma de Pagamento e tem tamanho 2 ",manutencao)
           tela.tipo.focus()
           return      
     
    if len(tela.produto.get())!=5:
         messagebox1("Produto tamanho 5 ",manutencao)
         tela.produto.focus()
         return 
    
    
    codigomem=tela.codigo.get()
    documentomem=tela.documento.get()
    tparcelamem = tela.tparcela.get()
    compramem=dataa(tela.compra.get()) 
    vencimentomem=dataa(tela.vencimento.get())
    descricaomem=tela.descricao.get()
    if tela.pagamento.get()!="":
          pagamentomem=dataa(tela.pagamento.get()) 
    else:    
          pagamentomem=tela.pagamento.get()
    tipomem=tela.tipo.get()
    valpagarmem=valores(tela.valpagar.get())
    descontomem = valores(tela.desconto.get())
    jurosmem = valores(tela.juros.get())
    csmem=tela.cs.get().upper()
    produtomem=tela.produto.get()
    if len(tela.pagamento.get())!=0:
         if vencimentomem > pagamentomem:
             tela.vencimento.delete(0, END)
             tela.vencimento.insert(0, tela.pagamento.get())
             vencimentomem=pagamentomem
 
    
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
                                                    cs='{csmem}',
                                                    produto='{produtomem}' WHERE codigo = '{codigomem}' AND documento= '{documentomem}' AND tparcela='{tparcelamem}' ''')
               

                                      
           banco.commit()
           cursor.close()     
           messagebox1("registro Alterado com sucesso",manutencao)
           limpacamposcontas()   
           tela.codigo.focus()
      except Error as ex:
            messagebox1("erro ao regravar tabela contas linha 1509"+ str(ex),manutencao)       
            limpacamposcontas() 
            return
    else:
           messagebox1("Registro não foi Alterado",manutencao)
           return
    
def alteracaocontas_click(janela1):
     #global opcao
     global tela
     #global manutencao
     global codigomem
     global documentomem
     global tparcelamem 
     opcao=variaveis.setopcao(3) 
     opcao1=variaveis.setopcao1(2) 
     opcao=variaveis.getopcao() 
     opcao1=variaveis.getopcao1() 
     #opcao=3
     #opcao1=2
     codigomem=""
     documentomem=""
     tparcelamem =""

     #manutencao = Toplevel() # janela de nível superior
     manutencao=variaveis.setmanutencao(Toplevel())
     manutencao=variaveis.getmanutencao()
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     #botao=Button(manutencao, text='Consutar',command=consultacontas)
     #botao.grid(row=13, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Alterar',command=alteracaocontas)
     botao1.grid(row=14, column=1,padx=0,pady=50,sticky=W)
     tab_order2()
     tela.codigo.focus()
     tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
     tela.tparcela.bind("<KeyRelease>", verchave)
     tela.produto.bind("<KeyRelease>",verproduto)
     tela.compra.bind("<KeyRelease>", dadosdatac)
     tela.vencimento.bind("<KeyRelease>", dadosdatav)
     tela.pagamento.bind("<KeyRelease>", dadosdatap)
     tela.valpagar.bind("<KeyRelease>", dadosvalor)
     tela.desconto.bind("<KeyRelease>", dadosdesconto)
     tela.juros.bind("<KeyRelease>", dadosjuros)
     tela.tipo.bind("<KeyRelease>", vertipo)  # rastreia as entradas
     tela.compra.bind("<FocusIn>",vercampos)
     tela.vencimento.bind("<FocusIn>",vercampos)
     tela.valpagar.bind("<FocusIn>",vercampos)
     tela.descricao.bind("<FocusIn>",vercampos)
     tela.pagamento.bind("<FocusIn>",vercampos)
     tela.tipo.bind("<FocusIn>",vercampos)
     tela.desctipo.bind("<FocusIn>",vercampos)
     tela.desconto.bind("<FocusIn>",vercampos)
     tela.juros.bind("<FocusIn>",vercampos)
     tela.cs.bind("<FocusIn>",vercampos)
     tela.produto.bind("<FocusIn>",vercampos)    
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
     
      
 
     
      
     
def exclusaocontas():
   codigomem=tela.codigo.get()
   documentomem=tela.documento.get()
   tparcelamem = tela.tparcela.get()
   manutencao=variaveis.getmanutencao()
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return
   if len(tela.documento.get()) ==0:
        messagebox1(" digite documento  ",manutencao)
        limpacamposcontas()
        tela.codigo.focus()
        return
   if len(tela.tparcela.get()) < 3:
        messagebox1("parcela tamanho 3 digite ",manutencao)
        limpacamposcontas() 
        tela.codigo.focus()
        return
    
   res = messagebox.askquestion('Confirma Exclusão', 'yes para sim - no para não')
   if res == 'yes':
       try:
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        
        try:
           cursor.execute(f"DELETE  FROM contas WHERE codigo = '{codigomem}' AND documento= '{documentomem}' AND tparcela='{tparcelamem}'")
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
     #global opcao
     global codigomem
     global documentomem
     global tparcelamem
     global tela
     #global manutencao
     opcao=variaveis.setopcao(4) 
     opcao1=variaveis.setopcao1(2) 
     opcao=variaveis.getopcao() 
     opcao1=variaveis.getopcao1() 
     #opcao=4
     #opcao1=2
     codigomem=""
     documentomem=""
     tparcelamem =""
     #manutencao = Toplevel() # janela de nível superior
     manutencao=variaveis.setmanutencao(Toplevel())
     manutencao=variaveis.getmanutencao() 
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao1=Button(manutencao, text='Excluir',command=exclusaocontas)
     botao1.grid(row=14, column=0,padx=0,pady=50,sticky=W)
     tela.codigo.bind("<KeyRelease>", verfornec)  # rastreia as entradas
     tela.tparcela.bind("<KeyRelease>", verchave)
     #tela.produto.bind("<KeyRelease>",verproduto)
     tela.compra.bind("<FocusIn>",vercampos)
     tela.vencimento.bind("<FocusIn>",vercampos)
     tela.valpagar.bind("<FocusIn>",vercampos)
     tela.descricao.bind("<FocusIn>",vercampos)
     tela.pagamento.bind("<FocusIn>",vercampos)
     tela.tipo.bind("<FocusIn>",vercampos)
     tela.desctipo.bind("<FocusIn>",vercampos)
     tela.desconto.bind("<FocusIn>",vercampos)
     tela.juros.bind("<FocusIn>",vercampos)
     tela.cs.bind("<FocusIn>",vercampos)
     tela.produto.bind("<FocusIn>",vercampos)
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
# consultas

def consultacompraopcao(event):
   tv.delete(*tv.get_children())
   data = date.today()
   ano = data.year
   mes = data.month
   dia = data.day
   
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get()) 
   escolhido=variaveis1.getescolhido() 
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.compra ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.compra DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
               co=recupdata(co)
               ve=recupdata(ve)
               pg=recupdata(pg)
               vp=recuperaval(vp)
               des=recuperaval(des)
               ju=recuperaval(ju)
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1505 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1632 "+str(ex),janela4)
        cursor.close() 


def consulta_compra(janela3):
   global janela4 
   global tv 
   #global escolhido
   global escolha
   
   janela4 = Toplevel()
   janela4.title("Consultas por Compras ESC para SAIR -  F3 - PARA COSULTAR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'tipo', 'desctipo', 'valpagar', 'desconto','juros','documento','tparcela','cs','produto','descproduto' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('compra', minwidth=0, width=250)
   tv.column('vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=250)
   tv.column('pagamento', minwidth=0, width=100)
   tv.column('tipo', minwidth=0, width=150)
   tv.column('desctipo',minwidth=0, width=250)
   tv.column('valpagar', minwidth=0, width=100)
   tv.column('desconto', minwidth=0, width=200)
   tv.column('juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   tv.column('produto', minwidth=5, width=50)
   tv.column('descproduto',minwidth=0, width=250)
   
   tv.heading('codigo', text='CÓDIGO' )
   tv.heading('nome', text='NOME')
   tv.heading('compra', text='COMPRA')
   tv.heading('vencimento', text='VENCIMENTO')
   tv.heading('descricao', text='DESCRIÇÃO')
   tv.heading('pagamento', text='PAGAMENTO')
   tv.heading('tipo', text='TIPO')
   tv.heading('desctipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('valpagar', text='VALOR A PAGAR')
   tv.heading('desconto', text='DESCONTO')
   tv.heading('juros', text='JUROS')
   tv.heading('documento', text='DOCUMENTO')
   tv.heading('tparcela', text='PARCELADO')
   tv.heading('cs', text='COMPRA OU SEVIÇO') 
   tv.heading('produto', text='PRODUTO' )
   tv.heading('descproduto',text= "DESCRIÇÃO DO PRODUTO")

   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)

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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   janela4.bind("<F3>", consultacompraopcao)
        
def consultapagopcao2(event):
   tv.delete(*tv.get_children())
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   
   #escolhido=escolha.get()  
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido() 
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.pagamento ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.pagamento DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
               co=recupdata(co)
               ve=recupdata(ve)
               pg=recupdata(pg)
               vp=recuperaval(vp)
               des=recuperaval(des)
               ju=recuperaval(ju)
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1613 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1740 "+str(ex),janela4)
        cursor.close() 

def consulta_pagamento(janela3):
   global janela4 
   global tv 
   #global escolhido
   global escolha
   
   
   janela4 = Toplevel()
   janela4.title("Consultas por Pagamento ESC para SAIR -  F3 - PARA COSULTAR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'tipo', 'desctipo', 'valpagar', 'desconto','juros','documento','tparcela','cs','produto','descproduto' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('compra', minwidth=0, width=250)
   tv.column('vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=250)
   tv.column('pagamento', minwidth=0, width=100)
   tv.column('tipo', minwidth=0, width=150)
   tv.column('desctipo',minwidth=0, width=250)
   tv.column('valpagar', minwidth=0, width=100)
   tv.column('desconto', minwidth=0, width=200)
   tv.column('juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   tv.column('produto', minwidth=5, width=50)
   tv.column('descproduto',minwidth=0, width=250)
   
   tv.heading('codigo', text='CÓDIGO' )
   tv.heading('nome', text='NOME')
   tv.heading('compra', text='COMPRA')
   tv.heading('vencimento', text='VENCIMENTO')
   tv.heading('descricao', text='DESCRIÇÃO')
   tv.heading('pagamento', text='PAGAMENTO')
   tv.heading('tipo', text='TIPO')
   tv.heading('desctipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('valpagar', text='VALOR A PAGAR')
   tv.heading('desconto', text='DESCONTO')
   tv.heading('juros', text='JUROS')
   tv.heading('documento', text='DOCUMENTO')
   tv.heading('tparcela', text='PARCELADO')
   tv.heading('cs', text='COMPRA OU SEVIÇO') 
   tv.heading('produto', text='PRODUTO' )
   tv.heading('descproduto', text="DESCRIÇÃO DO PRODUTO")
 
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)

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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   janela4.bind("<F3>", consultapagopcao2)


def consultavencopcao2(event):
   tv.delete(*tv.get_children())
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   memini=dataini.get()
   memfim=datafim.get()
   if dataini.get() !="":
       if datafim.get()=="":
         messagebox1("Data final precisa ser digitada",janela4)
         dataini.delete(0,END)
         return
   if datafim.get() !="":
       if dataini.get()=="":
         messagebox1("Data inicial precisa ser digitada",janela4)
         datafim.delete(0,END)
         return

      
   memini = memini[6:]+"-"+memini[3:5]+"-"+memini[0:2]
   memfim= memfim[6:]+"-"+memfim[3:5]+"-"+memfim[0:2]
   #   data5=  datetime.strptime(data1,"%d/%m/%Y").date()
   #memini=datetime.strptime(memini,"%Y-%m-%d").date()
   #memfim=datetime.strptime(memfim,"%Y-%m-%d").date()
   #escolhido=escolha.get()  
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido() 
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.vencimento ASC''')
   
        elif escolhido=="D" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo  ORDER BY a.vencimento DESC''')
        elif escolhido == "A" and dataini.get()!="":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento ASC''')  
        
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento DESC''')  
             
        
        sqlres=cursor.fetchall()
     
    
                         
      
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
               co=recupdata(co)
               ve=recupdata(ve)
               pg=recupdata(pg)
               vp=recuperaval(vp)
               des=recuperaval(des)
               ju=recuperaval(ju)
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1723 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1850 "+str(ex),janela4)
        cursor.close() 


def dadosdataini(event):
 indice=len(dataini.get())
 if indice==0:
   return
 indice=indice-1


 memdata=dataini.get()

 if str(indice) in ("0","1","3","4","6","7","8","9"):
    if memdata[indice].isnumeric():
       if indice ==1 or indice ==4:
          memdata=memdata+"/"
          dataini.delete(0,END)
          dataini.insert(0,memdata)
          return
       elif indice == 9:
           valida=verificadatac(memdata)
           if valida==False:
             dataini.delete(0,END) 
             dataini.focus()
             return
           else:
             return 
       else:         
           return
    else:
      messagebox1("data tem que ser numerica nessa posição",janela4) 
      dataini.delete(0,END)
      dataini.focus()
      return
 
 elif indice==2 or indice==5:
     if memdata[indice] not in ("/"):
         messagebox1("digite barra automatica nesta posição é data",janela4)
         dataini.delete(0,END)
         dataini.focus()
         return   
     else:
        return 
   
 if len(dataini.get())==0:
      dataini.focus()
      return 
 if len(tela.dataini.get()) ==1:
    digitado=dataini.get()
    if digitado in ("0","1","2","3","4","5","6","7","8","9"):
       return
    else: 
       messagebox1("digite números é data",janela4)
       dataini.delete(0,END)
       dataini.focus()   
       return
 if len(dataini.get()) ==2:
      memdata=dataini.get()
      if memdata.isnumeric():
         memdata=memdata+"/"
         dataini.delete(0,END)
         dataini.insert(0,memdata)
      else:
         messagebox1("digite números é data",janela4)
         dataini.delete(0,END)
         dataini.focus()
         return   
 elif len(dataini.get())==5:
         memdata1=dataini.get()
         memdata=dataini.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           dataini.delete(0,END)
           dataini.insert(0,memdata1)
           return
         else:
           messagebox1("digite números é data",janela4)
           dataini.delete(0,END)
           dataini.focus()   
           return
 elif len(dataini.get())==10:
         memdata=dataini.get()
         memdata1=memdata
         memdata=dataini.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           dataini.delete(0,END)
           dataini.insert(0,memdata1)
           valida=verificadatac(memdata1)
           if valida==False:
             dataini.delete(0,END) 
             dataini.focus()   
           return
         else:
           messagebox1("digite números é data",janela4) 
           dataini.delete(0,END)
           dataini.focus()   
           return

def dadosdatafim(event):
 indice=len(datafim.get())
 if indice==0:
   return
 indice=indice-1

 
 memdata=datafim.get()
 
 if str(indice) in ("0","1","3","4","6","7","8","9"):
    if memdata[indice].isnumeric():
       if indice ==1 or indice ==4:
          memdata=memdata+"/"
          datafim.delete(0,END)
          datafim.insert(0,memdata)
          return
       elif indice == 9:
           valida=verificadatac(memdata)
           if valida==False:
             datafim.delete(0,END) 
             datafim.focus()
             return
           else:
             return 
       else:         
           return
    else:
      messagebox1("data tem que ser numerica nessa posição",janela4) 
      datafim.delete(0,END)
      datafim.focus()
      return
 
 elif indice==2 or indice==5:
     if memdata[indice] not in ("/"):
         messagebox1("digite barra automatica nesta posição é data",janela4)
         datafim.delete(0,END)
         datafim.focus()
         return   
     else:
        return 
 if len(datafim.get())==0:
      datafim.focus()
      return 
 if len(datafim.get()) ==1:
    digitado=dataini.get()
    if digitado in ("0","1","2","3","4","5","6","7","8","9"):
       return
    else: 
       messagebox1("digite números é data",janela4)
       datafim.delete(0,END)
       datafim.focus()   
       return
 if len(datafim.get()) ==2:
      memdata=datafim.get()
      if memdata.isnumeric():
         memdata=memdata+"/"
         datafim.delete(0,END)
         datafim.insert(0,memdata)
      else:
         messagebox1("digite números é data",janela4)
         datafim.delete(0,END)
         datafim.focus()
         return   
 elif len(datafim.get())==5:
         memdata1=datafim.get()
         memdata=datafim.get().split('/')
         memdata=memdata[1]
         if memdata[1].isnumeric():
           memdata1=memdata1+"/"
           datafim.delete(0,END)
           datafim.insert(0,memdata1)
           return
         else:
           messagebox1("digite números é data",janela4)
           datafim.delete(0,END)
           datafim.focus()   
           return
 elif len(datafim.get())==10:
         memdata=datafim.get()
         memdata1=memdata
         memdata=datafim.get().split('/')
         memdata=memdata[2]
         if memdata[2].isnumeric():
           datafim.delete(0,END)
           datafim.insert(0,memdata1)
           valida=verificadatac(memdata1)
           if valida==False:
             datafim.delete(0,END) 
             datafim.focus()   
           return
         else:
           messagebox1("digite números é data",janela4) 
           datafim.delete(0,END)
           datafim.focus()   
           return

def vercampos1(event):
  manutencao=variaveis.getmanutencao()
  if len(dataini.get())>10:
       messagebox1("campo data tamanho 10 digite novamente",manutencao)
       dataini.delete(0,END)
       dataini.focus()
  if len(datafim.get())>10:
       messagebox1("campo data tamanho 10 digite novamente",manutencao)
       datafim.delete(0,END)
       datafim.focus()




def consulta_vencimento(janela3):
   global janela4 
   global tv 
   #global escolhido
   global escolha
   global dataini 
   global datafim
   janela4 = Toplevel()
   janela4.title("Consultas por Vencimento ESC para SAIR -  F3 - PARA COSULTAR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   tv=ttk.Treeview(janela4,columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'tipo', 'desctipo', 'valpagar', 'desconto','juros','documento','tparcela','cs','produto','descproduto' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('compra', minwidth=0, width=250)
   tv.column('vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=250)
   tv.column('pagamento', minwidth=0, width=100)
   tv.column('tipo', minwidth=0, width=150)
   tv.column('desctipo',minwidth=0, width=250)
   tv.column('valpagar', minwidth=0, width=100)
   tv.column('desconto', minwidth=0, width=200)
   tv.column('juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   tv.column('produto', minwidth=5, width=50)
   tv.column('descproduto',minwidth=0, width=250)
   
   tv.heading('codigo', text='CÓDIGO' )
   tv.heading('nome', text='NOME')
   tv.heading('compra', text='COMPRA')
   tv.heading('vencimento', text='VENCIMENTO')
   tv.heading('descricao', text='DESCRIÇÃO')
   tv.heading('pagamento', text='PAGAMENTO')
   tv.heading('tipo', text='TIPO')
   tv.heading('desctipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('valpagar', text='VALOR A PAGAR')
   tv.heading('desconto', text='DESCONTO')
   tv.heading('juros', text='JUROS')
   tv.heading('documento', text='DOCUMENTO')
   tv.heading('tparcela', text='PARCELADO')
   tv.heading('cs', text='COMPRA OU SEVIÇO') 
   tv.heading('produto', text='PRODUTO' )
   tv.heading('descproduto', text="DESCRIÇÃO DO PRODUTO")

   Label(janela4, text="Data Inicial:", font=('Arial', 9)).place(relx=0.005,rely=0.05)   
   dataini = Entry(janela4,width=15)
   dataini.place(relx=0.06,rely=0.05)
   Label(janela4, text="Data Final:", font=('Arial', 9)).place(relx=0.17,rely=0.05)   
   datafim = Entry(janela4,width=15)
   datafim.place(relx=0.22,rely=0.05)

   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)

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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   dataini.bind("<KeyRelease>", dadosdataini)
   datafim.bind("<KeyRelease>", dadosdatafim)
   dataini.bind("<FocusIn>",vercampos1)
   datafim.bind("<FocusIn>",vercampos1)
   janela4.bind("<F3>", consultavencopcao2)     

def consultacodigoopcao2(event):
   tv.delete(*tv.get_children())
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
   escolhido=variaveis1.getescolhido()   
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo ORDER BY a.codigo ASC''')
   
        else:
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo ORDER BY a.codigo DESC''')
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
               co=recupdata(co)
               ve=recupdata(ve)
               pg=recupdata(pg)
               vp=recuperaval(vp)
               des=recuperaval(des)
               ju=recuperaval(ju)
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 1947 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 1951 "+str(ex),janela4)
        cursor.close() 
        

def consulta_codigo2(janela3):
   global janela4 
   global tv 
   #global escolhido
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
   tv=ttk.Treeview(janela4,columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'tipo', 'desctipo', 'valpagar', 'desconto','juros','documento','tparcela','cs','produto','descproduto' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('compra', minwidth=0, width=250)
   tv.column('vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=250)
   tv.column('pagamento', minwidth=0, width=100)
   tv.column('tipo', minwidth=0, width=150)
   tv.column('desctipo',minwidth=0, width=250)
   tv.column('valpagar', minwidth=0, width=100)
   tv.column('desconto', minwidth=0, width=200)
   tv.column('juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   tv.column('produto', minwidth=5, width=50)
   tv.column('descproduto',minwidth=0, width=250)
   
   tv.heading('codigo', text='CÓDIGO' )
   tv.heading('nome', text='NOME')
   tv.heading('compra', text='COMPRA')
   tv.heading('vencimento', text='VENCIMENTO')
   tv.heading('descricao', text='DESCRIÇÃO')
   tv.heading('pagamento', text='PAGAMENTO')
   tv.heading('tipo', text='TIPO')
   tv.heading('desctipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('valpagar', text='VALOR A PAGAR')
   tv.heading('desconto', text='DESCONTO')
   tv.heading('juros', text='JUROS')
   tv.heading('documento', text='DOCUMENTO')
   tv.heading('tparcela', text='PARCELADO')
   tv.heading('cs', text='COMPRA OU SEVIÇO') 
   tv.heading('produto', text='PRODUTO' )
   tv.heading('descproduto',text= "DESCRIÇÃO DO PRODUTO")
  
 
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)

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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   janela4.bind("<F3>", consultacodigoopcao2)
   

                     
                        
   
def consutaporcao2(event):
    tv.delete(*tv.get_children())
    
    try: 
        banco = sqlite3.connect('contaspagar.db')
        cursor = banco.cursor()
        try:
            nomemem1= nomemem.get()
            nomemem1="%"+nomemem1+"%"
            cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND b.nome LIKE '{nomemem1}' ORDER BY b.nome ASC''')
      
         
       
                       
            sqlres=cursor.fetchall()
               
          
               
            if len(sqlres) == 0:
                    messagebox1("Não tem dados a mostrar na consulta",janela4)
                    cursor.close()
                    return
            else:
                    for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
                      co=recupdata(co)
                      ve=recupdata(ve)
                      pg=recupdata(pg)
                      vp=recuperaval(vp)
                      des=recuperaval(des)
                      ju=recuperaval(ju)
                      tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp)) 
 
                    
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
   global nomemem
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
   tv=ttk.Treeview(janela4,columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'tipo', 'desctipo', 'valpagar', 'desconto','juros','documento','tparcela','cs','produto','descproduto' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('compra', minwidth=0, width=250)
   tv.column('vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=250)
   tv.column('pagamento', minwidth=0, width=100)
   tv.column('tipo', minwidth=0, width=150)
   tv.column('desctipo',minwidth=0, width=250)
   tv.column('valpagar', minwidth=0, width=100)
   tv.column('desconto', minwidth=0, width=200)
   tv.column('juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   tv.column('produto', minwidth=5, width=50)
   tv.column('descproduto',minwidth=0, width=250)
   
   tv.heading('codigo', text='CÓDIGO' )
   tv.heading('nome', text='NOME')
   tv.heading('compra', text='COMPRA')
   tv.heading('vencimento', text='VENCIMENTO')
   tv.heading('descricao', text='DESCRIÇÃO')
   tv.heading('pagamento', text='PAGAMENTO')
   tv.heading('tipo', text='TIPO')
   tv.heading('desctipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('valpagar', text='VALOR A PAGAR')
   tv.heading('desconto', text='DESCONTO')
   tv.heading('juros', text='JUROS')
   tv.heading('documento', text='DOCUMENTO')
   tv.heading('tparcela', text='PARCELADO')
   tv.heading('cs', text='COMPRA OU SEVIÇO') 
   tv.heading('produto', text='PRODUTO' )
   tv.heading('descproduto', text= "DESCRIÇÃO DO PRODUTO")

   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)

   tv.configure(yscroll=verscrlbar)
  # tv.configure(xscroll=verscrlbar1.set)
   tv.configure(xscroll=verscrlbar1)
   tv.place(relx=0.01,rely=0.1,relwidth=0.97,relheight=0.75)
   verscrlbar.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.75)
   verscrlbar1.place(relx=0.01,rely=0.85,relwidth=0.95,relheight=0.05)
   Label(janela4, text="Entre com parte do nome :", font=('Arial', 15)).grid(row=1, column=3,sticky=W)   
   nomemem = Entry(janela4,width=50)
   nomemem.grid(row=1, column=4,sticky=W)
   nomemem.focus()
   # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   janela4.bind("<F3>", consutaporcao2)

def consultaatrasoopcao2(event):
   tv.delete(*tv.get_children())
   data = date.today() 
   ano = data.year
   mes = data.month
   dia = data.day
   if dataini.get() !="":
       if datafim.get()=="":
         messagebox1("Data final precisa ser digitada",janela4)
         dataini.delete(0,END)
         return
   if datafim.get() !="":
       if dataini.get()=="":
         messagebox1("Data inicial precisa ser digitada",janela4)
         datafim.delete(0,END)
         return

   memini=dataini.get()
   memfim=datafim.get()
      
   memini = memini[6:]+"-"+memini[3:5]+"-"+memini[0:2]
   memfim= memfim[6:]+"-"+memfim[3:5]+"-"+memfim[0:2]
      
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())   
   escolhido=variaveis1.getescolhido()
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
        if escolhido == "A" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) < '{data}' ORDER BY a.vencimento ASC''')
   
        elif escolhido=="D" and dataini.get()=="":
          cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) < '{data}' ORDER BY a.vencimento DESC''')
          
        elif escolhido == "A" and dataini.get()!="":
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento ASC''')  
        
        else:
           cursor.execute(f'''SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs,a.produto,d.nome
                                    FROM  contas a, fornecedor b, tipo c, produto d WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND a.produto = d.codigo AND a.pagamento='' AND strftime("%Y-%m-%d",a.vencimento) >= '{memini}' AND strftime("%Y-%m-%d",a.vencimento) <='{memfim}' ORDER BY a.vencimento DESC''')  
  
        sqlres=cursor.fetchall()
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",janela4)
            cursor.close()
            
        else:
            for (c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp) in sqlres:
               co=recupdata(co)
               ve=recupdata(ve)
               pg=recupdata(pg)
               vp=recuperaval(vp)
               des=recuperaval(des)
               ju=recuperaval(ju)
               tv.insert("","end",value=(c,n,co,ve,de,pg,tp,dt,vp,des,ju,doc,par,cs1,pr,dp)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 2199 "+str(ex),janela4)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 2203 "+str(ex),janela4)
        cursor.close() 


def consulta_ematraso(janela3):
   global janela4 
   global tv 
   #global escolhido
   global escolha
   global dataini 
   global datafim

   janela4 = Toplevel()
   janela4.title("Consultas por Pagamento em atraso ESC para SAIR -  F3 - PARA COSULTAR")
   janela4.resizable(False, False) # tamanho fixo             
   janela4.transient(janela3) # de onde vem a janela
   janela4.focus_force() #forçar foco
   janela4.grab_set()    # impede que click na janela principal sem
   #'1500x1500' 
   centro=centralizacao(janela4,1330, 650, posx, posy)
   janela4.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
   keyboard.on_press_key("esc", lambda _: janela4.destroy())
   

   tv=ttk.Treeview(janela4,columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'tipo', 'desctipo', 'valpagar', 'desconto','juros','documento','tparcela','cs','produto','descproduto' ), show= 'headings')
    
   tv.column('codigo', minwidth=5, width=50)
   tv.column('nome', minwidth=0, width=250)
   tv.column('compra', minwidth=0, width=250)
   tv.column('vencimento', minwidth=9, width=100)
   tv.column('descricao', minwidth=1, width=250)
   tv.column('pagamento', minwidth=0, width=100)
   tv.column('tipo', minwidth=0, width=150)
   tv.column('desctipo',minwidth=0, width=250)
   tv.column('valpagar', minwidth=0, width=100)
   tv.column('desconto', minwidth=0, width=200)
   tv.column('juros', minwidth=0, width=200)
   tv.column('documento', minwidth=0, width=200)
   tv.column('tparcela', minwidth=0, width=200)
   tv.column('cs', minwidth=0, width=200)
   tv.column('produto', minwidth=5, width=50)
   tv.column('descproduto',minwidth=0, width=250)
   
   tv.heading('codigo', text='CÓDIGO' )
   tv.heading('nome', text='NOME')
   tv.heading('compra', text='COMPRA')
   tv.heading('vencimento', text='VENCIMENTO')
   tv.heading('descricao', text='DESCRIÇÃO')
   tv.heading('pagamento', text='PAGAMENTO')
   tv.heading('tipo', text='TIPO')
   tv.heading('desctipo', text='DESCRIÇÃO DO TIPO')
   tv.heading('valpagar', text='VALOR A PAGAR')
   tv.heading('desconto', text='DESCONTO')
   tv.heading('juros', text='JUROS')
   tv.heading('documento', text='DOCUMENTO')
   tv.heading('tparcela', text='PARCELADO')
   tv.heading('cs', text='COMPRA OU SEVIÇO') 
   tv.heading('produto', text='PRODUTO' )
   tv.heading('descproduto', text="DESCRIÇÃO DO PRODUTO")
 
   Label(janela4, text="Data Inicial:", font=('Arial', 9)).place(relx=0.005,rely=0.05)   
   dataini = Entry(janela4,width=15)
   dataini.place(relx=0.06,rely=0.05)
   Label(janela4, text="Data Final:", font=('Arial', 9)).place(relx=0.17,rely=0.05)   
   datafim = Entry(janela4,width=15)
   datafim.place(relx=0.22,rely=0.05)
   verscrlbar = ttk.Scrollbar(janela4,orient ="vertical",command = tv.yview)
   verscrlbar1 = ttk.Scrollbar(janela4,orient ="horizontal",command = tv.xview)

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
   #escolhido=escolha.get()
   escolhido=variaveis1.setescolhido(escolha.get())
  # keyboard.on_press_key("f3", lambda _: consultacodigoopcao())
   janela4.bind("<F3>", consultaatrasoopcao2)
   dataini.bind("<KeyRelease>", dadosdataini)
   datafim.bind("<KeyRelease>", dadosdatafim)
   dataini.bind("<FocusIn>",vercampos1)
   datafim.bind("<FocusIn>",vercampos1)

  
  


def contas_menu(janela1):
 janela3 = Toplevel() # janela de nível superior
 janela3.title("Menu Manutenção - Pagar Consultas Relatorios  F1 - PARA SAIR")
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
 filemenu.add_command(label = " Alteração",command=lambda: alteracaocontas_click(janela3))
 filemenu.add_command(label = " Excluir", command=lambda:  excluircontas_click(janela3))
 menujan2.add_cascade(label = "Manutenção", menu = filemenu)


 consultamenu= Menu(menujan2, tearoff=0,)
 consultamenu.add_command(label = " Consulta por Compra",command= lambda: consulta_compra(janela3))
 consultamenu.add_command(label = " Consulta por pagamento",command= lambda: consulta_pagamento(janela3))
 consultamenu.add_command(label = " Consulta em atraso",command= lambda: consulta_ematraso(janela3))
 consultamenu.add_command(label = " Consulta por vencimento",command= lambda: consulta_vencimento(janela3))
 consultamenu.add_command(label = " Consulta por Codigo",command=lambda: consulta_codigo2(janela3))
 consultamenu.add_command(label = " consulta por pedaço do nome: ", command=lambda:  consulta_porcao2(janela3))
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
                                               tipo varchar(2),
                                               valpagar REAL(14,2) NOT NULL,
                                               desconto REAL(14,2),
                                               juros    REAL(14,2),   
                                               documento varchar(20),
                                               tparcela varchar(3),
                                               cs varchar(1),
                                               produto varchar(5),               
                                               PRIMARY KEY (codigo,documento,tparcela),   
                                               FOREIGN KEY(codigo) REFERENCES  fornecedor(codigo),
                                               FOREIGN KEY(tipo) REFERENCES  tipo(codigo),
                                               FOREIGN KEY(produto) REFERENCES  produto(codigo))'''

 criartabela2(janela3,sql) 
 janela3.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
 keyboard.on_press_key("f1", lambda _: janela3.destroy())
 #janela3.mainloop()
