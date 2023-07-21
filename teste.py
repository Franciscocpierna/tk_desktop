'''from tkinter import *
#o meu widgets
class framenome(Frame):
    def __init__(self, janela,texto):
      super().__init__()
      self['height'] =150
      self['width'] = 200
      self['bd'] = 2
      self['relief']= SOLID
        
      label_nome = Label(self,text=texto)
      text_nome = Entry(self)
      label_nome.grid(row=0,column=0)
      text_nome.grid(row=0, column=1)
#027
janela = Tk()
janela.title("App")
frame_nome_1=framenome(janela,"texto1").grid()
frame_nome_2=framenome(janela,"texto2").grid()
frame_nome_3=framenome(janela,"texto3").grid()
frame_nome_4=framenome(janela,"texto4").grid()




mainloop()
'''
'''#from tkinter import *
window = Tk()
window.geometry("400x400")
l1 = Label(window, text="Hello, world!")
#l1.place(x=15, y=20)
l1.grid(row = 0, column = 2, 
        padx = 150, pady = 30) 
window.mainloop()
'''
'''from tkinter import *

janela = Tk()
janela.title("App")
#
# widgets

from tkinter import *
 
def messagebox():
    toplevel = Toplevel(root)
 
    toplevel.title("QUIT")
    toplevel.geometry("300x100")
 
 
    l1=Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="Are you sure you want to Quit")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
 
    b1=Button(toplevel,text="Yes",command=root.destroy,width = 10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2=Button(toplevel,text="No",command=toplevel.destroy,width = 10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")
 
 
root = Tk()
root.geometry("300x200")
root.title("Main Window")
Button(root,text="Quit",command=messagebox,width = 7).pack(pady=80)
 
root.mainloop()
from tkinter import *
 
def messagebox():
    toplevel = Toplevel(root)
 
    toplevel.title("QUIT")
    toplevel.geometry(f"300x100+{root.winfo_x()}+{root.winfo_y()}")
     
 
    l1=Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="Are you sure you want to Quit")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
 
    b1=Button(toplevel,text="Yes",command=root.destroy,width = 10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2=Button(toplevel,text="No",command=toplevel.destroy,width = 10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")
 
 
root = Tk()
root.geometry("300x200")
root.title("Main Window")
Button(root,text="Quit",command=messagebox,width = 7).pack(pady=80)
 
root.mainloop()
'''
'''from tkinter import *
 
def messagebox():
    toplevel = Toplevel(root)
 
    toplevel.title("QUIT")
    toplevel.geometry("300x100")
 
 
    l1=Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="Are you sure you want to Quit")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
 
    b1=Button(toplevel,text="Yes",command=root.destroy,width = 10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2=Button(toplevel,text="No",command=toplevel.destroy,width = 10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")
 
 
root = Tk()
root.geometry("300x200")
root.title("Main Window")
Button(root,text="Quit",command=messagebox,width = 7).pack(pady=80)
 
root.mainloop()
'''

from tkinter import *
 
 
def messagebox():
    toplevel = Toplevel(root)
 
    toplevel.title("QUIT")
    x_position = 300
    y_position = 200
    toplevel.geometry(f"300x100+{x_position}+{y_position}")
 
    l1=Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel, text="Are you sure you want to Quit")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
 
    b1=Button(toplevel, text="Yes", command=root.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2=Button(toplevel, text="No", command=toplevel.destroy, width=10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")
 
 
root = Tk()
root.geometry("300x200")
root.title("Main Window")
Button(root, text="Quit", command=messagebox, width=7).pack(pady=80)
 
root.mainloop()
