import pygame


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
    

    def store_data(self):
        data = []
        return data

    def get_data(self):
        self.store_data()
        questions = [
            'name',
            'age',
            'sex',
            'skill'
        ]
        for quest in questions:
            response = input(f'Please enter your {quest}: ')
            self.data