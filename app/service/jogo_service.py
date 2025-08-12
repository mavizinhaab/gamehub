from app.repository.jogo_repository import JogoRepository
from app.models.jogo_model import JogoModel

class JogoService:
    def __init__(self):
        self.jogo_repository = JogoRepository()

    def get_all_jogos(self):
        return self.jogo_repository.get_all_jogos()

    def get_jogo_by_id(self, jogo_id):
        if jogo_id is None:
            raise ValueError("O ID do jogo é obrigatório para a busca.")
        return self.jogo_repository.get_jogo_by_id(jogo_id)

    def create_jogo(self, jogo: JogoModel):
        if jogo.get_id() is not None:
            raise ValueError("Não é permitido informar um ID ao criar um novo jogo.")
        if not jogo.get_nome() or not jogo.get_desenvolvedor() or jogo.get_preco() is None:
            raise ValueError("Nome, desenvolvedor e preço do jogo são obrigatórios.")
        if len(jogo.get_nome()) < 3:
            raise ValueError("O nome do jogo deve conter pelo menos 3 caracteres.")
        if jogo.get_nome().isdigit():
            raise ValueError("O nome do jogo não pode ser apenas números.")
        if len(jogo.get_desenvolvedor()) < 3:
            raise ValueError("O nome do desenvolvedor deve conter pelo menos 3 caracteres.")
        if jogo.get_preco() < 0:
            raise ValueError("O preço do jogo não pode ser negativo.")
        self.jogo_repository.create_jogo(jogo)

    def update_jogo(self, jogo: JogoModel):
        if jogo.get_id() is None:
            raise ValueError("O ID do jogo é obrigatório para a atualização.")
        if not jogo.get_nome() or not jogo.get_desenvolvedor() or jogo.get_preco() is None:
            raise ValueError("Nome, desenvolvedor e preço do jogo são obrigatórios.")
        if len(jogo.get_nome()) < 3:
            raise ValueError("O nome do jogo deve conter pelo menos 3 caracteres.")
        if jogo.get_nome().isdigit():
            raise ValueError("O nome do jogo não pode ser apenas números.")
        if len(jogo.get_desenvolvedor()) < 3:
            raise ValueError("O nome do desenvolvedor deve conter pelo menos 3 caracteres.")
        if jogo.get_preco() < 0:
            raise ValueError("O preço do jogo não pode ser negativo.")
        self.jogo_repository.update_jogo(jogo)

    def delete_jogo(self, jogo_id):
        if jogo_id is None:
            raise ValueError("O ID do jogo é obrigatório para a exclusão.")
        self.jogo_repository.delete_jogo(jogo_id)
