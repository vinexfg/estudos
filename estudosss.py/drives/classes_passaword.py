class Password:
    def __init__(self):
        self.caracteres_permitidos = 25
        self.minimo_caracteres = 6
        self.caracteres_necessarios = ['!', '@', '#', '%', '&', '*']
        ''
        
    def checker(self, Passaword):
        if len(Passaword) > self.caracteres_permitidos:
            print('Maximo de caracteres atingido')
        elif len(Passaword) < self.minimo_caracteres:
            print('a senha deve ter no minimo 7 carcteres')
        else:
            return True
        
    def checker_especial(self, passaword):
        if not any(char in passaword for char in self.caracteres_necessarios):
            print('A senha deve conter pelo menos um caractere especial: !, @, #, %, &, *')
            return False
        return True