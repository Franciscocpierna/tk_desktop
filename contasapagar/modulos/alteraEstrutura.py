import sqlite3
from tkinter import messagebox

# --- Banco de Dados ---
conn = sqlite3.connect('contaspagar.db')
cursor = conn.cursor()

def atualizar_estrutura_banco():
    try:
        # Verifica se a coluna já existe para evitar erro de "duplicate column"
        cursor.execute("PRAGMA table_info(contas)")
        colunas = [info[1] for info in cursor.fetchall()]
        print(colunas)
        if 'inclusao' not in colunas:
            if messagebox.askyesno("Confirmar", "A coluna 'inclusao' não existe. Deseja adicioná-la?"):
                # 1. Adiciona a coluna permitindo valores nulos (ou com um valor padrão estático)
                cursor.execute("ALTER TABLE contas ADD COLUMN inclusao DATE")
                conn.commit() # Salva a primeira alteração
                # 2. Atualiza as linhas antigas com a data de hoje (ou qualquer data padrão)
                cursor.execute("UPDATE contas SET inclusao = DATE('now')")
                conn.commit()
                # --- <--- AQUI É O LOCAL IDEAL PARA O PRINT --- ---
                cursor.execute("PRAGMA table_info(contas)")
                colunas_atualizadas = [info[1] for info in cursor.fetchall()]
                print("Colunas após a alteração:", colunas_atualizadas)
                # ----------------------------------------------- 
                messagebox.showinfo("Sucesso", "Estrutura atualizada com sucesso!")
        else:
            # --- <--- AQUI É O LOCAL IDEAL PARA O PRINT --- ---
            cursor.execute("PRAGMA table_info(contas)")
            colunas_atualizadas = [info[1] for info in cursor.fetchall()]
            print("Colunas após a alteração:", colunas_atualizadas)
            print("A coluna já existe.")
            
    except sqlite3.OperationalError as e:
        messagebox.showerror("Erro ao mudar estrutura", f"Erro no banco de dados: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

# Executa a função
atualizar_estrutura_banco()

conn.close()