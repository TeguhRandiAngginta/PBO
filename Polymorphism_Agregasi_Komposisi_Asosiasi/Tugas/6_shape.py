class Shape:
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        return "Drawing a square"
    
class Triangle(Shape):
    def draw(self):
        return "Drawing a triangle"
    
def draw_shape(shape):
    print(shape.draw())

shapes = [Square(), Triangle()]

for shape in shapes:
    draw_shape(shape)