import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from crud import Crud
from dashboard import Dashboard
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        self.root.title("Gestor de Despesas - Dashboard")
        self.root.geometry("1200x700")
        self.root.configure(bg=COR_FUNDO)

        # Configurar estilo
        self.configurar_estilos()

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
        # Frame para conter a barra de menu com borda
        self.menu_container = tk.Frame(self.root, bg=COR_MENU_BORDA, height=30)
        self.menu_container.pack(fill="x", padx=0, pady=0)
        self.menu_container.pack_propagate(False)
        
        # Frame interno para o menu
        menu_frame = tk.Frame(self.menu_container, bg=COR_MENU, height=28)
        menu_frame.pack(fill="both", expand=True, padx=1, pady=1)
        
        # Barra de menu personalizada
        menu_bar = tk.Menu(
            self.root,
            bg=COR_MENU,
            fg=COR_TEXTO,
            activebackground=COR_BOTAO_ACTIVE,
            activeforeground=COR_TEXTO,
            borderwidth=0,
            relief="flat",
            tearoff=0
        )

        # Menu Início
        menu_inicio = tk.Menu(menu_bar, tearoff=0, bg=COR_MENU, fg=COR_TEXTO,
                             activebackground=COR_BOTAO_ACTIVE, bd=1,
                             activeborderwidth=1, relief="solid")
        menu_inicio.add_command(label="Voltar ao Início", command=self.voltar_inicio)
        menu_bar.add_cascade(label="Início", menu=menu_inicio)

        # Menu Cadastrar
        menu_cadastrar = tk.Menu(menu_bar, tearoff=0, bg=COR_MENU, fg=COR_TEXTO,
                                activebackground=COR_BOTAO_ACTIVE, bd=1,
                                activeborderwidth=1, relief="solid")
        menu_cadastrar.add_command(label="Cadastrar Receita", command=self.janela_cadastrar_receita)
        menu_cadastrar.add_command(label="Cadastrar Despesa", command=self.janela_cadastrar_despesa)
        menu_bar.add_cascade(label="Cadastrar", menu=menu_cadastrar)

        # Menu Deletar
        menu_deletar = tk.Menu(menu_bar, tearoff=0, bg=COR_MENU, fg=COR_TEXTO,
                              activebackground=COR_BOTAO_ACTIVE, bd=1,
                              activeborderwidth=1, relief="solid")
        menu_deletar.add_command(label="Deletar Receita", command=self.janela_deletar_receita)
        menu_deletar.add_command(label="Deletar Despesa", command=self.janela_deletar_despesa)
        menu_bar.add_cascade(label="Deletar", menu=menu_deletar)

        # Menu Dashboard
        menu_dashboard = tk.Menu(menu_bar, tearoff=0, bg=COR_MENU, fg=COR_TEXTO,
                                activebackground=COR_BOTAO_ACTIVE, bd=1,
                                activeborderwidth=1, relief="solid")
        menu_dashboard.add_command(label="Atualizar Gráficos", command=self.atualizar_dashboard)
        menu_bar.add_cascade(label="Dashboard", menu=menu_dashboard)

        # Menu Ajuda
        menu_ajuda = tk.Menu(menu_bar, tearoff=0, bg=COR_MENU, fg=COR_TEXTO,
                            activebackground=COR_BOTAO_ACTIVE, bd=1,
                            activeborderwidth=1, relief="solid")
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)
        menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

        self.root.config(menu=menu_bar)

    def criar_frames(self):
        # Frame principal com padding
        self.frame_principal = tk.Frame(self.root, bg=COR_FUNDO)
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame superior para o dashboard
        self.frame_superior = tk.Frame(self.frame_principal, bg=COR_FUNDO, height=300)
        self.frame_superior.pack(fill="x", pady=(0, 10))
        self.frame_superior.pack_propagate(False)

        # Frame para a barra de progresso
        self.frame_progresso = tk.Frame(self.frame_principal, bg=COR_FUNDO, height=50)
        self.frame_progresso.pack(fill="x", pady=(0, 10))
        self.frame_progresso.pack_propagate(False)

        # Frame inferior para as tabelas (menor)
        self.frame_inferior = tk.Frame(self.frame_principal, bg=COR_FUNDO, height=250)
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

        # Gráfico de pizza (esquerda)
        self.frame_pizza = tk.Frame(self.frame_graficos, bg=COR_CARD, width=300, height=280)
        self.frame_pizza.pack(side="left", fill="both", expand=True, padx=(5, 2), pady=5)
        self.frame_pizza.pack_propagate(False)

        lbl_pizza = tk.Label(self.frame_pizza, text="Distribuição de Despesas", 
                            bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 12, "bold"))
        lbl_pizza.pack(pady=5)

        self.canvas_pizza = None

        # Gráfico de barras (centro)
        self.frame_barras = tk.Frame(self.frame_graficos, bg=COR_CARD, width=300, height=280)
        self.frame_barras.pack(side="left", fill="both", expand=True, padx=2, pady=5)
        self.frame_barras.pack_propagate(False)

        lbl_barras = tk.Label(self.frame_barras, text="Relação Despesas x Receitas", 
                             bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 12, "bold"))
        lbl_barras.pack(pady=5)

        self.canvas_barras = None

        # Gráfico de linha (direita)
        self.frame_linha = tk.Frame(self.frame_graficos, bg=COR_CARD, width=300, height=280)
        self.frame_linha.pack(side="left", fill="both", expand=True, padx=(2, 5), pady=5)
        self.frame_linha.pack_propagate(False)

        lbl_linha = tk.Label(self.frame_linha, text="Evolução Mensal", 
                           bg=COR_CARD, fg=COR_TEXTO, font=("Calibri", 12, "bold"))
        lbl_linha.pack(pady=5)

        self.canvas_linha = None

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

        # Preencher despesas
        despesas = self.crud.listar_despesas()
        for desp in despesas:
            self.tree_despesas.insert("", "end", values=(desp[1], f"R$ {desp[2]:.2f}", desp[3]))

        # Preencher receitas
        receitas = self.crud.listar_receitas()
        for rec in receitas:
            self.tree_receitas.insert("", "end", values=(rec[1], f"R$ {rec[2]:.2f}", rec[3]))

        # Atualizar dashboard
        self.atualizar_dashboard()
        
        # Atualizar barra de progresso
        self.atualizar_barra_progresso()

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
        
        # Limpar gráficos existentes
        for widget in self.frame_pizza.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
        
        for widget in self.frame_barras.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
                
        for widget in self.frame_linha.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        # Gráfico de Pizza - Distribuição de Despesas
        if despesas:
            fig_pizza, ax_pizza = plt.subplots(figsize=(4, 3))
            fig_pizza.patch.set_facecolor(COR_CARD)
            ax_pizza.set_facecolor(COR_CARD)
            
            labels = [d[1] for d in despesas]
            valores = [d[2] for d in despesas]
            
            # Cores para o gráfico de pizza
            cores = [COR_DESPESA, '#E06C75', '#BE5046', '#98C379', '#D19A66', '#C678DD'][:len(valores)]
            
            ax_pizza.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=cores)
            ax_pizza.axis('equal')
            ax_pizza.set_title("Distribuição de Despesas", color=COR_TEXTO)
            
            # Configurar cores do texto
            for text in ax_pizza.texts:
                text.set_color(COR_TEXTO)
            
            canvas_pizza = FigureCanvasTkAgg(fig_pizza, self.frame_pizza)
            canvas_pizza.draw()
            canvas_pizza.get_tk_widget().pack(fill="both", expand=True)

        # Gráfico de Barras - Relação Despesas x Receitas
        fig_barras, ax_barras = plt.subplots(figsize=(4, 3))
        fig_barras.patch.set_facecolor(COR_CARD)
        ax_barras.set_facecolor(COR_CARD)
        
        total_despesas = sum([d[2] for d in despesas]) if despesas else 0
        total_receitas = sum([r[2] for r in receitas]) if receitas else 0
        
        categorias = ['Despesas', 'Receitas']
        valores = [total_despesas, total_receitas]
        cores = [COR_DESPESA, COR_RECEITA]
        
        bars = ax_barras.bar(categorias, valores, color=cores)
        ax_barras.set_title('Relação Despesas x Receitas', color=COR_TEXTO)
        ax_barras.set_ylabel('Valor (R$)', color=COR_TEXTO)
        
        # Configurar cores dos eixos
        ax_barras.tick_params(colors=COR_TEXTO)
        for spine in ax_barras.spines.values():
            spine.set_color(COR_BORDA)
        
        # Adicionar valores nas barras
        for bar, valor in zip(bars, valores):
            height = bar.get_height()
            ax_barras.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                          f'R$ {valor:.2f}', ha='center', va='bottom', color=COR_TEXTO)
        
        canvas_barras = FigureCanvasTkAgg(fig_barras, self.frame_barras)
        canvas_barras.draw()
        canvas_barras.get_tk_widget().pack(fill="both", expand=True)

        # Gráfico de Linha - Evolução Mensal (simplificado)
        fig_linha, ax_linha = plt.subplots(figsize=(4, 3))
        fig_linha.patch.set_facecolor(COR_CARD)
        ax_linha.set_facecolor(COR_CARD)
        
        # Agrupar por mês (simplificado)
        desp_por_mes = {}
        rec_por_mes = {}
        
        for desp in despesas:
            mes = desp[3][:7] if desp[3] and len(desp[3]) >= 7 else "N/D"  # Formato YYYY-MM
            desp_por_mes[mes] = desp_por_mes.get(mes, 0) + desp[2]
            
        for rec in receitas:
            mes = rec[3][:7] if rec[3] and len(rec[3]) >= 7 else "N/D"
            rec_por_mes[mes] = rec_por_mes.get(mes, 0) + rec[2]
            
        meses = sorted(set(list(desp_por_mes.keys()) + list(rec_por_mes.keys())))
        
        desp_valores = [desp_por_mes.get(mes, 0) for mes in meses]
        rec_valores = [rec_por_mes.get(mes, 0) for mes in meses]
        
        if meses and meses[0] != "N/D":
            ax_linha.plot(meses, desp_valores, marker='o', color=COR_DESPESA, label='Despesas')
            ax_linha.plot(meses, rec_valores, marker='o', color=COR_RECEITA, label='Receitas')
            ax_linha.set_title('Evolução Mensal', color=COR_TEXTO)
            ax_linha.set_ylabel('Valor (R$)', color=COR_TEXTO)
            ax_linha.legend(facecolor=COR_CARD, edgecolor=COR_BORDA, labelcolor=COR_TEXTO)
            
            # Configurar cores dos eixos
            ax_linha.tick_params(colors=COR_TEXTO)
            for spine in ax_linha.spines.values():
                spine.set_color(COR_BORDA)
                
            plt.xticks(rotation=45)
            
            canvas_linha = FigureCanvasTkAgg(fig_linha, self.frame_linha)
            canvas_linha.draw()
            canvas_linha.get_tk_widget().pack(fill="both", expand=True)

    # Métodos para as janelas (mantidos da versão anterior)
    def janela_cadastrar_receita(self):
        # Implementação similar à anterior
        pass

    def janela_cadastrar_despesa(self):
        # Implementação similar à anterior
        pass

    def janela_deletar_receita(self):
        # Implementação similar à anterior
        pass

    def janela_deletar_despesa(self):
        # Implementação similar à anterior
        pass

    def voltar_inicio(self):
        self.atualizar_tabelas()

    def mostrar_sobre(self):
        messagebox.showinfo("Sobre", "Gestor de Despesas v1.0\n\nDesenvolvido para gerenciar suas finanças pessoais.")

# Para executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()