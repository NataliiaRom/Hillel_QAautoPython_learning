class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name = {self.name}, age = {self.age}"

name = input("Your Name: ")
age = input("Your age: ")
person = Person(name, age )
print(person)