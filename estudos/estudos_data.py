# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'nipe'],
#      defaults=['VALOR', 'NAIPE'] )
# as_espadas = Carta('A', 'Espadas')
# print(as_espadas)
# print(as_espadas[0])
# print(as_espadas[1])
# print(as_espadas._asdict())

from typing import NamedTuple

class Carta(NamedTuple):
    valor:str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A')
print(as_espadas._asdict())