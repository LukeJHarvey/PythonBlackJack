import json
from MenuEntree import MenuEntree
from Field import Field
from Button import Button

class Folder(MenuEntree):
    def __init__(self, folderData, settings):
        #Load Data
        self.name = folderData["Name"]
        self.entrees = []
        self.options = {}
        self.options["importFile"] = folderData["Options"]["Import"] if "Import" in folderData["Options"] else None
        self.options["exportFile"] = folderData["Options"]["Export"] if "Export" in folderData["Options"] else None
        self.options["format"] = folderData["Options"]["Format"] if "Format" in folderData["Options"] else None
        self.options["importFolders"] = folderData["Options"]["ImportFolders"] if "ImportFolders" in folderData["Options"] else None
        self.buttons = []

        #Create SubFolders and Fields
        if self.options["importFile"] is None and self.options["exportFile"] is None and self.options["format"] is None:
            for entreeData in folderData["Folder"]:
                entree = None
                match entreeData["Type"]:
                    case "Field":
                        entree = Field(entreeData, settings)
                    case "Folder":
                        entree = Folder(entreeData, settings)
                    case "Button":
                        entree = Button(entreeData)
                self.addEntree(entree)

            if "Buttons" in folderData:
                for button in folderData["Buttons"]:
                    entree = Button(button)
                    self.addEntree(entree)
        else:
            if "Buttons" in folderData:
                self.buttons = folderData["Buttons"]
    
    def __init__(self, _name, _options = {}, _buttons = None):
        self.name = _name 
        self.options = _options
        self.entrees = []
        self.buttons = _buttons

    
    def importFolders(self):
        self.entrees = []
        with open(self.options["importFile"], "r") as importFile:
            importData = json.loads(importFile.read())
            with open(self.options["format"], "r") as formatFile:
                formatData = json.loads(formatFile.read())
                for idx, folderData in enumerate(importData[formatData["Location"]]):
                    _name = folderData[formatData["Name"].split("local.")[1]]
                    _options = {
                        "exportFile": self.options["exportFile"],
                        "format": self.options["format"],
                        "importData": True,
                        "importDataIndex": idx
                    }
                    folder = Folder(_name, _options = _options, _buttons = self.buttons)
                    self.addEntree(folder)
        self.addEntree(Button("Back", "Back"))
        return self
    
    def importFieldsAndData(self, settings):
        self.entrees = []
        with open(self.options["exportFile"], "r") as importFile: 
            importData = json.loads(importFile.read())
            with open(self.options["format"], "r") as formatFile:
                formatData = json.loads(formatFile.read())
                for fieldFormat in formatData["Folder"]:
                    local = importData[formatData["Location"]][self.options["importDataIndex"]]
                    field = Field(_fieldData = fieldFormat, _settings = settings, _local = local)
                    self.addEntree(field)
        for button in self.buttons:
            self.addEntree(Button(button["Name"], button["Action"]))
    
    def importFields(self, settings):
        self.entrees = []
        with open(self.options["format"], "r") as formatFile:
            formatData = json.loads(formatFile.read())
            for fieldFormat in formatData["Folder"]:
                field = Field(_fieldData = fieldFormat, _settings = settings)
                self.addEntree(field)
        for button in self.buttons:
            self.addEntree(Button(button["Name"], button["Action"]))



    #Getters and Putters
    def addEntree(self, entree):
        self.entrees.append(entree)

    def getFieldVariables(self):
        ret = {}
        for entree in self.entrees:
            if entree is Field:
                ret[entree.fieldVar] = entree.value
        return ret