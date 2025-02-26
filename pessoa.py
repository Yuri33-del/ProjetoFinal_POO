class Pessoa:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome                    # Encapsulamento
        self.__nacionalidade = nacionalidade

    # Getters
    def get_nome(self):
        return self.__nome
    
    def get_nacionalidade(self):
        return self.__nacionalidade

class Artista(Pessoa):
    def __init__(self, nome, nacionalidade, estilo):
        super().__init__(nome, nacionalidade)  # Herança
        self.estilo = estilo

    def apresentar(self):
        return f"Artista: {self.get_nome()} ({self.get_nacionalidade()}) - Estilo: {self.estilo}"
