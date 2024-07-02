

class Client:
    def __init__(self, name, surname, age, cpf, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.cpf = cpf
        self.email = email


class Data_storage:
    def __init__(self):
        self.clients = []

    
    def add_client(self, client):
        if isinstance(client, Client):
            self.clients.append(client)
        else:
            raise TypeError('Expected instance of Client')
        
        