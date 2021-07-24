class ENEMY_TYPE (Enum):
    KAMIKAZE = 0
    CHASER = 1
    
class ENEMY_STATE(Enum):
    IDLE = 0
    CHASE = 1
    ATTACK = 2

class DynamicEnemy:
    dynamic_enemy_name = "DynamicEnemy"
    def __init__(self, world, originalEnemy , pos, ctrav , collisionHandler , type = ENEMY_TYPE.KAMIKAZE):
        self.gameObject = originalEnemy.copyTo(world)
        self.gameObject.setPos(world, pos )
        ctrav.addCollider( self.gameObject.find("**collision**") , collisionHandler )
        
        self.gameObject.setPythonTag("ObjectController", self)
        self.gameObject.setName(DynamicEnemy.dynamic_enemy_name)
        
        self.type = type
        self.state = ENEMY_STATE.IDLE
        
    def updateKamikaze(self, world, dt , player):
        diff = player.getPos(world) - self.gameObject.getPos(world)
        distance = diff.length()
        print(distance)
        
        if(self.state == ENEMY_STATE.IDLE and distance <= 80 ):
            self.state = ENEMY_STATE.ATTACK
            self.vel = player.getPos(world) - self.gameObject.getPos(world) 
            self.vel.normalize()
            
        if(self.state == ENEMY_STATE.ATTACK ):
            self.gameObject.setPos( world, self.gameObject.getPos(world) + self.vel*dt*60 )
    
    def update(self, world, dt , player):
        self.gameObject.lookAt(player)
        
        if( self.type == ENEMY_TYPE.KAMIKAZE):
            self.updateKamikaze(world,dt,player)