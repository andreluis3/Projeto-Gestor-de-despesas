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

    def deletar_receita(self, id_receita):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM receitas WHERE id = ?", (id_receita,))
        conn.commit()
        conn.close()
        

    def deletar_despesa(self, id_despesa):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM despesas WHERE id = ?", (id_despesa,))
        conn.commit()
        conn.close()

    def buscar_receita_por_nome(self, nome):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM receitas WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] if resultado else None

    def buscar_despesa_por_nome(self, nome):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM despesas WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] if resultado else None