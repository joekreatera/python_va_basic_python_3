# hacer un juego de narrativa interactiva, el usuario responde hacia donde quiere ir
# el programa debera presentar una historia, debe tener 4 finales, con al menos 2 decisiones.


def ask(msg, opt1, opt2):
    print(msg)
    print("presiona:")
    print(opt1)
    print(opt2)
    pr = int(input("Selección:"))
    return pr

def printStory(story):
    print("**************************************")
    print(story)
    print("**************************************")


r1 = ask("Estas en el espacio, solo, con tu traje y una nave de 2 km de largo, \n existe una capsula de escape y el largo corredor",
            "Si decides ir por el corredor (1)", 
            "si decides la capsula, presiona (2)")

if r1 == 1:
    r1 = ask("Has llegado a una cámara criogenica" , "levantar a los individuos de la cámara (1)" , "no levantar (2)" )
    if r1 == 1 :
        printStory("has despertado al jefe de la misión que empieza a disparar contra ti, al final lo ves desde el suelo diciendo \
    '\n Demasiado cerca de ese xenomorfo' ")
    else:
        printStory("Te acercas a las vitrinas y desconectas la alimentación, \nahora estas realmente solo....")
else:
    r1 = int(input("Has salido de la nave, ves un planeta. \nSi decides ir al planeta selecciona 1, si decides seguir hacia en frente, 2."))
    if r1 == 1:
        printStory("Has llegado a casa en un mar de lava y carroña, \nnada como el dulce aroma de la destruccion");
    else:
        printStory("La nave se ha dado cuenta y ha enviado una señal de auxilio, \npronto llegan a tu rescate... pero no se ven amigables...")