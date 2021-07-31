from panda3d.core import Vec3


class Bullet:
    
    bullet_name = "bulletC"
    def __init__(self, original, world, origin, cTrav, collisionHandler, fwd, velMag, colMask ):
        self.gameObject = original.copyTo(world)
        self.gameObject.setPos(origin)
        self.velocity = fwd*velMag
        self.gameObject.setPythonTag("ObjectController", self)
        
        cTrav.addCollider(self.gameObject.find("**collision**"), collisionHandler )
        
        self.gameObject.find("**collision**").node().setFromCollideMask(colMask)
        self.gameObject.find("**collision**").node().setIntoCollideMask(colMask)
        
        self.gameObject.setName(Bullet.bullet_name)
    
    def update(self, world, dt ,  cam):
        self.gameObject.setPos(world, self.gameObject.getPos(world) + self.velocity*dt )
        self.gameObject.setHpr(55,0,0)
    def crash(self, other):
        if( type(other) is not Bullet ):
            self.gameObject.removeNode()