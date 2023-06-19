import tkinter as tk
class tela():
    def __init__(self,**kwargs):
        super().__init__()
        for chave in kwargs:
          self.cordefundo =  'black'

    def get_tela(self):
        return self.x
    
    def set_tela(self,v):
        self.x = v
root= tk()

'''import Tkinter
root = Tkinter.Tk()
root.configure(background='black') 
root.mainloop()'''