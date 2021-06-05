from Creature import Creature
from random import randint
# Strength[50-140] 

class Elf(Creature):
    MIN_STRENGTH = 20
    MAX_STRENGTH = 50
    MIN_MAGIC = 60
    MAX_MAGIC = 120
    MIN_LIFE = 1500
    MAX_LIFE = 2000
    
    def __init__(self,px, py, max_speed = 1):
        super().__init__(px,py,max_speed)
        self.setStrength(randint(Elf.MIN_STRENGTH, Elf.MAX_STRENGTH))
        self.setMagic(randint(Elf.MIN_MAGIC, Elf.MAX_MAGIC))
        self.setMaxLife(randint(Elf.MIN_LIFE, Elf.MAX_LIFE))
        self.setLife(self.getMaxLife())
        
if __name__ == "__main__":
    e = Elf(20,20,10)
    print(e)
    e.move()
    print(e)
    e.move()
    print(e)
    