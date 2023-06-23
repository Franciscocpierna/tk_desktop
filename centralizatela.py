from tkinter import *
janela = Tk()
janela.title("titulo")
                        #CENTRLIZAR TELAS EM TKINTER
#DIMENSÕES DA JANELA
largura= 400 #1366
altura = 400 #768
#RESOLUÇÃO DO NOSSO SISTEMA
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
print(largura_screen, altura_screen)
posx=largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2
#definir a geometry


janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

mainloop()
