import os
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
# print(caminho)


# diretorio, arquivo = os.path.split(caminho)
# caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(caminho_arquivo, extensao_arquivo)



print(os.path.abspath('.'))
print(os.path.basename(caminho))