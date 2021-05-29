# Icrecream Shop
"""

Simular la llegada de clientes
Cada cliente tendra una cantidad de dinero aleatoria, asi como un sabor (que quiera) y un nombre 
que será un numero entre el 1 y el 100 para detectarlos. Los nombres podran ser mapeados a nombres reales opcionalmente

El cliente tiene una cantidad de dinero que determinará el tamaño del helado y tendrá 
un sabor favorito. Si la tienda le da el sabor que quiere, entonces dara propina, un aleatorio entre el 5 y el 10% 
del costo del helado siempre y cuando tenga dinero para hacerlo. 

La tienda de helados tiene 3 tamaños, 1b, 2b, 3b. 
La tienda tambien tiene 1 especial, BananaSplit. El banana split es en general un helado de 3 bolas que cuesta 20p
mas. 

Cada helado que se entrega a un cliente solo se diferencia por la cantida dde bolas de helado y todas las bolas 
de helado son del mismo sabor. 

Los clientes cuando llegan pueden pedir helado de 1,2,3b o banasplit, es aleatorio, y no depende de su dinero. 
Sin embargo, despuyes de pedirlo, si no cuentan copn el dinero suficiente, los clientes se van. 

El simulador tiene que entregar resultados de cantidad de dinero recabada a lo largo de 5 dias, en los cuales
pueden llegar un minimo de 10 clientes y un maximo de 30.

Se deberá resolver usando metodologia orientada a objetos, con al menos las Clases:
cliente
helado
bananasplit extiende/hereda de helado

La salida del programa deberá indicar por cada cliente qué sucedió y al final dar la cuenta total. 
5 sabores... 10 pesos por bola -> 50
cantidad de dinero [5, 70]
"""