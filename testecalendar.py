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

# 1. Pega o objeto de data direto do DateEntry (já validado)
data_objeto = dataini.get_date()

# 2. Converte para string no formato internacional (Ano-Mês-Dia) que o SQLite ama
data_para_sql = data_objeto.strftime('%Y-%m-%d')
print(data_para_sql)

#para jogar para um campo entry do tkinter  para evitar sujeira(espaço adicional)
# Pega o texto que está no Entry comum
# texto_do_entry = meu_entry.get().strip()

# # Verifica se está vazio (para salvar como NULL se necessário)
# if not texto_do_entry:
#     data_para_banco = None
# else:
#     # O .strip() já tira a "sujeira" de espaços nas pontas.
#     # Se você tem certeza que o formato ali dentro é 'YYYY-MM-DD', pode usar:
#     data_para_banco = texto_do_entry
root.mainloop()