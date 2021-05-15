# el juego s trata de desarmar bombas
# si la bomba es de tipo AB101 entonces los cables que hay que cortar son el rojo y el azul
# si la bomba es de tipo IU12 el cable rojo se debe cortar y el azul se debe mantener
# si la bomba es de tipo MAA089 el verde se debe conectar a la terminal negra y el cable rojo a la amarilla
# si la bomba es de tipo T78 solo hay que quitar la bateria
# KABOOM-> perder , UFFF -> ganar
import random
from os import system
from time import sleep
system("cls")

NORMAL = 0
CUT = 1
TO_BLACK = 2
TO_YELLOW = 3


def getBomb():
    if( random.random() > 0.5):
        return "AB101"
    elif random.random() > 0.5:
        return "IU12"
    elif random.random() > 0.5:
        return "MAA089"
    else:
        return "T78"

b = getBomb()
print(f"Se te ha presentado la bomba {b}")


def ask(msg):
    print(msg)
    print("presiona:")
    pr = int(input("Selección:"))
    return pr

red = ask("Que deseas hacer con el cable rojo (0) Dejarlo (1) Cortarlo (2) Llevar a negra (3) Llevar a amarilla")
blue = ask("Que deseas hacer con el cable azul (0) Dejarlo (1) Cortarlo (2) Llevar a negra (3) Llevar a amarilla")
green = ask("Que deseas hacer con el cable verde (0) Dejarlo (1) Cortarlo (2) Llevar a negra (3) Llevar a amarilla")
battery = ask("Que deseas hacer con la bateria (0) Dejarla (1) Desconectar")


success = False
# si la bomba es de tipo AB101 entonces los cables que hay que cortar son el rojo y el azul
if b == "AB101" and red == CUT and blue == CUT and green == NORMAL and battery == NORMAL:
    success = True

# si la bomba es de tipo IU12 el cable rojo se debe cortar y el azul se debe mantener
if b == "IU12" and red == CUT and blue == NORMAL and green == NORMAL and battery == NORMAL:
    success = True
    
# si la bomba es de tipo MAA089 el verde se debe conectar a la terminal negra y el cable rojo a la amarilla
if b == "MAA089" and red == TO_YELLOW and blue == NORMAL and green == TO_BLACK and battery == NORMAL:
    success = True
    
# si la bomba es de tipo T78 solo hay que quitar la bateria
if b == "T78" and red == NORMAL and blue == NORMAL and green == NORMAL and battery == CUT:
    success = True

i = 100
while(i >= 0):
    i -= 1
    sleep(0.01)
    system("cls")
    s = "-"*i + "*"
    print(s)

system("cls")
if success : 
    print("UFFF")
else:
    print("K - A - B - O - O - M")