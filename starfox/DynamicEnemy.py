class DynamicEnemy:
    dynamic_enemy_name = "DynamicEnemy"
    def __init__(self, world, originalEnemy , pos, ctrav , collisionHandler):
        self.gameObject = originalEnemy.copyTo(world)
        self.gameObject.setPos(world, pos )
        ctrav.addCollider( self.gameObject.find("**collision**") , collisionHandler )
        
        self.gameObject.setPythonTag("ObjectController", self)
        self.gameObject.setName(DynamicEnemy.dynamic_enemy_name)
        
    def update(self, world, dt , player):
        pass