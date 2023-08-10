#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4  
#import win32print
import win32api
import os
from time import sleep
from rotinas import messagebox1

caminho = r"C:\python_projetos\3.11.2\tk_desktop\arquivo"
lista_arquivos = os.listdir(caminho)

print(lista_arquivos[0])
 # https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
 
win32api.ShellExecute(0, "open", lista_arquivos[0],None, caminho, 0) 
input("Pressione <enter> para encerrar!") 

