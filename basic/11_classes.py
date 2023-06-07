### CLASSES ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname


my_person = Person('Mathias', 'Hole')

print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias = "Sin alias") -> None:
        self.full_name = f"{name} {surname} ({alias})"
    
    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person('Mathias', 'Hole')

print(my_person.full_name)

my_person.walk()

my_other_person = Person("Harry", "Tief", "Dev")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Hector Ramon Etor"
print(my_other_person.full_name)