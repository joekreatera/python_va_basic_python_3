from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import OrthographicLens
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent, CollisionBox
from panda3d.core import Point3
from panda3d.core import loadPrcFileData
from math import sin, cos

loadPrcFileData('', 'win-size 800 600')
# loadPrcFileData('', 'want-directtools #t')
# loadPrcFileData('', 'want-tk #t')

loadPrcFileData('', 'textures-auto-power-2 #f')
loadPrcFileData('', 'textures-power-2 none')
loadPrcFileData('', 'textures-square none')

class DonkeyKong(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.angle = 0
        self.taskMgr.add(self.setup, "setup")
        self.taskMgr.add(self.update, "update")

        self.scene = self.loader.loadModel('models/DKSet')
        self.scene.reparentTo(self.render)
        
        self.arcadeTexture = self.loader.loadTexture('models/dk-arcade.png')
        self.scene.setTexture(self.arcadeTexture)
        self.scene.setTransparency(1)
        
        self.blocksTexture = self.loader.loadTexture('models/block.png')
        self.stairsTexture = self.loader.loadTexture('models/stairs.png')
        
        messenger.toggleVerbose()

    def setup(self,task):
        lens = OrthographicLens()
        lens.setFilmSize(25,20)
        base.camNode.setLens(lens)
        
        self.player = self.scene.attachNewNode("Player")
        
        self.marioGfx = self.scene.find('root/mario')
        self.marioGfx.reparentTo(self.player)
        
        
        # input setup 
        
        self.input = {
        'up':False,
        'down': False,
        'left': False , 
        'right': False 
        }
        
        key_list = ['up','down','left','right']
        for k in key_list:
            self.accept(f'raw-arrow_{k}' , self.buildPress(k) )
            self.accept(f'raw-arrow_{k}-up', self.buildRelease(k) )
        
        
        # collision set up
        base.cTrav = CollisionTraverser()
        self.collisionHandlerEvent = CollisionHandlerEvent()
        self.collisionHandlerEvent.addInPattern('into-%in')
        self.collisionHandlerEvent.addOutPattern('outof-%out')

        
        self.createInvisibleSquareCollider(0,0,8,5,"NewCollision","NewNode")
        self.createInvisibleSquareCollider(-6,0,4,5,"NewCollisio2","NewNode2")
        base.cTrav.showCollisions(self.render)
        return Task.done

    def createInvisibleSquareCollider(self, px,pz, w, h, collisionNodeName, nodeName ):
        obj = self.scene.attachNewNode(nodeName)
        hitBox = CollisionBox( Point3(0,0,0), w, 5, h )
        cNodePath = obj.attachNewNode( CollisionNode(collisionNodeName) )
        cNodePath.node().addSolid(hitBox)
        cNodePath.show()
        base.cTrav.addCollider(cNodePath, self.collisionHandlerEvent)
        obj.setPos(px,0,pz)
        
    
    def buildPress(self,key):
        def pressKey():
            self.input[key] = True
        return pressKey
        
    def buildRelease(self, key):
        def releaseKey():
            self.input[key] = False
        return releaseKey
        
    def update(self, task):
        self.camera.setPos(0,35,0)
        self.camera.lookAt(self.scene)
        
        playerPos = self.player.getPos()
        
        if( self.input["up"]):
            playerPos.z += .1
        
        if( self.input["down"]):
            playerPos.z -= .1
        
        if( self.input["right"]):
            playerPos.x -= .1
            
        if( self.input["left"]):
            playerPos.x += .1
        
        self.player.setPos(playerPos)
            
        return Task.cont  

s = DonkeyKong()
s.run()