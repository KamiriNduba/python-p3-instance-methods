# dog.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

fido = Dog(name="Fido", age=3)