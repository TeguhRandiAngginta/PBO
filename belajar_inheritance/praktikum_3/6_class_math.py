class Math:
    @staticmethod
    def multiply(a, b):
        return a * b
    
# Memanggil metode static tanpa membuat objek
result = Math.multiply(5, 6)
print(f"Multiplication: {result}")