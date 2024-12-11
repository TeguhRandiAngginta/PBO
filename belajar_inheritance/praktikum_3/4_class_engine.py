class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
class Car:
    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.engine = Engine(horsepower)

    def display_info(self):
        print(f"Car brand: {self.brand}, Model: {self.model}, Horsepower: {self.engine.horsepower}")

# Membuat objek Car dengan objek Engine di dalamnya 
car2 = Car("Honda", "Accord", 200)
car2.display_info()