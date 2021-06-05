from random import random
from math import pi, sin, cos

class Creature:
    MIN_SPEED = 2
    def __init__(self, px, py, max_speed = 1):
        self.__px = px
        self.__py = py
        self.__strength = 0
        self.__magic = 0
        self.__life = 0
        self.__max_life = 0
        self.changeDirection(max_speed)
    def move(self):
        pass
    def getPx(self):
        return self.__px
    def getPy(self):
        return self.__py
    def getSx(self):
        return self.__sx
    def getSy(self):
        return self.__sy
    def getLife(self):
        return self.__life
    def getMaxLife(self):
        return self.__max_life
    def getStrength(self):
        return self.__strength
    def getMagic(self):
        return self.__magic
    def changeDirection(self, max_speed):
        max_speed = max(max_speed, Creature.MIN_SPEED)
        random_speed = int(random()*(max_speed-Creature.MIN_SPEED) + Creature.MIN_SPEED)
        random_angle = 2*pi*random()
        self.__sx = int(  random_speed*cos(random_angle)  )
        self.__sy =int(  random_speed*sin(random_angle)  )
    def __str__(self):
        return f'{self.getPx()} {self.getPy()} {self.getSx()} {self.getSy()} \
        {self.getStrength()} {self.getMagic()} {self.getLife()} {self.getMaxLife()}'
if __name__ == "__main__":
    c = Creature(10,10,10)
    print(c)