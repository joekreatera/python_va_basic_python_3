"""

Muestra la distancia a la que dos objetos circulares (bala y enemigo)
deberian de estar para NO chocar y la distancia a la que realmente están. 

Puedes pedir las siguientes entradas:
x,y de bala y enemigo
radio de bala y enemigo

"""
from math import sqrt

x1 = int(input('X enemigo:'))
y1 = int(input('Y enemigo:'))
r1 = int(input('Radio enemigo:'))

x2 = int(input('X bala:'))
y2 = int(input('Y bala:'))
r2 = int(input('Radio bala:'))

a = (x2-x1)**2
b = (y2-y1)**2
d = sqrt( a + b) 
r = r1 + r2
print(f"Distancia real: {d} Distance critica: {r} ")