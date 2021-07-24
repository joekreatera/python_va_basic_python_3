from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent
from panda3d.core import Point3, Vec3
from panda3d.core import loadPrcFileData
from random import random
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from InputManager import *

# loadPrcFileData('', 'win-size 800 600')
# loadPrcFileData('', 'want-directtools #t')
# loadPrcFileData('', 'want-tk #t')

class Starfox(ShowBase):
    def __init__(self):
        super().__init__(self)
        
        self.scene = self.loader.loadModel("models/world.egg")
        playerTexture = self.loader.loadTexture('models/starfoxShip.jpg')
        enemyTexture = self.loader.loadTexture('models/enemyShip.jpg')
        bulletTexture = loader.loadTexture('models/shot.png')
        
        self.scene.reparentTo(self.render)
        
        self.player = self.scene.find("player")
        self.player.setTexture(playerTexture)
        self.player.setPos(3,3,3)
        
        self.dynamic_enemy = self.scene.find("enemy1")
        self.dynamic_enemy.setTexture(enemyTexture)
        self.dynamic_enemy.setPos(6,6,6)
        
        
        self.taskMgr.add(self.update, "update")
        
        
        InputManager.initWith(self, 
        [InputManager.arrowUp,
        InputManager.arrowDown,
        InputManager.arrowLeft,
        InputManager.arrowRight,
        InputManager.space,
        InputManager.keyX,
        InputManager.keyV
        ])
        
    def update(self, evt):
        return Task.cont
        

starfox = Starfox()
starfox.run()