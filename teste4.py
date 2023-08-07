from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4  

cnv = canvas.Canvas("rel_nome.pdf", pagesize=A4) 
#cnv.drawString(10,830, "teste") # canto superior A4
cnv.drawString(250,830, "Relatório por nome") # centro do pdf linha superior
#cnv.drawString(10,810, "codigo  nome                endereço           telefone      CPF             Cnpj           cep        E-mail ") #proxima linha
eixo = 20
y= 810
for x in range(8): # para pagina(pesquisar continuar proxima pagina)
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
      
cnv.save()