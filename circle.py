import math

class Circle:
    def __init__(self, radius):
        try:
            self.radius = radius
            self.circunference = math.pi * 2 * radius
            self.field = math.pi * radius * radius
        except:
            print("Invalid data type, Radius must be a number")
        
    def getCircunference(self):
        return(self.circunference)

    def getField(self):
        return(self.field)
