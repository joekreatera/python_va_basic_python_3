from InputManager import *

class Player:
    def __init__(self, pandaNode):
        self.gameObject = pandaNode
        
    def update(self, world , dt ):
        up = InputManager.getInput(InputManager.arrowUp)
        down = InputManager.getInput(InputManager.arrowDown)
        
        pos = self.gameObject.getPos(world)
        
        if( up ):
            self.gameObject.setZ(world, pos.z + 2*dt)
        
        if( down ):
            self.gameObject.setZ(world, pos.z - 2*dt)
        