from Orc import Orc

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
            
        return sum([ c.getPx() for c in self.__members ])/len(self.__members)
    
    def addMember(self, creature):
        if( len(self.__members) == 0 ):
            self.__type = Horde.ORC_HORDE if type(creature) is Orc else Horde.ELF_HORDE
        self.__members.append(creature)
    
    def move(self , world_width, world_height):
        if( len( self.__members) > 0):
            sx_list = [ c.getSx() for c in self.__members ]
            sy_list = [ c.getSy() for c in self.__members ]
    
            sx = sum(sx_list)/len(sx_list)
            sy = sum(sy_list)/len(sy_list)
            
            for c in self.__members:
                c.move(world_width, world_height, overwrite_sx = sx, overwrite_sy = sy)
    
    def __str__(self):
        res = f'\t Horde {len(self.__members)} x:{ self.getPx() } y:{ self.getPy() }:'
        for c in self.__members:
            res += f'\t\t {c}\n'
        return res
        