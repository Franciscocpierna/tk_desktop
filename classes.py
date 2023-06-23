from tkinter import *
#import centralizatela

#import awesometkinter as atk
largura=0
altura=0
posx=0
posy=0
#def centraliza(janelac, largura, altura):
 # janela = Tk()
 #janela.title("titulo")
                        #CENTRLIZAR TELAS EM TKINTER
 #DIMENSÕES DA JANELA
 
 #definir a geometry


 
#mainloop()



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
janela.configure(background='Gray')
janela.geometry('1500x1500')


#tela 2

janela1 = Toplevel()
janela1.title("janela de trabalho")
#janela1.configure(height= 400)
#janela1.configure(width= 400)              
janela1.resizable(False, False)              
janela1.transient(janela)
janela1.focus_force()
janela1.grab_set()


#adicionando menu
menujan = Menu(janela1)

filemenu= Menu(menujan)
filemenu.add_command(label = "novo")
filemenu.add_command(label = "inclusao")
filemenu.add_command(label = "consulta")
menujan.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menujan)
editmenu.add_command(label = "mudar um campo")
editmenu.add_command(label = "Alteração")
editmenu.add_command(label = "local")
menujan.add_cascade(label = "Edit", menu = editmenu)
janela1.config(menu=menujan) #linha necessaria para aprecer o menu na janela de trabalho


#centraliza(janela1,400,400)
largura= 400
altura = 400
#RESOLUÇÃO DO NOSSO SISTEMA
largura_screen = janela1.winfo_screenwidth()
altura_screen = janela1.winfo_screenheight()
# print(largura_screen, altura_screen)
posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2 
janela1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
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