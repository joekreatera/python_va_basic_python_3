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

#
# Generar un sistema de inventarios
# El usuario va a meter 3 objetos en su mochila con una cantidad de repeticiones de la misma
# El usuario usara uno de ellos requiriendo al sistema el nombre 
# Si el sistema identifica que existe y que tiene suficientes unidades, le dara una de ellas , restando del total

def add_to_backpack(bp_items, bp_units):
    item = input("Usuario que vas a meter en la mochila?:")
    bp_items.append(item)
    bp_units.append(0)
    units = int(input(f"Cuantas unidades del item {item} vas a meter en la mochila:"))
    last_value = len(bp_units)-1
    bp_units[last_value] = units
    
def use_from_backpack(bp_items, bp_units):
    item = input("Usuario que vas a usar de la mochila?:")
    units = int(input(f"Usuario, cuánto vas a usar de {item}?") )
    
    if item in bp_items:
        print("Obtenido")
        idx = bp_items.index(item)
        units = min(bp_units[idx], units)
        bp_units[idx] = bp_units[idx] - units 
    else:
        print(f"Sin unidaes de {item}!")
        units = 0
    return units
    
backpack_items = []
backpack_units = []

#for i in range(0,5):
#    print(i)
#    add_to_backpack(backpack_items, backpack_units)
#    print(backpack_items)
#    print(backpack_units)

do_next = True
i = 0
while i < 5  and do_next:
    i += 1
    add_to_backpack(backpack_items, backpack_units)
    print(backpack_items)
    print(backpack_units)
    r = int(input("Deseas agregar mas cosas? 0) SI 1) NO ::>"))
    if(r == 1):
        do_next = False

units_to_use = use_from_backpack(backpack_items, backpack_units)
print(backpack_items)
print(backpack_units)
print(f'Used {units_to_use}')

# Utilizar objetos mientras el usuario quiera
# Validar que los objetos no se puedan agregar
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
# Hacer una batalla contra un enemigo. El enemigo es de tipo agua, fuego, aire o tierra 
# y cuenta con una vida en cada uno
# el usuario agregar hasta 3 elementos a su mochila
# cada uso, va a decidir cuanto usar de cada cosa, si su inventario se acaba antes de quitarle toda la vida
# al enemigo, entonces, pierde. 
# EN caso contrario gana. El enemigo cuenta con una vida aleatoria entre 10 y 30, el usuario 
# puede meter máximo 20 de cada elemento en su mochila, pero con un máximo de 50. 
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