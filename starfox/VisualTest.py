from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from panda3d.core import DirectionalLight, AmbientLight, Fog, PointLight
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import AntialiasAttrib

from panda3d.core import loadPrcFileData
from panda3d.core import Vec3



class VisualTest(ShowBase):
    def __init__(self):
        super().__init__(self)
        
        self.scene = loader.loadModel('models/world')
        pTexture = loader.loadTexture('models/starfoxShip.jpg')
        self.player = self.scene.find("player")
        self.player.setTexture(pTexture)
        
        
        self.player.setPos(50,50,3)
        self.scene.reparentTo(self.render)
        self.taskMgr.add(self.update , "update")
        
    def update(self, evt):
        self.camera.setPos(60,60,20)
        self.camera.lookAt(self.player)
        
        return Task.cont
        
vt = VisualTest()
vt.run()