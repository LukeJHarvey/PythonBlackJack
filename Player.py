from AbsPlayer import AbsPlayer
class Player(AbsPlayer):
    
    def __init__(self, name, manual, tips=False):
        super().__init__()
        self.name = name
        self.manual = manual #Boolean, is this player controlled by the user
        self.tips = tips #Boolean, if this player is controlled by the user should tips show


    def choice(self):
        if self.manual:
            print("{}'s Current Hand: {}".format(self.name, self.hand_string()))
            option = input("Hit(h) or Stay(s)?: ")
            #self.show_tip()
            if option == "h":
                return True
            else:
                return False
        else: 
            hand_value = self.get_hand_value()
            if min(hand_value) >= 17:
                return False
            else:
                return True

    def show_tip(self):
        print("TIP")
        pass