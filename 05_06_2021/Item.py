class Item:
    def __init__(self, px, py):
        self.__px = px
        self.__py = py
        self.__taken = False
    def take(self):
        self.__taken = True
    def isTaken(self):
        return self.__taken
    def getPx(self):
        return self.__px
    def getPy(self):
        return self.__py
    def __str__(self):
        return f'x:{self.getPx()},y:{self.getPy()}{type(self)} {self.isTaken()}'
        
class Weapon(Item):
    def __init__(self, px, py):
        super().__init__(px,py)
    
class Amulet(Item):
    def __init__(self, px, py):
        super().__init__(px,py)

class Healer(Item):
    def __init__(self, px, py):
        super().__init__(px,py)
