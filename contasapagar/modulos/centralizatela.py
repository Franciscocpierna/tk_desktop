


                        #CENTRLIZAR TELAS EM TKINTER
#DIMENSÕES DA JANELA
def centralizacao(janinclusao,largura1, altura1):
   #RESOLUÇÃO DO NOSSO SISTEMA
   largura_screen = janinclusao.winfo_screenwidth()
   altura_screen = janinclusao.winfo_screenheight()
   # print(largura_screen, altura_screen)
   posx=largura_screen/2 - largura1/2
   posy= altura_screen/2 - altura1/2 
   #janela1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
   print(f'a posy = {posy} e a posx = {posx}')
   return  posy, posx  

