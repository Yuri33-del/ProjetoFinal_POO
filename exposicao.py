class Exposicao:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        print(f"Exposição: {self.nome}")
        for item in self.itens:
            print(item.exibir_info())
