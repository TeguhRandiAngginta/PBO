# Level 1 Superclass
class Animal:
    def make_sound(self):
        return "Some generic sound"

# Level 2 Subclass
class Mammal(Animal):
    def has_hair(self):
        return True

# Level 3 Subclass yang mewarisi dari Mammal
class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

# Pengujian
dog = Dog()
print(dog.make_sound())   # Output: Woof!
print(dog.has_hair())     # Output: True