class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
# Membuat objek
calc = Calculator()
result_add = calc.add(10, 5)
result_subtract = calc.subtract(10, 5)

print(f"Addition: {result_add}")
print(f"subtraction: {result_subtract}")