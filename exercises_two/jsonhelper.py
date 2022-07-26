# javascript object notation used for lightweight data exchange
import json

person  = {"name":"John", "age": 5, "city": "Eugene"}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('example.json', 'r') as file:
    person_two = json.load(file)
    print(person_two)


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)


