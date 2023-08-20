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
def comparar_tam(event):
  #s=var_codigo.get()
  #tam=len(s)
  #s1=en_codigo.get()
  #tam1=len(s1)
  print(en_codigo.get())
  if len(en_codigo.get())==4:
    print("chame o nome") 
   
  
root = Tk() 
root.geometry("300x300") 

w = Label(root, text ='Codigo:', 
          font = "50")
w.grid(row=0, column=0)  
#var_codigo = StringVar()
#var_codigo.trace("w", tamanho_codigo)  # rastrear validar
en_codigo = Entry(root, width=7)
en_codigo.grid(row=0, column=1)
en_codigo.bind("<Key>", comparar_tam)  # rastreia as entradas

#banco = sqlite3.connect('contaspagar.db')
#cursor = banco.cursor()
#tipomem="1C001"
#cursor.execute(f"SELECT nome FROM fornecedor WHERE codigo = '{tipomem}'")
#sql=cursor.fetchall()
#cursor.close()
#print(sql)
#print(sql[0][0])

   
 
   
root.mainloop() 