from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import OrthographicLens
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

    def setup(self,task):
        lens = OrthographicLens()
        lens.setFilmSize(25,20)
        base.camNode.setLens(lens)
        
        self.player = self.scene.attachNewNode("Player")
        
        self.marioGfx = self.scene.find('root/mario')
        self.marioGfx.reparentTo(self.player)
        
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
        
        return Task.done
    
    def buildPress(self,key):
        def pressKey():
            self.input[key] = True
            print(f"press {key} {self.input}")
        return pressKey
        
    def buildRelease(self, key):
        def releaseKey():
            self.input[key] = False
            print(f"release {key} {self.input}")
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