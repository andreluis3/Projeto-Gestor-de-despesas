import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from datetime import datetime, timedelta
import calendar
import json
import os

class CalendarioDespesas:
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app
        self.janela_calendario = None
        self.despesas_recorrentes = []
        self.categorias = self.carregar_categorias()
        
        # Carregar despesas salvas
        self.carregar_despesas()
    
    def carregar_categorias(self):
        """Carrega categorias padrão com cores"""
        return {
            "Academia": "#FF6B6B",
            "Aluguel": "#4ECDC4",
            "Supermercado": "#45B7D1",
            "Transporte": "#96CEB4",
            "Luz": "#FECA57",
            "Água": "#FF9FF3",
            "Internet": "#54A0FF",
            "Telefone": "#5F27CD",
            "Outros": "#95AFBA"
        }
    
    def carregar_despesas(self):
        """Carrega despesas do arquivo JSON"""
        try:
            if os.path.exists('despesas_recorrentes.json'):
                with open('despesas_recorrentes.json', 'r', encoding='utf-8') as f:
                    self.despesas_recorrentes = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar despesas: {e}")
            self.despesas_recorrentes = []
    
    def salvar_despesas(self):
        """Salva despesas no arquivo JSON"""
        try:
            with open('despesas_recorrentes.json', 'w', encoding='utf-8') as f:
                json.dump(self.despesas_recorrentes, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Sucesso", "Despesas salvas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar despesas: {e}")
    
    def abrir_calendario(self):
        """Abre a janela do calendário"""
        if self.janela_calendario is None or not self.janela_calendario.winfo_exists():
            self.criar_janela_calendario()
        else:
            self.janela_calendario.lift()
            self.janela_calendario.focus_set()
    
    def criar_janela_calendario(self):
        """Cria a janela do calendário"""
        self.janela_calendario = tk.Toplevel(self.parent)
        self.janela_calendario.title("📅 Calendário de Despesas Recorrentes")
        self.janela_calendario.geometry("900x700")
        self.janela_calendario.configure(bg="#1E1E1E")
        
        # Frame principal
        main_frame = tk.Frame(self.janela_calendario, bg="#1E1E1E", padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Botões superiores
        btn_frame = tk.Frame(main_frame, bg="#1E1E1E")
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(btn_frame, text="➕ Nova Despesa", 
                  command=self.cadastrar_despesa_recorrente).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="💾 Salvar Tudo", 
                  command=self.salvar_despesas).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🔔 Alertas", 
                  command=self.mostrar_alertas).pack(side=tk.LEFT, padx=5)
        
        # Calendário
        self.criar_calendario_widget(main_frame)
        
        # Lista de despesas
        self.criar_lista_despesas(main_frame)
        
        self.atualizar_calendario()
    
    def criar_calendario_widget(self, parent):
        """Cria o widget do calendário"""
        cal_frame = tk.Frame(parent, bg="#252526", bd=1, relief=tk.SOLID)
        cal_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Cabeçalho com navegação
        header_frame = tk.Frame(cal_frame, bg="#252526")
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(header_frame, text="◀", 
                  command=self.mes_anterior, width=3).pack(side=tk.LEFT)
        
        self.mes_ano_label = tk.Label(header_frame, text="", 
                                     bg="#252526", fg="#CCCCCC", 
                                     font=("Arial", 14, "bold"))
        self.mes_ano_label.pack(side=tk.LEFT, expand=True)
        
        ttk.Button(header_frame, text="▶", 
                  command=self.mes_proximo, width=3).pack(side=tk.RIGHT)
        
        # Dias da semana
        dias_frame = tk.Frame(cal_frame, bg="#252526")
        dias_frame.pack(fill=tk.X, padx=10)
        
        dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
        for dia in dias_semana:
            lbl = tk.Label(dias_frame, text=dia, bg="#252526", fg="#CCCCCC", 
                          font=("Arial", 10, "bold"), width=10)
            lbl.pack(side=tk.LEFT, padx=2, pady=5)
        
        # Grid dos dias
        self.dias_grid = []
        grid_frame = tk.Frame(cal_frame, bg="#252526")
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for i in range(6):
            row = []
            for j in range(7):
                cell = tk.Frame(grid_frame, bg="#2D2D30", bd=1, relief=tk.RAISED,
                               width=100, height=80)
                cell.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                cell.grid_propagate(False)
                
                # Labels dentro da célula
                num_label = tk.Label(cell, text="", bg="#2D2D30", fg="#CCCCCC",
                                   font=("Arial", 10, "bold"))
                num_label.place(x=5, y=5)
                
                cat_label = tk.Label(cell, text="", bg="#2D2D30", fg="#CCCCCC",
                                   font=("Arial", 8))
                cat_label.place(x=5, y=25)
                
                val_label = tk.Label(cell, text="", bg="#2D2D30", fg="#CCCCCC",
                                   font=("Arial", 8, "bold"))
                val_label.place(x=5, y=40)
                
                cell.bind("<Button-1>", lambda e, row=i, col=j: self.clicar_dia(row, col))
                
                row.append({
                    'frame': cell,
                    'numero': num_label,
                    'categoria': cat_label,
                    'valor': val_label
                })
            self.dias_grid.append(row)
            
        # Configurar grid
        for i in range(6):
            grid_frame.rowconfigure(i, weight=1)
        for j in range(7):
            grid_frame.columnconfigure(j, weight=1)
    
    def criar_lista_despesas(self, parent):
        """Cria a lista de despesas do dia selecionado"""
        lista_frame = tk.LabelFrame(parent, text="Despesas do Dia", 
                                  bg="#1E1E1E", fg="#CCCCCC",
                                  font=("Arial", 10, "bold"))
        lista_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.lista_despesas = tk.Listbox(lista_frame, height=6, bg="#252526", 
                                       fg="#CCCCCC", font=("Arial", 10),
                                       selectbackground="#007ACC")
        self.lista_despesas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(lista_frame, orient=tk.VERTICAL, 
                                 command=self.lista_despesas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_despesas.config(yscrollcommand=scrollbar.set)
    
    def atualizar_calendario(self):
        """Atualiza o calendário com o mês atual"""
        if not hasattr(self, 'dias_grid'):
            return
            
        hoje = datetime.now()
        if not hasattr(self, 'data_atual'):
            self.data_atual = hoje
        
        # Atualizar label do mês/ano
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.mes_ano_label.config(text=f"{meses[self.data_atual.month-1]} {self.data_atual.year}")
        
        # Limpar grid
        for i in range(6):
            for j in range(7):
                cell = self.dias_grid[i][j]
                cell['numero'].config(text="")
                cell['categoria'].config(text="")
                cell['valor'].config(text="")
                cell['frame'].config(bg="#2D2D30")
        
        # Preencher grid
        primeiro_dia = self.data_atual.replace(day=1)
        dias_no_mes = calendar.monthrange(self.data_atual.year, self.data_atual.month)[1]
        
        linha = 0
        coluna = primeiro_dia.weekday()
        
        for dia in range(1, dias_no_mes + 1):
            data_dia = self.data_atual.replace(day=dia)
            cell = self.dias_grid[linha][coluna]
            
            cell['numero'].config(text=str(dia))
            
            # Verificar se é hoje
            if data_dia.date() == hoje.date():
                cell['frame'].config(bg="#3E3E42")
            
            # Verificar despesas
            despesas = self.obter_despesas_do_dia(data_dia)
            if despesas:
                cor = self.categorias.get(despesas[0]['categoria'], "#FF6B6B")
                cell['frame'].config(bg=cor)
                
                if len(despesas) == 1:
                    cell['categoria'].config(text=despesas[0]['categoria'])
                    cell['valor'].config(text=f"R$ {despesas[0]['valor']:.2f}")
                else:
                    cell['categoria'].config(text=f"{len(despesas)} despesas")
                    total = sum(d['valor'] for d in despesas)
                    cell['valor'].config(text=f"R$ {total:.2f}")
            
            coluna += 1
            if coluna == 7:
                coluna = 0
                linha += 1
    
    def mes_anterior(self):
        if self.data_atual.month == 1:
            self.data_atual = self.data_atual.replace(year=self.data_atual.year-1, month=12)
        else:
            self.data_atual = self.data_atual.replace(month=self.data_atual.month-1)
        self.atualizar_calendario()
    
    def mes_proximo(self):
        if self.data_atual.month == 12:
            self.data_atual = self.data_atual.replace(year=self.data_atual.year+1, month=1)
        else:
            self.data_atual = self.data_atual.replace(month=self.data_atual.month+1)
        self.atualizar_calendario()
    
    def clicar_dia(self, row, col):
        texto = self.dias_grid[row][col]['numero'].cget("text")
        if texto:
            dia = int(texto)
            data_selecionada = self.data_atual.replace(day=dia)
            self.mostrar_despesas_dia(data_selecionada)
    
    def mostrar_despesas_dia(self, data):
        self.lista_despesas.delete(0, tk.END)
        despesas = self.obter_despesas_do_dia(data)
        
        if not despesas:
            self.lista_despesas.insert(0, f"Nenhuma despesa para {data.strftime('%d/%m/%Y')}")
        else:
            for desp in despesas:
                self.lista_despesas.insert(tk.END, 
                    f"{desp['categoria']}: R$ {desp['valor']:.2f} - {desp['descricao']}")
    
    def obter_despesas_do_dia(self, data):
        return [d for d in self.despesas_recorrentes 
                if d['dia'] == data.day and d['mes'] == data.month and d['ano'] == data.year]
    
    def cadastrar_despesa_recorrente(self):
        """Janela para cadastrar nova despesa recorrente"""
        janela = tk.Toplevel(self.janela_calendario or self.parent)
        janela.title("Nova Despesa Recorrente")
        janela.geometry("400x500")
        janela.configure(bg="#1E1E1E")
       
    
    def mostrar_alertas(self):
        """Mostra alertas de despesas próximas"""
        hoje = datetime.now()
        alertas = []
        
        for desp in self.despesas_recorrentes:
            data_desp = datetime(desp['ano'], desp['mes'], desp['dia'])
            dias_restantes = (data_desp - hoje).days
            
            if 0 <= dias_restantes <= 7:  # Despesas nos próximos 7 dias
                alertas.append(f"{data_desp.strftime('%d/%m')}: {desp['categoria']} - R$ {desp['valor']:.2f}")
        
        if alertas:
            mensagem = "Despesas próximas:\n\n" + "\n".join(alertas)
            messagebox.showwarning("Alertas de Despesas", mensagem)
        else:
            messagebox.showinfo("Alertas", "Nenhuma despesa próxima encontrada.")
            