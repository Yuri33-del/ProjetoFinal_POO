from abc import ABC, abstractmethod

class ItemExposicao(ABC):
    def __init__(self, titulo, ano):
        self.__titulo = titulo
        self.__ano = ano

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_ano(self):
        return self.__ano

    @abstractmethod
    def exibir_info(self):
        pass
