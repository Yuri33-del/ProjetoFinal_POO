from obra_de_arte import ObraDeArte

class Escultura(ObraDeArte):
    def __init__(self, titulo, ano, artista, material, altura):
        super().__init__(titulo, ano, artista)
        self.material = material
        self.altura = altura

    def exibir_info(self):
        return f"Escultura: {super().exibir_info()} - Material: {self.material}, Altura: {self.altura}m"
