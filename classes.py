from tkinter import *

class tela(Frame):
    def __init__(self,**kwargs):
        super().__init__()
        for chave in kwargs:
          self.cordefundo =  'black'

    def get_tela(self):
        return self.x
    
    def set_tela(self,v):
        self.x = v
janela= Tk()
janela1 = Tk()
print(help(Frame))
#jam1=tela(janela)
janela.configure(background='Gray')
janela.configure(height= 2000)
janela.configure(width=2000)
janela1.mainloop()
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