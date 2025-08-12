from app.repository.categoria_repository import CategoriaRepository 
from app.models.categoria_model import CategoriaModel
from app.repository.jogo_repository import JogoRepository

class CategoriaService:
    def __init__(self):
        self.categoria_repository = CategoriaRepository()
        self.jogo_repository = JogoRepository()
        
    def get_all_categorias(self):
        return self.categoria_repository.get_all_categorias()
    
    def get_categoria_by_id(self, categoria_id):
        if categoria_id is None:
            raise ValueError("O ID da categoria é obrigatório para a busca.")
        return self.categoria_repository.get_categoria_by_id(categoria_id)
    
    def create_categoria(self, categoria: CategoriaModel):
        if categoria.get_id() is not None:
            raise ValueError("Não é permitido informar um ID ao criar uma nova categoria.")
        if categoria.get_nome().isdigit():
            raise ValueError("O nome da categoria não pode ser apenas números.")
        if categoria.get_descricao().isdigit():
            raise ValueError("A descrição da categoria não pode ser apenas números.")
        if len(categoria.get_descricao()) < 8:
            raise ValueError("A descrição da categoria deve conter pelo menos 8 caracteres.")
        if not categoria.get_nome() or not categoria.get_descricao():
            raise ValueError("Informe o nome e a descrição da categoria.")
        if len(categoria.get_nome()) < 3:
            raise ValueError("O nome da categoria deve conter pelo menos 3 caracteres.")
        self.categoria_repository.create_categoria(categoria)
        
    def update_categoria(self, categoria: CategoriaModel):
        if categoria.get_id() is None:
            raise ValueError("O ID da categoria é obrigatório para a atualização.")
        if not categoria.get_nome() or not categoria.get_descricao():
            raise ValueError("Informe o nome e a descrição da categoria.")
        if categoria.get_nome().isdigit():
            raise ValueError("O nome da categoria não pode ser apenas números.")
        if categoria.get_descricao().isdigit():
            raise ValueError("A descrição da categoria não pode ser apenas números.")
        if len(categoria.get_descricao()) < 10:
            raise ValueError("A descrição da categoria deve conter pelo menos 10 caracteres.")
        if len(categoria.get_nome()) < 3:
            raise ValueError("O nome da categoria deve conter pelo menos 3 caracteres.")
        self.categoria_repository.update_categoria(categoria)
        
    def delete_categoria(self, categoria_id):
        if categoria_id is None:
            raise ValueError("O ID da categoria é obrigatório para a exclusão.")
        jogos = self.jogo_repository.get_all_jogos()
        for jogo in jogos:
            if jogo.get_categoria_id() == categoria_id:
                raise ValueError("Exclusão negada: esta categoria possui jogos cadastrados.")
        self.categoria_repository.delete_categoria(categoria_id)
