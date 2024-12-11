class Rectangle:
    def area(self, width, height):
        return width * height
    
class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2
    
def calculate_area(shape, *args):
    print("Area:", shape.area(*args))

rect = Rectangle()
circle = Circle()

calculate_area(rect, 5, 10)
calculate_area(circle, 7)