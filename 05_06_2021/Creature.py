from random import random
from math import pi, sin, cos

class Creature:
    
    MIN_SPEED = 2
    
    def __init__(self, px, py, max_speed = 1):
        self.__px = px
        self.__py = py
        
        max_speed = max(max_speed, Creature.MIN_SPEED)
        random_speed = int(random()*(max_speed-Creature.MIN_SPEED) + Creature.MIN_SPEED)
        random_angle = 2*pi*random()
        
        self.__sx = int(  random_speed*cos(random_angle)  )
        self.__sy =int(  random_speed*sin(random_angle)  )
        self.__strength = 0
        self.__magic = 0
        self.__life = 0
        self.__max_life = 0
        
    def move(self):
        pass