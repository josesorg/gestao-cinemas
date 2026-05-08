from db.database import get_connection

class CinemaRepository:
    def salvar(self, cinema):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cinemas (nome, endereco, capacidade_maxima)
            VALUES (?, ?, ?)
        """, (cinema.nome, cinema.endereco, cinema.capacidade_maxima))
        conn.commit()
        conn.close()