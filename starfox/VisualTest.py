from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from panda3d.core import DirectionalLight, AmbientLight, Fog, PointLight
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import AntialiasAttrib

from panda3d.core import loadPrcFileData
from panda3d.core import Vec3

from math import sin, cos
loadPrcFileData("","framebuffer-multisample 1")
loadPrcFileData("","multisamples 2")


class VisualTest(ShowBase):
    def __init__(self):
        self.var1 = 0
        super().__init__(self)
        
        self.scene = loader.loadModel('models/world')
        pTexture = loader.loadTexture('models/starfoxShip.jpg')
        self.player = self.scene.find("player")
        self.player.setTexture(pTexture)
        
        base.setBackgroundColor(.1,.1,.1,1)
        self.player.setPos(50,50,1)
        self.scene.reparentTo(self.render)
        
        self.ambient = AmbientLight('ambient')
        self.ambient.color = (.1,0.1,0.1,1)
        self.ambientPath = self.render.attachNewNode(self.ambient)
        self.render.setLight(self.ambientPath)

        self.dirLight = DirectionalLight('dir light')
        self.dirLight.color = (1,1,1,1)
        #self.dirLight.setShadowCaster(True, 512,512)
        self.dirPath = self.render.attachNewNode(self.dirLight)
        self.dirPath.setHpr(0,-90,0)
        self.render.setLight(self.dirPath)

        
        self.pointLight = PointLight('point light')
        self.pointLight.color = (1,1,1,1)
        self.pointLightPath = self.render.attachNewNode(self.pointLight)
        self.pointLightPath.setPos(70,72.5,4)
        self.pointLight.attenuation = (.5,0,0)
        #self.pointLight.setShadowCaster(True, 2048,2048)
        self.render.setLight(self.pointLightPath)
        
        self.fog = Fog('fog')
        self.fog.setColor(.1,.1,.1)
        self.fog.setExpDensity(.3)
        self.fog.setLinearRange(150,300)
        self.fog.setLinearFallback(45,160,320)
        self.render.setFog(self.fog)
        
        
        self.render.setShaderAuto()
        self.render.setAntialias(AntialiasAttrib.MMultisample)
        
        
        filters = CommonFilters(base.win, base.cam)
        filters.setBloom(size='large')
        filters.setAmbientOcclusion(strength=0.6, falloff=0.005, radius=0.1)
        #filters.setCartoonInk(separation=2, color=(0,0,0,1))
        
        
        self.taskMgr.add(self.update , "update")
        
    def update(self, evt):
        # self.camera.setPos(60,60,20)
        
        xp = 50 + cos(self.var1)*20
        yp = 50 + sin(self.var1)*20
        # max(10.0,sin(self.var1)*300)
        self.camera.setPos(xp,yp, 10)
        # self.dirPath.setHpr(0,self.var1,0)
        self.camera.lookAt(self.player)
        self.var1 += .005
        return Task.cont
        
vt = VisualTest()
vt.run()