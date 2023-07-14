'''
#for n in range(0, 7):
    globals()['strg%s' % n] = 'Hello'
# strg0 = 'Hello', strg1 = 'Hello' ... strg6 = 'Hello'

for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"


print(variable15)
'''


'''name = 'Elon'
exec("%s = %s" % (name,"100"))
Elon = "maria"
print(type(name))
print(Elon)'''
'''from tkinter import *

janela3 = Tk()
janela3.title("FAHRENHEIT PARA CELSIUS")
final = StringVar()

def calcular():
    F=float(textbox1.get())
    C = (F-32)*5/6
    final.set(str(round(C,2)) + ' Graus celsius')

#widgets
label1=Label(janela3,text="Graus Fahrenheit:")
textbox1=Entry(janela3)
button1=Button(janela3,text="Calcular",command=calcular).grid()
label_resultado=Label(janela3,textvariable=final).grid()

# layout
#label1.grid()
textbox1.grid()
#button1.grid()
#label_resultado.grid()

mainloop()
'''