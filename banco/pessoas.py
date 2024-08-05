class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

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
    def idade(self):
        return self._idade
    