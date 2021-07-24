from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent
from panda3d.core import Point3, Vec3
from panda3d.core import loadPrcFileData
from random import random
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from InputManager import *
from Path import *
from Player import *
# loadPrcFileData('', 'win-size 800 600')
#loadPrcFileData('', 'want-directtools #t')
#loadPrcFileData('', 'want-tk #t')

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
        self.player.setPythonTag("ObjectController" , Player(self.player) )
        #self.player.setPos(20,20,20)
        
        self.dynamic_enemy = self.scene.find("enemy1")
        self.dynamic_enemy.setTexture(enemyTexture)
        #self.dynamic_enemy.setPos(6,6,6)
        
        self.building_enemy = self.scene.find("building_enemy")
        #self.building_enemy.setPos(20,20,20)
        
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
        
        base.cTrav = CollisionTraverser()
        self.CollisionHandlerEvent = CollisionHandlerEvent()
        
        self.CollisionHandlerEvent.addInPattern('into-%in')
        self.CollisionHandlerEvent.addInPattern('out-%in')
        
        self.accept('into-collision_player' , self.crash)
        self.accept('into-collision_plane' , self.crash)
        self.accept('into-collision_enemy' , self.crash)
        
        base.cTrav.addCollider( self.scene.find("player/collision**") ,self.CollisionHandlerEvent )
        base.cTrav.addCollider( self.scene.find("basePlane/collision**") ,self.CollisionHandlerEvent )
        
        base.cTrav.showCollisions(self.render)
        
        self.rails = self.scene.attachNewNode("rails")
        self.scene.find("basePlane").setPos(self.scene,0,0,-10)
        self.scene.find("basePlane").setHpr(70,0,0)
        self.scene.setPos(self.scene,0,0,0)
        self.player.reparentTo(self.rails)
        self.player.setPos(self.rails, 0,0,0)
        
        
    def crash(self, evt):
        print(evt)
        
    def update(self, evt):
        
        rails_pos = self.rails.getPos(self.scene)
        new_y = rails_pos.y + globalClock.getDt()*10
        self.rails.setPos( Path.getXOfY(new_y) , new_y, 1 )
        self.rails.setHpr( Path.getHeading(new_y) ,0 ,0 )
        
        #self.camera.lookAt(self.player)
        self.camera.setHpr( Path.getHeading(new_y) ,0 ,0 )
        self.camera.setPos(self.rails, 0,-30,0)
        
        self.player.getPythonTag("ObjectController").update(self.scene, globalClock.getDt() )
        return Task.cont
        

starfox = Starfox()
starfox.run()