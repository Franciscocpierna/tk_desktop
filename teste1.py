from tkinter import *

janela = Tk()
janela.title("App")

Label(janela, text='Usuario:').grid(row=0, sticky=W)
Label(janela, text='Senha:').grid(row=1, sticky=W)
text_usuario= Entry(janela).grid(row=0, column=1)
text_senha = Entry(janela).grid(row=1,column=1)
login = Button(janela, text='login').grid(row=2, column=1,sticky=E)






mainloop()
