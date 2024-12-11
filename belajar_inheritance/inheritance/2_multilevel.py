class Animal:
    def sound(self):
        return "Some sound"

class Mammal(Animal):
    def has_hair(self):
        return True

class Dog(Mammal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())   # Output: Bark
print(dog.has_hair()) # Output: True