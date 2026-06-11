"""
========================================================================
 PROJETO FINAL - APOSTILA TKINTER & CUSTOMTKINTER
 Aplicativo único integrando TODOS os widgets estudados.
 Autor: Apostila Lovable - 2026
========================================================================

Requisitos:
    pip install customtkinter pillow

Execução:
    python projeto_final_tkinter.py

Estrutura (navegável via Sidebar / CTkTabview):
    1. Home           - Apresentação + Labels, Buttons, Images
    2. Formulário     - Entry, Text, Combobox, Spinbox, Radio, Check, Switch, Slider
    3. Listas/Tabela  - Listbox, Treeview, Scrollbar
    4. Canvas/Desenho - Canvas com formas, eventos de mouse
    5. Diálogos       - messagebox, filedialog, colorchooser, Toplevel
    6. Configurações  - Tema (Light/Dark), cores, fontes (CustomTkinter)
========================================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser, font
import customtkinter as ctk
import json
import os

# ------------------------------------------------------------
# Configuração global do CustomTkinter
# ------------------------------------------------------------
ctk.set_appearance_mode("System")          # "Light" | "Dark" | "System"
ctk.set_default_color_theme("blue")        # "blue" | "green" | "dark-blue"


# ============================================================
# APLICATIVO PRINCIPAL
# ============================================================
class AppPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Projeto Final - Tkinter & CustomTkinter")
        self.geometry("1100x680")
        self.minsize(900, 600)

        # Armazenamento de dados em memória (simula banco)
        self.dados_cadastros = []

        # Grid 1x2: sidebar | conteudo
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._construir_sidebar()
        self._construir_area_conteudo()

        # Frames de cada "tela"
        self.frames = {}
        for nome, classe in [
            ("home", TelaHome),
            ("form", TelaFormulario),
            ("lista", TelaListas),
            ("canvas", TelaCanvas),
            ("dialogos", TelaDialogos),
            ("config", TelaConfiguracoes),
        ]:
            frame = classe(self.container, app=self)
            self.frames[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_frame("home")

    # --------------------------------------------------------
    # SIDEBAR (navegação)
    # --------------------------------------------------------
    def _construir_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1)

        titulo = ctk.CTkLabel(
            self.sidebar, text="📚 Apostila\nProjeto Final",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        titulo.grid(row=0, column=0, padx=20, pady=(20, 20))

        botoes = [
            ("🏠  Home",          "home"),
            ("📝  Formulário",    "form"),
            ("📋  Listas/Tabela", "lista"),
            ("🎨  Canvas",        "canvas"),
            ("💬  Diálogos",      "dialogos"),
            ("⚙️  Configurações", "config"),
        ]
        for i, (texto, chave) in enumerate(botoes, start=1):
            btn = ctk.CTkButton(
                self.sidebar, text=texto, anchor="w",
                command=lambda c=chave: self.mostrar_frame(c),
            )
            btn.grid(row=i, column=0, padx=20, pady=6, sticky="ew")

        # Combobox para mudar tema rapidamente
        modo_lbl = ctk.CTkLabel(self.sidebar, text="Aparência:", anchor="w")
        modo_lbl.grid(row=11, column=0, padx=20, pady=(10, 0), sticky="ew")
        self.modo_optionmenu = ctk.CTkOptionMenu(
            self.sidebar, values=["System", "Light", "Dark"],
            command=ctk.set_appearance_mode,
        )
        self.modo_optionmenu.grid(row=12, column=0, padx=20, pady=(0, 20), sticky="ew")

    def _construir_area_conteudo(self):
        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def mostrar_frame(self, chave):
        self.frames[chave].tkraise()


# ============================================================
# TELA 1 - HOME
# ============================================================
class TelaHome(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        ctk.CTkLabel(
            self, text="Bem-vindo ao Projeto Final",
            font=ctk.CTkFont(size=28, weight="bold"),
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self,
            text=("Este aplicativo único integra TODOS os widgets vistos\n"
                  "na apostila de Tkinter e CustomTkinter."),
            font=ctk.CTkFont(size=14),
            justify="center",
        ).pack(pady=10)

        # Card com Progressbar de demonstração
        card = ctk.CTkFrame(self, corner_radius=12)
        card.pack(pady=30, padx=60, fill="x")

        ctk.CTkLabel(card, text="Conteúdo da Apostila",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(20, 10))

        topicos = [
            "✅ Widgets básicos: Label, Button, Entry, Text",
            "✅ Seleção: Checkbutton, Radiobutton, Combobox, Spinbox",
            "✅ Listagem: Listbox, Treeview, Scrollbar",
            "✅ Layout: pack, grid, place, Frame, Notebook",
            "✅ Canvas e desenho vetorial",
            "✅ Diálogos: messagebox, filedialog, colorchooser",
            "✅ CustomTkinter: CTkSwitch, CTkSlider, CTkTabview, CTkScrollableFrame",
        ]
        for t in topicos:
            ctk.CTkLabel(card, text=t, anchor="w").pack(fill="x", padx=40, pady=2)

        self.barra = ctk.CTkProgressBar(card, width=400)
        self.barra.pack(pady=20)
        self.barra.set(0)
        self._anim_barra(0.0)

        ctk.CTkButton(
            self, text="Começar pelo Formulário →",
            command=lambda: app.mostrar_frame("form"),
            height=40, font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(pady=10)

    def _anim_barra(self, v):
        if v >= 1.0:
            v = 0.0
        self.barra.set(v)
        self.after(80, lambda: self._anim_barra(v + 0.02))


# ============================================================
# TELA 2 - FORMULÁRIO (todos widgets de entrada)
# ============================================================
class TelaFormulario(ctk.CTkScrollableFrame):
    def __init__(self, parent, app):
        super().__init__(parent, label_text="📝 Formulário Completo de Cadastro")
        self.app = app

        # ----- Variáveis Tk -----
        self.var_nome = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_idade = tk.IntVar(value=18)
        self.var_genero = tk.StringVar(value="Outro")
        self.var_newsletter = tk.BooleanVar(value=True)
        self.var_notif = tk.BooleanVar(value=False)
        self.var_nivel = tk.IntVar(value=3)
        self.var_estado = tk.StringVar()

        pad = {"padx": 15, "pady": 6}

        # Nome (Entry)
        ctk.CTkLabel(self, text="Nome completo:").grid(row=0, column=0, sticky="w", **pad)
        ctk.CTkEntry(self, textvariable=self.var_nome, width=320,
                     placeholder_text="Digite seu nome").grid(row=0, column=1, **pad)

        # Email
        ctk.CTkLabel(self, text="E-mail:").grid(row=1, column=0, sticky="w", **pad)
        ctk.CTkEntry(self, textvariable=self.var_email, width=320,
                     placeholder_text="email@dominio.com").grid(row=1, column=1, **pad)

        # Idade (Spinbox do ttk)
        ctk.CTkLabel(self, text="Idade (Spinbox):").grid(row=2, column=0, sticky="w", **pad)
        ttk.Spinbox(self, from_=0, to=120, textvariable=self.var_idade,
                    width=8).grid(row=2, column=1, sticky="w", **pad)

        # Estado (Combobox)
        ctk.CTkLabel(self, text="Estado (Combobox):").grid(row=3, column=0, sticky="w", **pad)
        ctk.CTkComboBox(
            self, values=["SP", "RJ", "MG", "RS", "BA", "PR", "SC", "CE"],
            variable=self.var_estado, width=200,
        ).grid(row=3, column=1, sticky="w", **pad)

        # Gênero (Radiobutton)
        ctk.CTkLabel(self, text="Gênero (Radio):").grid(row=4, column=0, sticky="w", **pad)
        fr_radio = ctk.CTkFrame(self, fg_color="transparent")
        fr_radio.grid(row=4, column=1, sticky="w", **pad)
        for g in ["Masculino", "Feminino", "Outro"]:
            ctk.CTkRadioButton(fr_radio, text=g, value=g,
                               variable=self.var_genero).pack(side="left", padx=6)

        # Checkbuttons
        ctk.CTkLabel(self, text="Preferências (Check):").grid(row=5, column=0, sticky="w", **pad)
        fr_chk = ctk.CTkFrame(self, fg_color="transparent")
        fr_chk.grid(row=5, column=1, sticky="w", **pad)
        ctk.CTkCheckBox(fr_chk, text="Newsletter",
                        variable=self.var_newsletter).pack(side="left", padx=6)
        ctk.CTkCheckBox(fr_chk, text="Notificações",
                        variable=self.var_notif).pack(side="left", padx=6)

        # Switch (CustomTkinter)
        ctk.CTkLabel(self, text="Modo Premium (Switch):").grid(row=6, column=0, sticky="w", **pad)
        self.sw_premium = ctk.CTkSwitch(self, text="Ativado")
        self.sw_premium.grid(row=6, column=1, sticky="w", **pad)

        # Slider
        ctk.CTkLabel(self, text="Nível de experiência (Slider):").grid(row=7, column=0, sticky="w", **pad)
        fr_sl = ctk.CTkFrame(self, fg_color="transparent")
        fr_sl.grid(row=7, column=1, sticky="w", **pad)
        self.lbl_nivel = ctk.CTkLabel(fr_sl, text="3")
        self.lbl_nivel.pack(side="right", padx=8)
        ctk.CTkSlider(fr_sl, from_=1, to=10, number_of_steps=9,
                      variable=self.var_nivel,
                      command=lambda v: self.lbl_nivel.configure(text=str(int(float(v))))
                      ).pack(side="left")

        # Text (multi-linha)
        ctk.CTkLabel(self, text="Comentários (Text):").grid(row=8, column=0, sticky="nw", **pad)
        self.txt_obs = ctk.CTkTextbox(self, width=400, height=120)
        self.txt_obs.grid(row=8, column=1, **pad)

        # Botões de ação
        fr_btn = ctk.CTkFrame(self, fg_color="transparent")
        fr_btn.grid(row=9, column=0, columnspan=2, pady=20)
        ctk.CTkButton(fr_btn, text="💾 Salvar Cadastro",
                      command=self.salvar).pack(side="left", padx=8)
        ctk.CTkButton(fr_btn, text="🧹 Limpar", fg_color="gray",
                      command=self.limpar).pack(side="left", padx=8)
        ctk.CTkButton(fr_btn, text="📋 Ir para Lista →",
                      command=lambda: app.mostrar_frame("lista")).pack(side="left", padx=8)

    def salvar(self):
        if not self.var_nome.get().strip():
            messagebox.showwarning("Atenção", "Informe o nome.")
            return
        reg = {
            "nome": self.var_nome.get(),
            "email": self.var_email.get(),
            "idade": self.var_idade.get(),
            "estado": self.var_estado.get(),
            "genero": self.var_genero.get(),
            "newsletter": self.var_newsletter.get(),
            "notif": self.var_notif.get(),
            "premium": bool(self.sw_premium.get()),
            "nivel": self.var_nivel.get(),
            "obs": self.txt_obs.get("1.0", "end").strip(),
        }
        self.app.dados_cadastros.append(reg)
        self.app.frames["lista"].recarregar()
        messagebox.showinfo("Sucesso", f"Cadastro de {reg['nome']} salvo!")
        self.limpar()

    def limpar(self):
        self.var_nome.set("")
        self.var_email.set("")
        self.var_idade.set(18)
        self.var_estado.set("")
        self.var_genero.set("Outro")
        self.var_newsletter.set(True)
        self.var_notif.set(False)
        self.var_nivel.set(3)
        self.lbl_nivel.configure(text="3")
        self.sw_premium.deselect()
        self.txt_obs.delete("1.0", "end")


# ============================================================
# TELA 3 - LISTAS / TABELA
# ============================================================
class TelaListas(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        ctk.CTkLabel(self, text="📋 Listbox + Treeview + Scrollbar",
                     font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        tabs = ctk.CTkTabview(self, width=900, height=480)
        tabs.pack(padx=20, pady=10, fill="both", expand=True)
        tabs.add("Listbox")
        tabs.add("Treeview (Tabela)")

        # ----- Listbox -----
        f1 = tabs.tab("Listbox")
        sb = tk.Scrollbar(f1)
        sb.pack(side="right", fill="y")
        self.listbox = tk.Listbox(f1, yscrollcommand=sb.set,
                                  font=("Segoe UI", 12), height=18)
        self.listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        sb.config(command=self.listbox.yview)

        # ----- Treeview -----
        f2 = tabs.tab("Treeview (Tabela)")
        cols = ("nome", "email", "idade", "estado", "premium")
        self.tree = ttk.Treeview(f2, columns=cols, show="headings", height=18)
        for c, t, w in [
            ("nome", "Nome", 200), ("email", "E-mail", 200),
            ("idade", "Idade", 60), ("estado", "Estado", 70),
            ("premium", "Premium", 80),
        ]:
            self.tree.heading(c, text=t)
            self.tree.column(c, width=w, anchor="w")
        sb2 = ttk.Scrollbar(f2, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb2.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        sb2.pack(side="right", fill="y")

        # Botões
        fr = ctk.CTkFrame(self, fg_color="transparent")
        fr.pack(pady=10)
        ctk.CTkButton(fr, text="🔄 Recarregar",
                      command=self.recarregar).pack(side="left", padx=8)
        ctk.CTkButton(fr, text="🗑️ Remover selecionado",
                      fg_color="#c0392b", command=self.remover).pack(side="left", padx=8)
        ctk.CTkButton(fr, text="➕ Adicionar exemplo",
                      command=self.exemplo).pack(side="left", padx=8)

    def recarregar(self):
        self.listbox.delete(0, "end")
        for r in self.app.dados_cadastros:
            self.listbox.insert("end", f"{r['nome']} - {r['email']}")
        for i in self.tree.get_children():
            self.tree.delete(i)
        for r in self.app.dados_cadastros:
            self.tree.insert("", "end", values=(
                r["nome"], r["email"], r["idade"],
                r["estado"], "Sim" if r["premium"] else "Não",
            ))

    def remover(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Selecione uma linha.")
            return
        idx = self.tree.index(sel[0])
        del self.app.dados_cadastros[idx]
        self.recarregar()

    def exemplo(self):
        self.app.dados_cadastros.append({
            "nome": "Ana Demo", "email": "ana@demo.com",
            "idade": 27, "estado": "SP", "genero": "Feminino",
            "newsletter": True, "notif": False, "premium": True,
            "nivel": 7, "obs": "Registro de exemplo",
        })
        self.recarregar()


# ============================================================
# TELA 4 - CANVAS / DESENHO
# ============================================================
class TelaCanvas(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.cor = "#1f6aa5"

        ctk.CTkLabel(self, text="🎨 Canvas - Desenho Livre + Formas",
                     font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        # Toolbar
        tb = ctk.CTkFrame(self)
        tb.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(tb, text="🎨 Cor", width=80,
                      command=self.escolher_cor).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(tb, text="⬛ Retângulo", width=100,
                      command=lambda: self.forma("ret")).pack(side="left", padx=5)
        ctk.CTkButton(tb, text="⚫ Círculo", width=100,
                      command=lambda: self.forma("circ")).pack(side="left", padx=5)
        ctk.CTkButton(tb, text="📏 Linha", width=80,
                      command=lambda: self.forma("linha")).pack(side="left", padx=5)
        ctk.CTkButton(tb, text="🧹 Limpar", fg_color="gray", width=80,
                      command=lambda: self.canvas.delete("all")).pack(side="left", padx=5)

        self.canvas = tk.Canvas(self, bg="white", height=450,
                                highlightthickness=1, highlightbackground="#888")
        self.canvas.pack(fill="both", expand=True, padx=20, pady=10)

        # Eventos de mouse — desenho livre
        self.canvas.bind("<B1-Motion>", self.desenhar)
        self._ult = None
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, "_ult", None))

    def escolher_cor(self):
        c = colorchooser.askcolor(title="Escolha a cor")
        if c[1]:
            self.cor = c[1]

    def desenhar(self, e):
        if self._ult:
            self.canvas.create_line(self._ult[0], self._ult[1], e.x, e.y,
                                    fill=self.cor, width=3, capstyle="round")
        self._ult = (e.x, e.y)

    def forma(self, tipo):
        import random
        w = self.canvas.winfo_width() or 800
        h = self.canvas.winfo_height() or 400
        x1, y1 = random.randint(20, w - 120), random.randint(20, h - 120)
        x2, y2 = x1 + random.randint(40, 120), y1 + random.randint(40, 120)
        if tipo == "ret":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.cor, outline="")
        elif tipo == "circ":
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.cor, outline="")
        else:
            self.canvas.create_line(x1, y1, x2, y2, fill=self.cor, width=4)


# ============================================================
# TELA 5 - DIÁLOGOS
# ============================================================
class TelaDialogos(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        ctk.CTkLabel(self, text="💬 Diálogos Nativos do Tkinter",
                     font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        grid = ctk.CTkFrame(self, fg_color="transparent")
        grid.pack(pady=10)

        botoes = [
            ("ℹ️ Info",     lambda: messagebox.showinfo("Info", "Mensagem informativa!")),
            ("⚠️ Aviso",    lambda: messagebox.showwarning("Aviso", "Atenção!")),
            ("❌ Erro",     lambda: messagebox.showerror("Erro", "Algo deu errado.")),
            ("❓ Sim/Não",  self._sim_nao),
            ("📂 Abrir arquivo", self._abrir),
            ("💾 Salvar arquivo", self._salvar),
            ("🎨 Escolher cor",  self._cor),
            ("🪟 Janela Toplevel", self._toplevel),
            ("📤 Exportar JSON cadastros", self._exportar),
        ]
        for i, (txt, cmd) in enumerate(botoes):
            ctk.CTkButton(grid, text=txt, width=220, height=40, command=cmd)\
               .grid(row=i // 3, column=i % 3, padx=10, pady=10)

        self.saida = ctk.CTkTextbox(self, width=800, height=200)
        self.saida.pack(pady=20)
        self.log("Pronto. Clique em um diálogo acima.\n")

    def log(self, txt):
        self.saida.insert("end", txt + "\n")
        self.saida.see("end")

    def _sim_nao(self):
        r = messagebox.askyesno("Confirmação", "Deseja continuar?")
        self.log(f"Resposta: {'Sim' if r else 'Não'}")

    def _abrir(self):
        f = filedialog.askopenfilename(title="Selecione um arquivo")
        if f: self.log(f"Aberto: {f}")

    def _salvar(self):
        f = filedialog.asksaveasfilename(defaultextension=".txt")
        if f: self.log(f"Salvar como: {f}")

    def _cor(self):
        c = colorchooser.askcolor()
        if c[1]: self.log(f"Cor selecionada: {c[1]}")

    def _toplevel(self):
        top = ctk.CTkToplevel(self)
        top.title("Janela Secundária")
        top.geometry("400x250")
        ctk.CTkLabel(top, text="🪟 Toplevel Window",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=30)
        ctk.CTkLabel(top, text="Uma nova janela independente.").pack()
        ctk.CTkButton(top, text="Fechar", command=top.destroy).pack(pady=20)

    def _exportar(self):
        if not self.app.dados_cadastros:
            messagebox.showinfo("Vazio", "Nenhum cadastro para exportar.")
            return
        f = filedialog.asksaveasfilename(defaultextension=".json",
                                         filetypes=[("JSON", "*.json")])
        if f:
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(self.app.dados_cadastros, fp, indent=2, ensure_ascii=False)
            self.log(f"Exportado: {f}")
            messagebox.showinfo("OK", "Cadastros exportados!")


# ============================================================
# TELA 6 - CONFIGURAÇÕES (Tema, escala, cores)
# ============================================================
class TelaConfiguracoes(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        ctk.CTkLabel(self, text="⚙️ Configurações de Aparência",
                     font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        card = ctk.CTkFrame(self)
        card.pack(padx=40, pady=20, fill="x")

        # Modo
        ctk.CTkLabel(card, text="Modo de aparência:").grid(row=0, column=0, padx=20, pady=15, sticky="w")
        ctk.CTkOptionMenu(card, values=["System", "Light", "Dark"],
                          command=ctk.set_appearance_mode)\
            .grid(row=0, column=1, padx=20, pady=15)

        # Tema de cor
        ctk.CTkLabel(card, text="Tema de cor (requer reiniciar):").grid(row=1, column=0, padx=20, pady=15, sticky="w")
        ctk.CTkOptionMenu(card, values=["blue", "green", "dark-blue"],
                          command=ctk.set_default_color_theme)\
            .grid(row=1, column=1, padx=20, pady=15)

        # Escala
        ctk.CTkLabel(card, text="Escala da UI:").grid(row=2, column=0, padx=20, pady=15, sticky="w")
        ctk.CTkOptionMenu(card, values=["80%", "90%", "100%", "110%", "120%"],
                          command=lambda s: ctk.set_widget_scaling(int(s[:-1]) / 100))\
            .grid(row=2, column=1, padx=20, pady=15)

        # Sobre
        sobre = ctk.CTkFrame(self)
        sobre.pack(padx=40, pady=20, fill="x")
        ctk.CTkLabel(sobre, text="Sobre",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(15, 5))
        ctk.CTkLabel(sobre, justify="center",
                     text=("Projeto Final - Apostila Tkinter & CustomTkinter\n"
                           "Integra: Label, Button, Entry, Text, Combobox, Spinbox,\n"
                           "Radio, Check, Switch, Slider, Listbox, Treeview, Canvas,\n"
                           "messagebox, filedialog, colorchooser, Toplevel,\n"
                           "CTkScrollableFrame, CTkTabview, CTkProgressBar, CTkOptionMenu.")
                     ).pack(pady=(0, 15))


# ============================================================
# Inicialização
# ============================================================
if __name__ == "__main__":
    app = AppPrincipal()
    app.mainloop()
