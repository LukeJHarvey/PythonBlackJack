import json
class CountStrategy:
    def __init__(self, countStrategy): 
        with open("CountStrategies.json", "r") as file:
            data = json.loads(file.read())
            self.blackJackValues = data[countStrategy]
        self.strategy = countStrategy
    
    def get_bj_values(self, value):
        if isinstance(value, str):
            if value in ["10", "J", "Q", "K"]:
                return self.blackJackValues["10"]
            else: 
                return self.blackJackValues[value]
        return self.blackJackValues[str(value)]

    def __str__(self):
        ret = "Strategy: " + self.strategy + "\n"
        loop = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in loop:
            ret += i + ": " + str(self.blackJackValues[i]) + "\n"
        return ret