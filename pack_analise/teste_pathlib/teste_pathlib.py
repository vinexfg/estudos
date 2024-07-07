

class Produt:
    def __init__(self, number, name,amount):
        self.number = number
        self.name = name
        self.list = []
        self.amount = amount

    def data(self):
        self.list.append(self.name , self.amount)
        return self.list
    
    def Print(self):
        print(self.list)

    

product1 = Produt(12, 'biscoito', 23)

product1.Print()

