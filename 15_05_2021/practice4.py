# practice 4


"""
El usuario va a introducir las velocidades de tres disparos, cada disparo
consta de una velocidad en y i x

La computadora coloca aleatoriamente un objetivo en un posición x, y=0- QUe es 
la misma altura del usuario. 


Despues de haber recibido la información la computadora deberá indicar si el usuario
dio en el blanco o no, con una diferencia de hasta 3 unidades a la izquierda o a la derecha. 

  /\
 /  \
/    \

(vy)/g = t

d = vx*2*t

"""
from random import random

def getRandom(a,b):
    return a + (b-a)*random()

def ask(msg):
    print(msg)
    return float(input("-> "))

def getDistance(vx, vy):
    t = vy/9.81
    d = vx*2*t
    return d

def results(tX, dx, idx):
    print( f"D{idx}: {dx}" )
    diff = abs(dx-targetX)
    print(f" Quedaste a {diff} mts")
    
    if( diff < 3):
        print("*********************")
        print("*********************")
        print("******GANASTE********")
        print("*********************")
        print("*********************")
    
s1vx = ask("Velocidad D1 X")
s1vy = ask("Velocidad D1 Y")
s2vx = ask("Velocidad D2 X")
s2vy = ask("Velocidad D2 Y")
s3vx = ask("Velocidad D3 X")
s3vy = ask("Velocidad D3 Y")


targetX = getRandom(10,30)
results(  targetX,   getDistance(s1vx, s1vy) , 1  )
results(  targetX,   getDistance(s2vx, s2vy) , 2  )
results(  targetX,   getDistance(s3vx, s3vy) , 3  )



