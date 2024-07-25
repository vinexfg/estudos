


class Time:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
    
class Planeta:
    def __init__(self, name):
        self.name = name

brasil = Time('Brasil')
portugal = Time('Portugal')



        