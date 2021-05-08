"""
EN un juego, el usuario entrega su magia por vida

Si la magia es menor a 5, la vida es 5
Si la magia esta entre 5 y 20 la vida es igual a 5 + la magia
Si la magia es mayor a 20, la vida seria de 20

"""
# 3
magic = int(input("dame tu magia"))
base_life = min(max(5, magic),20)
over_life = min(magic, 20)

life =max(over_life, base_life)

print(life)