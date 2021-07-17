from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import OrthographicLens, TextureStage
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent, CollisionBox, CollisionSegment, CollisionSphere
from panda3d.core import Point3, Vec3
from panda3d.core import loadPrcFileData
from panda3d.physics import *
from math import sin, cos
from random import random
from direct.interval.IntervalGlobal import *

from direct.gui.DirectGui import *

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
        
        self.dkTimer = -1
        self.lifeCounter = 3
        self.playerLost = False
        self.playerWon = False
        #messenger.toggleVerbose()

    def setup(self,task):
        lens = OrthographicLens()
        lens.setFilmSize(25,20)
        base.camNode.setLens(lens)
        
        self.player = self.scene.attachNewNode("Player")
        
        self.marioGfx = self.scene.find('root/mario')
        self.marioGfx.reparentTo(self.player)
        self.marioGfx.setTwoSided(True)
        
        self.lifes = [
        self.scene.attachNewNode("life1"),
        self.scene.attachNewNode("life2"),
        self.scene.attachNewNode("life3")
        ]
        self.marioGfx.instanceTo(self.lifes[0])
        self.marioGfx.instanceTo(self.lifes[1])
        self.marioGfx.instanceTo(self.lifes[2])
        
        self.lifes[0].setPos(-9,0,7.5)
        self.lifes[1].setPos(-10,0,7.5)
        self.lifes[2].setPos(-11,0,7.5)

        
        self.hammerTime = False
        
        self.hammerDown = self.scene.find('root/hammerdowm')
        self.hammerDown.reparentTo(self.marioGfx)
        self.hammerDown.setPos(1,0,0)
        
        self.hammerUp = self.scene.find('root/hammerup')
        self.hammerUp.reparentTo(self.marioGfx)
        self.hammerUp.setPos(0,0,1)
        
        frame1 = Func(self.hammerFrame1)
        frame2 = Func(self.hammerFrame2)
        delay = Wait(0.1)
        self.hammerSequence = Sequence(frame1, delay, frame2, delay)
        # self.hammerSequence.loop()
        
        self.hammerUp.hide()
        self.hammerDown.hide()
        
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
        #cNodePath.show()
        base.cTrav.addCollider(cNodePath, self.collisionHandlerEvent)

        self.donkeykong = self.scene.find('root/donkeykong')
        self.donkeykonghit = self.createSquareCollider(8.7,5,1,1,'donkeykong','dkhitbox', 'DK' , self.reachedDK, self.exitDK , self.arcadeTexture, 0x02)
        self.createDkSequence()
        self.dk_sequence.start()
        
        self.floor1 = self.createSquareCollider(-1.8, -5.5 , 9.3, .5, 'floor0' , 'floor1HitBox', 'Floor1', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor2 = self.createSquareCollider(2.08, -2.5 , 8.0, .5, 'floor1' , 'floor2HitBox', 'Floor2', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor3_1 = self.createSquareCollider(3.6, 0.5 , 3.8, .5, 'floor2' , 'floor3_1HitBox', 'Floor3_1', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor3_2 = self.createSquareCollider(-6.3, 0.5 , 5, .5, 'pCube4' , 'floor3_2HitBox', 'Floor3_2', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        self.floor4 = self.createSquareCollider(1.8, 3.5 , 8.0, .5, 'floors' , 'floor4HitBox', 'Floor4', self.enableJump, self.disableJump , self.blocksTexture, 0x1)
        
        self.hammer = self.createSquareCollider(6,1.5,0.5,0.5,'hammer', 'hammerHitBox', 'hammer', self.enableHammer, self.disableHammer, self.arcadeTexture, 0x02) 
        self.topStair = self.createSquareCollider(-6.8, 3.5 , 0.5, 2.5, 'topstair' , 'topStairHitBox', 'TopStair', self.enableStairs, self.disableStairs , self.stairsTexture, 0x2)
        self.middleStair= self.createSquareCollider(-0.86, 0.1 , 0.5, 2.5, 'middlestair' , 'middleStairHitBox', 'MiddleStair', self.enableStairs, self.disableStairs , self.stairsTexture, 0x2)
        self.bottomStair = self.createSquareCollider(-6.8, -2.5 , 0.5, 2.5, 'bottomstair' , 'bottomStairHitBox', 'BottomStair', self.enableStairs, self.disableStairs , self.stairsTexture, 0x2)
        
        self.leftWall = self.createInvisibleSquareCollider(-12.5, 0, 1, 10 , 'leftWallHitBox','leftWall',0x1)
        self.rightWall = self.createInvisibleSquareCollider(11.3, 0, 1, 20 , 'rightWallHitBox','rightWall',0x1)
        
        self.barrelDestroyer = self.createInvisibleSquareCollider(-.5,-10,10.5,1, 'barrelDestroyerHitBox' , 'barrelDestroyer'  ,0x1) 
        self.barrelBridge = self.createInvisibleSquareCollider(-0.4,0.5,2,0.5, 'barrelBridgeHitBox' , 'barrelBridge'  ,0x4)
        self.accept('into-barrelCollider', self.barrelCrash)
        base.enableParticles()
        
        self.physicsCollisionPusher = PhysicsCollisionHandler()
        gravity = ForceNode('world-forces')
        gravityP = render.attachNewNode(gravity)
        gravityForce = LinearVectorForce(0,0,-9.81)
        gravity.addForce(gravityForce)
        base.physicsMgr.addLinearForce(gravityForce)
        
        
        #self.createInvisibleSquareCollider(0,0,8,3,"NewCollision","NewNode")
        #self.createInvisibleSquareCollider(-6,0,4,5,"NewCollisio2","NewNode2")
        #base.cTrav.showCollisions(self.render)
        
        # self.accept('raw-a', self.throwBarrel)
        # self.player.setPos(3,0,-3.5)
        self.player.setPos(-8,0,-1.5)
        return Task.done

    def reachedDK(self, evt):
        pass
    
    def exitDK(self, evt):
        pass

    def calcNextBarrelThrow(self):
        self.dkTimer = random()*3+3

    def changeDkFrame(self, dk,new_u, new_v):
        self.dkTimer = -1
        dk.setTexOffset( TextureStage.getDefault() , new_u , new_v )

    def createDkSequence(self):
        f1 = Func(self.changeDkFrame, self.donkeykong , 0.1408067 - 0.0446603 , 0 )
        f2 = Func(self.changeDkFrame, self.donkeykong , 0.0431023 - 0.0446603 , 0.806672 - 0.703844 )
        f3 = Func(self.changeDkFrame, self.donkeykong , 0 , 0 )
        th = Func(self.throwBarrel)
        reset = Func(self.calcNextBarrelThrow)
        d = Wait(0.2)
        
        self.dk_sequence = Sequence(f1,d,f2,d,f3,th,d,f1,reset)


    def barrelCrash(self, evt):
        physicalBarrel = evt.getIntoNodePath().node().getParent(0).getParent(0)
        other = evt.getFromNodePath().node().getParent(0)
        
        print(f'{physicalBarrel.name} {other.name} ')
        
        if( other.name == 'leftWall' or other.name == 'rightWall'):
            forceNode = physicalBarrel.getChildren()[1]
            force = forceNode.getForce(0)
            force.setVector( force.getLocalVector().x*-1 , 0 ,0 )
            forceNode.clear()
            forceNode.addForce(force)
            
        if( other.name == 'barrelDestroyer' ):
            self.scene.node().removeChild( physicalBarrel.getParent(0) )
        
        
        if( other.name == 'Player' ):
            if(self.hammerTime):
                self.scene.node().removeChild( physicalBarrel.getParent(0) )
            else:
                self.minusLife()
    
    def minusLife(self):
        self.lifes[self.lifeCounter-1].hide()
        self.lifeCounter -= 1
        
        if( self.lifeCounter <= 1):
            self.playerLost = True

    def hammerFrame1(self):
        self.hammerUp.show()
        self.hammerDown.hide()

    
    def hammerFrame2(self):
        self.hammerUp.hide()
        self.hammerDown.show()
    

    def enableHammer(self, evt):
        self.hammerTime = True
        self.scene.node().removeChild( evt.getIntoNodePath().node().getParent(0) )
        self.hammerSequence.loop()
                
    def disableHammer(self, evt):
        pass

    def enableJump(self, evt):
        #print(f'IN----> {evt}')
        self.floorZ = evt.getIntoNodePath().node().getParent(0).getTransform().getPos().z + 1
        self.jumpAvailable = True
    
    def disableJump(self, evt):
        #print(f'Out----> {evt}')
        self.jumpAvailable = False

    def enableStairs(self, evt):
        #print(f'IN----> {evt}')
        self.onStairs = True
    
    def disableStairs(self, evt):
        #print(f'Out----> {evt}')
        self.onStairs = False



    def throwBarrel(self):
        barrelNode = self.scene.attachNewNode("PhysicalBarrel")
        physicalBarrel = ActorNode("physics_barrel")
        physicalBarrel.getPhysicsObject().setMass(0.01)
        
        barrel = barrelNode.attachNewNode(physicalBarrel)
        base.physicsMgr.attachPhysicalNode(physicalBarrel)
        
        visualBarrel = barrel.attachNewNode("BarrelCopy")
        originalBarrel = self.scene.find('root/barrel')
        originalBarrel.instanceTo(visualBarrel)
        visualBarrel.setPos(0,-100,0)
        
        sphere = CollisionSphere(0.16,100,0,0.5)
        cNodePath = visualBarrel.attachNewNode( CollisionNode("barrelCollider") )
        cNodePath.node().addSolid(sphere)
        cNodePath.node().setIntoCollideMask(0x05)
        cNodePath.node().setFromCollideMask(0x05)
        #cNodePath.show()
        
        self.physicsCollisionPusher.addCollider(cNodePath, barrel)
        base.cTrav.addCollider(cNodePath, self.physicsCollisionPusher)
        
        barrelForceNode = ForceNode("barrelForce")
        barrel.attachNewNode(barrelForceNode)
        barrelForce = LinearVectorForce(-8,0,0,1,False)
        barrelForceNode.addForce(barrelForce)
        physicalBarrel.getPhysical(0).addLinearForce(barrelForce)
        
        barrelNode.setPos(self.scene,7 , 0 , 4.5)
        
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
        #cNodePath.show()
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
            self.marioGfx.setSx(self.player , -1)        
            self.lifes[0].setSx(-1)
            self.lifes[1].setSx(-1)
            self.lifes[2].setSx(-1)
                    
            
        if( self.input["left"]):
            mv.x = .1
            self.marioGfx.setSx(self.player , 1)
            self.lifes[0].setSx(1)
            self.lifes[1].setSx(1)
            self.lifes[2].setSx(1)
            
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
        
        if( self.dkTimer > -1):
            self.dkTimer -= globalClock.getDt()
            if(self.dkTimer <= 0):
                self.dk_sequence.start()
        
        if( self.playerLost):
            text = DirectLabel(text="Player Lost" , text_scale=(0.5,0.5) )
            return Task.done
            
        if( self.playerWon):
            text = DirectLabel(text="Player Won" , text_scale=(0.5,0.5) )
            return Task.done
            
                    
        self.applyMove()
            
        return Task.cont  

s = DonkeyKong()
s.run()