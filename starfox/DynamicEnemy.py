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
        self.state = ENEMY_TYPE.IDLE
        
    def updateKamikaze(self, world, dt , player):
        pass
    
    def update(self, world, dt , player):
        self.gameObject.lookAt(player)
        if( type == ENEMY_TYPE.KAMIKAZE):
            updateKamikaze(world,dt,player)