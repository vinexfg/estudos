

class Passaword:
    def __init__(self):
        self.caracteres_permitidos = 25
        self.minimo_de_caracteres = 8
        self.caracteres_especias = ['!', '@', '#', '%', '&', '*']

    def check_caracteres(self, passaword):
        if len(passaword) > self.caracteres_permitidos:
            print('Sua senha excedeu a quantidade de caracteres permitidos')
            return False
        elif len(passaword) < self.minimo_de_caracteres:
            print('a senha deve ter no minimo 7 caracteres')
        else:
            return True
        
        
    def check_minimo(self, passaword):
        if not any(char in passaword for char in self.caracteres_especias):
            print('A senha deve conter pelo menos um caractere especial: !, @, #, %, &, *')

