from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3
from panda3d.core import loadPrcFileData
from math import sin, cos

loadPrcFileData('', 'win-size 640 480')
# loadPrcFileData('', 'want-directtools #t')
# loadPrcFileData('', 'want-tk #t')

class Skybox(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.angle = 0
        self.taskMgr.add(self.setup, "setup")
        self.taskMgr.add(self.update, "update")
        self.input = {
        'up':False,
        'down': False,
        'left': False , 
        'right': False 
        }
    
    def loadPlane(self, texName, heading, pitch, roll , side, depth, height, scale):
        square = self.loader.loadModel("models/Square")
        tex1 = self.loader.loadTexture(f'models/{texName}')
        square.setTexture(tex1)
        square.reparentTo(self.render)
        square.setPos(side,depth,height)
        square.setHpr(heading, pitch, roll )
        square.setScale(scale,scale,scale)
        return square
        
    def setup(self,task):
        sc = 200
        d  = 1.638*sc
        self.loadPlane('skybox_nx.jpg', 90  ,0      ,0  , -d    ,  0    , 0     , sc)
        self.loadPlane('skybox_px.jpg', -90 ,0      ,0  , d     ,  0    , 0     , sc)
        self.loadPlane('skybox_nz.jpg', 0   ,0      ,0  , 0     ,  d    , 0     , sc)
        self.loadPlane('skybox_pz.jpg', 180 ,0      ,0  , 0     ,  -d   , 0     , sc)
        self.loadPlane('skybox_py.jpg', 180 ,90     ,0  , 0     ,  0    , d     , sc)
        self.loadPlane('skybox_ny.jpg', 0   ,-90    ,0  , 0     ,  0    , -d    , sc)
        
        self.accept('raw-arrow_up', self.pressUp)
        self.accept('raw-arrow_up-up', self.releaseUp)
        
        self.accept('raw-arrow_down', self.pressDown)
        self.accept('raw-arrow_down-up', self.releaseDown)
        
        self.accept('raw-arrow_left', self.pressLeft)
        self.accept('raw-arrow_left-up', self.releaseLeft)
        
        self.accept('raw-arrow_right', self.pressRight)
        self.accept('raw-arrow_right-up', self.releaseRight)
        
        
        self.altitude = 0
        return Task.done
    
    def pressUp(self):
        print("Pressing up")
        self.input["up"]  = True
        
    def releaseUp(self):
        print("Pressing up")
        self.input["up"]  = False
    
    def pressDown(self):
        print("Pressing down")
        self.input["down"]  = True
        
    def releaseDown(self):
        print("Pressing down")
        self.input["down"]  = False
        
    def pressLeft(self):
        print("Pressing left")
        self.input["left"]  = True
        
    def releaseLeft(self):
        print("Pressing left")
        self.input["left"]  = False
        
    def pressRight(self):
        print("Pressing right")
        self.input["right"]  = True

    def releaseRight(self):
        print("Pressing right")
        self.input["right"]  = False
            
    def update(self, task):
        # self.camera.setPos(-5,5,0)
        if( self.input["up"] ):
            self.altitude += 0.5
        if( self.input["down"] ):
            self.altitude -= 0.5
        if( self.input["left"] ):
            self.angle -= 0.01
        if( self.input["right"] ):
            self.angle += 0.01
            
        self.camera.setPos(0, 0,0)
        #self.camera.setHpr(self.angle , 0 , 0)
        #self.angle += 0.2
        x = 100*sin(self.angle)
        y = 100*cos(self.angle)
        
        self.camera.lookAt(x,y,self.altitude)
        return Task.cont  

s = Skybox()
s.run()