# Superclass
class Animal:
    def make_sound(self):
        return "Some sound"

# Subclass yang mewarisi dari Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Pengujian
dog = Dog()
print(dog.make_sound())  # Output: Woof!
