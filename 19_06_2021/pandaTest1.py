from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3
from panda3d.core import loadPrcFileData
from math import sin, cos
from random import random
loadPrcFileData('', 'win-size 640 480')

class FirstApp(ShowBase):
    def __init__(self):
        super().__init__(self)
        base.messenger.toggleVerbose()
        self.taskMgr.add(self.setup, 'setup')
        self.taskMgr.add(self.update, 'update')
        self.angle = 0
        self.time = 0
        
    def setup(self,task):
        
        self.square = self.loader.loadModel("models/Square")
        self.square.setPos(0,0,0)
        
        for i in range(0,100):
            square2 = self.loader.loadModel("models/Square")
            texture = self.loader.loadTexture("models/logo_VGA.png")
            square2.setPos(random()*20-10,random()*20-10,random()*20-10)
            square2.setTexture(texture)
            square2.reparentTo(self.render)
            square2.setTransparency(1)
        
        self.square.setTransparency(1)
        self.square.setTexture(texture)
        self.square.reparentTo(self.render)
        return Task.done
    
    def update(self, task):
        self.time += 0.01
        xp = cos(self.time)*10
        yp = sin(self.time)*10
        
        self.camera.setPos(xp,yp,0)
        self.camera.lookAt(0,0,0)
        
        # self.square.setHpr(self.angle, 0, 0)
        # self.angle += 1
        return Task.cont
    
        
t = FirstApp()
t.run()