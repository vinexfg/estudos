class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        pass

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta = None

if __name__ == '__name__':
    c1 = Cliente('vinicius', 30 )
    print(c1)
    print(c1.conta)