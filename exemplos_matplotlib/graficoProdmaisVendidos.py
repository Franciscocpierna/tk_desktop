import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Cria a janela principal do sistema
root = tk.Tk()
root.title("Exemplo de Gráficos Comerciais - Sistema")  # <--- Corrigido para .title()
root.geometry("900x600")

# Título do Dashboard
lbl_titulo = tk.Label(root, text="Dashboard Gerencial de Vendas", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# Frame principal para organizar os gráficos lado a lado
frame_graficos = tk.Frame(root)
frame_graficos.pack(fill="both", expand=True, padx=10, pady=10)

# ==========================================
# 1. GRÁFICO DE COLUNAS (Top Produtos)
# ==========================================
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Cadeira"]
quantidades = [15, 45, 30, 20, 10]

fig1, ax1 = plt.subplots(figsize=(4, 4))
ax1.bar(produtos, quantidades, color="#3498db")
ax1.set_title("Top 5 Produtos Mais Vendidos", fontsize=10)
ax1.set_ylabel("Quantidade")
ax1.tick_params(axis='x', rotation=15)

canvas1 = FigureCanvasTkAgg(fig1, master=frame_graficos)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5)

# ==========================================
# 2. GRÁFICO DE PIZZA (Formas de Pagamento)
# ==========================================
formas_pagamento = ["Pix", "Cartão Crédito", "Dinheiro", "Boleto"]
valores_pagamento = [50, 30, 12, 8]
cores = ["#2ecc71", "#e74c3c", "#f1c40f", "#9b59b6"]

fig2, ax2 = plt.subplots(figsize=(4, 4))
ax2.pie(valores_pagamento, labels=formas_pagamento, autopct="%1.1f%%", startangle=90, colors=cores)
ax2.set_title("Vendas por Forma de Pagamento", fontsize=10)

canvas2 = FigureCanvasTkAgg(fig2, master=frame_graficos)
canvas2.draw()
canvas2.get_tk_widget().pack(side="right", fill="both", expand=True, padx=5)

# ==========================================
# CORREÇÃO PARA FECHAR CORRETAMENTE
# ==========================================
def fechar_janela():
    plt.close('all')  # Fecha todas as instâncias de figuras abertas do matplotlib
    root.destroy()    # Destroi a janela do Tkinter e encerra o processo

root.protocol("WM_DELETE_WINDOW", fechar_janela)

# Inicia a aplicação
root.mainloop()