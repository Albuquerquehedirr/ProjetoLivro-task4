# 1 Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
# 2 Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return  f'O livro {self.titulo}, que foi escrito por {self.autor} no ano de {self.ano_publicacao}.'

    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano_publicacao):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano_publicacao and livro.disponivel]
        return livros_disponiveis



livro1 = Livro('Ponto de inflexão', 'Flávio Augusto', 2019)
livro2 = Livro('Ou vai ou voa', 'Hendel Favarin', 2024)
livro3 = Livro('Seja foda', 'Caio Carneiro', 2017)
livro4 = Livro('O homem mais rico da babilônia', 'George Samuel Clason', 1926)
# print(livro1)
# print(livro2)
# 3 Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
# def emprestar(self):
#     self.disponivel = False

livro3 = Livro('Seja foda', 'Caio Carneiro', 2017)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")
Livro.livros = [livro1, livro2, livro3]
resultado = Livro.verificar_disponibilidade(1999)

for livros in resultado:
    print(f"Livros disponiveis: {livros}")

# 4 Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

#     def verificar_disponibilidade(ano):
#         livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
#         return livros_disponiveis


# livro.