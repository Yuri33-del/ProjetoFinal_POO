from item_exposicao import ItemExposicao

class ObraDeArte(ItemExposicao):
    def __init__(self, titulo, ano, artista):
        super().__init__(titulo, ano)
        self.artista = artista

    def exibir_info(self):
        return f"'{self.get_titulo()}' ({self.get_ano()}) - {self.artista.get_nome()}"
