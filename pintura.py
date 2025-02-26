from obra_de_arte import ObraDeArte

class Pintura(ObraDeArte):
    def __init__(self, titulo, ano, artista, tecnica):
        super().__init__(titulo, ano, artista)
        self.tecnica = tecnica

    def exibir_info(self):
        return f"Pintura: {super().exibir_info()} - Técnica: {self.tecnica}"
