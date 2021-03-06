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
from helpers import near

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
        e_horde_str = "\tElf Hordes:\n"
        o_horde_str = "\tOrc Hordes:\n"
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
            
        for i in self.elf_hordes:
            e_horde_str += '\t' + str(i) + '\n'
            
        for i in self.orc_hordes:
            o_horde_str += '\t' + str(i) + '\n'
    
        return f'o:{orcs_str}\no:{o_horde_str}\ne:{elves_str}\ne:{e_horde_str}\nt:{trolls_str}\ni:{items_str}'
    
    def cleanse_list(self, from_list, original_list):
        while len(from_list) > 0 :
            original_list.remove(from_list[0])
            from_list.pop(0)
    
    def getIsHordeUseless(self,i):
        return i.allDead()
        
    def getIsItemTaken(self,i):
        return i.isTaken()
    
    def getIsICreatureDead(self, c):
        return c.getLife() <= 0
    
    def getTakenItems(self, items_list):
        return filter( self.getIsItemTaken  , items_list)
    
    def getDeadCreatures(self, creatures_list):
        return filter( self.getIsICreatureDead  , creatures_list)
    
    def getUselessHordes(self, hordes_list):
        return filter( self.getIsHordeUseless  , hordes_list)

    def fight(self,creatureA, creatureB, forceFight=False):
        if near(creatureA, creatureB) < GB.APPROACH_DISTANCE or forceFight:
            while( creatureA.getLife() > 0 and creatureB.getLife()  > 0):
    
                cAh = creatureA.getHitForce()
                cBh = creatureB.getHitForce()
                creatureA.receiveHit(cBh)
                creatureB.receiveHit(cAh)
                
    def doHorde(self,creatureA, creatureB , horde_list , this_day_horde_list ):
        if near(creatureA, creatureB) < 2*GB.APPROACH_DISTANCE \
            and  \
            not creatureA in this_day_horde_list \
            and \
            not creatureB in this_day_horde_list \
            and not creatureA is creatureB :
            horde_list.append( Horde([creatureA, creatureB]) )
            this_day_horde_list.append(creatureA)
            this_day_horde_list.append(creatureB)
    
    def joinHorde(self, horde, creature, creatures_in_hordes ):
        if( not creature in creatures_in_hordes ):
            if  ( horde.joinHorde(creature ,  GB.APPROACH_DISTANCE) ):
                creatures_in_hordes.append(creature)
    
    def mergeHordes(self, hordeA, hordeB):
        if  near(hordeA, hordeB) < 2*GB.APPROACH_DISTANCE and not hordeA is hordeB:
            hordeA.mergeWithHorde(hordeB)
    
    def fightTroll(self, horde, troll):
        if  near(horde, troll) < 2*GB.APPROACH_DISTANCE:
            horde.setAllDead()
    
        
    
    def fightHordes(self, hordeA, hordeB):
        if  near(hordeA, hordeB) < 2*GB.APPROACH_DISTANCE and not hordeA is hordeB:
            print(hordeA)
            print(hordeB)
            while( not hordeA.allDead() and not hordeB.allDead() ):
                hA_members = hordeA.getMembers()
                hB_members = hordeB.getMembers()
                fights_list = []
                longer = hA_members if len(hB_members) < len(hA_members) else hB_members
                smaller = hB_members if len(hB_members) < len(hA_members) else hA_members
                i = 0
                for i in range(0, len(longer) ):
                    fight = [ [smaller[i%len(smaller)]] , [longer[i]] ]
                    if len(fights_list) < len(smaller):
                        fights_list.append( fight )
                    else:
                        fights_list[i%len(smaller)][1].append(longer[i])
                
                for f in fights_list:
                    oppA = f[0]
                    oppB = f[1]
                    if len(oppA) < len(oppB):
                        oppA[0].receiveHit( oppA[0].getLife() )
                    else:
                        self.fight(oppA[0], oppB[0], forceFight = True)
                
                hordeA.cleanDead()
                hordeB.cleanDead()
    
    def killCreature(self, horde, creature):
        if( horde.nearHorde(creature , GB.APPROACH_DISTANCE) ):
            creature.setLife(0)        
    
    def canTakeItem(self,creature, item):
        
        if( not item.isTaken() ):
            distance = near(creature, item)
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
        elves_in_hordes = [] 
        orcs_in_hordes = [] 
        
        for i in self.orcs: # 5
            if i in orcs_in_hordes:
                continue
            i.move(self.__width, self.__height)
            for item in self.items: # 5
                self.canTakeItem(i, item)
            for j in self.orcs:
                self.doHorde(i,j, self.orc_hordes, orcs_in_hordes)
            for j in self.elves:
                self.fight(i,j)
            for j in self.trolls:
                self.fight(i,j)
         
        self.cleanse_list(   list(self.getDeadCreatures(self.orcs))   , self.orcs)
        self.cleanse_list(   list(self.getDeadCreatures(self.elves))   , self.elves)
        
        for i in self.elves:
            if i in elves_in_hordes:
                continue
            i.move(self.__width, self.__height)
            for item in self.items: # 5
                self.canTakeItem(i, item)
            for j in self.elves:
                self.doHorde(i,j, self.elf_hordes, elves_in_hordes)
            for j in self.orcs:
                self.fight(i,j)
            for j in self.trolls:
                self.fight(i,j)
        
        self.cleanse_list(   list(self.getDeadCreatures(self.orcs))   , self.orcs)
        self.cleanse_list(   list(self.getDeadCreatures(self.elves))   , self.elves)
        
                
        self.cleanse_list(   list(self.getTakenItems(self.items))   , self.items)
        self.cleanse_list(   elves_in_hordes   , self.elves)
        self.cleanse_list(   orcs_in_hordes   , self.orcs)
        
        elves_in_hordes = [] 
        orcs_in_hordes = [] 
                
        for horde in self.orc_hordes:
            horde.move(self.__width, self.__height)
            for orc in self.orcs:
                self.joinHorde(horde, orc, orcs_in_hordes )
            for elf in self.elves:
                self.killCreature(horde, elf)
            for friends in self.orc_hordes:
                self.mergeHordes(horde, friends )
            for orc in horde.getMembers():
                for item in self.items:
                    self.canTakeItem(orc, item)
            for j in self.trolls:
                self.fightTroll(horde, j)
        
        self.cleanse_list(   orcs_in_hordes   , self.orcs)
        self.cleanse_list(   list(self.getDeadCreatures(self.elves))   , self.elves)
        self.cleanse_list(   list(self.getTakenItems(self.items))   , self.items)

        for horde in self.elf_hordes:
            horde.move(self.__width, self.__height)
            for elf in self.elves:
                self.joinHorde(horde, elf, elves_in_hordes )
            for orc in self.orcs:
                self.killCreature(horde, orc)
            for friends in self.elf_hordes:
                self.mergeHordes(horde, friends )
            for elf in horde.getMembers():
                for item in self.items:
                    self.canTakeItem(elf, item)
            for j in self.trolls:
                self.fightTroll(horde, j)
    
        self.cleanse_list(   elves_in_hordes   , self.elves)
        self.cleanse_list(   list(self.getDeadCreatures(self.orcs))   , self.orcs)
        self.cleanse_list(   list(self.getTakenItems(self.items))   , self.items)
    
        for elfs in self.elf_hordes:
            for orcs in self.orc_hordes:
                self.fightHordes(elfs, orcs)


        self.cleanse_list(   list(self.getUselessHordes(self.elf_hordes))   , self.elf_hordes)
        self.cleanse_list(   list(self.getUselessHordes(self.orc_hordes))   , self.orc_hordes)
        
w = World()

            
for i in range(0,100):
    system("cls")
    w.day()
    print(w)
    sleep(.1)