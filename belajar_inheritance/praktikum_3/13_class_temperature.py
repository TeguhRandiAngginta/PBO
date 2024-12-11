class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return (celcius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celcius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
# Mengonversi suhu tanpa membuat instance
temp_c = 100
temp_f = TemperatureConverter.celcius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")