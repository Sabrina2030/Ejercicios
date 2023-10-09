import random


def simple_list():
    lista = []
    for i in range(10):
        diccionario = {
            'id': i + 1,
            'age': random.randint(1, 100)
        }
        lista.append(diccionario)
    return lista

def sort_list():
    lista = simple_list()
    lista.sort(key=lambda x: x['age'])
    return lista
