


"""GAME do meu jeito"""


class Person:
    def __init__(self, name =None, age= None, sex= None, skill= None, level= None):
        self.name = name
        self.age = age
        self.sex = sex
        self.skill = skill
        self.level = level

    def __repr__(self):
        return (f'Person: (name={self.name} / age={self.age} / sex={self.sex} / '
                f'skill={self.skill} / level={self.level})')


class DataCollector:

    def __init__(self):
        self.data = []


    def store_data(self, person):
        self.data.append(person)

    def get_data(self):
        questions = [
            'name',
            'age',
            'sex',
            'skill',
            'level'
        ]
        response = {}
        for quest in questions:
            answer = input(f'Please enter your {quest}: ')
            response[quest] = answer

        person = Person(
            name=response['name'],
            age=response['age'],
            sex=response['sex'],
            skill=response['skill'],
            level=response['level']
            )
        self.store_data(person)