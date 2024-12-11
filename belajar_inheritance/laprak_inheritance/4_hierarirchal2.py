# Superclass
class Vehicle:
    def start(self):
        return "Vehicle is starting."

# Subclass pertama yang mewarisi dari Vehicle
class Bicycle(Vehicle):
    def pedal(self):
        return "Pedaling the bicycle."

# Subclass kedua yang mewarisi dari Vehicle
class Scooter(Vehicle):
    def kick_start(self):
        return "Kick-starting the scooter."

# Pengujian
bicycle = Bicycle()
scooter = Scooter()
print(bicycle.start())        # Output: Vehicle is starting.
print(bicycle.pedal())        # Output: Pedaling the bicycle.
print(scooter.start())        # Output: Vehicle is starting.
print(scooter.kick_start())   # Output: Kick-starting the scooter.