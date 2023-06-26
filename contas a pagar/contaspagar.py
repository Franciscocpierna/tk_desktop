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
def incluir_click():
  print('incusão') 

janela= Tk()
janela.title("janela principal")
janela.configure(background='Gray')
janela.geometry('1500x1500')


#tela 2

janela1 = Toplevel() # janela de nível superior
janela1.title("janela de trabalho")
#janela1.configure(height= 400)
#janela1.configure(width= 400) 
           
janela1.resizable(False, False) # tamanho fixo             
janela1.transient(janela) # de onde vem a janela
janela1.focus_force() #forçar foco
janela1.grab_set()    # impede que click na janela principal sem fechar janela atiual
#janela1.overrideredirect(True)  

#adicionando menu
menujan = Menu(janela1)

filemenu= Menu(menujan, tearoff=0)
filemenu.add_command(label = "inclusão",command=incluir_click)
filemenu.add_command(label = "consulta")
filemenu.add_command(label = "alteração")
filemenu.add_command(label = "excluir")
filemenu.add_separator()
filemenu.add_command(label='Sair', command=quit)

menujan.add_cascade(label = "Manutenção", menu = filemenu)

editmenu = Menu(menujan, tearoff=0)
editmenu.add_command(label = "copy")
editmenu.add_command(label = "colar")
editmenu.add_command(label = "deletar")
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