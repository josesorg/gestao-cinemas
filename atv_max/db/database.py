import sqlite3

def get_connection():
    conn = sqlite3.connect("cinemas.db")
    # Habilita chaves estrangeiras no SQLite
    conn.execute("PRAGMA foreign_keys = ON") 
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            capacidade_maxima INTEGER NOT NULL
        )
    """)
    
    return conn