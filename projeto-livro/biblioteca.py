from exercicio1_ao_4 import Livro

# 5 Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
# from exercicio1_ao_4 import Livro

 # 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro_biblioteca = Livro('O homem mais rico da babilônia', 'George Samuel Clason', 1926)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

# 7) No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

ano_escolhido = 2024
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_escolhido)
print(f"Livros disponíveis em {ano_escolhido}: {livros_disponiveis_ano}")

# verificar o retorno do objeto e não o valor

