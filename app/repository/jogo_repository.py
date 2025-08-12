from app.database.connection import get_db
from app.models.jogo_model import JogoModel

class JogoRepository:
    
    def get_all_jogos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT j.id, j.nome, j.preco, j.desenvolvedor, j.categoria_id, c.nome, c.descricao
                       FROM jogos j
                       JOIN categorias c ON j.categoria_id = c.id """)
        rows = cursor.fetchall()
        jogos = []
        for row in rows:
            jogo = JogoModel(
                id=row[0],
                nome=row[1],
                preco=row[2],
                desenvolvedor=row[3],
                categoria_id=row[4]
            )
            jogo.categoria_nome = row[5]
            jogo.categoria_descricao = row[6]
            jogos.append(jogo)
        return jogos
    
    
    def get_jogo_by_id(self, jogo_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT j.id, j.nome, j.preco, j.desenvolvedor, j.categoria_id, c.nome
                       FROM jogos j
                       JOIN categorias c ON j.categoria_id = c.id
                       WHERE j.id = ?""", (jogo_id,))
        row = cursor.fetchone()
        if row:
            jogo = JogoModel(
                id=row[0],
                nome=row[1],
                preco=row[2],
                desenvolvedor=row[3],
                categoria_id=row[4]
            )
            jogo.categoria_nome = row[5]
            return jogo
        
        
    def create_jogo(self, jogo):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       INSERT INTO jogos (nome, preco, desenvolvedor, categoria_id)
                       VALUES (?, ?, ?, ?)""",
                       (jogo.get_nome(), jogo.get_preco(), jogo.get_desenvolvedor(), jogo.get_categoria_id()))
        connection.commit()
        
    def update_jogo(self, jogo):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE jogos
                       SET nome = ?, preco = ?, desenvolvedor = ?, categoria_id = ?
                       WHERE id = ?""",
                       (jogo.get_nome(), jogo.get_preco(), jogo.get_desenvolvedor(), jogo.get_categoria_id(), jogo.get_id()))
        connection.commit()
        
    def delete_jogo(self, jogo_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM jogos WHERE id = ?", (jogo_id,))
        connection.commit()
        
    def get_jogos_by_categoria_id(self, categoria_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SElECT * FROM jogos WHERE categoria_id = ?", (categoria_id,))
        return cursor.fetchall()