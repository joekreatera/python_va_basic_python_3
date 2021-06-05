class Item:
    def __init__(self, px, py):
        self.__px = px
        self.__py = py
    def getPx(self):
        return self.__px
    def getPy(self):
        return self.__py
        
class Weapon(Item):
    def __init__(self, px, py):
        super()__init__(px,py)
    
class Amulet(Item):
    def __init__(self, px, py):
        super()__init__(px,py)

class Healer(Item):
    def __init__(self, px, py):
        super()__init__(px,py)
