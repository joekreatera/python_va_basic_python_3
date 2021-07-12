from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import OrthographicLens
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent, CollisionBox, CollisionSegment
from panda3d.core import Point3, Vec3
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
        
        #messenger.toggleVerbose()

    def setup(self,task):
        lens = OrthographicLens()
        lens.setFilmSize(25,20)
        base.camNode.setLens(lens)
        
        self.player = self.scene.attachNewNode("Player")
        
        self.marioGfx = self.scene.find('root/mario')
        self.marioGfx.reparentTo(self.player)
        
        self.jumpAvailable = False
        self.gravity = -.5
        self.verticalTime = 0
        self.v0 = 0
        self.floorZ = 0
        self.onStairs = False
        self.jumpCounter = 1
        # input setup 
        
        self.input = {
        'up':False,
        'down': False,
        'left': False , 
        'right': False,
        'space': False
        }
        
        key_list = ['up','down','left','right']
        for k in key_list:
            self.accept(f'raw-arrow_{k}' , self.buildPress(k) )
            self.accept(f'raw-arrow_{k}-up', self.buildRelease(k) )
        
        self.accept(f'raw-space' , self.buildPress('space') )
        self.accept(f'raw-space-up', self.buildRelease('space') )
        
        
        # collision set up
        base.cTrav = CollisionTraverser()
        self.collisionHandlerEvent = CollisionHandlerEvent()
        self.collisionHandlerEvent.addInPattern('into-%in')
        self.collisionHandlerEvent.addOutPattern('outof-%in')

        ray = CollisionSegment(0,0,0,0,0,-.6)
        cNodePath = self.player.attachNewNode( CollisionNode('marioRay') )
        cNodePath.node().addSolid(ray)
        cNodePath.node().setIntoCollideMask(0x03)
        cNodePath.node().setFromCollideMask(0x03)
        cNodePath.show()
        base.cTrav.addCollider(cNodePath, self.collisionHandlerEvent)


        self.floor1 = self.createSquareCollider(-1.8, -5.5 , 9.3, .5, 'floor0' , 'floor1HitBox', 'Floor1', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor2 = self.createSquareCollider(2.08, -2.5 , 8.0, .5, 'floor1' , 'floor2HitBox', 'Floor2', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor3_1 = self.createSquareCollider(3.6, 0.5 , 3.8, .5, 'floor2' , 'floor3_1HitBox', 'Floor3_1', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor3_2 = self.createSquareCollider(-6.3, 0.5 , 5, .5, 'pCube4' , 'floor3_2HitBox', 'Floor3_2', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor4 = self.createSquareCollider(1.8, 3.5 , 8.0, .5, 'floors' , 'floor4HitBox', 'Floor4', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        
        
        self.topStair = self.createSquareCollider(-6.8, 3.5 , 0.5, 2.5, 'topstair' , 'topStairHitBox', 'TopStair', self.enableStairs, self.disableStairs , self.stairsTexture, 0x2)
        self.middleStair= self.createSquareCollider(-0.86, 0.1 , 0.5, 2.5, 'middlestair' , 'middleStairHitBox', 'MiddleStair', self.enableStairs, self.disableStairs , self.stairsTexture, 0x2)
        self.bottomStair = self.createSquareCollider(-6.8, -2.5 , 0.5, 2.5, 'bottomstair' , 'bottomStairHitBox', 'BottomStair', self.enableStairs, self.disableStairs , self.stairsTexture, 0x2)
        
        #self.createInvisibleSquareCollider(0,0,8,3,"NewCollision","NewNode")
        #self.createInvisibleSquareCollider(-6,0,4,5,"NewCollisio2","NewNode2")
        base.cTrav.showCollisions(self.render)
        
        # self.player.setPos(3,0,-3.5)
        self.player.setPos(-8,0,-1.5)
        return Task.done

    def enableJump(self, evt):
        print(f'IN----> {evt}')
        self.floorZ = evt.getIntoNodePath().node().getParent(0).getTransform().getPos().z + 1
        self.jumpAvailable = True
    
    def disableJump(self, evt):
        print(f'Out----> {evt}')
        self.jumpAvailable = False

    def enableStairs(self, evt):
        print(f'IN----> {evt}')
        self.onStairs = True
    
    def disableStairs(self, evt):
        print(f'Out----> {evt}')
        self.onStairs = False

    def createSquareCollider(self, px,pz, w, h, modelName, collisionNodeName, nodeName , intoFunction, outFunction, texture, mask ):
        obj = self.scene.attachNewNode(nodeName)
        hitBox = CollisionBox( Point3(0,0,0), w, 5, h )
        cNodePath = obj.attachNewNode( CollisionNode(collisionNodeName) )
        cNodePath.node().addSolid(hitBox)
        cNodePath.node().setIntoCollideMask(mask)
        cNodePath.node().setFromCollideMask(mask)
        #cNodePath.show()
        base.cTrav.addCollider(cNodePath, self.collisionHandlerEvent)
        
        self.scene.find(f'root/{modelName}').reparentTo(obj)
        obj.setPos(px,0,pz)
        obj.setTexture(texture)
        
        self.accept(f'into-{collisionNodeName}' , intoFunction)
        self.accept(f'outof-{collisionNodeName}' , outFunction)
        
        
        return obj
    

    def createInvisibleSquareCollider(self, px,pz, w, h, collisionNodeName, nodeName , mask ):
        obj = self.scene.attachNewNode(nodeName)
        hitBox = CollisionBox( Point3(0,0,0), w, 5, h )
        cNodePath = obj.attachNewNode( CollisionNode(collisionNodeName) )
        cNodePath.node().addSolid(hitBox)
        cNodePath.node().setIntoCollideMask(mask)
        cNodePath.node().setFromCollideMask(mask)
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

    def applyMove(self):
        
        mv = Vec3(0,0,0)
        p = self.player.getPos()
        
        if( self.input["right"]):
            mv.x = -.1
            
        if( self.input["left"]):
            mv.x = .1
            
        """
        if( self.input["space"]):
            playerPos.z += .1
            
        if( self.input["down"]):
            playerPos.z -= .1
        """
        
        if( self.jumpAvailable and not self.onStairs ):
            self.jumpCounter = 1
            self.verticalTime = 0
            self.v0 = 0
            p.z = self.floorZ
            if(self.input["space"]):
                self.v0 = .165
                self.jumpAvailable = False
            
        if(not self.jumpAvailable and not self.onStairs):
            self.verticalTime += globalClock.getDt()
            mv.z = self.v0  + self.gravity*self.verticalTime
            
        if( self.onStairs):
            self.jumpCounter = 0
            self.v0 = 0
            if( self.input["down"]):
                mv.z = -.1
            if( self.input["up"]):
                mv.z = .1
            
        if( not self.onStairs ):
            if(not self.jumpAvailable):
                if(self.input["space"] and self.jumpCounter == 0):
                    self.v0 = .165
                    self.jumpAvailable = False
                    self.jumpCounter = 1
            
        p.x += mv.x
        p.z += mv.z
        
        self.player.setPos(p)
        
        # hacer que se pueda agarrar el martillo, cuando suceda : self.marioGfx.setSx(self.player  , -1)
        # self.hammer = self.createSquareCollider(6,1.5,.5,.5,'hammer','hammerHitbox', 'hammer', self.enableHammer, self.disableHammer, self.arcadeTexture, 0x02)
        
        
    def update(self, task):
        self.camera.setPos(0,35,0)
        self.camera.lookAt(self.scene)
        
        self.applyMove()
            
        return Task.cont  

s = DonkeyKong()
s.run()