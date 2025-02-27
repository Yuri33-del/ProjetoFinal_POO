# ProjetoFinal_POO

Sistema de Gestão de Museu 
 Descrição
Este projeto é um sistema de gestão de exposições de museu, desenvolvido em Python usando Programação Orientada a Objetos (POO).

Ele permite cadastrar artistas e suas obras de arte, como pinturas e esculturas, além de exibir informações sobre as exposições.

 Recursos Implementados:
 Cadastro de artistas e obras
 Suporte para Pinturas e Esculturas
 Organização das obras em Exposições
 Uso dos pilares da POO: Herança, Polimorfismo, Encapsulamento e Abstração

 Como Executar o Projeto
 Rodando no VS Code (Recomendado para Iniciantes)
Instale o Python se ainda não tiver.
Instale o VS Code e o plugin de Python.
Clone o repositório ou baixe o código:
bash
Copiar
Editar
git clone https://github.com/seu-usuario/museu-poo.git
cd museu-poo
Abra o VS Code e execute main.py:
No Explorer, clique com o botão direito no main.py e selecione "Run Python File".
 Rodando no PyCharm
Instale o PyCharm e abra o projeto.
Se precisar, crie um ambiente virtual (File > Settings > Project > Python Interpreter).
Execute o main.py clicando no botão Run .
 Rodando Online (Google Colab ou Replit)
Caso não queira instalar nada, pode rodar o código online:

Google Colab (Copie e cole o código lá):
Acesse: Google Colab
Clique em "Novo Notebook"
Cole os arquivos .py e execute
Replit (mais fácil para rodar projetos inteiros):
Acesse: Replit
Clique em "Create Python Repl"
Faça upload dos arquivos .py e execute main.py
 Estrutura do Projeto
bash
Copiar
Editar
museu/
── main.py                # Arquivo principal
── pessoa.py              # Classe Pessoa e Artista
── item_exposicao.py      # Classe abstrata ItemExposicao├── obra_de_arte.py        # Classe base para obras de arte
── escultura.py           # Subclasse para Esculturas
── pintura.py             # Subclasse para Pinturas
── exposicao.py           # Classe para gerenciar Exposições
 Como o Código Funciona
  1. Cadastro de Artistas
Criamos artistas com nome, nacionalidade e estilo artístico:

python
Copiar
Editar
artista1 = Artista("Leonardo da Vinci", "Itália", "Renascimento")
 2. Cadastro de Obras de Arte
Criamos Pinturas e Esculturas, associando um artista a cada uma:

python
Copiar
Editar
pintura1 = Pintura("Mona Lisa", 1503, artista1, "Óleo sobre madeira")
escultura1 = Escultura("O Pensador", 1904, artista2, "Bronze", 1.89)
 3. Criando uma Exposição
Organizamos as obras em uma exposição e as exibimos:

python
Copiar
Editar
expo = Exposicao("Grandes Clássicos")
expo.adicionar_item(pintura1)
expo.adicionar_item(escultura1)

expo.listar_itens()
 Saída esperada no terminal:
vbnet
Copiar
Editar
Exposição: Grandes Clássicos
Pintura: 'Mona Lisa' (1503) - Leonardo da Vinci - Técnica: Óleo sobre madeira
Escultura: 'O Pensador' (1904) - Auguste Rodin - Material: Bronze, Altura: 1.89m
 Conceitos de POO Aplicados
 Herança → Pintura e Escultura herdam de ObraDeArte
 Polimorfismo → exibir_info() se comporta diferente em Pintura e Escultura
 Encapsulamento → Atributos privados com métodos getters e setters
 Abstração → ItemExposicao é uma classe abstrata
