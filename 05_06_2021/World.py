# world
from Orc import Orc
from Elf import Elf
from Troll import Troll
from Item import Weapon, Healer, Amulet
from random import randint as getRandomBetween

class World:
    
    def __init__(self):
        self.__width = 100
        self.__height = 100
        self.__max_speed = 10
        self.orcs = []
        self.elves = []
        self.items = []
        self.trolls = []
        
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
    def day():
        pass
        
w = World()
print(w)
            