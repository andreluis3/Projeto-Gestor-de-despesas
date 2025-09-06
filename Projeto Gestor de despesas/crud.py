import sqlite3
from database import Database

class Crud:
    def __init__(self):
        self.db = Database()

    def adicionar_receita(self, nome, valor, data):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO receitas (nome, valor, data) VALUES (?, ?, ?)",
            (nome, valor, data)
        )
        conn.commit()
        conn.close()

    def adicionar_despesa(self, nome, valor, data):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO despesas (nome, valor, data) VALUES (?, ?, ?)",
            (nome, valor, data)
        )
        conn.commit()
        conn.close()

   
    def listar_receitas(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM receitas")
        receitas = cursor.fetchall()
        conn.close()
        return receitas

    def listar_despesas(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM despesas")
        despesas = cursor.fetchall()
        conn.close()
        return despesas

   
    def deletar_receita(self, nome):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM receitas WHERE nome = ?", (nome,))
        conn.commit()
        conn.close()

    def deletar_despesa(self, nome):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM despesas WHERE nome = ?", (nome,))
        conn.commit()
        conn.close()
