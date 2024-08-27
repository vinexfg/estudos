from threading import Thread
from threading import Lock


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return
        self.estoque -= quantidade

        print(f'Você comprou {quantidade} ingressos.'
               f'Ainda temos {self.estoque} e, estoque')
        self.lock.release()

if __name__== '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 10):
        t= Thread(target= ingressos.comprar, args=(i,))
        ingressos.comprar(i)
