class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old"

person = Person('Qozeem', 30)
print(person)