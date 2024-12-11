# Superclass 1
class Engine:
    def start_engine(self):
        return "Engine started"

# Superclass 2
class Wheels:
    def wheel_count(self):
        return "It has wheels"

# Kelas yang mewarisi dari dua superclass di atas
class Car(Engine, Wheels):
    def num_wheels(self):
        return 4

# Pengujian
car = Car()
print(car.start_engine())  # Output: Engine started
print(car.wheel_count())   # Output: It has wheels
print(car.num_wheels())    # Output: 4