from interface import InterfaceApp
from database import Database
from dashboard import Dashboard
from calendario import CalendarioDespesas
import tkinter as tk
import os




class App:
    def __init__(self):
        self.db = Database()
        self.dashboard = Dashboard()
        
        self.root = tk.Tk()
        self.root.title("Gestor de Despesas - Dashboard")
        self.root.geometry("1200x700")
        
        # Inicializar a interface
        self.ui = InterfaceApp(self.root)
        
        # Inicializar o calendário
        self.calendario = CalendarioDespesas(self.root, self)
        
        # Tornar o calendário acessível pela interface
        self.ui.calendario = self.calendario
        
        # Adicionar menu Calendário à interface existente
        self.adicionar_menu_calendario()

    def adicionar_menu_calendario(self):
        try:
            # Aguardar a interface criar o menu
            self.root.after(100, self._adicionar_menu_delay)
        except Exception as e:
            print(f"Erro ao agendar adição do menu: {e}")

    def _adicionar_menu_delay(self):
        """Adiciona o menu após um delay para garantir que a interface esteja criada"""
        try:
            # Verificar se a barra de menus existe
            if hasattr(self.root, 'menu') and self.root.menu:
                # Criar menu Calendário
                menu_calendario = tk.Menu(self.root.menu, tearoff=0,
                                        bg="#2D2D30", 
                                        fg="#CCCCCC",
                                        activebackground="#3E3E42",
                                        activeforeground="#CCCCCC",
                                        bd=1,
                                        relief="solid")
                
                menu_calendario.add_command(label="Abrir Calendário", 
                                          command=self.calendario.abrir_calendario)
                menu_calendario.add_command(label="Cadastrar Despesa Recorrente", 
                                          command=self.calendario.cadastrar_despesa_recorrente)
                menu_calendario.add_separator()
                menu_calendario.add_command(label="Ver Alertas de Despesas", 
                                          command=self.calendario.mostrar_alertas)
                
                # Adicionar ao menu principal
                self.root.menu.add_cascade(label="📅 Calendário", menu=menu_calendario)
                
        except Exception as e:
            print(f"Erro ao adicionar menu calendário: {e}")
            self.criar_menu_fallback()

    def criar_menu_fallback(self):
        """Cria uma barra de menus alternativa"""
        try:
            # Criar nova barra de menus
            menu_bar = tk.Menu(self.root, 
                             bg="#2D2D30", 
                             fg="#CCCCCC",
                             activebackground="#3E3E42",
                             activeforeground="#CCCCCC",
                             tearoff=0)
            
            self.root.config(menu=menu_bar)
            
            # Menu Calendário
            menu_calendario = tk.Menu(menu_bar, tearoff=0,
                                    bg="#2D2D30", 
                                    fg="#CCCCCC",
                                    activebackground="#3E3E42",
                                    activeforeground="#CCCCCC",
                                    bd=1,
                                    relief="solid")
            
            menu_calendario.add_command(label="Abrir Calendário", 
                                      command=self.calendario.abrir_calendario)
            menu_calendario.add_command(label="Cadastrar Despesa Recorrente", 
                                      command=self.calendario.cadastrar_despesa_recorrente)
            menu_calendario.add_separator()
            menu_calendario.add_command(label="Ver Alertas de Despesas", 
                                      command=self.calendario.mostrar_alertas)
            
            menu_bar.add_cascade(label="📅 Calendário", menu=menu_calendario)
            
            # Menu básico para completar
            menu_arquivo = tk.Menu(menu_bar, tearoff=0,
                                 bg="#2D2D30", 
                                 fg="#CCCCCC",
                                 activebackground="#3E3E42",
                                 activeforeground="#CCCCCC")
            menu_arquivo.add_command(label="Sair", command=self.root.quit)
            menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
            
        except Exception as e:
            print(f"Erro ao criar menu fallback: {e}")

    def run(self):
        """Inicia a aplicação"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nAplicação encerrada pelo usuário")
        except Exception as e:
            print(f"Erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    app = App()
    app.run()