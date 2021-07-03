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
        
        self.taskMgr.add(self.setup, "setup")
        self.taskMgr.add(self.update, "update")
    
    def loadPlane(self, texName, heading, pitch, roll , side, depth, height):
        square = self.loader.loadModel("models/Square")
        tex1 = self.loader.loadTexture(f'models/{texName}')
        square.setTexture(tex1)
        square.reparentTo(self.render)
        square.setPos(side,depth,height)
        square.setHpr(heading, pitch, roll )
        
    def setup(self,task):
        self.loadPlane('skybox_nx.jpg', 90 ,0 ,0  , -5 , 0 ,  0)
        self.loadPlane('skybox_px.jpg', -90 ,0 ,0  , 5 ,  0  , 0)
        
        return Task.done
        
    def update(self, task):
        self.camera.setPos(0,0,0)
        self.camera.lookAt(10,0,0)
        return Task.cont  

s = Skybox()
s.run()