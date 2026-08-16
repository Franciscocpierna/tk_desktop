# 1. O seu Treeview original intacto:
tv = ttk.Treeview(janela4, columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'valpagar', 'documento','tparcela','inclusao' ), show= 'headings')

# ... (suas configurações de column e heading aqui) ...

# 2. Suas barras de rolagem
verscrlbar = ttk.Scrollbar(janela4, orient="vertical", command=tv.yview)
verscrlbar1 = ttk.Scrollbar(janela4, orient="horizontal", command=tv.xview)

# 3. Aceleração rápida para as setas do teclado (Esquerda e Direita)
def acelerar_horizontal(event):
    if event.keysym == 'Left':
        tv.xview('scroll', -3, 'units') # Move 3 unidades para a esquerda
        return 'break' # Impede o comportamento padrão super lento
    elif event.keysym == 'Right':
        tv.xview('scroll', 3, 'units')  # Move 3 unidades para a direita
        return 'break'

tv.bind('<Left>', acelerar_horizontal)
tv.bind('<Right>', acelerar_horizontal)


# ou dessa forma


import tkinter as tk
from tkinter import ttk

# 1. Defina essa classe antes de criar a sua treeview (pode colocar logo no início do arquivo)
class AcceleratedTreeview(ttk.Treeview):
    def xview(self, *args):
        # Acelera o scroll horizontal (setas e cliques nas pontas)
        if args and args[0] == 'scroll':
            try:
                multiplier = 30  # Ajuste este valor se quiser mais rápido ou mais devagar
                new_args = args[:1] + (str(multiplier * int(args[1])),) + args[2:]
                return super().xview(*new_args)
            except (ValueError, IndexError):
                pass
        return super().xview(*args)

# 2. Agora sim, aqui você usa exatamente o tv = ttk.Treeview (mas herdando da classe acima)
# Se quiser manter o padrão exato, basta alterar a classe base:
tv = AcceleratedTreeview(janela4, columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'valpagar', 'documento','tparcela','inclusao' ), show= 'headings')

# 3. Suas configurações de colunas continuam idênticas
tv.column('codigo', minwidth=5, width=50)
tv.column('nome', minwidth=0, width=250)
# ... (demais colunas e headings) ...

# 4. As barras de rolagem continuam conectadas normalmente no seu tv
verscrlbar = ttk.Scrollbar(janela4, orient="vertical", command=tv.yview)
verscrlbar1 = ttk.Scrollbar(janela4, orient="horizontal", command=tv.xview)