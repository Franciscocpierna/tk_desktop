from tkinter import *
from time import sleep
#import awesometkinter as atk
class tela(Frame):
    def __init__(self,janela,texto):
      super().__init__()
      self['height'] = 150
      self['width'] = 200
      self['bd'] = 2
      self['relief']= SOLID
      label_nome = Label(self,text=texto)
      text_nome = Entry(self)
      label_nome.grid(row=0,column=0)
      text_nome.grid(row=0, column=1)
    def get_tela(self):
        return self.x
    
    def set_tela(self,v):
        self.x = v
janela= Tk()
janela.title("janela principal")
frm1=tela(janela,"nome:").grid()
frame2=tela(janela,"endereço").grid()
janela.title="janela principal"
janela.configure(background='Gray')
janela.configure(height= 2000)
janela.configure(width=2000)
janela.mainloop()


'''import Tkinter
root = Tkinter.Tk()
root.configure(background='black') 
root.mainloop()
super().__init__()
      self['height'] =150
      self['width'] = 200
      self['bd'] = 2
      self['relief']= SOLID

      label_nome = Label(self,text=texto)
      text_nome = Entry(self)
      label_nome.grid(row=0,column=0)
      text_nome.grid(row=0, column=1)'''