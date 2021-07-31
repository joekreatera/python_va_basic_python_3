from InputManager import *
from Bullet import *
class Player:
    def __init__(self, pandaNode, ctrav, collisionHandler):
        self.gameObject = pandaNode
        self.px = 0
        self.pz = 0
        self.ctrav= ctrav
        self.collisionHandler = collisionHandler
        
        self.shouldShoot = True
        
    def update(self, world , dt , globalWorld,  bullet):
        up = InputManager.getInput(InputManager.arrowUp)
        down = InputManager.getInput(InputManager.arrowDown)
        left = InputManager.getInput(InputManager.arrowLeft)
        right = InputManager.getInput(InputManager.arrowRight)
        shoot = InputManager.getInput(InputManager.space)
        
        
        
        vel = 20*dt
        self.pz += vel if up else 0
        self.pz -= vel if down else 0
        self.px += vel if right else 0
        self.px -= vel if left else 0
        
        limitX = 24
        limitZ = 12
        
        camLimitX = limitX*2.0/3
        camLimitZ = limitZ*2.0/3
        
        self.pz = min(max( self.pz, -limitZ) ,limitZ )
        self.px = min(max( self.px, -limitX) ,limitX )
        
        self.gameObject.setZ(world, self.pz)
        self.gameObject.setX(world, self.px)
        
        camZ = min(max( self.pz, -camLimitZ) ,camLimitZ )
        camX = min(max( self.px, -camLimitX) ,camLimitX )
        
        
        if( shoot and self.shouldShoot ):
            self.shouldShoot = False
            b = Bullet(bullet, 
            globalWorld, 
            self.gameObject.getPos(globalWorld) , 
            self.ctrav , 
            self.collisionHandler, 
            globalWorld.getRelativeVector(self.gameObject, Vec3(0,1,0) ) ,
            50,
            0x4
            )
        
        if( not shoot and not self.shouldShoot ):
            self.shouldShoot = True
            
        return camX, camZ