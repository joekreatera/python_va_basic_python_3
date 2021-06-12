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
    
    def addMember(self, creature):
        if( len(self.__members) == 0 ):
            self.__type = Horde.ORC_HORDE if type(creature]) is Orc else Horde.ELF_HORDE
        self.__members.append(creature)
    
    
        