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
from random import random
from time import sleep
def getIntRandom(a,b):
    return a + int((b-a)*random())
    

class Icecream:
    CHOCOLATE = 0
    STRAWBERRY = 1
    LEMON = 2
    BERRY = 3
    VANILLA = 4
    COMBINED = 5
    BALL_COST = 10
    MAX_FLAVOUR = 4.99
    def __init__(self , balls = 1, force_flavour = -1):
        self.__price = balls*Icecream.BALL_COST
        
        if( force_flavour > -1 ):
            self.__flavour = min(Icecream.COMBINED, force_flavour)
        else:
            self.__flavour = getIntRandom(0,Icecream.MAX_FLAVOUR)

    def getFlavour(self):
        return [self.__flavour]
    
    def getPrice(self):
        return self.__price
        
    def __str__(self):
        return f'p: {self.__price} f:{self.__flavour}'
        
class BananaIcrecream(Icecream):
    EXTRA = 20
    def __init__(self):
        super().__init__(3, force_flavour = Icecream.COMBINED)
    
    
    def getFlavour(self):
        return [Icecream.CHOCOLATE, Icecream.STRAWBERRY, Icecream.VANILLA]
        
    def getPrice(self):
        return super().getPrice()+BananaIcrecream.EXTRA
    
    def __str__(self):
        return f'BANANA SPLIT ICREAM  p: {self.getPrice()} f:{self.getFlavour() }'
        
class Client:
    MAX_NAMES = 10
    MAX_BUDGET = 70
    MIN_BUDGET = 5
    FIRST_NAME = ["Mario","Ana","Jorge","Claudia","Dany","Ari","Jose","Jesus","Eva","Adan"]
    LAST_NAME = ["Glez","Perez","Hdez","Fdez","Mora","Ruiz","Mayo","Rojo","Flores","Rocha"]
    def __init__(self):
        self.__name = Client.FIRST_NAME[getIntRandom(0,Client.MAX_NAMES-0.00001)] + " " + Client.LAST_NAME[getIntRandom(0,Client.MAX_NAMES-0.0001)]
        self.__budget = Client.MIN_BUDGET + random()*(Client.MAX_BUDGET-Client.MIN_BUDGET)
        self.__flavour = getIntRandom(0,Icecream.MAX_FLAVOUR)
        
    def getFlavour(self):
        return self.__flavour
    
    def getBudget(self):
        return self.__budget
    def getName(self):
        return self.__name
    def __str__(self):
        return f'{self.__name} {self.__flavour} {self.__budget}'
        

class IcecreamShop():
    def __init__(self):
        pass
    
    def day(self):
        clients = getIntRandom(10,30.99)
        earnings = 0
        
        for i in range(1,clients):
            sleep(0.1)
            c = Client()
            h = None 
            if( random() > 0.7 ):
                h = BananaIcrecream()
            else:
                h = Icecream()
            if c.getBudget() >= h.getPrice():
                earnings += c.getBudget()
                if c.getFlavour() in h.getFlavour():
                    # tip
                    tip = 0.05*h.getPrice() + h.getPrice()*(.05*random())
                    money_available = c.getBudget() - h.getPrice()
                    t = min(money_available, tip)
                    earnings += t
                    print(f'{i}:{c} did spend icecream {h} with a tip of {t}')
                else:
                    print(f'{i}:{c} did spend icecream {h}')
            else:
                print(f'{i}:{c} did not spend anything on icecream {h}')
        print("Day earnings: " + str(earnings) )
        return earnings
        
def tests():
    ice1 = Icecream()
    print(ice1)
    ice2 = Icecream(balls = 2)
    print(ice2)
    ice3 = Icecream(balls = 2, force_flavour = Icecream.VANILLA)
    print(ice3)
    ice4 = Icecream(balls = 3, force_flavour = 10)
    print(ice4)
    bc = BananaIcrecream()
    print(bc)
    c = Client()
    print(c)
    c = Client()
    print(c)
    
def do_simulation():
    shop = IcecreamShop()
    total = 0
    for i in range(0,5):
        print(f"################################## DAY {i}#################################################")
        total += shop.day()
    
    print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  TOTAL EARNINGS (${total})   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

do_simulation()