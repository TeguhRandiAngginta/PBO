# Superclass 1
class Flyable:
    def fly(self):
        return "I can fly!"

# Superclass 2
class Swimmable:
    def swim(self):
        return "I can swim!"

# Subclass yang mewarisi dari Flyable dan Swimmable
class Duck(Flyable, Swimmable):
    def make_sound(self):
        return "Quack!"

# Pengujian
duck = Duck()
print(duck.fly())         # Output: I can fly!
print(duck.swim())        # Output: I can swim!
print(duck.make_sound())  # Output: Quack!
