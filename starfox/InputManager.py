class InputManager:
    
    arrowUp = 'arrow_up'
    arrowDown = 'arrow_down'
    arrowDown = 'arrow_down'
    arrowDown = 'arrow_down'
    space = 'space'
    keyA= 'a'
    keyS= 's'
    keyD= 'd'
    keyW= 'w'
    keyV= 'v'
    keyX= 'x'
    
    instance = None
    
    @staticmethod
    def initWith(app, key_list):
        InputManager.instance = InputManager()
        
        for k in key_list:
            InputManager.instance.setInput(k, False)
            self.accept(f'raw-{k}' , InputManager.createInputFunction(i, InputManager.instance, True)  )
            self.accept(f'raw-{k}-up' , InputManager.createInputFunction(i, InputManager.instance, False)  )
            
    @staticmethod
    def createInputFunction(key, inputInstance, down):
        def pressKey():
            inputInstance.setInput(key,down)
        return pressKey
        
    @staticmethod
    def getInput(k):
        return InputManager.instance.getInput(k)    
        
    def __init__(self):
        self.input=[]
    
    def setInput(key,state):
        self.input[key] = state
    
    def getInput(key):
        return self.input[key]
        
    def __str__(self):
        res = ""
        for k in self.input.items():
            res += f'\n {k[0 } {k[1]}'
        return res