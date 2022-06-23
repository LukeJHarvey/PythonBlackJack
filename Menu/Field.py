from MenuEntree import MenuEntree

class Field(MenuEntree):
    def __init__(self, _fieldData, _settings):
        self.name = _fieldData["Name"]
        self.type = _fieldData["Field"]["Type"]
        self.fieldVar = _fieldData["Field"]["FieldVar"]
        self.choices = _fieldData["Field"]["Choices"] if "Choices" in _fieldData["Field"] else None
        self.notes = _fieldData["Field"]["Notes"] if "Notes" in _fieldData["Field"] else None
        
        self.value = None
        if "settings." in self.fieldVar:
            self.value = _settings[self.fieldVar.split("settings.")[1]]
            if self.choices:
                self.value = self.choices.index(self.value)
        elif "local." in self.fieldVar:
            if self.choices:
                self.value = 0
            elif "Default" in _fieldData["Field"]:
                self.value = _fieldData["Field"]["Default"]

    def __init__(self, _fieldData, _settings, _local):
        self.name = _fieldData["Name"]
        self.type = _fieldData["Field"]["Type"]
        self.fieldVar = _fieldData["Field"]["FieldVar"]
        self.choices = _fieldData["Field"]["Choices"] if "Choices" in _fieldData["Field"] else None
        self.notes = _fieldData["Field"]["Notes"] if "Notes" in _fieldData["Field"] else None
        self.value = None
        if "settings." in self.fieldVar:
            self.value = _settings[self.fieldVar.split("settings.")[1]]
            if self.choices:
                self.value = self.choices.index(self.value)
        elif "local." in self.fieldVar:
            self.value = _local[self.fieldVar.split("local.")[1]]
            if self.choices:
                self.value = self.choices.index(self.value)

    def __init__(self, _name, _type, _fieldVar, _choices = None, _notes = None, _value = None):
        self.name = _name #String
        self.type = _type #String
        self.fieldVar = _fieldVar #String
        self.choices = _choices #Array
        self.notes = _notes #String
        self.value = _value #Index of Choice or type stated in self.type