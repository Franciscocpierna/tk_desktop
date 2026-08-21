import tkinter as tk

# 1. Cria a janela principal da aplicação
root = tk.Tk()
root.title("Validação de Campos Diferentes")
root.geometry("350x250")

# 2. Define a função para validar a Data (formato DD/MM/AAAA)
# def validar_data(P):
#     if P == "":
#         return True
#     if len(P) > 10:
#         return False
#     for i, c in enumerate(P):
#         if i == 2 or i == 5:
#             if c != '/':
#                 return False
#         else:
#             if not c.isdigit():
#                 return False
#     return True


def validar_data(P): #essa rotina pra incluir a / sem digitar
  if P == "":
    return True
  if len(P) > 10:
    return False

  # Extrai apenas os números digitados
  numeros = "".join(c for c in P if c.isdigit())

  # Reconstrói a string adicionando a barra após o índice 1 (2º número)
  # e após o índice 3 (4º número)
  novo_P = ""
  for i, c in enumerate(numeros):
    if i == 2 or i == 4:  # Equivalente a somar a barra após o índice 1 e após o 3
      novo_P += "/"
    novo_P += c

  # Atualiza a StringVar e o cursor se o texto formatado for diferente
  if len(novo_P) <= 10 and novo_P != P:
    data_var.set(novo_P)
    entry_data.icursor(len(novo_P))
    return False

  # Validação mantendo as posições das barras em 2 e 5 na string final
  for i, c in enumerate(P):
    if i == 2 or i == 5:
      if c != "/":
        return False
    else:
      if not c.isdigit():
        return False

  return True


# 3. Define a função para validar apenas Números Inteiros (ex: quantidade, ID)
def validar_apenas_numeros(P):
    if P == "":
        return True
    # Verifica se todos os caracteres digitados são números
    return all(c.isdigit() for c in P)

# 4. Registra cada função separadamente no motor do Tkinter
vcmd_data = root.register(validar_data)
vcmd_numero = root.register(validar_apenas_numeros)

# --- PRIMEIRO CAMPO: Data (Usa o validador de data) ---
tk.Label(root, text="Data de Vencimento:", font=("Arial", 10)).pack(pady=(15, 0))
entry_data = tk.Entry(root, validate="key", validatecommand=(vcmd_data, '%P'), font=("Arial", 12))
entry_data.pack(pady=5)
entry_data.insert(0, "DD/MM/AAAA")

# --- SEGUNDO CAMPO: Número (Usa o validador numérico) ---
tk.Label(root, text="Quantidade de Produtos:", font=("Arial", 10)).pack(pady=(10, 0))
entry_qtd = tk.Entry(root, validate="key", validatecommand=(vcmd_numero, '%P'), font=("Arial", 12))
entry_qtd.pack(pady=5)

# 5. Inicia o loop principal da interface gráfica
root.mainloop()



# Não exatamente! Há uma diferença bem importante no funcionamento entre usar o validatecommand e o <KeyRelease> (com bind).

# Veja o que muda na prática:

# 1. validatecommand (O Bloqueador / Pré-validação)
# Quando age: Acontece antes de o caractere aparecer na tela.

# Comportamento: Se a sua função retornar False, o caractere nem chega a ser digitado. O usuário pode ficar esmagando a tecla que for inválida (como uma letra), e o campo simplesmente não vai aceitar.

# 2. <KeyRelease> com .bind() (O Revisor / Pós-validação)
# Quando age: Acontece depois que a tecla já foi solta e o caractere já apareceu na tela.

# Comportamento: Se você usar o <KeyRelease>, a letra ou caractere errado vai ser digitado no campo primeiro, e só depois o seu código vai rodar para checar. Para corrigir, você teria que apagar o caractere via código (o que costuma causar um efeito visual "chato" de o texto piscando ou sumindo sozinho).

# Resumo da diferença:
# validatecommand: Funciona como uma catraca. Ou você passa (digita certo), ou a catraca trava e você nem entra.

# <KeyRelease>: Funciona como um fiscal na saída. O erro entra no campo, e depois o fiscal tenta corrigir.

# Por isso, para impedir que o usuário digite letras onde só deveria ter números e hífens, o validatecommand é muito superior ao <KeyRelease>.