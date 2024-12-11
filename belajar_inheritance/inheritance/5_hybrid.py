class Animal:
    def sound(self):
        return "Some sound"

class Mammal(Animal):
    def has_hair(self):
        return True

class Bird(Animal):
    def lay_eggs(self):
        return True

class Bat(Mammal):
    def fly(self):
        return "Flying"

bat = Bat()
print(bat.sound())    # Output: Some sound
print(bat.has_hair()) # Output: True
print(bat.fly())      # Output: Flying