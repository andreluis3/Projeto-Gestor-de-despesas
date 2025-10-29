import tkinter as tk
from tkinter import ttk, messagebox
from crud import Crud
from dashboard import Dashboard
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from calendario import CalendarioDespesas
import os
crud = Crud()
dashboard = Dashboard()


crud = Crud()
dashboard = Dashboard()



COR_FUNDO = "#1E1E1E"           
COR_CARD = "#252526"         
COR_BOTAO = "#2D2D30"           
COR_BOTAO_ACTIVE = "#3E3E42"     
COR_BORDA = "#404040"            
COR_TEXTO = "#CCCCCC"          
COR_TEXTO_SECUNDARIO = "#969696" 
COR_DESTAQUE = "#007ACC"         
COR_DESPESA = "#F44747"          
COR_RECEITA = "#4EC9B0"          
COR_MENU = "#2D2D30"            
COR_MENU_BORDA = "#404040"       


class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.crud = Crud()
        self.dashboard = Dashboard()
        self.calendario = CalendarioDespesas(root, self)

        # Configurações modernas para a janela principal
        self.root.title("💸 Gestor de Despesas Pessoais 📊")
        self.root.geometry("1400x800")
        self.root.configure(bg="#0A1929")  # Dark blue moderno
        self.root.minsize(1200, 700)
        
        
        # Centralizar a janela na tela
        self.centralizar_janela()
        
        try:
            # Caminho absoluto do ícone usando caminho relativo
            icone_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "icones", "logo.ico")
            self.root.iconbitmap(icone_path)
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")
        
        try:
            caminho_icone = os.path.join(os.path.dirname(__file__), "assets", "icone.ico")
            self.root.iconbitmap(caminho_icone)
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")
        
        # Configurar fonte padrão moderna
        self.fonte_titulo = ("Segoe UI", 16, "bold")
        self.fonte_normal = ("Segoe UI", 11)
        self.fonte_pequena = ("Segoe UI", 9)
        
        # Configurar estilo
        self.configurar_estilos()
        
        # Criar header moderno
        self.criar_header_moderno()

        # Menu
        self.criar_menu_principal()

        # Frames principais
        self.criar_frames()

        # Dashboard com gráficos
        self.criar_dashboard()

        # Barra de progresso
        self.criar_barra_progresso()

        # Treeviews (menores)
        self.criar_treeviews()

        # Atualizar dados na tela
        self.atualizar_tabelas()
        
    def centralizar_janela(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def criar_header_moderno(self):
        """Cria um header moderno para a aplicação"""
        header_frame = tk.Frame(self.root, bg="#102A43", height=60)
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Título com emojis e estilo moderno
        titulo_frame = tk.Frame(header_frame, bg="#102A43")
        titulo_frame.pack(expand=True, fill="both", padx=20)
        
        titulo_label = tk.Label(titulo_frame, 
                              text="💸 Gestor de Despesas Pessoais 📊", 
                              bg="#102A43", 
                              fg="#FFFFFF",
                              font=("Segoe UI", 18, "bold"),
                              pady=15)
        titulo_label.pack(side="left")
        
        # Data atual no header
        from datetime import datetime
        data_atual = datetime.now().strftime("%d/%m/%Y")
        data_label = tk.Label(titulo_frame,
                            text=f"📅 {data_atual}",
                            bg="#102A43",
                            fg="#B0BEC5",
                            font=("Segoe UI", 11),
                            pady=15)
        data_label.pack(side="right")

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores modernas
        COR_FUNDO = "#0A1929"           # Dark blue principal
        COR_CARD = "#1E3A5F"            # Cards em azul mais claro
        COR_BOTAO = "#2A4B7A"           # Botões
        COR_BOTAO_ACTIVE = "#3D5A80"    # Botões ativos
        COR_BORDA = "#152642"           # Bordas
        COR_TEXTO = "#E0E0E0"           # Texto principal
        COR_TEXTO_SECUNDARIO = "#90A4AE" # Texto secundário
        COR_DESTAQUE = "#4FC3F7"        # Destaque (azul claro)
        COR_DESPESA = "#FF6B6B"         # Despesas (vermelho)
        COR_RECEITA = "#4ECDC4"         # Receitas (verde)
        COR_MENU = "#102A43"            # Menu
        COR_MENU_BORDA = "#0D1F33"      # Borda do menu

        # Configurar estilo da treeview moderna
        style.configure("Modern.Treeview",
                        background=COR_CARD,
                        foreground=COR_TEXTO,
                        fieldbackground=COR_CARD,
                        bordercolor=COR_BORDA,
                        borderwidth=1,
                        relief="flat",
                        font=self.fonte_normal)
        style.map('Modern.Treeview', 
                 background=[('selected', COR_DESTAQUE)],
                 foreground=[('selected', "#FFFFFF")])
        
        style.configure("Modern.Treeview.Heading",
                        background=COR_MENU,
                        foreground=COR_TEXTO,
                        relief="flat",
                        borderwidth=0,
                        font=("Segoe UI", 10, "bold"))
        style.map("Modern.Treeview.Heading", 
                 background=[('active', COR_BOTAO_ACTIVE)])
        
        # Configurar estilo dos botões modernos
        style.configure("Modern.TButton",
                        background=COR_BOTAO,
                        foreground=COR_TEXTO,
                        bordercolor=COR_BORDA,
                        borderwidth=0,
                        focuscolor=COR_BOTAO_ACTIVE,
                        font=("Segoe UI", 10),
                        padding=(10, 5))
        style.map("Modern.TButton",
                 background=[('active', COR_BOTAO_ACTIVE)],
                 relief=[('pressed', 'sunken'), ('!pressed', 'flat')])
        
        # Configurar estilo da barra de progresso moderna
        style.configure("Modern.Horizontal.TProgressbar",
                        background=COR_DESPESA,
                        troughcolor=COR_RECEITA,
                        bordercolor=COR_BORDA,
                        thickness=15)

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilo da treeview
        style.configure("Custom.Treeview",
                        background=COR_CARD,
                        foreground=COR_TEXTO,
                        fieldbackground=COR_CARD,
                        bordercolor=COR_BORDA,
                        borderwidth=1,
                        relief="solid")
        style.map('Custom.Treeview', 
                 background=[('selected', COR_DESTAQUE)],
                 foreground=[('selected', COR_TEXTO)])
        
        style.configure("Custom.Treeview.Heading",
                        background=COR_MENU,
                        foreground=COR_TEXTO,
                        relief="solid",
                        borderwidth=1,
                        bordercolor=COR_MENU_BORDA)
        style.map("Custom.Treeview.Heading", 
                 background=[('active', COR_BOTAO_ACTIVE)])
        
        # Configurar estilo dos botões
        style.configure("Dark.TButton",
                        background=COR_BOTAO,
                        foreground=COR_TEXTO,
                        bordercolor=COR_BORDA,
                        borderwidth=1,
                        focuscolor=COR_BOTAO_ACTIVE)
        style.map("Dark.TButton",
                 background=[('active', COR_BOTAO_ACTIVE)],
                 relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
        
        # Configurar estilo da barra de progresso
        style.configure("Custom.Horizontal.TProgressbar",
                        background=COR_DESPESA,
                        troughcolor=COR_RECEITA,
                        bordercolor=COR_BORDA,
                        lightcolor=COR_DESPESA,
                        darkcolor=COR_DESPESA,
                        thickness=20)

    def criar_menu_principal(self):
        # Cores para o menu azul dark
        COR_MENU_AZUL = "#1E3A5F"           # Azul dark principal
        COR_MENU_AZUL_ACTIVE = "#2A4B7A"    # Azul dark quando ativo
        COR_MENU_BORDA_AZUL = "#152642"     # Borda azul mais escuro
        COR_TEXTO_MENU = "#FFFFFF"          # Texto branco para contraste
        
        # Frame para conter a barra de menu com borda
        self.menu_container = tk.Frame(self.root, bg=COR_MENU_BORDA_AZUL, height=30)
        self.menu_container.pack(fill="x", padx=0, pady=0)
        self.menu_container.pack_propagate(False)
        
        # Frame interno para o menu
        menu_frame = tk.Frame(self.menu_container, bg=COR_MENU_AZUL, height=28)
        menu_frame.pack(fill="both", expand=True, padx=1, pady=1)
        
        # Barra de menu personalizada
        menu_bar = tk.Menu(
            self.root,
            bg=COR_MENU_AZUL,
            fg=COR_TEXTO_MENU,
            activebackground=COR_MENU_AZUL_ACTIVE,
            activeforeground=COR_TEXTO_MENU,
            borderwidth=0,
            relief="flat",
            tearoff=0
        )

        # Menu Início
        menu_inicio = tk.Menu(menu_bar, tearoff=0, 
                            bg=COR_MENU_AZUL, 
                            fg=COR_TEXTO_MENU,
                            activebackground=COR_MENU_AZUL_ACTIVE,
                            activeforeground=COR_TEXTO_MENU,
                            bd=1,
                            activeborderwidth=1,
                            relief="solid")
        menu_inicio.add_command(label="Voltar ao Início", command=self.voltar_inicio)
        menu_bar.add_cascade(label="Início", menu=menu_inicio)

        # Menu Cadastrar
        menu_cadastrar = tk.Menu(menu_bar, tearoff=0, 
                                bg=COR_MENU_AZUL, 
                                fg=COR_TEXTO_MENU,
                                activebackground=COR_MENU_AZUL_ACTIVE,
                                activeforeground=COR_TEXTO_MENU,
                                bd=1,
                                activeborderwidth=1,
                                relief="solid")
        menu_cadastrar.add_command(label="Cadastrar Receita", command=self.janela_cadastrar_receita)
        menu_cadastrar.add_command(label="Cadastrar Despesa", command=self.janela_cadastrar_despesa)
        menu_bar.add_cascade(label="Cadastrar", menu=menu_cadastrar)


        # Menu Calendário
        menu_calendario = tk.Menu(menu_bar, tearoff=0,
                                bg=COR_MENU_AZUL,
                                fg=COR_TEXTO_MENU,
                                activebackground=COR_MENU_AZUL_ACTIVE,
                                activeforeground=COR_TEXTO_MENU,
                                bd=1,
                                activeborderwidth=1,
                                relief="solid")
        menu_calendario.add_command(label="Abrir Calendário", command=self.abrir_calendario)
        menu_bar.add_cascade(label="Calendário", menu=menu_calendario)

        # Menu Atualizar
        menu_atualizar = tk.Menu(menu_bar, tearoff=0,
                                bg=COR_MENU_AZUL,
                                fg=COR_TEXTO_MENU,
                                activebackground=COR_MENU_AZUL_ACTIVE,
                                activeforeground=COR_TEXTO_MENU,
                                bd=1,
                                activeborderwidth=1,
                                relief="solid")
        menu_atualizar.add_command(label="Atualizar Interface", command=self.atualizar_interface)
        menu_bar.add_cascade(label="Atualizar", menu=menu_atualizar)

        
        
        # Menu Deletar
        menu_deletar = tk.Menu(menu_bar, tearoff=0, 
                            bg=COR_MENU_AZUL, 
                            fg=COR_TEXTO_MENU,
                            activebackground=COR_MENU_AZUL_ACTIVE,
                            activeforeground=COR_TEXTO_MENU,
                            bd=1,
                            activeborderwidth=1,
                            relief="solid")
        menu_deletar.add_command(label="Deletar Receita", command=self.janela_deletar_receita)
        menu_deletar.add_command(label="Deletar Despesa", command=self.janela_deletar_despesa)
        menu_bar.add_cascade(label="Deletar", menu=menu_deletar)

        # Menu Dashboard
        menu_dashboard = tk.Menu(menu_bar, tearoff=0, 
                                bg=COR_MENU_AZUL, 
                                fg=COR_TEXTO_MENU,
                                activebackground=COR_MENU_AZUL_ACTIVE,
                                activeforeground=COR_TEXTO_MENU,
                                bd=1,
                                activeborderwidth=1,
                                relief="solid")
        menu_dashboard.add_command(label="Atualizar Gráficos", command=self.atualizar_dashboard)
        menu_bar.add_cascade(label="Dashboard", menu=menu_dashboard)

        # Menu Ajuda
        menu_ajuda = tk.Menu(menu_bar, tearoff=0, 
                            bg=COR_MENU_AZUL, 
                            fg=COR_TEXTO_MENU,
                            activebackground=COR_MENU_AZUL_ACTIVE,
                            activeforeground=COR_TEXTO_MENU,
                            bd=1,
                            activeborderwidth=1,
                            relief="solid")
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)
        menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

        self.root.config(menu=menu_bar)

    def criar_frames(self):
        # Frame principal com padding
        self.frame_principal = tk.Frame(self.root, bg=COR_FUNDO)
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame superior para o dashboard (aumentado para 4 gráficos)
        self.frame_superior = tk.Frame(self.frame_principal, bg=COR_FUNDO, height=300)
        self.frame_superior.pack(fill="x", pady=(0, 10))
        self.frame_superior.pack_propagate(False)

        # Frame para a barra de progresso
        self.frame_progresso = tk.Frame(self.frame_principal, bg=COR_FUNDO, height=50)
        self.frame_progresso.pack(fill="x", pady=(0, 10))
        self.frame_progresso.pack_propagate(False)

        # Frame inferior para as tabelas (reduzido)
        self.frame_inferior = tk.Frame(self.frame_principal, bg=COR_FUNDO, height=180)
        self.frame_inferior.pack(fill="both", expand=True)

        # Frame para as treeviews
        self.frame_tables = tk.Frame(self.frame_inferior, bg=COR_FUNDO)
        self.frame_tables.pack(fill="both", expand=True)

        self.frame_despesas = tk.Frame(self.frame_tables, bg=COR_FUNDO)
        self.frame_despesas.pack(side="left", fill="both", expand=True, padx=(0, 5))

        self.frame_receitas = tk.Frame(self.frame_tables, bg=COR_FUNDO)
        self.frame_receitas.pack(side="right", fill="both", expand=True, padx=(5, 0))

    def criar_dashboard(self):
        # Frame para os gráficos com borda
        self.frame_graficos = tk.Frame(self.frame_superior, bg=COR_BORDA, bd=1, relief="solid")
        self.frame_graficos.pack(fill="both", expand=True)

        # Gráfico de pizza (esquerda) - Distribuição de Despesas
        self.frame_pizza = tk.Frame(self.frame_graficos, bg=COR_CARD, width=250, height=280)
        self.frame_pizza.pack(side="left", fill="both", expand=True, padx=(5, 2), pady=5)
        self.frame_pizza.pack_propagate(False)

        lbl_pizza = tk.Label(self.frame_pizza, text="Distribuição de Despesas", 
                            bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 10, "bold"))
        lbl_pizza.pack(pady=3)

        self.canvas_pizza = None

        # Gráfico de categorias (segundo) - Categorias que Mais Gasta
        self.frame_categorias = tk.Frame(self.frame_graficos, bg=COR_CARD, width=250, height=280)
        self.frame_categorias.pack(side="left", fill="both", expand=True, padx=2, pady=5)
        self.frame_categorias.pack_propagate(False)

        lbl_categorias = tk.Label(self.frame_categorias, text="Categorias que Mais Gasta", 
                                bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 10, "bold"))
        lbl_categorias.pack(pady=3)

        self.canvas_categorias = None

        # Gráfico de barras (terceiro) - Relação Despesas x Receitas
        self.frame_barras = tk.Frame(self.frame_graficos, bg=COR_CARD, width=250, height=280)
        self.frame_barras.pack(side="left", fill="both", expand=True, padx=2, pady=5)
        self.frame_barras.pack_propagate(False)

        lbl_barras = tk.Label(self.frame_barras, text="Relação Despesas x Receitas", 
                            bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 10, "bold"))
        lbl_barras.pack(pady=3)

        self.canvas_barras = None

        # Gráfico de saldo (direita) - Saldo Mensal
        self.frame_saldo = tk.Frame(self.frame_graficos, bg=COR_CARD, width=250, height=280)
        self.frame_saldo.pack(side="left", fill="both", expand=True, padx=(2, 5), pady=5)
        self.frame_saldo.pack_propagate(False)

        lbl_saldo = tk.Label(self.frame_saldo, text="Saldo Mensal", 
                        bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 10, "bold"))
        lbl_saldo.pack(pady=3)

        self.canvas_saldo = None
        
    def criar_barra_progresso(self):
        # Frame para a barra de progresso
        frame_progress_container = tk.Frame(self.frame_progresso, bg=COR_BORDA, bd=1, relief="solid")
        frame_progress_container.pack(fill="both", expand=True)
        
        # Frame interno centralizado
        frame_progress_interno = tk.Frame(frame_progress_container, bg=COR_CARD)
        frame_progress_interno.pack(expand=True, fill="both", padx=5, pady=5)
        
        # Título
        lbl_titulo = tk.Label(frame_progress_interno, text="Relação Despesas/Receitas", 
                             bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 12, "bold"))
        lbl_titulo.pack(pady=(0, 5))
        
        # Frame para centralizar a barra de progresso
        frame_centro = tk.Frame(frame_progress_interno, bg=COR_CARD)
        frame_centro.pack(expand=True, fill="x", padx=50)
        
        # Barra de progresso personalizada
        self.progress_bar = ttk.Progressbar(frame_centro, orient="horizontal", 
                                           mode="determinate", length=600,
                                           style="Custom.Horizontal.TProgressbar")
        self.progress_bar.pack(expand=True, fill="x", pady=5)
        
        # Labels informativos
        frame_labels = tk.Frame(frame_progress_interno, bg=COR_CARD)
        frame_labels.pack(fill="x", padx=50)
        
        lbl_despesas = tk.Label(frame_labels, text="Despesas", bg=COR_CARD, 
                               fg=COR_DESPESA, font=("Calibri", 10))
        lbl_despesas.pack(side="left")
        
        lbl_receitas = tk.Label(frame_labels, text="Receitas", bg=COR_CARD, 
                               fg=COR_RECEITA, font=("Calibri", 10))
        lbl_receitas.pack(side="right")

    def criar_treeviews(self):
        colunas = ("Nome", "Valor", "Data")

        # Frame para despesas com borda (menor)
        frame_desp_container = tk.Frame(self.frame_despesas, bg=COR_BORDA, bd=1, relief="solid")
        frame_desp_container.pack(fill="both", expand=True)
        
        label_desp = tk.Label(frame_desp_container, text="Despesas", 
                             bg=COR_CARD, fg=COR_DESPESA, font=("Calibri", 12, "bold"))
        label_desp.pack(anchor="w", padx=10, pady=(8, 5))

        # Frame interno para a treeview de despesas
        frame_desp_interno = tk.Frame(frame_desp_container, bg=COR_CARD)
        frame_desp_interno.pack(fill="both", expand=True, padx=5, pady=(0, 5))

        # Treeview com altura reduzida
        self.tree_despesas = ttk.Treeview(frame_desp_interno, columns=colunas, show="headings", 
                                         height=5, style="Custom.Treeview")
        for col in colunas:
            self.tree_despesas.heading(col, text=col)
            self.tree_despesas.column(col, anchor="center", width=100)
        self.tree_despesas.pack(side="left", fill="both", expand=True)

        vsb1 = ttk.Scrollbar(frame_desp_interno, orient="vertical", command=self.tree_despesas.yview)
        self.tree_despesas.configure(yscroll=vsb1.set)
        vsb1.pack(side="right", fill="y")

        # Frame para receitas com borda (menor)
        frame_rec_container = tk.Frame(self.frame_receitas, bg=COR_BORDA, bd=1, relief="solid")
        frame_rec_container.pack(fill="both", expand=True)
        
        label_rec = tk.Label(frame_rec_container, text="Receitas", 
                            bg=COR_CARD, fg=COR_RECEITA, font=("Calibri", 12, "bold"))
        label_rec.pack(anchor="w", padx=10, pady=(8, 5))

        # Frame interno para a treeview de receitas
        frame_rec_interno = tk.Frame(frame_rec_container, bg=COR_CARD)
        frame_rec_interno.pack(fill="both", expand=True, padx=5, pady=(0, 5))

        # Treeview com altura reduzida
        self.tree_receitas = ttk.Treeview(frame_rec_interno, columns=colunas, show="headings", 
                                         height=5, style="Custom.Treeview")
        for col in colunas:
            self.tree_receitas.heading(col, text=col)
            self.tree_receitas.column(col, anchor="center", width=100)
        self.tree_receitas.pack(side="left", fill="both", expand=True)

        vsb2 = ttk.Scrollbar(frame_rec_interno, orient="vertical", command=self.tree_receitas.yview)
        self.tree_receitas.configure(yscroll=vsb2.set)
        vsb2.pack(side="right", fill="y")

    def atualizar_tabelas(self):
        # Limpar trees
        for item in self.tree_despesas.get_children():
            self.tree_despesas.delete(item)
        for item in self.tree_receitas.get_children():
            self.tree_receitas.delete(item)

        # Preencher despesas com data formatada
        despesas = self.crud.listar_despesas()
        for desp in despesas:
            # desp[0] = id, desp[1] = nome, desp[2] = valor, desp[3] = data
            data_formatada = self.formatar_data(desp[3])
            self.tree_despesas.insert("", "end", values=(desp[1], f"R$ {desp[2]:.2f}", data_formatada))

        # Preencher receitas com data formatada
        receitas = self.crud.listar_receitas()
        for rec in receitas:
            data_formatada = self.formatar_data(rec[3])
            self.tree_receitas.insert("", "end", values=(rec[1], f"R$ {rec[2]:.2f}", data_formatada))

        # Atualizar dashboard
        self.atualizar_dashboard()
        
        # Atualizar barra de progresso
        self.atualizar_barra_progresso()
    def formatar_data(self, data_db):
        """Converte data de YYYY-MM-DD para DD-MM-YYYY"""
        if data_db and len(data_db) == 10 and data_db[4] == '-' and data_db[7] == '-':
            return f"{data_db[8:10]}-{data_db[5:7]}-{data_db[0:4]}"
        return data_db

    def atualizar_barra_progresso(self):
        # Calcular totais
        total_despesas = sum(float(self.tree_despesas.item(item)['values'][1].replace('R$ ', '').replace(',', '')) 
                           for item in self.tree_despesas.get_children())
        total_receitas = sum(float(self.tree_receitas.item(item)['values'][1].replace('R$ ', '').replace(',', '')) 
                           for item in self.tree_receitas.get_children())
        
        # Calcular porcentagem
        if total_receitas > 0:
            porcentagem_despesas = min(total_despesas / total_receitas, 1.0)
            self.progress_bar['value'] = porcentagem_despesas * 100
            
            # Atualizar texto informativo
            for widget in self.frame_progresso.winfo_children():
                if isinstance(widget, tk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, tk.Frame):
                            for label in child.winfo_children():
                                if isinstance(label, tk.Label) and label['text'].startswith("Despesas:"):
                                    label.destroy()
                            
                            # Adicionar novo label com informações
                            texto = f"Despesas: R$ {total_despesas:.2f} ({porcentagem_despesas*100:.1f}%) | Receitas: R$ {total_receitas:.2f} | Saldo: R$ {total_receitas - total_despesas:.2f}"
                            lbl_info = tk.Label(child, text=texto, bg=COR_CARD, 
                                               fg=COR_TEXTO, font=("Calibri", 10))
                            lbl_info.pack(pady=(0, 5))

    def atualizar_dashboard(self):
        # Obter dados
        despesas = self.crud.listar_despesas()
        receitas = self.crud.listar_receitas()

        # --- DESTRUIR CANVASES ANTIGOS (com segurança) ---
        # usamos atributos self.canvas_pizza, self.canvas_categorias, self.canvas_barras, self.canvas_saldo
        for attr, frame in (
            ("canvas_pizza", self.frame_pizza),
            ("canvas_categorias", self.frame_categorias),
            ("canvas_barras", self.frame_barras),
            ("canvas_saldo", self.frame_saldo),
        ):
            canvas_obj = getattr(self, attr, None)
            if canvas_obj is not None:
                try:
                    # destrói o widget Tk associado ao canvas do matplotlib
                    canvas_obj.get_tk_widget().destroy()
                except Exception:
                    # fallback: destrói filhos não-labels do frame (protege o label-título)
                    for child in frame.winfo_children():
                        if child.winfo_class() != "Label":
                            try:
                                child.destroy()
                            except Exception:
                                pass
                finally:
                    setattr(self, attr, None)

        # --- GRÁFICO 1: Pizza - Distribuição de Despesas ---
        if despesas:
            fig_pizza, ax_pizza = plt.subplots(figsize=(3, 2.5))
            fig_pizza.patch.set_facecolor(COR_CARD)
            ax_pizza.set_facecolor(COR_CARD)

            labels = [d[1] for d in despesas]
            valores = [d[2] for d in despesas]

            cores = [COR_DESPESA, '#E06C75', '#BE5046', '#98C379', '#D19A66', '#C678DD'][:len(valores)]

            ax_pizza.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=cores)
            ax_pizza.axis('equal')
            ax_pizza.set_title("Distribuição de Despesas", color=COR_TEXTO, fontsize=10)

            for text in ax_pizza.texts:
                text.set_color(COR_TEXTO)
                text.set_fontsize(8)

            self.canvas_pizza = FigureCanvasTkAgg(fig_pizza, self.frame_pizza)
            self.canvas_pizza.draw()
            self.canvas_pizza.get_tk_widget().pack(fill="both", expand=True)

            plt.close(fig_pizza)  # libera memória

        # --- GRÁFICO 2: Categorias que Mais Gasta (despesas recorrentes) ---
        # zera canvas_categorias antes de recriar (feito acima)
        if hasattr(self, 'calendario') and self.calendario.despesas_recorrentes:
            # Agrupar despesas por categoria
            categorias = {}
            for desp in self.calendario.despesas_recorrentes:
                categoria = desp.get('categoria', 'Outros')
                categorias[categoria] = categorias.get(categoria, 0) + desp.get('valor', 0)

            if categorias:
                fig_cat, ax_cat = plt.subplots(figsize=(3, 2.5))
                fig_cat.patch.set_facecolor(COR_CARD)
                ax_cat.set_facecolor(COR_CARD)

                cats = list(categorias.keys())
                valores_cat = list(categorias.values())

                sorted_indices = sorted(range(len(valores_cat)), key=lambda i: valores_cat[i], reverse=True)
                cats = [cats[i] for i in sorted_indices][:5]
                valores_cat = [valores_cat[i] for i in sorted_indices][:5]

                cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'][:len(cats)]
                bars = ax_cat.bar(cats, valores_cat, color=cores)
                ax_cat.set_title('Top Categorias', color=COR_TEXTO, fontsize=10)
                ax_cat.tick_params(axis='x', rotation=45, colors=COR_TEXTO, labelsize=8)
                ax_cat.tick_params(axis='y', colors=COR_TEXTO)

                for spine in ax_cat.spines.values():
                    spine.set_color(COR_BORDA)

                for bar, valor in zip(bars, valores_cat):
                    height = bar.get_height()
                    ax_cat.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                                f'R$ {valor:.2f}', ha='center', va='bottom',
                                color=COR_TEXTO, fontsize=7)

                self.canvas_categorias = FigureCanvasTkAgg(fig_cat, self.frame_categorias)
                self.canvas_categorias.draw()
                self.canvas_categorias.get_tk_widget().pack(fill="both", expand=True)

                plt.close(fig_cat)

        # --- GRÁFICO 3: Barras - Relação Despesas x Receitas ---
        fig_barras, ax_barras = plt.subplots(figsize=(3, 2.5))
        fig_barras.patch.set_facecolor(COR_CARD)
        ax_barras.set_facecolor(COR_CARD)

        total_despesas = sum([d[2] for d in despesas]) if despesas else 0
        total_receitas = sum([r[2] for r in receitas]) if receitas else 0

        categorias_plot = ['Despesas', 'Receitas']
        valores_plot = [total_despesas, total_receitas]
        cores_plot = [COR_DESPESA, COR_RECEITA]

        bars = ax_barras.bar(categorias_plot, valores_plot, color=cores_plot)
        ax_barras.set_title('Despesas vs Receitas', color=COR_TEXTO, fontsize=10)
        ax_barras.tick_params(colors=COR_TEXTO)

        for spine in ax_barras.spines.values():
            spine.set_color(COR_BORDA)

        for bar, valor in zip(bars, valores_plot):
            height = bar.get_height()
            ax_barras.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                        f'R$ {valor:.2f}', ha='center', va='bottom',
                        color=COR_TEXTO, fontsize=8)

        self.canvas_barras = FigureCanvasTkAgg(fig_barras, self.frame_barras)
        self.canvas_barras.draw()
        self.canvas_barras.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig_barras)

        # --- GRÁFICO 4: Saldo Mensal ---
        fig_saldo, ax_saldo = plt.subplots(figsize=(3, 2.5))
        fig_saldo.patch.set_facecolor(COR_CARD)
        ax_saldo.set_facecolor(COR_CARD)

        saldo = total_receitas - total_despesas
        cores_saldo = COR_RECEITA if saldo >= 0 else COR_DESPESA

        ax_saldo.bar(['Saldo'], [saldo], color=cores_saldo)
        ax_saldo.set_title('Saldo Atual', color=COR_TEXTO, fontsize=10)
        ax_saldo.tick_params(colors=COR_TEXTO)

        for spine in ax_saldo.spines.values():
            spine.set_color(COR_BORDA)

        ax_saldo.text(0, saldo/2 if saldo != 0 else 0, f'R$ {saldo:.2f}', ha='center', va='center',
                    color=COR_TEXTO, fontsize=12, fontweight='bold')

        self.canvas_saldo = FigureCanvasTkAgg(fig_saldo, self.frame_saldo)
        self.canvas_saldo.draw()
        self.canvas_saldo.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig_saldo)

        # Força o Tk a redesenhar imediatamente
        try:
            self.root.update_idletasks()
        except Exception:
            pass


     # MÉTODOS DE CADASTRO COMPLETOS
    def janela_cadastrar_receita(self):
        """Janela para cadastrar nova receita"""
        self.janela_cadastro("receita")

    def janela_cadastrar_despesa(self):
        """Janela para cadastrar nova despesa"""
        self.janela_cadastro("despesa")
        
    def janela_deletar_receita(self):
        self.janela_deletar("receita")

    def janela_deletar_despesa(self):
        self.janela_deletar("despesa")

    def janela_cadastro(self, tipo):
        """Janela genérica para cadastro de receita/despesa"""
        janela = tk.Toplevel(self.root)
        janela.title(f"Cadastrar {tipo.capitalize()}")
        janela.geometry("400x500")
        janela.configure(bg=COR_FUNDO)
        janela.resizable(False, False)
        janela.transient(self.root)
        janela.grab_set()
        
        # Frame principal
        frame = tk.Frame(janela, bg=COR_FUNDO, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        tk.Label(frame, text=f"Cadastrar {tipo.capitalize()}", 
                bg=COR_FUNDO, fg=COR_TEXTO, font=("Calibri", 16, "bold")).pack(pady=(0, 20))
        
        # Campo Descrição
        tk.Label(frame, text="Descrição:", bg=COR_FUNDO, fg=COR_TEXTO, 
                font=("Calibri", 11)).pack(anchor="w", pady=(5, 2))
        entry_descricao = tk.Entry(frame, font=("Calibri", 11), bg=COR_CARD, fg=COR_TEXTO,
                                insertbackground=COR_TEXTO, relief="solid", bd=1)
        entry_descricao.pack(fill=tk.X, pady=(0, 10))
        
        # Campo Valor
        tk.Label(frame, text="Valor (R$):", bg=COR_FUNDO, fg=COR_TEXTO, 
                font=("Calibri", 11)).pack(anchor="w", pady=(5, 2))
        entry_valor = tk.Entry(frame, font=("Calibri", 11), bg=COR_CARD, fg=COR_TEXTO,
                            insertbackground=COR_TEXTO, relief="solid", bd=1)
        entry_valor.pack(fill=tk.X, pady=(0, 10))
        
        # Campo Data - CORRIGIDO para DD-MM-YYYY
        tk.Label(frame, text="Data (DD-MM-YYYY):", bg=COR_FUNDO, fg=COR_TEXTO, 
                font=("Calibri", 11)).pack(anchor="w", pady=(5, 2))
        entry_data = tk.Entry(frame, font=("Calibri", 11), bg=COR_CARD, fg=COR_TEXTO,
                            insertbackground=COR_TEXTO, relief="solid", bd=1)
        entry_data.pack(fill=tk.X, pady=(0, 15))
        
        # Variáveis para despesa recorrente
        combobox_recorrente = None
        combobox_categoria = None
        
        # Campo Recorrente (apenas para despesas)
        if tipo == "despesa":
            frame_recorrente = tk.Frame(frame, bg=COR_FUNDO)
            frame_recorrente.pack(fill=tk.X, pady=(0, 15))
            
            tk.Label(frame_recorrente, text="Despesa Recorrente:", bg=COR_FUNDO, fg=COR_TEXTO,
                    font=("Calibri", 11)).pack(side=tk.LEFT)
            
            combobox_recorrente = ttk.Combobox(frame_recorrente, 
                                            values=["Não", "Sim"], 
                                            state="readonly",
                                            width=5,
                                            font=("Calibri", 11))
            combobox_recorrente.set("Não")
            combobox_recorrente.pack(side=tk.RIGHT, padx=(10, 0))
            
            # Campo Categoria (apenas para despesas recorrentes)
            frame_categoria = tk.Frame(frame, bg=COR_FUNDO)
            frame_categoria.pack(fill=tk.X, pady=(0, 15))
            
            tk.Label(frame_categoria, text="Categoria:", bg=COR_FUNDO, fg=COR_TEXTO,
                    font=("Calibri", 11)).pack(side=tk.LEFT)
            
            categorias = list(self.calendario.categorias.keys())
            combobox_categoria = ttk.Combobox(frame_categoria, 
                                            values=categorias,
                                            state="readonly",
                                            width=15,
                                            font=("Calibri", 11))
            combobox_categoria.set(categorias[0] if categorias else "Outros")
            combobox_categoria.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Botões
        frame_botoes = tk.Frame(frame, bg=COR_FUNDO)
        frame_botoes.pack(fill=tk.X, pady=(20, 0))
        
        def cadastrar():
            try:
                descricao = entry_descricao.get().strip()
                valor_str = entry_valor.get().strip()
                data = entry_data.get().strip()
                
                if not descricao or not valor_str or not data:
                    messagebox.showerror("Erro", "Preencha todos os campos!")
                    return
                
                # Validar valor - DEVE VIR ANTES da conversão de data
                try:
                    valor = float(valor_str)
                    if valor <= 0:
                        messagebox.showerror("Erro", "O valor deve ser maior que zero!")
                        return
                except ValueError:
                    messagebox.showerror("Erro", "Digite um valor numérico válido!")
                    return
                
                # Validar data (formato DD-MM-YYYY)
                if len(data) != 10 or data[2] != '-' or data[5] != '-':
                    messagebox.showerror("Erro", "Use o formato DD-MM-YYYY para a data!")
                    return
                
                # Converter data para YYYY-MM-DD para o banco
                try:
                    from datetime import datetime
                    data_obj = datetime.strptime(data, "%d-%m-%Y")
                    data_db = data_obj.strftime("%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Erro", "Data inválida! Use o formato DD-MM-YYYY")
                    return
                
                if tipo == "receita":
                    # Cadastrar receita usando CRUD
                    self.crud.adicionar_receita(descricao, valor, data_db)
                    messagebox.showinfo("Sucesso", "Receita cadastrada com sucesso!")
                    
                elif tipo == "despesa":
                    # Cadastrar despesa usando CRUD
                    self.crud.adicionar_despesa(descricao, valor, data_db)
                    
                    # Verificar se é recorrente
                    if combobox_recorrente.get() == "Sim":
                        despesa_recorrente = {
                            'descricao': descricao,
                            'valor': valor,
                            'dia': data_obj.day,
                            'mes': data_obj.month,
                            'ano': data_obj.year,
                            'categoria': combobox_categoria.get()
                        }
                        
                        self.calendario.despesas_recorrentes.append(despesa_recorrente)
                        self.calendario.salvar_despesas()
                        messagebox.showinfo("Sucesso", "Despesa recorrente cadastrada com sucesso!")
                    else:
                        messagebox.showinfo("Sucesso", "Despesa cadastrada com sucesso!")
                
                # Atualizar a interface
                self.atualizar_tabelas()
                if self.calendario.janela_calendario and self.calendario.janela_calendario.winfo_exists():
                    self.calendario.atualizar_calendario()
                
                janela.destroy()
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")
        
        btn_cadastrar = ttk.Button(frame_botoes, text="Cadastrar", command=cadastrar)
        btn_cadastrar.pack(side=tk.RIGHT, padx=(10, 0))
        
        btn_cancelar = ttk.Button(frame_botoes, text="Cancelar", command=janela.destroy)
        btn_cancelar.pack(side=tk.RIGHT)
        
        # Focar no primeiro campo
        entry_descricao.focus()

    def janela_deletar(self, tipo):
        """Janela genérica para deletar receita/despesa"""
        janela = tk.Toplevel(self.root)
        janela.title(f"Deletar {tipo.capitalize()}")
        janela.geometry("500x400")
        janela.configure(bg=COR_FUNDO)
        janela.resizable(False, False)
        janela.transient(self.root)
        janela.grab_set()
        
        # Frame principal
        frame = tk.Frame(janela, bg=COR_FUNDO, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        tk.Label(frame, text=f"Deletar {tipo.capitalize()}", 
                bg=COR_FUNDO, fg=COR_TEXTO, font=("Calibri", 16, "bold")).pack(pady=(0, 20))
        
        # Listar itens para deletar
        if tipo == "receita":
            itens = self.crud.listar_receitas()
            titulo = "Receitas:"
        else:
            itens = self.crud.listar_despesas()
            titulo = "Despesas:"
        
        tk.Label(frame, text=titulo, bg=COR_FUNDO, fg=COR_TEXTO, 
                font=("Calibri", 11)).pack(anchor="w", pady=(5, 5))
        
        # Frame para a listbox com scrollbar
        frame_lista = tk.Frame(frame, bg=COR_FUNDO)
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Listbox para selecionar item
        listbox = tk.Listbox(frame_lista, bg=COR_CARD, fg=COR_TEXTO, 
                        selectbackground=COR_DESTAQUE, font=("Calibri", 10),
                        height=10)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)
        
        # Preencher listbox
        for item in itens:
            # item[0] = id, item[1] = nome, item[2] = valor, item[3] = data
            listbox.insert(tk.END, f"ID: {item[0]} - {item[1]} - R$ {item[2]:.2f} - {item[3]}")
        
        # Botões
        frame_botoes = tk.Frame(frame, bg=COR_FUNDO)
        frame_botoes.pack(fill=tk.X)
        
        def deletar():
            selecionado = listbox.curselection()
            if not selecionado:
                messagebox.showerror("Erro", "Selecione um item para deletar!")
                return
            
            index = selecionado[0]
            item_selecionado = listbox.get(index)
            
            # Extrair o ID do item selecionado
            try:
                id_item = int(item_selecionado.split(" - ")[0].replace("ID: ", ""))
            except (ValueError, IndexError):
                messagebox.showerror("Erro", "Erro ao identificar o item selecionado!")
                return
            
            # Confirmar exclusão
            confirmacao = messagebox.askyesno(
                "Confirmar Exclusão", 
                f"Tem certeza que deseja excluir este item?\n{item_selecionado}"
            )
            
            if not confirmacao:
                return
            
            try:
                if tipo == "receita":
                    self.crud.deletar_receita(id_item)
                    messagebox.showinfo("Sucesso", "Receita deletada com sucesso!")
                else:
                    self.crud.deletar_despesa(id_item)
                    messagebox.showinfo("Sucesso", "Despesa deletada com sucesso!")
                
                # Atualizar a interface
                self.atualizar_tabelas()
                janela.destroy()
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar: {str(e)}")
        
        btn_deletar = ttk.Button(frame_botoes, text="Deletar", command=deletar)
        btn_deletar.pack(side=tk.RIGHT, padx=(10, 0))
        
        btn_cancelar = ttk.Button(frame_botoes, text="Cancelar", command=janela.destroy)
        btn_cancelar.pack(side=tk.RIGHT)
        
        
        
    def voltar_inicio(self):
        self.atualizar_tabelas()
        self.atualizar_interface()
        self.atualizar_dashboard()

    def mostrar_sobre(self):
        messagebox.showinfo("Sobre", "Gestor de Despesas v1.0\n\nDesenvolvido para gerenciar suas finanças pessoais.")
        
    def abrir_calendario(self):
        """Abre a janela do calendário"""
        if self.calendario.janela_calendario and self.calendario.janela_calendario.winfo_exists():
            self.calendario.janela_calendario.lift()
            self.calendario.janela_calendario.focus_set()
        else:
            self.calendario.criar_janela_calendario()

    def atualizar_interface(self):
        try:
            self.atualizar_tabelas()

            # Atualiza calendário se estiver aberto
            if hasattr(self, "calendario") and self.calendario.janela_calendario and self.calendario.janela_calendario.winfo_exists():
                self.calendario.atualizar_calendario()

            messagebox.showinfo("Atualizado", "Interface atualizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar: {str(e)}")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()
    
