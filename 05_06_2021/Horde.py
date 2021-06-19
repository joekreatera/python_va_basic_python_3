from Orc import Orc
from helpers import near
"""
Horde class is a container for an unlimited amount of creatures.
Horde will have the type of its very first member
Add Member will not check the type of each member
"""
class Horde:
    NO_TYPE = 0
    ORC_HORDE = 1
    ELF_HORDE = 2
    def __init__(self, creature_list = []):
        if( len(creature_list) > 0 ):
            self.__type = Horde.ORC_HORDE if type(creature_list[0]) is Orc else Horde.ELF_HORDE
        else:
            self.__type = Horde.NO_TYPE
        
        self.__members = creature_list
    
    def getPx(self):
        if( len(self.__members) == 0):
            return 0 
        
        return sum([ c.getPx() for c in self.__members ])/len(self.__members)
        
    def getPy(self):
        if( len(self.__members) == 0):
            return 0 
            
        return sum([ c.getPy() for c in self.__members ])/len(self.__members)
    
    def addMember(self, creature):
        if( len(self.__members) == 0 ):
            self.__type = Horde.ORC_HORDE if type(creature) is Orc else Horde.ELF_HORDE
        self.__members.append(creature)
    
    def getMembers(self):
        return self.__members
    
    def allDead(self):
        for m in self.__members:
            if m.getLife() > 0:
                return False
        return True    
    
    def setAllDead(self):
        for m in self.__members:
            m.receiveHit( m.getLife() )

    def cleanDead(self):
        dead_guys = []
        for m in self.__members:
            if m.getLife() <= 0:
                dead_guys.append(m)
        
        while( len(dead_guys) > 0 ):
            self.__members.remove(dead_guys[0])
            dead_guys.pop(0)
            
    def cleanMembers(self):
        self.__members.clear()
        
    def mergeWithHorde(self, horde):
        other_members = horde.getMembers()
        for m in other_members:
            print(m)
            self.addMember(m)
        
        horde.cleanMembers()
        
    def move(self , world_width, world_height):
        if( len( self.__members) > 0):
            sx_list = [ c.getSx() for c in self.__members ]
            sy_list = [ c.getSy() for c in self.__members ]
    
            sx = sum(sx_list)/len(sx_list)
            sy = sum(sy_list)/len(sy_list)
            
            for c in self.__members:
                c.move(world_width, world_height, overwrite_sx = sx, overwrite_sy = sy)
    
    def joinHorde(self, creature, distance):
        for c in self.__members:
            if near(c, creature) < distance:
                self.addMember(creature)
                return True
        return False
    
    def nearHorde(self, creature, distance):
        for c in self.__members:
            if near(c, creature) < distance:
                return True
        return False
        
    def __str__(self):
        res = f'\t Horde q:{len(self.__members)} x:{ self.getPx() } y:{ self.getPy() }: \n'
        for c in self.__members:
            res += f'\t\t {c}\n'
        return res
        