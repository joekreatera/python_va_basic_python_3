from Creature import Creature
from random import randint
# Strength[50-140] 

class Troll(Creature):
    MIN_STRENGTH = 100000
    MAX_STRENGTH = 900000
    MIN_MAGIC = 0
    MAX_MAGIC = 0
    MIN_LIFE = 999999
    MAX_LIFE = 999999
    
    def __init__(self,px, py, max_speed = 0):
        super().__init__(px,py,max_speed)
        self.setStrength(randint(Troll.MIN_STRENGTH, Troll.MAX_STRENGTH))
        self.setMagic(randint(Troll.MIN_MAGIC, Troll.MAX_MAGIC))
        self.setMaxLife(randint(Troll.MIN_LIFE, Troll.MAX_LIFE))
        self.setLife(self.getMaxLife())
        self.setSx(0)
        self.setSy(0)    
        self.setStrengthPercentage(1)
        self.setMagicPercentage(0)   
if __name__ == "__main__":
    e = Troll(20,20,10)
    print(e)
    e.move()
    print(e)
    e.move()
    print(e)
    