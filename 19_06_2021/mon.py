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

  def loadPlane(self, texName, heading, pitch, roll, side, depth, height, scale):
    square = self.loader.loadModel("models/Square")
    tex1 = self.loader.loadTexture(f'models/{texName}')
    
    square.setTexture(tex1)
    square.reparentTo(self.render)
    
    square.setPos(side,depth,height)
    square.setHpr(heading, pitch, roll)
    square.setScale(scale,scale,scale)

  def setup(self, task):
    sc = 200
    d = 1.64*sc

    self.loadPlane("skybox_nx.jpg",  90, 0,  0,  -d, 0, 0,  1)
    self.loadPlane("skybox_px.jpg", -90, 0,  0,   d, 0, 0,  sc)
    self.loadPlane("skybox_nz.jpg",   0, 0,  0,   0, d, 0,  sc)
    self.loadPlane("skybox_pz.jpg", 180, 0,  0,   0,-d, 0,  sc)
    self.loadPlane("skybox_ny.jpg",   0, 0, 90,   0, 0, d,  sc)
    self.loadPlane("skybox_py.jpg",   0, 0, 90,   0, 0,-d,  sc)
    
    return Task.done

  def update(self, task):
    self.angle += 0.2

    #self.camara.setPos(-10,-10,0)
    #self.camera.lookAt(0,0,0)
    self.camera.setPos(100,100,0)
    self.camera.setHpr(self.angle, 0, 0)
    
    return Task.cont

s = Skybox()
s.run()