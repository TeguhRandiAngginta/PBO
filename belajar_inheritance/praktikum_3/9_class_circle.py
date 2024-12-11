class circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi

# Membuat objek dari kelas circle
c1 = circle(5)
circle.change_pi(3.14159)
print(circle.pi)