class Formacao:
    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao