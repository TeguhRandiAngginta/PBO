class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = self.salary * Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Mengubah nilai raise_amount melalui metode kelas
Employee.set_raise_amount(1.1)

# Membuat objek Employee
e1 = Employee("John", 5000)
e1.apply_raise()
print(f"New Salary: {e1.salary}")