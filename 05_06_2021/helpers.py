# helpers
from math import sqrt
    
def near(objA, objB):
    dx = objA.getPx() - objB.getPx()
    dy = objA.getPy() - objB.getPy()
    distance = sqrt(dx**2 + dy**2)
    return distance
    