# person.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

guido = Person(name="Guido", age=40)