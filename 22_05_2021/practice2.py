"""
g = [1,2,3,4,5,6,7]
print(g)

a = g[0]
print(a)

names = ['Monica','Leo','Fer','Iliana','Marco','Joe']
print(names)

a = names[0]
print(a)

nn = input("Dame el nombre a remover")
#names.append(nn)
names.remove(nn)
names.sort()
print(names)
"""
from random import random
types = ['fuego','agua','aire','tierra']

def getRandom(a,b):
    return a + (b-a)*random()

def getIntRandom(a,b):
    return a + int((b-a)*random())
    
#
# Generar un sistema de inventarios
# El usuario va a meter 3 objetos en su mochila con una cantidad de repeticiones de la misma
# El usuario usara uno de ellos requiriendo al sistema el nombre 
# Si el sistema identifica que existe y que tiene suficientes unidades, le dara una de ellas , restando del total

def add_to_backpack(bp_items, bp_units, total_add, interactive = True, backpack_total = 50):
    item = ''
    units = 0
    
    if(interactive):
        item = input("Usuario que vas a meter en la mochila?:")
        units = int(input(f"Cuantas unidades del item {item} vas a meter en la mochila:"))
        units = min(backpack_total-total_add, units)
    else:
        item = types[ getIntRandom(0,3.99) ]
        units = getIntRandom(0,30)
        units = min(backpack_total-total_add, units)
        
    if item in bp_items:
        idx = bp_items.index(item)
        units = min(units, 20-bp_units[idx] )
        bp_units[idx] = bp_units[idx] +  units 
    else:
        bp_items.append(item)
        bp_units.append(0)
        units = min(units, 20)
        last_value = len(bp_units)-1
        bp_units[last_value] = units
        
    return units
    
def use_from_backpack(bp_items, bp_units , interactive = True, max_units_to_choose = 30):
    item = ''
    units = 0
    
    if( interactive):
        item = input("Usuario que vas a usar de la mochila?:")
        units = int(input(f"Usuario, cuánto vas a usar de {item}?") )
    else:
        item = bp_items[getIntRandom(0,1.99)]
        units = getIntRandom(0,max_units_to_choose)
        
    if item in bp_items:
        print("Obtenido")
        idx = bp_items.index(item)
        units = min(bp_units[idx], units)
        bp_units[idx] = bp_units[idx] - units 
    else:
        print(f"Sin unidaes de {item}!")
        units = 0
    return units, item
    
backpack_items = []
backpack_units = []

enemy_backpack_items = []
enemy_backpack_units = []
#for i in range(0,5):
#    print(i)
#    add_to_backpack(backpack_items, backpack_units)
#    print(backpack_items)
#    print(backpack_units)

do_next = True
i = 0
units_added = 0
while i < 3  and do_next:
    i += 1
    units_added = units_added + add_to_backpack(backpack_items, backpack_units, units_added,  interactive=True, backpack_total = 50)
    print(backpack_items)
    print(backpack_units)
    if( units_added >= 50 ):
        do_next = False
    else:
        r = int(input("Deseas agregar mas cosas? 0) SI 1) NO ::>"))
        if(r == 1):
            do_next = False
            
do_next = True
i = 0
units_added = 0
while i < 2  and do_next:
    i += 1
    units_added = units_added + add_to_backpack(enemy_backpack_items, enemy_backpack_units, units_added, interactive=False, backpack_total = 30)
    print(enemy_backpack_items)
    print(enemy_backpack_units)
    if( units_added >= 30 ):
        do_next = False

print("******************************************************")
print("********************BATTLE****************************")
print("******************************************************")

# se genera el enemigo!

enemy_type = types[ getIntRandom(0,3.9) ]
enemy_life = getIntRandom(10,30)
combinations = ['aireagua','aguaaire','fuegotierra','tierrafuego']

user_type = types[ getIntRandom(0,3.9) ]
user_life  = getIntRandom(10,30)

total_inventory = 0
for i in range(0, len(backpack_units) ):
    total_inventory += backpack_units[i]

do_battle = True
while do_battle:
    print(f'USER LIFE: > {user_life}')
    print(f'ENEMY LIFE: > {enemy_life}')
    print(" USER BACKPACK")
    print(backpack_items)
    print(backpack_units)
    print(" ENEMY BACKPACK")
    print(enemy_backpack_items)
    print(enemy_backpack_units)
    
    units_to_use, type = use_from_backpack(backpack_items, backpack_units, interactive = True, max_units_to_choose = 20)
    enemy_units_to_use, enemy_item_type = use_from_backpack(enemy_backpack_items, enemy_backpack_units, interactive = False, max_units_to_choose = 20)
    
    total_inventory -= units_to_use
    
    if( type == enemy_type):
        enemy_life -= units_to_use
    else:
        crash = type+enemy_type
        if(crash in combinations):
            units_to_use = 0
        else:
            enemy_life -= units_to_use/2
            
    if( enemy_item_type == user_type):
        user_life -= enemy_units_to_use
    else:
        crash = enemy_item_type+user_type
        if(crash in combinations):
            units_to_use = 0
        else:
            user_life -= enemy_units_to_use/2
    
    if( enemy_life <= 0):
        print("Ganaste!!!!!")
        do_battle = False
    elif total_inventory <= 0:
        print("Perdiste")
        do_battle = False
    elif( user_life <= 0):
        print("Perdiste!!!!!")
        do_battle = False
    

# [X] Utilizar objetos mientras el usuario quiera
# [X] Validar que los objetos no se puedan agregar
"""
a-1
a-2
a-3
Mala lista 
[a,a,a]
[1,2,3]
deberia quedar

[a]
[6]
"""
# [X] Hacer una batalla contra un enemigo. El enemigo es de tipo agua, fuego, aire o tierra 
# [X] y cuenta con una vida en cada uno
# [X] el usuario agregar hasta 3 elementos a su mochila
# [X]cada uso, va a decidir cuanto usar de cada cosa, si su inventario se acaba antes de quitarle toda la vida
# [X] al enemigo, entonces, pierde. 
# [X] EN caso contrario gana. El enemigo cuenta con una vida aleatoria entre 10 y 30, el usuario 
# [X] puede meter máximo 20 de cada elemento en su mochila, pero con un máximo de 50. 
# Ver sig tabla:
"""


    A F W E 
A   T M 0 M
F   M T M 0 
W   0 M T M
E   M 0 M T
0 -> sin daño
T -> Daño total de la cantidad de unidades
M -> Daño a la mitad de la cantidad de unidades

"""

# MISION
#
# Agregar vida a usuario
# Agregar elemento al usuario
# Agregar contraataque de enemigo eligiendo un poder entre 2 elementos 
# Colocar una mochila para el enemigo con maximo 2 elementos y con un maximo de 30 unidades
# Aplican las mismas tablas
#