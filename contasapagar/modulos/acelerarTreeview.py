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
# Cria uma classe nova que "herda" todas as funções da Treeview padrão do ttk.
class AcceleratedTreeview(ttk.Treeview):
    
    # Sobrescreve o método de rolagem horizontal (xview) da tabela.
    def xview(self, *args):
        
        # Verifica se o comando enviado é do tipo 'scroll' (gerado por setas ou pelas pontas da barra).
        if args and args[0] == 'scroll':
            try:
                # Define o fator multiplicador para deixar o movimento mais rápido (30x).
                multiplier = 30  
                
                # Modifica o argumento numérico da velocidade multiplicando ele por 30,
                # mantendo a estrutura original que o Tkinter espera receber.
                new_args = args[:1] + (str(multiplier * int(args[1])),) + args[2:]
                
                # Envia os argumentos modificados para a classe original fazer a rolagem rápida.
                return super().xview(*new_args)
                
            # Caso ocorra algum erro na conversão dos argumentos, apenas ignora.
            except (ValueError, IndexError):
                pass
                
        # Se não for um comando de 'scroll' (por exemplo, arrastar a barra com o mouse),
        # executa o comportamento padrão normal da tabela.
        return super().xview(*args)

# 2. Agora sim, aqui você usa exatamente o tv = ttk.Treeview (mas herdando da classe acima)
# Instancia a tabela usando a nova classe personalizada 'AcceleratedTreeview', 
# passando a janela, as colunas e os parâmetros visuais normais.
tv = AcceleratedTreeview(janela4, columns=('codigo', 'nome', 'compra', 'vencimento','descricao', 'pagamento', 'valpagar', 'documento','tparcela','inclusao' ), show= 'headings')

# 3. Suas configurações de colunas continuam idênticas
# Define o tamanho mínimo e a largura padrão da coluna 'codigo'.
tv.column('codigo', minwidth=5, width=50)

# Define o tamanho mínimo e a largura padrão da coluna 'nome'.
tv.column('nome', minwidth=0, width=250)
# ... (demais colunas e headings) ...

# 4. As barras de rolagem continuam conectadas normalmente no seu tv
# Cria a barra de rolagem vertical ligada ao método yview da tabela.
verscrlbar = ttk.Scrollbar(janela4, orient="vertical", command=tv.yview)

# Cria a barra de rolagem horizontal ligada ao método xview da tabela (que agora passa pela nossa classe acelerada).
verscrlbar1 = ttk.Scrollbar(janela4, orient="horizontal", command=tv.xview)