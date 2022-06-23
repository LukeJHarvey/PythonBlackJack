from MenuEntree import MenuEntree

class Button(MenuEntree):
    def __init__(self, buttonData):
        self.name = buttonData["Name"]
        self.action = buttonData["Action"]
        
    def __init__(self, _name, _action):
        self.name = _name
        self.action = _action