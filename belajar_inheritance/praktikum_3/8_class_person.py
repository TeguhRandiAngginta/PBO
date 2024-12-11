class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Membuat objek dari kelas person
p1 = Person("Teguh Randi Angginta", 20)
p1.greet()