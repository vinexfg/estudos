class Mylist:
    def __init__(self) -> None:
        self._data= {}

    def append(self, value):
        self._data[0] = value

if __name__=='__main__':
    lista = Mylist()
    lista.append('maria')
    print(lista)
