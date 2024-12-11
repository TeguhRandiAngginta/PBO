class Car:
    def move(self):
        return "Car is moving"
    
class Airplane:
    def move(self):
        return "Airplane is flying"
    
def transport(vehicle):
    print(vehicle.move())

car = Car()
airplane = Airplane()

transport(car)
transport(airplane)