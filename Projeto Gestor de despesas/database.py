import sqlite3

class Database:
    def __init__(self, db_name="gestor.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS receitas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                valor REAL NOT NULL,
                data TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS despesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                valor REAL NOT NULL,
                data TEXT
            )
        """)
        conn.commit()
        conn.close()

    def insert_receita(self, nome, valor, data):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO receitas (nome, valor, data) VALUES (?, ?, ?)", (nome, valor, data))
        conn.commit()
        conn.close()

    def insert_despesa(self, nome, valor, data):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO despesas (nome, valor, data) VALUES (?, ?, ?)", (nome, valor, data))
        conn.commit()
        conn.close()

    def delete_receita(self, nome):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM receitas WHERE nome = ?", (nome,))
        conn.commit()
        conn.close()

    def delete_despesa(self, nome):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM despesas WHERE nome = ?", (nome,))
        conn.commit()
        conn.close()

    def fetch_receitas(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, valor, data FROM receitas")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def fetch_despesas(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, valor, data FROM despesas")
        rows = cursor.fetchall()
        conn.close()
        return rows


