# world

class World:
    def __init__(self):
        self.orcs = []
        self.elves = []
        self.items = []
        self.trolls = []
    
    def __str__(self):
        orcs_str = ""
        elves_str = ""
        items_str = ""
        trolls_str = ""
        for i in self.orcs:
            orcs_str += str(i)
        
        for i in self.elves:
            elves_str += str(i)
            
        for i in self.items:
            items_str += str(i)
            
        for i in self.trolls:
            trolls_str += str(i)
    
        return f'o:{orcs_str}\ne:{elves_str}\nt:{trolls_str}\ni:{items_str}'
    def day():
        pass
        
w = World()
print(w)
            