class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0 # Default age

    def set_age(self, age):
        self.age = age
        print(f"he is {self.age} years old")

    def bark(self):
        print(f"{self.name} is barking!")

# Membuat objek dari kelas Dog
dog1 = Dog("Buddy")
dog1.set_age(3)
dog1.bark()