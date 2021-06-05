from Creature import Creature
from random import randint
# Strength[50-140] 

class Orc(Creature):
    MIN_STRENGTH = 50
    MAX_STRENGTH = 140
    MIN_MAGIC = 1
    MAX_MAGIC = 10
    MIN_LIFE = 1000
    MAX_LIFE = 2500
    
    def __init__(self,px, py, max_speed = 1):
        super().__init__(px,py,max_speed)
        self.setStrength(randint(Orc.MIN_STRENGTH, Orc.MAX_STRENGTH))
        self.setMagic(randint(Orc.MIN_MAGIC, Orc.MAX_MAGIC))
        self.setMaxLife(randint(Orc.MIN_LIFE, Orc.MAX_LIFE))
        self.setLife(self.getMaxLife())
        
if __name__ == "__main__":
    o = Orc(20,20,10)
    print(o)
    o.move()
    print(o)
    o.move()
    print(o)
    