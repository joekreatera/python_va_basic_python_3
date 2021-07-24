from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerEvent
from panda3d.core import Point3, Vec3
from panda3d.core import loadPrcFileData
from random import random
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *


# loadPrcFileData('', 'win-size 800 600')
# loadPrcFileData('', 'want-directtools #t')
# loadPrcFileData('', 'want-tk #t')

class Starfox(ShowBase):
    def __init__(self):
        super().__init__(self)
        
        self.taskMgr.add(self.update, "update")
        
    def update(self, evt):
        return Task.cont
        

starfox = Starfox()
starfox.run()