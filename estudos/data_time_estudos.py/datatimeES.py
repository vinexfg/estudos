import os
import shutil


os.system('cls')
caminho = os.path.join('C:\\Users\\vinys\\OneDrive\\Tarefas\\estudos')
# print(caminho)


for item in os.listdir(caminho):
    # print(item)
    pass

diretorio_atual = 'C:\\Users\\vinys\\OneDrive\\Tarefas\\estudos'


descobrir_diretorio = os.getcwd()


HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
nova_pasta = os.path.join(DESKTOP, 'nova_pasta')
# print(nova_pasta)


os.makedirs('nova_pasta')
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for file in files:
        print(file)

