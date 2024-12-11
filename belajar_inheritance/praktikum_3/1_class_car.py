class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"car brand: {self.brand}, model: {self.model}")


# Membuat objek dari kelas car
car1 = car("toyota", "camry")
car1.display_info()