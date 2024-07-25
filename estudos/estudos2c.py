from estudos1 import MyOpen
from contextlib import contextmanager




@contextmanager
def my_open(caminho_arquivo, modo):
    arquivo = open(caminho_arquivo, modo, encoding= 'utf8')
    yield arquivo
    print('Fechando arquivo')
    arquivo.close()
    

with my_open('aula689.txt', 'w') as arquivo:
    arquivo.write('teste1/n')s