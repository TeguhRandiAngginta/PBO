class Bird:
    def fly(self):
        return "Bird is flying"
    
class Airplane:
    def fly(self):
        return "Airplane is flying"
    
object = [Bird(), Airplane()]

for obj in object:
    print(obj.fly())