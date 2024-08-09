class Mylist:
    def __init__(self) -> None:
        self._data= {}
        self.index = 0

    def append(self, value):
        self._data[self.index] = value
        self.index+= 1

if __name__=='__main__':
    lista = Mylist()
    lista.append('maria')
    print(lista._data)
    lista.append('vinicius')
    print(lista._data)
