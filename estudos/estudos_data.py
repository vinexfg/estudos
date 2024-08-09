from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int


p1 = Pessoa('vinicius', 21 )

if __name__== '__main__':
    print(p1)