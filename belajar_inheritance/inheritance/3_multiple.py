class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print(duck.fly())   # Output: Flying
print(duck.swim())  # Output: Swimming