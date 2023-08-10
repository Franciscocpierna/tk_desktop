from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4  
import win32print
import win32api
import os


lista_impressoras = win32print.EnumPrinters(2)
impressora = lista_impressoras[2]
#for impressora in lista_impressoras: 
# print(impressora)
#
win32print.SetDefaultPrinter(impressora[2])

# mandar imprimir todos os arquivos de uma pasta
caminho = r"C:\python_projetos\3.11.2\tk_desktop\arquivo"
lista_arquivos = os.listdir(caminho)
#print(lista_arquivos)
# https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
for arquivo in lista_arquivos:
      win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)       

'''
    cnv = canvas.Canvas("rel_nome.pdf", pagesize=A4)
    cnv.setFont('Helvetica', 9)  
    #cnv.drawString(10,830, "teste") # canto superior A4
    cnv.drawString(250,830, "Relatório por nome") # centro do pdf linha superior
    #cnv.drawString(10,810, "codigo  nome                endereço           telefone      CPF             Cnpj           cep        E-mail ") #proxima linha
    eixo = 20
    y= 810
    z=7
    for x in range(40): # para pagina(pesquisar continuar proxima pagina)
        y -= 20
        
      
        cnv.drawString(10,y,"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        y-= 20
        cnv.drawString(10,y, "codigo: 12345 Nome:2345678901234567890123456789012345678901234567890 ")
        y -= 20
        cnv.drawString(10,y, "Endereço: 12345678901234567890123456789012345678901234567890 ")
        y -= 20               
        cnv.drawString(10,y, "Telefone: 12345678901 Cpf:12345678901 Cnpj: 12345678901234 ")               
        y -= 20
        cnv.drawString(10,y, "Cep: 07011-040 E_mail: Chico@hotmail.com12345678901234")
        if x == z:
        
          z += 8 
          y=810
          
          if z <= 39:
          cnv.showPage()
          cnv.setFont('Helvetica', 9)
          cnv.drawString(250,830, "Relatório por nome") # centro do pdf linha superior    
          else:
          if x== 39: 
            cnv.save()

    '''





'''
cnv = canvas.Canvas("rel_nome.pdf", pagesize=A4)
cnv.setFont('Helvetica', 9)  
#cnv.drawString(10,830, "teste") # canto superior A4
cnv.drawString(250,830, "Relatório por nome") # centro do pdf linha superior
#cnv.drawString(10,810, "codigo  nome                endereço           telefone      CPF             Cnpj           cep        E-mail ") #proxima linha
eixo = 20
y= 810
z=7
for x in range(40): # para pagina(pesquisar continuar proxima pagina)
        y -= 20
        cnv.drawString(10,y,"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        y-= 20
        cnv.drawString(10,y, "codigo: 12345 Nome:2345678901234567890123456789012345678901234567890 ")
        y -= 20
        cnv.drawString(10,y, "Endereço: 12345678901234567890123456789012345678901234567890 ")
        y -= 20               
        cnv.drawString(10,y, "Telefone: 12345678901 Cpf:12345678901 Cnpj: 12345678901234 ")               
        y -= 20
        cnv.drawString(10,y, "Cep: 07011-040 E_mail: Chico@hotmail.com12345678901234")
        if x == z:
        
          z += 8 
          y=810
          
          if z <= 7:       #39:
            cnv.showPage()
            cnv.setFont('Helvetica', 9)
            cnv.drawString(250,830, "Relatório por nome") # centro do pdf linha superior    
          else:
           if x== 7:    #39: 
            cnv.save()

'''