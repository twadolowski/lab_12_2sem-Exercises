import math

class EquilateralTriangle:
    def __init__(self, side):
        self.side = side
        self.circunference = side * 3
        try:
            self.field = math.sqrt(3)/4 * side * side
        except ZeroDivisionError:
            print("Cannot divide by zero")
    
    def getCircunference(self):
        return(self.circunference)

    def getField(self):
        return(self.field)
