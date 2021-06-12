# world
from Orc import Orc
from Elf import Elf
from Troll import Troll
from Item import Weapon, Healer, Amulet
from random import randint as getRandomBetween
from time import sleep
from os import system
from math import sqrt
from Horde import Horde
import Constants as GB

# system("cls") windows
# system('clear') mac
class World:
    
    def __init__(self):
        self.__width = 100
        self.__height = 100
        self.__max_speed = 10
        self.orcs = []
        self.elves = []
        self.items = []
        self.trolls = []
        self.elf_hordes  = []
        self.orc_hordes = []
        
        for i in range(0,5):
            self.orcs.append(
                Orc( getRandomBetween(0,self.__width) ,
                    getRandomBetween(0,self.__height) ,
                    getRandomBetween( 3 ,self.__max_speed) , 
                )
            )
    
        for i in range(0,5):
            self.elves.append(
                Elf( getRandomBetween(0,self.__width) ,
                    getRandomBetween(0,self.__height) ,
                    getRandomBetween( 3 ,self.__max_speed) , 
                )
            )
        
        for i in range(0,3):
            self.trolls.append(
                Troll( getRandomBetween(0,self.__width) ,
                    getRandomBetween(0,self.__height) 
                )
            )
            
        for i in range(0,12):
            if( i < 4):
                self.items.append(
                    Weapon( getRandomBetween(0,self.__width) ,
                        getRandomBetween(0,self.__height) 
                    )
                )
            elif( i < 8):
                self.items.append(
                    Amulet( getRandomBetween(0,self.__width) ,
                        getRandomBetween(0,self.__height) 
                    )
                )
            else:
                self.items.append(
                    Healer( getRandomBetween(0,self.__width) ,
                        getRandomBetween(0,self.__height) 
                    )
                )
    
    def __str__(self):
        orcs_str = "Orcs:\n"
        elves_str = "Elves:\n"
        items_str = "Items:\n"
        trolls_str = "Trolls:\n"
        for i in self.orcs:
            orcs_str += '\t' + str(i) + '\n'
        
        for i in self.elves:
            elves_str+= '\t' + str(i) + '\n'
            
        for i in self.items:
            items_str+= '\t' + str(i) + '\n'
            
        for i in self.trolls:
            trolls_str += '\t' + str(i) + '\n'
    
        return f'o:{orcs_str}\ne:{elves_str}\nt:{trolls_str}\ni:{items_str}'
    
    def cleanse_list(self, from_list, original_list):
        while len(from_list) > 0 :
            original_list.remove(from_list[0])
            from_list.pop(0)
    
    def getIsItemTaken(self,i):
        return i.isTaken()
    
    def getIsICreatureDead(self, c):
        return c.getLife() <= 0
    
    def getTakenItems(self, items_list):
        return filter( self.getIsItemTaken  , items_list)
    
    def getDeadCreatures(self, creatures_list):
        return filter( self.getIsICreatureDead  , creatures_list)
        
    def near(self, objA, objB):
        dx = objA.getPx() - objB.getPx()
        dy = objA.getPy() - objB.getPy()
        distance = sqrt(dx**2 + dy**2)
        return distance
        
    def fight(self,creatureA, creatureB):
        if self.near(creatureA, creatureB) < GB.APPROACH_DISTANCE:
            while( creatureA.getLife() > 0 and creatureB.getLife()  > 0):
    
                cAh = creatureA.getHitForce()
                cBh = creatureB.getHitForce()
                creatureA.receiveHit(cBh)
                creatureB.receiveHit(cAh)
                
    def doHorde(self,creatureA, creatureB , horde_list):
        if self.near(creatureA, creatureB) < GB.APPROACH_DISTANCE:
            horde_list.append( Horde([creatureA, creatureB]) )
                
    def canTakeItem(self,creature, item):
        
        if( not item.isTaken() ):
            distance = self.near(creature, item)
            if distance < GB.APPROACH_DISTANCE:
                item.take()
                if type(item) is Weapon:
                    if type(creature) is Orc:
                        creature.setStrength( creature.getStrength() + GB.WEAPON_EXTRA_STRENGTH_ORCS ) 
                    if type(creature) is Elf:
                        creature.setStrength( creature.getStrength() + GB.WEAPON_EXTRA_STRENGTH_ELVES  )
                if type(item) is Amulet:
                    if type(creature) is Elf:
                        creature.setMagic( creature.getMagic() + GB.AMULET_EXTRA_MAGIC_ELVES  )
                    if type(creature) is Orc:
                        creature.setMagic( creature.getMagic() + GB.AMULET_EXTRA_MAGIC_ORCS  )
                if type(item) is Healer:
                    creature.heal()
    
    def day(self):
        """
        for i in self.orcs: # 5
            i.move(self.__width, self.__height)
            for item in self.items: # 5
                self.canTakeItem(i, item)
            for j in self.elves:
                self.fight(i,j)
            for j in self.trolls:
                self.fight(i,j)
        """        
        for i in self.elves:
            i.move(self.__width, self.__height)
            for item in self.items: # 5
                self.canTakeItem(i, item)
            for j in self.elves:
                self.doHorde(i,j, self.elf_hordes)
            #for j in self.orcs:
            #    self.fight(i,j)
            #for j in self.trolls:
            #    self.fight(i,j)
                
        self.cleanse_list(   list(self.getTakenItems(self.items))   , self.items)
        self.cleanse_list(   list(self.getDeadCreatures(self.orcs))   , self.orcs)
        self.cleanse_list(   list(self.getDeadCreatures(self.elves))   , self.elves)
        
        
        
        
w = World()

            
for i in range(0,100):
    system("cls")
    w.day()
    print(w)
    sleep(.1)