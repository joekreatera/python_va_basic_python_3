from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent
from panda3d.core import Point3, Vec3
from panda3d.core import loadPrcFileData
from random import random
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from InputManager import *
from Path import *
from Player import *
from DynamicEnemy import *
# loadPrcFileData('', 'win-size 800 600')
#loadPrcFileData('', 'want-directtools #t')
#loadPrcFileData('', 'want-tk #t')
from panda3d.core import DirectionalLight, AmbientLight, Fog, PointLight
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import AntialiasAttrib

from direct.showbase import Audio3DManager

from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TextNode


loadPrcFileData("","framebuffer-multisample 1")
loadPrcFileData("","multisamples 2")

loadPrcFileData("", "audio-library-name p3fmod_audio")
loadPrcFileData("","fmod-use-surround-sound true")

class Starfox(ShowBase):
    def __init__(self):
        super().__init__(self)
        
        self.scene = self.loader.loadModel("models/world.egg")
        playerTexture = self.loader.loadTexture('models/starfoxShip.jpg')
        enemyTexture = self.loader.loadTexture('models/enemyShip.jpg')
        bulletTexture = loader.loadTexture('models/shot.png')
        base.setBackgroundColor(0.1,0.1, 0.1, 1)
        self.scene.reparentTo(self.render)
        
        self.player = self.scene.find("player")
        self.player.setTexture(playerTexture)
        #self.player.setPos(20,20,20)
        
        self.dynamic_enemy = self.scene.find("enemy1")
        self.dynamic_enemy.setTexture(enemyTexture)
        #self.dynamic_enemy.setPos(6,6,6)
        
        self.building_enemy = self.scene.find("building_enemy")
        #self.building_enemy.setPos(20,20,20)
        
        self.taskMgr.add(self.update, "update")
        
        self.bullet = self.scene.find("bullet")
        self.bullet.setTexture(bulletTexture)
        
        InputManager.initWith(self, 
        [InputManager.arrowUp,
        InputManager.arrowDown,
        InputManager.arrowLeft,
        InputManager.arrowRight,
        InputManager.space,
        InputManager.keyX,
        InputManager.keyV
        ])
        
        base.cTrav = CollisionTraverser()
        self.CollisionHandlerEvent = CollisionHandlerEvent()
        
        self.player.setPythonTag("ObjectController" , Player(self.player, base.cTrav , self.CollisionHandlerEvent) )
        
        self.CollisionHandlerEvent.addInPattern('into-%in')
        self.CollisionHandlerEvent.addInPattern('out-%in')
        
        self.accept('into-collision_player' , self.crash)
        self.accept('into-collision_plane' , self.crash)
        self.accept('into-collision_enemy' , self.crash)
        
        base.cTrav.addCollider( self.scene.find("player/collision**") ,self.CollisionHandlerEvent )
        base.cTrav.addCollider( self.scene.find("basePlane/collision**") ,self.CollisionHandlerEvent )
        
        self.player.find("**collision**").node().setFromCollideMask(0x3)
        self.player.find("**collision**").node().setIntoCollideMask(0x3)
        
        
        
        #base.cTrav.showCollisions(self.render)
        
        self.rails = self.scene.attachNewNode("rails")
        #self.scene.find("basePlane").setPos(self.scene,0,0,-10)
        self.scene.find("basePlane").setHpr(70,0,0)
        self.scene.setPos(self.scene,0,0,0)
        self.player.reparentTo(self.rails)
        self.player.setPos(self.rails, 0,0,0)
        
        self.createStaticEnemy(self.building_enemy,0,50,0)
        self.createStaticEnemy(self.building_enemy,-50,40,0)
        self.createStaticEnemy(self.building_enemy,-100,50,0)
        self.createStaticEnemy(self.building_enemy,-70,130,0)
        self.createStaticEnemy(self.building_enemy,-120,80,0)
        self.createStaticEnemy(self.building_enemy,-220,130,0)
        
        DynamicEnemy( self.scene, self.dynamic_enemy , Vec3(-230,140,10), base.cTrav , self.CollisionHandlerEvent, colMask=0x5);
        DynamicEnemy( self.scene, self.dynamic_enemy , Vec3(-240,160,10), base.cTrav , self.CollisionHandlerEvent, colMask=0x5);


        self.dirLight = DirectionalLight('dir light')
        self.dirLight.color = (0.7,0.7,1,1)
        self.dirPath = self.render.attachNewNode(self.dirLight)
        self.dirPath.setHpr(45,-45,0)
        self.dirLight.setShadowCaster(True, 512,512)
        self.render.setLight(self.dirPath)
                
        self.fog = Fog('fog')
        self.fog.setColor(.1,.1,.1)
        self.fog.setExpDensity(.3)
        self.fog.setLinearRange(50,150)
        self.fog.setLinearFallback(45,160,320)
        self.render.setFog(self.fog)
        
        
        self.render.setShaderAuto()
        self.render.setAntialias(AntialiasAttrib.MAuto)
        
        filters = CommonFilters(base.win, base.cam)
        filters.setBloom(size='large')
        
        self.initUI()
        self.initAudio()
        self.onGame = False


    def initAudio(self):
        self.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0] , self.camera)
        
        self.flyingSound = self.audio3d.loadSfx("./sounds/great fox flying.mp3")
        self.flyingSound.setLoop(True)
        
        self.audio3d.attachSoundToObject(self.flyingSound, self.player)
        self.audio3d.setSoundVelocityAuto(self.flyingSound)
        self.audio3d.setListenerVelocityAuto()
        self.audio3d.setDropOffFactor(0)
        
        self.fireSound = self.audio3d.loadSfx("./sounds/arwing double laser one shot.mp3")
        self.crashSound = self.audio3d.loadSfx("./sounds/break.mp3")

    def initUI(self):
        self.font = loader.loadFont('./fonts/Magenta.ttf')

        self.lifes = [
        OnscreenImage(image='./UI/fox-icon-png-8.png' , pos=(1.10,0,0.8) , scale=0.05),
        OnscreenImage(image='./UI/fox-icon-png-8.png' , pos=(1.20,0,0.8) , scale=0.05)
        ]
        self.lifes[0].setTransparency(True)
        self.lifes[1].setTransparency(True)
        

        self.dialogScreen = DirectDialog(
            frameSize = (-0.7,0.7, -0.7, 0.7),
            relief = DGG.FLAT
        )
        
        self.finishedDialogScreen = DirectDialog(
            frameSize = (-0.7,0.7, -0.7, 0.7),
            relief = DGG.FLAT
        )
        
        s = OnscreenImage(image='./UI/fox-icon-png-8.png' , pos=(0,0,-0.2) , scale=0.20, parent = self.dialogScreen)
        s.setTransparency(True)
        
        self.titleUI = DirectLabel(
        text = "Starlost Region 4",
        parent = self.dialogScreen,
        scale = 0.1,
        pos = (0,0,.2),
        text_font = self.font
        )
        
        self.finishtitleUI = DirectLabel(
        text = "Termin?? la misi??n",
        parent = self.finishedDialogScreen,
        scale = 0.1,
        pos = (0,0,.2),
        text_font = self.font
        )
        
        self.btn = DirectButton(text = "Start", command = self.startGame, pos =(0,0,0), parent = self.dialogScreen, scale=0.07 )
        
        self.finishedDialogScreen.hide()

    def startGame(self):
        self.dialogScreen.hide()
        self.onGame = True
        self.flyingSound.play()

    def createStaticEnemy(self , original, px, py, pz):
        be = original.copyTo(self.scene)
        be.setPos(px,py,pz)
        base.cTrav.addCollider( be.find("**collision**") , self.CollisionHandlerEvent )

    def crash(self, evt):
        
        self.crashSound.play()
        objectInto = evt.getIntoNodePath().node().getParent(0).getPythonTag("ObjectController")
        objectFrom = evt.getFromNodePath().node().getParent(0).getPythonTag("ObjectController")
        
        if( objectInto is not None):
            objectInto.crash(objectFrom)
        
        
    def update(self, evt):
        
        if(self.onGame):
            rails_pos = self.rails.getPos(self.scene)
            new_y = rails_pos.y + globalClock.getDt()*10
            self.rails.setPos( Path.getXOfY(new_y) , new_y, 12 )
            self.rails.setHpr( Path.getHeading(new_y) ,0 ,0 )
            
            #self.camera.lookAt(self.player)
            self.camera.setHpr( Path.getHeading(new_y) ,0 ,0 )
            
            relX, relZ = self.player.getPythonTag("ObjectController").update(self.rails, globalClock.getDt() , self.scene,  self.bullet , self.fireSound)
            self.camera.setPos(self.rails, relX,-30,relZ)
            
            enemies = self.scene.findAllMatches(DynamicEnemy.dynamic_enemy_name)
            for e in enemies:
                e.getPythonTag("ObjectController").update(self.scene, globalClock.getDt() , self.player, self.bullet, self.fireSound)
                
                
            bullets = self.scene.findAllMatches(Bullet.bullet_name)
            for b in bullets:
                b.getPythonTag("ObjectController").update(self.scene, globalClock.getDt() , self.camera )
            
            
            for life in range(0, len(self.lifes) ) :
                self.lifes[life].hide()
            
            for life in range(0,self.player.getPythonTag("ObjectController").lifes) :
                self.lifes[life].show()
                
            if( self.player.getPythonTag("ObjectController").lifes < 0 ):
                self.onGame = False
                self.finishedDialogScreen.show()
                        
        return Task.cont
        

starfox = Starfox()
starfox.run()