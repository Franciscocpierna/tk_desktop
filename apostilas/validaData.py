import tkinter as tk

# 1. Cria a janela principal da aplicação
root = tk.Tk()
root.title("Validação Estrita de Data")
root.geometry("300x150")

# 2. Define a função que valida a digitação e trava as barras nas posições exatas (DD/MM/AAAA)
def validar_data_estrita(P):
    # 3. Permite que o campo fique totalmente vazio (caso o usuário apague tudo)
    if P == "":
        return True

    # 4. Impede que o usuário digite mais de 10 caracteres (tamanho máximo de DD/MM/AAAA)
    if len(P) > 10:
        return False

    # 5. Percorre cada caractere da string junto com sua respectiva posição (índice 'i')
    for i, c in enumerate(P):
        # 6. Nas posições 2 e 5 (3º e 6º caracteres), o caractere DEVE ser obrigatoriamente uma barra '/'
        if i == 2 or i == 5:
            if c != '/':
                return False
        # 7. Nas demais posições, o caractere DEVE ser obrigatoriamente um número
        else:
            if not c.isdigit():
                return False

    # 8. Se todas as regras de posição e tipo forem atendidas, autoriza a digitação
    return True

# 9. Registra a função Python no motor do Tkinter
vcmd = root.register(validar_data_estrita)

# 10. Cria o campo Entry aplicando a regra em tempo real a cada tecla pressionada ('key')
meu_entry = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'), font=("Arial", 14))
meu_entry.pack(pady=20)

# 11. Insere um texto guia para orientar o usuário
meu_entry.insert(0, "DD/MM/AAAA")

# 12. Inicia o loop da interface gráfica
root.mainloop()
#verificação de data valida


from datetime import datetime
from tkinter import messagebox

def verificar_data_digitada():
    texto_data = meu_entry.get().strip()
    
    try:
        # Valida se é uma data real (ex: rejeita 31/02/2026)
        data_obj = datetime.strptime(texto_data, '%d/%m/%Y')
        messagebox.showinfo("Sucesso", f"Data válida: {data_obj.strftime('%d/%m/%Y')}")
    except ValueError:
        messagebox.showerror("Erro", "A data digitada não é válida ou está incompleta!")
        meu_entry.focus()