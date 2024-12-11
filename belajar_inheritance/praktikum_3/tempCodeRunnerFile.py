class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
# Memanggil metode statis tanpa membuat objek
print(MathOperations.add(5, 3))
print(MathOperations.multiply(4, 2))