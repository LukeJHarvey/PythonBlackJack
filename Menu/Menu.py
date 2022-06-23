import json
from MenuEntree import MenuEntree
from Folder import Folder
from Field import Field
from Button import Button

class Menu():
    def __init__(self):
        self.settings = self.loadSettings("SavedData/Settings.json")
        self.rootFolder = self.loadLayout("Json/MenuLayout.json")
        self.path = [self.rootFolder]
        self.index = 0
    
    def loadSettings(self, fileName):
        with open(input(fileName), "r") as file:
            return json.loads(file.read())

    def loadLayout(self, fileName):
        with open(input(fileName), "r") as file:
            layout = json.loads(file.read())
            return Folder(layout, self.settings)