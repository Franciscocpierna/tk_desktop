from tkinter import *
#o meu widgets
'''class framenome(Frame):
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




mainloop() '''

#from tkinter import *
window = Tk()
window.geometry("400x400")
l1 = Label(window, text="Hello, world!")
#l1.place(x=15, y=20)
l1.grid(row = 0, column = 2, 
        padx = 150, pady = 30) 
window.mainloop()
