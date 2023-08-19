from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from sqlite3 import Error


  
root = Tk() 
root.geometry("700x700") 
   
w = Label(root, text ='GeeksForGeeks', 
          font = "50")  
banco = sqlite3.connect('contaspagar.db')
cursor = banco.cursor()
tipomem="1C001"
cursor.execute(f"SELECT nome FROM fornecedor WHERE codigo = '{tipomem}'")
sql=cursor.fetchall()
cursor.close()
print(sql)
print(sql[0][0])
w.pack() 
   
 
   
root.mainloop() 