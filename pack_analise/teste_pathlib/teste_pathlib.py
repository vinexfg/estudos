
class Product:
    def __init__(self, number, name, amount):
        self.number = number
        self.name = name
        self.amount = amount
        self.list = []

    def data(self):
        return(self.name, self.amount)
    
    def Print_data(self):
        print(f'Number: {self.number} / Name: {self.name} /  Amount: {self.amount} Unit ')

    def add_list_products(self):
        self.list.append(self.data())
        return self.list
    
    def Print_list(self):
        for item in self.list:
            return item


Number_product = int(input('Number: '))
Name_product = input('Name: ')
Amount_product = int(input('Amount: '))
print('           ')
print('           ')
print('           ')
print('           ')

Product1 = Product(Number_product, Name_product, Amount_product)

Product1.Print_data()
Product1.add_list_products()
Product1.Print_list()
