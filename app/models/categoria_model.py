class CategoriaModel:
    def __init__(self, id, nome, descricao, plataforma):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__plataforma = plataforma
        
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao

    def get_plataforma(self):
        return self.__plataforma
            
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def set_plataforma(self, plataforma):
        self.__plataforma = plataforma