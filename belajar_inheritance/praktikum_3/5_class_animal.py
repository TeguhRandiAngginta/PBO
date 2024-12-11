class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound!")


class cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")


# Membuat objek cat yang mewarisi sifat dari kelas animal
cat1 = cat("whiskers")
cat1.speak()