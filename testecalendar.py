import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Teste DateEntry")
root.geometry("500x400") # Garanta que a janela tem um tamanho definido!

# Aumentamos o width para 16 para caber o texto e o botão do calendário com folga
tk.Label(root, text="Data Inicial:", font=('Arial', 9)).place(relx=0.005,rely=0.05)

dataini = DateEntry(root, width=16, background='darkblue',
                    foreground='white', borderwidth=2, 
                    locale='pt_BR', date_pattern='dd/mm/yyyy')
dataini.place(relx=0.15, rely=0.05)

root.mainloop()