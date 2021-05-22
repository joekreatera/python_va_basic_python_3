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
    units = input(f"Cuantas unidades del item {item} vas a meter en la mochila")
    last_value = len(bp_units)-1
    bp_units[last_value] = units
    
backpack_items = []
backpack_units = []

add_to_backpack(backpack_items, backpack_units)

print(backpack_items)
print(backpack_units)