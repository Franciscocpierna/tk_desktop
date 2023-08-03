from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from rotinas import *
import sqlite3
from sqlite3 import Error
from time import sleep
from classes import montatela,centralizacao
import keyboard
#from contasapagar import *
largura=1200
altura=650

posx=0
posy=0
X=0
ler=""
opcao=0


def criartabela():
   vererro=""
   try:
     banco = sqlite3.connect('contaspagar.db')
     cursor = banco.cursor()
     
     cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor (codigo varchar(5) PRIMARY KEY NOT NULL, 
                                               nome varchar(50) NOT NULL,
                                               endereco varchar(50) NOT NULL, 
                                               telefone varchar(11),
                                               tipo varchar(1)  NOT NULL,
                                               cpf varchar(11),
                                               cnpj varchar(14),
                                               cep varchar(8),
                                               e_mail varchar(30))''')
     cursor.close() 
   except Error as ex:
     messagebox1(str(ex)+ " linha 35",manutencao)
     limpacamposfor()
     vererro=str(ex)
     return vererro
   return vererro


def verificacodigo():
   vererro=""
   codigomem=tela.codigo.get()
   try:
       banco = sqlite3.connect('contaspagar.db')
       cursor = banco.cursor()
   except Error as ex:
       messagebox1("Erro na conexão com Banco de dados linha 26 "+str(ex),manutencao)
       limpacamposfor()
       vererro=str(ex)
       return vererro
   
   try:
       cursor.execute(f"SELECT * FROM fornecedor WHERE codigo = '{codigomem}'")
       sqlres=cursor.fetchall()
       cursor.close() 
       if len(sqlres) == 0:  
        verdadeiro=False
        return verdadeiro,sqlres
       else:
        verdadeiro=True
        messagebox1("Informação: Registro já existe não pode ser inserido linha 62",manutencao)
        limpacamposfor()
        tela.codigo.focus()
        return verdadeiro,sqlres 
   except Error as ex:
       messagebox1("Erro na leitura da tabela Fornecedor linha 67 "+str(ex),manutencao)
       limpacamposfor()
       vererro=str(ex)
       return vererro

def consultafor():
   vererro=""
   
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
        return 
   try: 
      banco = sqlite3.connect('contaspagar.db')
      cursor = banco.cursor()
      try:
       codigomem=tela.codigo.get()
       cursor.execute(f"SELECT * FROM fornecedor WHERE codigo = '{codigomem}'")
       sqlres=cursor.fetchall()
       
       

       if len(sqlres) == 0:
            messagebox1("Registro não existe linha 101",manutencao)

            tela.codigo.delete(0,END)   
            tela.codigo.focus()
            return vererro,sqlres 
       else:
            tela.nome.insert(0, sqlres[0][1])
            tela.endereco.insert(0,sqlres[0][2])
            tela.telefone.insert(0, sqlres[0][3])
            tela.tipo.insert(0, sqlres[0][4]) 
            tela.cpf.insert(0, sqlres[0][5])
            tela.cnpj.insert(0, sqlres[0][6])
            tela.cep.insert(0, sqlres[0][7])
            tela.e_mail.insert(0, sqlres[0][8])
            print(sqlres[0][1])
      except Error as ex: 
         messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
         limpacamposfor()
         vererro=str(ex)
         
   except Error as ex:
      messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 125 "+str(ex),manutencao)
      limpacamposfor()
      vererro=(str(ex))
   cursor.close()  
   return vererro,sqlres                    
   
    
 
 

def tab_order():
  tela.codigo.focus
  widgets = [tela.codigo,tela.nome,tela.endereco,tela.telefone,tela.tipo,tela.cpf,tela.cnpj,tela.cep,tela.e_mail]
  for w in widgets:
     w.lift()

def limpacamposfor():
  tela.codigo.delete(0,END)
  tela.nome.delete(0,END) 
  tela.endereco.delete(0,END) 
  tela.telefone.delete(0,END)
  tela.tipo.delete(0,END) 
  tela.cpf.delete(0,END)
  tela.cnpj.delete(0,END)
  tela.cep.delete(0,END)
  tela.e_mail.delete(0,END)
  return



def incluirfor():
      
   sqlres="" 
   verdadeiro=False
   ver = criartabela()
   if len(ver) != 0:
      limpacamposfor()
      tela.codigo.focus()
      return
      
   if len(tela.codigo.get())!=5:
        messagebox1("codigo tamanho 5",manutencao)
        tela.codigo.focus()
        return
   else:
        verdadeiro, sqlres =  verificacodigo()
        if verdadeiro == True:
          print(sqlres)
          tela.codigo.focus
          return          
   
   if len(tela.nome.get())==0 or len(tela.nome.get())>50:
     
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 50",manutencao)
        tela.nome.focus()
        return
   elif len(tela.endereco.get())==0 or len(tela.endereco.get())>50: 
        messagebox1("Informação: Endereço esta vazio ou é maior que 50",manutencao)
        tela.endereco.focus()
        return
   elif len(tela.telefone.get())==0 or len(tela.telefone.get())>11:
        messagebox1("Informação: digite o Nome esta vazio ou é maior que 11",manutencao)
        tela.telefone.focus()
        return    
   elif len(tela.tipo.get())!=1 or tela.tipo.get() not in ("F","J", "f", "j"):
        messagebox1("Informação: tipo  tamanho 1 e pessoa (F)isica ou (J)urica",manutencao)
        tela.tipo.focus()
        return        
   else:
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
           cursor.execute(f'''INSERT INTO fornecedor VALUES('{codigomem}','{nomemem}','{enderecomem}',
                                                            '{telefonemem}','{tipomem}','{cpfmem}',
                                                                 '{cnpjmem}','{cepmem}','{e_mailmem}')''')
               

                                      
           banco.commit()
           cursor.close()
           messagebox1("registro Incluido com sucesso",manutencao)     
           limpacamposfor()   
           tela.codigo.focus()
          except Error as ex:
            messagebox1("erro ao gravar tabela Fornecedor linha 219"+ str(ex),manutencao)       
            limpacamposfor()
        else:
           messagebox1("Registro não foi gravado",manutencao)

      except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 225 "+ str(ex),manutencao)
       limpacamposfor()   
       tela.codigo.focus()
      return
   
def incluirfor_click(janela1):
    opcao=1
    opcao1=1
    
    global tela
    global manutencao  
    manutencao = Toplevel() # janela de nível superior
    tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
    botao=Button(manutencao, text='Salvar',command=incluirfor)
    botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
    tab_order()
    tela.codigo.focus()
    keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
             
    
    
    
           
     
def cosultafor_click(janela1):
     opcao=2
     opcao1=1
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consultar',command=consultafor)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     tela.codigo.focus()
     keyboard.on_press_key("esc", lambda _: manutencao.destroy()) 
      
def alteracaofor():
    codigomem=tela.codigo.get()
    nomemem=tela.nome.get()
    enderecomem=tela.endereco.get()
    telefonemem=tela.telefone.get()
    tipomem=tela.tipo.get().upper()
    cpfmem=tela.cpf.get()
    cnpjmem=tela.cnpj.get()
    cepmem=tela.cep.get()
    e_mailmem = tela.e_mail.get()
    if len(codigomem)!=5:
        messagebox1("codigo tamanho 5",manutencao)
        tela.codigo.focus()
        return
          
   
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

    ver, sqlres= consultafor()
    if len(ver) != 0 or len(sqlres)==0:
      limpacamposfor()
      tela.codigo.focus()
      return
    res = messagebox.askquestion('Confirma Alteração', 'yes para sim - no para não')
    if res == 'yes':
    
      try:
          banco = sqlite3.connect('contaspagar.db')
          cursor = banco.cursor()
          
      except Error as ex:
       messagebox1("erro ao conectar com banco de dados linha 307 "+ str(ex),manutencao)
       limpacamposfor()   
       tela.codigo.focus()
       return
          

      try:
           cursor.execute(f'''UPDATE fornecedor SET codigo = '{codigomem}',
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
           limpacamposfor()   
           tela.codigo.focus()
      except Error as ex:
            messagebox("erro ao regravar tabela Fornecedor linha 333"+ str(ex),manutencao)       
            limpacamposfor() 
            return
    else:
           messagebox1("Registro não foi Alterado",manutencao)
           return
    
def alteracaofor_clik(janela1):
     opcao=3
     opcao1=1
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consutar',command=consultafor)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Alterar',command=alteracaofor)
     botao1.grid(row=10, column=1,padx=0,pady=50,sticky=W)
     tab_order()
     tela.codigo.focus()
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
     
      
 
     
      
     
def exclusaofor():
    codigomem=tela.codigo.get()
    ver, sqlres= consultafor()
    if len(ver) != 0 or len(sqlres)==0:
      limpacamposfor()
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
           messagebox("Registro Excluido com sucesso",manutencao)
           limpacamposfor()   
           tela.codigo.focus()
        except Error as ex:
            messagebox1("erro ao Excluir tabela Fornecedor linha 366"+ str(ex),manutencao)       
            limpacamposfor() 
       except Error as ex:
           messagebox1("erro ao conectar com banco de dados linha 343 "+ str(ex),manutencao)
           limpacamposfor()   
           tela.codigo.focus()
           return
    else:
           messagebox1("Registro não foi Excluido",manutencao)      
    return 
def excluirfor_click(janela1): 
     opcao=4
     opcao1=1
     global tela
     global manutencao
     manutencao = Toplevel() # janela de nível superior
     tela = montatela(manutencao,janela1,opcao,posx,posy,largura, altura,opcao1)
     botao=Button(manutencao, text='Consultar',command=consultafor)
     botao.grid(row=10, column=0,padx=0,pady=50,sticky=W)
     botao1=Button(manutencao, text='Excluir',command=exclusaofor)
     botao1.grid(row=10, column=1,padx=0,pady=50,sticky=W)
     keyboard.on_press_key("esc", lambda _: manutencao.destroy())
# consultas

def consulta_nome(janela3):
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
        cursor.execute(f"SELECT *  FROM  fornecedor ORDER BY nome")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",manutencao)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),manutencao)
        cursor.close() 
        
 
def cosulta_cpf(janela3):
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
        cursor.execute(f"SELECT *  FROM  fornecedor ORDER BY cpf")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",manutencao)
            cursor.close()
            return
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
           cursor.close()
           return
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),manutencao)
        cursor.close() 
        return
def consulta_codigo(janela3):
   janela4 = Toplevel()
   janela4.title("Consultas por Codigo ESC para SAIR")
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
        cursor.execute(f"SELECT *  FROM  fornecedor ORDER BY codigo")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",manutencao)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),manutencao)
        cursor.close() 
        

def cosulta_cnpj(janela3):
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
        cursor.execute(f"SELECT *  FROM  fornecedor ORDER BY cnpj")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",manutencao)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),manutencao)
        cursor.close() 
        

def consulta_codigo(janela3):
   janela4 = Toplevel()
   janela4.title("Consultas por Codigo ESC para SAIR")
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
        cursor.execute(f"SELECT *  FROM  fornecedor ORDER BY codigo")
        sqlres=cursor.fetchall()
     
    
         
        if len(sqlres) == 0:
            messagebox1("Não tem dados a mostrar na consulta",manutencao)
            cursor.close()
            
        else:
            for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
               tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               
      except Error as ex: 
           messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
           cursor.close()
           
   except Error as ex:
        messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),manutencao)
        cursor.close() 
        
   
def tecla_obtida(teclado):
    teclado=True
    return teclado  

def consulta_porcao(janela3):
   
   janela4 = Toplevel()
   janela4.title("Consultas por pedaços de Nomes ESC para SAIR")
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
   teclado=False
   Label(janela4, text="Entre com parte do nome:", font=('Arial', 15)).grid(row=1, column=3,sticky=W)   
   nomemem = Entry(janela4,width=50)
   nomemem.grid(row=1, column=4,sticky=W)
   nomemem.focus()
   keyboard.on_press_key("f3", lambda _: tecla_obtida(teclado))
      
   if teclado:   
     try: 
         banco = sqlite3.connect('contaspagar.db')
         cursor = banco.cursor()
         try:
          cursor.execute(f"SELECT *  FROM  fornecedor ORDER BY nome WHERE nome LIKE '{nomemem}'% ")
          sqlres=cursor.fetchall()
          
     
          
          if len(sqlres) == 0:
               messagebox1("Não tem dados a mostrar na consulta",manutencao)
               cursor.close()
               
          else:
               for (c,n,e,t,ti,cp,cn,ce,ema) in sqlres:
                    tv.insert("","end",value=(c,n,e,t,ti,cp,cn,ce,ema)) 
               cursor.close()
                   
         except Error as ex: 
               messagebox1("Erro ao tentar ler o registro linha 88 "+str(ex),manutencao)
               cursor.close()
               
     except Error as ex:
          messagebox1("Erro ao tentar ao conectar com Banco de Dados contaspagar linha 456 "+str(ex),manutencao)
          cursor.close() 
     
     teclado=False 
     

# relatorios
  


def fornecedor_menu(janela1):
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


 filemenu.add_command(label = " Inclusão",command= lambda: incluirfor_click(janela3))
 filemenu.add_command(label = " Consulta",command= lambda: cosultafor_click(janela3))
 filemenu.add_command(label = " Alteração",command=lambda: alteracaofor_clik(janela3))
 filemenu.add_command(label = " Excluir", command=lambda:  excluirfor_click(janela3))
 menujan2.add_cascade(label = "Manutenção", menu = filemenu)


 consultamenu= Menu(menujan2, tearoff=0,)
 consultamenu.add_command(label = " Consulta por nome",command= lambda: consulta_nome(janela3))
 consultamenu.add_command(label = " Consulta por Cnpj",command= lambda: cosulta_cnpj(janela3))
 consultamenu.add_command(label = " Consulta por Cnpj",command= lambda: cosulta_cpf(janela3))
 consultamenu.add_command(label = " Consulta por Codigo",command=lambda: consulta_codigo(janela3))
 consultamenu.add_command(label = " consulta por pedaço do nome", command=lambda:  consulta_porcao(janela3))
 menujan2.add_cascade(label = "Consutas diversas", menu = consultamenu)



 editmenu2 = Menu(menujan2, tearoff=0)
 editmenu2.add_command(label = "nome ")
 editmenu2.add_command(label = "Cnpj/Cpf")
 editmenu2.add_command(label = "pedaço do nome")
 editmenu2.add_command(label = "outros")
 menujan2.add_cascade(label = "Relatórios", menu = editmenu2)

 menusair = Menu(menujan2, tearoff=0)
 menusair.add_command(label= "Sair click aqui", command=janela3.destroy) 
 menujan2.add_cascade(label='para Sair',menu = menusair)

 janela3.config(menu=menujan2) #linha necessaria para aprecer o menu na janela de trabalho
 largura= 550
 altura = 450
 centro=centralizacao(janela3,largura, altura, posx, posy)

 janela3.geometry("%dx%d+%d+%d" % (centro.largura1, centro.altura1, centro.posx, centro.posy))
 keyboard.on_press_key("f1", lambda _: janela3.destroy())
 #janela3.mainloop()

