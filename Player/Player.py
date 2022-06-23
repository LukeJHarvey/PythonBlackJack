from AbsPlayer import AbsPlayer
class Player(AbsPlayer):
    
    def __init__(self, name, manual, tips=False, money=1000):
        super().__init__()
        self.name = name
        self.manual = manual #Boolean, is this player controlled by the user
        self.tips = tips #Boolean, if this player is controlled by the user should tips show
        #self.money = money #Int, amount of money player currently has.


    def choice(self):
        if self.manual:
            print("{}'s Current Hand: {}".format(self.name, self.handString()))
            option = input("Hit(h) or Stay(s)?: ")
            #self.showTip()
            if option == "h":
                return True
            else:
                return False
        else: 
            hand_value = self.getHandValue()
            if min(hand_value) >= 17:
                return False
            else:
                return True

    def showTip(self):
        print("TIP")
        pass