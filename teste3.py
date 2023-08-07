from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4  

cnv = canvas.Canvas("rel_nome.pdf", pagesize=A4) 
#cnv.drawString(10,830, "teste") # canto superior A4
cnv.drawString(250,830, "Relatório por nome") # centro do pdf linha superior
cnv.drawString(10,810, "codigo  nome                endereço           telefone      CPF             Cnpj           cep        E-mail ") #proxima linha
eixo = 20
y= 790
for x in range(40):
    cnv.drawString(10,y, '''12345 2345678901234567890123456789012345678901234567890 12345678901234567890123456789012345678901234567890 
                    12345678901   12345678901  12345678901  12345678901234  07011-040  Chico@hotmail.com12345678901234''')
    y -= 20  
cnv.save()