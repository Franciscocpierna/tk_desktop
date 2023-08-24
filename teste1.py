from tkinter import *
#from tkinter import messagebox
#from tkinter import ttk
import sqlite3

from sqlite3 import Error
import keyboard
from tkinter import Tk, ttk, StringVar, END, Entry

#def  tamanho_codigo():
#  s=var_codigo.get()
#  tam=len(s)
 # s1=en_codigo.get()
 # tam1=len(s1)
  #print(tam)
 # print(tam1)
def obter():
  print(en_codigo.get())
  
  

def comparar_tam(event):
  #s=var_codigo.get()
  #tam=len(s)
  #s1=en_codigo.get()
  #tam1=len(s1)
  print(en_codigo.get())
  print(len(en_codigo.get()))
  if len(en_codigo.get())==5:
    print("chame o nome") 
    obter()
  
root = Tk() 
root.geometry("300x300") 

w = Label(root, text ='Codigo:', 
          font = "50")
w.grid(row=0, column=0)  
#var_codigo = StringVar()
#var_codigo.trace("w", tamanho_codigo())  # rastrear validar
en_codigo = Entry(root,width=7)
en_codigo.grid(row=0, column=1)
en_codigo.focus()
#en_codigo.bind("<Key>", comparar_tam)  # rastreia as entradas
en_codigo.bind("<KeyRelease>", comparar_tam)  # rastreia as entradas
#banco = sqlite3.connect('contaspagar.db')
#cursor = banco.cursor()
#tipomem="1C001"
#cursor.execute(f"SELECT nome FROM fornecedor WHERE codigo = '{tipomem}'")
#sql=cursor.fetchall()
#cursor.close()
#print(sql)
#print(sql[0][0])

'''
sql='''CREATE TABLE IF NOT EXISTS contas (codigo varchar(5)  NOT NULL, 
                                               compra TEXT NOT NULL, 
                                               vencimento TEXT not null,
                                               descricao varchar(50),
                                               pagamento TEXT,
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
SELECT a.codigo,b.nome,a.compra,a.vencimento,a.descricao,a.pagamento,
                                    a.tipo,c.nome,a.valpagar,a.desconto,a.juros,a.documento,a.tparcela,a.cs
                                    FROM  contas a, fornecedor b, tipo c WHERE a.codigo = b.codigo AND a.tipo = c.codigo AND pagamento="" AND strftime("%Y-%m-%d", vencimento) < data3 ORDER BY a.pagamento ASC''')
'''   
 
   
root.mainloop() 