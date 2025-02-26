from pessoa import Artista
from escultura import Escultura
from pintura import Pintura
from exposicao import Exposicao

# Criando artistas
artista1 = Artista("Leonardo da Vinci", "Itália", "Renascimento")
artista2 = Artista("Auguste Rodin", "França", "Escultura")
artista3 = Artista("Vincent van Gogh", "Paises Baixos", "Pintura")
artista4 = Artista("Michelangelo", "Itália", "Escultura")
# Criando obras
pintura1 = Pintura("Mona Lisa", 1503, artista1, "Pintura a óleo")
pintura2 = Pintura("A Noite Estrelada", 1889, artista3, "Pintura a óleo")
escultura1 = Escultura("O Pensador", 1904, artista2, "Bronze", 1.89)
escultura2 = Escultura("Davi", "1504", artista4, "Mármore de Carrara", 5.17)
escultura3 = Escultura("A Pietà de Michelangelo","1499", artista4, "Mármore", 1.74)

# Criando exposição
expo = Exposicao("Grandes Clássicos")

# Adicionando obras à exposição
expo.adicionar_item(pintura1)
expo.adicionar_item(pintura2)
expo.adicionar_item(escultura1)
expo.adicionar_item(escultura2)
expo.adicionar_item(escultura3)
# Exibindo a exposição
expo.listar_itens()
