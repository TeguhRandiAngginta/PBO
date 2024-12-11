# Level 1 Superclass
class Device:
    def power_on(self):
        return "Device is powering on."

# Level 2 Subclass
class Computer(Device):
    def operate(self):
        return "Computer is operating."

# Level 3 Subclass yang mewarisi dari Computer
class Laptop(Computer):
    def portability(self):
        return "Laptop is portable."

# Pengujian
laptop = Laptop()
print(laptop.power_on())      # Output: Device is powering on.
print(laptop.operate())       # Output: Computer is operating.
print(laptop.portability())   # Output: Laptop is portable.