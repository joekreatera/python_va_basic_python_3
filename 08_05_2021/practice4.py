"""

En un juego de plataforma de laberintos, hay que saber si la celda en la que esta 
el player y el enemigo es la misma. Si lo esta, entraran a una batalla. 

Para poder saber si estan cerca, el mundo cuenta con una reticula. Los mov. solo 
opuede ser hacia adelante o atras, arriba o abajo. El programa puede preguntar 
la ubicación en x i y de player y enemeigo, y debera indicar la distancia manhattan 
a la que se encuentran. 

|__|__|__x
|__|__|__|
|__|__|__|
|__|__|__|
y__|__|__|

"""


x1 = int(input('X enemigo:'))
y1 = int(input('Y enemigo:'))

x2 = int(input('X player:'))
y2 = int(input('Y player:'))

d = abs(y2-y1) + abs(x2-x1)

print(f"Distancia enemigo a player {d}")