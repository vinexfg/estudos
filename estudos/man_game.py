import json
from pprint import pprint # um print mais bonito
from typing import TypedDict #permite criar um class para que use no json
# fica mais facil de achar quando for fazer o print('filme[aqui voce achar as coisas da sua class]
# ')


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float




string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
} '''

filme: Movie = json.loads(string_json) # transformando um dicionario para o json
print(filme)

# # pprint(filme)
# print(json.dumps(filme, ensure_ascii=False, indent=2))
# #deixa mais facil de ler o json


json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)