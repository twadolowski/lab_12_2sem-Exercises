class Square:
    def __init__(self, side):
        self.side = side
        self.circunference = side * 4
        self.field = side * side
    
    def getCircunference(self):
        return(self.circunference)

    def getField(self):
        return(self.field)
