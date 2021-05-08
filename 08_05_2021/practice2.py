"""
Hay un hechicero que tiene un caldero. El caldero se llama RGB,
El usuario debe indicar al hechicero la cantidad de cada uno de los componentes del hechizo que colocara
en el caldero RGB

0-> 255 Ml {Rooibos, Greenish, Boost} > 765 ml

indica Lts pocion:> Cuanto componente se crea de cada sustancia ingresada.

Cual es el color final lineal de acuerdo a cantidades posterior al hechizo:

Formula = ColorFinal  = (QtyR)/? + QtyG*255/?  + QtyB*255*255/?
"""

r = int( input("Cantidad de rooibos [0-255]") )
g = int( input("Cantidad de  greeninsh [0-255]") )
b = int( input("Cantidad de boost [0-255]") )

t = r + g + b  # ml de formula

fc = r/t + g/t*255 + b/t*255*255

print(f"Cantidad de ml {t}ml c:{fc}")