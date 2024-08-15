from pathlib import Path



arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

arquivo.touch()
print(arquivo)