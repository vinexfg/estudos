from contextlib import contextmanager


@contextmanager
def abrir_arquivo(nome):
    arquivo = open(nome, 'r')
    try:
        yield arquivo
    finally:
        arquivo.close()


with abrir_arquivo('teste_abrindo') as f:
    conteudo = f.read()
    print(conteudo)