import random

def generate_person():
    """
    Generate a random person with 'id' and 'age' attributes.
    'id' is a unique identifier (integer).
    'age' is a random integer between 1 and 100.
    """
    return {'id': random.randint(1, 1000), 'age': random.randint(1, 100)}

def simple_list():
    """
    Generate a list of 10 random persons using the generate_person function.
    """
    return [generate_person() for _ in range(10)]

def sort_list(persons):
    """
    Sort a list of persons by their 'age' attribute in ascending order.
    """
    return sorted(persons, key=lambda x: x['age'])
