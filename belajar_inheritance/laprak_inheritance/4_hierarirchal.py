# Superclass
class Vehicle:
    def start(self):
        return "Vehicle started"

# Subclass yang berbeda mewarisi dari Vehicle
class Car(Vehicle):
    def num_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def num_wheels(self):
        return 2

# Pengujian
car = Car()
motorcycle = Motorcycle()
print(car.start())          # Output: Vehicle started
print(car.num_wheels())     # Output: 4
print(motorcycle.start())   # Output: Vehicle started
print(motorcycle.num_wheels())  # Output: 2