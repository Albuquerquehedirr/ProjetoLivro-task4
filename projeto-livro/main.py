# 8) Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método __str__.
from exercicio1_ao_4 import Livro

livro_main = Livro("O poder do Hábito","Charles Duhigg",2012)
livro_main1 = Livro("Os segredos da mente milionária","T harv Eker ",2006)

print(livro_main)
print(livro_main1)