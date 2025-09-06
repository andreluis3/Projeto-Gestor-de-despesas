from interface import InterfaceApp
from database import Database
from dashboard import Dashboard
import tkinter as tk

class App:
    def __init__(self):
        self.db = Database()
        self.dashboard = Dashboard()
        
        self.root = tk.Tk()
        self.ui = InterfaceApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()